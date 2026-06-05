# Table

## What It Does

Shows rows of structured data with sorting, pagination, and export.

## Signature

```python
db.Table(data: 'List[Dict[str, Any]]', columns: 'Optional[List[Dict[str, Any]]]' = None, pagination: 'int' = 20, on_row_click: 'Optional[Callable[[Dict[str, Any]], None]]' = None, editable: 'bool' = False, loading: 'bool' = False, empty_message: 'str' = 'No data available', error_message: 'Optional[str]' = None, exportable: 'bool' = False) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `data` | `List[Dict[str, Any]]` | `required` | |
| `columns` | `Optional[List[Dict[str, Any]]]` | `None` | |
| `pagination` | `int` | `20` | |
| `on_row_click` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |
| `editable` | `bool` | `False` | |
| `loading` | `bool` | `False` | |
| `empty_message` | `str` | `'No data available'` | |
| `error_message` | `Optional[str]` | `None` | |
| `exportable` | `bool` | `False` | |

## Example

```python
import brickflowui as db

node = db.Table(data=[{"name": "Bronze Orders", "status": "Healthy"}], columns=[{"key": "name", "label": "Name"}, {"key": "status", "label": "Status", "format": "status"}], pagination=10, exportable=True)
```

## Integration Notes

- Table supports loading, export, sorting, pagination, row clicks, and richer cell formats such as `badge`, `status`, `currency`, `progress`, and `image`.

## Responsive Notes

Tables can overflow horizontally on small screens. Keep the most important columns first and use cell formats like `status`, `badge`, and `progress` to reduce wordiness.

## Accessibility Notes

Pair this component with clear visible copy and predictable state changes so keyboard and assistive-technology users are not surprised.
