# 11. Charts And Visualizations

## Learning Goal

Choose the right chart component and connect chart interactions to state.

## Chart Components

BrickflowUI includes:

- `AreaChart`
- `LineChart`
- `BarChart`
- `DonutChart`
- `ScatterChart`
- `ComposedChart`
- `GaugeChart`
- `RadarChart`
- `Heatmap`
- `FunnelChart`
- `TreeMap`
- `SparklineStat`

## Area Chart

Use for trends with volume.

```python
db.AreaChart(
    data=[
        {"day": "Mon", "rows": 120},
        {"day": "Tue", "rows": 148},
    ],
    x_key="day",
    y_keys=["rows"],
    title="Rows Processed",
)
```

## Composed Chart

Use when you need multiple signals in one chart.

```python
db.ComposedChart(
    data=[
        {"day": "Mon", "runs": 85, "success": 98.6, "cost": 310},
        {"day": "Tue", "runs": 89, "success": 98.9, "cost": 328},
    ],
    x_key="day",
    bar_keys=["runs"],
    line_keys=["success"],
    area_keys=["cost"],
    title="Runs, Success, and Cost",
)
```

## Gauge Chart

Use for one important score.

```python
db.GaugeChart(97.8, label="Reliability score")
```

## Heatmap

Use for failures, latency, or freshness by time and layer.

```python
db.Heatmap(
    data=[
        {"hour": "08", "layer": "bronze", "failures": 0},
        {"hour": "08", "layer": "silver", "failures": 2},
    ],
    x_key="hour",
    y_key="layer",
    value_key="failures",
    title="Failures by Hour and Layer",
)
```

## Chart Clicks

Many charts support `on_click`:

```python
selected, set_selected = db.use_state("No point selected")

db.ScatterChart(
    rows,
    x_key="cost",
    y_key="duration",
    title="Cost vs Duration",
    on_click=lambda point: set_selected(point["pipeline"]),
)
```

## Loading And Empty States

```python
db.BarChart(
    data=rows,
    x_key="week",
    y_keys=["runs"],
    loading=is_loading,
    empty_message="No run data available.",
)
```

## Common Mistakes

- Using too many chart types on one page.
- Charting unfiltered data while the table shows filtered data.
- Forgetting units in titles or labels.
- Making every chart clickable without a useful drilldown.

## Exercise

Build a page with:

- a `GaugeChart` for success rate
- a `ComposedChart` for runs and cost
- a `Heatmap` for failures
- a `Table` showing the same filtered rows

## Checkpoint

You should be able to choose chart types based on the question your dashboard needs to answer.
