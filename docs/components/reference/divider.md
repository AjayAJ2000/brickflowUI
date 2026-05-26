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
