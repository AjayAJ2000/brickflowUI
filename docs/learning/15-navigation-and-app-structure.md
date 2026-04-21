# 15. Navigation And App Structure

## Learning Goal

Structure larger apps with pages, tabs, view state, sidebars, drawers, and modals.

## Multiple Pages

```python
@app.page("/", title="Overview")
def overview():
    return db.Text("Overview", variant="h1")

@app.page("/pipelines", title="Pipelines")
def pipelines():
    return db.Text("Pipelines", variant="h1")
```

Use pages when the URL should represent a different screen.

## State-Based Views

Use state when views are part of one workflow:

```python
view, set_view = db.use_state("overview")

nav = db.Row(
    [
        db.Button("Overview", on_click=lambda: set_view("overview")),
        db.Button("Health", on_click=lambda: set_view("health")),
    ]
)

content = overview_view() if view == "overview" else health_view()

return db.Column([nav, content])
```

## Tabs

Use tabs for related sub-sections:

```python
db.Tabs(
    [
        db.TabItem("Runs", [db.Table(runs)]),
        db.TabItem("Incidents", [db.Table(incidents)]),
    ]
)
```

## Drawers

Use drawers for drilldowns:

```python
open_drawer, set_open_drawer = db.use_state(False)

db.Drawer(
    visible=open_drawer,
    title="Pipeline Details",
    on_close=lambda: set_open_drawer(False),
    children=[db.Text("Details go here")],
)
```

## Modals

Use modals for focused actions:

- confirm
- submit
- acknowledge
- create action plan

## Common Mistakes

- Creating too many pages when tabs would be simpler.
- Hiding important dashboard context inside modals.
- Using a modal for information users need to compare.
- Not giving drawers an obvious close action.

## Exercise

Create a page with top navigation buttons, three state-based views, a row-click drawer, and a modal for creating an action plan.

## Checkpoint

You should be able to choose between pages, tabs, state views, drawers, and modals.
