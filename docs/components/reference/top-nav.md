# TopNav

## What It Does

Creates a responsive top navigation bar with automatic mobile collapse.

## Signature

```python
db.TopNav(items: 'List[VNode]', logo: 'Optional[str]' = None, brand_name: 'str' = 'BrickflowUI', tagline: 'Optional[str]' = None, actions: 'Optional[List[VNode]]' = None, sticky: 'bool' = True, show_theme_toggle: 'bool' = False, **kwargs) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[VNode]` | `required` | |
| `logo` | `Optional[str]` | `None` | |
| `brand_name` | `str` | `'BrickflowUI'` | |
| `tagline` | `Optional[str]` | `None` | |
| `actions` | `Optional[List[VNode]]` | `None` | |
| `sticky` | `bool` | `True` | |
| `show_theme_toggle` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.TopNav([db.NavItem("Dashboard", "/"), db.NavItem("Analytics", "/analytics")], brand_name="Acme Analytics", actions=[db.Button("Export", variant="secondary")], show_theme_toggle=True)
```

## Integration Notes

- TopNav collapses its route list into a menu button on smaller screens and can host secondary action buttons on the right.

## Responsive Notes

TopNav collapses route links into a mobile panel. Keep high-priority actions in the `actions` slot so they remain reachable on dense screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
