# DateRangePicker

## What It Does

Captures a start and end date in one controlled component.

## Signature

```python
db.DateRangePicker(name: 'str', label: 'Optional[str]' = None, start: 'str' = '', end: 'str' = '', on_change: 'Optional[Callable[[Dict[str, str]], None]]' = None, disabled: 'bool' = False, loading: 'bool' = False) -> 'VNode'
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

## Example

```python
import brickflowui as db

node = db.DateRangePicker(name="window", label="Window", start="2026-05-01", end="2026-05-07", on_change=lambda value: None)
```

## Integration Notes

- DateRangePicker emits a dictionary shaped like `{"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}`.
- Use it for filters, compare-period controls, and data-refresh windows.
