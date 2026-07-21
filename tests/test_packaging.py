from pathlib import Path
import re

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def _load_workflow(name: str) -> tuple[str, dict]:
    workflow_path = REPO_ROOT / ".github" / "workflows" / name
    text = workflow_path.read_text(encoding="utf-8")
    workflow = yaml.safe_load(text)
    assert isinstance(workflow, dict)
    assert isinstance(workflow.get("jobs"), dict)
    return text, workflow


def _step_commands(job: dict) -> list[str]:
    return [step["run"] for step in job["steps"] if "run" in step]


def test_ci_splits_python_matrix_from_python_311_integration_gates():
    text, workflow = _load_workflow("ci.yml")
    jobs = workflow["jobs"]

    assert set(jobs) == {"python", "integration"}

    python_job = jobs["python"]
    assert python_job["strategy"]["matrix"]["python-version"] == [
        "3.10",
        "3.11",
        "3.12",
    ]
    python_setup = next(
        step for step in python_job["steps"] if step.get("uses") == "actions/setup-python@v5"
    )
    assert python_setup["with"]["python-version"] == "${{ matrix.python-version }}"
    python_commands = "\n".join(_step_commands(python_job))
    assert 'python -m pip install -e ".[dev]"' in python_commands
    assert "python -m pytest -q" in python_commands
    assert "python -m ruff check brickflowui tests examples" in python_commands
    assert "python -m mypy brickflowui" in python_commands

    integration_job = jobs["integration"]
    integration_setup = next(
        step for step in integration_job["steps"] if step.get("uses") == "actions/setup-python@v5"
    )
    assert integration_setup["with"]["python-version"] == "3.11"
    integration_commands = "\n".join(_step_commands(integration_job))
    for command in (
        "npm test -- --run",
        "npm run lint",
        "npm audit --audit-level=high",
        "npm run typecheck",
        "npm run build",
        "git diff --exit-code -- brickflowui/frontend/dist",
        "python scripts/smoke_examples.py",
        "python scripts/generate_component_reference.py",
        "git diff --exit-code -- docs/components/reference",
        "python -m mkdocs build --strict",
        "python -m build",
    ):
        assert command in integration_commands

    integration_only_commands = (
        "npm ",
        "brickflowui/frontend/dist",
        "scripts/smoke_examples.py",
        "scripts/generate_component_reference.py",
        "docs/components/reference",
        "mkdocs build",
        "python -m build",
    )
    assert not any(command in python_commands for command in integration_only_commands)
    assert (
        '    strategy:\n      matrix:\n        python-version: ["3.10", "3.11", "3.12"]'
        in text
    )


def test_security_audits_installed_project_dependencies():
    _, workflow = _load_workflow("security.yml")
    audit_job = workflow["jobs"]["audit"]
    commands = _step_commands(audit_job)
    joined_commands = "\n".join(commands)

    assert "python -m pip install pip-audit" in joined_commands
    assert 'python -m pip install -e ".[dev]"' in joined_commands
    assert 'python -m pip install -e ".[databricks,viz]"' in joined_commands
    audit_index = next(index for index, command in enumerate(commands) if "python -m pip_audit" in command)
    project_install_indexes = [
        index
        for index, command in enumerate(commands)
        if 'python -m pip install -e ".[dev]"' in command
        or 'python -m pip install -e ".[databricks,viz]"' in command
    ]
    assert all(index < audit_index for index in project_install_indexes)


def test_frontend_distribution_contains_only_one_current_entry_bundle():
    dist = REPO_ROOT / "brickflowui" / "frontend" / "dist"
    index_html = (dist / "index.html").read_text(encoding="utf-8")
    assets = dist / "assets"

    entry_bundles = list(assets.glob("index-*.js"))
    assert len(entry_bundles) == 1, (
        "frontend/dist contains stale entry bundles; run a clean frontend build"
    )

    references = re.findall(r'(?:src|href)="/assets/([^"]+)"', index_html)
    assert references
    assert all((assets / reference).is_file() for reference in references)
