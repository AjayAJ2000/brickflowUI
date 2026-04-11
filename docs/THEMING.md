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

surfaces:
  background: "#F7F7F5"
  surface: "#F1F5F9"
  overlay: "rgba(255,255,255,0.88)"

typography:
  font_family: "'IBM Plex Sans', sans-serif"
  font_mono: "'IBM Plex Mono', monospace"
  base_size: "15px"

spacing:
  unit: "6px"

borders:
  radius: "14px"

shadows:
  small: "0 1px 2px rgba(0,0,0,0.05)"
  medium: "0 10px 30px rgba(0,0,0,0.08)"
  large: "0 18px 45px rgba(0,0,0,0.12)"

motion:
  duration_fast: "140ms"
  duration_normal: "220ms"
  duration_slow: "420ms"
  easing_standard: "cubic-bezier(0.4, 0, 0.2, 1)"
  stagger_step: "40ms"
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
  - `surfaces.background` maps to `canvas`
  - `surfaces.surface` maps to `muted`
  - `shadows.medium` maps to `md`
  - `motion.duration_normal` maps to `duration-normal`

## Polish-Oriented Tokens

For `0.1.4`, the theme surface is broad enough to support more than dashboards:

- `colors.*` for brand identity and semantics
- `surfaces.*` for softer backgrounds and overlay layers
- `shadows.*` for depth and premium card treatments
- `motion.*` for transitions and stagger timing

That makes it easier to style:

- dashboards
- pipeline command centers
- chatbot surfaces
- landing pages
- internal launch or product sites

## Recommendation

For teams, keep one shared branding YAML per product and let apps override only the few values they need locally. That gives you consistent portals without forcing every app author to hand-roll theme tokens.
