# 06. Components And Composition

## Learning Goal

Learn how to create reusable Python helper functions that return BrickflowUI components.

## Why Compose

If you write every card inline, pages become hard to read.

Instead of repeating:

```python
db.Card(
    [
        db.Stat(label="Runs", value="96", delta="+4%"),
        db.Text("Healthy run volume", muted=True),
    ]
)
```

create a helper:

```python
def metric_card(label: str, value: str, delta: str, note: str):
    return db.Card(
        [
            db.Stat(label=label, value=value, delta=delta, delta_type="increase"),
            db.Text(note, variant="caption", muted=True),
        ],
        elevated=True,
        hover=True,
    )
```

Then use:

```python
db.Grid(
    [
        metric_card("Runs", "96", "+4%", "Healthy run volume"),
        metric_card("Success", "99.1%", "+0.3 pts", "Stable reliability"),
    ],
    cols=2,
)
```

## Component Helpers Are Just Python

You can use parameters, if statements, loops, list comprehensions, and data transformations.

Example:

```python
def status_badge(status: str):
    color = {
        "healthy": "green",
        "watch": "orange",
        "failed": "red",
    }.get(status.lower(), "gray")

    return db.Badge(status, color=color)
```

## Pattern: View Functions

For larger apps, split sections into functions:

```python
def overview_view(rows):
    return db.Column(
        [
            db.Text("Overview", variant="h1"),
            db.Grid([...], cols=4),
        ]
    )

def detail_view(rows):
    return db.Column(
        [
            db.Text("Details", variant="h1"),
            db.Table(rows),
        ]
    )
```

Then switch between them:

```python
view, set_view = db.use_state("overview")
content = overview_view(rows) if view == "overview" else detail_view(rows)
return db.Column([nav, content])
```

## Common Mistakes

- Hiding too much state inside helper functions.
- Making helpers depend on global mutable state.
- Returning lists from helpers instead of a single VNode when a VNode is expected.
- Creating helpers that are too generic too early.

## Exercise

Create three helpers:

- `metric_card`
- `section_header`
- `pipeline_badge`

Use them in a small page.

## Checkpoint

You should now be able to make BrickflowUI code readable by composing UI with Python helper functions.
