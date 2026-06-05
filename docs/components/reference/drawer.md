# Drawer

## What It Does

Slides contextual detail in from the side without leaving the page.

## Signature

```python
db.Drawer(visible: 'bool', title: 'str', children: 'List[VNode]', on_close: 'Optional[EventHandler]' = None, side: "Literal['left', 'right']" = 'right', width: 'str' = '420px', animated: 'bool' = True, animation: 'Optional[str]' = 'fade-up', animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `visible` | `bool` | `required` | |
| `title` | `str` | `required` | |
| `children` | `List[VNode]` | `required` | |
| `on_close` | `Optional[EventHandler]` | `None` | |
| `side` | `Literal['left', 'right']` | `'right'` | |
| `width` | `str` | `'420px'` | |
| `animated` | `bool` | `True` | |
| `animation` | `Optional[str]` | `'fade-up'` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Drawer(visible=True, title="Command center", children=[db.Text("Example content")], animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
