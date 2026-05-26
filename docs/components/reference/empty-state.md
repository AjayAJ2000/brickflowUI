# EmptyState

## What It Does

Explains why a view has no content and what to do next.

## Signature

```python
db.EmptyState(title: 'str', message: 'str', icon: 'Optional[str]' = None, actions: 'Optional[List[VNode]]' = None, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `title` | `str` | `required` | |
| `message` | `str` | `required` | |
| `icon` | `Optional[str]` | `None` | |
| `actions` | `Optional[List[VNode]]` | `None` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.EmptyState(title="Command center", message="Everything is healthy.", icon="LayoutDashboard", animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
