# BricksFlowUI

Build dashboards, portals, and internal web apps for Databricks using pure Python.

BricksFlowUI is designed to feel simple for first-time users and structured enough for teams building larger apps with multiple pages, auth, theming, and data access.

## What you get

- Python-first UI building with no frontend framework required
- Reactive state with hooks like `use_state`
- Multi-page apps with routing
- Built-in components for layout, forms, tables, charts, and navigation
- Auth-ready app structure for public, user-only, and app-only pages
- YAML-based branding and theme customization

## Start here

If you are new to the library, follow these in order:

1. [Quick Start](./GETTING_STARTED.md) to install the package and run your first app
2. [First App Tutorial](./TUTORIAL.md) to build a more realistic dashboard-style app
3. [Theming](./THEMING.md) to brand your app
4. [API Reference](./API_REFERENCE.md) when you want to explore the full surface area

## Install

```bash
pip install bricksflowui
```

Then import it with:

```python
import brickflowui as db
```

## First app

```python
import brickflowui as db

app = db.App(title="Hello BricksFlowUI")

@app.page("/", title="Home")
def home():
    count, set_count = db.use_state(0)
    return db.Column(
        [
            db.Text("Hello BricksFlowUI", variant="h1"),
            db.Text(f"Count: {count}"),
            db.Button("Increment", on_click=lambda: set_count(count + 1)),
        ],
        gap=4,
        padding=6,
    )

if __name__ == "__main__":
    app.run()
```

Run it with:

```bash
python app.py
```

Open `http://127.0.0.1:8050`.

## Free hosting recommendation

For a free public documentation site, the best fit for this project is:

- MkDocs + Material for MkDocs for authoring and navigation
- GitHub Pages for hosting
- GitHub Actions for automatic deployment

This repository already includes:

- `mkdocs.yml`
- `.github/workflows/docs.yml`

Once GitHub Pages is enabled for the repository, pushes to `main` can publish the docs site automatically.
