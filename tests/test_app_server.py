import pytest
from fastapi.testclient import TestClient
from brickflowui.app import App
from brickflowui.auth import HeaderAuthProvider, current_user
from brickflowui.server import create_asgi_app
from brickflowui.vdom import VNode

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

def test_extract_event_payload_unwraps_single_value():
    from brickflowui.server import _extract_event_payload

    assert _extract_event_payload({"value": "abc"}) == "abc"
    assert _extract_event_payload({"row": {"id": 1}}) == {"id": 1}
    assert _extract_event_payload({"a": 1, "b": 2}) == {"a": 1, "b": 2}
