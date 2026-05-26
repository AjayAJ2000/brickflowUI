# Sidebar

## What It Does

Creates the left navigation shell for multi-page apps.

## Signature

```python
db.Sidebar(items: 'List[VNode]', logo: 'Optional[str]' = None, brand_name: 'str' = 'BrickflowUI', tagline: 'Optional[str]' = None, collapsed: 'bool' = False, **kwargs) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[VNode]` | `required` | |
| `logo` | `Optional[str]` | `None` | |
| `brand_name` | `str` | `'BrickflowUI'` | |
| `tagline` | `Optional[str]` | `None` | |
| `collapsed` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.Sidebar([db.NavItem("Dashboard", "/"), db.NavItem("Pipelines", "/pipelines", icon="GitBranch")], brand_name="Acme Analytics", tagline="Built with BrickflowUI")
```

## Integration Notes

- Sidebar collapses behind a mobile menu automatically and can expose the shared `ThemeToggle` in the shell footer.
