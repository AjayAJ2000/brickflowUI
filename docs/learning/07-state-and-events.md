# 07. State And Events

## Learning Goal

Build interactive pages where user actions update state and re-render the UI.

## `use_state`

State is declared inside a page:

```python
value, set_value = db.use_state("initial")
```

Use the value in your UI:

```python
db.Text(f"Current value: {value}")
```

Update it from an event:

```python
db.Button("Change", on_click=lambda: set_value("changed"))
```

## Event Handler Shapes

Different components send different values:

- `Button.on_click` receives no required value.
- `Input.on_change` receives a string.
- `Select.on_change` receives a string.
- `Checkbox.on_change` receives a boolean.
- `Slider.on_change` receives a number.
- `DateRangePicker.on_change` receives `{"start": "...", "end": "..."}`.
- `MultiSelect.on_change` receives `list[str]`.
- `Table.on_row_click` receives the row dictionary.
- `PipelineGraph.on_node_click` receives the node dictionary.
- `ChatInput.on_submit` receives the submitted text.

## Example: Filter State

```python
@app.page("/")
def home():
    layer, set_layer = db.use_state("all")
    urgent_only, set_urgent_only = db.use_state(False)

    rows = [
        {"pipeline": "Orders", "layer": "silver", "status": "watch"},
        {"pipeline": "Finance", "layer": "gold", "status": "healthy"},
    ]

    filtered = [
        row
        for row in rows
        if (layer == "all" or row["layer"] == layer)
        and (not urgent_only or row["status"] == "watch")
    ]

    return db.Column(
        [
            db.Select(
                name="layer",
                label="Layer",
                value=layer,
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "Silver", "value": "silver"},
                    {"label": "Gold", "value": "gold"},
                ],
                on_change=set_layer,
            ),
            db.Checkbox(
                name="urgent",
                label="Urgent only",
                checked=urgent_only,
                on_change=set_urgent_only,
            ),
            db.Table(filtered),
        ]
    )
```

## Common Mistakes

- Forgetting to pass `value=state` into controlled inputs.
- Forgetting to pass `checked=state` into checkbox/toggle controls.
- Calling setters during render instead of inside callbacks.
- Mutating a state list directly.

Bad:

```python
items.append("new")
set_items(items)
```

Better:

```python
set_items([*items, "new"])
```

## Exercise

Create a page with a search input, status select, and table. The table should filter when either control changes.

## Checkpoint

You should understand how user events flow into state and how state drives the next render.
