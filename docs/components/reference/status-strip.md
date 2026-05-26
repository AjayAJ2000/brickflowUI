# StatusStrip

## What It Does

Displays a row or grid of operational health and freshness signals.

## Signature

```python
db.StatusStrip(items: 'List[Dict[str, Any]]', title: 'Optional[str]' = None, columns: 'int' = 4, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[Dict[str, Any]]` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `columns` | `int` | `4` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.StatusStrip(items=[{"label": "Overview", "path": "/"}], title="Command center", animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
