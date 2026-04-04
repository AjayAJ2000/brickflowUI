# Quick Start

This guide gets a new user from zero to a running BrickflowUI app as quickly as possible.

## 1. Install

Basic install:

```bash
pip install brickflowui
```

If you plan to use Databricks SQL helpers too:

```bash
pip install "brickflowui[databricks]"
```

## 2. Know the package names

- install package: `brickflowui`
- CLI command: `brickflowui`
- Python import: `import brickflowui as db`

That means install and import use different names on purpose.

## 3. Create your first app

Create an `app.py` file:

```python
import brickflowui as db

app = db.App(title="My First App")

@app.page("/", title="Home")
def home():
    count, set_count = db.use_state(0)

    return db.Column(
        [
            db.Text("My First App", variant="h1"),
            db.Text("You are running a BrickflowUI app.", muted=True),
            db.Card(
                [
                    db.Text(f"Count: {count}", variant="h3"),
                    db.Button("Increment", on_click=lambda: set_count(count + 1)),
                ],
                title="Counter",
            ),
        ],
        gap=5,
        padding=6,
    )

if __name__ == "__main__":
    app.run()
```

## 4. Run it

```bash
python app.py
```

Open:

```text
http://127.0.0.1:8050
```

## 5. Create a scaffolded project instead

If you want a starter project instead of writing files manually:

```bash
brickflowui new my_app
cd my_app
brickflowui dev
```

## 6. Add another page

BrickflowUI supports multi-page apps out of the box.

```python
@app.page("/reports", title="Reports")
def reports():
    return db.Column(
        [
            db.Text("Reports", variant="h1"),
            db.Text("Your second page is live."),
        ],
        gap=4,
        padding=6,
    )
```

## 7. Add branding with YAML

Create `branding.yaml`:

```yaml
branding:
  title: "Acme Portal"

colors:
  primary: "#C81E5B"
  background: "#F7F7F5"
  surface: "#FFFFFF"
  text: "#16161A"
  border: "#E4E4E7"
```

Then load it:

```python
app = db.App(theme="branding.yaml")
```

## 8. What to learn next

- [First App Tutorial](./TUTORIAL.md) for a more realistic app
- [Theming](./THEMING.md) for branding and visual customization
- [API Reference](./API_REFERENCE.md) for the full API
- [Examples](./EXAMPLES.md) for runnable app patterns
- [Databricks Apps](./DATABRICKS_APPS.md) for deployment and runtime troubleshooting
- [Publishing](./PUBLISHING.md) for release and PyPI setup
