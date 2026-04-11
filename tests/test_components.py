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
