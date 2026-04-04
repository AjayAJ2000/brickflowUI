from __future__ import annotations

import brickflowui as db


THEME = {
    "branding": {"title": "BrickflowUI Workspace Studio"},
    "colors": {
        "primary": "#0E7490",
        "primary_hover": "#155E75",
        "background": "#F4F7FB",
        "surface": "#FFFFFF",
        "text": "#0F172A",
        "text_muted": "#475569",
        "border": "#D8E1EC",
    },
    "typography": {
        "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif",
        "base_size": "15px",
    },
    "spacing": {"unit": "6px"},
    "borders": {"radius": "14px"},
}

THEME_SNIPPET = """branding:
  title: "BrickflowUI Workspace Studio"
colors:
  primary: "#0E7490"
  primary_hover: "#155E75"
  background: "#F4F7FB"
  surface: "#FFFFFF"
  text: "#0F172A"
  text_muted: "#475569"
  border: "#D8E1EC"
typography:
  font_family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
  base_size: "15px"
spacing:
  unit: "6px"
borders:
  radius: "14px"
"""

SITE_OPTIONS = [
    {"label": "Network", "value": "network"},
    {"label": "Toyama", "value": "toyama"},
    {"label": "Leiden", "value": "leiden"},
]

TREND = [
    {"week": "W01", "throughput": 94, "yield": 97.1, "cycle": 2.8},
    {"week": "W02", "throughput": 97, "yield": 97.4, "cycle": 2.6},
    {"week": "W03", "throughput": 101, "yield": 97.9, "cycle": 2.4},
    {"week": "W04", "throughput": 105, "yield": 98.0, "cycle": 2.2},
]

ORDERS = [
    {"line": "Granulation A", "site": "Toyama", "owner": "Mina", "priority": "High", "status": "Running", "confidence": 96},
    {"line": "Packaging 2", "site": "Leiden", "owner": "Elias", "priority": "Medium", "status": "Watch", "confidence": 91},
    {"line": "Vial Fill 1", "site": "Toyama", "owner": "Nora", "priority": "Critical", "status": "Escalated", "confidence": 88},
]

RELEASES = [
    {"lot": "AT-2049", "site": "Toyama", "stage": "QC Review", "owner": "Sara", "eta": "Today 17:00", "status": "On Track"},
    {"lot": "AT-2055", "site": "Leiden", "stage": "Deviation Review", "owner": "Mark", "eta": "Tomorrow 09:30", "status": "Watch"},
    {"lot": "AT-2068", "site": "Leiden", "stage": "Micro Hold", "owner": "Rosa", "eta": "Tomorrow 15:45", "status": "At Risk"},
]

RISK_MIX = [
    {"label": "Low", "value": 58},
    {"label": "Moderate", "value": 27},
    {"label": "High", "value": 15},
]

TOKEN_ROWS = [
    {"token": "branding.title", "purpose": "Browser title and header", "value": "Workspace Studio"},
    {"token": "colors.primary", "purpose": "Primary actions", "value": "#0E7490"},
    {"token": "colors.background", "purpose": "Page canvas", "value": "#F4F7FB"},
    {"token": "borders.radius", "purpose": "Rounded cards and controls", "value": "14px"},
]

app = db.App(theme=THEME)


def metric_card(label: str, value: str, delta: str, delta_type: str, note: str):
    return db.Card(
        [db.Stat(label=label, value=value, delta=delta, delta_type=delta_type), db.Spacer(1), db.Text(note, variant="caption", muted=True)],
        hover=True,
    )


def top_nav(active: str, set_active):
    def nav(label: str, value: str):
        return db.Button(label, on_click=lambda: set_active(value), variant="primary" if active == value else "ghost")

    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("BrickflowUI Workspace Studio", variant="h3"),
                            db.Text("Traditional top nav, rich UI primitives, and a dedicated Themes section in one self-contained example.", variant="caption", muted=True),
                        ],
                        gap=1,
                    ),
                    db.Row([nav("Executive", "executive"), nav("Operations", "operations"), nav("Themes", "themes")], gap=2),
                    db.Row([db.Badge("Live Demo", color="green"), db.Badge("Databricks-ready", color="purple")], gap=2),
                ],
                justify="between",
                align="center",
            )
        ],
        padding=4,
        style={"background": "var(--db-surface)", "borderBottom": "1px solid var(--db-border)", "position": "sticky", "top": "0", "zIndex": "20"},
    )


def filters(site, set_site, query, set_query, urgent_only, set_urgent_only, min_confidence, set_min_confidence, set_show_modal):
    return db.Card(
        [
            db.Row(
                [
                    db.Column([db.Text("Control Center", variant="h3"), db.Text("Drive the page with real interactive controls.", variant="caption", muted=True)], gap=1),
                    db.Row(
                        [
                            db.Button("Open Action Pack", on_click=lambda: set_show_modal(True), variant="outline"),
                            db.Button(
                                "Reset Filters",
                                on_click=lambda: (set_site("network"), set_query(""), set_urgent_only(False), set_min_confidence(90.0)),
                                variant="secondary",
                            ),
                        ],
                        gap=2,
                    ),
                ],
                justify="between",
                align="center",
            ),
            db.Spacer(3),
            db.Grid(
                [
                    db.Input(name="search", label="Search Work Orders", placeholder="Search by line or owner", value=query, on_change=set_query),
                    db.Select(name="site", label="Site Scope", options=SITE_OPTIONS, value=site, on_change=set_site),
                    db.Slider(name="confidence", label=f"Minimum Confidence: {int(min_confidence)}%", min=80, max=100, step=1, value=min_confidence, on_change=set_min_confidence),
                    db.Checkbox(name="urgent_only", label="Only show urgent items", checked=urgent_only, on_change=set_urgent_only),
                ],
                cols=4,
                gap=4,
            ),
        ]
    )


def executive_view(filtered_orders, filtered_releases):
    return db.Column(
        [
            db.Grid(
                [
                    metric_card("Network Throughput", "105 lots", "+3.1%", "increase", "Strong fill-finish execution."),
                    metric_card("Batch Release", "2.2 days", "-0.3 days", "decrease", "Disposition cycle is improving."),
                    metric_card("Watchlist Items", str(sum(1 for row in filtered_orders if row["status"] != "Running")), "-1", "decrease", "Fewer lines require escalation."),
                    metric_card("Release On Track", f"{sum(1 for row in filtered_releases if row['status'] != 'At Risk')}/{len(filtered_releases)}", "+2 lots", "increase", "Most lots remain inside target windows."),
                ],
                cols=4,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card([db.AreaChart(data=TREND, x_key="week", y_keys=["throughput", "yield"], title="Throughput and Yield Trend", height=300)]),
                    db.Card([db.DonutChart(data=RISK_MIX, title="Network Risk Mix", height=300)]),
                ],
                cols=2,
                gap=4,
            ),
            db.Tabs(
                [
                    db.TabItem("Watchlist", [db.Table(data=filtered_orders, columns=[{"key": "line", "label": "Line"}, {"key": "site", "label": "Site"}, {"key": "owner", "label": "Owner"}, {"key": "priority", "label": "Priority"}, {"key": "status", "label": "Status"}, {"key": "confidence", "label": "Confidence"}], pagination=8)]),
                    db.TabItem("Release Queue", [db.Table(data=filtered_releases, columns=[{"key": "lot", "label": "Lot"}, {"key": "site", "label": "Site"}, {"key": "stage", "label": "Stage"}, {"key": "owner", "label": "Owner"}, {"key": "eta", "label": "ETA"}, {"key": "status", "label": "Status"}], pagination=8)]),
                    db.TabItem("Action Plan", [db.Form([db.Input(name="owner", label="Plan Owner", placeholder="e.g. Mina Sato"), db.Select(name="site", label="Target Site", options=SITE_OPTIONS, value="network"), db.Input(name="summary", label="Action Summary", placeholder="Describe the risk or action"), db.Button("Create Action Plan", html_type="submit", width="100%")], action="/api/action-plan", method="POST", reload_on_success=True)]),
                ]
            ),
        ],
        gap=5,
    )


def operations_view(filtered_orders, filtered_releases):
    return db.Column(
        [
            db.Alert("Use this section to inspect tables, charts, badges, and progress states together.", type="info", title="Component Showcase"),
            db.Grid(
                [
                    db.Card([db.BarChart(data=TREND, x_key="week", y_keys=["throughput"], title="Weekly Throughput", height=280)]),
                    db.Card([db.LineChart(data=TREND, x_key="week", y_keys=["cycle"], title="Release Cycle Trend", height=280)]),
                ],
                cols=2,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card([db.Text("Disposition Progress", variant="h3"), db.Spacer(2), db.Progress(88, label="Deviation closure"), db.Progress(93, label="Document readiness"), db.Progress(82, label="Micro review completion")]),
                    db.Card([db.Text("Current Queue", variant="h3"), db.Spacer(2), db.Table(data=filtered_releases, columns=[{"key": "lot", "label": "Lot"}, {"key": "site", "label": "Site"}, {"key": "status", "label": "Status"}], pagination=5)]),
                ],
                cols=2,
                gap=4,
            ),
            db.Card([db.Text("Operational Watchlist", variant="h3"), db.Spacer(2), db.Table(data=filtered_orders, columns=[{"key": "line", "label": "Line"}, {"key": "owner", "label": "Owner"}, {"key": "priority", "label": "Priority"}, {"key": "status", "label": "Status"}], pagination=8)]),
        ],
        gap=5,
    )


def themes_view():
    return db.Column(
        [
            db.Alert("This page exists to make the theme model obvious to new users. The same keys can be moved into a YAML file later.", type="info", title="Theme Guide"),
            db.Grid(
                [
                    db.Card([db.Text("Theme YAML", variant="h3"), db.Spacer(2), db.Code(THEME_SNIPPET, language="yaml")]),
                    db.Card([db.Text("Token Mapping", variant="h3"), db.Spacer(2), db.Table(data=TOKEN_ROWS, columns=[{"key": "token", "label": "Token"}, {"key": "purpose", "label": "Purpose"}, {"key": "value", "label": "Value"}], pagination=10)]),
                ],
                cols=2,
                gap=4,
            ),
            db.Card(
                [
                    db.Text("Live Preview", variant="h3"),
                    db.Spacer(2),
                    db.Row([db.Badge("Primary color", color="blue"), db.Badge("Surface cards", color="gray"), db.Badge("Healthy status", color="green")], gap=2),
                    db.Spacer(2),
                    db.Row([db.Button("Primary Action"), db.Button("Secondary Action", variant="secondary"), db.Button("Outline Action", variant="outline")], gap=2, wrap=True),
                    db.Spacer(2),
                    db.Text("Rounded cards, soft borders, and the teal accent are all being driven by the theme tokens shown above.", muted=True),
                ],
                hover=True,
            ),
        ],
        gap=5,
    )


@app.route("/api/action-plan", methods=["POST"])
async def create_action_plan(request):
    payload = await request.json()
    return {"status": "ok", "message": f"Action plan queued for {payload.get('site', 'network')}", "owner": payload.get("owner"), "summary": payload.get("summary")}


@app.page("/", title="Workspace")
def workspace():
    active, set_active = db.use_state("executive")
    site, set_site = db.use_state("network")
    query, set_query = db.use_state("")
    urgent_only, set_urgent_only = db.use_state(False)
    min_confidence, set_min_confidence = db.use_state(90.0)
    show_modal, set_show_modal = db.use_state(False)

    normalized = query.strip().lower()

    filtered_orders = [
        row
        for row in ORDERS
        if (site == "network" or row["site"].lower() == site)
        and row["confidence"] >= float(min_confidence)
        and (not urgent_only or row["priority"] in {"High", "Critical"})
        and (not normalized or normalized in row["line"].lower() or normalized in row["owner"].lower())
    ]
    filtered_releases = [row for row in RELEASES if site == "network" or row["site"].lower() == site]

    view = {
        "executive": executive_view(filtered_orders, filtered_releases),
        "operations": operations_view(filtered_orders, filtered_releases),
        "themes": themes_view(),
    }[active]

    return db.Column(
        [
            top_nav(active, set_active),
            db.Column(
                [
                    filters(site, set_site, query, set_query, urgent_only, set_urgent_only, min_confidence, set_min_confidence, set_show_modal)
                    if active != "themes"
                    else db.Card([db.Text("Theme explorer mode", variant="h3"), db.Text("Switch back to Executive or Operations to see filters affecting live content.", muted=True)]),
                    db.Row(
                        [
                            db.Row([db.Badge(f"Scope: {site.title()}", color="blue"), db.Badge(f"{len(filtered_orders)} work orders", color="purple")], gap=2),
                            db.Text("Traditional top nav plus rich component composition in pure Python.", variant="caption", muted=True),
                        ],
                        justify="between",
                        align="center",
                        wrap=True,
                    ),
                    view,
                ],
                padding=6,
                gap=5,
                style={"maxWidth": "1380px", "margin": "0 auto", "width": "100%"},
            ),
            db.Modal(
                visible=show_modal,
                title="Weekly Action Pack",
                on_close=lambda: set_show_modal(False),
                size="lg",
                children=[
                    db.Column(
                        [
                            db.Text("This modal demonstrates a secondary workflow without leaving the current page.", muted=True),
                            db.Spacer(2),
                            db.Alert("Prepare the Leiden escalation review, clear the release risks, and lock tomorrow's staffing plan.", type="info", title="Suggested Focus"),
                            db.Spacer(2),
                            db.Progress(92, label="Action pack completeness"),
                            db.Spacer(2),
                            db.Row([db.Button("Close", variant="secondary", on_click=lambda: set_show_modal(False)), db.Button("Acknowledge", on_click=lambda: set_show_modal(False))], justify="end"),
                        ],
                        gap=2,
                    )
                ],
            ),
        ],
        gap=0,
        style={"minHeight": "100vh", "background": "linear-gradient(180deg, var(--db-bg) 0%, #ffffff 100%)"},
    )


if __name__ == "__main__":
    app.run()
