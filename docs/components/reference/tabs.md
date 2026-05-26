# Tabs

## What It Does

Switches between multiple content sections without leaving the page.

## Signature

```python
db.Tabs(items: 'List[VNode]', default_active: 'int' = 0, on_change: 'Optional[Callable[[int], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `items` | `List[VNode]` | `required` | |
| `default_active` | `int` | `0` | |
| `on_change` | `Optional[Callable[[int], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Tabs(items=[db.TabItem("Overview", [db.Text("Overview panel")])])
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
