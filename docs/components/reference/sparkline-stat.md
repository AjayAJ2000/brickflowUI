# SparklineStat

## What It Does

Combines a compact KPI value with a tiny embedded trend line.

## Signature

```python
db.SparklineStat(label: 'str', value: 'str', data: 'List[Dict[str, Any]]', x_key: 'str', y_key: 'str', delta: 'Optional[str]' = None, delta_type: "Literal['increase', 'decrease', 'neutral']" = 'neutral', color: 'Optional[str]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `str` | `required` | |
| `value` | `str` | `required` | |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `x_key` | `str` | `required` | |
| `y_key` | `str` | `required` | |
| `delta` | `Optional[str]` | `None` | |
| `delta_type` | `Literal['increase', 'decrease', 'neutral']` | `'neutral'` | |
| `color` | `Optional[str]` | `None` | |

## Example

```python
import brickflowui as db

node = db.SparklineStat(label="Pipeline health", value="active", data=[{"day": "Mon", "value": 14}, {"day": "Tue", "value": 12}], x_key="week", y_key="cost")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
