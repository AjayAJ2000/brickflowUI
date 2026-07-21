# BrickflowUI 0.2 Showcase Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the overlapping example archive with six self-contained, end-to-end showcases led by a polished Databricks pipeline command center, and make repository validation reproducible from a clean clone.

**Architecture:** A tracked JSON manifest becomes the single source of truth for maintained examples, tests, smoke tooling, and documentation. The existing data-pipeline and pipeline-observability examples are consolidated into one flagship without adding new public framework APIs in this milestone. Repository and CI checks validate manifests, assets, runtime startup, frontend bundle drift, and supported Python versions.

**Tech Stack:** Python 3.10-3.12, FastAPI TestClient, pytest, PowerShell cleanup tooling, GitHub Actions, BrickflowUI VDOM/components, React/Vite packaged frontend.

## Global Constraints

- Build from BrickflowUI 0.1.15 on branch `codex/production-data-apps-02`.
- Retain exactly: `counter`, `component_studio`, `data_pipeline_command_center`, `clinical_trial_command_center`, `auth_portal`, and `chatbot_workspace`.
- Keep raw credentials, SDK clients, SQL connections, and exception details out of browser payloads.
- Preserve active Git worktrees, `Branding_Files/`, `frontend/package-lock.json`, `brickflowui/frontend/dist/`, and generated component reference pages.
- Every behavior change uses a failing test before implementation.
- Do not add public runtime components in this milestone; `AppShell`, resources, and `DataGrid` belong to later plans.
- The flagship must support mock data without Databricks credentials and use the same normalized record shape for Databricks SQL.
- No removed example may remain referenced by tracked documentation, tests, or scripts.

---

## File map

- `examples/manifest.json`: authoritative maintained-example inventory and validation metadata.
- `scripts/example_manifest.py`: manifest parser and structural validator shared by tests and smoke tooling.
- `scripts/smoke_examples.py`: bounded HTTP/WebSocket smoke runner driven by the manifest.
- `scripts/cleanup_local_artifacts.ps1`: safe, explicit local cleanup utility.
- `tests/test_examples.py`: compile, manifest, asset, deployment, render, HTTP, and WebSocket contracts.
- `examples/data_pipeline_command_center/app.py`: flagship mock/Databricks operational workflow.
- `docs/EXAMPLES.md`: concise showcase catalog containing only maintained examples.
- `DEVELOPMENT.md`: clean-clone development and showcase verification commands.
- `.github/workflows/ci.yml`: Python matrix and generated-bundle drift checks.
- `.github/workflows/security.yml`: project-aware Python dependency audit.

### Task 1: Authoritative maintained-example manifest

**Files:**
- Create: `examples/manifest.json`
- Create: `scripts/example_manifest.py`
- Modify: `tests/test_examples.py`

**Interfaces:**
- Produces: `load_example_manifest(repo_root: Path) -> tuple[ExampleSpec, ...]`
- Produces: `ExampleSpec(name: str, title: str, kind: str, routes: tuple[str, ...], auth_headers: Mapping[str, str])`
- Consumes: standard-library `json`, `dataclasses`, and `pathlib` only.

- [ ] **Step 1: Write failing manifest tests**

Add tests that import `scripts.example_manifest`, assert the exact six names, assert unique names, and assert every declared directory has `app.py`, `requirements.txt`, and `app.yaml`:

```python
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
```

- [ ] **Step 2: Run the tests and verify RED**

Run: `python -m pytest tests/test_examples.py::test_maintained_example_manifest_is_complete -q -p no:cacheprovider`

Expected: FAIL because `scripts.example_manifest` or `examples/manifest.json` does not exist.

- [ ] **Step 3: Add the manifest**

Create this exact shape, including headers required by protected examples:

```json
{
  "schema_version": 1,
  "examples": [
    {"name": "counter", "title": "Quickstart Counter", "kind": "quickstart", "routes": ["/"], "auth_headers": {}},
    {"name": "component_studio", "title": "Component Studio", "kind": "reference", "routes": ["/"], "auth_headers": {}},
    {"name": "data_pipeline_command_center", "title": "Data Pipeline Command Center", "kind": "flagship", "routes": ["/"], "auth_headers": {}},
    {"name": "clinical_trial_command_center", "title": "Clinical Trial Command Center", "kind": "industry", "routes": ["/", "/overview", "/safety", "/dataops"], "auth_headers": {"x-brickflow-user-id": "clinical.demo@example.com", "x-brickflow-user-roles": "clinician,ops"}},
    {"name": "auth_portal", "title": "Authentication Portal", "kind": "security", "routes": ["/", "/workspace", "/admin", "/app-ops"], "auth_headers": {}},
    {"name": "chatbot_workspace", "title": "Chatbot Workspace", "kind": "assistant", "routes": ["/"], "auth_headers": {}}
  ]
}
```

- [ ] **Step 4: Implement strict manifest parsing**

`scripts/example_manifest.py` must reject unknown schema versions, non-list examples, duplicate names, invalid relative names, missing routes, and non-string headers. Use frozen dataclasses and return tuples so callers cannot mutate shared configuration.

```python
@dataclass(frozen=True)
class ExampleSpec:
    name: str
    title: str
    kind: str
    routes: tuple[str, ...]
    auth_headers: Mapping[str, str]

def load_example_manifest(repo_root: Path) -> tuple[ExampleSpec, ...]:
    payload = json.loads((repo_root / "examples" / "manifest.json").read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError("Unsupported examples manifest schema_version")
    rows = payload.get("examples")
    if not isinstance(rows, list):
        raise ValueError("examples must be a list")
    specs = tuple(_parse_spec(row) for row in rows)
    if len({spec.name for spec in specs}) != len(specs):
        raise ValueError("Example names must be unique")
    return specs
```

- [ ] **Step 5: Run focused tests and verify GREEN**

Run: `python -m pytest tests/test_examples.py -q -p no:cacheprovider`

Expected: existing tests plus new manifest tests pass after Task 3 supplies the missing counter deployment files; until then only the parser tests are required to pass.

- [ ] **Step 6: Commit**

```text
git add examples/manifest.json scripts/example_manifest.py tests/test_examples.py
git commit -m "test: define maintained example manifest"
```

### Task 2: Tracked smoke and cleanup tooling

**Files:**
- Create: `scripts/smoke_examples.py`
- Create: `scripts/cleanup_local_artifacts.ps1`
- Modify: `.gitignore`
- Test: `tests/test_examples.py`

**Interfaces:**
- Consumes: `load_example_manifest()` from Task 1.
- Produces: `run_check(spec: ExampleSpec, port: int) -> tuple[bool, str]`.
- Produces: PowerShell parameters `-IncludeBuildArtifacts` and `-WhatIf` through `SupportsShouldProcess`.

- [ ] **Step 1: Write failing tooling tests**

Add tests asserting both files are tracked candidates, `scripts/` is not globally ignored, and the smoke module enumerates exactly the manifest entries:

```python
def test_smoke_runner_uses_the_maintained_manifest() -> None:
    from scripts.smoke_examples import configured_checks
    assert [item.name for item in configured_checks(REPO_ROOT)] == [
        spec.name for spec in load_example_manifest(REPO_ROOT)
    ]
```

- [ ] **Step 2: Verify RED**

Run: `python -m pytest tests/test_examples.py::test_smoke_runner_uses_the_maintained_manifest -q -p no:cacheprovider`

Expected: FAIL because the tracked smoke module is absent in this worktree.

- [ ] **Step 3: Implement the manifest-driven smoke runner**

Port the bounded process launcher into `scripts/smoke_examples.py`, replace the hard-coded check list with:

```python
def configured_checks(repo_root: Path = REPO_ROOT) -> tuple[ExampleSpec, ...]:
    return load_example_manifest(repo_root)
```

For each spec, start `app.py`, request every declared route with `auth_headers`, connect to `/events?path=<route>`, require a `full` message with a non-empty VDOM root, then stop the process in `finally`. Keep per-example startup bounded to 35 seconds and HTTP calls bounded to 5 seconds.

- [ ] **Step 4: Implement explicit safe cleanup**

The PowerShell script must resolve and validate every target beneath the repository root before removal. Default targets are `.tmp`, `.pytest_cache`, `site`, root `pytest-cache-files-*`, root `_tmp_cli_*`, and `__pycache__` beneath `brickflowui`, `tests`, and `examples`. `-IncludeBuildArtifacts` additionally includes root `dist`, `build`, and `frontend/node_modules`. It must never target `.worktrees`, `Branding_Files`, `brickflowui/frontend/dist`, or the repository root.

```powershell
[CmdletBinding(SupportsShouldProcess)]
param([switch]$IncludeBuildArtifacts)
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
function Remove-RepoTarget([string]$Path) {
    $resolved = [System.IO.Path]::GetFullPath($Path)
    if (-not $resolved.StartsWith($repoRoot + [System.IO.Path]::DirectorySeparatorChar)) {
        throw "Refusing cleanup outside repository: $resolved"
    }
    if (Test-Path -LiteralPath $resolved) {
        if ($PSCmdlet.ShouldProcess($resolved, "Remove generated artifact")) {
            Remove-Item -LiteralPath $resolved -Recurse -Force
        }
    }
}
```

- [ ] **Step 5: Stop ignoring all scripts**

Remove the terminal `scripts/` rule from `.gitignore`. Keep generated caches ignored with explicit patterns already present.

- [ ] **Step 6: Verify GREEN and dry-run cleanup**

Run:

```text
python -m pytest tests/test_examples.py -q -p no:cacheprovider
powershell -ExecutionPolicy Bypass -File scripts/cleanup_local_artifacts.ps1 -WhatIf
git check-ignore scripts/smoke_examples.py
```

Expected: tests pass; cleanup lists only approved targets; `git check-ignore` exits 1.

- [ ] **Step 7: Commit**

```text
git add .gitignore scripts/smoke_examples.py scripts/cleanup_local_artifacts.ps1 tests/test_examples.py
git commit -m "chore: track reproducible repository tooling"
```

### Task 3: Self-contained retained examples

**Files:**
- Create: `examples/counter/requirements.txt`
- Create: `examples/counter/app.yaml`
- Create: `examples/component_studio/assets/brickflowui-mark.svg`
- Create: `examples/clinical_trial_command_center/assets/brickflowui-mark.svg`
- Modify: retained example `app.py` files where asset roots or `sys.path` are unsafe.
- Modify: `tests/test_examples.py`

**Interfaces:**
- Every retained directory produces an independently runnable `python app.py` deployment unit.
- Local media paths resolve beneath that example directory.

- [ ] **Step 1: Write failing self-containment tests**

Add assertions that retained source does not mutate `sys.path`, does not use `../../` asset paths, all local asset props resolve inside the example directory, requirements contain `brickflowui`, and manifests run `python app.py`.

```python
def test_maintained_examples_are_self_contained() -> None:
    for spec in load_example_manifest(REPO_ROOT):
        root = EXAMPLES_ROOT / spec.name
        source = (root / "app.py").read_text(encoding="utf-8-sig")
        assert "sys.path" not in source
        assert "../../" not in source.replace("\\\\", "/")
        assert "brickflowui" in (root / "requirements.txt").read_text(encoding="utf-8").lower()
        manifest = (root / "app.yaml").read_text(encoding="utf-8")
        assert "python" in manifest and "app.py" in manifest
```

- [ ] **Step 2: Verify RED**

Run: `python -m pytest tests/test_examples.py::test_maintained_examples_are_self_contained -q -p no:cacheprovider`

Expected: FAIL for missing counter files, external logo paths, or `sys.path` mutation.

- [ ] **Step 3: Add counter deployment files**

`requirements.txt`:

```text
brickflowui>=0.1.15,<0.3
```

`app.yaml`:

```yaml
command:
  - python
  - app.py
env:
  - name: BRICKFLOWUI_ENV
    value: demo
```

- [ ] **Step 4: Bundle logos and fix roots**

Copy the canonical `docs/assets/brickflowui-mark.svg` bytes into each retained example that uses the mark. Resolve assets with `Path(__file__).parent / "assets" / "brickflowui-mark.svg"` and configure `asset_roots=[Path(__file__).parent]` when constructing `db.App`.

- [ ] **Step 5: Remove repository path mutation**

Delete `sys.path` manipulation from `auth_portal`. Imports must be only from installed dependencies and local modules inside that example directory.

- [ ] **Step 6: Verify retained apps**

Run: `python -m pytest tests/test_examples.py -q -p no:cacheprovider`

Expected: all manifest, self-containment, render, and WebSocket tests pass.

- [ ] **Step 7: Commit**

```text
git add examples/counter examples/component_studio examples/clinical_trial_command_center examples/auth_portal tests/test_examples.py
git commit -m "fix: make maintained examples deployable"
```

### Task 4: Consolidate the flagship command center

**Files:**
- Modify: `examples/data_pipeline_command_center/app.py`
- Modify: `examples/data_pipeline_command_center/requirements.txt`
- Test: `tests/test_examples.py`

**Interfaces:**
- Keeps: `load_pipeline_records(source_mode: str) -> list[dict]` normalized mock/SQL boundary.
- Adds: `pipeline_flow(records: list[dict]) -> tuple[list[dict], list[dict]]`.
- Adds: `triage_columns(records: list[dict]) -> list[dict]`.
- Adds view keys: `overview`, `pipelines`, `reliability`, `triage`, and `assistant`.

- [ ] **Step 1: Write failing flagship contract tests**

Load the example with `runpy`, assert the mock adapter returns stable records, helper functions produce stable IDs, and WebSocket interactions can switch to every declared view without an error message.

```python
def test_flagship_exposes_complete_operational_views() -> None:
    namespace = runpy.run_path(str(EXAMPLES_ROOT / "data_pipeline_command_center" / "app.py"))
    rows = namespace["load_pipeline_records"]("mock")
    nodes, edges = namespace["pipeline_flow"](rows)
    columns = namespace["triage_columns"](rows)
    assert rows and all("pipeline" in row for row in rows)
    assert {node["id"] for node in nodes}
    assert all(edge["from"] != edge["to"] for edge in edges)
    assert [column["id"] for column in columns] == ["healthy", "watch", "at-risk"]
```

- [ ] **Step 2: Verify RED**

Run: `python -m pytest tests/test_examples.py::test_flagship_exposes_complete_operational_views -q -p no:cacheprovider`

Expected: FAIL because `pipeline_flow` and `triage_columns` are not defined.

- [ ] **Step 3: Add stable operational helpers**

Build graph nodes from pipeline IDs and statuses, use deterministic layer edges, and construct Kanban cards with `id`, `title`, `subtitle`, and status. Never use list indexes as IDs.

```python
def triage_columns(records: list[dict]) -> list[dict]:
    groups = (("healthy", "Healthy", {"Healthy", "Strong"}),
              ("watch", "Watch", {"Watch"}),
              ("at-risk", "At Risk", {"At Risk"}))
    return [{
        "id": group_id,
        "label": label,
        "cards": [{
            "id": row["pipeline"],
            "title": row["pipeline_label"],
            "subtitle": f"{row['freshness_min']}m freshness · {row['success_rate']:.1f}% success",
            "status": row["status"].lower().replace(" ", "-"),
        } for row in records if row["status"] in statuses],
    } for group_id, label, statuses in groups]
```

- [ ] **Step 4: Merge high-value observability workflows**

Add a pipeline-flow view with `PipelineGraph`, a triage view with `KanbanBoard`, a reliability view using the existing heatmap/scatter/composed chart primitives, and an assistant view using `ChatMessage` and `ChatInput`. Retain current filtering, executive summary, source switching, data model documentation, modal brief, and SQL fallback.

- [ ] **Step 5: Apply the showcase visual system**

Use a single light/dark-compatible token system with restrained burgundy primary, green operational success, neutral canvas, 14-18px radii, and compact typography. Replace repeated equal-card grids with a hierarchy of one summary strip, one dominant operational surface, and supporting panels. Keep the page at `maxWidth: 1480px`, desktop navigation on one line, controls wrapping at narrow widths, and all visible copy domain-specific. Remove version labels, fake trust claims, and generic “serious internal apps” language.

- [ ] **Step 6: Add complete states**

The source adapter and each view must render explicit mock/source status, empty filtered results, SQL fallback notice, permission/error notice, pending job action, success acknowledgement, disconnected runtime banner from the core, and assistant empty/pending response copy. Simulated actions must say “Simulated” in visible feedback.

- [ ] **Step 7: Verify interaction paths**

Run:

```text
python -m pytest tests/test_examples.py tests/test_app_server.py -q -p no:cacheprovider
python scripts/smoke_examples.py
```

Expected: all maintained apps render, all flagship views switch without runtime errors, and every declared route returns HTTP/full WebSocket success.

- [ ] **Step 8: Commit**

```text
git add examples/data_pipeline_command_center tests/test_examples.py
git commit -m "feat: consolidate flagship command center"
```

### Task 5: Remove redundant examples and repair documentation

**Files:**
- Remove: nine example directories listed in the approved design.
- Rewrite: `docs/EXAMPLES.md`
- Modify: `DEVELOPMENT.md`
- Modify: `docs/BUILD.md`
- Modify or remove: `docs/GEOMETRIC_UI.md`
- Modify: `docs/LOCAL_DEVELOPMENT.md`
- Modify: `mkdocs.yml`
- Modify: `tests/test_examples.py`

**Interfaces:**
- Consumes: exact six-name manifest from Task 1.
- Produces: no tracked references to deleted examples.

- [ ] **Step 1: Add a failing inventory/reference test**

```python
def test_examples_directory_matches_manifest() -> None:
    declared = {spec.name for spec in load_example_manifest(REPO_ROOT)}
    actual = {path.name for path in EXAMPLES_ROOT.iterdir() if path.is_dir()}
    assert actual == declared

def test_tracked_docs_do_not_reference_removed_examples() -> None:
    removed = {"acme_analytics_command_center", "geometric_signal_lab", "landing_site", "local_playground", "operations_finance_portal", "pipeline_observability_015", "secure_internal_tools", "weather_dashboard", "workspace_studio"}
    text = "\n".join(path.read_text(encoding="utf-8") for path in (REPO_ROOT / "docs").rglob("*.md"))
    assert not any(name in text for name in removed)
```

- [ ] **Step 2: Verify RED**

Run: `python -m pytest tests/test_examples.py -k "matches_manifest or removed_examples" -q -p no:cacheprovider`

Expected: FAIL because nine redundant directories and their documentation references remain.

- [ ] **Step 3: Remove exact redundant directories**

Remove only the directories named in the test. Do not remove any manifest-listed directory, `.worktrees`, branding assets, or packaged frontend assets.

- [ ] **Step 4: Rewrite showcase documentation**

`docs/EXAMPLES.md` must contain one concise section per retained example: purpose, capabilities proven, local command, deployment files, expected auth mode, and its place in the learning path. `DEVELOPMENT.md` must recommend `counter`, `component_studio`, and `data_pipeline_command_center`; all commands must exist in a clean clone.

- [ ] **Step 5: Repair navigation and build docs**

Remove deleted pages from `mkdocs.yml`. Replace geometric-only guidance with links to the component studio and design tokens, or remove the page if no unique supported guidance remains. Update build docs to use a retained deployment example.

- [ ] **Step 6: Verify GREEN**

Run:

```text
python -m pytest tests/test_examples.py -q -p no:cacheprovider
rg "acme_analytics_command_center|geometric_signal_lab|landing_site|local_playground|operations_finance_portal|pipeline_observability_015|secure_internal_tools|weather_dashboard|workspace_studio" README.md DEVELOPMENT.md docs mkdocs.yml tests scripts
python -m mkdocs build --strict -d .site_validation_showcase
```

Expected: tests and docs build pass; `rg` returns no matches.

- [ ] **Step 7: Commit**

```text
git add examples docs DEVELOPMENT.md mkdocs.yml tests/test_examples.py
git commit -m "docs: curate end-to-end showcase examples"
```

### Task 6: CI, security, and release hygiene

**Files:**
- Modify: `.github/workflows/ci.yml`
- Modify: `.github/workflows/security.yml`
- Modify: `pyproject.toml`
- Modify: `docs/STABILITY.md`
- Modify: `docs/CHANGELOG.md`
- Modify: `docs/MIGRATION_GUIDE.md`
- Modify: `SKILL.md`

**Interfaces:**
- CI validates Python 3.10, 3.11, and 3.12 core tests.
- One Python 3.11 integration job owns frontend, docs, bundle-drift, examples, and packaging checks.

- [ ] **Step 1: Write failing workflow metadata tests**

Add packaging tests that parse workflow text and require the Python version matrix, `pip install -e ".[dev]"` before `pip_audit`, frontend bundle drift, and the manifest-driven smoke command.

- [ ] **Step 2: Verify RED**

Run: `python -m pytest tests/test_packaging.py -q -p no:cacheprovider`

Expected: FAIL on the absent Python matrix or project-aware audit installation.

- [ ] **Step 3: Split CI matrix and integration gates**

Add `strategy.matrix.python-version: ["3.10", "3.11", "3.12"]` to a Python job running install, pytest, Ruff, and mypy. Keep Node, frontend build/tests/audit, `git diff --exit-code -- brickflowui/frontend/dist`, example smoke, strict docs, and package build in a Python 3.11 integration job.

- [ ] **Step 4: Audit installed project dependencies**

In `security.yml`, install `pip-audit` and `-e ".[databricks,viz]"` before running `python -m pip_audit`. Do not print environment variables or credentials.

- [ ] **Step 5: Repair metadata and release docs**

Replace the WSGI classifier with ASGI, align support claims to the tested matrix, update changelog/migration notes for the showcase consolidation, and replace stale `brickflowui==0.1.4` examples in `SKILL.md` with the supported `>=0.1.15,<0.3` range.

- [ ] **Step 6: Verify workflows and docs**

Run:

```text
python -m pytest tests/test_packaging.py -q -p no:cacheprovider
python -m mkdocs build --strict -d .site_validation_showcase
git diff --check
```

Expected: all pass.

- [ ] **Step 7: Commit**

```text
git add .github pyproject.toml docs/STABILITY.md docs/CHANGELOG.md docs/MIGRATION_GUIDE.md SKILL.md tests/test_packaging.py
git commit -m "ci: enforce production showcase gates"
```

### Task 7: Browser verification and milestone closeout

**Files:**
- Create: `docs/verification/2026-07-21-showcase-foundation-report.md`
- Modify only if verification finds a reproducible defect: source/test file owning that defect.

**Interfaces:**
- Produces: reproducible evidence for all six examples and the flagship browser flow.

- [ ] **Step 1: Run complete automated verification**

```text
python -m pytest -q -p no:cacheprovider
python scripts/smoke_examples.py
python scripts/generate_component_reference.py
git diff --exit-code -- docs/components/reference
python -m mkdocs build --strict -d .site_validation_showcase
python -m build
python -m twine check dist/*
npm --prefix frontend test -- --run
npm --prefix frontend run lint
npm --prefix frontend run typecheck
npm --prefix frontend audit --audit-level=high
npm --prefix frontend run build
git diff --exit-code -- brickflowui/frontend/dist
git diff --check
```

Expected: zero failures, zero high npm vulnerabilities, no generated drift.

- [ ] **Step 2: Browser-check every retained example**

For each manifest entry, verify initial load, every route, one state-changing interaction, direct-route refresh, reconnect, light/dark mode where available, and zero browser-console errors.

- [ ] **Step 3: Perform flagship responsive and accessibility pass**

At 390x844, 768x1024, 1280x800, and 1440x900 verify no document-level horizontal overflow, readable hierarchy, reachable primary actions, wrapping controls, visible focus, keyboard navigation, modal close/focus restoration, and reduced-motion behavior.

- [ ] **Step 4: Record exact evidence and remaining boundaries**

The report must list commit, environment, commands, pass counts, browser viewport results, console result, and any external Databricks validation still unavailable. Do not infer live workspace behavior from mocks.

- [ ] **Step 5: Commit**

```text
git add docs/verification/2026-07-21-showcase-foundation-report.md
git commit -m "docs: verify showcase foundation"
```

## Plan self-review

- Spec coverage: this plan covers Milestone A and the showcase consolidation portion of the approved specification. Runtime keys, resources, DataGrid, accessible shell, and doctor remain intentionally separated into later implementation plans.
- Placeholder scan: no `TBD`, `TODO`, deferred error-handling instruction, or undefined neighboring interface remains.
- Type consistency: all tasks consume the same `ExampleSpec` and `load_example_manifest` contracts; the flagship retains the existing normalized record field names.
