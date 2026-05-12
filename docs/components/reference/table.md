# Table

## What It Does

`Table` renders structured rows with sorting, pagination, row click handling, CSV export, loading states, and richer cell presentation patterns.

## When To Use It

Use `Table` for dashboards, review queues, release lists, customer scorecards, and any screen where dense operational data matters.

## Inputs To Know

- `data`: list of row dictionaries
- `columns`: explicit column definitions
- `pagination`: page size
- `on_row_click`: callback when a row is selected
- `loading`: show a loading state while data is in flight
- `empty_message`: custom empty-state copy
- `exportable`: turn on built-in CSV export

## Useful Column Patterns

`Table` columns can now describe richer cell formats:

```python
columns = [
    {"key": "account", "label": "Account", "format": "metric"},
    {"key": "plan", "label": "Plan", "format": "badge", "toneKey": "planTone"},
    {"key": "mrr", "label": "MRR", "format": "currency", "currency": "USD"},
    {"key": "health", "label": "Health", "format": "progress", "toneKey": "statusTone"},
    {"key": "status", "label": "Status", "format": "status", "toneKey": "statusTone"},
]
```

Supported practical formats:

- `text`
- `metric`
- `badge`
- `status`
- `progress`
- `currency`
- `image`
- `avatar`

## Example

```python
import brickflowui as db

rows = [
    {
        "account": "Acme Corp",
        "plan": "Enterprise",
        "planTone": "info",
        "mrr": 12400,
        "health": 88,
        "status": "Active",
        "statusTone": "success",
    }
]

table = db.Table(
    data=rows,
    columns=[
        {"key": "account", "label": "Account", "format": "metric"},
        {"key": "plan", "label": "Plan", "format": "badge", "toneKey": "planTone"},
        {"key": "mrr", "label": "MRR", "format": "currency", "currency": "USD"},
        {"key": "health", "label": "Health", "format": "progress", "toneKey": "statusTone"},
        {"key": "status", "label": "Status", "format": "status", "toneKey": "statusTone"},
    ],
    exportable=True,
)
```

## Works Well With

`Card`, `SectionHeader`, `Drawer`, `DateRangePicker`, `MultiSelect`, `PipelineGraph`

## Notes

- Use `loading=True` when you are waiting on backend data, or let the runtime-driven loading flow handle it from interaction events.
- Use column formatting when you need a screenshot-grade table rather than plain strings.
