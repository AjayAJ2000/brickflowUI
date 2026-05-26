# Stat

## What It Does

Shows KPI values with optional deltas and motion-friendly counters.

## Signature

```python
db.Stat(label: 'str', value: 'str', delta: 'Optional[str]' = None, delta_type: "Literal['increase', 'decrease', 'neutral']" = 'neutral', icon: 'Optional[str]' = None, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `str` | `required` | |
| `value` | `str` | `required` | |
| `delta` | `Optional[str]` | `None` | |
| `delta_type` | `Literal['increase', 'decrease', 'neutral']` | `'neutral'` | |
| `icon` | `Optional[str]` | `None` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Stat(label="Pipeline health", value="active", icon="LayoutDashboard", animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
