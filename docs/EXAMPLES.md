# Examples

BrickflowUI ships with a few examples that cover different levels of complexity.

Use this page when you want to skip the docs theory and start from something runnable.

## Recommended starting points

| Example | Path | Best for |
|---|---|---|
| Counter | `examples/counter/app.py` | Fastest possible sanity check |
| Auth Portal | `examples/auth_portal/app.py` | Login, access control, protected routes |
| Operations + Finance Portal | `examples/operations_finance_portal/app.py` | Executive dashboard with a traditional top nav |
| Data Pipeline Command Center | `examples/data_pipeline_command_center/app.py` | Industry-style data engineering monitoring with filters, SLA controls, cost, freshness, and Databricks SQL handoff |
| Pipeline Observability 0.1.5 | `examples/pipeline_observability_015/app.py` | New 0.1.5 showcase with pipeline graph, chatbot UI, heatmap, treemap, funnel, radar, gauge, kanban, and table export |
| Chatbot Workspace | `examples/chatbot_workspace/app.py` | Assistant-style UI with drawers, toast, timelines, and multi-value inputs |
| Landing Site | `examples/landing_site/app.py` | Product-style landing page and launch-site composition |
| Workspace Studio | `examples/workspace_studio/app.py` | Rich app structure with filters, tables, tabs, forms, modal flows, charts, and a dedicated themes page |

## Data Pipeline Command Center

Use this example when your goal is to connect a real Databricks ingestion or transformation pipeline to an operations dashboard.

- `examples/data_pipeline_command_center/app.py`
- `examples/data_pipeline_command_center/app.yaml`
- `examples/data_pipeline_command_center/requirements.txt`

It demonstrates:

- multiple live controls on one dashboard
- source switching between mock data and Databricks SQL
- top navigation across executive, health, cost, and data model views
- KPI cards for throughput, freshness, cost, and reliability
- charts for SLA trend, incident mix, and cost concentration
- guardrail controls like minimum success-rate threshold and critical-only filtering
- a practical SQL shape for your pipeline metrics table

This is a good starting point for:

- lakehouse ingestion monitoring
- bronze/silver/gold pipeline visibility
- engineering + analytics stakeholder review dashboards
- free-edition Databricks prototypes that later grow into team dashboards

## Pipeline Observability 0.1.5

Use this example when you want to test the newest visual toolkit and confirm user inputs drive real state changes.

- `examples/pipeline_observability_015/app.py`
- `examples/pipeline_observability_015/app.yaml`
- `examples/pipeline_observability_015/requirements.txt`

It demonstrates:

- `PipelineGraph` with node click drilldowns
- `ChatMessage` and `ChatInput` for a copilot-style dashboard assistant
- `StatusStrip`, `Hero`, and `SectionHeader` for polished dashboard composition
- `ComposedChart`, `ScatterChart`, `GaugeChart`, `RadarChart`, `Heatmap`, `FunnelChart`, and `TreeMap`
- `KanbanBoard` for operational triage
- multiple controls driving charts, tables, graph, and chat output
- `Table(exportable=True)` for CSV export

Run it locally:

```bash
cd examples/pipeline_observability_015
python app.py
```

## Workspace Studio

The most complete example right now is:

- `examples/workspace_studio/app.py`
- `examples/workspace_studio/app.yaml`
- `examples/workspace_studio/requirements.txt`

It demonstrates:

- traditional top navigation instead of a sidebar-only layout
- reusable KPI cards
- `use_state` for page-level interactivity
- filters with `Input`, `Select`, `Checkbox`, `Toggle`, and `Slider`
- `AreaChart`, `BarChart`, `LineChart`, and `DonutChart`
- multi-section views switched with state
- `Tabs` for sub-workflows inside a page
- `Table` for operational and release data
- `Form` posting to a custom `@app.route(...)`
- `Modal` for secondary flows without leaving the current page
- a dedicated `Themes` section that shows token mapping and theme-driven UI behavior
- inline theming for Databricks-friendly deployment

## Chatbot Workspace

Use this example when you want to prove BrickflowUI can power assistant-style interfaces as well as dashboards.

- `examples/chatbot_workspace/app.py`
- `examples/chatbot_workspace/app.yaml`
- `examples/chatbot_workspace/requirements.txt`

It demonstrates:

- conversation layouts built with standard cards and rows
- `DateRangePicker` for structured prompt scope
- `MultiSelect` for answer mode selection
- `Toast` for interaction feedback
- `Drawer` for sources, trace, or tool output
- `Timeline` for execution trace storytelling
- `Accordion` for prompt guidance and tool context

## Landing Site

Use this example when you want a product or launch-style page rather than a traditional dashboard.

- `examples/landing_site/app.py`
- `examples/landing_site/app.yaml`
- `examples/landing_site/requirements.txt`

It demonstrates:

- hero-card composition
- feature grids with elevated surfaces
- FAQ via `Accordion`
- roadmap storytelling via `Timeline`
- launch feedback via `Toast`
- supporting narrative in a `Drawer`

## Run Workspace Studio locally

```bash
cd examples/workspace_studio
python app.py
```

Open:

```text
http://127.0.0.1:8050
```

## Run Workspace Studio in Databricks Apps

Put these three files in your Databricks App project:

- `app.py`
- `requirements.txt`
- `app.yaml`

`requirements.txt`:

```text
brickflowui>=0.1.4
```

For the 0.1.5 visualization showcase, use:

```text
brickflowui>=0.1.5
```

`app.yaml`:

```yaml
command:
  - python
  - app.py

env:
  - name: BRICKFLOWUI_ENV
    value: production
```

## How to use an example as a template

The most effective pattern is:

1. Copy the example closest to your real use case.
2. Replace the mock data lists with your Databricks SQL or Unity Catalog data.
3. Keep the page structure and component composition.
4. Move repeated UI patterns into helper functions.
5. Add auth and route protection once the page flow is stable.

## Which example should I choose?

- Choose `counter` if you just want to verify installation and runtime.
- Choose `auth_portal` if your main concern is access control and protected pages.
- Choose `operations_finance_portal` if you want a polished dashboard-style shell quickly.
- Choose `chatbot_workspace` if you want an assistant-style interface with real UI controls around it.
- Choose `landing_site` if you want a cleaner marketing or internal product-launch layout.
- Choose `workspace_studio` if you want the broadest example of how the library fits together.
- Choose `data_pipeline_command_center` if your real goal is pipeline observability and operational dashboarding on Databricks.
- Choose `pipeline_observability_015` if you want the newest chart, pipeline graph, kanban, and chatbot UI primitives.
