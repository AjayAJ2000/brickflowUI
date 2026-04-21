# 01. What Is BrickflowUI

## Learning Goal

Understand what BrickflowUI is, what it is good for, and how it differs from notebooks, Streamlit-style rerun apps, and hand-written frontend apps.

## What BrickflowUI Is

BrickflowUI is a Python UI framework for building dashboards, portals, internal tools, Databricks Apps, and data products.

You build pages from Python functions:

```python
import brickflowui as db

app = db.App(title="Ops Portal")

@app.page("/", title="Home")
def home():
    return db.Text("Hello BrickflowUI", variant="h1")

if __name__ == "__main__":
    app.run()
```

The UI is not a notebook cell. It is an app with pages, layout components, controls, state, charts, tables, API routes, packaged frontend assets, and Databricks-friendly runtime behavior.

## When To Use It

Use BrickflowUI when you want to build:

- data engineering dashboards
- pipeline command centers
- admin portals
- approval workflows
- lightweight internal apps
- assistant or chatbot workspaces
- Databricks Apps backed by SQL or Unity Catalog

## When Not To Use It

BrickflowUI may not be the right fit when:

- you need a public consumer-scale website with custom frontend engineering
- you need pixel-perfect marketing animation controlled by frontend specialists
- you need a full React codebase with custom client-side routing
- you only need a one-off notebook chart

## The Mental Shift

Instead of thinking:

> I need to write HTML, CSS, JavaScript, and backend APIs.

Think:

> I need to return a tree of Python components, then update state when users interact.

That tree is called a VNode tree.

## A Tiny Example

```python
@app.page("/")
def home():
    count, set_count = db.use_state(0)

    return db.Card(
        [
            db.Text("Counter", variant="h2"),
            db.Text(f"Current value: {count}"),
            db.Button("Increment", on_click=lambda: set_count(count + 1)),
        ]
    )
```

What happens:

1. Python renders the component tree.
2. The browser displays it.
3. The user clicks the button.
4. BrickflowUI calls your Python handler.
5. State changes.
6. The changed UI is sent back to the browser.

## Common Mistakes

- Treating BrickflowUI like a notebook instead of an app framework.
- Putting too much business logic directly inside UI code.
- Forgetting that every interactive value should be connected to state.
- Expecting custom frontend files to be required for normal dashboards.

## Exercise

Write down one app you want to build with BrickflowUI. Classify it as a dashboard, portal, pipeline command center, chatbot workspace, landing page, or workflow app.

Then list the first three components you think it needs.

## Checkpoint

You should now understand that BrickflowUI is a Python-first app framework that renders interactive browser UIs without requiring you to write frontend code.
