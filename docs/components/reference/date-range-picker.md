# DateRangePicker

## What It Does

Captures a start and end date in one controlled component.

## Signature

```python
db.DateRangePicker(name: 'str', label: 'Optional[str]' = None, start: 'str' = '', end: 'str' = '', on_change: 'Optional[Callable[[Dict[str, str]], None]]' = None, disabled: 'bool' = False, loading: 'bool' = False, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | `str` | `required` | |
| `label` | `Optional[str]` | `None` | |
| `start` | `str` | `''` | |
| `end` | `str` | `''` | |
| `on_change` | `Optional[Callable[[Dict[str, str]], None]]` | `None` | |
| `disabled` | `bool` | `False` | |
| `loading` | `bool` | `False` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.DateRangePicker(name="window", label="Window", start="2026-05-01", end="2026-05-07", on_change=lambda value: None)
```

## Integration Notes

- DateRangePicker emits a dictionary shaped like `{"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}`.
- Use it for filters, compare-period controls, and data-refresh windows.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
