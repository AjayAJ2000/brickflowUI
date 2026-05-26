# Timeline

## What It Does

Narrates chronological events such as incidents, approvals, or jobs.

## Signature

```python
db.Timeline(items: 'List[Dict[str, Any]]', title: 'Optional[str]' = None, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[Dict[str, Any]]` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Timeline(items=[{"label": "Overview", "path": "/"}], title="Command center", animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
