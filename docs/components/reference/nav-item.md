# NavItem

## What It Does

Defines one route entry inside a sidebar navigation list.

## Signature

```python
db.NavItem(label: 'str', path: 'str', icon: 'Optional[str]' = None, badge: 'Optional[str]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `str` | `required` | |
| `path` | `str` | `required` | |
| `icon` | `Optional[str]` | `None` | |
| `badge` | `Optional[str]` | `None` | |

## Example

```python
import brickflowui as db

node = db.NavItem(label="Pipeline health", path="/analytics", icon="LayoutDashboard")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
