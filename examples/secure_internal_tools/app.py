from __future__ import annotations

from pathlib import Path

import brickflowui as db


REPO_ROOT = Path(__file__).resolve().parents[2]
LOGO = REPO_ROOT / "docs" / "assets" / "brickflowui-mark.svg"

app = db.App(
    title="Secure Internal Tools Workspace",
    logo=str(LOGO) if LOGO.exists() else None,
    favicon=str(LOGO) if LOGO.exists() else None,
    auth_mode="user",
    auth_provider=db.HeaderAuthProvider(),
    allow_anonymous=False,
    loading={
        "title": "Secure Internal Tools",
        "message": "Verifying identity governance and opening the workspace...",
        "animation": "pulse",
        "asset": str(LOGO) if LOGO.exists() else None,
    },
    theme={
        "branding": {"title": "Secure Internal Tools Workspace"},
        "colors": {
            "primary": "#0F766E",
            "primary_hover": "#115E59",
            "background": "#F7FCFB",
            "surface": "#FFFFFF",
            "text": "#0F172A",
            "text_muted": "#475569",
            "border": "#D8E7E5",
            "info": "#2563EB",
        },
    },
)

STATUS = [
    {"label": "Identity", "value": "HeaderAuthProvider", "status": "success", "detail": "User context resolved per request"},
    {"label": "Governance", "value": "Page roles", "status": "info", "detail": "Each page can be independently restricted"},
    {"label": "Exports", "value": "Controlled", "status": "warning", "detail": "Use policy checks before file release"},
]

QUEUE = [
    {"id": "q1", "title": "Approve access request", "subtitle": "Analytics sandbox", "status": "Queued"},
    {"id": "q2", "title": "Review dataset policy", "subtitle": "Customer 360 curated", "status": "Watch"},
]


@app.page("/", title="Home", icon="Home", access="user")
def home():
    principal = db.current_principal()
    return db.Column(
        [
            db.Hero(
                "Secure internal tools without a custom frontend team",
                subtitle="This example shows how to combine role-aware routing, identity signals, governance surfaces, and workflow components inside one BrickflowUI app.",
                eyebrow="Security and governance",
                badges=[db.Badge("Authenticated", color="green"), db.Badge(", ".join(principal.roles) or "No roles", color="purple")],
                visual=db.Card([db.GaugeChart(96, title="Governance score", label="policy readiness")]),
            ),
            db.StatusStrip(STATUS, title="Security posture"),
            db.Alert("Set x-brickflow-user-id and x-brickflow-user-roles headers when testing locally. Example roles: analyst, admin, security.", type="info"),
        ],
        gap=5,
        padding=5,
    )


@app.page("/ops", title="Operations Desk", icon="LayoutDashboard", access="user", roles=["analyst", "admin", "security"])
def ops():
    drawer_open, set_drawer_open = db.use_state(False)
    popup_open, set_popup_open = db.use_state(False)

    return db.Column(
        [
            db.SectionHeader("Operations desk", subtitle="Use drawers, tables, toasts, and workflow controls for analyst-facing tooling."),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Table(
                                data=[
                                    {"tool": "Lineage explorer", "owner": "Platform", "access": "Analyst", "freshness": "5 min"},
                                    {"tool": "Customer export", "owner": "Operations", "access": "Admin", "freshness": "15 min"},
                                ],
                                columns=[
                                    {"key": "tool", "label": "Tool", "sortable": True},
                                    {"key": "owner", "label": "Owner"},
                                    {"key": "access", "label": "Access"},
                                    {"key": "freshness", "label": "Freshness"},
                                ],
                                exportable=True,
                            )
                        ]
                    ),
                    db.Card(
                        [
                            db.KanbanBoard(
                                [{"id": "review", "label": "Needs review", "cards": QUEUE}],
                                on_card_click=lambda _: set_drawer_open(True),
                            ),
                            db.Spacer(2),
                            db.Button("Raise acknowledgement popup", on_click=lambda: set_popup_open(True), variant="outline"),
                        ]
                    ),
                ],
                cols=2,
                gap=4,
            ),
            db.Drawer(
                visible=drawer_open,
                title="Governance notes",
                on_close=lambda: set_drawer_open(False),
                children=[
                    db.Text("Drawers are useful for evidence trails, policy detail, and operator context without breaking the current page."),
                    db.Spacer(2),
                    db.Timeline([
                        {"title": "Request opened", "time": "08:40", "description": "Access request routed to data governance."},
                        {"title": "Policy matched", "time": "08:47", "description": "Workspace policy matched by entitlement tag."},
                    ]),
                ],
            ),
            db.Popup(
                visible=popup_open,
                title="Governance acknowledgement",
                on_close=lambda: set_popup_open(False),
                children=[
                    db.Text("Use popups for short-lived confirmations that should not interrupt the main tool flow."),
                    db.Spacer(2),
                    db.Button("Acknowledge", on_click=lambda: set_popup_open(False)),
                ],
            ),
        ],
        gap=5,
        padding=5,
    )


@app.page("/admin", title="Admin View", icon="Settings", access="user", roles=["admin"])
def admin():
    return db.Column(
        [
            db.SectionHeader("Admin-only controls", subtitle="Page-level role checks keep high-risk operations separated cleanly."),
            db.Grid(
                [
                    db.Card([db.Stat("Active approvals", "14", delta="+2", delta_type="increase"), db.Text("Review before provisioning or export release.", variant="caption", muted=True)]),
                    db.Card([db.Stat("Policy exceptions", "1", delta="-1", delta_type="decrease"), db.Text("Drive admin work through auditable flows.", variant="caption", muted=True)]),
                    db.Card([db.Stat("Privileged tools", "6", delta="stable", delta_type="neutral"), db.Text("Restrict by role per page or per route.", variant="caption", muted=True)]),
                ],
                cols=3,
                gap=4,
            ),
        ],
        gap=5,
        padding=5,
    )


@app.page("/security", title="Security Review", icon="Lock", access="user", roles=["security", "admin"])
def security():
    return db.Column(
        [
            db.SectionHeader("Security review", subtitle="Identity governance can be visible on every page, not hidden in backend-only code."),
            db.Accordion(
                [
                    db.AccordionItem("What is protected here?", [db.Text("Routing, API access, and the websocket session all share the same principal resolution path.")]),
                    db.AccordionItem("How should teams test this?", [db.Text("Use header-based identities locally, then replace the provider with your enterprise identity source.")]),
                ],
                default_open=[0],
                allow_multiple=True,
            ),
        ],
        gap=5,
        padding=5,
    )


if __name__ == "__main__":
    app.run()
