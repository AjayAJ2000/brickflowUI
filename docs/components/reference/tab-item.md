# TabItem

## What It Does

Defines one tab label and its corresponding content tree.

## Signature

```python
db.TabItem(label: 'str', children: 'List[VNode]', icon: 'Optional[str]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `str` | `required` | |
| `children` | `List[VNode]` | `required` | |
| `icon` | `Optional[str]` | `None` | |

## Example

```python
import brickflowui as db

node = db.TabItem(label="Pipeline health", children=[db.Text("Example content")], icon="LayoutDashboard")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
