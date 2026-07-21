from __future__ import annotations

import json
from collections.abc import Mapping
import os
from pathlib import Path
import runpy
import subprocess
import uuid

import pytest
from fastapi.testclient import TestClient

from brickflowui.server import create_asgi_app
from scripts.example_manifest import load_example_manifest

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_ROOT = REPO_ROOT / "examples"

FLAGSHIP_EXAMPLES = {
    "acme_analytics_command_center",
    "component_studio",
    "clinical_trial_command_center",
    "data_pipeline_command_center",
    "geometric_signal_lab",
    "secure_internal_tools",
    "workspace_studio",
}

RUNTIME_SMOKE_EXAMPLES = (
    "operations_finance_portal",
    "weather_dashboard",
    "component_studio",
    "auth_portal",
    "pipeline_observability_015",
)

MEDIA_PROP_KEYS = frozenset({"src", "poster", "logo", "favicon", "avatar", "image"})
REMOTE_MEDIA_PREFIXES = ("http://", "https://", "data:", "blob:")


def _load_example_app(example_name: str):
    app_path = EXAMPLES_ROOT / example_name / "app.py"
    namespace = runpy.run_path(
        str(app_path),
        run_name=f"brickflowui_example_{example_name}",
    )
    return namespace["app"]


def _iter_media_props(payload: object):
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key in MEDIA_PROP_KEYS:
                yield key, value
            yield from _iter_media_props(value)
    elif isinstance(payload, list):
        for value in payload:
            yield from _iter_media_props(value)


def _assert_media_value_stays_in_example(app, root: Path, value: object) -> None:
    if not isinstance(value, (str, Path)):
        return

    raw = str(value)
    if raw.lower().startswith(REMOTE_MEDIA_PREFIXES):
        return

    if raw.startswith("/__brickflow_asset__/"):
        asset_id = raw.split("/", 3)[2]
        asset_path = app.get_registered_asset(asset_id)
        assert asset_path is not None, f"Unregistered app asset URL: {raw}"
        assert asset_path.is_file(), f"Missing app asset: {asset_path}"
        resolved_root = root.resolve()
        assert asset_path == resolved_root or resolved_root in asset_path.parents
        return

    asset_path = Path(raw).expanduser().resolve()
    resolved_root = root.resolve()
    assert asset_path == resolved_root or resolved_root in asset_path.parents


def test_maintained_example_manifest_is_complete() -> None:
    specs = load_example_manifest(REPO_ROOT)

    assert [spec.name for spec in specs] == [
        "counter",
        "component_studio",
        "data_pipeline_command_center",
        "clinical_trial_command_center",
        "auth_portal",
        "chatbot_workspace",
    ]
    assert len({spec.name for spec in specs}) == len(specs)
    for spec in specs:
        root = EXAMPLES_ROOT / spec.name
        assert (root / "app.py").is_file()
        assert (root / "requirements.txt").is_file()
        assert (root / "app.yaml").is_file()


def test_maintained_examples_are_self_contained() -> None:
    for spec in load_example_manifest(REPO_ROOT):
        root = EXAMPLES_ROOT / spec.name
        source = (root / "app.py").read_text(encoding="utf-8-sig")

        assert "sys.path" not in source
        assert "../../" not in source.replace("\\\\", "/")
        assert "brickflowui" in (root / "requirements.txt").read_text(encoding="utf-8").lower()
        manifest = (root / "app.yaml").read_text(encoding="utf-8")
        assert "python" in manifest and "app.py" in manifest


def test_manifest_auth_headers_are_immutable() -> None:
    specs = load_example_manifest(REPO_ROOT)
    clinical_trial = next(spec for spec in specs if spec.name == "clinical_trial_command_center")

    assert isinstance(clinical_trial.auth_headers, Mapping)
    assert not isinstance(clinical_trial.auth_headers, dict)
    with pytest.raises(TypeError):
        clinical_trial.auth_headers["x-brickflow-user-id"] = "changed@example.com"


def test_repository_tooling_is_tracked_candidate() -> None:
    for tool_path in (
        "scripts/smoke_examples.py",
        "scripts/cleanup_local_artifacts.ps1",
    ):
        result = subprocess.run(
            ["git", "check-ignore", "--quiet", tool_path],
            cwd=REPO_ROOT,
            check=False,
        )
        assert result.returncode == 1, f"{tool_path} must not be ignored"


def test_smoke_runner_uses_the_maintained_manifest() -> None:
    from scripts.smoke_examples import configured_checks

    assert [item.name for item in configured_checks(REPO_ROOT)] == [
        spec.name for spec in load_example_manifest(REPO_ROOT)
    ]


def test_smoke_tree_validator_rejects_unrecognizable_vdom_root() -> None:
    from scripts.smoke_examples import validate_full_tree

    with pytest.raises(RuntimeError, match="non-empty VDOM root"):
        validate_full_tree({"type": "full", "tree": {"unexpected": True}}, "/")


def test_smoke_tree_validator_accepts_vdom_root() -> None:
    from scripts.smoke_examples import validate_full_tree

    validate_full_tree({"type": "full", "tree": {"type": "div", "children": []}}, "/")


def test_cleanup_rejects_reparse_target() -> None:
    test_root = REPO_ROOT / ".tmp" / f"cleanup-reparse-{uuid.uuid4().hex}"
    target = test_root / "target"
    target.mkdir(parents=True)
    reparse_target = test_root / "reparse-target"
    try:
        os.symlink(target, reparse_target, target_is_directory=True)
    except OSError as exc:
        target.rmdir()
        test_root.rmdir()
        pytest.skip(f"Symlink creation is not supported: {exc}")
    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                "scripts/cleanup_local_artifacts.ps1",
                "-ValidateTarget",
                str(reparse_target),
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        assert result.returncode != 0
        assert "Refusing cleanup through reparse point" in result.stderr
    finally:
        reparse_target.unlink(missing_ok=True)
        target.rmdir()
        test_root.rmdir()


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        ({"schema_version": 2, "examples": []}, "Unsupported examples manifest schema_version"),
        ({"schema_version": 1, "examples": {}}, "examples must be a list"),
        (
            {
                "schema_version": 1,
                "examples": [
                    {"name": "counter", "title": "Counter", "kind": "quickstart", "routes": ["/"], "auth_headers": {}},
                    {"name": "counter", "title": "Counter", "kind": "quickstart", "routes": ["/"], "auth_headers": {}},
                ],
            },
            "Example names must be unique",
        ),
        (
            {
                "schema_version": 1,
                "examples": [{"name": "../counter", "title": "Counter", "kind": "quickstart", "routes": ["/"], "auth_headers": {}}],
            },
            "Example name must be a relative directory name",
        ),
        (
            {
                "schema_version": 1,
                "examples": [{"name": "counter", "title": "Counter", "kind": "quickstart", "routes": [], "auth_headers": {}}],
            },
            "Example routes must be a non-empty list of strings",
        ),
        (
            {
                "schema_version": 1,
                "examples": [{"name": "counter", "title": "Counter", "kind": "quickstart", "routes": ["/"], "auth_headers": {"x-user": 1}}],
            },
            "Example auth_headers must map strings to strings",
        ),
    ],
)
def test_manifest_rejects_invalid_configuration(
    tmp_path: Path, payload: dict[str, object], message: str
) -> None:
    manifest_path = tmp_path / "examples" / "manifest.json"
    manifest_path.parent.mkdir()
    manifest_path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        load_example_manifest(tmp_path)


@pytest.mark.parametrize(
    "name",
    (
        "counter ",
        "counter.",
        "NUL",
        "nul",
        "CON",
        "PRN",
        "AUX",
        "COM1",
        "LPT9",
        "com\u00b9",
        "COM\u00b2",
        "com\u00b3",
        "lpt\u00b9",
        "LPT\u00b2",
        "lpt\u00b3",
        "foo<bar",
        "foo>bar",
        'foo"bar',
        "foo:bar",
        "foo/bar",
        r"foo\bar",
        "foo|bar",
        "foo?bar",
        "foo*bar",
        "foo\u0001bar",
        "foo\u001fbar",
    ),
)
def test_manifest_rejects_windows_aliasing_names(tmp_path: Path, name: str) -> None:
    manifest_path = tmp_path / "examples" / "manifest.json"
    manifest_path.parent.mkdir()
    manifest_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "examples": [
                    {
                        "name": name,
                        "title": "Counter",
                        "kind": "quickstart",
                        "routes": ["/"],
                        "auth_headers": {},
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Example name must be a relative directory name"):
        load_example_manifest(tmp_path)


def test_every_example_app_compiles() -> None:
    example_apps = sorted(EXAMPLES_ROOT.glob("*/app.py"))

    assert example_apps, "Expected at least one example app."

    for app_path in example_apps:
        source = app_path.read_text(encoding="utf-8-sig")
        compile(source, str(app_path), "exec")


def test_flagship_examples_exist() -> None:
    available_examples = {path.name for path in EXAMPLES_ROOT.iterdir() if path.is_dir()}

    assert FLAGSHIP_EXAMPLES.issubset(available_examples)


def test_retained_example_routes_render_with_self_contained_media() -> None:
    for spec in load_example_manifest(REPO_ROOT):
        root = EXAMPLES_ROOT / spec.name
        app = _load_example_app(spec.name)
        client = TestClient(create_asgi_app(app))

        for route in spec.routes:
            response = client.get(route, headers=dict(spec.auth_headers))
            assert response.status_code == 200, f"{spec.name} did not serve {route}"

            with client.websocket_connect(
                f"/events?path={route}", headers=dict(spec.auth_headers)
            ) as websocket:
                payload = websocket.receive_json()

            assert payload["type"] == "full"
            tree = payload["tree"]
            json.dumps(tree)
            for _, value in _iter_media_props(tree):
                _assert_media_value_stays_in_example(app, root, value)


def test_flagship_exposes_complete_operational_views() -> None:
    namespace = runpy.run_path(
        str(EXAMPLES_ROOT / "data_pipeline_command_center" / "app.py")
    )

    rows = namespace["load_pipeline_records"]("mock")
    nodes, edges = namespace["pipeline_flow"](rows)
    columns = namespace["triage_columns"](rows)

    assert rows and all("pipeline" in row for row in rows)
    assert len({row["pipeline"] for row in rows}) == len(rows)
    assert {node["id"] for node in nodes} == {row["pipeline"] for row in rows}
    assert all(edge["from"] != edge["to"] for edge in edges)
    assert [column["id"] for column in columns] == ["healthy", "watch", "at-risk"]
    assert {
        card["id"] for column in columns for card in column["cards"]
    } == {row["pipeline"] for row in rows}


def test_flagship_websocket_switches_every_operational_view() -> None:
    namespace = runpy.run_path(
        str(EXAMPLES_ROOT / "data_pipeline_command_center" / "app.py")
    )
    assert namespace["VIEW_KEYS"] == (
        "overview",
        "pipelines",
        "reliability",
        "triage",
        "assistant",
    )

    def find_view_button(node: dict, view_key: str) -> dict | None:
        if node.get("type") == "Button" and node.get("props", {}).get(
            "viewKey"
        ) == view_key:
            return node
        for child in node.get("children", []):
            found = find_view_button(child, view_key)
            if found:
                return found
        return None

    app = namespace["app"]
    client = TestClient(create_asgi_app(app))
    expected_markers = {
        "overview": "Operational pulse",
        "pipelines": "Pipeline flow",
        "reliability": "Reliability signals",
        "triage": "Triage queue",
        "assistant": "Pipeline assistant",
    }

    for view_key in namespace["VIEW_KEYS"]:
        with client.websocket_connect("/events?path=/") as websocket:
            full = websocket.receive_json()
            buttons = {
                key: find_view_button(full["tree"], key)
                for key in namespace["VIEW_KEYS"]
            }
            assert all(buttons.values())

            if view_key != "overview":
                button = buttons[view_key]
                assert button is not None
                websocket.send_json(
                    {
                        "type": "event",
                        "event_id": button["props"]["click"],
                        "data": {"value": None},
                    }
                )
                response = websocket.receive_json()
            else:
                pipelines_button = buttons["pipelines"]
                overview_button = buttons["overview"]
                assert pipelines_button is not None and overview_button is not None
                websocket.send_json(
                    {
                        "type": "event",
                        "event_id": pipelines_button["props"]["click"],
                        "data": {"value": None},
                    }
                )
                assert websocket.receive_json()["type"] == "patch"
                assert websocket.receive_json()["type"] == "event_complete"
                websocket.send_json(
                    {
                        "type": "event",
                        "event_id": overview_button["props"]["click"],
                        "data": {"value": None},
                    }
                )
                response = websocket.receive_json()

        assert response["type"] == "patch", response
        assert expected_markers[view_key] in json.dumps(response)


@pytest.mark.parametrize("example_name", RUNTIME_SMOKE_EXAMPLES)
def test_maintained_example_serves_shell_and_full_websocket_tree(example_name: str) -> None:
    app = _load_example_app(example_name)
    client = TestClient(create_asgi_app(app))

    response = client.get("/")

    assert response.status_code == 200
    assert "BrickflowUI" in response.text

    with client.websocket_connect("/events?path=/") as websocket:
        payload = websocket.receive_json()

    assert payload["type"] == "full"
    assert isinstance(payload["tree"], dict)
    assert payload["tree"]["type"]
    json.dumps(payload["tree"])
