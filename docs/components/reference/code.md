# Code

## What It Does

Shows a syntax-friendly code block for docs, debug output, or examples.

## Signature

```python
db.Code(value: 'str', language: 'str' = 'python') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `value` | `str` | `required` | |
| `language` | `str` | `'python'` | |

## Example

```python
import brickflowui as db

node = db.Code("SELECT * FROM prod.pipeline_runs LIMIT 10")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
