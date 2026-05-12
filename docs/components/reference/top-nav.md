# TopNav

## What It Does

`TopNav` creates a responsive top navigation bar that collapses into a menu button on smaller screens automatically.

## When To Use It

Use `TopNav` when your app should feel like a modern SaaS shell instead of a stacked row of buttons. It works especially well for executive dashboards, portals, landing pages, and authenticated workspaces.

## Inputs To Know

- `items`: a list of `db.NavItem(...)` entries
- `brand_name`: product or workspace name
- `tagline`: optional secondary line under the brand
- `logo`: optional local or remote logo asset
- `actions`: optional buttons, selects, or other controls on the right side
- `sticky`: keep the nav attached to the top while the page scrolls
- `show_theme_toggle`: render the built-in dark/light mode switch

## Works Well With

`Hero`, `SectionHeader`, `Badge`, `Button`, `Select`, `ThemeToggle`

## Example

```python
import brickflowui as db

nav = db.TopNav(
    items=[
        db.NavItem("Overview", "/"),
        db.NavItem("Pipelines", "/pipelines"),
        db.NavItem("Users", "/users", badge="2.4k"),
    ],
    brand_name="Acme Analytics",
    tagline="Built with BrickflowUI",
    show_theme_toggle=True,
    actions=[
        db.Button("Export", variant="secondary"),
        db.Button("New report"),
    ],
)
```

## Notes

- `TopNav` is the easiest way to avoid mobile horizontal scrolling for nav bars.
- On mobile, the link list and right-side actions are moved into the menu panel automatically.
