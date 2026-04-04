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
| Workspace Studio | `examples/workspace_studio/app.py` | Rich app structure with filters, tables, tabs, forms, modal flows, charts, and a dedicated themes page |

## Data Pipeline Command Center

Use this example when your goal is to connect a real Databricks ingestion or transformation pipeline to an operations dashboard.

- [app.py](/D:/Projects/brickflowUI/brickflowUI/examples/data_pipeline_command_center/app.py)
- [app.yaml](/D:/Projects/brickflowUI/brickflowUI/examples/data_pipeline_command_center/app.yaml)
- [requirements.txt](/D:/Projects/brickflowUI/brickflowUI/examples/data_pipeline_command_center/requirements.txt)

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

## Workspace Studio

The most complete example right now is:

- [app.py](/D:/Projects/brickflowUI/brickflowUI/examples/workspace_studio/app.py)
- [app.yaml](/D:/Projects/brickflowUI/brickflowUI/examples/workspace_studio/app.yaml)
- [requirements.txt](/D:/Projects/brickflowUI/brickflowUI/examples/workspace_studio/requirements.txt)

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
brickflowui>=0.1.3
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
- Choose `workspace_studio` if you want the broadest example of how the library fits together.
- Choose `data_pipeline_command_center` if your real goal is pipeline observability and operational dashboarding on Databricks.
