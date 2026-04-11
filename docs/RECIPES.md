# Recipes

Use these patterns when you know the kind of product you want to build and want a practical starting point.

## Executive dashboard

Use:

- `Grid`
- `Card`
- `Stat`
- `Table`
- `AreaChart`
- `BarChart`
- `DateRangePicker`
- `MultiSelect`
- `Drawer`

Good examples:

- [Data Pipeline Command Center](./EXAMPLES.md)
- [Workspace Studio](./EXAMPLES.md)

## Chatbot workspace

Use:

- `Input`
- `Button`
- `Card`
- `Toast`
- `Drawer`
- `Timeline`
- `Accordion`
- `Breadcrumbs`

Recommended pattern:

1. Keep the conversation in `use_state`.
2. Use `Card` blocks for user and assistant messages.
3. Use a `Drawer` for traces, sources, or tool results.
4. Use `Toast` for completion or send-state feedback.

## Landing page or internal product site

Use:

- `Card`
- `Grid`
- `SparklineStat`
- `Accordion`
- `Timeline`
- `Button`
- `Badge`

Recommended pattern:

1. Lead with a hero `Card`.
2. Use a 3-column feature grid.
3. Add a roadmap `Timeline`.
4. Use `Accordion` for FAQ.
5. Keep the theme calm and whitespace-heavy.

## Pipeline command center

Use:

- `Stat`
- `AreaChart`
- `BarChart`
- `DonutChart`
- `Table`
- `Breadcrumbs`
- `DateRangePicker`
- `MultiSelect`
- `Drawer`

Recommended pattern:

1. Start in mock mode.
2. Keep every metric visible as plain values and charts.
3. Add drilldown with row click or chart click.
4. Use `empty_message` and `loading` aggressively so the app stays honest while data loads.
