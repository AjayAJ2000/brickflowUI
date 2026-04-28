# Navigation And Overlays

These components shape how users move through the app and open secondary workflows.

## `Sidebar` and `NavItem`

Multi-page apps get an app shell automatically. If you want to build it manually or understand the primitive:

```python
db.Sidebar(
    [
        db.NavItem("Overview", "/"),
        db.NavItem("Pipelines", "/pipelines", icon="GitBranch"),
    ],
    brand_name="Data Ops",
)
```

On mobile the sidebar becomes toggle-based navigation.

## `Breadcrumbs`

```python
db.Breadcrumbs(
    [
        {"label": "Home", "path": "/"},
        {"label": "Pipelines", "path": "/pipelines"},
        {"label": "Bronze Orders"},
    ]
)
```

## `Tabs` and `TabItem`

Use tabs when multiple sub-workflows belong to the same page.

```python
db.Tabs(
    [
        db.TabItem("Summary", [db.Text("Overview")]),
        db.TabItem("Incidents", [db.Text("Incident list")]),
    ]
)
```

## `Modal`

Use `Modal` for focused workflows with background interruption.

```python
db.Modal(
    visible=show_modal,
    title="Approve Release",
    on_close=lambda: set_show_modal(False),
    children=[db.Text("Review the release checklist.")],
)
```

## `Drawer`

Use `Drawer` when the main page should stay visible while details slide in.

```python
db.Drawer(
    visible=show_drawer,
    title="Pipeline Detail",
    side="right",
    on_close=lambda: set_show_drawer(False),
    children=[db.Text("Row-level drilldown goes here.")],
)
```

## `Popup`

Use `Popup` for lightweight confirm or helper flows that should feel smaller than a full modal.

```python
db.Popup(
    visible=show_popup,
    title="Quick Note",
    on_close=lambda: set_show_popup(False),
    children=[db.Text("Acknowledge and continue.")],
)
```

## `Accordion` and `AccordionItem`

Use an accordion for FAQs, operator notes, advanced settings, or playbook steps.

```python
db.Accordion(
    [
        db.AccordionItem("What happened?", [db.Text("Pipeline lag increased at 09:30")]),
        db.AccordionItem("Recommended action", [db.Text("Re-run the silver validation task")]),
    ],
    default_open=[0],
)
```

## Overlay selection guide

- Use `Modal` for a blocking focused task.
- Use `Drawer` for a side-panel detail workflow.
- Use `Popup` for a small helper or confirm surface.
- Use `Accordion` when the content should stay inline instead of floating.
