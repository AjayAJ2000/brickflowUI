# Input

## What It Does

Captures controlled text, search, numeric, date, URL, or textarea input.

## Signature

```python
db.Input(name: 'str', label: 'Optional[str]' = None, type: 'InputType' = 'text', placeholder: 'str' = '', value: 'str' = '', on_change: 'Optional[Callable[[str], None]]' = None, disabled: 'bool' = False, required: 'bool' = False, error: 'Optional[str]' = None, loading: 'bool' = False, debounce_ms: 'int' = 180, change_strategy: "Literal['debounce', 'immediate', 'blur']" = 'debounce', sync_on_blur: 'bool' = True) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | `str` | `required` | |
| `label` | `Optional[str]` | `None` | |
| `type` | `InputType` | `'text'` | |
| `placeholder` | `str` | `''` | |
| `value` | `str` | `''` | |
| `on_change` | `Optional[Callable[[str], None]]` | `None` | |
| `disabled` | `bool` | `False` | |
| `required` | `bool` | `False` | |
| `error` | `Optional[str]` | `None` | |
| `loading` | `bool` | `False` | |
| `debounce_ms` | `int` | `180` | |
| `change_strategy` | `Literal['debounce', 'immediate', 'blur']` | `'debounce'` | |
| `sync_on_blur` | `bool` | `True` | |

## Example

```python
import brickflowui as db

node = db.Input(name="search", label="Search", placeholder="Search pipelines...", value="", on_change=lambda value: None, debounce_ms=220)
```

## Integration Notes

- Text-like inputs default to `change_strategy="debounce"`, which keeps typing local and fast while syncing state back to Python after `debounce_ms`.
- Use `change_strategy="immediate"` only when every character must trigger backend logic.
- Use `change_strategy="blur"` when the input kicks off a heavier query and should only sync once the field loses focus.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Always provide `label` for production forms unless the field is purely decorative or already described by adjacent UI copy.
