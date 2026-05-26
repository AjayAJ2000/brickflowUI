# Button

## What It Does

Triggers actions, navigation, or secondary workflows.

## Signature

```python
db.Button(label: 'str', on_click: 'Optional[EventHandler]' = None, variant: 'ButtonVariant' = 'primary', icon: 'Optional[str]' = None, disabled: 'bool' = False, loading: 'bool' = False, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None, html_type: "Literal['button', 'submit', 'reset']" = 'button', **kwargs) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `label` | `str` | `required` | |
| `on_click` | `Optional[EventHandler]` | `None` | |
| `variant` | `ButtonVariant` | `'primary'` | |
| `icon` | `Optional[str]` | `None` | |
| `disabled` | `bool` | `False` | |
| `loading` | `bool` | `False` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |
| `html_type` | `Literal['button', 'submit', 'reset']` | `'button'` | |

## Example

```python
import brickflowui as db

node = db.Button("Run refresh", on_click=lambda: None, icon="Sparkles")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
