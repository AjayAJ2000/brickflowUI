# 13. Chatbot And Assistant UI

## Learning Goal

Build assistant-style interfaces that work alongside dashboards.

## Why Add A Chat UI

An assistant UI is useful when users want to ask:

- why is this pipeline delayed?
- which dataset is stale?
- what changed since yesterday?
- what should I investigate first?
- summarize the current incidents

BrickflowUI gives you the building blocks. You decide whether the response comes from simple rules, an API route, a model, or a Databricks job.

## Basic Chat

```python
prompt, set_prompt = db.use_state("")
answer, set_answer = db.use_state("Ask me about pipeline health.")

db.Column(
    [
        db.ChatMessage("assistant", answer, name="Ops Copilot"),
        db.ChatInput(
            value=prompt,
            on_change=set_prompt,
            on_submit=lambda text: set_answer(f"Investigating: {text}"),
        ),
    ],
    gap=4,
)
```

## Chat With Dashboard Context

```python
rows = filtered_rows

def answer_question(text: str):
    if "failed" in text.lower():
        failed = [row for row in rows if row["status"] == "failed"]
        set_answer(f"{len(failed)} pipelines failed in the current filter.")
    else:
        set_answer(f"{len(rows)} pipelines match the current dashboard filters.")
```

Then:

```python
db.ChatInput(value=prompt, on_change=set_prompt, on_submit=answer_question)
```

## Assistant Layout Pattern

```python
db.Card(
    [
        db.SectionHeader("Pipeline Copilot", "Ask questions about the filtered dashboard state."),
        db.ChatMessage("assistant", answer, name="Ops Copilot"),
        db.ChatInput(value=prompt, on_change=set_prompt, on_submit=answer_question),
    ],
    elevated=True,
)
```

## Common Mistakes

- Building a chat box that ignores current dashboard filters.
- Not storing prompt text in state.
- Not clearing or updating the prompt after submit when desired.
- Making the assistant sound authoritative when the data is incomplete.

## Exercise

Create a chat card that answers:

- "what is at risk?"
- "what costs most?"
- "how many pipelines are healthy?"

Use simple Python logic over mock rows.

## Checkpoint

You should be able to create a useful assistant UI that is grounded in dashboard state.
