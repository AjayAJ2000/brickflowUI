"""
BrickflowUI Demo App — multi-page showcase.

Pages:
  /           Dashboard with KPI stats and charts
  /tables     Unity Catalog table browser
  /pipelines  Pipeline monitoring (mock data)
  /mlflow     MLflow experiment viewer (mock data)
  /settings   App settings form
  /login      Authentication demo

Run locally: python app.py
"""

from __future__ import annotations
import random
from datetime import datetime, timedelta

import brickflowui as db

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = db.App(
    title="Databricks Ops Hub",
    theme_color="#FF3621",
)

# ---------------------------------------------------------------------------
# Mock data generators
# ---------------------------------------------------------------------------

def _mock_metrics():
    return [
        {"day": (datetime.now() - timedelta(days=i)).strftime("%b %d"), "queries": random.randint(300, 900), "latency_ms": random.randint(40, 200)}
        for i in range(14, -1, -1)
    ]

def _mock_jobs():
    statuses = ["Succeeded", "Succeeded", "Succeeded", "Running", "Failed", "Pending"]
    return [
        {
            "job_id": f"job_{1000 + i}",
            "name": f"ETL Pipeline {['Bronze → Silver', 'Silver → Gold', 'Feature Store Refresh', 'Model Training', 'Report Export'][i % 5]}",
            "status": random.choice(statuses),
            "duration_s": random.randint(30, 3600),
            "started_at": (datetime.now() - timedelta(minutes=random.randint(5, 120))).strftime("%H:%M"),
        }
        for i in range(10)
    ]

def _mock_tables():
    schemas = ["bronze", "silver", "gold", "features"]
    return [
        {
            "catalog": "main",
            "schema": random.choice(schemas),
            "table": f"fact_{['orders', 'events', 'sessions', 'clicks', 'signups'][i % 5]}",
            "rows": f"{random.randint(1, 999):,}M",
            "size_gb": f"{random.uniform(0.5, 250):.1f}",
            "last_modified": (datetime.now() - timedelta(hours=random.randint(1, 72))).strftime("%Y-%m-%d %H:%M"),
        }
        for i in range(12)
    ]

def _mock_experiments():
    return [
        {
            "run_id": f"run_{i:04d}",
            "model": ["XGBoost", "LightGBM", "Random Forest", "Neural Net", "Logistic Reg"][i % 5],
            "accuracy": f"{random.uniform(0.82, 0.97):.4f}",
            "f1": f"{random.uniform(0.80, 0.96):.4f}",
            "status": random.choice(["FINISHED", "FINISHED", "RUNNING", "FAILED"]),
            "duration_min": random.randint(2, 90),
        }
        for i in range(15)
    ]

# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

@app.page("/", title="Dashboard", icon="LayoutDashboard")
def dashboard_page():
    time_range, set_time_range = db.use_state("7d")
    metrics = _mock_metrics()

    return db.Column([
        # ── Header
        db.Row([
            db.Column([
                db.Text("Operations Dashboard", variant="h1"),
                db.Text("Real-time data platform health overview", muted=True),
            ]),
            db.Row([
                db.Button("7d", on_click=lambda: set_time_range("7d"),
                          variant="primary" if time_range == "7d" else "secondary"),
                db.Button("30d", on_click=lambda: set_time_range("30d"),
                          variant="primary" if time_range == "30d" else "secondary"),
            ], gap=1),
        ], justify="between"),

        db.Divider(),

        # ── KPI Stats
        db.Grid([
            db.Card([db.Stat("Total Queries", "247,831", "+12.4%", "increase", "Activity")], bordered=True),
            db.Card([db.Stat("Avg Latency", "84 ms", "-8.2%", "decrease", "Clock")], bordered=True),
            db.Card([db.Stat("Active Warehouses", "6", "+2", "increase", "Server")], bordered=True),
            db.Card([db.Stat("Failed Jobs", "3", "+1", "increase", "AlertTriangle")], bordered=True),
        ], cols=4, gap=4),

        # ── Charts row
        db.Grid([
            db.Card([
                db.AreaChart(
                    data=metrics,
                    x_key="day",
                    y_keys=["queries"],
                    title="Query Volume (last 15 days)",
                    colors=["#FF3621"],
                    height=260,
                ),
            ]),
            db.Card([
                db.LineChart(
                    data=metrics,
                    x_key="day",
                    y_keys=["latency_ms"],
                    title="Avg Latency (ms)",
                    height=260,
                ),
            ]),
        ], cols=2, gap=4),

        # ── Recent Jobs
        db.Card(
            title="Recent Job Runs",
            children=[
                db.Table(
                    data=_mock_jobs()[:5],
                    columns=[
                        {"key": "name", "label": "Job Name", "sortable": True},
                        {"key": "status", "label": "Status", "sortable": True},
                        {"key": "duration_s", "label": "Duration (s)", "sortable": True},
                        {"key": "started_at", "label": "Started At"},
                    ],
                    pagination=5,
                ),
            ],
        ),
    ], padding=6, gap=6)


@app.page("/tables", title="Table Browser", icon="Database")
def tables_page():
    selected_catalog, set_catalog = db.use_state("main")
    selected_schema, set_schema = db.use_state(None)
    search, set_search = db.use_state("")

    catalogs = ["main", "hive_metastore", "external_data"]
    schemas = ["bronze", "silver", "gold", "features", "ml"]
    all_tables = _mock_tables()

    filtered = [
        t for t in all_tables
        if (not selected_schema or t["schema"] == selected_schema)
        and (not search or search.lower() in t["table"].lower())
    ]

    return db.Column([
        db.Text("Unity Catalog Browser", variant="h1"),
        db.Text("Browse and inspect tables across your Lakehouse.", muted=True),
        db.Divider(),

        # Filters
        db.Row([
            db.Select(
                name="catalog",
                label="Catalog",
                options=[{"label": c, "value": c} for c in catalogs],
                value=selected_catalog,
                on_change=set_catalog,
            ),
            db.Select(
                name="schema",
                label="Schema",
                options=[{"label": "All Schemas", "value": ""}] +
                        [{"label": s, "value": s} for s in schemas],
                value=selected_schema or "",
                on_change=lambda v: set_schema(v or None),
            ),
            db.Input(
                name="search",
                label="Search tables",
                placeholder="Filter by name...",
                value=search,
                on_change=set_search,
            ),
        ], gap=4, align="end"),

        db.Card([
            db.Row([
                db.Text(f"{len(filtered)} tables found", muted=True),
                db.Badge(f"{selected_catalog}", color="blue"),
                *([] if not selected_schema else [db.Badge(selected_schema, color="purple")]),
            ], justify="between"),
            db.Spacer(2),
            db.Table(
                data=filtered,
                columns=[
                    {"key": "schema", "label": "Schema", "sortable": True},
                    {"key": "table", "label": "Table Name", "sortable": True},
                    {"key": "rows", "label": "Row Count"},
                    {"key": "size_gb", "label": "Size (GB)", "sortable": True},
                    {"key": "last_modified", "label": "Last Modified", "sortable": True},
                ],
                pagination=10,
            ),
        ]),
    ], padding=6, gap=4)


@app.page("/pipelines", title="Pipelines", icon="GitBranch")
def pipelines_page():
    refresh, set_refresh = db.use_state(0)
    jobs = _mock_jobs()

    def _status_badge(status: str):
        color_map = {"Succeeded": "green", "Running": "blue", "Failed": "red", "Pending": "yellow"}
        return db.Badge(status, color=color_map.get(status, "gray"))

    running = [j for j in jobs if j["status"] == "Running"]
    failed = [j for j in jobs if j["status"] == "Failed"]

    return db.Column([
        db.Row([
            db.Column([
                db.Text("Pipeline Monitor", variant="h1"),
                db.Text("Track all Databricks Job runs in real-time", muted=True),
            ]),
            db.Button("↻ Refresh", on_click=lambda: set_refresh(refresh + 1), variant="secondary"),
        ], justify="between"),
        db.Divider(),

        db.Grid([
            db.Card([db.Stat("Running", str(len(running)), icon="PlayCircle")], bordered=True),
            db.Card([db.Stat("Succeeded", str(len([j for j in jobs if j["status"] == "Succeeded"])), icon="CheckCircle")], bordered=True),
            db.Card([db.Stat("Failed", str(len(failed)), icon="XCircle")], bordered=True),
            db.Card([db.Stat("Pending", str(len([j for j in jobs if j["status"] == "Pending"])), icon="Clock")], bordered=True),
        ], cols=4, gap=4),

        *([db.Alert(f"{len(failed)} job(s) failed — check logs below.", type="error")] if failed else []),

        db.Card(
            title=f"All Jobs (refresh #{refresh})",
            children=[
                db.Table(
                    data=jobs,
                    columns=[
                        {"key": "job_id", "label": "Job ID"},
                        {"key": "name", "label": "Name", "sortable": True},
                        {"key": "status", "label": "Status", "sortable": True},
                        {"key": "duration_s", "label": "Duration (s)", "sortable": True},
                        {"key": "started_at", "label": "Started"},
                    ],
                    pagination=10,
                ),
            ],
        ),
    ], padding=6, gap=4)


@app.page("/mlflow", title="MLflow", icon="FlaskConical")
def mlflow_page():
    sort_by, set_sort_by = db.use_state("accuracy")
    show_only_finished, set_show_only_finished = db.use_state(False)

    experiments = _mock_experiments()
    if show_only_finished:
        experiments = [e for e in experiments if e["status"] == "FINISHED"]

    best = max((e for e in experiments if e["status"] == "FINISHED"), key=lambda e: float(e["accuracy"]), default=None)

    return db.Column([
        db.Text("MLflow Experiment Explorer", variant="h1"),
        db.Text("Compare model runs, metrics, and artifacts across experiments.", muted=True),
        db.Divider(),

        *(
            [db.Card([
                db.Row([
                    db.Column([
                        db.Badge("Best Model", color="green"),
                        db.Text(f"{best['model']} — {best['accuracy']} accuracy", variant="h3"),
                    ]),
                    db.Stat("F1 Score", best["f1"], icon="Target"),
                ], justify="between"),
            ])]
            if best else []
        ),

        db.Row([
            db.Select(
                name="sort_by",
                label="Sort by",
                options=[{"label": "Accuracy", "value": "accuracy"}, {"label": "F1 Score", "value": "f1"}, {"label": "Duration", "value": "duration_min"}],
                value=sort_by,
                on_change=set_sort_by,
            ),
            db.Toggle(
                name="only_finished",
                label="Show finished runs only",
                checked=show_only_finished,
                on_change=set_show_only_finished,
            ),
        ], gap=4, align="end"),

        db.Grid([
            db.Card([
                db.DonutChart(
                    data=[{"label": "XGBoost", "value": 5}, {"label": "LightGBM", "value": 4},
                          {"label": "Random Forest", "value": 3}, {"label": "Neural Net", "value": 2}, {"label": "Logistic Reg", "value": 1}],
                    title="Runs by Model Type",
                    height=240,
                ),
            ]),
            db.Card([
                db.BarChart(
                    data=experiments[:8],
                    x_key="run_id",
                    y_keys=["accuracy"],
                    title="Accuracy by Run",
                    height=240,
                ),
            ]),
        ], cols=2, gap=4),

        db.Card(
            title="All Runs",
            children=[
                db.Table(
                    data=sorted(experiments, key=lambda e: float(e[sort_by]) if sort_by in ("accuracy", "f1") else e[sort_by], reverse=True),
                    pagination=10,
                ),
            ],
        ),
    ], padding=6, gap=4)


@app.page("/settings", title="Settings", icon="Settings")
def settings_page():
    saved, set_saved = db.use_state(False)
    warehouse_id, set_warehouse_id = db.use_state("")
    volume_uri, set_volume_uri = db.use_state("")
    dark_mode, set_dark_mode = db.use_state(True)
    page_size, set_page_size = db.use_state(20.0)

    def save():
        # In a real app: persist to Databricks secrets or config
        set_saved(True)

    return db.Column([
        db.Text("App Settings", variant="h1"),
        db.Text("Configure your BrickflowUI app and Databricks connections.", muted=True),
        db.Divider(),

        *(
            [db.Alert("Settings saved successfully!", type="success")]
            if saved else []
        ),

        db.Grid([
            db.Card(
                title="Databricks Connection",
                children=[
                    db.Input(
                        name="warehouse_id",
                        label="SQL Warehouse ID",
                        placeholder="e.g. 4a2bc3def456789",
                        value=warehouse_id,
                        on_change=set_warehouse_id,
                    ),
                    db.Input(
                        name="volume_uri",
                        label="Volume URI",
                        placeholder="/Volumes/catalog/schema/volume",
                        value=volume_uri,
                        on_change=set_volume_uri,
                    ),
                ],
            ),
            db.Card(
                title="UI Preferences",
                children=[
                    db.Toggle(
                        name="dark_mode",
                        label="Dark Mode",
                        checked=dark_mode,
                        on_change=set_dark_mode,
                    ),
                    db.Spacer(2),
                    db.Slider(
                        name="page_size",
                        label=f"Default Table Page Size: {int(page_size)}",
                        min=10,
                        max=100,
                        step=10,
                        value=page_size,
                        on_change=set_page_size,
                    ),
                ],
            ),
        ], cols=2, gap=4),

        db.Row([
            db.Button("Save Settings", on_click=save),
            db.Button("Reset to Defaults", on_click=lambda: set_saved(False), variant="secondary"),
        ]),
    ], padding=6, gap=4)


@app.page("/login", title="Login", icon="Lock")
def login_page():
    username, set_username = db.use_state("")
    password, set_password = db.use_state("")
    error, set_error = db.use_state(None)
    loading, set_loading = db.use_state(False)

    def handle_login():
        if not username or not password:
            set_error("Please enter username and password.")
            return
        set_loading(True)
        # Mock validation (real apps use Databricks OAuth or PAT)
        if username == "admin" and password == "admin":
            set_error(None)
            set_loading(False)
            # In a real app: redirect to dashboard
        else:
            set_error("Invalid credentials. Try admin / admin.")
            set_loading(False)

    return db.Column([
        db.Column([
            db.Text("Databricks Ops Hub", variant="h1"),
            db.Text("Sign in to access your data platform", muted=True),
        ], align="center"),
        db.Divider(),

        db.Card(
            title="Sign In",
            children=[
                *(
                    [db.Alert(error, type="error")]
                    if error else []
                ),
                db.Form(
                    action="/api/login",
                    method="POST",
                    success_redirect="/",
                    children=[
                        db.Input(
                            name="username",
                            label="Username",
                            placeholder="Enter your username",
                            value=username,
                            on_change=set_username,
                            required=True,
                        ),
                        db.Input(
                            name="password",
                            label="Password",
                            type="password",
                            placeholder="Enter your password",
                            value=password,
                            on_change=set_password,
                            required=True,
                        ),
                        db.Checkbox(name="remember", label="Keep me signed in"),
                        db.Spacer(2),
                        db.Button(
                            "Sign In" if not loading else "Signing in…",
                            on_click=handle_login,
                            loading=loading,
                            disabled=loading,
                        ),
                    ],
                ),
                db.Text("Demo credentials: admin / admin", muted=True, variant="caption"),
            ],
        ),
    ], padding=6, gap=4, align="center")


# ── Custom API route ──────────────────────────────────────────────────────────

@app.route("/api/login", methods=["POST"])
async def login_api():
    from fastapi.responses import JSONResponse
    from fastapi import Request
    # This route is just for Form POSTs from the HTML fallback shell
    return JSONResponse({"status": "success", "redirect": "/"})


@app.route("/api/health", methods=["GET"])
async def health():
    from fastapi.responses import JSONResponse
    from brickflowui import __version__
    return JSONResponse({"status": "ok", "version": __version__})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run()
