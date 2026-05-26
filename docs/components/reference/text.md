# Text

## What It Does

Renders headings, body copy, captions, labels, and lightweight code text.

## Signature

```python
db.Text(value: 'str', variant: 'TextVariant' = 'body', color: 'Optional[str]' = None, bold: 'bool' = False, italic: 'bool' = False, muted: 'bool' = False) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `value` | `str` | `required` | |
| `variant` | `TextVariant` | `'body'` | |
| `color` | `Optional[str]` | `None` | |
| `bold` | `bool` | `False` | |
| `italic` | `bool` | `False` | |
| `muted` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.Text("Warehouse latency is stable.", variant="body", muted=False)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
