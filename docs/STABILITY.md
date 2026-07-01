# Stability Contract

BrickflowUI `0.1.14` is an alpha framework with a tested core-runtime baseline. “Stable” here means that the supported verification gates pass and there are no known reproducible core defects at release time. It is not a claim that undiscovered defects are impossible, nor is it a security or regulatory certification.

## Supported baseline

- Python 3.10, 3.11, and 3.12 are declared package targets.
- The backend is FastAPI/Starlette and the browser runtime is the packaged React production build.
- Published wheels must contain `brickflowui/frontend/dist/index.html` and its referenced hashed assets.
- A source checkout must run `npm ci` and `npm run build` in `frontend/` before it can serve an application.
- If the frontend bundle is missing, BrickflowUI returns an actionable HTTP 503 diagnostic. It does not expose the old incomplete fallback renderer.

## Release gates

Run from the repository root:

```powershell
python -m pytest -q
python scripts/generate_component_reference.py
git diff --exit-code -- docs/components/reference
python -m mkdocs build --strict
python -m build
```

Run from `frontend/`:

```powershell
npm ci
npm test -- --run
npm run lint
npm run build
npm audit --audit-level=high
```

The release is not ready when a test, lint, build, documentation-drift, package-content, or high-severity runtime dependency gate fails.

## Browser verification

A representative multi-page application must pass:

- initial page load and WebSocket connection;
- event dispatch and incremental state patching;
- direct deep links;
- repeated user navigation and browser Back/Forward operations;
- reconnect after a forced WebSocket closure;
- table sorting, pagination, and CSV export;
- standalone and table progress indicators with proportional width and a non-transparent computed color;
- chat typing, IME composition, and submission;
- light/dark theme switching;
- desktop and narrow viewport smoke tests;
- a console check with no uncaught exceptions.

## Security boundaries

BrickflowUI escapes application titles and favicon attributes, embeds loading configuration as inert JSON data, prevents configured CSS from terminating its style element, validates scaffold targets, validates WebSocket origins, requires CSRF tokens for browser-like unsafe HTTP requests, and neutralizes spreadsheet formulas in CSV exports.

The runtime accepts event handlers from only the current and immediately previous render generations. This narrow compatibility window preserves ordered browser events such as ChatInput's final change plus submit without retaining stale handlers indefinitely.

Theme files and application configuration are trusted developer inputs. Authentication supports both user identity and shared application identity; deployment owners must configure the mode and provider appropriate for their environment.

## Known capability boundaries

`CatalogBrowser`, `WarehouseSelector`, and `JobTrigger` are present in the Python component API but do not yet have complete frontend and backend data contracts. They must not be described as production-ready until the dedicated Databricks integration plan and browser tests pass.

Formal load limits, configurable idle-session policy, deployment observability, and an actual Databricks Apps environment test belong to the production-lifecycle validation phase. The WebSocket handler cleans session state in its `finally` path, but this does not substitute for measured concurrency and failure testing.

## Reporting a regression

Open a GitHub issue with the BrickflowUI version, Python and Node versions, operating system, minimal reproduction, complete traceback or browser-console error, and whether the failure occurs from source or an installed wheel. A regression fix must include a test that fails before the fix and passes afterward.
