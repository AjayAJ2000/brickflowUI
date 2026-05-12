# Sidebar

## What It Does

`Sidebar` creates the left navigation shell for multi-page apps and now includes mobile collapse behavior by default.

## Inputs To Know

- `items`: a list of `db.NavItem(...)`
- `brand_name`
- `tagline`
- `logo`
- `show_theme_toggle`

## Example

```python
import brickflowui as db

sidebar = db.Sidebar(
    items=[
        db.NavItem("Dashboard", "/"),
        db.NavItem("Pipelines", "/pipelines"),
        db.NavItem("Settings", "/settings"),
    ],
    brand_name="Acme Analytics",
    tagline="Built with BrickflowUI",
    logo="assets/logo.svg",
    show_theme_toggle=True,
)
```

## Responsive Behavior

On smaller screens, `Sidebar` automatically:

- hides behind a menu button
- opens as an overlay panel
- closes after a navigation click
- keeps the theme toggle accessible in the footer

## Works Well With

`NavItem`, `ThemeToggle`, `Image`, multi-page `App(...)` shells

## Notes

- If you register multiple pages with `@app.page(...)`, BrickflowUI uses `Sidebar` automatically for the built-in shell.
- For a top navigation pattern instead, use `TopNav`.
