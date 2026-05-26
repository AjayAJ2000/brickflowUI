from __future__ import annotations

import brickflowui as db


app = db.App(
    theme={
        "default_mode": "dark",
        "branding": {
            "title": "Acme Analytics",
            "tagline": "Built with BrickflowUI",
            "show_theme_toggle": True,
        },
        "loading": {
            "title": "Acme Analytics",
            "subtitle": "Runtime-secure analytics workspace",
            "message": "Connecting to warehouse and restoring your view...",
            "animation": "pulse",
        },
        "colors": {
            "primary": "#4361EE",
            "primary_hover": "#3650D8",
        },
        "light_mode": {
            "colors": {
                "background": "#F8FAFC",
                "surface": "#FFFFFF",
                "text": "#0F172A",
                "text_muted": "#475569",
                "border": "#E2E8F0",
            }
        },
    }
)


SIDEBAR_PAGES = [
    ("Dashboard", "/", "LayoutDashboard"),
    ("Analytics", "/analytics", "Activity"),
    ("Users", "/users", "Target"),
    ("Pipelines", "/pipelines", "GitBranch"),
    ("Settings", "/settings", "Settings"),
]

ROWS = [
    {"account": "Acme Corp", "plan": "Enterprise", "mrr": 12400, "users": 184, "health": 88, "status": "Active"},
    {"account": "DataWorks Inc", "plan": "Enterprise", "mrr": 9800, "users": 97, "health": 72, "status": "Active"},
    {"account": "Helios AI", "plan": "Pro", "mrr": 4200, "users": 41, "health": 54, "status": "At risk"},
    {"account": "Meridian Labs", "plan": "Pro", "mrr": 3600, "users": 28, "health": 81, "status": "Active"},
    {"account": "Stackform", "plan": "Starter", "mrr": 840, "users": 7, "health": 31, "status": "Churned"},
    {"account": "NovaTech", "plan": "Enterprise", "mrr": 7100, "users": 63, "health": 95, "status": "Active"},
]

ACTIVITY = [
    {"title": "Pipeline deployed", "subtitle": "etl_revenue_v3 ran successfully in 4.2s", "time": "2 minutes ago"},
    {"title": "New user signup", "subtitle": "priya@datacrux.io joined DataWorks Inc", "time": "18 minutes ago"},
    {"title": "Query failed", "subtitle": "reports/weekly_churn.py raised ValueError on line 84", "time": "1 hour ago"},
    {"title": "Report generated", "subtitle": "Q1 executive summary exported to PDF (14 pages)", "time": "1 hour ago"},
]


def plan_tone(plan: str) -> str:
    if plan == "Enterprise":
        return "info"
    if plan == "Pro":
        return "warning"
    return "neutral"


def status_tone(status: str) -> str:
    if status == "Active":
        return "success"
    if status == "At risk":
        return "warning"
    return "error"


def enriched_rows(query: str) -> list[dict]:
    scoped = [
        {
            **row,
            "planTone": plan_tone(row["plan"]),
            "statusTone": status_tone(row["status"]),
            "mrrDisplay": row["mrr"],
        }
        for row in ROWS
        if query.lower() in row["account"].lower()
    ]
    return scoped


def metric(label: str, value: str, delta: str, tone: str, detail: str) -> db.VNode:
    return db.Card(
        [
            db.Stat(label=label, value=value, delta=delta, delta_type=tone, animated=True),
            db.Text(detail, variant="caption", muted=True),
        ],
        bordered=True,
        hover=True,
        elevated=True,
    )


@app.page("/", title="Dashboard", icon="LayoutDashboard")
def dashboard():
    query, set_query = db.use_state("")
    time_window, set_time_window = db.use_state("Last 30 days")
    rows = enriched_rows(query)

    return db.Column(
        [
            db.Hero(
                "Customer command center",
                subtitle="Responsive KPI surfaces, dense operational tables, and dark-mode native shell patterns built entirely from Python.",
                eyebrow="Acme Analytics",
                tagline="Built with BrickflowUI",
                actions=[
                    db.Select(
                        name="window",
                        options=[
                            {"label": "Last 7 days", "value": "Last 7 days"},
                            {"label": "Last 30 days", "value": "Last 30 days"},
                            {"label": "Last 90 days", "value": "Last 90 days"},
                        ],
                        value=time_window,
                        on_change=set_time_window,
                    ),
                    db.Button("Export", variant="secondary", icon="Database"),
                    db.Button("New report", icon="Sparkles"),
                ],
                badges=[
                    db.Badge("Runtime secure", color="green"),
                    db.Badge("Mobile ready", color="blue"),
                ],
            ),
            db.Grid(
                [
                    metric("MRR", "$37.9K", "+8.4%", "increase", "Healthy expansion across enterprise plans."),
                    metric("Users", "420", "+11.2%", "increase", "Active seats grew across analytics tenants."),
                    metric("Health", "76.8", "-1.6 pts", "decrease", "Two accounts need intervention this week."),
                    metric("Retention", "93.1%", "+2.1 pts", "increase", "Churn risk remains isolated."),
                ],
                cols=4,
                gap=4,
            ),
            db.Card(
                [
                    db.Row(
                        [
                            db.Input(
                                name="search",
                                label="Search accounts",
                                placeholder="Search accounts...",
                                value=query,
                                on_change=set_query,
                                # style={"maxWidth": "320px"},
                            ),
                            db.Button("Filter", variant="secondary"),
                            db.Text(f"Showing {len(rows)} of {len(ROWS)}", variant="caption", muted=True),
                        ],
                        gap=3,
                        wrap=True,
                        justify="between",
                    ),
                    db.Spacer(4),
                    db.Table(
                        data=rows,
                        columns=[
                            {"key": "account", "label": "Account", "sortable": True, "format": "metric"},
                            {"key": "plan", "label": "Plan", "format": "badge", "toneKey": "planTone"},
                            {"key": "mrrDisplay", "label": "MRR", "sortable": True, "format": "currency", "currency": "USD"},
                            {"key": "users", "label": "Users", "sortable": True, "align": "right"},
                            {"key": "health", "label": "Health", "sortable": True, "format": "progress", "toneKey": "statusTone"},
                            {"key": "status", "label": "Status", "sortable": True, "format": "status", "toneKey": "statusTone"},
                        ],
                        pagination=6,
                        exportable=True,
                    ),
                ],
                title="Dashboard",
                bordered=True,
                elevated=True,
            ),
            db.Card(
                [
                    db.SectionHeader("Recent activity", subtitle=f"Window: {time_window}"),
                    db.Timeline(ACTIVITY),
                ],
                bordered=True,
                elevated=True,
            ),
        ],
        gap=5,
        style={"maxWidth": "1280px", "margin": "0 auto", "width": "100%"},
    )


@app.page("/analytics", title="Analytics", icon="Activity")
def analytics():
    return db.Card(
        [
            db.SectionHeader("Analytics workspace", subtitle="Drop in charts, embeds, and deeper drilldowns here."),
            db.Embed("https://example.com", title="External analytics artifact", height="420px"),
        ],
        bordered=True,
        elevated=True,
    )


@app.page("/users", title="Users", icon="Target")
def users():
    return db.EmptyState(
        title="User view scaffolded",
        message="Use Image variants for avatars, tables for directory views, and ThemeToggle through the built-in shell footer.",
        icon="Users",
        actions=[db.Button("Back to dashboard", on_click=lambda: None, variant="secondary")],
    )


@app.page("/pipelines", title="Pipelines", icon="GitBranch")
def pipelines():
    return db.Card(
        [
            db.SectionHeader("Pipelines", subtitle="This shows the screenshot-style shell next to a pipeline graph."),
            db.PipelineGraph(
                nodes=[
                    {"id": "extract", "label": "Extract", "status": "running", "layer": "bronze"},
                    {"id": "transform", "label": "Transform", "status": "active", "layer": "silver"},
                    {"id": "serve", "label": "Serve", "status": "active", "layer": "gold"},
                ],
                edges=[
                    {"from": "extract", "to": "transform"},
                    {"from": "transform", "to": "serve"},
                ],
                title="Revenue pipeline",
                animated=True,
            ),
        ],
        bordered=True,
        elevated=True,
    )


@app.page("/settings", title="Settings", icon="Settings")
def settings():
    return db.Card(
        [
            db.SectionHeader("Brand and runtime controls", subtitle="Theme toggle, custom loading, assets, and mobile nav are all framework-level now."),
            db.Text("This page is intentionally lightweight. Use it as a starting point for auth, governance, and runtime settings.", muted=True),
        ],
        bordered=True,
        elevated=True,
    )


if __name__ == "__main__":
    app.run()
