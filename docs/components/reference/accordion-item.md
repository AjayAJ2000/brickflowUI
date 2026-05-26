# AccordionItem

## What It Does

Defines one expandable section inside an accordion.

## Signature

```python
db.AccordionItem(title: 'str', children: 'List[VNode]', subtitle: 'Optional[str]' = None, icon: 'Optional[str]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `title` | `str` | `required` | |
| `children` | `List[VNode]` | `required` | |
| `subtitle` | `Optional[str]` | `None` | |
| `icon` | `Optional[str]` | `None` | |

## Example

```python
import brickflowui as db

node = db.AccordionItem(title="Command center", children=[db.Text("Example content")], icon="LayoutDashboard")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
