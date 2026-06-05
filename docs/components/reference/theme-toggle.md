# ThemeToggle

## What It Does

Switches between dark and light modes directly in the UI.

## Signature

```python
db.ThemeToggle(label: 'str' = 'Theme', light_label: 'str' = 'Light', dark_label: 'str' = 'Dark') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `str` | `'Theme'` | |
| `light_label` | `str` | `'Light'` | |
| `dark_label` | `str` | `'Dark'` | |

## Example

```python
import brickflowui as db

node = db.ThemeToggle(label="Theme", light_label="Light", dark_label="Dark")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
