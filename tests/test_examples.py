from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
import runpy
import subprocess

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


@pytest.mark.parametrize("example_name", RUNTIME_SMOKE_EXAMPLES)
def test_maintained_example_serves_shell_and_full_websocket_tree(example_name: str) -> None:
    app_path = EXAMPLES_ROOT / example_name / "app.py"
    namespace = runpy.run_path(
        str(app_path),
        run_name=f"brickflowui_example_{example_name}",
    )
    app = namespace["app"]
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
