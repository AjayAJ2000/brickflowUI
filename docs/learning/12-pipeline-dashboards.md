# 12. Pipeline Dashboards

## Learning Goal

Build a pipeline command center with graph structure, health signals, filters, charts, and drilldowns.

## Pipeline Dashboard Anatomy

A useful pipeline dashboard usually has:

- health summary
- freshness or SLA score
- pipeline graph
- failure or latency trend
- table of runs
- owner/team context
- drilldown for selected node or row
- triage queue

## Pipeline Graph

```python
nodes = [
    {"id": "source", "label": "Source API", "layer": "source", "status": "healthy"},
    {"id": "bronze", "label": "Bronze Events", "layer": "bronze", "status": "running"},
    {"id": "silver", "label": "Silver Quality", "layer": "silver", "status": "watch"},
    {"id": "gold", "label": "Gold Marts", "layer": "gold", "status": "healthy"},
]

edges = [
    {"from": "source", "to": "bronze"},
    {"from": "bronze", "to": "silver"},
    {"from": "silver", "to": "gold"},
]

selected, set_selected = db.use_state("No node selected")

db.PipelineGraph(
    nodes=nodes,
    edges=edges,
    title="Lakehouse Flow",
    on_node_click=lambda node: set_selected(f"{node['label']} selected"),
)
```

## Status Strip

```python
db.StatusStrip(
    [
        {"label": "Pipelines", "value": "12", "status": "info"},
        {"label": "Success", "value": "99.1%", "status": "healthy"},
        {"label": "Freshness", "value": "18m", "status": "healthy"},
        {"label": "Incidents", "value": "2", "status": "watch"},
    ]
)
```

## Triage Board

```python
db.KanbanBoard(
    [
        {"id": "healthy", "label": "Healthy", "cards": []},
        {"id": "watch", "label": "Watch", "cards": [{"id": "orders", "title": "Orders Lakehouse"}]},
        {"id": "risk", "label": "At Risk", "cards": [{"id": "ml", "title": "ML Features"}]},
    ],
    on_card_click=lambda card: set_selected(card["title"]),
)
```

## Recommended Data Shape

Start with rows like:

```python
{
    "pipeline": "Orders Lakehouse",
    "layer": "silver",
    "status": "watch",
    "freshness": 44,
    "success": 97.8,
    "rows_m": 84,
    "cost": 127,
    "duration": 36,
}
```

This shape is simple enough for mock data and easy to replace with Databricks SQL results.

## Common Mistakes

- Showing a graph with no table for operational details.
- Showing a table with no summary of what matters.
- Forgetting owners and runbook context.
- Mixing pipeline topology with run history without labels.

## Exercise

Build a command center with:

- `StatusStrip`
- `PipelineGraph`
- `GaugeChart`
- `ComposedChart`
- `Table`
- `KanbanBoard`

All should use the same mock pipeline data.

## Checkpoint

You should be able to represent data pipelines as both operational metrics and flow structure.
