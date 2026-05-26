# BrickflowUI

<div class="bf-docs-hero">
  <div class="bf-docs-hero-copy">
    <p class="bf-docs-eyebrow">Python-First UI Framework</p>
    <h1>Build serious dashboards, portals, copilots, and Web Apps in pure Python.</h1>
    <p>
      BrickflowUI is designed for teams that want a Python-first authoring experience without giving up
      structured UI composition, interactivity, theming, professional branding, or packaged deployment.
    </p>
  </div>
  <div class="bf-docs-hero-panel">
    <div class="bf-docs-kpi">
      <strong>What it enables</strong>
      <span>Dashboards, pipeline portals, chatbot workspaces, landing sites, and secure internal tools.</span>
    </div>
    <div class="bf-docs-kpi">
      <strong>What it optimizes</strong>
      <span>Python-first authoring, realtime state, packaged frontend assets, and Platform-safe delivery.</span>
    </div>
  </div>
</div>

## Product Areas

<div class="bf-docs-card-grid">
  <a class="bf-docs-card" href="./GETTING_STARTED/">
    <strong>Get Started</strong>
    <span>Install the library, run your first app, and learn the runtime shape quickly.</span>
  </a>
  <a class="bf-docs-card" href="./learning/">
    <strong>Learn BrickflowUI</strong>
    <span>Follow the step-by-step learning path from first principles to a capstone app.</span>
  </a>
  <a class="bf-docs-card" href="./components/">
    <strong>Component Library</strong>
    <span>Browse the design system, grouped component guides, and detailed reference pages.</span>
  </a>
  <a class="bf-docs-card" href="./PORTAL_TUTORIAL/">
    <strong>Build A Real Portal</strong>
    <span>Walk through a larger SaaS-style portal build with multiple workflows and polished UI patterns.</span>
  </a>
  <a class="bf-docs-card" href="./EXAMPLES/">
    <strong>Examples</strong>
    <span>Explore working apps for analytics, pipelines, landing pages, secure tools, and local validation.</span>
  </a>
  <a class="bf-docs-card" href="./DATABRICKS_APPS/">
    <strong>Databricks Apps</strong>
    <span>Understand how to package, deploy, and run BrickflowUI inside stricter enterprise environments.</span>
  </a>
</div>

## What You Can Build

- executive dashboards
- data pipeline command centers
- chatbot and copilot workspaces
- landing pages and internal product sites
- Databricks App portals
- operational triage and release management tools

## Recommended Reading Order

If you are new to the library, follow these in order:

1. [Quick Start](./GETTING_STARTED.md)
2. [Learn BrickflowUI](./learning/index.md)
3. [Architecture](./ARCHITECTURE.md)
4. [Component Library](./components/index.md)
5. [Build A Real Portal](./PORTAL_TUTORIAL.md)
6. [Examples](./EXAMPLES.md)
7. [Local Development](./LOCAL_DEVELOPMENT.md)
8. [Databricks Apps Guide](./DATABRICKS_APPS.md)

## Why Teams Choose It

- Python-first UI authoring with no frontend code required for common use cases
- session-scoped state with reactive rerenders
- built-in layout, forms, tables, charts, overlays, and workflow patterns
- runtime-aware loading feedback on common interactive components
- packaged frontend assets that work in stricter environments like Databricks Apps
- dark/light mode theming, branded loading screens, and local media assets

## Key Documentation Paths

- [Architecture](./ARCHITECTURE.md) for the runtime model and packaging details
- [Performance And Scalability](./PERFORMANCE.md) for large-app guidance and responsiveness strategy
- [Component Library](./components/index.md) for component-by-component learning
- [Component Pages](./components/catalog.md) for a dedicated page per component
- [Visualizations And Pipelines](./VISUALIZATIONS.md) for the chart and graph surface
- [Theming](./THEMING.md) for branding and design tokens
- [Local Development](./LOCAL_DEVELOPMENT.md) for auth, assets, responsive testing, and runtime debugging
- [Examples](./EXAMPLES.md#local-playground) when you want a fast validation sandbox before working on a bigger app
- [Project Standards](./PROJECT_STANDARDS.md) for repository discipline, release checks, and product-grade expectations
- [Troubleshooting](./TROUBLESHOOTING.md) for common deployment and runtime problems

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
