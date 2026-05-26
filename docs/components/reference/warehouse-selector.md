# WarehouseSelector

## What It Does

Selects a Databricks SQL warehouse from the current environment.

## Signature

```python
db.WarehouseSelector(on_select: 'Optional[Callable[[str], None]]' = None, selected_id: 'Optional[str]' = None, label: 'str' = 'SQL Warehouse') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `on_select` | `Optional[Callable[[str], None]]` | `None` | |
| `selected_id` | `Optional[str]` | `None` | |
| `label` | `str` | `'SQL Warehouse'` | |

## Example

```python
import brickflowui as db

node = db.WarehouseSelector(label="Pipeline health")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
