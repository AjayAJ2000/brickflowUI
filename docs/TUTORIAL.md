# BrickflowUI Tutorial: Building Reactive Databricks Apps

Welcome to BrickflowUI! This tutorial will guide you through building a modern, interactive web application for Databricks using only Python.

## 1. Core Philosophy

BrickflowUI is inspired by React but tailored for the Python ecosystem and Databricks. Key concepts:
- **Declarative UI**: You describe *what* the UI should look like based on the current state.
- **Unidirectional Data Flow**: State updates trigger re-renders.
- **Reactive Hooks**: Management of state and side effects using `use_state`, `use_effect`, and `use_memo`.
- **WebSocket Communication**: Only the minimal changes (patches) are sent to the frontend.

## 2. Basic Layout

Every BrickflowUI component is a function returning a `VNode`. Let's start with a simple layout.

```python
import brickflowui as db

app = db.App(title="Tutorial App")

@app.page("/")
def home():
    return db.Column([
        db.Text("Welcome to BrickflowUI", variant="h1"),
        db.Text("Building UIs in Python has never been easier.", variant="body"),
        db.Row([
            db.Button("Learn More", variant="primary"),
            db.Button("Get Started", variant="outline"),
        ], gap=4)
    ], padding=8, gap=6)

if __name__ == "__main__":
    app.run()
```

### Layout Primitives:
- `db.Column`: Vertical stack.
- `db.Row`: Horizontal stack.
- `db.Grid`: Multi-column layout.
- `db.Card`: Container with a border and optional title.

## 3. State Management with `use_state`

The most important hook is `use_state`. It returns the current value and a setter function.

```python
@app.page("/counter")
def counter():
    count, set_count = db.use_state(0)
    
    return db.Card([
        db.Text(f"Current Count: {count}", variant="h2"),
        db.Button("Increment", on_click=lambda: set_count(count + 1))
    ], title="Counter Example")
```

> [!TIP]
> Changes to state automatically trigger a re-render of the component. BrickflowUI optimizes this by only sending the diff to the browser.

## 4. Input and Forms

Handling user input is straightforward. Use `on_change` handlers to update state.

```python
@app.page("/form")
def input_demo():
    name, set_name = db.use_state("")
    
    return db.Column([
        db.Input(label="Enter your name", value=name, on_change=set_name),
        db.Text(f"Hello, {name}!" if name else "Please enter your name."),
    ], gap=4)
```

## 5. Side Effects with `use_effect`

`use_effect` allows you to perform actions when a component mounts or when certain dependencies change.

```python
@app.page("/timer")
def timer_demo():
    seconds, set_seconds = db.use_state(0)
    
    def start_timer():
        import asyncio
        async def tick():
            while True:
                await asyncio.sleep(1)
                set_seconds(lambda s: s + 1)
        # In a real app, you'd handle task cancellation
        asyncio.create_task(tick())

    db.use_effect(start_timer, []) # Empty deps means run only on mount
    
    return db.Text(f"Elapsed time: {seconds}s", variant="code")
```

## 6. Real-time Data with Charts

BrickflowUI comes with built-in charting components.

```python
import random

@app.page("/charts")
def chart_demo():
    data, set_data = db.use_state([
        {"time": "12:00", "value": 10},
        {"time": "12:01", "value": 15},
    ])
    
    def refresh():
        new_point = {"time": "12:02", "value": random.randint(10, 50)}
        set_data(data + [new_point])

    return db.Column([
        db.Button("Refresh Data", on_click=refresh),
        db.AreaChart(data=data, x_key="time", y_keys=["value"])
    ])
```

## 7. Working with Databricks SQL

In a Databricks environment, use the built-in SQL helpers to fetch data directly from your tables.

```python
from brickflowui.databricks import sql

@app.page("/query")
def sql_page():
    rows = db.use_memo(
        lambda: sql.query_to_records("SELECT * FROM samples.nyctaxi.trips LIMIT 10"),
        []
    )
    
    return db.Table(data=rows)
```

## 8. Deployment

To deploy your app to Databricks:
1. Ensure your `app.yaml` specifies the entry point.
2. Ensure `brickflowui` is in your `requirements.txt`.
3. Create a Databricks App and upload your code.

```yaml
# app.yaml
command:
  - python
  - app.py
```

## 9. Branding With YAML

You can keep branding and theme tokens in a YAML file and pass it directly to `App`.

```python
app = db.App(theme="branding.yaml")
```

See [THEMING.md](/D:/Projects/brickflowUI/docs/THEMING.md) for the full theme model.

---

Happy Building!
