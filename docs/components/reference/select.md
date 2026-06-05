# Select

## What It Does

Lets the user choose one option from a list.

## Signature

```python
db.Select(name: 'str', options: 'List[Dict[str, str]]', label: 'Optional[str]' = None, value: 'Optional[str]' = None, placeholder: 'str' = 'Select an option', on_change: 'Optional[Callable[[str], None]]' = None, disabled: 'bool' = False, loading: 'bool' = False, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
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
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Select(name="site", label="Site", options=[{"label": "Toyama", "value": "toyama"}], value="toyama", on_change=lambda value: None)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair `label` with concise option labels so screen-reader and keyboard navigation stay predictable.
