# 09. Forms And API Routes

## Learning Goal

Use forms for backend submissions and custom API routes for app-specific actions.

## When To Use Forms

Use `Form` when a user submits structured data:

- action plan
- approval request
- feedback
- job configuration
- support ticket

Use direct component callbacks when the action is mainly UI state:

- changing filters
- opening a drawer
- selecting a row
- switching views

## Basic Form

```python
db.Form(
    [
        db.Input(name="owner", label="Owner"),
        db.Input(name="summary", label="Summary"),
        db.Button("Submit", html_type="submit"),
    ],
    action="/api/action-plan",
    method="POST",
)
```

## API Route

```python
@app.route("/api/action-plan", methods=["POST"])
async def create_action_plan(request):
    payload = await request.json()
    return {
        "status": "ok",
        "owner": payload.get("owner"),
        "summary": payload.get("summary"),
    }
```

## Full Example

```python
import brickflowui as db

app = db.App()

@app.route("/api/feedback", methods=["POST"])
async def feedback(request):
    payload = await request.json()
    return {"status": "received", "message": payload.get("message", "")}

@app.page("/")
def home():
    return db.Card(
        [
            db.Text("Feedback", variant="h2"),
            db.Form(
                [
                    db.Input(name="name", label="Name"),
                    db.Input(name="message", label="Message", type="textarea"),
                    db.Button("Send", html_type="submit"),
                ],
                action="/api/feedback",
                method="POST",
            ),
        ]
    )
```

## Form Serialization

Inputs with the same name become arrays. This matters for multi-value fields.

## Common Mistakes

- Forgetting `html_type="submit"` on the submit button.
- Expecting `Form` to update page state automatically.
- Using forms for every interaction when simple callbacks are clearer.
- Forgetting `await request.json()` in async route handlers.

## Exercise

Create an action-plan form with owner, priority, summary, and due date.

Return a JSON response from `/api/action-plan`.

## Checkpoint

You should know when to use component callbacks and when to use form submissions/API routes.
