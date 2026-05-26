![BrickflowUI](/docs/assets/brickflowui-logo.svg)

# BrickflowUI

Databricks-first Python UI framework for building dashboards, portals, chatbot workspaces, landing pages, and internal web apps with pure Python.

Canonical package name: `brickflowui`

Install:

```bash
pip install brickflowui
```

Import:

```python
import brickflowui as db
```

Documentation:

- [Docs site](https://ajayaj2000.github.io/brickflowUI/)
- [Learn BrickflowUI](https://ajayaj2000.github.io/brickflowUI/learning/)
- [Component Gallery](https://ajayaj2000.github.io/brickflowUI/components/)
- [Architecture](https://ajayaj2000.github.io/brickflowUI/ARCHITECTURE/)

## What BrickflowUI is for

Use BrickflowUI when you want to stay in Python and still ship a serious interactive app.

Good fits:

- executive dashboards
- data engineering pipeline portals
- Databricks App experiences
- internal ops tools
- chatbot and copilot UIs
- product-style landing pages

## Why teams use it

- Python-first authoring model
- session-scoped reactive state
- multi-page routing and app shell support
- built-in tables, forms, overlays, charts, pipeline graphs, workflow boards, and chat patterns
- packaged frontend assets that work in stricter CSP environments
- branding and theme tokens for enterprise rollout

## Quick start

Scaffold a new app:

```bash
brickflowui new my_app
cd my_app
brickflowui dev
```

Or write one manually:

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

## Core concepts

BrickflowUI works as:

1. Python page functions produce a `VNode` tree.
2. The server serializes that tree and sends it over WebSocket.
3. The frontend renders it and returns interaction events.
4. Python handlers update state and trigger rerenders.

This gives you a React-style interaction model without requiring users to write frontend code.

## Current component surface

### Layout and app structure

- `Column`
- `Row`
- `Grid`
- `Card`
- `Divider`
- `Spacer`
- `Hero`
- `SectionHeader`
- `StatusStrip`

### Inputs and overlays

- `Button`
- `Input`
- `Select`
- `Checkbox`
- `Toggle`
- `Slider`
- `DateRangePicker`
- `MultiSelect`
- `Form`
- `Modal`
- `Drawer`
- `Popup`

### Data and workflow

- `Table`
- `Timeline`
- `SparklineStat`
- `Stepper`
- `KanbanBoard`
- `ChatMessage`
- `ChatInput`
- `PipelineGraph`

### Charts

- `Plot`
- `AreaChart`
- `BarChart`
- `LineChart`
- `DonutChart`
- `ScatterChart`
- `ComposedChart`
- `GaugeChart`
- `RadarChart`
- `Heatmap`
- `FunnelChart`
- `TreeMap`

## Databricks Apps

Use this minimum setup:

`requirements.txt`

```text
brickflowui>=0.1.9
```

Install from GitHub instead:

```text
brickflowui @ git+https://github.com/AjayAJ2000/brickflowUI.git@main
```

`app.yaml`

```yaml
command:
  - python
  - app.py
```

Important packaging rule:

The installed package must contain:

```text
brickflowui/frontend/dist/index.html
brickflowui/frontend/dist/assets/*
```

If those files are missing, Databricks Apps often stop at the loading shell.

## Local development

Framework tests:

```bash
python -m pytest -q
```

Frontend build:

```bash
cd frontend
npm run build
```

Docs build:

```bash
python -m mkdocs build
```

Package build:

```bash
python -m build
```

## Recommended playgrounds

- `examples/local_playground/app.py` for framework validation
- `examples/component_studio/app.py` for a broad component walkthrough
- `examples/acme_analytics_command_center/app.py` for a product-style shell reference

## Open source standards

- [Contributing guide](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security policy](./SECURITY.md)
- [Support guide](./SUPPORT.md)

## Repo map

```text
brickflowui/
  app.py
  components.py
  server.py
  state.py
  vdom.py
  frontend/dist/
  cli/
  databricks/

frontend/
  src/
  vite.config.ts

docs/
  learning/
  components/
  ARCHITECTURE.md
```

## License

MIT

