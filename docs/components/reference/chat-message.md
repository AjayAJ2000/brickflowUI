# ChatMessage

## What It Does

Renders one message inside an assistant or copilot transcript.

## Signature

```python
db.ChatMessage(role: "Literal['user', 'assistant', 'system', 'tool']", content: 'str', name: 'Optional[str]' = None, timestamp: 'Optional[str]' = None, avatar: 'Optional[str]' = None, tone: "Literal['default', 'success', 'warning', 'error', 'info']" = 'default', animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `role` | `Literal['user', 'assistant', 'system', 'tool']` | `required` | |
| `content` | `str` | `required` | |
| `name` | `Optional[str]` | `None` | |
| `timestamp` | `Optional[str]` | `None` | |
| `avatar` | `Optional[str]` | `None` | |
| `tone` | `Literal['default', 'success', 'warning', 'error', 'info']` | `'default'` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.ChatMessage(role="assistant", content="Two jobs are outside SLA.", name="Ops Copilot")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
