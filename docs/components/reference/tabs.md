# Tabs

## What It Does

Switches between multiple content sections without leaving the page.

## Signature

```python
db.Tabs(items: 'List[VNode]', default_active: 'int' = 0, on_change: 'Optional[Callable[[int], None]]' = None, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[VNode]` | `required` | |
| `default_active` | `int` | `0` | |
| `on_change` | `Optional[Callable[[int], None]]` | `None` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Tabs(items=[db.TabItem("Overview", [db.Text("Overview panel")])], animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
