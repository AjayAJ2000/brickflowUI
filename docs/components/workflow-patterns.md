# Workflow Patterns

These components help you build applications, not just isolated widgets.

## `Stepper`

Use for release phases, onboarding flows, or medallion progression.

```python
db.Stepper(
    [
        {"label": "Bronze"},
        {"label": "Silver"},
        {"label": "Gold"},
    ],
    active=1,
)
```

## `KanbanBoard`

Use for operational triage, incident management, and action queues.

```python
db.KanbanBoard(
    [
        {"id": "todo", "label": "Todo", "cards": [{"id": "a", "title": "Fix SLA"}]},
        {"id": "doing", "label": "Doing", "cards": [{"id": "b", "title": "Backfill silver"}]},
    ],
    on_card_click=handle_card_click,
)
```

## `ChatMessage`

Use for assistant/copilot responses, run summaries, or operator notes.

```python
db.ChatMessage("assistant", "I found two delayed pipelines.", name="Ops Copilot")
db.ChatMessage("user", "Show the most recent failures.")
```

## `ChatInput`

Use with `ChatMessage` to create chatbot-style workflows.

## Full pattern

```python
db.Column(
    [
        db.Hero(...),
        db.StatusStrip(...),
        db.Row(
            [
                db.Card([db.PipelineGraph(...)]),
                db.Card([db.KanbanBoard(...)]),
            ],
            gap=4,
            wrap=True,
        ),
        db.Card(
            [
                db.ChatMessage("assistant", answer, name="Ops Copilot"),
                db.ChatInput(value=prompt, on_change=set_prompt, on_submit=submit_prompt),
            ]
        ),
    ],
    gap=5,
)
```
