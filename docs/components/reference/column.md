# Column

## What It Does

Stacks child components vertically with consistent spacing.

## Signature

```python
db.Column(children: 'List[VNode]', gap: 'int' = 2, padding: 'int' = 0, align: "Literal['start', 'center', 'end', 'stretch']" = 'stretch', **kwargs) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `children` | `List[VNode]` | `required` | |
| `gap` | `int` | `2` | |
| `padding` | `int` | `0` | |
| `align` | `Literal['start', 'center', 'end', 'stretch']` | `'stretch'` | |

## Example

```python
import brickflowui as db

node = db.Column([db.Text("Pipeline health", variant="h3"), db.Text("Everything is healthy.", muted=True)], gap=2)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
