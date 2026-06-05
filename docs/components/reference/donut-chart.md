# DonutChart

## What It Does

Shows part-to-whole composition in a compact circular chart.

## Signature

```python
db.DonutChart(data: 'List[Dict[str, str | float]]', value_key: 'str' = 'value', label_key: 'str' = 'label', title: 'Optional[str]' = None, height: 'int' = 300, loading: 'bool' = False, empty_message: 'str' = 'No chart data available', on_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, str | float]]` | `required` | |
| `value_key` | `str` | `'value'` | |
| `label_key` | `str` | `'label'` | |
| `title` | `Optional[str]` | `None` | |
| `height` | `int` | `300` | |
| `loading` | `bool` | `False` | |
| `empty_message` | `str` | `'No chart data available'` | |
| `on_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.DonutChart(data=[{"label": "Healthy", "value": 42}], title="Command center", height="320px")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
