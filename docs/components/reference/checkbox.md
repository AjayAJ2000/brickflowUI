# Checkbox

## What It Does

Toggles a boolean value with an explicit label.

## Signature

```python
db.Checkbox(name: 'str', label: 'str', checked: 'bool' = False, on_change: 'Optional[Callable[[bool], None]]' = None, disabled: 'bool' = False, loading: 'bool' = False, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | `str` | `required` | |
| `label` | `str` | `required` | |
| `checked` | `bool` | `False` | |
| `on_change` | `Optional[Callable[[bool], None]]` | `None` | |
| `disabled` | `bool` | `False` | |
| `loading` | `bool` | `False` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Checkbox(name="watch_only", label="Only show watchlist", checked=False, on_change=lambda value: None)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Checkbox works best for explicit yes/no or on/off decisions where the label clearly communicates the resulting state.
