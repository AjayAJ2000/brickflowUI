# API Reference

Use this page when you already understand the overall framework shape and want the current public surface in one place.

Pair this page with:

- [Quick Start](./GETTING_STARTED.md)
- [Examples](./EXAMPLES.md)
- [How It Works](./HOW_IT_WORKS.md)
- [Polish Guide](./POLISH_GUIDE.md)

## Core

### `db.App(...)`

Main application object.

Important parameters:

- `title`
- `theme`
- `theme_color`
- `logo`
- `favicon`
- `auth_mode`
- `auth_provider`
- `cors_origins`
- `trusted_hosts`
- `websocket_origins`

Methods:

- `@app.page(path, title=..., icon=..., access=..., roles=...)`
- `@app.route(path, methods=[...], access=..., roles=...)`
- `app.mount(component)`
- `app.run(host=None, port=None, reload=False)`

## State Hooks

- `db.use_state(initial)`
- `db.use_effect(fn, deps=None)`
- `db.use_memo(fn, deps=[...])`
- `db.use_context(key, default=None)`
- `db.set_context(key, value)`

## Auth Helpers

- `db.current_principal()`
- `db.current_user()`
- `db.current_app_identity()`
- `db.is_authenticated()`
- `db.require_auth()`
- `db.require_role(role)`
- `db.Principal(...)`
- `db.HeaderAuthProvider()`
- `db.StaticAuthProvider(principal)`

## Layout Components

- `db.Column`
- `db.Row`
- `db.Grid`
- `db.Card`
- `db.Divider`
- `db.Spacer`

Useful additive props:

- `Card(..., elevated=True, animated=True, animation="fade-up", animation_delay=0.1)`
- `Button(..., animated=True, animation="pulse")`

## Content Components

- `db.Text`
- `db.Code`
- `db.Badge`
- `db.Alert`
- `db.Stat`
- `db.Progress`
- `db.Spinner`
- `db.EmptyState`
- `db.Toast`
- `db.Timeline`
- `db.SparklineStat`

Useful additive props:

- `Stat(..., animated=True)`
- `Toast(..., visible=True)`

## Input Components

- `db.Button`
- `db.Input`
- `db.Select`
- `db.Checkbox`
- `db.Toggle`
- `db.Slider`
- `db.DateRangePicker`
- `db.MultiSelect`
- `db.Form`

Notes:

- `Input(..., loading=True)` and `Select(..., loading=True)` show inline loading affordances
- `DateRangePicker` emits `{"start": "...", "end": "..."}` to its `on_change`
- `MultiSelect` emits `list[str]` to its `on_change`
- `Form` preserves repeated field names as arrays when posting JSON

## Navigation And Surface Components

- `db.Sidebar`
- `db.NavItem`
- `db.Breadcrumbs`
- `db.Tabs`
- `db.TabItem`
- `db.Modal`
- `db.Drawer`
- `db.Accordion`
- `db.AccordionItem`

## Data Components

- `db.Table`

Useful additive props:

- `Table(..., loading=True)`
- `Table(..., empty_message="No rows yet")`
- `Table(..., exportable=True)`
- `Table(..., on_row_click=handler)`

## Chart Components

- `db.Plot`
- `db.AreaChart`
- `db.BarChart`
- `db.LineChart`
- `db.DonutChart`

Useful additive props:

- `loading`
- `empty_message`
- `on_click`
- `colors`

Example:

```python
db.BarChart(
    data=rows,
    x_key="week",
    y_keys=["runs", "failures"],
    title="Pipeline trend",
    loading=is_loading,
    empty_message="No pipeline data available",
    on_click=handle_bar_click,
)
```

## Theme Surface

Supported theme sections:

- `branding`
- `colors`
- `surfaces`
- `typography`
- `spacing`
- `borders`
- `shadows`
- `motion`

Useful aliases:

- `background -> bg`
- `primary_hover -> primary-hover`
- `text_muted -> text-muted`
- `font_family -> sans`
- `base_size -> base-size`
- `surfaces.background -> canvas`
- `surfaces.surface -> muted`
- `shadows.medium -> md`
- `motion.duration_normal -> duration-normal`

## Databricks Helpers

### `brickflowui.databricks.sql`

- `query(sql, params=None)`
- `query_to_records(sql, params=None)`
- `execute(sql, params=None)`
- `transaction()`

### `brickflowui.databricks.uc`

- `list_catalogs()`
- `list_schemas(catalog)`
- `list_tables(catalog, schema)`
- `table_schema(catalog, schema, table)`
- `get_table(catalog, schema, table, limit=100)`
