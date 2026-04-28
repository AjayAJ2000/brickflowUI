# Content And Feedback

These components communicate meaning, status, progress, and narrative.

## Typography

### `Text`

```python
db.Text("Executive Summary", variant="h1")
db.Text("Muted helper copy", variant="caption", muted=True)
db.Text("Inline label", variant="label", bold=True)
```

Variants:

- `h1`
- `h2`
- `h3`
- `h4`
- `body`
- `caption`
- `code`
- `label`

### `Code`

Use `Code` for examples, SQL snippets, and API payloads.

## Status and feedback

### `Badge`

```python
db.Badge("Healthy", color="green")
db.Badge("At Risk", color="red")
```

### `Alert`

```python
db.Alert(
    "The silver quality checks are behind schedule.",
    type="warning",
    title="Pipeline Attention Needed",
    dismissible=True,
)
```

### `Toast`

Use `Toast` for transient feedback after an action.

```python
show_toast, set_show_toast = db.use_state(False)

db.Toast(
    "Action plan saved",
    title="Success",
    type="success",
    visible=show_toast,
    on_close=lambda: set_show_toast(False),
    auto_hide_ms=3000,
)
```

### `Spinner`

Use `Spinner("sm")`, `Spinner("md")`, or `Spinner("lg")` for direct loading indicators.

## Progress and KPI components

### `Progress`

```python
db.Progress(83, label="Validation completeness")
```

### `Stat`

```python
db.Stat(
    label="Freshness",
    value="11 min",
    delta="-3 min",
    delta_type="decrease",
    animated=True,
)
```

### `SparklineStat`

```python
db.SparklineStat(
    label="Cost per run",
    value="$42",
    data=[{"day": "Mon", "value": 38}, {"day": "Tue", "value": 42}],
    x_key="day",
    y_key="value",
)
```

## Empty and narrative components

### `EmptyState`

```python
db.EmptyState(
    title="No failed jobs",
    message="The current filter set has no matching incidents.",
    actions=[db.Button("Reset Filters")],
)
```

### `Timeline`

```python
db.Timeline(
    [
        {"title": "Bronze job started", "time": "09:10"},
        {"title": "Silver quality check", "time": "09:22", "description": "2 warnings"},
    ],
    title="Run History",
)
```

## Media

### `Image`

Use `Image` when you want screenshots, diagrams, photos, or branded illustrations inside the app.

```python
db.Image(
    src="https://example.com/pipeline-map.png",
    alt="Pipeline map",
    caption="Current production ingestion flow",
    fit="contain",
)
```

Useful props:

- `src`
- `alt`
- `width`
- `height`
- `fit`
- `caption`
- `radius`
- `loading`
