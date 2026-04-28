# Charts And Visualizations

BrickflowUI now supports both classic dashboard charts and richer operational visuals.

## Classic charts

### `AreaChart`

Best for throughput, rows processed, or cost over time.

### `LineChart`

Best for SLA, latency, freshness, or success-rate trend lines.

### `BarChart`

Best for pipeline comparison by team, domain, or environment.

### `DonutChart`

Best for incident mix, owner mix, or environment mix.

## Expanded chart toolkit

### `ScatterChart`

Use for anomaly views like duration vs cost.

### `ComposedChart`

Use when you need bars and lines in one visual.

```python
db.ComposedChart(
    data=rows,
    x_key="day",
    bar_keys=["runs"],
    line_keys=["success_rate"],
    title="Runs And Success Rate",
)
```

### `GaugeChart`

Use for a single health or readiness score.

### `RadarChart`

Use for scorecards across multiple dimensions.

### `Heatmap`

Use for hour-by-layer, day-by-team, or incident density views.

### `FunnelChart`

Use for stage drop-off.

### `TreeMap`

Use for cost concentration, storage concentration, or workload share.

## `Plot`

Use `Plot` when you need raw Plotly power beyond the built-in chart set.

## `PipelineGraph`

`PipelineGraph` is the operational visualization primitive for data engineering apps.

```python
db.PipelineGraph(
    nodes=[
        {"id": "bronze", "label": "Bronze Orders", "status": "running"},
        {"id": "silver", "label": "Silver Quality", "status": "watch"},
        {"id": "gold", "label": "Gold Mart", "status": "healthy"},
    ],
    edges=[
        {"from": "bronze", "to": "silver"},
        {"from": "silver", "to": "gold"},
    ],
    on_node_click=select_node,
)
```

## Shared chart props

Most visual components support:

- `title`
- `height`
- `loading`
- `empty_message`
- click callbacks where appropriate

## Dashboard composition pattern

```python
db.Grid(
    [
        db.Card([db.ComposedChart(...)]),
        db.Card([db.Heatmap(...)]),
        db.Card([db.GaugeChart(...)]),
        db.Card([db.PipelineGraph(...)]),
    ],
    cols=2,
    gap=4,
)
```
