# Hero

## What It Does

Creates a premium top-of-page introduction for dashboards, portals, or landing pages.

## Signature

```python
db.Hero(title: 'str', subtitle: 'Optional[str]' = None, eyebrow: 'Optional[str]' = None, tagline: 'Optional[str]' = None, image: 'Optional[str]' = None, image_alt: 'str' = '', actions: 'Optional[List[VNode]]' = None, badges: 'Optional[List[VNode]]' = None, visual: 'Optional[VNode]' = None, animated: 'bool' = True, animation: 'Optional[str]' = 'fade-up', animation_delay: 'Optional[float]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `title` | `str` | `required` | |
| `subtitle` | `Optional[str]` | `None` | |
| `eyebrow` | `Optional[str]` | `None` | |
| `tagline` | `Optional[str]` | `None` | |
| `image` | `Optional[str]` | `None` | |
| `image_alt` | `str` | `''` | |
| `actions` | `Optional[List[VNode]]` | `None` | |
| `badges` | `Optional[List[VNode]]` | `None` | |
| `visual` | `Optional[VNode]` | `None` | |
| `animated` | `bool` | `True` | |
| `animation` | `Optional[str]` | `'fade-up'` | |
| `animation_delay` | `Optional[float]` | `None` | |

## Example

```python
import brickflowui as db

node = db.Hero("Pipeline command center", subtitle="Observe jobs, freshness, and cost from one place.", tagline="Built with BrickflowUI", image="assets/logo.svg", actions=[db.Button("Refresh")], badges=[db.Badge("Live", color="green")])
```

## Integration Notes

- Hero is intentionally designed for product-level first impressions, so it works well at the top of dashboards, landing pages, and admin portals.
