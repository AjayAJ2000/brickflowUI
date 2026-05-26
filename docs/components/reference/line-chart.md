# LineChart

## What It Does

Highlights trends, latency, or rate movement across an x-axis.

## Signature

```python
db.LineChart(data: 'List[Dict[str, Any]]', x_key: 'str', y_keys: 'List[str]', title: 'Optional[str]' = None, colors: 'Optional[List[str]]' = None, height: 'int' = 300, loading: 'bool' = False, empty_message: 'str' = 'No chart data available', on_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `x_key` | `str` | `required` | |
| `y_keys` | `List[str]` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `colors` | `Optional[List[str]]` | `None` | |
| `height` | `int` | `300` | |
| `loading` | `bool` | `False` | |
| `empty_message` | `str` | `'No chart data available'` | |
| `on_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.LineChart(data=[{"week": "W01", "latency": 4.2}], x_key="week", y_keys=["runs"], title="Command center")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
