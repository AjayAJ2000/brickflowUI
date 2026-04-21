# 08. Inputs And User Actions

## Learning Goal

Use input components safely so user-provided values become useful app state.

## Inputs Are Controlled

A controlled input receives its current value from state and sends changes back through an event.

```python
query, set_query = db.use_state("")

db.Input(
    name="query",
    label="Search",
    value=query,
    on_change=set_query,
)
```

## Select

```python
layer, set_layer = db.use_state("all")

db.Select(
    name="layer",
    label="Layer",
    value=layer,
    options=[
        {"label": "All", "value": "all"},
        {"label": "Bronze", "value": "bronze"},
        {"label": "Silver", "value": "silver"},
        {"label": "Gold", "value": "gold"},
    ],
    on_change=set_layer,
)
```

## Checkbox

```python
urgent_only, set_urgent_only = db.use_state(False)

db.Checkbox(
    name="urgent",
    label="Only show urgent items",
    checked=urgent_only,
    on_change=set_urgent_only,
)
```

## Slider

```python
min_success, set_min_success = db.use_state(95.0)

db.Slider(
    name="min_success",
    label=f"Minimum success: {min_success:.1f}%",
    min=90,
    max=100,
    step=0.1,
    value=min_success,
    on_change=set_min_success,
)
```

## Date Range

```python
window, set_window = db.use_state({"start": "2026-04-01", "end": "2026-04-07"})

db.DateRangePicker(
    name="window",
    label="Run window",
    start=window["start"],
    end=window["end"],
    on_change=set_window,
)
```

## Multi Select

```python
layers, set_layers = db.use_state(["bronze", "silver"])

db.MultiSelect(
    name="layers",
    label="Layers",
    values=layers,
    options=[
        {"label": "Bronze", "value": "bronze"},
        {"label": "Silver", "value": "silver"},
        {"label": "Gold", "value": "gold"},
    ],
    on_change=set_layers,
)
```

## Chat Input

```python
prompt, set_prompt = db.use_state("")
answer, set_answer = db.use_state("Ask a question.")

db.ChatInput(
    value=prompt,
    on_change=set_prompt,
    on_submit=lambda text: set_answer(f"You asked: {text}"),
)
```

## Common Mistakes

- Missing `name` on inputs used in forms.
- Treating slider values as strings when your logic expects numbers.
- Letting input state and displayed values drift apart.
- Forgetting that `DateRangePicker` returns a dictionary.
- Forgetting that `MultiSelect` returns a list.

## Exercise

Build a control panel with:

- search input
- layer select
- urgent checkbox
- success-rate slider
- date range picker

Show the current values below the controls.

## Checkpoint

You should be able to collect user input, store it in state, and use it to drive UI.
