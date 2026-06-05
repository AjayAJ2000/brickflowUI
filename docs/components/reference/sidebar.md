# Sidebar

## What It Does

Creates the left navigation shell for multi-page apps.

## Signature

```python
db.Sidebar(items: 'List[VNode]', logo: 'Optional[str]' = None, brand_name: 'str' = 'BrickflowUI', tagline: 'Optional[str]' = None, collapsed: 'bool' = False, show_theme_toggle: 'bool' = False, sticky: 'bool' = True, **kwargs) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[VNode]` | `required` | |
| `logo` | `Optional[str]` | `None` | |
| `brand_name` | `str` | `'BrickflowUI'` | |
| `tagline` | `Optional[str]` | `None` | |
| `collapsed` | `bool` | `False` | |
| `show_theme_toggle` | `bool` | `False` | |
| `sticky` | `bool` | `True` | |

## Example

```python
import brickflowui as db

node = db.Sidebar([db.NavItem("Dashboard", "/"), db.NavItem("Pipelines", "/pipelines", icon="GitBranch")], brand_name="Acme Analytics", tagline="Built with BrickflowUI")
```

## Integration Notes

- Sidebar collapses behind a mobile menu automatically and can expose the shared `ThemeToggle` in the shell footer.

## Responsive Notes

Sidebar auto-collapses behind a mobile menu on smaller screens, so keep labels concise and rely on icons plus text rather than icons alone.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
