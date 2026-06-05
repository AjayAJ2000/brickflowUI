# RadarChart

## What It Does

Compares several dimensions around a shared center.

## Signature

```python
db.RadarChart(data: 'List[Dict[str, Any]]', angle_key: 'str', value_keys: 'List[str]', title: 'Optional[str]' = None, colors: 'Optional[List[str]]' = None, height: 'int' = 320, loading: 'bool' = False, empty_message: 'str' = 'No chart data available') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `angle_key` | `str` | `required` | |
| `value_keys` | `List[str]` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `colors` | `Optional[List[str]]` | `None` | |
| `height` | `int` | `320` | |
| `loading` | `bool` | `False` | |
| `empty_message` | `str` | `'No chart data available'` | |

## Example

```python
import brickflowui as db

node = db.RadarChart(data=[{"metric": "Freshness", "score": 92}], angle_key="metric", value_keys="value_keys", title="Command center")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
