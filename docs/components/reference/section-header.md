# SectionHeader

## What It Does

Adds a reusable title block with subtitle and actions.

## Signature

```python
db.SectionHeader(title: 'str', subtitle: 'Optional[str]' = None, actions: 'Optional[List[VNode]]' = None, eyebrow: 'Optional[str]' = None, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `title` | `str` | `required` | |
| `subtitle` | `Optional[str]` | `None` | |
| `actions` | `Optional[List[VNode]]` | `None` | |
| `eyebrow` | `Optional[str]` | `None` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.SectionHeader(title="Command center", animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
