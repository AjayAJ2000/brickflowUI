# 05. Layout Skills

## Learning Goal

Use BrickflowUI layout primitives to create readable, responsive pages.

## Core Layout Components

The most important layout components are:

- `Column`
- `Row`
- `Grid`
- `Card`
- `Spacer`
- `Divider`

## Column

Use `Column` for vertical structure.

```python
db.Column(
    [
        db.Text("Title", variant="h1"),
        db.Text("Subtitle"),
    ],
    gap=4,
    padding=6,
)
```

## Row

Use `Row` for horizontal alignment.

```python
db.Row(
    [
        db.Text("Pipeline Health", variant="h2"),
        db.Button("Refresh"),
    ],
    justify="between",
    align="center",
)
```

## Grid

Use `Grid` for dashboards.

```python
db.Grid(
    [
        db.Card([db.Stat("Runs", "96")]),
        db.Card([db.Stat("Success", "99.1%")]),
        db.Card([db.Stat("Freshness", "11m")]),
    ],
    cols=3,
    gap=4,
)
```

On smaller screens, the grid collapses responsively.

## Card

Use `Card` to group related content.

```python
db.Card(
    [
        db.Text("Freshness", variant="h3"),
        db.Progress(88, label="Freshness score"),
    ],
    elevated=True,
    hover=True,
)
```

## Page Skeleton Pattern

Most apps can start with:

```python
return db.Column(
    [
        db.Row(
            [
                db.Column(
                    [
                        db.Text("Dashboard", variant="h1"),
                        db.Text("Operational overview", muted=True),
                    ]
                ),
                db.Button("Refresh"),
            ],
            justify="between",
        ),
        db.Grid(kpi_cards, cols=4),
        db.Grid(chart_cards, cols=2),
        db.Card([table]),
    ],
    gap=5,
    padding=6,
)
```

## Common Mistakes

- Using too many nested `Row` components when a `Grid` would be clearer.
- Putting every component in its own `Card`.
- Forgetting `wrap=True` for rows that may overflow on small screens.
- Using large padding everywhere instead of creating a page-level padding once.

## Exercise

Build a dashboard shell with a title row, four KPI cards, two chart cards, and one table card.

## Checkpoint

You should be able to create structured pages with clear vertical rhythm, responsive grids, and grouped surfaces.
