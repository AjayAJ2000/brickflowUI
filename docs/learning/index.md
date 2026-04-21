# Learn BrickflowUI

This learning guide is a practical curriculum for becoming productive with BrickflowUI.

It is not an API reference. It is a guided path that teaches the mental model, the common patterns, the sharp edges, and the way experienced users build real apps with the library.

The guide assumes you already know Python. It does not assume you know React, frontend build systems, WebSockets, Databricks Apps, or dashboard design.

## What You Will Learn

By the end, you should be able to build:

- a simple interactive app
- a multi-section dashboard
- a filtered table and chart experience
- a pipeline observability portal
- a chatbot-style assistant UI
- a polished landing page
- a Databricks-ready app package
- a full capstone app that combines all of the above

## Recommended Path

Follow the chapters in order the first time:

1. [What Is BrickflowUI](./01-what-is-brickflowui.md)
2. [Install And Run](./02-install-and-run.md)
3. [Your First App](./03-your-first-app.md)
4. [Mental Model](./04-mental-model.md)
5. [Layout Skills](./05-layout-skills.md)
6. [Components And Composition](./06-components-and-composition.md)
7. [State And Events](./07-state-and-events.md)
8. [Inputs And User Actions](./08-inputs-and-user-actions.md)
9. [Forms And API Routes](./09-forms-and-api-routes.md)
10. [Tables And Data Display](./10-tables-and-data-display.md)
11. [Charts And Visualizations](./11-charts-and-visualizations.md)
12. [Pipeline Dashboards](./12-pipeline-dashboards.md)
13. [Chatbot And Assistant UI](./13-chatbot-and-assistant-ui.md)
14. [Theming And Branding](./14-theming-and-branding.md)
15. [Navigation And App Structure](./15-navigation-and-app-structure.md)
16. [Databricks Apps Deployment](./16-databricks-apps-deployment.md)
17. [Debugging And Reliability](./17-debugging-and-reliability.md)
18. [Production Checklist](./18-production-checklist.md)
19. [Capstone Project](./19-capstone-project.md)
20. [Glossary](./glossary.md)

## How To Use This Guide

Each chapter has:

- a learning goal
- a practical explanation
- copy-paste code
- common mistakes
- exercises
- a checkpoint

Do not rush the exercises. BrickflowUI skill comes from understanding how state, events, data, layout, and visuals fit together.

## The Big Idea

BrickflowUI lets you describe UI in Python:

```python
return db.Column(
    [
        db.Text("Pipeline Health", variant="h1"),
        db.Button("Refresh", on_click=refresh),
    ]
)
```

The framework renders that Python component tree through a bundled frontend, listens for user events, calls your Python handlers, and sends UI updates back to the browser.

You write Python. BrickflowUI handles the browser runtime.
