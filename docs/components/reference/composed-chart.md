# ComposedChart

## What It Does

Combines bars, lines, and areas in one chart.

## Signature

```python
db.ComposedChart(data: 'List[Dict[str, Any]]', x_key: 'str', bar_keys: 'Optional[List[str]]' = None, line_keys: 'Optional[List[str]]' = None, area_keys: 'Optional[List[str]]' = None, title: 'Optional[str]' = None, colors: 'Optional[List[str]]' = None, height: 'int' = 320, loading: 'bool' = False, empty_message: 'str' = 'No chart data available', on_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `x_key` | `str` | `required` | |
| `bar_keys` | `Optional[List[str]]` | `None` | |
| `line_keys` | `Optional[List[str]]` | `None` | |
| `area_keys` | `Optional[List[str]]` | `None` | |
| `title` | `Optional[str]` | `None` | |
| `colors` | `Optional[List[str]]` | `None` | |
| `height` | `int` | `320` | |
| `loading` | `bool` | `False` | |
| `empty_message` | `str` | `'No chart data available'` | |
| `on_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.ComposedChart(data=[{"week": "W01", "runs": 24, "sla": 98}], x_key="week", title="Command center", height="320px")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
