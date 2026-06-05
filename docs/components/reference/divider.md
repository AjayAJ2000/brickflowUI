# Divider

## What It Does

Separates related content blocks visually.

## Signature

```python
db.Divider(label: 'Optional[str]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `Optional[str]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Divider(label="Pipeline health")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
