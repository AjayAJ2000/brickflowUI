# Heatmap

## What It Does

Maps intensity across two dimensions such as week vs signal.

## Signature

```python
db.Heatmap(data: 'List[Dict[str, Any]]', x_key: 'str', y_key: 'str', value_key: 'str', title: 'Optional[str]' = None, color: 'Optional[str]' = None, empty_message: 'str' = 'No heatmap data available', on_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `x_key` | `str` | `required` | |
| `y_key` | `str` | `required` | |
| `value_key` | `str` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `color` | `Optional[str]` | `None` | |
| `empty_message` | `str` | `'No heatmap data available'` | |
| `on_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Heatmap(data=[{"hour": "09", "layer": "Bronze", "value": 2}], x_key="week", y_key="cost", value_key="value", title="Command center")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
