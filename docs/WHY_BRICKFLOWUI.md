# Why BrickflowUI

BrickflowUI exists for teams that are caught between two uncomfortable options:

- notebook-style Python UI tools that are fast to start but can feel constrained once the app needs real product surface area
- full custom frontend stacks that are flexible, but expensive for Python-heavy teams to own end to end

BrickflowUI is the middle path:

- Python-first authoring
- a real packaged frontend runtime
- stronger application shells
- better theming and branding control
- a clearer Databricks-friendly deployment story

## Who It Is For

BrickflowUI is a strong fit when your team is trying to build:

- internal analytics and operations portals
- data pipeline command centers
- secure internal tools with governed views
- copilots and assistant workspaces
- branded product-style launch pages and portal shells
- domain-specific portals in healthcare, finance, and enterprise SaaS

The common pattern is the same: the app needs to feel intentional, not improvised.

## What It Optimizes For

### Product-grade surfaces

You should be able to build:

- left-nav or top-nav application shells
- dense dashboards with charts, KPIs, status cells, and drilldowns
- role-aware pages and navigation
- chat and copilot interfaces
- media-rich pages with images, GIFs, videos, and embeds
- theme-aware light/dark experiences with branded loading states

### Python team ergonomics

The library is designed so Python teams can stay productive without splitting ownership too early:

- state is authored in Python
- page structure is authored in Python
- common UI patterns are already packaged
- the frontend runtime handles the visual layer and interaction plumbing

### Evaluator readability

This project is not only trying to be usable by builders. It also needs to be understandable to:

- platform teams
- security reviewers
- engineering managers
- architecture evaluators
- enterprise buyers

That is why documentation, examples, and deployment guidance are treated as part of the product.

## Where It Differs From Notebook UI Tools

BrickflowUI is not trying to replace every Python UI framework. It is intentionally biased toward teams who need more application shape.

| Area | BrickflowUI bias |
|---|---|
| Layout ambition | product-style portals and shells |
| Runtime story | packaged frontend runtime instead of simple page reruns |
| Deployment narrative | Databricks-friendly and enterprise-aware |
| Brand control | presets, tokens, loading identity, media |
| Evaluator support | architecture, operations, security, and example depth |

## Where It Still Needs To Keep Growing

BrickflowUI is promising, but the project is still in the `0.1.x` maturity phase.

Near-term priorities remain:

- smoother end-to-end interaction quality
- deeper auth and governance patterns
- stronger visual examples and screenshots
- broader performance and observability guidance
- continued hardening of examples and deployment flows

## Recommended Next Reads

1. [Quick Start](./GETTING_STARTED.md)
2. [Examples](./EXAMPLES.md)
3. [API Reference](./API_REFERENCE.md)
4. [Performance And Scalability](./PERFORMANCE.md)
5. [Auth And Security](./AUTH_AND_SECURITY.md)
