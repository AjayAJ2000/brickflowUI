# ScatterChart

## What It Does

Plots correlations, clusters, or anomaly candidates.

## Signature

```python
db.ScatterChart(data: 'List[Dict[str, Any]]', x_key: 'str', y_key: 'str', title: 'Optional[str]' = None, group_key: 'Optional[str]' = None, color: 'Optional[str]' = None, height: 'int' = 300, loading: 'bool' = False, empty_message: 'str' = 'No chart data available', on_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `x_key` | `str` | `required` | |
| `y_key` | `str` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `group_key` | `Optional[str]` | `None` | |
| `color` | `Optional[str]` | `None` | |
| `height` | `int` | `300` | |
| `loading` | `bool` | `False` | |
| `empty_message` | `str` | `'No chart data available'` | |
| `on_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.ScatterChart(data=[{"freshness": 12, "cost": 240}], x_key="week", y_key="cost", title="Command center")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
