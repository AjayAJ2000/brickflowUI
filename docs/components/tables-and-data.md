# Tables And Data

BrickflowUI tables are designed for practical internal tools.

## `Table`

```python
db.Table(
    data=rows,
    columns=[
        {"key": "pipeline", "label": "Pipeline", "sortable": True},
        {"key": "owner", "label": "Owner"},
        {"key": "freshness", "label": "Freshness", "sortable": True},
    ],
    pagination=10,
    exportable=True,
)
```

Useful props:

- `data`
- `columns`
- `pagination`
- `on_row_click`
- `loading`
- `empty_message`
- `exportable`

## Common patterns

### Loading state

```python
db.Table(data=[], columns=columns, loading=True)
```

### Empty state

```python
db.Table(data=[], columns=columns, empty_message="No late pipelines")
```

### Row drilldown

```python
selected, set_selected = db.use_state(None)
show_drawer, set_show_drawer = db.use_state(False)

def open_row(row):
    set_selected(row)
    set_show_drawer(True)

db.Table(data=rows, columns=columns, on_row_click=open_row)
```

Then pair it with:

```python
db.Drawer(
    visible=show_drawer,
    title="Pipeline Detail",
    on_close=lambda: set_show_drawer(False),
    children=[db.Text(str(selected))],
)
```

## Table composition pattern

```python
db.Card(
    [
        db.SectionHeader(
            "Pipeline Inventory",
            subtitle="Sortable operational view",
            actions=[db.Button("Refresh")],
        ),
        db.Table(...),
    ],
    bordered=True,
)
```
