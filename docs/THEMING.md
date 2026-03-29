# BrickflowUI Theming

BrickflowUI supports loading app branding and design tokens from a YAML or JSON file:

```python
import brickflowui as db

app = db.App(theme="branding.yaml")
```

## Theme Model

```yaml
branding:
  title: "Acme Ops Portal"
  logo: "/static/acme-logo.svg"
  favicon: "/static/acme-favicon.ico"

colors:
  primary: "#FF5F2E"
  primary_hover: "#D9481C"
  background: "#F7F7F5"
  surface: "#FFFFFF"
  text: "#18181B"
  text_muted: "#71717A"
  border: "#E4E4E7"
  success: "#16A34A"
  warning: "#D97706"
  error: "#DC2626"
  link: "#1D4ED8"

typography:
  font_family: "'IBM Plex Sans', sans-serif"
  font_mono: "'IBM Plex Mono', monospace"
  base_size: "15px"

spacing:
  unit: "6px"

borders:
  radius: "14px"
```

## Notes

- `branding.title` becomes the browser tab title when you leave `App(title=...)` at its default.
- `branding.logo` is used by the app shell sidebar when `App(logo=...)` is not provided directly.
- `branding.favicon` is injected into the HTML shell automatically.
- Friendly aliases are supported:
  - `background` maps to `bg`
  - `primary_hover` maps to `primary-hover`
  - `text_muted` maps to `text-muted`
  - `font_family` maps to `sans`
  - `base_size` maps to `base-size`
  - `borders.radius` maps to the default corner radius token

## Recommendation

For teams, keep one shared branding YAML per product and let apps override only the few values they need locally. That gives you consistent portals without forcing every app author to hand-roll theme tokens.
