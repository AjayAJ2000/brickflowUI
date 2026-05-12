# Video

## What It Does

`Video` renders local or remote videos directly from your BrickflowUI script.

## When To Use It

Use `Video` for:

- short product walkthroughs
- embedded motion demos in docs-like pages
- loading and onboarding support media
- internal runbook clips

## Inputs To Know

- `src`
- `poster`
- `controls`
- `autoplay`
- `loop`
- `muted`
- `caption`
- `width`
- `height`

## Example

```python
import brickflowui as db

demo = db.Video(
    "assets/demo.mp4",
    poster="assets/poster.png",
    caption="Quarterly analytics workflow walkthrough",
    controls=True,
)
```

## Works Well With

`Card`, `Hero`, `Accordion`, `Embed`

## Notes

- Local video paths are served automatically through the runtime asset layer.
- For a startup screen, use `App(loading={"video": ...})`.
