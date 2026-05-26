# FunnelChart

## What It Does

Shows stage conversion or drop-off across a pipeline.

## Signature

```python
db.FunnelChart(data: 'List[Dict[str, Any]]', value_key: 'str' = 'value', label_key: 'str' = 'label', title: 'Optional[str]' = None, colors: 'Optional[List[str]]' = None, height: 'int' = 300, loading: 'bool' = False, empty_message: 'str' = 'No chart data available', on_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `value_key` | `str` | `'value'` | |
| `label_key` | `str` | `'label'` | |
| `title` | `Optional[str]` | `None` | |
| `colors` | `Optional[List[str]]` | `None` | |
| `height` | `int` | `300` | |
| `loading` | `bool` | `False` | |
| `empty_message` | `str` | `'No chart data available'` | |
| `on_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.FunnelChart(data=[{"label": "Bronze", "value": 120}], title="Command center", height="320px")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
