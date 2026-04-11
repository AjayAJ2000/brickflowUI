from __future__ import annotations

import brickflowui as db


CHAT_THEME = {
    "branding": {"title": "BrickflowUI Chatbot Workspace"},
    "colors": {
        "primary": "#5B21B6",
        "primary_hover": "#4C1D95",
        "background": "#F6F6FB",
        "surface": "#FFFFFF",
        "text": "#1F2937",
        "text_muted": "#6B7280",
        "border": "#E5E7EB",
        "success": "#0F9D6C",
        "warning": "#D97706",
        "error": "#DC2626",
    },
    "surfaces": {
        "canvas": "#F6F6FB",
        "muted": "#F3F4F6",
        "overlay": "rgba(255,255,255,0.92)",
    },
    "motion": {
        "duration_normal": "260ms",
        "easing_standard": "cubic-bezier(0.22, 1, 0.36, 1)",
    },
}

app = db.App(theme=CHAT_THEME)

STARTER_MESSAGES = [
    {
        "role": "assistant",
        "title": "Pipeline copilot",
        "body": "I can help summarize overnight failures, explain a KPI spike, or draft a stakeholder update.",
    },
    {
        "role": "user",
        "title": "Ajay",
        "body": "Summarize the overnight data platform incidents for leadership.",
    },
    {
        "role": "assistant",
        "title": "Pipeline copilot",
        "body": "Two pipelines need attention. Orders Lakehouse missed its freshness target by 18 minutes, and ML Features had four incidents tied to upstream schema drift.",
    },
]

TRACE_ITEMS = [
    {"title": "Intent parsed", "time": "09:14", "subtitle": "Executive summary", "description": "Detected request type and tone"},
    {"title": "Warehouse queried", "time": "09:14", "subtitle": "Databricks SQL", "description": "Fetched last 24 hours of pipeline metrics"},
    {"title": "Response composed", "time": "09:15", "subtitle": "Narrative draft", "description": "Prepared a concise leadership-friendly answer"},
]

MODE_OPTIONS = [
    {"label": "Executive summary", "value": "executive"},
    {"label": "Engineering detail", "value": "engineering"},
    {"label": "Customer-safe wording", "value": "customer"},
]


def message_card(message: dict, index: int) -> db.VNode:
    tone = {
        "assistant": {"background": "linear-gradient(180deg, #ffffff 0%, #f5f3ff 100%)", "border": "1px solid rgba(91, 33, 182, 0.12)"},
        "user": {"background": "linear-gradient(180deg, #ffffff 0%, #eef2ff 100%)", "border": "1px solid rgba(79, 70, 229, 0.12)"},
    }[message["role"]]
    return db.Card(
        [
            db.Row(
                [
                    db.Text(message["title"], variant="h4"),
                    db.Badge("Assistant" if message["role"] == "assistant" else "User", color="purple" if message["role"] == "assistant" else "blue"),
                ],
                justify="between",
            ),
            db.Spacer(2),
            db.Text(message["body"]),
        ],
        animated=True,
        animation="fade-up",
        animation_delay=0.05 * index,
        style=tone,
    )


@app.page("/", title="Chatbot Workspace", icon="Sparkles")
def home():
    messages, set_messages = db.use_state(STARTER_MESSAGES)
    draft, set_draft = db.use_state("")
    modes, set_modes = db.use_state(["executive"])
    selected_window, set_selected_window = db.use_state({"start": "2026-04-01", "end": "2026-04-07"})
    show_trace, set_show_trace = db.use_state(False)
    toast_visible, set_toast_visible = db.use_state(False)

    def send_message():
        if not draft.strip():
            return
        next_messages = list(messages)
        next_messages.append({"role": "user", "title": "Ajay", "body": draft.strip()})
        next_messages.append(
            {
                "role": "assistant",
                "title": "Pipeline copilot",
                "body": f"I used the {', '.join(modes)} mode for {selected_window['start']} to {selected_window['end']} and prepared a concise response: {draft.strip()}",
            }
        )
        set_messages(next_messages)
        set_draft("")
        set_toast_visible(True)

    return db.Column(
        [
            db.Toast(
                "Response drafted successfully. You can now review sources in the trace drawer.",
                title="Chat updated",
                type="success",
                icon="CheckCircle",
                visible=toast_visible,
            ),
            db.Breadcrumbs(
                [
                    {"label": "Examples", "path": "/"},
                    {"label": "Chatbot Workspace"},
                ]
            ),
            db.Row(
                [
                    db.Column(
                        [
                            db.Text("Chatbot workspace", variant="h1"),
                            db.Text(
                                "A polished assistant-style UI built entirely with BrickflowUI primitives, including controls, drawers, timelines, and multi-value inputs.",
                                muted=True,
                            ),
                        ],
                        gap=1,
                    ),
                    db.Row(
                        [
                            db.Button("Open trace", on_click=lambda: set_show_trace(True), variant="outline", icon="Activity"),
                            db.Button("Clear toast", on_click=lambda: set_toast_visible(False), variant="secondary"),
                        ],
                        gap=2,
                    ),
                ],
                justify="between",
                wrap=True,
            ),
            db.Grid(
                [
                    db.Card(
                        [
                            db.Text("Conversation controls", variant="h3"),
                            db.Spacer(2),
                            db.DateRangePicker(
                                name="window",
                                label="Observation window",
                                start=selected_window["start"],
                                end=selected_window["end"],
                                on_change=set_selected_window,
                            ),
                            db.Spacer(3),
                            db.MultiSelect(
                                name="modes",
                                label="Answer style",
                                options=MODE_OPTIONS,
                                values=modes,
                                on_change=set_modes,
                            ),
                            db.Spacer(3),
                            db.Accordion(
                                [
                                    db.AccordionItem(
                                        "Prompt guidance",
                                        [
                                            db.Text("Use this panel for reusable system instructions, operating rules, or escalation criteria."),
                                        ],
                                        subtitle="Best-practice prompt notes",
                                    ),
                                    db.AccordionItem(
                                        "Connected tools",
                                        [
                                            db.Text("Databricks SQL"),
                                            db.Text("Pipeline metrics warehouse", variant="caption", muted=True),
                                        ],
                                        subtitle="Available at runtime",
                                    ),
                                ],
                                default_open=[0],
                            ),
                        ],
                        elevated=True,
                    ),
                    db.Column(
                        [
                            db.Card(
                                [
                                    db.Row(
                                        [
                                            db.Text("Conversation", variant="h3"),
                                            db.Badge(f"{len(messages)} messages", color="purple"),
                                        ],
                                        justify="between",
                                    ),
                                    db.Spacer(3),
                                    db.Column(
                                        [message_card(message, index) for index, message in enumerate(messages)]
                                        if messages
                                        else [db.EmptyState("No messages yet", "Start by asking the assistant to summarize a KPI, debug a pipeline, or draft an update.")],
                                        gap=3,
                                    ),
                                ],
                                elevated=True,
                            ),
                            db.Card(
                                [
                                    db.Input(
                                        name="chat_draft",
                                        label="Message",
                                        placeholder="Ask about pipeline health, write a release note, or explain a metric swing...",
                                        value=draft,
                                        on_change=set_draft,
                                    ),
                                    db.Spacer(2),
                                    db.Row(
                                        [
                                            db.Button("Send", on_click=send_message, icon="PlayCircle", animated=True),
                                            db.Button("Add sample question", on_click=lambda: set_draft("Explain why the gold layer freshness dropped."), variant="secondary"),
                                        ],
                                        justify="between",
                                        wrap=True,
                                    ),
                                ],
                                elevated=True,
                            ),
                        ],
                        gap=4,
                    ),
                ],
                cols=2,
                gap=4,
            ),
            db.Drawer(
                visible=show_trace,
                title="Response trace",
                on_close=lambda: set_show_trace(False),
                children=[
                    db.Text("Use the drawer to show citations, execution traces, or tool call summaries without leaving the conversation."),
                    db.Spacer(3),
                    db.Timeline(TRACE_ITEMS, title="Runtime timeline"),
                ],
            ),
        ],
        gap=5,
        padding=6,
        style={"maxWidth": "1380px", "margin": "0 auto"},
    )


if __name__ == "__main__":
    app.run()
