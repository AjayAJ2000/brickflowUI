"""
Manufacturing + Finance command center example for BrickflowUI.

Run locally:
    python app.py
"""

from __future__ import annotations

from pathlib import Path
import sys

APP_DIR = Path(__file__).parent
REPO_ROOT = APP_DIR.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import brickflowui as db


app = db.App(
    theme=APP_DIR / "portal_theme.yaml",
)


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]

MANUFACTURING_TREND = [
    {"month": "Jan", "oee": 73, "yield": 95.8, "throughput": 92},
    {"month": "Feb", "oee": 74, "yield": 96.1, "throughput": 96},
    {"month": "Mar", "oee": 76, "yield": 96.5, "throughput": 99},
    {"month": "Apr", "oee": 78, "yield": 96.9, "throughput": 104},
    {"month": "May", "oee": 79, "yield": 97.2, "throughput": 107},
    {"month": "Jun", "oee": 81, "yield": 97.5, "throughput": 111},
    {"month": "Jul", "oee": 82, "yield": 97.4, "throughput": 114},
    {"month": "Aug", "oee": 84, "yield": 97.9, "throughput": 118},
]

PLANT_SCORECARD = [
    {"site": "Toyama", "oee": 86, "yield": "98.2%", "downtime": "3.8%", "batch_release": "2.1 days", "status": "On Track"},
    {"site": "Leiden", "oee": 81, "yield": "97.6%", "downtime": "5.2%", "batch_release": "2.5 days", "status": "Watch"},
    {"site": "Northbrook", "oee": 84, "yield": "97.9%", "downtime": "4.1%", "batch_release": "2.0 days", "status": "On Track"},
    {"site": "Kerry", "oee": 78, "yield": "96.8%", "downtime": "6.4%", "batch_release": "3.0 days", "status": "At Risk"},
]

DOWN_TIME_CAUSES = [
    {"label": "Changeover", "value": 34},
    {"label": "Material Delay", "value": 22},
    {"label": "Equipment", "value": 27},
    {"label": "Quality Hold", "value": 17},
]

FINANCIAL_TREND = [
    {"month": "Jan", "revenue": 1180, "gross_margin": 71.1, "ebitda": 302},
    {"month": "Feb", "revenue": 1215, "gross_margin": 71.4, "ebitda": 316},
    {"month": "Mar", "revenue": 1248, "gross_margin": 71.9, "ebitda": 321},
    {"month": "Apr", "revenue": 1275, "gross_margin": 72.2, "ebitda": 334},
    {"month": "May", "revenue": 1302, "gross_margin": 72.6, "ebitda": 341},
    {"month": "Jun", "revenue": 1338, "gross_margin": 73.0, "ebitda": 352},
    {"month": "Jul", "revenue": 1366, "gross_margin": 73.2, "ebitda": 359},
    {"month": "Aug", "revenue": 1404, "gross_margin": 73.8, "ebitda": 368},
]

BUSINESS_UNIT_SPLIT = [
    {"label": "Oncology", "value": 42},
    {"label": "Urology", "value": 23},
    {"label": "Immunology", "value": 19},
    {"label": "Emerging Markets", "value": 16},
]

COMMERCIAL_SCORECARD = [
    {"business_unit": "Oncology", "revenue_usd_m": "590", "vs_plan": "+4.6%", "opex_ratio": "22.1%", "status": "Above Plan"},
    {"business_unit": "Urology", "revenue_usd_m": "322", "vs_plan": "+2.1%", "opex_ratio": "18.3%", "status": "On Plan"},
    {"business_unit": "Immunology", "revenue_usd_m": "261", "vs_plan": "-1.2%", "opex_ratio": "24.0%", "status": "Watch"},
    {"business_unit": "Emerging Markets", "revenue_usd_m": "231", "vs_plan": "+5.3%", "opex_ratio": "20.4%", "status": "Above Plan"},
]


def kpi_card(label: str, value: str, delta: str, delta_type: str, icon: str) -> db.VNode:
    return db.Card(
        [
            db.Stat(label=label, value=value, delta=delta, delta_type=delta_type, icon=icon),
        ],
        bordered=True,
    )


def top_nav(active_view: str, set_view) -> db.VNode:
    def nav_button(label: str, view: str) -> db.VNode:
        return db.Button(
            label,
            on_click=lambda: set_view(view),
            variant="primary" if active_view == view else "ghost",
        )

    return db.Column(
        [
            db.Row(
                [
                    db.Row(
                        [
                            db.Column(
                                [
                                    db.Text("Astellas Enterprise Pulse", variant="h3"),
                                    db.Text("Manufacturing and financial performance command center", muted=True, variant="caption"),
                                ],
                                gap=1,
                            ),
                        ],
                        gap=3,
                    ),
                    db.Row(
                        [
                            nav_button("Overview", "overview"),
                            nav_button("Manufacturing", "manufacturing"),
                            nav_button("Financials", "financials"),
                        ],
                        gap=2,
                    ),
                    db.Row(
                        [
                            db.Badge("Updated 08:45 JST", color="green"),
                            db.Badge("Demo Workspace", color="purple"),
                        ],
                        gap=2,
                    ),
                ],
                justify="between",
                align="center",
            ),
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


def executive_overview() -> db.VNode:
    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Executive Overview", variant="h1"),
                            db.Text("A unified view of plant execution, product supply stability, and financial performance.", muted=True),
                        ]
                    ),
                    db.Badge("Board Review Ready", color="blue"),
                ],
                justify="between",
            ),
            db.Grid(
                [
                    kpi_card("Network OEE", "84.0%", "+2.1 pts", "increase", "Activity"),
                    kpi_card("Batch Release", "2.3 days", "-0.4 days", "decrease", "Clock"),
                    kpi_card("Revenue", "$1.40B", "+6.3%", "increase", "Target"),
                    kpi_card("EBITDA", "$368M", "+4.8%", "increase", "CheckCircle"),
                ],
                cols=4,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.LineChart(
                                data=MANUFACTURING_TREND,
                                x_key="month",
                                y_keys=["oee", "yield"],
                                title="Manufacturing Quality and Efficiency Trend",
                                height=290,
                            ),
                        ],
                        bordered=True,
                    ),
                    db.Card(
                        [
                            db.BarChart(
                                data=FINANCIAL_TREND,
                                x_key="month",
                                y_keys=["revenue", "ebitda"],
                                title="Revenue and EBITDA Momentum",
                                height=290,
                            ),
                        ],
                        bordered=True,
                    ),
                ],
                cols=2,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Text("Executive Notes", variant="h3"),
                            db.Spacer(2),
                            db.Alert("Toyama and Northbrook are carrying the strongest throughput gains this month.", type="success"),
                            db.Alert("Kerry remains the main operational watchpoint due to downtime and slower release cadence.", type="warning"),
                            db.Alert("Immunology is slightly under plan, but overall portfolio revenue remains ahead of target.", type="info"),
                        ],
                        bordered=True,
                    ),
                    db.Card(
                        [
                            db.Text("Portfolio Mix", variant="h3"),
                            db.Spacer(2),
                            db.DonutChart(
                                data=BUSINESS_UNIT_SPLIT,
                                title="Revenue Split by Business Unit",
                                height=250,
                            ),
                        ],
                        bordered=True,
                    ),
                ],
                cols=2,
                gap=4,
            ),
        ],
        gap=5,
    )


def manufacturing_dashboard() -> db.VNode:
    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Manufacturing Performance", variant="h1"),
                            db.Text("Plant-level efficiency, quality, and supply reliability across the network.", muted=True),
                        ]
                    ),
                    db.Badge("4 Sites in Scope", color="blue"),
                ],
                justify="between",
            ),
            db.Grid(
                [
                    kpi_card("OEE", "84.0%", "+2.1 pts", "increase", "Activity"),
                    kpi_card("Yield", "97.9%", "+0.5 pts", "increase", "CheckCircle"),
                    kpi_card("Throughput Index", "118", "+7.3%", "increase", "PlayCircle"),
                    kpi_card("Downtime", "4.9%", "-0.8 pts", "decrease", "AlertTriangle"),
                ],
                cols=4,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.AreaChart(
                                data=MANUFACTURING_TREND,
                                x_key="month",
                                y_keys=["throughput"],
                                title="Throughput Index",
                                colors=["#9E1B32"],
                                height=280,
                            ),
                        ],
                        bordered=True,
                    ),
                    db.Card(
                        [
                            db.DonutChart(
                                data=DOWN_TIME_CAUSES,
                                title="Downtime Mix",
                                height=280,
                            ),
                        ],
                        bordered=True,
                    ),
                ],
                cols=2,
                gap=4,
            ),
            db.Card(
                [
                    db.Text("Plant Scorecard", variant="h3"),
                    db.Spacer(2),
                    db.Table(
                        data=PLANT_SCORECARD,
                        columns=[
                            {"key": "site", "label": "Site", "sortable": True},
                            {"key": "oee", "label": "OEE", "sortable": True},
                            {"key": "yield", "label": "Yield", "sortable": True},
                            {"key": "downtime", "label": "Downtime"},
                            {"key": "batch_release", "label": "Batch Release"},
                            {"key": "status", "label": "Status", "sortable": True},
                        ],
                        pagination=10,
                    ),
                ],
                bordered=True,
            ),
        ],
        gap=5,
    )


def financial_dashboard() -> db.VNode:
    return db.Column(
        [
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Financial Performance", variant="h1"),
                            db.Text("Commercial growth, margin quality, and operating discipline across the portfolio.", muted=True),
                        ]
                    ),
                    db.Badge("FY Outlook Ahead of Plan", color="green"),
                ],
                justify="between",
            ),
            db.Grid(
                [
                    kpi_card("Revenue", "$1.40B", "+6.3%", "increase", "Target"),
                    kpi_card("Gross Margin", "73.8%", "+0.8 pts", "increase", "CheckCircle"),
                    kpi_card("EBITDA", "$368M", "+4.8%", "increase", "Activity"),
                    kpi_card("OpEx Ratio", "21.4%", "-0.6 pts", "decrease", "Clock"),
                ],
                cols=4,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.BarChart(
                                data=FINANCIAL_TREND,
                                x_key="month",
                                y_keys=["revenue"],
                                title="Revenue Trend (USD M)",
                                height=280,
                            ),
                        ],
                        bordered=True,
                    ),
                    db.Card(
                        [
                            db.LineChart(
                                data=FINANCIAL_TREND,
                                x_key="month",
                                y_keys=["gross_margin"],
                                title="Gross Margin Trend",
                                height=280,
                            ),
                        ],
                        bordered=True,
                    ),
                ],
                cols=2,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Text("Business Unit Mix", variant="h3"),
                            db.Spacer(2),
                            db.DonutChart(
                                data=BUSINESS_UNIT_SPLIT,
                                title="Revenue Mix",
                                height=260,
                            ),
                        ],
                        bordered=True,
                    ),
                    db.Card(
                        [
                            db.Text("Commercial Scorecard", variant="h3"),
                            db.Spacer(2),
                            db.Table(
                                data=COMMERCIAL_SCORECARD,
                                columns=[
                                    {"key": "business_unit", "label": "Business Unit", "sortable": True},
                                    {"key": "revenue_usd_m", "label": "Revenue (USD M)", "sortable": True},
                                    {"key": "vs_plan", "label": "Vs Plan", "sortable": True},
                                    {"key": "opex_ratio", "label": "OpEx Ratio"},
                                    {"key": "status", "label": "Status", "sortable": True},
                                ],
                                pagination=10,
                            ),
                        ],
                        bordered=True,
                    ),
                ],
                cols=2,
                gap=4,
            ),
        ],
        gap=5,
    )


@app.page("/", title="Portal")
def portal():
    active_view, set_active_view = db.use_state("overview")
    period, set_period = db.use_state("YTD")

    view_node = {
        "overview": executive_overview(),
        "manufacturing": manufacturing_dashboard(),
        "financials": financial_dashboard(),
    }[active_view]

    return db.Column(
        [
            top_nav(active_view, set_active_view),
            db.Column(
                [
                    db.Row(
                        [
                            db.Row(
                                [
                                    db.Text("Reporting Period", variant="label"),
                                    db.Button("MTD", on_click=lambda: set_period("MTD"), variant="secondary" if period != "MTD" else "primary"),
                                    db.Button("QTD", on_click=lambda: set_period("QTD"), variant="secondary" if period != "QTD" else "primary"),
                                    db.Button("YTD", on_click=lambda: set_period("YTD"), variant="secondary" if period != "YTD" else "primary"),
                                ],
                                gap=2,
                                align="center",
                            ),
                            db.Badge(f"{period} Snapshot", color="orange"),
                        ],
                        justify="between",
                        align="center",
                    ),
                    view_node,
                ],
                padding=6,
                gap=5,
                style={"maxWidth": "1360px", "margin": "0 auto", "width": "100%"},
            ),
        ],
        gap=0,
        style={"minHeight": "100vh", "background": "linear-gradient(180deg, var(--db-bg) 0%, #ffffff 100%)"},
    )


if __name__ == "__main__":
    app.run()
