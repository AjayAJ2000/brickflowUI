# Stepper

## What It Does

Shows progress through onboarding, review, or release stages.

## Signature

```python
db.Stepper(steps: 'List[Dict[str, Any]]', active: 'int' = 0, orientation: "Literal['horizontal', 'vertical']" = 'horizontal', animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `steps` | `List[Dict[str, Any]]` | `required` | |
| `active` | `int` | `0` | |
| `orientation` | `Literal['horizontal', 'vertical']` | `'horizontal'` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Stepper(steps=[{"label": "Bronze"}, {"label": "Silver"}], animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
