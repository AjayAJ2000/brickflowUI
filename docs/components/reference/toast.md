# Toast

## What It Does

Shows dismissible, state-safe notifications in the corner of the app.

## Signature

```python
db.Toast(message: 'str', title: 'Optional[str]' = None, type: 'AlertType' = 'info', visible: 'bool' = True, icon: 'Optional[str]' = None, on_close: 'Optional[EventHandler]' = None, dismissible: 'bool' = True, auto_hide_ms: 'Optional[int]' = None, animated: 'bool' = True, animation: 'Optional[str]' = 'fade-up', animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `message` | `str` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `type` | `AlertType` | `'info'` | |
| `visible` | `bool` | `True` | |
| `icon` | `Optional[str]` | `None` | |
| `on_close` | `Optional[EventHandler]` | `None` | |
| `dismissible` | `bool` | `True` | |
| `auto_hide_ms` | `Optional[int]` | `None` | |
| `animated` | `bool` | `True` | |
| `animation` | `Optional[str]` | `'fade-up'` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Toast(message="Everything is healthy.", title="Command center", icon="LayoutDashboard", animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
