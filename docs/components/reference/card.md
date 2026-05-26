# Card

## What It Does

Creates a surface container for sections, KPIs, or grouped controls.

## Signature

```python
db.Card(children: 'List[VNode]', title: 'Optional[str]' = None, subtitle: 'Optional[str]' = None, bordered: 'bool' = True, padding: 'int' = 4, hover: 'bool' = False, elevated: 'bool' = False, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None, **kwargs) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `children` | `List[VNode]` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `subtitle` | `Optional[str]` | `None` | |
| `bordered` | `bool` | `True` | |
| `padding` | `int` | `4` | |
| `hover` | `bool` | `False` | |
| `elevated` | `bool` | `False` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Card([db.Text("Warehouse health", variant="h3"), db.Text("Last refresh: 4 minutes ago", muted=True)], bordered=True, elevated=True)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
