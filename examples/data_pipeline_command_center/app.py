from __future__ import annotations

import os
from collections import defaultdict

import brickflowui as db


THEME = {
    "branding": {"title": "Data Pipeline Command Center"},
    "colors": {
        "primary": "#14532D",
        "primary_hover": "#166534",
        "background": "#F5F7F4",
        "surface": "#FFFFFF",
        "text": "#102A1C",
        "text_muted": "#4B6355",
        "border": "#D9E4DB",
    },
    "typography": {
        "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif",
        "base_size": "15px",
    },
    "spacing": {"unit": "6px"},
    "borders": {"radius": "14px"},
}

app = db.App(theme=THEME)

SOURCE_OPTIONS = [
    {"label": "Mock Demo", "value": "mock"},
    {"label": "Databricks SQL", "value": "sql"},
]

DOMAIN_OPTIONS = [
    {"label": "All Layers", "value": "all"},
    {"label": "Bronze", "value": "bronze"},
    {"label": "Silver", "value": "silver"},
    {"label": "Gold", "value": "gold"},
]

PIPELINE_OPTIONS = [
    {"label": "All Pipelines", "value": "all"},
    {"label": "Customer 360", "value": "customer_360"},
    {"label": "Orders Lakehouse", "value": "orders_lakehouse"},
    {"label": "Finance Mart", "value": "finance_mart"},
    {"label": "ML Features", "value": "ml_features"},
]

PIPELINE_RECORDS = [
    {"pipeline": "customer_360", "pipeline_label": "Customer 360", "domain": "gold", "owner": "Data Platform", "status": "Healthy", "freshness_min": 12, "sla_target_min": 30, "rows_processed_m": 248, "cost_usd": 186, "success_rate": 99.8, "latency_min": 18, "incidents": 0},
    {"pipeline": "orders_lakehouse", "pipeline_label": "Orders Lakehouse", "domain": "silver", "owner": "Supply Analytics", "status": "Watch", "freshness_min": 47, "sla_target_min": 45, "rows_processed_m": 412, "cost_usd": 263, "success_rate": 98.9, "latency_min": 36, "incidents": 2},
    {"pipeline": "finance_mart", "pipeline_label": "Finance Mart", "domain": "gold", "owner": "Finance BI", "status": "Healthy", "freshness_min": 21, "sla_target_min": 60, "rows_processed_m": 128, "cost_usd": 141, "success_rate": 99.5, "latency_min": 29, "incidents": 1},
    {"pipeline": "ml_features", "pipeline_label": "ML Features", "domain": "silver", "owner": "ML Platform", "status": "At Risk", "freshness_min": 83, "sla_target_min": 60, "rows_processed_m": 96, "cost_usd": 219, "success_rate": 96.8, "latency_min": 54, "incidents": 4},
    {"pipeline": "raw_ingestion", "pipeline_label": "Raw Ingestion", "domain": "bronze", "owner": "Data Platform", "status": "Healthy", "freshness_min": 8, "sla_target_min": 20, "rows_processed_m": 690, "cost_usd": 308, "success_rate": 99.9, "latency_min": 11, "incidents": 0},
]

THROUGHPUT_TREND = [
    {"week": "W01", "rows_m": 1310, "cost_usd": 1012, "sla_pct": 97.8},
    {"week": "W02", "rows_m": 1384, "cost_usd": 1038, "sla_pct": 98.2},
    {"week": "W03", "rows_m": 1451, "cost_usd": 1076, "sla_pct": 97.5},
    {"week": "W04", "rows_m": 1495, "cost_usd": 1092, "sla_pct": 98.6},
    {"week": "W05", "rows_m": 1548, "cost_usd": 1110, "sla_pct": 98.8},
    {"week": "W06", "rows_m": 1602, "cost_usd": 1128, "sla_pct": 99.1},
]

INCIDENT_TREND = [
    {"week": "W01", "sev1": 1, "sev2": 3, "sev3": 6},
    {"week": "W02", "sev1": 0, "sev2": 4, "sev3": 5},
    {"week": "W03", "sev1": 2, "sev2": 3, "sev3": 7},
    {"week": "W04", "sev1": 1, "sev2": 2, "sev3": 4},
    {"week": "W05", "sev1": 0, "sev2": 2, "sev3": 3},
    {"week": "W06", "sev1": 0, "sev2": 1, "sev3": 2},
]

TEAM_HEALTH = [
    {"team": "Data Platform", "pipelines": 14, "sla_pct": 99.2, "cost_usd": 824, "status": "Strong"},
    {"team": "Supply Analytics", "pipelines": 8, "sla_pct": 97.6, "cost_usd": 492, "status": "Watch"},
    {"team": "Finance BI", "pipelines": 5, "sla_pct": 98.7, "cost_usd": 221, "status": "Strong"},
    {"team": "ML Platform", "pipelines": 6, "sla_pct": 95.9, "cost_usd": 381, "status": "At Risk"},
]

SQL_EXAMPLE = """-- Expected schema for the Databricks SQL mode
-- Set DEMO_PIPELINE_METRICS_TABLE to a fully-qualified table name.
--
-- Required columns:
-- pipeline, pipeline_label, domain, owner, status,
-- freshness_min, sla_target_min, rows_processed_m,
-- cost_usd, success_rate, latency_min, incidents
SELECT
  pipeline,
  pipeline_label,
  domain,
  owner,
  status,
  freshness_min,
  sla_target_min,
  rows_processed_m,
  cost_usd,
  success_rate,
  latency_min,
  incidents
FROM your_catalog.your_schema.pipeline_metrics
"""


def load_pipeline_records(source_mode: str) -> list[dict]:
    if source_mode != "sql":
        return PIPELINE_RECORDS

    table_name = os.getenv("DEMO_PIPELINE_METRICS_TABLE", "").strip()
    if not table_name:
        return PIPELINE_RECORDS

    try:
        from brickflowui.databricks import sql

        query = f"""
        SELECT
          pipeline,
          pipeline_label,
          domain,
          owner,
          status,
          freshness_min,
          sla_target_min,
          rows_processed_m,
          cost_usd,
          success_rate,
          latency_min,
          incidents
        FROM {table_name}
        """
        return sql.query_to_records(query)
    except Exception:
        return PIPELINE_RECORDS


def status_badge_color(status: str) -> str:
    return {
        "Healthy": "green",
        "Strong": "green",
        "Watch": "orange",
        "At Risk": "red",
    }.get(status, "gray")


def kpi_card(label: str, value: str, delta: str, delta_type: str, note: str):
    return db.Card(
        [
            db.Stat(label=label, value=value, delta=delta, delta_type=delta_type),
            db.Spacer(1),
            db.Text(note, variant="caption", muted=True),
        ],
        hover=True,
    )


def top_nav(active_view: str, set_view):
    def nav_button(label: str, view: str):
        return db.Button(
            label,
            on_click=lambda: set_view(view),
            variant="primary" if active_view == view else "ghost",
        )

    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Data Pipeline Command Center", variant="h3"),
                            db.Text(
                                "Industry-style monitoring for freshness, SLA health, cost, throughput, and pipeline reliability.",
                                variant="caption",
                                muted=True,
                            ),
                        ],
                        gap=1,
                    ),
                    db.Row(
                        [
                            nav_button("Overview", "overview"),
                            nav_button("Pipeline Health", "pipelines"),
                            nav_button("Cost & Reliability", "costs"),
                            nav_button("Data Model", "model"),
                        ],
                        gap=2,
                    ),
                    db.Row(
                        [
                            db.Badge("Lakehouse Ops", color="blue"),
                            db.Badge("Free Edition Friendly", color="purple"),
                        ],
                        gap=2,
                    ),
                ],
                justify="between",
                align="center",
            )
        ],
        padding=4,
        style={
            "background": "var(--db-surface)",
            "borderBottom": "1px solid var(--db-border)",
            "position": "sticky",
            "top": "0",
            "zIndex": "20",
        },
    )


def control_panel(
    source_mode,
    set_source_mode,
    domain,
    set_domain,
    pipeline,
    set_pipeline,
    period,
    set_period,
    search,
    set_search,
    min_sla,
    set_min_sla,
    critical_only,
    set_critical_only,
    show_benchmarks,
    set_show_benchmarks,
):
    return db.Card(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Pipeline Controls", variant="h3"),
                            db.Text("Filter the command center by layer, pipeline, SLA guardrails, and source mode.", variant="caption", muted=True),
                        ],
                        gap=1,
                    ),
                    db.Row(
                        [
                            db.Button("MTD", on_click=lambda: set_period("MTD"), variant="primary" if period == "MTD" else "secondary"),
                            db.Button("QTD", on_click=lambda: set_period("QTD"), variant="primary" if period == "QTD" else "secondary"),
                            db.Button("YTD", on_click=lambda: set_period("YTD"), variant="primary" if period == "YTD" else "secondary"),
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
                    db.Select(name="source_mode", label="Data Source", options=SOURCE_OPTIONS, value=source_mode, on_change=set_source_mode),
                    db.Select(name="domain", label="Pipeline Layer", options=DOMAIN_OPTIONS, value=domain, on_change=set_domain),
                    db.Select(name="pipeline", label="Pipeline Scope", options=PIPELINE_OPTIONS, value=pipeline, on_change=set_pipeline),
                    db.Input(name="search", label="Search Owner / Pipeline", placeholder="customer, finance, platform...", value=search, on_change=set_search),
                ],
                cols=4,
                gap=4,
            ),
            db.Spacer(2),
            db.Row(
                [
                    db.Slider(
                        name="min_sla",
                        label=f"Minimum Success Rate: {min_sla:.1f}%",
                        min=95,
                        max=100,
                        step=0.1,
                        value=min_sla,
                        on_change=set_min_sla,
                    ),
                    db.Checkbox(name="critical_only", label="Only show watch / at risk pipelines", checked=critical_only, on_change=set_critical_only),
                    db.Toggle(name="benchmarks", label="Show benchmark notes", checked=show_benchmarks, on_change=set_show_benchmarks),
                ],
                justify="between",
                align="center",
                wrap=True,
            ),
        ]
    )


def overview_page(filtered_records: list[dict], period: str, show_benchmarks: bool):
    rows_total = sum(item["rows_processed_m"] for item in filtered_records)
    avg_sla = sum(item["success_rate"] for item in filtered_records) / max(len(filtered_records), 1)
    avg_freshness = sum(item["freshness_min"] for item in filtered_records) / max(len(filtered_records), 1)
    total_cost = sum(item["cost_usd"] for item in filtered_records)

    notes = []
    if show_benchmarks:
        notes.append(
            db.Alert(
                f"{period} benchmark: filtered pipelines are averaging {avg_sla:.1f}% success rate and {avg_freshness:.0f} minute freshness.",
                type="info",
                title="Benchmark Overlay",
            )
        )

    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Executive View", variant="h1"),
                            db.Text("Use this view to see whether your free-edition Databricks pipeline is reliable enough to power downstream dashboards and stakeholder reporting.", muted=True),
                        ],
                        gap=1,
                    ),
                    db.Badge(f"{period} snapshot", color="green"),
                ],
                justify="between",
            ),
            *notes,
            db.Grid(
                [
                    kpi_card("Rows Processed", f"{rows_total:,.0f}M", "+6.1%", "increase", "Across all filtered pipelines"),
                    kpi_card("Avg Success Rate", f"{avg_sla:.1f}%", "+0.4 pts", "increase", "Weighted by selected pipeline scope"),
                    kpi_card("Freshness", f"{avg_freshness:.0f} min", "-5 min", "decrease", "Lower is better for consumers"),
                    kpi_card("Compute Cost", f"${total_cost:,.0f}", "-2.7%", "decrease", "Good baseline for free-edition cost discipline"),
                ],
                cols=4,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.AreaChart(
                                data=THROUGHPUT_TREND,
                                x_key="week",
                                y_keys=["rows_m", "sla_pct"],
                                title="Throughput and SLA Trend",
                                height=300,
                            )
                        ]
                    ),
                    db.Card(
                        [
                            db.BarChart(
                                data=INCIDENT_TREND,
                                x_key="week",
                                y_keys=["sev1", "sev2", "sev3"],
                                title="Incident Volume by Severity",
                                height=300,
                            )
                        ]
                    ),
                ],
                cols=2,
                gap=4,
            ),
            db.Card(
                [
                    db.Text("Pipeline Summary", variant="h3"),
                    db.Spacer(2),
                    db.Table(
                        data=filtered_records,
                        columns=[
                            {"key": "pipeline_label", "label": "Pipeline", "sortable": True},
                            {"key": "domain", "label": "Layer", "sortable": True},
                            {"key": "owner", "label": "Owner", "sortable": True},
                            {"key": "status", "label": "Status", "sortable": True},
                            {"key": "freshness_min", "label": "Freshness (min)", "sortable": True},
                            {"key": "success_rate", "label": "Success %", "sortable": True},
                            {"key": "cost_usd", "label": "Cost USD", "sortable": True},
                        ],
                        pagination=10,
                    ),
                ]
            ),
        ],
        gap=5,
    )


def pipeline_health_page(filtered_records: list[dict]):
    status_distribution: dict[str, int] = defaultdict(int)
    domain_distribution: dict[str, int] = defaultdict(int)

    for item in filtered_records:
        status_distribution[item["status"]] += 1
        domain_distribution[item["domain"].title()] += 1

    status_rows = [{"label": key, "value": value} for key, value in status_distribution.items()]
    domain_rows = [{"label": key, "value": value} for key, value in domain_distribution.items()]

    watch_rows = [row for row in filtered_records if row["status"] in {"Watch", "At Risk"}]

    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Pipeline Health", variant="h1"),
                            db.Text("This section is designed for daily engineering operations: identify freshness drift, reliability drops, and teams that need intervention.", muted=True),
                        ],
                        gap=1,
                    ),
                    db.Badge(f"{len(watch_rows)} pipelines need attention", color="orange" if watch_rows else "green"),
                ],
                justify="between",
            ),
            db.Grid(
                [
                    db.Card([db.DonutChart(data=status_rows or [{"label": "Healthy", "value": 1}], title="Status Distribution", height=280)]),
                    db.Card([db.DonutChart(data=domain_rows or [{"label": "Gold", "value": 1}], title="Pipeline Layer Mix", height=280)]),
                ],
                cols=2,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Text("Operational Guardrails", variant="h3"),
                            db.Spacer(2),
                            db.Progress(96, label="Schema stability"),
                            db.Progress(91, label="Upstream contract health"),
                            db.Progress(88, label="Downstream freshness compliance"),
                            db.Spacer(2),
                            db.Alert("Use these progress bars as a pattern for reporting quality gates or orchestration milestones.", type="info"),
                        ]
                    ),
                    db.Card(
                        [
                            db.Text("Teams in Scope", variant="h3"),
                            db.Spacer(2),
                            db.Table(
                                data=TEAM_HEALTH,
                                columns=[
                                    {"key": "team", "label": "Team", "sortable": True},
                                    {"key": "pipelines", "label": "Pipelines", "sortable": True},
                                    {"key": "sla_pct", "label": "SLA %", "sortable": True},
                                    {"key": "cost_usd", "label": "Cost USD", "sortable": True},
                                    {"key": "status", "label": "Status", "sortable": True},
                                ],
                                pagination=8,
                            ),
                        ]
                    ),
                ],
                cols=2,
                gap=4,
            ),
        ],
        gap=5,
    )


def cost_reliability_page(filtered_records: list[dict]):
    ranked = sorted(filtered_records, key=lambda row: (row["cost_usd"], row["incidents"]), reverse=True)
    cost_mix = [{"label": item["pipeline_label"], "value": item["cost_usd"]} for item in filtered_records]

    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Cost & Reliability", variant="h1"),
                            db.Text("A good industry dashboard does not stop at SLA. It connects cost, success rate, and incident load so you can prioritize engineering work sensibly.", muted=True),
                        ],
                        gap=1,
                    ),
                    db.Badge("Engineering review", color="blue"),
                ],
                justify="between",
            ),
            db.Grid(
                [
                    db.Card([db.BarChart(data=filtered_records, x_key="pipeline_label", y_keys=["cost_usd", "incidents"], title="Cost vs Incident Load", height=320)]),
                    db.Card([db.DonutChart(data=cost_mix or [{"label": "No data", "value": 1}], title="Cost Mix by Pipeline", height=320)]),
                ],
                cols=2,
                gap=4,
            ),
            db.Card(
                [
                    db.Text("Most Expensive or Unstable Pipelines", variant="h3"),
                    db.Spacer(2),
                    db.Table(
                        data=ranked,
                        columns=[
                            {"key": "pipeline_label", "label": "Pipeline", "sortable": True},
                            {"key": "owner", "label": "Owner", "sortable": True},
                            {"key": "cost_usd", "label": "Cost USD", "sortable": True},
                            {"key": "success_rate", "label": "Success %", "sortable": True},
                            {"key": "latency_min", "label": "Latency (min)", "sortable": True},
                            {"key": "incidents", "label": "Incidents", "sortable": True},
                        ],
                        pagination=10,
                    ),
                ]
            ),
        ],
        gap=5,
    )


def model_page(source_mode: str):
    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Data Model", variant="h1"),
                            db.Text("This page makes the expected warehouse shape explicit so you can swap the mock demo for real Databricks pipeline metrics quickly.", muted=True),
                        ],
                        gap=1,
                    ),
                    db.Badge("Source mode: " + source_mode.upper(), color="purple"),
                ],
                justify="between",
            ),
            db.Alert(
                "Start with the mock mode while building the UI. Once your free-edition pipeline writes a metrics table, set DEMO_PIPELINE_METRICS_TABLE and switch to Databricks SQL.",
                type="info",
                title="Recommended rollout path",
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Text("Expected SQL Shape", variant="h3"),
                            db.Spacer(2),
                            db.Code(SQL_EXAMPLE, language="sql"),
                        ]
                    ),
                    db.Card(
                        [
                            db.Text("Recommended metrics to store", variant="h3"),
                            db.Spacer(2),
                            db.Table(
                                data=[
                                    {"metric": "freshness_min", "reason": "Measures whether dashboards are stale"},
                                    {"metric": "success_rate", "reason": "Tracks orchestration stability"},
                                    {"metric": "rows_processed_m", "reason": "Shows business value and scale"},
                                    {"metric": "cost_usd", "reason": "Makes compute efficiency visible"},
                                    {"metric": "incidents", "reason": "Connects engineering reliability to user trust"},
                                ],
                                columns=[
                                    {"key": "metric", "label": "Metric"},
                                    {"key": "reason", "label": "Why it matters"},
                                ],
                                pagination=10,
                            ),
                        ]
                    ),
                ],
                cols=2,
                gap=4,
            ),
        ],
        gap=5,
    )


@app.page("/", title="Command Center")
def command_center():
    active_view, set_active_view = db.use_state("overview")
    source_mode, set_source_mode = db.use_state("mock")
    domain, set_domain = db.use_state("all")
    pipeline, set_pipeline = db.use_state("all")
    period, set_period = db.use_state("YTD")
    search, set_search = db.use_state("")
    min_sla, set_min_sla = db.use_state(97.0)
    critical_only, set_critical_only = db.use_state(False)
    show_benchmarks, set_show_benchmarks = db.use_state(True)

    all_records = db.use_memo(lambda: load_pipeline_records(source_mode), [source_mode])
    normalized_search = search.strip().lower()

    filtered_records = [
        item
        for item in all_records
        if (domain == "all" or item["domain"] == domain)
        and (pipeline == "all" or item["pipeline"] == pipeline)
        and item["success_rate"] >= float(min_sla)
        and (not critical_only or item["status"] in {"Watch", "At Risk"})
        and (
            not normalized_search
            or normalized_search in item["pipeline_label"].lower()
            or normalized_search in item["owner"].lower()
        )
    ]

    if not filtered_records:
        filtered_records = []

    view_node = {
        "overview": overview_page(filtered_records, period, show_benchmarks),
        "pipelines": pipeline_health_page(filtered_records),
        "costs": cost_reliability_page(filtered_records),
        "model": model_page(source_mode),
    }[active_view]

    return db.Column(
        [
            top_nav(active_view, set_active_view),
            db.Column(
                [
                    control_panel(
                        source_mode,
                        set_source_mode,
                        domain,
                        set_domain,
                        pipeline,
                        set_pipeline,
                        period,
                        set_period,
                        search,
                        set_search,
                        min_sla,
                        set_min_sla,
                        critical_only,
                        set_critical_only,
                        show_benchmarks,
                        set_show_benchmarks,
                    ),
                    db.Row(
                        [
                            db.Row(
                                [
                                    db.Badge(f"Source: {source_mode.upper()}", color="gray"),
                                    db.Badge(f"{len(filtered_records)} pipelines visible", color="blue"),
                                    db.Badge(f"SLA floor {min_sla:.1f}%", color="green"),
                                ],
                                gap=2,
                            ),
                            db.Text("Copy this app first, then replace the mock metrics with your Databricks table when your pipeline is ready.", variant="caption", muted=True),
                        ],
                        justify="between",
                        align="center",
                        wrap=True,
                    ),
                    view_node,
                ],
                padding=6,
                gap=5,
                style={"maxWidth": "1440px", "margin": "0 auto", "width": "100%"},
            ),
        ],
        gap=0,
        style={"minHeight": "100vh", "background": "linear-gradient(180deg, var(--db-bg) 0%, #ffffff 100%)"},
    )


if __name__ == "__main__":
    app.run()
