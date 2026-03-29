# BricksFlowUI

> Canonical package name: `bricksflowui`
>
> Install with:
>
> ```bash
> pip install bricksflowui
> ```
>
> Import with:
>
> ```python
> import brickflowui as db
> ```
>
> Start here:
> - [Getting Started](./docs/GETTING_STARTED.md)
> - [Build Guide](./docs/BUILD.md)
> - [API Reference](./docs/API_REFERENCE.md)
> - [Theming](./docs/THEMING.md)
> - [Publishing](./docs/PUBLISHING.md)

## Release Notes

- PyPI package name is now `bricksflowui`
- CLI commands supported: `brickflowui` and `bricksflowui`
- Standard Python import remains `brickflowui`
- Source distributions and wheels include bundled frontend assets plus docs/examples

> **Databricks-first, React-style Python UI library** for building composable, production-ready Databricks Apps — without writing a single line of JavaScript.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## What is BricksFlowUI?

BricksFlowUI lets data engineers build beautiful, interactive Databricks Apps in **pure Python**. It ships a pre-built React frontend and communicates over WebSocket, so you get:

- ⚡ **No full-script reruns** — only changed components re-render (unlike Streamlit)
- 🧩 **React-style component model** — composable functions, hooks, one-way data flow
- 🔒 **Databricks-native** — reads `DATABRICKS_APP_PORT`, Unity Catalog helpers, SQL warehouse wrappers
- 🎨 **Beautiful dark theme** — Databricks-inspired design system, no CSS required

---

## Quick Start

```bash
pip install bricksflowui

# Scaffold a new app
brickflowui new my_app
cd my_app

# Run locally
brickflowui dev
# → open http://localhost:8050
```

Or manually:

```python
# app.py
import brickflowui as db

app = db.App(title="My Databricks App")

@app.page("/", title="Home", icon="Home")
def home():
    count, set_count = db.use_state(0)
    return db.Column([
        db.Text("Counter", variant="h1"),
        db.Text(f"Count: {count}", variant="h3"),
        db.Button("Increment", on_click=lambda: set_count(count + 1)),
    ], padding=6)

if __name__ == "__main__":
    app.run()
```

---

## Core Concepts

### Components

Every UI element is a plain Python function returning a `VNode`:

```python
import brickflowui as db

# Layout
db.Column(children, gap=4, padding=6)
db.Row(children, gap=2, justify="between")
db.Grid(children, cols=3, gap=4)
db.Card(children, title="My Card")

# Typography
db.Text("Hello!", variant="h1")   # h1, h2, h3, h4, body, caption, label, code

# Controls
db.Button("Click me", on_click=handler, variant="primary")
db.Input(name="q", label="Search", on_change=setter)
db.Select(name="w", options=[{"label": "A", "value": "a"}], on_change=setter)
db.Checkbox(name="x", label="Enable", on_change=setter)
db.Toggle(name="y", label="Dark mode", on_change=setter)
db.Slider(name="s", min=0, max=100, on_change=setter)

# Data
db.Table(data=rows, columns=[{"key": "id", "label": "ID"}], pagination=20)
db.Badge("Active", color="green")
db.Alert("Something went wrong", type="error")
db.Progress(value=65, max=100)
db.Stat(label="Queries", value="248K", delta="+12%", delta_type="increase")

# Charts
db.AreaChart(data=rows, x_key="date", y_keys=["value"], colors=["#FF3621"])
db.BarChart(data=rows, x_key="category", y_keys=["count"])
db.LineChart(data=rows, x_key="day", y_keys=["metric"])
db.DonutChart(data=rows, value_key="count", label_key="name")

# Navigation
db.Tabs([db.TabItem("Tab A", [db.Text("Content A")]), ...])
db.Sidebar([db.NavItem("Home", "/", icon="Home"), ...], brand_name="My App")
db.Modal(visible=True, title="Confirm", children=[...], on_close=handler)

# Forms
db.Form(action="/api/submit", success_redirect="/", children=[
    db.Input(name="username", label="Username"),
    db.Button("Submit", html_type="submit"),
])

# Databricks-specific
db.CatalogBrowser(on_select=handler)
db.WarehouseSelector(on_select=handler)
db.JobTrigger(job_id="123", label="Run Pipeline")
```

### State (Hooks)

```python
@app.page("/")
def my_page():
    count, set_count = db.use_state(0)          # local state
    data = db.use_memo(load_data, deps=[count])  # memoized compute
    db.use_effect(lambda: print("mounted"), [])  # side effects
    theme = db.use_context("theme")              # session context

    return db.Button(str(count), on_click=lambda: set_count(count + 1))
```

### Multi-page Apps

```python
app = db.App(title="Ops Hub")

@app.page("/", title="Dashboard", icon="LayoutDashboard")
def dashboard(): ...

@app.page("/tables", title="Tables", icon="Database")
def tables(): ...

@app.page("/settings", title="Settings", icon="Settings")
def settings(): ...
```

### Auth And Access Control

```python
import brickflowui as db

app = db.App(
    title="Ops Hub",
    auth_mode="hybrid",  # "app", "user", or "hybrid"
    auth_provider=db.HeaderAuthProvider(),
)

@app.page("/", title="Home")
def home():
    principal = db.current_principal()
    return db.Text(f"Hello {principal.display_name or principal.subject}")

@app.page("/admin", title="Admin", access="user", roles=["admin"])
def admin():
    user = db.require_role("admin")
    return db.Text(f"Welcome, {user.subject}")

@app.route("/api/profile", methods=["GET"], access="user")
async def profile():
    user = db.require_auth()
    return {"user": user.subject, "roles": list(user.roles)}
```

`access` supports:

- `public` â€” anyone can access it
- `authenticated` â€” any authenticated principal
- `user` â€” requires a signed-in user identity
- `app` â€” restricted to the shared application identity

### Branding And Themes

```python
app = db.App(theme="branding.yaml")
```

Example `branding.yaml`:

```yaml
branding:
  title: "Acme Ops Portal"
  logo: "/static/acme-logo.svg"
  favicon: "/static/acme-favicon.ico"

colors:
  primary: "#FF5F2E"
  primary_hover: "#D9481C"
  background: "#F7F7F5"
  surface: "#FFFFFF"
  text: "#18181B"
  text_muted: "#71717A"
  border: "#E4E4E7"

typography:
  font_family: "'IBM Plex Sans', sans-serif"
  base_size: "15px"

spacing:
  unit: "6px"

borders:
  radius: "14px"
```

Supported theme model sections:

- `branding`: `title`, `logo`, `favicon`
- `colors`: `primary`, `primary_hover`, `background`, `surface`, `text`, `text_muted`, `border`, `success`, `warning`, `error`, `link`
- `typography`: `font_family`, `font_mono`, `base_size`
- `spacing`: `unit`
- `borders`: `radius`

You can also keep using the lower-level internal keys like `primary-hover`, `bg`, `text-muted`, `sans`, and `base-size` if you prefer.

### Custom API Routes

```python
@app.route("/api/submit", methods=["POST"])
async def submit_handler():
    from fastapi.responses import JSONResponse
    return JSONResponse({"status": "ok"})
```

---

## Databricks Integration

### SQL Queries

```python
from brickflowui.databricks import sql

# Returns a pandas DataFrame
df = sql.query("SELECT * FROM catalog.schema.table LIMIT 100")

# Returns list[dict] (for db.Table component)
rows = sql.query_to_records("SELECT id, name FROM my_table")
return db.Table(data=rows)
```

Set environment variables (or use `app.yaml`):

```env
DATABRICKS_HOST=https://adb-xxx.azuredatabricks.net
DATABRICKS_TOKEN=dapiXXXXXXXX
DATABRICKS_WAREHOUSE_ID=your-warehouse-id
```

### Unity Catalog

```python
from brickflowui.databricks import uc

catalogs = uc.list_catalogs()
schemas  = uc.list_schemas("main")
tables   = uc.list_tables("main", "gold")
rows     = uc.get_table("main", "gold", "fact_orders", limit=50)
```

---

## Deploying to Databricks Apps

### `app.yaml`

```yaml
command:
  - python
  - app.py

env:
  - name: DATABRICKS_WAREHOUSE_ID
    value: your-warehouse-id
```

Then in the Databricks workspace:
1. Create a new Databricks App
2. Upload your project as a ZIP (include `app.py`, `app.yaml`, `requirements.txt`)
3. The app binds to `DATABRICKS_APP_PORT` automatically

### `requirements.txt`

```text
bricksflowui>=0.1.0
# bricksflowui[databricks]  # for SQL + Unity Catalog
```

---

## CLI Reference

| Command | Description |
|---------|-------------|
| `brickflowui new <name>` | Scaffold a new app |
| `brickflowui dev` | Run local dev server (hot reload) |

---

## Project Structure

```text
brickflowui/
├── __init__.py          # Public API
├── app.py               # App class
├── vdom.py              # Virtual DOM + diff algorithm
├── state.py             # Hooks (use_state, use_effect, use_memo)
├── components.py        # All component primitives
├── server.py            # FastAPI ASGI + WebSocket server
├── cli/
│   ├── main.py          # CLI (typer)
│   └── templates/       # App scaffolding templates
├── databricks/
│   ├── env.py           # DATABRICKS_* env helpers
│   ├── sql.py           # SQL connector wrappers
│   └── uc.py            # Unity Catalog helpers
└── frontend/
    └── dist/            # Pre-built React bundle (served automatically)

examples/
├── counter/             # Minimal Counter example
└── demo_app/            # Full multi-page dashboard demo
    ├── app.py
    ├── app.yaml
    └── requirements.txt
```

---

## Architecture

```
Python App (app.py)
    │
    │  Component tree (VNode)
    ▼
BrickflowUI Runtime
    │  FastAPI ASGI Server
    │  WS /events   ──── JSON patches ────▶  React Frontend
    │  GET /         ◀─── HTML shell ──────
    │  GET /static/* ◀─── React bundle ────
    │
    ▼
Databricks Runtime
    (DATABRICKS_APP_PORT, SQL warehouse, Unity Catalog)
```

---

## License

MIT © BrickflowUI Contributors
