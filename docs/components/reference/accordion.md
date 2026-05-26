# Accordion

## What It Does

Groups expandable sections for FAQs, help, or dense detail.

## Signature

```python
db.Accordion(items: 'List[VNode]', default_open: 'Optional[List[int]]' = None, allow_multiple: 'bool' = False) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[VNode]` | `required` | |
| `default_open` | `Optional[List[int]]` | `None` | |
| `allow_multiple` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.Accordion(items=[{"label": "Overview", "path": "/"}])
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
