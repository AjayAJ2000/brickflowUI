# 10. Tables And Data Display

## Learning Goal

Display structured data with tables, badges, empty states, loading states, and row drilldowns.

## Basic Table

```python
rows = [
    {"pipeline": "Orders", "status": "Healthy", "freshness": 12},
    {"pipeline": "Finance", "status": "Watch", "freshness": 47},
]

db.Table(rows)
```

## Explicit Columns

```python
db.Table(
    rows,
    columns=[
        {"key": "pipeline", "label": "Pipeline", "sortable": True},
        {"key": "status", "label": "Status", "sortable": True},
        {"key": "freshness", "label": "Freshness", "sortable": True},
    ],
)
```

## Empty State

```python
db.Table(
    [],
    columns=[{"key": "pipeline", "label": "Pipeline"}],
    empty_message="No pipelines match your filters.",
)
```

## Export CSV

```python
db.Table(rows, exportable=True)
```

This adds a CSV export button in the browser.

## Row Click

```python
selected, set_selected = db.use_state(None)

db.Table(
    rows,
    columns=[...],
    on_row_click=set_selected,
)
```

Then render selected details:

```python
if selected:
    detail = db.Alert(f"Selected {selected['pipeline']}", type="info")
else:
    detail = db.EmptyState("No row selected", "Click a row to inspect it.")
```

## Badge Pattern

```python
def status_badge(status: str):
    color = {
        "Healthy": "green",
        "Watch": "orange",
        "Failed": "red",
    }.get(status, "gray")

    return db.Badge(status, color=color)
```

Tables currently display plain values, so use badges in cards, drawers, or detail sections next to tables.

## Common Mistakes

- Letting tables grow too wide without using focused columns.
- Showing raw technical column names to business users.
- Forgetting empty states.
- Hiding export behind custom code when `exportable=True` is enough.

## Exercise

Create a table of pipeline runs with pipeline, layer, owner, status, freshness, and cost.

Add row click that displays the selected row in an alert or card.

## Checkpoint

You should be able to render useful operational tables with sorting, pagination, empty states, export, and drilldowns.
