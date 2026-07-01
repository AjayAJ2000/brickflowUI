# Patch Removal Ordering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Eliminate page-switch protocol errors by making every generated child-removal patch valid when applied sequentially, then publish the verified fix as BrickflowUI 0.1.14.

**Architecture:** Keep the strict frontend patch validator and incremental protocol. Change only Python VDOM child diff ordering: shared children first, surplus removals in descending order, surplus insertions in ascending order. Validate at the unit, WebSocket, browser, package, CI, and registry layers.

**Tech Stack:** Python 3.10+, pytest, FastAPI TestClient WebSockets, TypeScript, Vitest, React, Vite, MkDocs, Hatchling, Twine, GitHub Actions, PyPI trusted publishing.

---

## File Map

- Modify: brickflowui/vdom.py — generate sequentially valid child-list patches.
- Modify: tests/test_vdom.py — protocol ordering and nested-tree regressions.
- Modify: tests/test_app_server.py — real WebSocket navigation regression.
- Modify: frontend/src/runtime/applyPatch.test.ts — client application and defensive-validation regressions.
- Modify: brickflowui/version.py and pyproject.toml — patch release version.
- Modify: docs/CHANGELOG.md and docs/STABILITY.md — release behavior and support statement.
- Modify: active requirements/install snippets where 0.1.13 is the current minimum.
- Create: docs/verification/2026-07-01-navigation-patch-report.md — exact test and release evidence.

### Task 1: Prove the protocol defect with failing tests

**Files:**
- Modify: tests/test_vdom.py
- Modify: tests/test_app_server.py
- Modify: frontend/src/runtime/applyPatch.test.ts

- [ ] **Step 1: Add root and nested removal-order tests**

Add helpers and assertions equivalent to:

    def _texts(count):
        return [VNode(type="Text", props={"value": str(index)}) for index in range(count)]

    def test_diff_removes_surplus_children_from_highest_index_first():
        patches = diff(
            VNode(type="Column", children=_texts(5)),
            VNode(type="Column", children=_texts(1)),
            {},
        )
        assert [patch["path"] for patch in patches if patch["op"] == "remove"] == [
            [4], [3], [2], [1]
        ]

    def test_diff_removes_nested_surplus_children_from_highest_index_first():
        old = VNode(type="Column", children=[VNode(type="Row", children=_texts(5))])
        new = VNode(type="Column", children=[VNode(type="Row", children=_texts(1))])
        patches = diff(old, new, {})
        assert [patch["path"] for patch in patches if patch["op"] == "remove"] == [
            [0, 4], [0, 3], [0, 2], [0, 1]
        ]

Also cover five-to-zero, shared-child prop updates plus removals, and one-to-five insertion ordering.

- [ ] **Step 2: Add the WebSocket navigation regression**

Register a large page and a compact page, connect with path=/large, navigate to /compact, and assert the emitted removal paths are descending:

    with client.websocket_connect("/events?path=/large") as websocket:
        full = websocket.receive_json()
        assert full["type"] == "full"
        websocket.send_json({"type": "navigate", "path": "/compact"})
        patch = websocket.receive_json()

    assert patch["type"] == "patch"
    removals = [item["path"] for item in patch["patches"] if item["op"] == "remove"]
    assert removals == sorted(removals, reverse=True)

Use page VNodes with the same root/container types but different child counts so the bug cannot be hidden by a root replacement.

- [ ] **Step 3: Add frontend patch-sequence coverage**

Add a Vitest case that applies the expected server-compatible removal list:

    const source = {
      type: 'Column',
      props: {},
      children: ['0', '1', '2', '3', '4'].map(leaf),
      key: null,
    }
    const updated = applyPatches(source, [
      { op: 'remove', path: [4] },
      { op: 'remove', path: [3] },
      { op: 'remove', path: [2] },
      { op: 'remove', path: [1] },
    ])
    expect(updated.children.map(child => child.props.value)).toEqual(['0'])

Retain explicit rejection coverage for ascending stale indexes, negative indexes, missing nodes, and genuine out-of-bounds paths.

- [ ] **Step 4: Run targeted tests and verify RED**

Run:

    python -m pytest tests/test_vdom.py tests/test_app_server.py -q -p no:cacheprovider
    npm test -- --run src/runtime/applyPatch.test.ts

Expected: the new Python removal-order and WebSocket assertions fail because paths are currently ascending. Existing frontend defensive tests remain green.

- [ ] **Step 5: Commit only the RED tests**

    git add tests/test_vdom.py tests/test_app_server.py frontend/src/runtime/applyPatch.test.ts
    git commit -m "test: reproduce navigation patch index drift"

### Task 2: Implement sequentially valid patch ordering

**Files:**
- Modify: brickflowui/vdom.py

- [ ] **Step 1: Replace max-length child iteration with three ordered phases**

Use this structure:

    shared_len = min(len(old.children), len(new.children))
    for index in range(shared_len):
        patches.extend(
            diff(old.children[index], new.children[index], handler_registry, path + [index])
        )

    for index in range(len(old.children) - 1, shared_len - 1, -1):
        patches.append({"op": "remove", "path": path + [index]})

    for index in range(shared_len, len(new.children)):
        patches.append({
            "op": "insert",
            "path": path + [index],
            "node": new.children[index].serialize(handler_registry),
        })

- [ ] **Step 2: Run targeted tests and verify GREEN**

    python -m pytest tests/test_vdom.py tests/test_app_server.py -q -p no:cacheprovider
    npm test -- --run src/runtime/applyPatch.test.ts

Expected: all targeted tests pass and the frontend still rejects malformed sequences.

- [ ] **Step 3: Run property-style adversarial coverage**

Add a deterministic pytest parameterization across old/new child counts 0 through 12. For every pair, generate patches, apply their structural operations to a serialized tree in a small test helper, and assert the result matches the serialized new tree. Include nested depth two.

- [ ] **Step 4: Commit the implementation**

    git add brickflowui/vdom.py tests/test_vdom.py
    git commit -m "fix: order child removals for sequential patches"

### Task 3: Prepare patch release 0.1.14

**Files:**
- Modify: brickflowui/version.py
- Modify: pyproject.toml
- Modify: docs/CHANGELOG.md
- Modify: docs/STABILITY.md
- Modify: README.md
- Modify: active example and scaffold requirements files
- Modify: current install snippets in deployment and troubleshooting docs
- Create: docs/verification/2026-07-01-navigation-patch-report.md

- [ ] **Step 1: Update canonical version declarations**

Set both:

    __version__ = "0.1.14"
    version = "0.1.14"

- [ ] **Step 2: Add the 0.1.14 changelog entry**

Document the confirmed root cause, descending-removal invariant, unchanged strict frontend validation, and navigation regression coverage. Keep the historical 0.1.13 entry unchanged.

- [ ] **Step 3: Align active installation guidance**

Update current minimum-version requirements and current installation examples to 0.1.14. Do not rewrite historical 0.1.13 verification reports, roadmap entries, or the named 0.1.13 showcase.

- [ ] **Step 4: Start the verification report with confirmed evidence**

Record the reproduced root cause and the completed targeted-test results. Add later
sections only after their checks run, so the report never contains speculative
success claims or placeholder evidence.

- [ ] **Step 5: Run version and docs tests**

    python -m pytest tests/test_version.py tests/test_docs_generation.py -q -p no:cacheprovider
    python -m mkdocs build --strict --site-dir site-navigation-fix

- [ ] **Step 6: Commit release metadata**

Stage only the intended version/docs/requirements files and commit:

    git commit -m "docs: prepare 0.1.14 patch release"

### Task 4: Senior-level automated and adversarial verification

**Files:**
- Update: docs/verification/2026-07-01-navigation-patch-report.md
- Generated: brickflowui/frontend/dist/*

- [ ] **Step 1: Run complete Python quality gates**

    python -m pytest -q -p no:cacheprovider
    python -m ruff check --no-cache brickflowui tests examples scripts/generate_component_reference.py
    python -m mypy --no-incremental --cache-dir NUL brickflowui

Expected: zero failures and no lint/type errors.

- [ ] **Step 2: Run complete frontend quality gates**

    npm test -- --run
    npm run lint
    npm audit --audit-level=high
    npm run build

Expected: all Vitest files pass, ESLint passes, zero high-severity audit findings, deterministic production bundle builds.

- [ ] **Step 3: Verify generated artifacts and references**

    python scripts/generate_component_reference.py
    git diff --exit-code -- docs/components/reference
    git diff --exit-code -- brickflowui/frontend/dist
    python -m mkdocs build --strict --site-dir site-navigation-fix

If the deterministic frontend build changes its hash, stage the complete new bundle and delete only superseded hashed files.

- [ ] **Step 4: Exercise edge cases**

Run targeted tests for:

- old/new child lengths 0..12
- nested shrink/grow
- shared prop update plus removal
- type replacement adjacent to removals
- repeated large→small→large navigation
- browser Back/Forward after page switches
- reconnect following one intentionally malformed patch in the unit harness
- two simultaneous WebSocket sessions navigating independently

- [ ] **Step 5: Browser-test maintained examples**

Launch and test at least:

- operations_finance_portal
- weather_dashboard
- component_studio
- auth_portal or secure_internal_tools
- one pipeline-oriented example

For each multi-page app, navigate every visible page twice, then exercise browser Back/Forward. Check that page content changes, no Runtime protocol error banner appears, the socket remains connected, and the console contains no uncaught error.

- [ ] **Step 6: Update verification report with exact evidence**

Record command counts, example names/routes, browser observations, known environmental warnings, and any defect found and fixed.

### Task 5: Package and clean-install verification

**Files:**
- Generated and ignored: release-navigation-fix/*
- Update: docs/verification/2026-07-01-navigation-patch-report.md

- [ ] **Step 1: Build and inspect distributions**

    python -m build --outdir release-navigation-fix
    python -m twine check release-navigation-fix/*
    python -m zipfile -l release-navigation-fix/brickflowui-0.1.14-py3-none-any.whl

- [ ] **Step 2: Create a clean environment and install the wheel**

    python -m venv release-navigation-smoke
    release-navigation-smoke\Scripts\python.exe -m pip install release-navigation-fix\brickflowui-0.1.14-py3-none-any.whl
    release-navigation-smoke\Scripts\python.exe -m pip check

- [ ] **Step 3: Smoke test installed package outside the repository**

Confirm version 0.1.14, frontend bundle discovery, HTTP 200 for / and the hashed JavaScript asset, and a TestClient WebSocket large→small navigation sequence with descending removals.

- [ ] **Step 4: Audit installed dependencies and record hashes**

    python -m pip_audit --path release-navigation-smoke\Lib\site-packages
    Get-FileHash -Algorithm SHA256 release-navigation-fix\*

- [ ] **Step 5: Commit final report evidence**

    git add docs/verification/2026-07-01-navigation-patch-report.md
    git commit -m "docs: record 0.1.14 release verification"

### Task 6: Publish branch and merge through guarded CI

**Files:** No new source files.

- [ ] **Step 1: Inspect exact scope**

    git diff origin/main...HEAD --check
    git diff origin/main...HEAD --stat
    git status -sb

Confirm CRLF-only phantom files are not staged.

- [ ] **Step 2: Push and create a ready-for-review PR**

Push codex/fix-patch-removal-order, create a PR to main, and include root cause, protocol invariant, test matrix, browser examples, package hashes, and release intent.

- [ ] **Step 3: Monitor every PR check**

Wait for CI, CodeQL, security audit, and docs checks. If anything fails, inspect logs, fix the root cause, rerun locally, push, and wait again.

- [ ] **Step 4: Merge only when all required checks pass**

Use the repository's normal merge policy. Do not bypass a required review without explicit user authorization.

### Task 7: Release and verify PyPI

**Files:** No source changes after merge.

- [ ] **Step 1: Verify merged main**

Confirm the PR merge commit equals GitHub main, post-merge workflows pass, version files read 0.1.14, and no v0.1.14 tag/release exists.

- [ ] **Step 2: Publish GitHub Release v0.1.14**

Create the release from the exact merged main commit with notes summarizing the protocol fix and verification.

- [ ] **Step 3: Monitor the guarded publish workflow**

Wait for both Run release gates and Publish package distributions to PyPI to succeed.

- [ ] **Step 4: Verify immutable registry evidence**

Confirm:

    https://pypi.org/pypi/brickflowui/0.1.14/json
    https://pypi.org/project/brickflowui/0.1.14/

- [ ] **Step 5: Fresh-install from PyPI and smoke test**

Install brickflowui==0.1.14 into a new clean environment with no local wheel path. Confirm version, dependencies, bundle presence, HTTP asset serving, and WebSocket navigation.

- [ ] **Step 6: Report completion**

Provide PR, merge commit, GitHub Release, workflow, PyPI links, exact artifact hashes, test totals, browser matrix, and any residual known risks. Do not call the release complete until every item above is confirmed.
