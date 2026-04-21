# 04. Mental Model

## Learning Goal

Understand the component tree, render cycle, event flow, and how BrickflowUI keeps Python and the browser connected.

## Component Tree

Every BrickflowUI component returns a VNode.

```python
db.Text("Hello")
db.Button("Run")
db.Card([db.Text("Inside")])
```

When you return a layout:

```python
return db.Column(
    [
        db.Text("A"),
        db.Text("B"),
    ]
)
```

you are returning a tree:

```text
Column
  Text
  Text
```

## Render Cycle

The render cycle is:

1. Browser connects to the app runtime.
2. Python calls the current page function.
3. The page function returns a VNode tree.
4. The tree is serialized to JSON.
5. The frontend renders the JSON.
6. User events are sent back to Python.
7. Python handlers update state.
8. BrickflowUI sends a patch back to the browser.

## Events

When you write:

```python
db.Button("Refresh", on_click=refresh)
```

BrickflowUI registers an event handler. The browser does not know your Python function. It knows an event id. When clicked, the event id is sent to Python, and Python calls `refresh`.

## State

State is what lets the next render remember something.

```python
value, set_value = db.use_state("all")
```

When `set_value("gold")` runs, the page renders again with `value == "gold"`.

## Why This Matters

If your UI does not update, ask:

- Is the value stored in state?
- Is the input connected to a setter?
- Does the component receive the current state value?
- Is the event handler being called?
- Is the page returning the new value?

## Example

```python
@app.page("/")
def home():
    layer, set_layer = db.use_state("bronze")

    return db.Column(
        [
            db.Select(
                name="layer",
                label="Layer",
                value=layer,
                options=[
                    {"label": "Bronze", "value": "bronze"},
                    {"label": "Silver", "value": "silver"},
                    {"label": "Gold", "value": "gold"},
                ],
                on_change=set_layer,
            ),
            db.Text(f"Selected layer: {layer}"),
        ]
    )
```

The select value and text are both driven by the same state.

## Common Mistakes

- Creating local variables and expecting them to survive user events.
- Updating a variable instead of state.
- Passing a fixed value to an input instead of the current state value.
- Mutating lists or dictionaries in place and expecting the UI to notice.

## Exercise

Create a page with a `Select` and a `Badge`. The badge should show the currently selected environment: dev, staging, or prod.

## Checkpoint

You should be able to explain the path from Python component tree to browser event and back to Python state.
