# Embed

## What It Does

Hosts external artifacts, dashboards, and review content inside the page.

## Signature

```python
db.Embed(src: 'str', title: 'str' = 'Embedded content', height: 'str' = '420px', allow_fullscreen: 'bool' = True, loading: "Literal['lazy', 'eager']" = 'lazy', sandbox: 'Optional[str]' = None, radius: 'str' = 'var(--radius-lg)', animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `src` | `str` | `required` | |
| `title` | `str` | `'Embedded content'` | |
| `height` | `str` | `'420px'` | |
| `allow_fullscreen` | `bool` | `True` | |
| `loading` | `Literal['lazy', 'eager']` | `'lazy'` | |
| `sandbox` | `Optional[str]` | `None` | |
| `radius` | `str` | `'var(--radius-lg)'` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Embed(src="https://example.com", title="Command center", height="320px", animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Use a descriptive `title` so embedded dashboards and external artifacts remain understandable to assistive technologies.
