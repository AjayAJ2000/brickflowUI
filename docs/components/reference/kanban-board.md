# KanbanBoard

## What It Does

Visualizes work queues grouped by workflow stage.

## Signature

```python
db.KanbanBoard(columns: 'List[Dict[str, Any]]', on_card_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None, animated: 'bool' = False, animation: 'Optional[str]' = None, animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `columns` | `List[Dict[str, Any]]` | `required` | |
| `on_card_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |
| `animated` | `bool` | `False` | |
| `animation` | `Optional[str]` | `None` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.KanbanBoard(columns=[{"id": "todo", "label": "Todo", "cards": [{"id": "a", "title": "Investigate SLA drift"}]}], animated="animated")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.

## Responsive Notes

Check the component inside a realistic layout, not only in isolation, so spacing, overflow, and action density stay comfortable on smaller screens.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
