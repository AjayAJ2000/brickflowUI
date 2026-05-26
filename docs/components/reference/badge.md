# Badge

## What It Does

Highlights compact status labels such as environment, freshness, or risk.

## Signature

```python
db.Badge(label: 'str', color: 'BadgeColor' = 'blue') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `str` | `required` | |
| `color` | `BadgeColor` | `'blue'` | |

## Example

```python
import brickflowui as db

node = db.Badge(label="Pipeline health")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
