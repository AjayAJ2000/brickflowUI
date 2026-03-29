"""
ASGI server for BrickflowUI.

Creates a FastAPI app that:
- Serves the pre-built React frontend at GET /
- Manages WebSocket sessions at WS /events
- Dispatches events to Python handlers and sends re-renders back
"""

from __future__ import annotations

import asyncio
import inspect
import json
import logging
import uuid
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Optional
from urllib.parse import urlparse

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from .auth import (
    AuthenticationRequired,
    AuthorizationError,
    authorize_principal,
    reset_current_principal,
    resolve_principal,
    set_current_principal,
)
from .state import RenderContext, set_render_context
from .vdom import VNode, diff

if TYPE_CHECKING:
    from .app import App

logger = logging.getLogger("brickflowui.server")

# Path to bundled frontend
_FRONTEND_DIST = Path(__file__).parent / "frontend" / "dist"


# ---------------------------------------------------------------------------
# Serialisation helpers
# ---------------------------------------------------------------------------


def _full_tree_msg(vnode: VNode, handler_registry: dict) -> str:
    """Build full-tree WebSocket message."""
    return json.dumps({
        "type": "full",
        "tree": vnode.serialize(handler_registry),
    })


def _patch_msg(patches: list) -> str:
    """Build patch WebSocket message."""
    return json.dumps({"type": "patch", "patches": patches})


def _error_msg(message: str) -> str:
    return json.dumps({"type": "error", "message": message})


def _consume_task_exception(task: asyncio.Task) -> None:
    """Prevent noisy unretrieved-task warnings during websocket disconnect races."""
    try:
        task.exception()
    except (asyncio.CancelledError, RuntimeError):
        pass


def _origin_allowed(origin: Optional[str], host: Optional[str], allowed_origins: list[str]) -> bool:
    """Allow same-origin browser sessions by default, plus any explicitly configured origins."""
    if not origin:
        return True

    if "*" in allowed_origins:
        return True

    parsed_origin = urlparse(origin)
    if not parsed_origin.scheme or not parsed_origin.netloc:
        return False

    if host and parsed_origin.netloc == host:
        return True

    normalized_allowed = {value.rstrip("/") for value in allowed_origins}
    return origin.rstrip("/") in normalized_allowed


def _extract_event_payload(event_data: object) -> object:
    """Unwrap common frontend payload shapes into the value Python handlers expect."""
    if not isinstance(event_data, dict):
        return event_data

    if len(event_data) == 1:
        return next(iter(event_data.values()))

    return event_data


# ---------------------------------------------------------------------------
# ASGI app factory
# ---------------------------------------------------------------------------


def create_asgi_app(dbrx_app: "App") -> FastAPI:
    """Create and return the FastAPI ASGI application."""
    docs_url = "/docs" if dbrx_app.enable_dev_docs else None
    openapi_url = "/openapi.json" if dbrx_app.enable_dev_docs else None
    fastapi_app = FastAPI(
        title="BrickflowUI App",
        docs_url=docs_url,
        redoc_url=None,
        openapi_url=openapi_url,
    )

    if dbrx_app.cors_origins:
        fastapi_app.add_middleware(
            CORSMiddleware,
            allow_origins=dbrx_app.cors_origins,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    if dbrx_app.trusted_hosts:
        fastapi_app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=dbrx_app.trusted_hosts,
        )

    @fastapi_app.middleware("http")
    async def add_security_headers(request, call_next):
        try:
            principal = resolve_principal(
                auth_mode=dbrx_app.auth_mode,
                auth_provider=dbrx_app.auth_provider,
                app_principal=dbrx_app.app_principal,
                allow_anonymous=dbrx_app.allow_anonymous,
                source=request,
            )
        except AuthenticationRequired as exc:
            if request.url.path == "api" or request.url.path.startswith("/api/"):
                return JSONResponse({"detail": str(exc)}, status_code=401)
            raise
        request.state.brickflow_principal = principal
        token = set_current_principal(principal)
        try:
            response = await call_next(request)
        finally:
            reset_current_principal(token)
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; connect-src 'self' ws: wss:; img-src 'self' data: https:; "
            "style-src 'self' 'unsafe-inline'; script-src 'self'; font-src 'self' data: https:; "
            "frame-ancestors 'self';",
        )
        return response

    # ── Static frontend assets ──────────────────────────────────────────────
    _assets_dir = _FRONTEND_DIST / "assets"
    if _assets_dir.exists():
        fastapi_app.mount(
            "/assets",
            StaticFiles(directory=str(_assets_dir)),
            name="assets",
        )

    # ── Custom API Routes ──────────────────────────────────────────────────
    _mount_custom_routes(fastapi_app, dbrx_app)

    # ── WebSocket session handler (MUST come before catch-all GET) ──────────
    @fastapi_app.websocket("/events")
    async def events(ws: WebSocket):
        if not _origin_allowed(
            ws.headers.get("origin"),
            ws.headers.get("host"),
            dbrx_app.websocket_origins,
        ):
            await ws.close(code=1008)
            return

        principal = resolve_principal(
            auth_mode=dbrx_app.auth_mode,
            auth_provider=dbrx_app.auth_provider,
            app_principal=dbrx_app.app_principal,
            allow_anonymous=dbrx_app.allow_anonymous,
            source=ws,
        )

        await ws.accept()

        session_id = str(uuid.uuid4())
        logger.info(f"[{session_id}] WebSocket connected")

        # Create a fresh render context for this session
        ctx = RenderContext(
            session_id=session_id,
            rerender_event=asyncio.Event(),
        )
        dbrx_app._sessions[session_id] = ctx
        dbrx_app._session_paths[session_id] = ws.query_params.get("path") or "/"
        ctx.context["principal"] = principal

        # Per-session event handler registry (event_id → callable)
        handler_registry: Dict[str, callable] = {}

        # ── Helper: render + send full tree ───────────────────────────────
        async def send_full_tree():
            nonlocal handler_registry
            handler_registry = {}  # refresh on each full render
            render_token = set_render_context(ctx)
            principal_token = set_current_principal(principal)
            try:
                ctx.reset_indices()
                vnode: VNode = dbrx_app._render(session_id)
                ctx.run_effects()
                ctx.dirty = False
                msg = _full_tree_msg(vnode, handler_registry)
                await ws.send_text(msg)
                return vnode
            except Exception as exc:
                logger.exception(f"[{session_id}] Render error")
                await ws.send_text(_error_msg(str(exc)))
                return None
            finally:
                set_render_context(None)
                reset_current_principal(principal_token)

        # ── Helper: re-render + send patch ────────────────────────────────
        async def send_patch(old_tree: Optional[VNode]):
            nonlocal handler_registry
            new_handler_registry: Dict[str, callable] = {}
            render_token = set_render_context(ctx)
            principal_token = set_current_principal(principal)
            try:
                ctx.reset_indices()
                new_tree: VNode = dbrx_app._render(session_id)
                ctx.run_effects()
                ctx.dirty = False
                patches = diff(old_tree, new_tree, new_handler_registry)
                handler_registry = new_handler_registry
                if patches:
                    await ws.send_text(_patch_msg(patches))
                return new_tree
            except Exception as exc:
                logger.exception(f"[{session_id}] Re-render error")
                await ws.send_text(_error_msg(str(exc)))
                return old_tree
            finally:
                set_render_context(None)
                reset_current_principal(principal_token)

        current_tree = await send_full_tree()

        # ── Event/rerender loop ────────────────────────────────────────────
        try:
            while True:
                # Wait for either an incoming WS message or a dirty flag
                receive_task = asyncio.ensure_future(ws.receive_text())
                rerender_task = asyncio.ensure_future(ctx.rerender_event.wait())
                receive_task.add_done_callback(_consume_task_exception)
                rerender_task.add_done_callback(_consume_task_exception)

                done, pending = await asyncio.wait(
                    [receive_task, rerender_task],
                    return_when=asyncio.FIRST_COMPLETED,
                )

                for task in pending:
                    task.cancel()
                if pending:
                    await asyncio.gather(*pending, return_exceptions=True)

                if receive_task in done:
                    # Handle incoming event from frontend
                    try:
                        raw = receive_task.result()
                        msg_data = json.loads(raw)
                    except RuntimeError as exc:
                        if "disconnect message" in str(exc).lower():
                            raise WebSocketDisconnect(code=1000) from exc
                        raise
                    except Exception:
                        continue

                    if msg_data.get("type") == "event":
                        event_id = msg_data.get("event_id")
                        event_data = msg_data.get("data", {})
                        handler = handler_registry.get(event_id)
                        if handler is not None:
                            try:
                                payload = _extract_event_payload(event_data)
                                principal_token = set_current_principal(principal)
                                sig = inspect.signature(handler)
                                if not sig.parameters:
                                    result = handler()
                                elif isinstance(payload, dict) and len(sig.parameters) > 1:
                                    result = handler(**payload)
                                else:
                                    result = handler(payload)

                                if inspect.isawaitable(result):
                                    await result
                            except Exception as exc:
                                logger.exception(f"[{session_id}] Handler error for {event_id}")
                                await ws.send_text(_error_msg(str(exc)))
                            finally:
                                reset_current_principal(principal_token)

                    elif msg_data.get("type") == "navigate":
                        path = msg_data.get("path", "/")
                        dbrx_app._navigate(session_id, path)

                if rerender_task in done:
                    ctx.rerender_event.clear()

                # If any state change occurred, re-render
                if ctx.dirty:
                    current_tree = await send_patch(current_tree)

        except WebSocketDisconnect:
            logger.info(f"[{session_id}] WebSocket disconnected")
        except asyncio.CancelledError:
            pass
        finally:
            ctx.cleanup_effects()
            dbrx_app._sessions.pop(session_id, None)
            dbrx_app._session_paths.pop(session_id, None)

    # ── HTML shell (MUST come last as a catch-all) ─────────────────────────
    @fastapi_app.get("/{full_path:path}", include_in_schema=False)
    async def spa_shell(full_path: str):
        """Serve the SPA shell for all non-API, non-WS routes."""
        if full_path == "api" or full_path.startswith("api/"):
            raise HTTPException(status_code=404, detail="Not found")

        theme_css = dbrx_app.theme.to_css_variables()
        style_block = f"<style id=\"bf-theme-vars\">{theme_css}</style>"
        favicon_block = (
            f'<link rel="icon" href="{dbrx_app.favicon}" />'
            if dbrx_app.favicon
            else ""
        )
        head_injections = f"{style_block}\n{favicon_block}" if favicon_block else style_block
        
        index_path = _FRONTEND_DIST / "index.html"
        if index_path.exists():
            html = index_path.read_text(encoding="utf-8")
            html = html.replace("<title>BrickflowUI App</title>", f"<title>{dbrx_app.title}</title>")
            if "</head>" in html:
                html = html.replace("</head>", f"{head_injections}\n</head>")
            else:
                html = f"{head_injections}\n{html}"
            return HTMLResponse(html)
            
        return HTMLResponse(_minimal_html_shell(head_injections, dbrx_app.title))

    return fastapi_app


# ---------------------------------------------------------------------------
# Server runner
# ---------------------------------------------------------------------------


def run_server(dbrx_app: "App", host: str, port: int, reload: bool = False):
    logger.info(f"Starting BrickflowUI server on http://{host}:{port}")
    asgi_app = create_asgi_app(dbrx_app)

    uvicorn.run(
        asgi_app,
        host=host,
        port=port,
        log_level="info",
        reload=reload,
    )


def _mount_custom_routes(fastapi_app: FastAPI, dbrx_app: "App"):
    """Mount any routes registered via @app.route(...)."""
    async def _guard(request: Request):
        spec = dbrx_app._custom_routes.get(request.url.path)
        principal = getattr(request.state, "brickflow_principal", None)
        if spec is None or principal is None:
            return
        try:
            authorize_principal(principal, access=spec.access, roles=spec.roles)
        except AuthenticationRequired as exc:
            raise HTTPException(status_code=401, detail=str(exc)) from exc
        except AuthorizationError as exc:
            raise HTTPException(status_code=403, detail=str(exc)) from exc

    for path, spec in dbrx_app._custom_routes.items():
        fastapi_app.add_api_route(
            path,
            spec.handler,
            methods=spec.methods,
            dependencies=[] if spec.access == "public" and not spec.roles else [Depends(_guard)],
        )


# ---------------------------------------------------------------------------
# Fallback HTML shell (used when frontend/dist doesn't exist yet)
# ---------------------------------------------------------------------------


def _minimal_html_shell(style_block: str = "", title: str = "BrickflowUI App") -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>__APP_TITLE__</title>
  __STYLE_BLOCK__
  <style>
    :root {{
      --db-bg: #0d1117;
      --db-surface: #161b22;
      --db-border: #30363d;
      --db-text: #e6edf3;
      --db-text-muted: #8b949e;
      --db-primary: #FF3621;
      --db-primary-hover: #e02d1a;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--db-bg);
      color: var(--db-text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    #root {{ flex: 1; display: flex; flex-direction: column; width: 100%; }}
    
    /* Layout components fallback styles */
    column, .column {{ display: flex; flex-direction: column; }}
    row, .row {{ display: flex; flex-direction: row; }}
    
    .loading-screen {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      flex: 1;
      gap: 16px;
    }}
    .spinner {{
      width: 40px; height: 40px;
      border: 3px solid var(--db-border);
      border-top-color: var(--db-primary);
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }}
    @keyframes spin {{
      to {{ transform: rotate(360deg); }}
    }}
    .loading-brand {{ font-size: 24px; font-weight: 600; color: var(--db-primary); }}
    .loading-hint {{ font-size: 14px; color: var(--db-text-muted); }}
  </style>
</head>
<body>
  <div id="root">
    <div class="loading-screen">
      <div class="spinner"></div>
      <div class="loading-brand">BrickflowUI</div>
      <div class="loading-hint">Connecting to runtime...</div>
    </div>
  </div>
  <script>
    const WS_URL = (location.protocol === 'https:' ? 'wss' : 'ws') + '://' + location.host + '/events';
    let ws;
    let tree = null;

    function connect() {{
      ws = new WebSocket(WS_URL);
      ws.onopen = () => {{ document.title = "BrickflowUI - Connected"; }};
      ws.onmessage = (e) => {{
        const msg = JSON.parse(e.data);
        if (msg.type === 'full') {{
          tree = msg.tree;
          render(tree);
        }} else if (msg.type === 'patch') {{
          // Simplistic patch application (full re-render for now in fallback)
          tree = applyPatches(tree, msg.patches);
          render(tree);
        }} else if (msg.type === 'error') {{
          console.error(msg.message);
        }}
      }};
      ws.onclose = () => {{
        document.title = "BrickflowUI - Disconnected";
        setTimeout(connect, 2000);
      }};
    }}

    function render(node) {{
      const root = document.getElementById('root');
      root.innerHTML = '';
      if (node) root.appendChild(createEl(node));
    }}

    function createEl(node) {{
      if (!node) return document.createTextNode('');
      if (typeof node === 'string') return document.createTextNode(node);
      
      const type = node.type.toLowerCase().split('.').pop();
      // Map components to standard HTML where obvious
      const tagMap = {{ 'column': 'div', 'row': 'div', 'text': 'div', 'button': 'button', 'input': 'input', 'card': 'div' }};
      const el = document.createElement(tagMap[type] || 'div');
      if (tagMap[type]) el.classList.add(type);
      
      if (node.props) {{
        Object.entries(node.props).forEach(([k, v]) => {{
          if (k === 'style' && typeof v === 'object') {{
             Object.assign(el.style, v);
          }} else if (k === 'className') {{
             el.className += ' ' + v;
          }} else if (k.startsWith('on')) {{
             el.addEventListener(k.toLowerCase().slice(2), () => {{
                ws.send(JSON.stringify({{ type: 'event', event_id: v }}));
             }});
          }} else {{
             if (v !== null && v !== undefined) el.setAttribute(k, v);
          }}
        }});
      }}
      if (node.children) {{
        node.children.forEach(child => el.appendChild(createEl(child)));
      }}
      return el;
    }}

    function applyPatches(oldTree, patches) {{
      // In a real VDOM this is complex. For fallback, we just return the new tree 
      // if the patch contains the whole thing, or do nothing.
      // But our backend sends full patches. For now, let's just hope for the best 
      // or implement a minimal patch applier.
      // Since 'patch' msg in server.py sends a list of diffs, 
      // and our fallback render cleared root, we might need a better way.
      // ACTUALLY, server.py send_patch sends 'type': 'patch', 'patches': diffs
      return oldTree; // Fallback doesn't support complex patching yet
    }

    connect();
  </script>
</body>
</html>
""".replace("__STYLE_BLOCK__", style_block).replace("__APP_TITLE__", title)
