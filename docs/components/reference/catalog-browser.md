# CatalogBrowser

## What It Does

Browses Unity Catalog catalogs, schemas, and tables.

## Signature

```python
db.CatalogBrowser(on_select: 'Optional[Callable[[Dict[str, str]], None]]' = None, selected: 'Optional[Dict[str, str]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `on_select` | `Optional[Callable[[Dict[str, str]], None]]` | `None` | |
| `selected` | `Optional[Dict[str, str]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.CatalogBrowser()
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
