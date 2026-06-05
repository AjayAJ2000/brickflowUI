# Vibe Coding Skills

BrickflowUI works especially well with modern AI coding tools when the assistant is given a clear product shape and a few framework-specific guardrails.

This page collects the repo-local skill files we ship for that purpose.

## Why this matters

Generic "build me a dashboard" prompts often produce one of two bad outcomes:

- notebook-style pages with weak product structure
- generic frontend advice that ignores BrickflowUI's Python-first runtime

The skills in `skills/` keep the assistant closer to the framework's real strengths: data and AI portals, internal tools, branded shells, smoother controls, and Databricks-aware delivery.

## Included skills

| Skill | Path | Best for |
|---|---|---|
| BrickflowUI App Starter | `skills/brickflowui-app-starter/SKILL.md` | Starting new apps from the right example and keeping structure clean |
| BrickflowUI Data + AI Portal | `skills/brickflowui-data-ai-portal/SKILL.md` | Dashboards, copilots, pipeline command centers, and analytics workspaces |
| BrickflowUI Polish + QA | `skills/brickflowui-polish-and-qa/SKILL.md` | Responsiveness, loading, spacing, interaction quality, and release polish |
| BrickflowUI Databricks Delivery | `skills/brickflowui-databricks-delivery/SKILL.md` | Packaging, deployment, managed-platform handoff, and enterprise delivery review |

## Recommended workflow

1. Pick the closest real example from `examples/`.
2. Start with `skills/brickflowui-app-starter/SKILL.md`.
3. Move to the domain skill that fits the app shape.
4. Finish with `skills/brickflowui-polish-and-qa/SKILL.md`.
5. Use `skills/brickflowui-databricks-delivery/SKILL.md` before shipping or demoing to a platform team.

## Example prompts

### Build a data platform portal

```text
Use skills/brickflowui-data-ai-portal/SKILL.md and adapt examples/data_pipeline_command_center/app.py into a multi-page portal for data and AI teams. Keep the shell product-grade, add KPI cards, a pipeline graph, cost view, and an operations table.
```

### Start from the best baseline

```text
Use skills/brickflowui-app-starter/SKILL.md and tell me which existing example is the best baseline for a secure internal AI operations workspace. Then implement the first working page.
```

### Polish before demo day

```text
Use skills/brickflowui-polish-and-qa/SKILL.md and tighten this app for a buyer demo: smooth inputs, loading states, better spacing, mobile fixes, and more product-grade empty states.
```

### Prepare for Databricks

```text
Use skills/brickflowui-databricks-delivery/SKILL.md and make this app deployment-ready for Databricks Apps with a mock-data fallback and packaging checks.
```

## Best practice

Whenever possible, ask the assistant to **adapt a real example** instead of generating a new app from scratch. That keeps the output closer to the framework's proven patterns and lowers the chance of drifting into a generic web-app shape that BrickflowUI does not need.
