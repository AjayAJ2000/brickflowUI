# PipelineGraph

## What It Does

Renders a pipeline or DAG-like structure inside the portal.

## Signature

```python
db.PipelineGraph(nodes: 'List[Dict[str, Any]]', edges: 'List[Dict[str, Any]]', title: 'Optional[str]' = None, layout: "Literal['left-to-right', 'top-to-bottom']" = 'left-to-right', animated: 'bool' = True, empty_message: 'str' = 'No pipeline nodes available', on_node_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `nodes` | `List[Dict[str, Any]]` | `required` | |
| `edges` | `List[Dict[str, Any]]` | `required` | |
| `title` | `Optional[str]` | `None` | |
| `layout` | `Literal['left-to-right', 'top-to-bottom']` | `'left-to-right'` | |
| `animated` | `bool` | `True` | |
| `empty_message` | `str` | `'No pipeline nodes available'` | |
| `on_node_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.PipelineGraph(nodes=[{"id": "extract", "label": "Extract", "status": "running"}], edges=[], title="Revenue pipeline")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

PipelineGraph is horizontally scrollable on smaller screens. Keep node labels short and use status layers or tooltips for deeper detail.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
