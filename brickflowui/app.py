"""
BrickflowUI App class — the main entry point for building apps.

Usage:
    import brickflowui as db

    app = db.App()

    @app.page("/", title="Home", icon="Home")
    def home():
        count, set_count = db.use_state(0)
        return db.Column([
            db.Text("Counter", variant="h2"),
            db.Text(f"Count: {count}"),
            db.Button("Increment", on_click=lambda: set_count(count + 1)),
        ])

    if __name__ == "__main__":
        app.run()
"""

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Union, Tuple

from .auth import (
    AccessLevel,
    AuthProvider,
    AuthMode,
    AuthenticationRequired,
    AuthorizationError,
    Principal,
    authorize_principal,
    current_principal,
)
from .state import RenderContext
from .vdom import VNode
from .theme import Theme
from .version import __version__

logger = logging.getLogger("brickflowui.app")


# ---------------------------------------------------------------------------
# Page descriptor
# ---------------------------------------------------------------------------


@dataclass
class Page:
    path: str
    title: str
    icon: Optional[str]
    render_fn: Callable[[], VNode]
    access: AccessLevel = "public"
    roles: Tuple[str, ...] = ()


@dataclass
class RouteSpec:
    path: str
    methods: List[str]
    handler: Callable
    access: AccessLevel = "public"
    roles: Tuple[str, ...] = ()


# ---------------------------------------------------------------------------
# App class
# ---------------------------------------------------------------------------


class App:
    """
    The main BrickflowUI application.

    - Register pages via the @app.page() decorator or app.mount()
    - Add custom API routes via @app.route()
    - Start the dev/prod server via app.run()
    """

    def __init__(
        self,
        title: str = "BrickflowUI App",
        theme: Union[str, Path, Dict[str, Any], None] = None,
        theme_color: Optional[str] = None,
        logo: Optional[str] = None,
        favicon: Optional[str] = None,
        cors_origins: Optional[List[str]] = None,
        trusted_hosts: Optional[List[str]] = None,
        websocket_origins: Optional[List[str]] = None,
        enable_dev_docs: bool = False,
        auth_mode: AuthMode = "app",
        auth_provider: Optional[AuthProvider] = None,
        app_principal: Optional[Principal] = None,
        allow_anonymous: bool = True,
    ):
        self.title = title
        self.theme = Theme(theme)
        if theme_color:
            self.theme.load({"colors": {"primary": theme_color}})
        if title == "BrickflowUI App":
            self.title = self.theme.branding_value("title", title)
        self.logo = logo or self.theme.branding_value("logo")
        self.favicon = favicon or self.theme.branding_value("favicon")
        self.cors_origins = list(cors_origins or [])
        self.trusted_hosts = list(trusted_hosts or [])
        self.websocket_origins = list(websocket_origins or [])
        self.enable_dev_docs = enable_dev_docs
        self.auth_mode = auth_mode
        self.auth_provider = auth_provider
        self.app_principal = app_principal
        self.allow_anonymous = allow_anonymous

        # page path → Page
        self._pages: Dict[str, Page] = {}
        # session_id → RenderContext
        self._sessions: Dict[str, RenderContext] = {}
        # session_id → current page path
        self._session_paths: Dict[str, str] = {}
        # path → (methods, handler)
        self._custom_routes: Dict[str, RouteSpec] = {}

        # Simple root-mount shortcut (single-page apps)
        self._root_fn: Optional[Callable[[], VNode]] = None

    def _invalidate_server(self) -> None:
        """Drop the cached ASGI app when runtime routes or pages change."""
        if hasattr(self, "_fastapi_app"):
            delattr(self, "_fastapi_app")

    # ── Page registration ────────────────────────────────────────────────

    def page(
        self,
        path: str,
        title: str = "",
        icon: Optional[str] = None,
        access: AccessLevel = "public",
        roles: Optional[List[str]] = None,
    ) -> Callable:
        """Decorator to register a page component."""
        def decorator(fn: Callable[[], VNode]) -> Callable[[], VNode]:
            self._pages[path] = Page(
                path=path,
                title=title or fn.__name__.replace("_", " ").title(),
                icon=icon,
                render_fn=fn,
                access=access,
                roles=tuple(roles or ()),
            )
            # Register "/" as the root if first page
            if not self._root_fn and path == "/":
                self._root_fn = fn
            self._invalidate_server()
            return fn
        return decorator

    def mount(self, component: Callable[[], VNode]) -> None:
        """Mount a single root component (single-page shortcut)."""
        self._root_fn = component
        self._pages["/"] = Page(path="/", title=self.title, icon=None, render_fn=component)
        self._invalidate_server()

    # ── Custom routes ────────────────────────────────────────────────────

    def route(
        self,
        path: str,
        methods: Optional[List[str]] = None,
        access: AccessLevel = "public",
        roles: Optional[List[str]] = None,
    ) -> Callable:
        """Decorator to register a custom API route."""
        if methods is None:
            methods = ["GET"]

        def decorator(fn: Callable) -> Callable:
            self._custom_routes[path] = RouteSpec(
                path=path,
                methods=methods,
                handler=fn,
                access=access,
                roles=tuple(roles or ()),
            )
            self._invalidate_server()
            return fn
        return decorator

    # ── Rendering ────────────────────────────────────────────────────────

    def _render(self, session_id: str) -> VNode:
        """Render the current page for a session."""
        ctx = self._sessions.get(session_id)
        if ctx is None:
            raise RuntimeError(f"No session context for {session_id}")

        path = self._session_paths.get(session_id, "/")
        page = self._pages.get(path)

        if page is None and self._root_fn is not None:
            # Fallback: use root fn
            return self._root_fn()

        if page is None:
            from .components import Column, Text, Alert
            return Column([
                Text("404 – Page Not Found", variant="h2"),
                Alert(f"No page registered for path: {path}", type="error"),
            ])

        try:
            authorize_principal(current_principal(), access=page.access, roles=page.roles)
        except (AuthenticationRequired, AuthorizationError) as exc:
            return self._render_access_denied(exc)

        # Wrap with app shell if multiple pages
        if len(self._pages) > 1:
            return self._render_with_shell(session_id, page)

        return page.render_fn()

    def _render_access_denied(self, exc: Exception) -> VNode:
        from .components import Alert, Column, Text

        title = "Sign In Required" if isinstance(exc, AuthenticationRequired) else "Access Denied"
        return Column(
            [
                Text(title, variant="h2"),
                Alert(str(exc), type="error"),
            ],
            padding=6,
            gap=4,
        )

    def _render_with_shell(self, session_id: str, current_page: Page) -> VNode:
        """Wrap page content in the app shell (sidebar + topbar)."""
        from .components import Column, Row, Sidebar, NavItem, Text, Divider

        nav_items = [
            NavItem(label=p.title, path=p.path, icon=p.icon)
            for p in self._pages.values()
        ]

        return Row(
            children=[
                Sidebar(
                    items=nav_items,
                    brand_name=self.title,
                    logo=self.logo,
                ),
                Column(
                    children=[current_page.render_fn()],
                    padding=6,
                    style={"flex": "1", "minHeight": "100vh", "overflowY": "auto"},
                ),
            ],
            gap=0,
            align="stretch",
            style={"minHeight": "100vh", "width": "100%"},
        )

    def _navigate(self, session_id: str, path: str) -> None:
        """Handle page navigation for a session."""
        self._session_paths[session_id] = path
        ctx = self._sessions.get(session_id)
        if ctx:
            # Reset state on navigation (new page = new component tree)
            ctx.cleanup_effects()
            ctx.state_slots = []
            ctx.memo_slots = []
            ctx.mark_dirty()

    # ── Server ────────────────────────────────────────────────────────────

    @property
    def server(self):
        """
        Access the underlying FastAPI app to register custom routes.
        Lazy-init so users can add routes before calling run().
        """
        if not hasattr(self, "_fastapi_app"):
            from .server import create_asgi_app
            self._fastapi_app = create_asgi_app(self)
        return self._fastapi_app

    def run(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        reload: bool = False,
    ) -> None:
        """Start the BrickflowUI server."""
        from .databricks.env import resolve_host_port
        from .server import run_server

        host, port = resolve_host_port(host, port)
        logger.info(f"BrickflowUI v{__version__} — starting on http://{host}:{port}")
        logger.info(f"Pages: {list(self._pages.keys())}")

        if not self._pages and self._root_fn is None:
            raise RuntimeError("No pages or root component registered. Use @app.page() or app.mount().")

        run_server(self, host=host, port=port, reload=reload)
