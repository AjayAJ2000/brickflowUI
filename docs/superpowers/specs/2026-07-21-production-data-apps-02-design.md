# BrickflowUI 0.2: Production Data Apps Design

**Date:** 2026-07-21  
**Status:** Approved for implementation planning  
**Baseline:** BrickflowUI 0.1.15 (`main` at `4b084de`)  
**Product position:** Databricks-first operational applications authored in Python

## 1. Product thesis

BrickflowUI 0.2 will stop competing on the size of its component catalog. Its product promise will be:

> Build secure, polished, production-oriented Databricks data applications in Python without maintaining a separate frontend codebase.

The release must make that promise credible in three ways:

1. The server-driven runtime preserves identity and interaction state through real application updates.
2. The framework provides first-class primitives for asynchronous data, operational tables, accessible navigation, and application feedback.
3. A small set of excellent examples proves the complete path from local mock data to authenticated Databricks workflows.

The release is not a general-purpose website builder, notebook replacement, or a collection of decorative dashboard widgets.

## 2. Success criteria

BrickflowUI 0.2 is successful when:

- A new developer can install the package, run the quickstart, and understand the framework within ten minutes.
- A data team can build a query-to-grid-to-detail-to-action workflow without inventing loading, error, selection, or mutation infrastructure.
- Reordering keyed components does not transfer local state, focus, selection, or handler identity to another component.
- The canonical command center works with local mock data and the same public interface used for Databricks SQL.
- Every retained example passes import, render, HTTP, WebSocket, interaction, responsive-layout, browser-console, and deployment-manifest checks.
- Keyboard-only users can operate the app shell, dialogs, tabs, forms, and the primary DataGrid workflows.
- `brickflowui doctor` detects missing runtime assets and common deployment mistakes before release or deployment.
- The repository can be cloned and verified using tracked commands without relying on ignored local scripts.

## 3. Delivery structure

This program is divided into independently testable milestones. Each milestone must leave the repository releasable and must use failing tests before behavior changes.

### Milestone A: Repository and showcase foundation

- Start from the 0.1.15 `main` branch.
- Preserve active Git worktrees, branding source files, the frontend lockfile, generated component references, and wheel-embedded frontend assets.
- Remove only verified generated caches, stale root build artifacts, and abandoned temporary test directories.
- Remove the broad `scripts/` ignore rule.
- Track the example smoke runner and local cleanup utility referenced by development documentation.
- Align CI, security auditing, version claims, changelog, migration guide, and package metadata.
- Establish the maintained-example manifest used by tests, documentation, and smoke tooling.

### Milestone B: Keyed runtime and protocol confidence

- Make `VNode.key` participate in child reconciliation.
- Detect duplicate sibling keys and return an actionable development error.
- Preserve index-based reconciliation for fully unkeyed legacy trees.
- Reject mixed keyed and unkeyed siblings when reordering would be ambiguous.
- Give event handlers stable identities for a stable session, node key/path, and event name.
- Keep a bounded compatibility window for events sent immediately before a rerender.
- Add a protocol version to full-tree and patch messages.
- On protocol or patch mismatch, request a fresh full tree without corrupting client state.
- Record optional development timings for render, diff, payload size, event execution, and patch application.

### Milestone C: Accessible adaptive application shell

Add the following public components:

- `AppShell`: responsive navigation, main-content landmark, skip link, optional header and utility rail.
- `PageHeader`: title, description, breadcrumbs, status, and actions with predictable responsive collapse.
- `Toolbar`: grouped filters and actions with overflow behavior.
- `IconButton`: accessible icon action requiring an explicit label.
- `SegmentedControl`: compact single-selection control with keyboard support.
- `Skeleton`: content-aware loading placeholder honoring reduced motion.
- `ErrorState`: actionable error presentation with retry and correlation-ID support.

Existing dialogs, drawers, tabs, selects, inputs, and live feedback will gain correct semantics, focus management, Escape behavior, label association, keyboard navigation, and assistive-technology announcements. Existing APIs remain compatible unless they currently expose a non-functional promise.

### Milestone D: Resource and mutation model

Add a server-side resource abstraction suitable for synchronous and asynchronous data sources.

The primary API will be:

```python
resource = db.use_resource(
    loader,
    key=("pipeline-metrics", catalog, schema),
    stale_time=30,
)
```

The returned resource exposes:

- `data`
- `loading`
- `refreshing`
- `error`
- `updated_at`
- `refresh()`
- `retry()`

The runtime will:

- deduplicate in-flight work per session and resource key;
- support sync and async loaders;
- discard stale completions after dependencies change or a session closes;
- bound cached resources by count and age;
- keep raw exceptions in server logs while exposing safe public messages and correlation IDs;
- trigger rerenders when resource state changes;
- clean up tasks when a session disconnects.

Mutation support will provide pending, success, and failure states without introducing a general client-side cache. Optimistic updates are deferred until the base resource lifecycle is stable and tested.

### Milestone E: DataGrid

`DataGrid` will be a new component. The existing `Table` remains supported for small, read-only datasets.

The Python contract will include:

- typed column definitions;
- required stable `row_id` configuration;
- client or server data modes;
- sorting and filtering state;
- pagination state and total row count;
- single and multiple selection;
- row actions;
- optional detail-drawer content;
- loading, empty, error, and permission-denied states;
- controlled editing for explicitly editable columns;
- event payloads containing stable row IDs rather than page indexes.

The frontend will provide:

- keyboard-operable headers, rows, selection, pagination, and actions;
- sticky header and optional sticky columns;
- responsive density and horizontal overflow containment;
- stable row keys through sorting and pagination;
- accessible sort and selection announcements;
- virtualization only after the non-virtualized server-pagination contract is correct.

The first release will not include spreadsheet formulas, arbitrary cell render plugins, grouped pivot tables, or Excel-scale local datasets.

### Milestone F: Developer confidence tooling

Add `brickflowui doctor` with checks for:

- Python and BrickflowUI versions;
- packaged frontend index and referenced assets;
- application and deployment manifests;
- supported authentication mode and required forwarded headers;
- origin, trusted-host, CSRF, and embed configuration;
- Databricks host, warehouse, and authorization readiness without printing secrets;
- example manifest completeness;
- stale generated documentation or frontend bundles in a source checkout.

Development mode will display a structured error overlay containing a safe message, correlation ID, phase, component/event context when available, and recovery action. Production mode continues to show concise safe feedback.

The package will add `py.typed` and strengthen public type contracts incrementally around the new APIs. This milestone does not require rewriting every legacy component signature.

## 4. Showcase strategy

The examples directory will become a product showroom, not an archive.

### Retained examples

1. **`counter`**
   - Purpose: ten-minute quickstart and state/event fundamentals.
   - Maximum size: one focused application file plus deployment manifests.

2. **`component_studio`**
   - Purpose: authoritative interactive catalog of supported components and states.
   - It must demonstrate loading, empty, error, disabled, responsive, dark, and keyboard states.

3. **`data_pipeline_command_center`**
   - Purpose: flagship production data application.
   - It will absorb the best operational flow from the earlier pipeline showcase.
   - It will demonstrate `AppShell`, `PageHeader`, `Toolbar`, `use_resource`, `DataGrid`, detail drawer, job action, audit feedback, mock/Databricks adapters, and responsive design.

4. **`clinical_trial_command_center`**
   - Purpose: governed, role-aware, regulated-industry workflow.
   - It will demonstrate authenticated data access, restricted actions, Plotly integration, and traceable operational feedback.

5. **`auth_portal`**
   - Purpose: authentication, session, role, API, and access-denied reference.
   - Repository path manipulation will be removed; the example must run against an installed package.

6. **`chatbot_workspace`**
   - Purpose: assistant workspace with composition-safe input, pending states, errors, citations/metadata slots, and multi-turn layout.

### Removed or consolidated examples

Nine explicitly approved overlapping examples will be deleted after unique, tested capabilities are migrated. The maintained manifest is the authoritative inventory.

Already-removed legacy examples remain removed. Documentation links and tests must be updated in the same change that removes an example.

### Visual quality bar

The two command centers and chatbot workspace must look intentionally designed rather than template-generated.

- Use one coherent product design system based on BrickflowUI tokens.
- Favor application hierarchy, whitespace, typography, and dense operational utility over decorative cards.
- Avoid repeated three-card layouts, unnecessary gradients, excessive pills, fake metrics, and unsupported claims.
- Provide meaningful responsive layouts at 390, 768, 1280, and 1440 CSS pixels.
- Support light and dark modes without section-level theme switching.
- Use motion only for state transitions and feedback, with reduced-motion fallbacks.
- Use real domain-shaped mock records and clearly label simulated actions.
- Include empty, loading, error, disconnected, permission-denied, and success states.
- Keep primary navigation on one desktop line and fully keyboard-operable.

The flagship command center is the release demo and must receive browser-based visual review before 0.2 can ship.

## 5. Data flow

```text
Python page
  -> use_resource loader
  -> session resource registry
  -> normalized records / safe error state
  -> keyed VDOM
  -> versioned full tree or patches
  -> React renderer
  -> DataGrid / AppShell interaction
  -> stable event ID + row/resource identity
  -> Python handler or mutation
  -> resource refresh
  -> minimal keyed patch
```

Credentials, SDK clients, SQL connections, and raw exceptions never enter VDOM props or browser messages.

## 6. Compatibility and migration

- Existing unkeyed component trees continue to reconcile by position.
- Existing `Table` remains available and documented as a small-data component.
- Existing hooks remain supported.
- Stable protocol additions are backward-compatible inside the 0.2 package because frontend and backend assets ship together.
- Non-functional props such as unsupported table editing will either be implemented through `DataGrid` or documented and deprecated rather than silently accepted.
- Removed examples are not public Python APIs, but their documentation links and deployment references must be migrated atomically.

## 7. Error handling and observability

- Server logs retain private tracebacks with correlation IDs.
- Browser errors contain safe messages, context category, recovery action, and the correlation ID.
- Failed resource loads retain previous successful data only when explicitly configured.
- Failed mutations never silently report success.
- WebSocket reconnects preserve browser-visible routing and request a fresh tree when protocol state is uncertain.
- Development timing diagnostics are opt-in and bounded; they do not record data values or credentials.

## 8. Testing and release gates

### Runtime

- Unit tests for keyed insert, remove, reorder, duplicate keys, mixed keys, nested props, and legacy unkeyed behavior.
- Red/green verification that tests fail against positional reconciliation.
- Stable handler identity and stale-event compatibility tests.
- Protocol mismatch and full-tree recovery tests.

### Resource model

- Sync and async success, refresh, retry, dependency change, stale completion, cancellation, eviction, and safe error tests.
- Multi-session isolation tests.
- Databricks adapter tests with injected providers and no live secrets.

### Components

- Python serialization tests for every new component and event contract.
- React behavior tests covering keyboard and accessibility semantics.
- DataGrid client and server mode tests using stable row IDs.

### Examples

- Compile/import checks.
- Full render and JSON serialization for every registered page.
- HTTP and WebSocket startup checks.
- Automated interaction flows for each maintained example.
- Manifest and dependency validation.
- Browser verification at defined viewports with zero console errors and no horizontal overflow.

### Repository and packaging

- Python 3.10, 3.11, and 3.12 CI matrix or an explicitly narrowed support claim.
- Frontend tests, lint, typecheck, audit, production build, and committed-bundle drift check.
- Strict documentation build and generated-reference drift check.
- Wheel/sdist build, metadata check, isolated installation, and installed-wheel browser smoke.
- `brickflowui doctor` must pass against the canonical example before release.

## 9. Non-goals for 0.2

- General-purpose React component plugins.
- A hosted BrickflowUI cloud service.
- A database ORM or migration system.
- Spreadsheet or notebook compatibility layers.
- Arbitrary browser-side JavaScript execution.
- A larger chart catalog.
- Full offline operation.
- Formal security certification or unverified claims about live Databricks production behavior.

## 10. Release narrative

BrickflowUI 0.2 will be presented as a focused step from Python dashboard prototype to governed operational data application:

1. Connect safely to Databricks resources.
2. Load data through a consistent resource lifecycle.
3. Explore and act through an accessible production DataGrid.
4. Preserve application state through keyed updates.
5. Diagnose deployment readiness before shipping.
6. Learn the complete pattern from a small, verified showcase collection.

The release will prioritize demonstrated quality over feature count. No capability is considered part of the pitch until it is exercised by a maintained example and covered by automated verification.
