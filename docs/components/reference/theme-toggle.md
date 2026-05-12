# ThemeToggle

## What It Does

`ThemeToggle` lets the user switch between dark mode and light mode at runtime.

## When To Use It

Use `ThemeToggle` when your product defines both `dark` and `light` theme tokens and you want the viewer to control the active mode.

## Inputs To Know

- `label`: visible control label
- `light_label`: copy shown when light mode is active
- `dark_label`: copy shown when dark mode is active

## Works Well With

`TopNav`, `Sidebar`, `Hero`, branded dashboards, local development previews

## Example

```python
import brickflowui as db

toggle = db.ThemeToggle(
    label="Color mode",
    light_label="Light",
    dark_label="Dark",
)
```

## Notes

- Theme selection is persisted in browser storage automatically.
- `Sidebar` and `TopNav` can render the toggle for you with `show_theme_toggle=True`.
