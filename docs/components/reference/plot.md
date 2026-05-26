# Plot

## What It Does

Embeds a native Plotly figure for advanced visualizations.

## Signature

```python
db.Plot(figure: 'Dict[str, Any]') -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `figure` | `Dict[str, Any]` | `required` | |

## Example

```python
import brickflowui as db

node = db.Plot({"data": [{"type": "bar", "x": ["Mon", "Tue"], "y": [24, 18]}]})
```

## Integration Notes

- Plot accepts a Plotly figure or a figure dictionary and is the escape hatch for advanced charting that goes beyond the built-in chart set.
