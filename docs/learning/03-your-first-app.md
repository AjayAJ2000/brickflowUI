# 03. Your First App

## Learning Goal

Build a small interactive app with state, layout, text, and a button.

## Start With A Page

```python
import brickflowui as db

app = db.App(title="First BrickflowUI App")

@app.page("/", title="Home")
def home():
    return db.Text("Hello from BrickflowUI", variant="h1")

if __name__ == "__main__":
    app.run()
```

Pages are normal Python functions decorated with `@app.page(...)`.

## Add Layout

```python
@app.page("/", title="Home")
def home():
    return db.Column(
        [
            db.Text("Hello from BrickflowUI", variant="h1"),
            db.Text("This is my first page."),
        ],
        gap=4,
        padding=6,
    )
```

`Column` stacks components vertically.

## Add State

```python
@app.page("/", title="Home")
def home():
    count, set_count = db.use_state(0)

    return db.Card(
        [
            db.Text("Counter", variant="h2"),
            db.Text(f"Count: {count}"),
            db.Button("Increment", on_click=lambda: set_count(count + 1)),
        ],
        elevated=True,
    )
```

State makes the page interactive.

## Complete First App

```python
import brickflowui as db

app = db.App(title="First BrickflowUI App")

@app.page("/", title="Home")
def home():
    count, set_count = db.use_state(0)

    return db.Column(
        [
            db.Text("My First BrickflowUI App", variant="h1"),
            db.Card(
                [
                    db.Text("Counter", variant="h2"),
                    db.Text(f"You clicked {count} times."),
                    db.Button("Increment", on_click=lambda: set_count(count + 1)),
                ],
                elevated=True,
                animated=True,
            ),
        ],
        gap=4,
        padding=6,
    )

if __name__ == "__main__":
    app.run()
```

## Common Mistakes

- Calling `set_count(count + 1)` immediately instead of inside `lambda`.
- Returning a raw list instead of a component.
- Forgetting `if __name__ == "__main__": app.run()`.
- Expecting state to be shared across all users. State is session-oriented.

## Exercise

Add two more buttons:

- one that decrements the count
- one that resets the count to zero

## Checkpoint

You should now be able to create a page, compose layout, and update UI from a button click.
