# Breadcrumbs

## What It Does

Shows where the user is inside a multi-step or nested flow.

## Signature

```python
db.Breadcrumbs(items: 'List[Dict[str, Any]]') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[Dict[str, Any]]` | `required` | |

## Example

```python
import brickflowui as db

node = db.Breadcrumbs(items=[{"label": "Overview", "path": "/"}])
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
