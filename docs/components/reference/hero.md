# Hero

## What It Does

`Hero` creates a premium top-of-page introduction for dashboards, portals, landing pages, and internal product surfaces.

## Inputs To Know

- `title`
- `subtitle`
- `eyebrow`
- `tagline`
- `image`
- `image_alt`
- `actions`
- `badges`
- `visual`
- `animated`, `animation`, `animation_delay`

## Example

```python
import brickflowui as db

hero = db.Hero(
    "Workspace command center",
    subtitle="Monitor jobs, data products, and release readiness in one place.",
    eyebrow="Acme Analytics",
    tagline="Built with BrickflowUI",
    image="assets/logo.svg",
    badges=[db.Badge("Runtime secure", color="green")],
    actions=[
        db.Button("Open report", variant="secondary"),
        db.Button("Create alert"),
    ],
)
```

## Works Well With

`Badge`, `Button`, `SectionHeader`, `StatusStrip`, `Image`, `TopNav`

## Notes

- Use `image` for a small inline logo or product mark in the hero header itself.
- Use `visual` when you want the right-hand side of the hero to host charts, cards, or another composed component.
- `Hero` is a strong fit for both dashboards and landing pages, so it is a good place to express the product brand clearly.
