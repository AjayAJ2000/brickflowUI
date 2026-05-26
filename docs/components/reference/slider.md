# Slider

## What It Does

Adjusts numeric values across a bounded range.

## Signature

```python
db.Slider(name: 'str', label: 'Optional[str]' = None, min: 'float' = 0, max: 'float' = 100, step: 'float' = 1, value: 'float' = 0, on_change: 'Optional[Callable[[float], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | `str` | `required` | |
| `label` | `Optional[str]` | `None` | |
| `min` | `float` | `0` | |
| `max` | `float` | `100` | |
| `step` | `float` | `1` | |
| `value` | `float` | `0` | |
| `on_change` | `Optional[Callable[[float], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Slider(name="confidence", label="Confidence", min=0, max=100, step=1, value=72, on_change=lambda value: None)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
