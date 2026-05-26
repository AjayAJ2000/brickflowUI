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
