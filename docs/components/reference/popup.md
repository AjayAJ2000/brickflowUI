# Popup

## What It Does

Shows a lightweight confirmation or quick-look overlay.

## Signature

```python
db.Popup(visible: 'bool', title: 'str', children: 'List[VNode]', on_close: 'Optional[EventHandler]' = None, size: "Literal['sm', 'md', 'lg']" = 'sm', backdrop: 'bool' = True, placement: "Literal['center']" = 'center', animated: 'bool' = True, animation: 'Optional[str]' = 'fade-up', animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `visible` | `bool` | `required` | |
| `title` | `str` | `required` | |
| `children` | `List[VNode]` | `required` | |
| `on_close` | `Optional[EventHandler]` | `None` | |
| `size` | `Literal['sm', 'md', 'lg']` | `'sm'` | |
| `backdrop` | `bool` | `True` | |
| `placement` | `Literal['center']` | `'center'` | |
| `animated` | `bool` | `True` | |
| `animation` | `Optional[str]` | `'fade-up'` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Popup(visible=True, title="Command center", children=[db.Text("Example content")], animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
