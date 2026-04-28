# BrickflowUI


Build dashboards, landing pages, chatbot workspaces, internal tools, and Databricks Apps in pure Python.

BrickflowUI is designed for teams that want a Python-first authoring experience without giving up structured UI composition, interactivity, theming, or packaged deployment.

## What you can build

- executive dashboards
- data pipeline command centers
- chatbot and copilot workspaces
- landing pages and internal product sites
- Databricks App portals
- operational triage and release management tools

## Start here

If you are new to the library, follow these in order:

1. [Learn BrickflowUI](./learning/index.md)
2. [Quick Start](./GETTING_STARTED.md)
3. [Architecture](./ARCHITECTURE.md)
4. [Component Gallery](./components/index.md)
5. [Examples](./EXAMPLES.md)
6. [Databricks Apps Guide](./DATABRICKS_APPS.md)

## Why teams choose it

- Python-first UI authoring with no frontend code required for common use cases
- session-scoped state with reactive rerenders
- built-in layout, forms, tables, charts, overlays, and workflow patterns
- packaged frontend assets that work in stricter environments like Databricks Apps
- theming and branding support for enterprise rollout

## Key documentation paths

- [Architecture](./ARCHITECTURE.md) for the runtime model and packaging details
- [Component Gallery](./components/index.md) for component-by-component learning
- [Visualizations And Pipelines](./VISUALIZATIONS.md) for the modern chart and graph surface
- [Theming](./THEMING.md) for branding and design tokens
- [Troubleshooting](./TROUBLESHOOTING.md) for the common deployment and runtime problems

## Install

```bash
pip install brickflowui
```

```python
import brickflowui as db
```

## First app

```python
import brickflowui as db

app = db.App(title="Hello BrickflowUI")

@app.page("/", title="Home")
def home():
    count, set_count = db.use_state(0)
    return db.Column(
        [
            db.Text("Hello BrickflowUI", variant="h1"),
            db.Text(f"Count: {count}"),
            db.Button("Increment", on_click=lambda: set_count(count + 1)),
        ],
        gap=4,
        padding=6,
    )

if __name__ == "__main__":
    app.run()
```
