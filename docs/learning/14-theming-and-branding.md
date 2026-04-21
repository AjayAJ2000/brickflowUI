# 14. Theming And Branding

## Learning Goal

Make apps feel intentional and branded without writing custom frontend code.

## Theme Object

You can pass a theme dictionary to `App`:

```python
app = db.App(
    theme={
        "branding": {"title": "Astellas Pipeline Studio"},
        "colors": {
            "primary": "#C81E5B",
            "primary_hover": "#A8184A",
            "background": "#F7F8F7",
            "surface": "#FFFFFF",
            "text": "#1B1F1D",
            "text_muted": "#5E6A64",
            "border": "#E2E8E3",
            "success": "#0F8A6C",
            "warning": "#C67A00",
            "error": "#B42318",
            "info": "#2563EB",
        },
        "borders": {"radius": "18px"},
    }
)
```

## What Branding Means

Branding is not just colors. A polished app also needs:

- clear typography
- spacing rhythm
- consistent surfaces
- restrained motion
- meaningful badges
- useful empty states
- action hierarchy

## Hero Pattern

```python
db.Hero(
    title="Pipeline observability for serious internal data apps",
    subtitle="Monitor freshness, reliability, and cost from one workspace.",
    eyebrow="Data Platform",
    badges=[db.Badge("Live", color="green")],
    actions=[db.Button("Refresh"), db.Button("Open runbook", variant="secondary")],
)
```

## Card Polish

```python
db.Card(
    [
        db.Stat("Success", "99.1%", delta="+0.3 pts", delta_type="increase"),
        db.Text("Stable reliability across selected pipelines.", variant="caption", muted=True),
    ],
    elevated=True,
    hover=True,
    animated=True,
)
```

## Common Mistakes

- Using brand colors everywhere.
- Mixing too many badge colors.
- Making every card elevated.
- Ignoring empty states and loading states.
- Choosing visual polish before information hierarchy.

## Exercise

Create two themes:

- a calm enterprise theme
- a high-energy command-center theme

Apply both to the same dashboard and compare readability.

## Checkpoint

You should be able to make a BrickflowUI app feel branded, clear, and intentional.
