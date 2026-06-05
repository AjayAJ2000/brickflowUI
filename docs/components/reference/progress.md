# Progress

## What It Does

Displays completion, readiness, or processing percentages.

## Signature

```python
db.Progress(value: 'float', max: 'float' = 100, label: 'Optional[str]' = None, color: 'str' = 'blue') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `value` | `float` | `required` | |
| `max` | `float` | `100` | |
| `label` | `Optional[str]` | `None` | |
| `color` | `str` | `'blue'` | |

## Example

```python
import brickflowui as db

node = db.Progress(value="active", label="Pipeline health")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
