# Getting Started

## Install

```bash
pip install bricksflowui
```

With Databricks support:

```bash
pip install "bricksflowui[databricks]"
```

## Create a minimal app

```python
import brickflowui as db

app = db.App(title="My App")

@app.page("/", title="Home")
def home():
    return db.Column(
        [
            db.Text("Hello from BricksFlowUI", variant="h1"),
            db.Button("Click me"),
        ],
        padding=6,
        gap=4,
    )

if __name__ == "__main__":
    app.run()
```

## Run it

```bash
python app.py
```

Open `http://127.0.0.1:8050`.

## Create a scaffolded project

```bash
brickflowui new my_app
cd my_app
brickflowui dev
```

## Install names vs import names

- install package: `bricksflowui`
- CLI: `brickflowui` or `bricksflowui`
- standard Python import: `import brickflowui as db`

## Next docs

- [Tutorial](./TUTORIAL.md)
- [Theming](./THEMING.md)
- [API Reference](./API_REFERENCE.md)
- [Publishing](./PUBLISHING.md)
