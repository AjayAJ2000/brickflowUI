# Video

## What It Does

Renders local or remote videos directly from your BrickflowUI script.

## Signature

```python
db.Video(src: 'str', poster: 'Optional[str]' = None, width: 'str' = '100%', height: 'str' = 'auto', caption: 'Optional[str]' = None, radius: 'str' = 'var(--radius-lg)', controls: 'bool' = True, autoplay: 'bool' = False, loop: 'bool' = False, muted: 'bool' = False, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `src` | `str` | `required` | |
| `poster` | `Optional[str]` | `None` | |
| `width` | `str` | `'100%'` | |
| `height` | `str` | `'auto'` | |
| `caption` | `Optional[str]` | `None` | |
| `radius` | `str` | `'var(--radius-lg)'` | |
| `controls` | `bool` | `True` | |
| `autoplay` | `bool` | `False` | |
| `loop` | `bool` | `False` | |
| `muted` | `bool` | `False` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Video("assets/demo.mp4", poster="assets/poster.png", caption="Product walkthrough")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Use caption or surrounding copy to explain what the user is seeing, especially when the video demonstrates workflow or onboarding steps.
