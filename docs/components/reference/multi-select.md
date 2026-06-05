# MultiSelect

## What It Does

Lets users activate multiple tags, scopes, or filters.

## Signature

```python
db.MultiSelect(name: 'str', options: 'List[Dict[str, str]]', label: 'Optional[str]' = None, values: 'Optional[List[str]]' = None, on_change: 'Optional[Callable[[List[str]], None]]' = None, disabled: 'bool' = False, loading: 'bool' = False, placeholder: 'Optional[str]' = None, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `name` | `str` | `required` | |
| `options` | `List[Dict[str, str]]` | `required` | |
| `label` | `Optional[str]` | `None` | |
| `values` | `Optional[List[str]]` | `None` | |
| `on_change` | `Optional[Callable[[List[str]], None]]` | `None` | |
| `disabled` | `bool` | `False` | |
| `loading` | `bool` | `False` | |
| `placeholder` | `Optional[str]` | `None` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.MultiSelect(name="layers", label="Layers", options=[{"label": "Bronze", "value": "bronze"}, {"label": "Silver", "value": "silver"}], values=["bronze"], on_change=lambda values: None)
```

## Integration Notes

- MultiSelect emits `list[str]` back to Python, which makes it a strong fit for scoped filters and dashboard drilldowns.
- Use it together with `Table`, `Heatmap`, `PipelineGraph`, or query builders to control slices of a larger workspace.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
