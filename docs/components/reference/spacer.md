# Spacer

## What It Does

Adds explicit breathing room between nearby components.

## Signature

```python
db.Spacer(size: 'int' = 4) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `size` | `int` | `4` | |

## Example

```python
import brickflowui as db

node = db.Spacer()
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
