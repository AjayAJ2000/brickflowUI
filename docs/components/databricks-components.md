# Databricks Components

These components and helpers focus on the Databricks workflow around SQL warehouses, catalogs, and job operations.

## `CatalogBrowser`

Use `CatalogBrowser` when you want a simple UI for exploring catalog, schema, and table choices from the app.

## `WarehouseSelector`

Use `WarehouseSelector` when the user should explicitly choose which SQL warehouse is active for a query or dashboard.

## `JobTrigger`

Use `JobTrigger` for simple operator actions such as running a job or pipeline from the UI.

## Related Python helpers

These live under `brickflowui.databricks`:

- `sql.query(...)`
- `sql.query_to_records(...)`
- `sql.execute(...)`
- `uc.list_catalogs()`
- `uc.list_schemas(...)`
- `uc.list_tables(...)`
- `uc.get_table(...)`

## Practical pattern

```python
rows = sql.query_to_records(
    \"\"\"
    select pipeline_name, success_rate, freshness_minutes
    from ops.pipeline_health
    order by updated_at desc
    \"\"\"
)

db.Column(
    [
        db.SectionHeader("Warehouse View"),
        db.Table(data=rows, exportable=True),
    ]
)
```

## Deployment reminder

For Databricks Apps, always verify:

- `requirements.txt` installs the intended `brickflowui` build
- `app.yaml` runs Python directly
- the installed package contains `brickflowui/frontend/dist`
