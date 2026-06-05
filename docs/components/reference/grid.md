# Grid

## What It Does

Builds a responsive multi-column layout for cards, charts, or forms.

## Signature

```python
db.Grid(children: 'List[VNode]', cols: 'int' = 2, gap: 'int' = 4) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `children` | `List[VNode]` | `required` | |
| `cols` | `int` | `2` | |
| `gap` | `int` | `4` | |

## Example

```python
import brickflowui as db

node = db.Grid([db.Card([db.Text("Runs")]), db.Card([db.Text("Failures")])], cols=2, gap=4)
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Prefer fewer columns on dense portal screens. The framework will wrap, but your card content should still read cleanly in a single-column stack.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
