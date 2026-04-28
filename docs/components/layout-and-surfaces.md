# Layout And Surfaces

These components define the page skeleton before you add data or interaction.

## `Column`

Use `Column` for vertical stacking.

```python
db.Column(
    [
        db.Text("Overview", variant="h2"),
        db.Card([db.Text("KPI content")]),
    ],
    gap=4,
    padding=6,
)
```

Useful props:

- `gap`
- `padding`
- `align`
- `style`

## `Row`

Use `Row` for horizontal grouping.

```python
db.Row(
    [
        db.Badge("Live", color="green"),
        db.Badge("Prod", color="blue"),
    ],
    gap=2,
    justify="between",
    wrap=True,
)
```

Useful props:

- `gap`
- `wrap`
- `align`
- `justify`

## `Grid`

Use `Grid` when you want a responsive multi-card layout.

```python
db.Grid(
    [
        db.Card([db.Text("Card A")]),
        db.Card([db.Text("Card B")]),
        db.Card([db.Text("Card C")]),
    ],
    cols=3,
    gap=4,
)
```

On smaller screens the grid collapses automatically.

## `Card`

Use `Card` for grouped information and interactive sections.

```python
db.Card(
    [
        db.Text("Freshness", variant="h3"),
        db.Text("11 minutes"),
    ],
    bordered=True,
    elevated=True,
    hover=True,
    animated=True,
)
```

Useful props:

- `title`
- `subtitle`
- `bordered`
- `padding`
- `hover`
- `elevated`
- `animated`
- `animation`
- `animation_delay`

## `Divider`

Use `Divider()` to split sections and `Divider("Filters")` to add a labeled break.

## `Spacer`

Use `Spacer(2)` or `Spacer(4)` when a small visual pause is clearer than adjusting the parent gap.

## `Hero`

Use `Hero` for landing pages, executive overview headers, or product-style intros.

```python
db.Hero(
    "Pipeline Command Center",
    subtitle="Observe freshness, SLA, cost, and incidents in one place.",
    eyebrow="Data Platform",
    badges=[db.Badge("Live", color="green")],
    actions=[db.Button("Open Runbook")],
)
```

## `SectionHeader`

Use `SectionHeader` inside larger pages to anchor a major section.

```python
db.SectionHeader(
    "Lakehouse Health",
    subtitle="Current state of bronze, silver, and gold data products.",
    actions=[db.Button("Export")],
)
```

## `StatusStrip`

Use `StatusStrip` when you want compact signal cards above the heavier visualizations.

```python
db.StatusStrip(
    [
        {"label": "Freshness", "value": "11m", "status": "healthy"},
        {"label": "SLA", "value": "99.4%", "status": "healthy"},
        {"label": "Failures", "value": "2", "status": "warning"},
    ]
)
```

## Composition pattern

This is the most reliable page composition pattern for dashboards:

```python
db.Column(
    [
        db.Hero(...),
        db.SectionHeader(...),
        db.StatusStrip(...),
        db.Grid([...], cols=3, gap=4),
    ],
    gap=5,
    padding=6,
)
```
