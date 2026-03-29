# First App Tutorial

This tutorial walks through a realistic BricksFlowUI app that includes:

- layout
- state
- navigation
- KPIs
- charts
- a data table

By the end, you will have a small portal-style app that feels closer to a real dashboard than a toy example.

## What you will build

A simple operations dashboard with:

- an overview page
- a manufacturing page
- KPI cards
- a line chart
- a table

## Step 1: Create the app shell

```python
import brickflowui as db

app = db.App(title="Operations Hub")
```

## Step 2: Add sample data

```python
TREND = [
    {"month": "Jan", "output": 92, "yield": 96.2},
    {"month": "Feb", "output": 96, "yield": 96.5},
    {"month": "Mar", "output": 101, "yield": 97.0},
    {"month": "Apr", "output": 108, "yield": 97.4},
]

LINES = [
    {"line": "Line A", "oee": "84%", "downtime": "3.1%", "status": "On Track"},
    {"line": "Line B", "oee": "79%", "downtime": "4.8%", "status": "Watch"},
    {"line": "Line C", "oee": "87%", "downtime": "2.9%", "status": "On Track"},
]
```

## Step 3: Build reusable KPI cards

```python
def kpi(label: str, value: str, delta: str, delta_type: str) -> db.VNode:
    return db.Card(
        [
            db.Stat(
                label=label,
                value=value,
                delta=delta,
                delta_type=delta_type,
            )
        ],
        bordered=True,
    )
```

## Step 4: Add an overview page

```python
@app.page("/", title="Overview")
def overview():
    return db.Column(
        [
            db.Text("Operations Hub", variant="h1"),
            db.Text("A simple multi-page dashboard built with BricksFlowUI.", muted=True),
            db.Grid(
                [
                    kpi("Output", "108 lots", "+6.9%", "increase"),
                    kpi("Yield", "97.4%", "+0.4 pts", "increase"),
                    kpi("Downtime", "3.6%", "-0.8 pts", "decrease"),
                ],
                cols=3,
                gap=4,
            ),
            db.Card(
                [
                    db.Text("Monthly performance", variant="h3"),
                    db.LineChart(
                        data=TREND,
                        x_key="month",
                        y_keys=["output", "yield"],
                    ),
                ]
            ),
        ],
        gap=6,
        padding=6,
    )
```

## Step 5: Add a manufacturing page

```python
@app.page("/manufacturing", title="Manufacturing")
def manufacturing():
    return db.Column(
        [
            db.Text("Manufacturing", variant="h1"),
            db.Text("Line-level performance snapshot", muted=True),
            db.Table(
                data=LINES,
                columns=[
                    {"key": "line", "label": "Line"},
                    {"key": "oee", "label": "OEE"},
                    {"key": "downtime", "label": "Downtime"},
                    {"key": "status", "label": "Status"},
                ],
            ),
        ],
        gap=5,
        padding=6,
    )
```

## Step 6: Run the app

```python
if __name__ == "__main__":
    app.run()
```

Start it with:

```bash
python app.py
```

Open `http://127.0.0.1:8050`.

## Full example

```python
import brickflowui as db

app = db.App(title="Operations Hub")

TREND = [
    {"month": "Jan", "output": 92, "yield": 96.2},
    {"month": "Feb", "output": 96, "yield": 96.5},
    {"month": "Mar", "output": 101, "yield": 97.0},
    {"month": "Apr", "output": 108, "yield": 97.4},
]

LINES = [
    {"line": "Line A", "oee": "84%", "downtime": "3.1%", "status": "On Track"},
    {"line": "Line B", "oee": "79%", "downtime": "4.8%", "status": "Watch"},
    {"line": "Line C", "oee": "87%", "downtime": "2.9%", "status": "On Track"},
]

def kpi(label: str, value: str, delta: str, delta_type: str) -> db.VNode:
    return db.Card(
        [
            db.Stat(
                label=label,
                value=value,
                delta=delta,
                delta_type=delta_type,
            )
        ],
        bordered=True,
    )

@app.page("/", title="Overview")
def overview():
    return db.Column(
        [
            db.Text("Operations Hub", variant="h1"),
            db.Text("A simple multi-page dashboard built with BricksFlowUI.", muted=True),
            db.Grid(
                [
                    kpi("Output", "108 lots", "+6.9%", "increase"),
                    kpi("Yield", "97.4%", "+0.4 pts", "increase"),
                    kpi("Downtime", "3.6%", "-0.8 pts", "decrease"),
                ],
                cols=3,
                gap=4,
            ),
            db.Card(
                [
                    db.Text("Monthly performance", variant="h3"),
                    db.LineChart(
                        data=TREND,
                        x_key="month",
                        y_keys=["output", "yield"],
                    ),
                ]
            ),
        ],
        gap=6,
        padding=6,
    )

@app.page("/manufacturing", title="Manufacturing")
def manufacturing():
    return db.Column(
        [
            db.Text("Manufacturing", variant="h1"),
            db.Text("Line-level performance snapshot", muted=True),
            db.Table(
                data=LINES,
                columns=[
                    {"key": "line", "label": "Line"},
                    {"key": "oee", "label": "OEE"},
                    {"key": "downtime", "label": "Downtime"},
                    {"key": "status", "label": "Status"},
                ],
            ),
        ],
        gap=5,
        padding=6,
    )

if __name__ == "__main__":
    app.run()
```

## What to do next

- Add auth with `auth_mode` and protected pages
- Add branding with a YAML theme file
- Replace the sample lists with Databricks SQL query results
- Explore the richer examples under `examples/`
