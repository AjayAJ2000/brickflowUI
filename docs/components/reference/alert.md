# Alert

## What It Does

Shows inline information, warnings, successes, or errors.

## Signature

```python
db.Alert(message: 'str', type: 'AlertType' = 'info', title: 'Optional[str]' = None, dismissible: 'bool' = False) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `message` | `str` | `required` | |
| `type` | `AlertType` | `'info'` | |
| `title` | `Optional[str]` | `None` | |
| `dismissible` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.Alert(message="Everything is healthy.", title="Command center")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
