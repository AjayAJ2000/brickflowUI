# Embed

## What It Does

`Embed` renders an external artifact inside an iframe so your BrickflowUI app can host dashboards, reports, notebooks, or other web content.

## When To Use It

Use `Embed` when you need to include an external artifact directly in the workflow instead of sending the user to another tab.

## Inputs To Know

- `src`: the artifact URL
- `title`: accessible title for the frame
- `height`: frame height such as `"420px"` or `"70vh"`
- `allow_fullscreen`: whether fullscreen is allowed
- `loading`: `"lazy"` or `"eager"`
- `sandbox`: optional iframe sandbox policy string

## Works Well With

`Card`, `SectionHeader`, `Tabs`, `Breadcrumbs`, analyst portals, secure review flows

## Example

```python
import brickflowui as db

artifact = db.Embed(
    "https://example.com/report",
    title="Quarterly embedded report",
    height="540px",
)
```

## Notes

- `Embed` is intentionally generic so it can host BI tools, internal docs, demos, and evaluation artifacts.
- The external target still needs to allow iframe embedding on its own side.
