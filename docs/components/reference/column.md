# Column

## What It Does

Column stacks child components vertically with consistent spacing.

## When To Use It

Use `Column` when you want a purposeful, reusable building block instead of hand-assembling HTML-like structure in every page.

## Typical Pattern

```python
import brickflowui as db

node = db.Column(...)
```

## Inputs To Know

Check the Python signature in the installed package or API reference for the full list. In practice, most teams should focus on:

- content props that define what the user sees
- state props that keep the component controlled from Python
- event props such as `on_change`, `on_click`, or `on_close`
- additive visual props such as `animated`, `animation`, and `animation_delay` when supported

## Works Well With

Row, Grid, Card

## Example

```python
import brickflowui as db

example = db.Card([
    db.Text("Column example", variant="h3"),
    db.Text("Replace this with real app data or actions.", muted=True),
])
```

## Notes

- BrickflowUI components are designed to compose with each other cleanly.
- Prefer controlled state from Python when the value matters to your business logic.
- When you need stronger visual polish, layer the component inside `Card`, `Grid`, `Hero`, or `SectionHeader` rather than over-customizing every instance.
