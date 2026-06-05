# Row

## What It Does

Lays out child components horizontally with optional wrapping and alignment controls.

## Signature

```python
db.Row(children: 'List[VNode]', gap: 'int' = 2, wrap: 'bool' = False, align: "Literal['start', 'center', 'end', 'stretch']" = 'center', justify: "Literal['start', 'center', 'end', 'between', 'around']" = 'start', **kwargs) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `children` | `List[VNode]` | `required` | |
| `gap` | `int` | `2` | |
| `wrap` | `bool` | `False` | |
| `align` | `Literal['start', 'center', 'end', 'stretch']` | `'center'` | |
| `justify` | `Literal['start', 'center', 'end', 'between', 'around']` | `'start'` | |

## Example

```python
import brickflowui as db

node = db.Row([db.Badge("Healthy", color="green"), db.Button("Refresh", variant="secondary")], gap=2, wrap=True)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
