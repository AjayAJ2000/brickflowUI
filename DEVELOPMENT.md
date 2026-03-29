# BrickflowUI — Development Notes

## Building the frontend

```bash
cd frontend
npm install
npm run build
# → outputs to brickflowui/frontend/dist/
```

## Running locally (development)

```bash
# Install Python package in editable mode
pip install -e ".[dev]"

# Run the counter example
python examples/counter/app.py

# Or the full demo
python examples/demo_app/app.py
# → http://localhost:8050
```

## CLI development

```bash
brickflowui --help
brickflowui new test_app
brickflowui dev
```

## Frontend development (with hot reload)

```bash
# Terminal 1: start the Python backend
python examples/demo_app/app.py

# Terminal 2: start the Vite dev server (auto-proxies /events to backend)
cd frontend
npm run dev
# → http://localhost:5173
```

## Environment variables

See `brickflowui/cli/templates/default/.env.example`

## Package structure

```
brickflowui/                     Python package
├── __init__.py                  Public API
├── app.py                       App class
├── vdom.py                      VNode + diff
├── state.py                     Hooks
├── components.py                UI primitives
├── server.py                    ASGI server
├── cli/
│   ├── main.py                  CLI
│   └── templates/default/       Scaffolding template
├── databricks/
│   ├── env.py                   Databricks env helpers
│   ├── sql.py                   SQL connector wrappers
│   └── uc.py                    Unity Catalog helpers
└── frontend/dist/               Pre-built React bundle

frontend/                        React source (for maintainers)
├── src/
│   ├── main.tsx                 Entry point
│   ├── App.tsx                  WebSocket client + state
│   ├── Renderer.tsx             VNode → React renderer
│   ├── types.ts                 Wire protocol types
│   └── theme.css                Databricks design system
├── package.json
└── vite.config.ts

examples/
├── counter/app.py               Minimal example
└── demo_app/app.py              Full multi-page demo
```
# Development Guide

## Build right away

From the repo root:

```bash
pip install -e ".[dev]"
python -m pytest -q
```

Run an app:

```bash
cd examples/auth_portal
python app.py
```

Or:

```bash
cd examples/operations_finance_portal
python app.py
```

Default URL:

```text
http://127.0.0.1:8050
```

Use a different port when needed:

```bash
# PowerShell
$env:DATABRICKS_APP_PORT=8061
python app.py
```

See `docs/BUILD.md` for the full local build and publish flow.
