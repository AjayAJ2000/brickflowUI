from pathlib import Path
import re

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def _load_workflow(name: str) -> dict:
    workflow_path = REPO_ROOT / ".github" / "workflows" / name
    workflow = yaml.safe_load(workflow_path.read_text(encoding="utf-8"))
    assert isinstance(workflow, dict)
    assert isinstance(workflow.get("jobs"), dict)
    return workflow


def _executable_lines(step: dict) -> tuple[str, ...]:
    run = step.get("run")
    if not isinstance(run, str):
        return ()

    commands = []
    for raw_line in run.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        executable = line.split(maxsplit=1)[0]
        if executable in {"echo", "printf"}:
            continue
        commands.append(line)
    return tuple(commands)


def _working_directory(job: dict, step: dict) -> str | None:
    return step.get("working-directory") or job.get("defaults", {}).get("run", {}).get(
        "working-directory"
    )


def _command_occurrences(workflow: dict, command: str) -> list[tuple[str, int, str | None]]:
    return [
        (job_name, step_index, _working_directory(job, step))
        for job_name, job in workflow["jobs"].items()
        for step_index, step in enumerate(job["steps"])
        if command in _executable_lines(step)
    ]


def _command_sequence(job: dict) -> list[str]:
    return [command for step in job["steps"] for command in _executable_lines(step)]


def _assert_owned_by(workflow: dict, command: str, job_name: str) -> None:
    occurrences = _command_occurrences(workflow, command)
    assert len(occurrences) == 1
    assert occurrences[0][0] == job_name


def test_workflow_command_parser_ignores_comments_and_output_only_commands():
    step = {
        "run": """
            # python -m pytest -q
            echo "python -m pytest -q"
            printf '%s\\n' "python -m pytest -q"
            python -m ruff check brickflowui tests examples
        """
    }

    assert _executable_lines(step) == ("python -m ruff check brickflowui tests examples",)


def test_ci_splits_python_matrix_from_python_311_integration_gates():
    workflow = _load_workflow("ci.yml")
    jobs = workflow["jobs"]

    assert {"python", "integration"} <= set(jobs)

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
    assert any(
        job_name == "python"
        for job_name, _, _ in _command_occurrences(
            workflow, 'python -m pip install -e ".[dev]"'
        )
    )
    for command in (
        "python -m pytest -q",
        "python -m ruff check brickflowui tests examples",
        "python -m mypy brickflowui",
    ):
        _assert_owned_by(workflow, command, "python")
    python_sequence = _command_sequence(python_job)
    python_gate_order = (
        'python -m pip install -e ".[dev]"',
        "python -m pytest -q",
        "python -m ruff check brickflowui tests examples",
        "python -m mypy brickflowui",
    )
    assert [python_sequence.index(command) for command in python_gate_order] == sorted(
        python_sequence.index(command) for command in python_gate_order
    )

    integration_job = jobs["integration"]
    integration_setup = next(
        step for step in integration_job["steps"] if step.get("uses") == "actions/setup-python@v5"
    )
    assert integration_setup["with"]["python-version"] == "3.11"
    assert any(
        step.get("uses") == "actions/setup-node@v4" for step in integration_job["steps"]
    )

    frontend_commands = (
        "npm ci",
        "npm test -- --run",
        "npm run lint",
        "npm audit --audit-level=high",
        "npm run typecheck",
        "npm run build",
    )
    for command in frontend_commands:
        _assert_owned_by(workflow, command, "integration")
        assert _command_occurrences(workflow, command)[0][2] == "frontend"

    for command in (
        "git diff --exit-code -- brickflowui/frontend/dist",
        "python scripts/smoke_examples.py",
        "python scripts/generate_component_reference.py",
        "git diff --exit-code -- docs/components/reference",
        "python -m mkdocs build --strict",
        "python -m build",
    ):
        _assert_owned_by(workflow, command, "integration")

    integration_sequence = _command_sequence(integration_job)
    integration_gate_order = (
        "npm ci",
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
    )
    assert [integration_sequence.index(command) for command in integration_gate_order] == sorted(
        integration_sequence.index(command) for command in integration_gate_order
    )


def test_security_audits_installed_project_dependencies():
    workflow = _load_workflow("security.yml")
    audit_job = workflow["jobs"]["audit"]
    assert any(step.get("uses") == "actions/setup-node@v4" for step in audit_job["steps"])

    commands = _command_sequence(audit_job)
    audit_index = commands.index("python -m pip_audit")
    for install_command in (
        "python -m pip install pip-audit",
        'python -m pip install -e ".[dev]"',
        'python -m pip install -e ".[databricks,viz]"',
    ):
        assert commands.count(install_command) == 1
        assert commands.index(install_command) < audit_index

    for frontend_command in ("npm ci", "npm audit --omit=dev"):
        occurrences = _command_occurrences(workflow, frontend_command)
        assert len(occurrences) == 1
        assert occurrences[0][0] == "audit"
        assert occurrences[0][2] == "frontend"
    assert commands.index("npm ci") < commands.index("npm audit --omit=dev")


def test_package_uses_canonical_async_framework_classifiers():
    pyproject = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")

    assert '"Framework :: AsyncIO"' in pyproject
    assert '"Framework :: FastAPI"' in pyproject
    assert "ASGI :: Application" not in pyproject
    assert "WSGI :: Application" not in pyproject


def test_current_changelog_does_not_claim_an_unconfigured_twine_gate():
    changelog = (REPO_ROOT / "docs" / "CHANGELOG.md").read_text(encoding="utf-8")
    current_release = changelog.split("## 0.1.14", maxsplit=1)[0]

    assert "Twine" not in current_release


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
