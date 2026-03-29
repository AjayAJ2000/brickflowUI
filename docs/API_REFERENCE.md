# API Reference

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

## Content Components

- `db.Text`
- `db.Code`
- `db.Badge`
- `db.Alert`
- `db.Stat`
- `db.Progress`
- `db.Spinner`

## Input Components

- `db.Button`
- `db.Input`
- `db.Select`
- `db.Checkbox`
- `db.Toggle`
- `db.Slider`
- `db.Form`

## Navigation Components

- `db.Sidebar`
- `db.NavItem`
- `db.Tabs`
- `db.TabItem`
- `db.Modal`

## Data Components

- `db.Table`

## Chart Components

- `db.Plot`
- `db.AreaChart`
- `db.BarChart`
- `db.LineChart`
- `db.DonutChart`

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
