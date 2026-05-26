# Form

## What It Does

Posts named child controls to a backend route as structured JSON.

## Signature

```python
db.Form(children: 'List[VNode]', action: 'str', method: 'str' = 'POST', success_redirect: 'Optional[str]' = None, reload_on_success: 'bool' = False) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `children` | `List[VNode]` | `required` | |
| `action` | `str` | `required` | |
| `method` | `str` | `'POST'` | |
| `success_redirect` | `Optional[str]` | `None` | |
| `reload_on_success` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.Form(children=[db.Text("Example content")], action="action")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
