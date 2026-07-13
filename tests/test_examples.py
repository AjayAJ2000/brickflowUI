from __future__ import annotations

import json
from pathlib import Path
import runpy

import pytest
from fastapi.testclient import TestClient

from brickflowui.server import create_asgi_app

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
