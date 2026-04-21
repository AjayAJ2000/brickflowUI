import brickflowui as db


def test_new_components_serialize_expected_props_and_nested_actions():
    node = db.Column(
        [
            db.Breadcrumbs(
                [
                    {"label": "Home", "path": "/"},
                    {"label": "Studio", "path": "/studio"},
                    {"label": "Preview"},
                ]
            ),
            db.EmptyState(
                title="No pipelines",
                message="Add a pipeline or adjust your filters.",
                actions=[db.Button("Create", on_click=lambda: None)],
            ),
            db.Drawer(visible=True, title="Details", children=[db.Text("Body")]),
            db.Accordion(
                [
                    db.AccordionItem("Section A", [db.Text("A content")]),
                    db.AccordionItem("Section B", [db.Text("B content")]),
                ],
                default_open=[0],
                allow_multiple=True,
            ),
            db.DateRangePicker(name="window", start="2026-04-01", end="2026-04-07"),
            db.MultiSelect(
                name="layers",
                options=[{"label": "Bronze", "value": "bronze"}],
                values=["bronze"],
            ),
            db.Toast("Saved", title="Success"),
            db.Timeline([{"title": "Run started", "time": "09:30"}]),
            db.SparklineStat(
                label="Freshness",
                value="17 min",
                data=[{"day": "Mon", "value": 12}, {"day": "Tue", "value": 17}],
                x_key="day",
                y_key="value",
            ),
        ]
    )

    payload = node.serialize({})
    rendered_types = [child["type"] for child in payload["children"]]

    assert "Breadcrumbs" in rendered_types
    assert "EmptyState" in rendered_types
    assert "Drawer" in rendered_types
    assert "Accordion" in rendered_types
    assert "DateRangePicker" in rendered_types
    assert "MultiSelect" in rendered_types
    assert "Toast" in rendered_types
    assert "Timeline" in rendered_types
    assert "SparklineStat" in rendered_types

    empty_state = next(child for child in payload["children"] if child["type"] == "EmptyState")
    assert empty_state["props"]["title"] == "No pipelines"
    assert empty_state["props"]["actions"][0]["type"] == "Button"


def test_chart_components_expose_loading_empty_and_click_handlers():
    chart = db.BarChart(
        data=[],
        x_key="week",
        y_keys=["runs"],
        loading=True,
        empty_message="Nothing here",
        on_click=lambda payload: payload,
    )

    registry = {}
    payload = chart.serialize(registry)

    assert payload["props"]["loading"] is True
    assert payload["props"]["emptyMessage"] == "Nothing here"
    assert "click" in payload["props"]
    assert payload["props"]["click"] in registry


def test_table_can_be_marked_exportable():
    table = db.Table(
        data=[{"id": 1, "name": "A"}],
        columns=[{"key": "id", "label": "ID"}, {"key": "name", "label": "Name"}],
        exportable=True,
    )

    payload = table.serialize({})

    assert payload["props"]["exportable"] is True


def test_015_visual_components_serialize_callbacks_and_props():
    node = db.Column(
        [
            db.Hero(
                "Pipeline command center",
                subtitle="Observe jobs, tables, and SLAs.",
                eyebrow="Data platform",
                badges=[db.Badge("Live", color="green")],
                actions=[db.Button("Refresh")],
            ),
            db.SectionHeader("Lakehouse health", actions=[db.Button("Export")]),
            db.StatusStrip([{"label": "Freshness", "value": "11m", "status": "healthy"}]),
            db.Stepper([{"label": "Bronze"}, {"label": "Silver"}], active=1),
            db.KanbanBoard(
                [{"id": "todo", "label": "Todo", "cards": [{"id": "a", "title": "Fix SLA"}]}],
                on_card_click=lambda payload: payload,
            ),
            db.ChatMessage("assistant", "I found two delayed jobs.", name="Ops Copilot"),
            db.ChatInput(on_change=lambda value: value, on_submit=lambda value: value),
        ]
    )

    registry = {}
    payload = node.serialize(registry)
    rendered_types = [child["type"] for child in payload["children"]]

    assert "Hero" in rendered_types
    assert "SectionHeader" in rendered_types
    assert "StatusStrip" in rendered_types
    assert "Stepper" in rendered_types
    assert "KanbanBoard" in rendered_types
    assert "ChatMessage" in rendered_types
    assert "ChatInput" in rendered_types

    kanban = next(child for child in payload["children"] if child["type"] == "KanbanBoard")
    chat_input = next(child for child in payload["children"] if child["type"] == "ChatInput")

    assert kanban["props"]["cardClick"] in registry
    assert chat_input["props"]["change"] in registry
    assert chat_input["props"]["submit"] in registry


def test_015_chart_and_pipeline_components_serialize_expected_props():
    charts = [
        db.ScatterChart([{"x": 1, "y": 2}], x_key="x", y_key="y", on_click=lambda payload: payload),
        db.ComposedChart([{"day": "Mon", "runs": 10, "sla": 96}], x_key="day", bar_keys=["runs"], line_keys=["sla"]),
        db.GaugeChart(91, label="Reliability"),
        db.RadarChart([{"metric": "Freshness", "score": 90}], angle_key="metric", value_keys=["score"]),
        db.Heatmap([{"hour": "09", "layer": "Bronze", "failures": 1}], x_key="hour", y_key="layer", value_key="failures"),
        db.FunnelChart([{"label": "Raw", "value": 100}]),
        db.TreeMap([{"name": "Storage", "value": 42}]),
        db.PipelineGraph(
            nodes=[{"id": "bronze", "label": "Bronze", "status": "running"}],
            edges=[],
            on_node_click=lambda payload: payload,
        ),
    ]

    registry = {}
    payloads = [chart.serialize(registry) for chart in charts]
    types = [payload["type"] for payload in payloads]

    assert types == [
        "ScatterChart",
        "ComposedChart",
        "GaugeChart",
        "RadarChart",
        "Heatmap",
        "FunnelChart",
        "TreeMap",
        "PipelineGraph",
    ]
    assert payloads[0]["props"]["click"] in registry
    assert payloads[-1]["props"]["nodeClick"] in registry
