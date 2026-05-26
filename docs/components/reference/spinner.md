# Spinner

## What It Does

Communicates local loading work for buttons, cards, and forms.

## Signature

```python
db.Spinner(size: "Literal['sm', 'md', 'lg']" = 'md') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `size` | `Literal['sm', 'md', 'lg']` | `'md'` | |

## Example

```python
import brickflowui as db

node = db.Spinner()
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
