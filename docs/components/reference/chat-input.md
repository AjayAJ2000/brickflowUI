# ChatInput

## What It Does

Collects assistant-style prompts with change and submit events.

## Signature

```python
db.ChatInput(name: 'str' = 'message', value: 'str' = '', placeholder: 'str' = 'Ask a question', on_change: 'Optional[Callable[[str], None]]' = None, on_submit: 'Optional[Callable[[str], None]]' = None, disabled: 'bool' = False, loading: 'bool' = False, submit_label: 'str' = 'Send', debounce_ms: 'int' = 180, change_strategy: "Literal['debounce', 'immediate', 'blur']" = 'debounce', animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | `str` | `'message'` | |
| `value` | `str` | `''` | |
| `placeholder` | `str` | `'Ask a question'` | |
| `on_change` | `Optional[Callable[[str], None]]` | `None` | |
| `on_submit` | `Optional[Callable[[str], None]]` | `None` | |
| `disabled` | `bool` | `False` | |
| `loading` | `bool` | `False` | |
| `submit_label` | `str` | `'Send'` | |
| `debounce_ms` | `int` | `180` | |
| `change_strategy` | `Literal['debounce', 'immediate', 'blur']` | `'debounce'` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.ChatInput(value="", placeholder="Ask about delayed jobs", on_change=lambda value: None, on_submit=lambda value: None, debounce_ms=200)
```

## Integration Notes

- Chat input uses the same debounced local-first sync model as `Input`, so composing prompts stays smooth.
- Call `on_submit` for the actual send action and reserve `on_change` for draft-aware UX, prompt suggestions, or validation.
