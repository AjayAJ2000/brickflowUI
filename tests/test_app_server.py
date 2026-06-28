import pytest
from fastapi.testclient import TestClient
import brickflowui as db
import brickflowui.server as server
from brickflowui.app import App
from brickflowui.auth import HeaderAuthProvider, current_user
from brickflowui.server import _missing_frontend_shell, create_asgi_app
from brickflowui.vdom import VNode
from pathlib import Path


def _find_node_by_type(node: dict, node_type: str) -> dict | None:
    if node.get("type") == node_type:
        return node
    for child in node.get("children", []):
        found = _find_node_by_type(child, node_type)
        if found:
            return found
    for value in node.get("props", {}).values():
        if isinstance(value, dict):
            found = _find_node_by_type(value, node_type)
            if found:
                return found
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    found = _find_node_by_type(item, node_type)
                    if found:
                        return found
    return None


def test_app_page_registration():
    app = App(title="Test App")
    
    @app.page("/", title="Home")
    def home():
        return VNode(type="div")
        
    assert "/" in app._pages
    assert app._pages["/"].title == "Home"
    assert app._root_fn == home

    @app.page("/other")
    def other():
        return VNode(type="span")
    
    assert "/other" in app._pages
    # _root_fn should still be home as it was registered first at "/"
    assert app._root_fn == home
 # First page at "/" or first page generally? 
    # Actually code says: if not self._root_fn and path == "/": self._root_fn = fn
    # So if I didn't register "/", it won't be root_fn yet.

def test_app_render_basic():
    app = App()
    @app.page("/")
    def home():
        return VNode(type="div", props={"id": "root-node"})
    
    # Simulate a session
    from brickflowui.state import RenderContext
    session_id = "sess-1"
    app._sessions[session_id] = RenderContext(session_id=session_id)
    app._session_paths[session_id] = "/"
    
    vnode = app._render(session_id)
    assert vnode.type == "div"
    assert vnode.props["id"] == "root-node"

def test_server_spa_shell():
    app = App()
    app.mount(lambda: VNode(type="div"))
    asgi = create_asgi_app(app)
    client = TestClient(asgi)
    
    response = client.get("/")
    assert response.status_code == 200
    assert "BrickflowUI App" in response.text


def test_shell_bootstrap_and_local_asset_route():
    asset = Path("docs/assets/brickflowui-mark.svg").resolve()

    app = App(
        title="Asset App",
        favicon=str(asset),
        loading={
            "asset": str(asset),
            "message": "Booting secure workspace",
            "animation": "pulse",
        },
    )
    app.mount(lambda: VNode(type="div"))
    client = TestClient(create_asgi_app(app))

    response = client.get("/")
    assert response.status_code == 200
    assert "__BRICKFLOW_BOOTSTRAP__" in response.text
    assert "Booting secure workspace" in response.text
    assert "/__brickflow_asset__/" in response.text

    asset_url = app.asset_url(str(asset))
    asset_response = client.get(asset_url)
    assert asset_response.status_code == 200
    assert b"<svg" in asset_response.content


def test_shell_bootstrap_includes_theme_mode_and_subtitle():
    app = App(
        title="Acme Analytics",
        theme={"branding": {"tagline": "React components. Python syntax."}},
        loading={"subtitle": "Querying warehouse metadata"},
    )
    app.mount(lambda: VNode(type="div"))
    client = TestClient(create_asgi_app(app))

    response = client.get("/")

    assert response.status_code == 200
    assert "Querying warehouse metadata" in response.text
    assert "\"themeMode\": \"light\"" in response.text


def test_shell_bootstrap_includes_style_preset_and_loading_modes():
    asset = Path("docs/assets/brickflowui-mark.svg").resolve()
    app = App(
        theme={"style_preset": "bento"},
        loading={
            "light": {"asset": str(asset), "message": "Loading light workspace"},
            "dark": {"message": "Loading dark workspace", "animation": "pulse"},
        },
    )
    app.mount(lambda: VNode(type="div"))
    client = TestClient(create_asgi_app(app))

    response = client.get("/")

    assert response.status_code == 200
    assert "\"stylePreset\": \"bento\"" in response.text
    assert "Loading light workspace" in response.text
    assert "Loading dark workspace" in response.text
    assert "/__brickflow_asset__/" in response.text


def test_missing_frontend_shell_is_static_and_actionable():
    shell = _missing_frontend_shell("", "Fallback App")

    assert "BrickflowUI frontend bundle is missing" in shell
    assert "npm ci" in shell
    assert "new WebSocket" not in shell


def test_shell_escapes_title_and_favicon_html():
    app = App(title='</title><img src=x>', favicon='" onload="alert(1)')
    app.mount(lambda: VNode(type="div"))

    response = TestClient(create_asgi_app(app)).get("/")

    assert response.status_code == 200
    assert "<title>&lt;/title&gt;&lt;img src=x&gt;</title>" in response.text
    assert '<link rel="icon" href="&quot; onload=&quot;alert(1)" />' in response.text


def test_shell_contains_theme_and_bootstrap_values_as_data():
    app = App(
        theme={"colors": {"primary": "</style><img src=theme>"}},
        loading={"message": "</script><img src=bootstrap>"},
    )
    app.mount(lambda: VNode(type="div"))

    response = TestClient(create_asgi_app(app)).get("/")

    assert response.status_code == 200
    assert "</style><img src=theme>" not in response.text
    assert "</script><img src=bootstrap>" not in response.text
    assert 'type="application/json"' in response.text


def test_missing_frontend_bundle_returns_diagnostic(monkeypatch):
    monkeypatch.setattr(server, "_FRONTEND_DIST", Path("missing-frontend-dist"))
    app = App()
    app.mount(lambda: VNode(type="div"))

    response = TestClient(create_asgi_app(app)).get("/")

    assert response.status_code == 503
    assert "frontend bundle is missing" in response.text.lower()
    assert "new WebSocket" not in response.text


def test_custom_api_route():
    app = App()
    
    @app.route("/api/health")
    async def health():
        return {"status": "ok"}
        
    asgi = create_asgi_app(app)
    client = TestClient(asgi)
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_custom_route_registered_after_server_access_is_available():
    app = App()
    _ = app.server

    @app.route("/api/late")
    async def late():
        return {"status": "late"}

    client = TestClient(app.server)
    response = client.get("/api/late")
    assert response.status_code == 200
    assert response.json() == {"status": "late"}

def test_unknown_api_path_returns_404():
    app = App()
    app.mount(lambda: VNode(type="div"))
    client = TestClient(create_asgi_app(app))

    response = client.get("/api/missing")
    assert response.status_code == 404

def test_security_headers_present_on_shell():
    app = App()
    app.mount(lambda: VNode(type="div"))
    client = TestClient(create_asgi_app(app))

    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["x-content-type-options"] == "nosniff"
    assert response.headers["x-frame-options"] == "SAMEORIGIN"


def test_safe_requests_receive_csrf_cookie_by_default():
    app = App()
    app.mount(lambda: VNode(type="div"))
    client = TestClient(create_asgi_app(app))

    response = client.get("/")

    assert response.status_code == 200
    assert "brickflowui_csrf" in response.cookies


def test_unsafe_browser_requests_require_valid_csrf_token():
    app = App()

    @app.route("/api/submit", methods=["POST"])
    async def submit():
        return {"status": "ok"}

    client = TestClient(create_asgi_app(app))
    seed = client.get("/")
    csrf = seed.cookies.get("brickflowui_csrf")
    assert csrf

    denied = client.post("/api/submit", json={"name": "blocked"}, headers={"origin": "http://testserver"})
    assert denied.status_code == 403

    allowed = client.post(
        "/api/submit",
        json={"name": "allowed"},
        headers={"origin": "http://testserver", "x-brickflow-csrf": csrf},
    )
    assert allowed.status_code == 200
    assert allowed.json() == {"status": "ok"}

def test_protected_route_requires_authenticated_user():
    app = App(auth_mode="user", auth_provider=HeaderAuthProvider())

    @app.route("/api/secure", methods=["GET"], access="user")
    async def secure():
        return {"status": "ok"}

    client = TestClient(create_asgi_app(app))

    denied = client.get("/api/secure")
    assert denied.status_code == 401

    allowed = client.get("/api/secure", headers={"x-brickflow-user-id": "alice"})
    assert allowed.status_code == 200
    assert allowed.json() == {"status": "ok"}

def test_websocket_page_uses_authenticated_user_context():
    app = App(auth_mode="user", auth_provider=HeaderAuthProvider())

    @app.page("/", access="user")
    def home():
        user = current_user()
        return VNode(type="Text", props={"value": user.subject if user else "missing", "variant": "body"})

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events", headers={"x-brickflow-user-id": "alice"}) as websocket:
        payload = websocket.receive_json()

    assert payload["type"] == "full"
    assert payload["tree"]["props"]["value"] == "alice"

def test_websocket_page_renders_access_denied_without_user():
    app = App(auth_mode="user", auth_provider=HeaderAuthProvider())

    @app.page("/", access="user")
    def home():
        return VNode(type="div")

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        payload = websocket.receive_json()

    assert payload["type"] == "full"
    assert payload["tree"]["type"] == "Column"


def test_shell_sidebar_hides_pages_user_cannot_access():
    app = App(auth_mode="user", auth_provider=HeaderAuthProvider())

    @app.page("/", title="Overview")
    def overview():
        return db.Text("Overview")

    @app.page("/admin", title="Admin", access="user", roles=["admin"])
    def admin():
        return db.Text("Admin")

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events", headers={"x-brickflow-user-id": "alice", "x-brickflow-user-roles": "viewer"}) as websocket:
        payload = websocket.receive_json()

    sidebar = _find_node_by_type(payload["tree"], "Sidebar")
    assert sidebar is not None
    labels = [child["props"]["label"] for child in sidebar["children"]]
    assert "Overview" in labels
    assert "Admin" not in labels

def test_extract_event_payload_unwraps_single_value():
    from brickflowui.server import _extract_event_payload

    assert _extract_event_payload({"value": "abc"}) == "abc"
    assert _extract_event_payload({"row": {"id": 1}}) == {"id": 1}
    assert _extract_event_payload({"value": ["bronze", "silver"]}) == ["bronze", "silver"]
    assert _extract_event_payload({"value": {"start": "2026-04-01", "end": "2026-04-07"}}) == {"start": "2026-04-01", "end": "2026-04-07"}
    assert _extract_event_payload({"a": 1, "b": 2}) == {"a": 1, "b": 2}


def test_multiselect_event_payload_updates_state_and_rerenders():
    app = App()

    @app.page("/")
    def home():
        values, set_values = db.use_state([])
        return db.Column(
            [
                db.Text(",".join(values) if values else "none"),
                db.MultiSelect(
                    name="layers",
                    label="Layers",
                    options=[
                        {"label": "Bronze", "value": "bronze"},
                        {"label": "Silver", "value": "silver"},
                    ],
                    values=values,
                    on_change=set_values,
                ),
            ]
        )

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        full = websocket.receive_json()
        control = _find_node_by_type(full["tree"], "MultiSelect")
        assert control is not None

        websocket.send_json(
            {
                "type": "event",
                "event_id": control["props"]["change"],
                "data": {"value": ["bronze", "silver"]},
            }
        )
        patch = websocket.receive_json()

    assert patch["type"] == "patch"
    text_patch = next(item for item in patch["patches"] if item["path"] == [0])
    assert text_patch["props"]["value"] == "bronze,silver"


def test_date_range_event_payload_updates_state_and_rerenders():
    app = App()

    @app.page("/")
    def home():
        selected, set_selected = db.use_state({"start": "", "end": ""})
        return db.Column(
            [
                db.Text(f"{selected['start']}->{selected['end']}"),
                db.DateRangePicker(
                    name="window",
                    label="Window",
                    start=selected["start"],
                    end=selected["end"],
                    on_change=set_selected,
                ),
            ]
        )

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        full = websocket.receive_json()
        control = _find_node_by_type(full["tree"], "DateRangePicker")
        assert control is not None

        websocket.send_json(
            {
                "type": "event",
                "event_id": control["props"]["change"],
                "data": {"value": {"start": "2026-04-01", "end": "2026-04-07"}},
            }
        )
        patch = websocket.receive_json()

    assert patch["type"] == "patch"
    text_patch = next(item for item in patch["patches"] if item["path"] == [0])
    assert text_patch["props"]["value"] == "2026-04-01->2026-04-07"


def test_chat_input_submit_payload_updates_state_and_rerenders():
    app = App()

    @app.page("/")
    def home():
        message, set_message = db.use_state("empty")
        return db.Column(
            [
                db.Text(message),
                db.ChatInput(on_submit=set_message),
            ]
        )

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        full = websocket.receive_json()
        control = _find_node_by_type(full["tree"], "ChatInput")
        assert control is not None

        websocket.send_json(
            {
                "type": "event",
                "event_id": control["props"]["submit"],
                "data": {"value": "show failed pipelines"},
            }
        )
        patch = websocket.receive_json()

    assert patch["type"] == "patch"
    text_patch = next(item for item in patch["patches"] if item["path"] == [0])
    assert text_patch["props"]["value"] == "show failed pipelines"


def test_checkbox_false_payload_updates_state_and_rerenders():
    app = App()

    @app.page("/")
    def home():
        enabled, set_enabled = db.use_state(True)
        return db.Column(
            [
                db.Text("enabled" if enabled else "disabled"),
                db.Checkbox(name="enabled", label="Enabled", checked=enabled, on_change=set_enabled),
            ]
        )

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        full = websocket.receive_json()
        control = _find_node_by_type(full["tree"], "Checkbox")
        assert control is not None

        websocket.send_json(
            {
                "type": "event",
                "event_id": control["props"]["change"],
                "data": {"value": False},
            }
        )
        patch = websocket.receive_json()

    assert patch["type"] == "patch"
    text_patch = next(item for item in patch["patches"] if item["path"] == [0])
    checkbox_patch = next(item for item in patch["patches"] if item["path"] == [1])
    assert text_patch["props"]["value"] == "disabled"
    assert checkbox_patch["props"]["checked"] is False


def test_input_empty_string_payload_updates_state_and_rerenders():
    app = App()

    @app.page("/")
    def home():
        query, set_query = db.use_state("seed")
        return db.Column(
            [
                db.Text(query or "empty"),
                db.Input(name="query", label="Query", value=query, on_change=set_query),
            ]
        )

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        full = websocket.receive_json()
        control = _find_node_by_type(full["tree"], "Input")
        assert control is not None

        websocket.send_json(
            {
                "type": "event",
                "event_id": control["props"]["change"],
                "data": {"value": ""},
            }
        )
        patch = websocket.receive_json()

    assert patch["type"] == "patch"
    text_patch = next(item for item in patch["patches"] if item["path"] == [0])
    input_patch = next(item for item in patch["patches"] if item["path"] == [1])
    assert text_patch["props"]["value"] == "empty"
    assert input_patch["props"]["value"] == ""


def test_websocket_serializes_local_media_paths_as_asset_urls():
    image_asset = Path("docs/assets/brickflowui-mark.svg").resolve()
    video_asset = Path("README.md").resolve()

    app = App()

    @app.page("/")
    def home():
        return db.Column(
            [
                db.Image(str(image_asset), alt="Preview"),
                db.Video(str(video_asset), caption="Demo"),
            ]
        )

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        payload = websocket.receive_json()

    assert payload["type"] == "full"
    image_node = _find_node_by_type(payload["tree"], "Image")
    video_node = _find_node_by_type(payload["tree"], "Video")
    assert image_node is not None
    assert video_node is not None
    assert str(image_node["props"]["src"]).startswith("/__brickflow_asset__/")
    assert str(video_node["props"]["src"]).startswith("/__brickflow_asset__/")


def test_embed_allowlist_rejects_unapproved_origins():
    app = App(allowed_embed_origins=["https://allowed.example.com"])

    with pytest.raises(ValueError, match="allowed_embed_origins"):
        app.transform_serialized_tree(
            {
                "type": "Embed",
                "props": {"src": "https://blocked.example.com/dashboard", "title": "Blocked"},
            }
        )


def test_pipeline_node_click_payload_updates_state_and_rerenders():
    app = App()

    @app.page("/")
    def home():
        selected, set_selected = db.use_state("none")

        def select_node(payload):
            set_selected(payload["id"])

        return db.Column(
            [
                db.Text(selected),
                db.PipelineGraph(
                    nodes=[{"id": "bronze", "label": "Bronze", "status": "running"}],
                    edges=[],
                    on_node_click=select_node,
                ),
            ]
        )

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        full = websocket.receive_json()
        control = _find_node_by_type(full["tree"], "PipelineGraph")
        assert control is not None

        websocket.send_json(
            {
                "type": "event",
                "event_id": control["props"]["nodeClick"],
                "data": {"value": {"id": "bronze", "status": "running"}},
            }
        )
        patch = websocket.receive_json()

    assert patch["type"] == "patch"
    text_patch = next(item for item in patch["patches"] if item["path"] == [0])
    assert text_patch["props"]["value"] == "bronze"


def test_websocket_sends_event_complete_for_non_dirty_handlers():
    app = App()
    touched = {"count": 0}

    @app.page("/")
    def home():
        return db.Button("Ping", on_click=lambda: touched.__setitem__("count", touched["count"] + 1))

    client = TestClient(create_asgi_app(app))

    with client.websocket_connect("/events") as websocket:
        full = websocket.receive_json()
        event_id = full["tree"]["props"]["click"]

        websocket.send_json(
            {
                "type": "event",
                "event_id": event_id,
                "data": {},
            }
        )
        completion = websocket.receive_json()

    assert touched["count"] == 1
    assert completion == {"type": "event_complete", "event_id": event_id}
