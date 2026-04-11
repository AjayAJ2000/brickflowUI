from __future__ import annotations

import brickflowui as db


LANDING_THEME = {
    "branding": {"title": "BrickflowUI Launch Site"},
    "colors": {
        "primary": "#0F766E",
        "primary_hover": "#115E59",
        "background": "#F8FAFC",
        "surface": "#FFFFFF",
        "text": "#0F172A",
        "text_muted": "#475569",
        "border": "#E2E8F0",
        "success": "#15803D",
        "warning": "#C2410C",
        "error": "#B91C1C",
    },
    "surfaces": {
        "canvas": "#F8FAFC",
        "muted": "#F1F5F9",
        "overlay": "rgba(255,255,255,0.88)",
    },
}

app = db.App(theme=LANDING_THEME)

FEATURES = [
    {"title": "Launch internal tools faster", "body": "Compose rich screens in pure Python without rebuilding your frontend stack from scratch."},
    {"title": "Deploy on Databricks Apps", "body": "Run dashboards, portals, and internal web apps with a runtime model that fits data teams."},
    {"title": "Polish without fighting CSS", "body": "Use theme tokens, motion props, and reusable surfaces to make enterprise apps feel premium."},
]

ROADMAP = [
    {"title": "Discover", "time": "Week 1", "subtitle": "Prototype quickly", "description": "Start with mock data and a business-friendly layout."},
    {"title": "Connect", "time": "Week 2", "subtitle": "Wire real sources", "description": "Connect Databricks SQL or platform APIs."},
    {"title": "Roll out", "time": "Week 3", "subtitle": "Harden UX", "description": "Add access control, empty states, and graceful retries."},
]


@app.page("/", title="Landing Site", icon="Home")
def home():
    show_toast, set_show_toast = db.use_state(False)
    show_drawer, set_show_drawer = db.use_state(False)

    return db.Column(
        [
            db.Toast(
                "A launch note was queued for your team. This is how announcements or sign-up confirmations can feel in production.",
                title="Nice touch",
                type="success",
                visible=show_toast,
                icon="CheckCircle",
            ),
            db.Row(
                [
                    db.Text("BrickflowUI Launch Site", variant="h3"),
                    db.Row(
                        [
                            db.Button("Preview launch brief", on_click=lambda: set_show_drawer(True), variant="outline"),
                            db.Button("Celebrate polish", on_click=lambda: set_show_toast(True)),
                        ],
                        gap=2,
                    ),
                ],
                justify="between",
                align="center",
            ),
            db.Card(
                [
                    db.Badge("Landing page recipe", color="green"),
                    db.Spacer(3),
                    db.Text("Ship internal products with the confidence of a real website", variant="h1"),
                    db.Spacer(2),
                    db.Text(
                        "This example shows how BrickflowUI can be used beyond dashboards: hero sections, feature storytelling, roadmap blocks, FAQ, and polished calls to action.",
                        muted=True,
                    ),
                    db.Spacer(4),
                    db.Row(
                        [
                            db.Button("Start a project", animated=True),
                            db.Button("Read the docs", variant="secondary"),
                        ],
                        gap=2,
                    ),
                    db.Spacer(4),
                    db.Grid(
                        [
                            db.SparklineStat(
                                label="Teams onboarded",
                                value="24",
                                data=[{"week": "W1", "value": 8}, {"week": "W2", "value": 12}, {"week": "W3", "value": 18}, {"week": "W4", "value": 24}],
                                x_key="week",
                                y_key="value",
                                delta="+9 this month",
                                delta_type="increase",
                            ),
                            db.SparklineStat(
                                label="Prototype time",
                                value="2.5 days",
                                data=[{"week": "W1", "value": 5}, {"week": "W2", "value": 4}, {"week": "W3", "value": 3}, {"week": "W4", "value": 2.5}],
                                x_key="week",
                                y_key="value",
                                delta="-40%",
                                delta_type="decrease",
                                color="#0F766E",
                            ),
                        ],
                        cols=2,
                        gap=4,
                    ),
                ],
                elevated=True,
                animated=True,
                animation="fade-up",
                style={
                    "background": "radial-gradient(circle at top left, rgba(15,118,110,0.14), transparent 28%), linear-gradient(135deg, #ffffff 0%, #f0fdfa 100%)",
                },
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Text(item["title"], variant="h3"),
                            db.Spacer(2),
                            db.Text(item["body"], muted=True),
                        ],
                        elevated=True,
                        animated=True,
                        animation_delay=0.05 * index,
                    )
                    for index, item in enumerate(FEATURES)
                ],
                cols=3,
                gap=4,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Text("Delivery path", variant="h3"),
                            db.Spacer(2),
                            db.Timeline(ROADMAP),
                        ],
                        elevated=True,
                    ),
                    db.Card(
                        [
                            db.Text("Frequently asked questions", variant="h3"),
                            db.Spacer(2),
                            db.Accordion(
                                [
                                    db.AccordionItem("Can this be used for marketing-like pages?", [db.Text("Yes. Landing pages, launch notes, and internal microsites are now straightforward compositions.")]),
                                    db.AccordionItem("Do I need custom JavaScript?", [db.Text("No. The goal is to keep the interaction model in Python while the frontend runtime stays pre-built and optimized.")]),
                                    db.AccordionItem("Can I mix this with dashboards?", [db.Text("Yes. The same theme, components, and layout system can power your landing site, chatbot surface, and operational dashboard.")]),
                                ],
                                default_open=[0],
                            ),
                        ],
                        elevated=True,
                    ),
                ],
                cols=2,
                gap=4,
            ),
            db.Drawer(
                visible=show_drawer,
                title="Launch brief",
                on_close=lambda: set_show_drawer(False),
                children=[
                    db.Text("Use a drawer for supporting narrative, sign-up context, release notes, or executive talking points."),
                    db.Spacer(3),
                    db.Alert("This layout intentionally feels calmer and more editorial than a typical dashboard.", type="info", title="Design note"),
                    db.Spacer(3),
                    db.Breadcrumbs(
                        [
                            {"label": "Marketing"},
                            {"label": "Launch"},
                            {"label": "Preview"},
                        ]
                    ),
                ],
            ),
        ],
        gap=6,
        padding=6,
        style={"maxWidth": "1320px", "margin": "0 auto"},
    )


if __name__ == "__main__":
    app.run()
