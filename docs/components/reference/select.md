# Select

## What It Does

Lets the user choose one option from a list.

## Signature

```python
db.Select(name: 'str', options: 'List[Dict[str, str]]', label: 'Optional[str]' = None, value: 'Optional[str]' = None, placeholder: 'str' = 'Select an option', on_change: 'Optional[Callable[[str], None]]' = None, disabled: 'bool' = False, loading: 'bool' = False) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | `str` | `required` | |
| `options` | `List[Dict[str, str]]` | `required` | |
| `label` | `Optional[str]` | `None` | |
| `value` | `Optional[str]` | `None` | |
| `placeholder` | `str` | `'Select an option'` | |
| `on_change` | `Optional[Callable[[str], None]]` | `None` | |
| `disabled` | `bool` | `False` | |
| `loading` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.Select(name="site", label="Site", options=[{"label": "Toyama", "value": "toyama"}], value="toyama", on_change=lambda value: None)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
