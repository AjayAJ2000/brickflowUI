# Image

## What It Does

Renders local or remote images, logos, screenshots, and GIFs from Python.

## Signature

```python
db.Image(src: 'str', alt: 'str' = '', width: 'str' = '100%', height: 'str' = 'auto', fit: "Literal['cover', 'contain', 'fill', 'none', 'scale-down']" = 'cover', caption: 'Optional[str]' = None, radius: 'str' = 'var(--radius-lg)', loading: "Literal['lazy', 'eager']" = 'lazy', variant: "Literal['content', 'inline', 'avatar']" = 'content', inline: 'bool' = False, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `src` | `str` | `required` | |
| `alt` | `str` | `''` | |
| `width` | `str` | `'100%'` | |
| `height` | `str` | `'auto'` | |
| `fit` | `Literal['cover', 'contain', 'fill', 'none', 'scale-down']` | `'cover'` | |
| `caption` | `Optional[str]` | `None` | |
| `radius` | `str` | `'var(--radius-lg)'` | |
| `loading` | `Literal['lazy', 'eager']` | `'lazy'` | |
| `variant` | `Literal['content', 'inline', 'avatar']` | `'content'` | |
| `inline` | `bool` | `False` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Image("assets/logo.svg", alt="Acme logo", variant="inline")
```

## Integration Notes

- Use `variant="inline"` for logos and product marks, `variant="avatar"` for circular profile images, and `variant="content"` for screenshots or larger visuals.
