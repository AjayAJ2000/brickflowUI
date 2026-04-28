# Inputs And Forms

These components collect user intent and move it back into Python handlers.

## `Button`

```python
db.Button("Refresh", on_click=refresh, variant="primary")
db.Button("Cancel", on_click=close, variant="ghost")
```

Useful props:

- `label`
- `on_click`
- `variant`
- `icon`
- `disabled`
- `loading`

## `Input`

```python
query, set_query = db.use_state("")

db.Input(
    name="query",
    label="Search Pipelines",
    value=query,
    placeholder="Search by owner or table",
    on_change=set_query,
)
```

Supported types:

- `text`
- `password`
- `email`
- `number`
- `url`
- `search`
- `date`
- `textarea`

## `Select`

```python
db.Select(
    name="site",
    label="Site",
    value=site,
    options=[{"label": "Toyama", "value": "toyama"}],
    on_change=set_site,
)
```

## `Checkbox`

```python
db.Checkbox(
    name="critical_only",
    label="Only critical incidents",
    checked=critical_only,
    on_change=set_critical_only,
)
```

## `Toggle`

```python
db.Toggle(
    name="auto_refresh",
    label="Auto refresh",
    checked=auto_refresh,
    on_change=set_auto_refresh,
)
```

## `Slider`

```python
db.Slider(
    name="confidence",
    label=f"Minimum confidence: {confidence}",
    min=80,
    max=100,
    step=1,
    value=confidence,
    on_change=set_confidence,
)
```

## `DateRangePicker`

```python
window, set_window = db.use_state({"start": "", "end": ""})

db.DateRangePicker(
    name="window",
    label="Observation window",
    start=window["start"],
    end=window["end"],
    on_change=set_window,
)
```

## `MultiSelect`

```python
db.MultiSelect(
    name="layers",
    label="Pipeline Layers",
    values=layers,
    options=[
        {"label": "Bronze", "value": "bronze"},
        {"label": "Silver", "value": "silver"},
        {"label": "Gold", "value": "gold"},
    ],
    on_change=set_layers,
)
```

## `ChatInput`

Use `ChatInput` for assistant and copilot interactions.

```python
prompt, set_prompt = db.use_state("")

db.ChatInput(
    value=prompt,
    placeholder="Ask about freshness, failures, or cost",
    on_change=set_prompt,
    on_submit=submit_prompt,
)
```

## `Form`

Use `Form` when you want a real HTTP submission to `@app.route(...)`.

```python
db.Form(
    [
        db.Input(name="owner", label="Owner"),
        db.Input(name="summary", label="Summary"),
        db.Button("Create Action Plan", html_type="submit"),
    ],
    action="/api/action-plan",
    method="POST",
    reload_on_success=True,
)
```

## Recommended filter-bar pattern

```python
db.Card(
    [
        db.Grid(
            [
                db.Input(...),
                db.Select(...),
                db.DateRangePicker(...),
                db.MultiSelect(...),
            ],
            cols=4,
            gap=4,
        ),
        db.Row(
            [
                db.Checkbox(...),
                db.Toggle(...),
                db.Button("Apply"),
            ],
            justify="between",
            wrap=True,
        ),
    ],
    bordered=True,
)
```
