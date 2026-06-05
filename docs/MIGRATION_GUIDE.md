# Migration Guide

Use this page when you are upgrading an existing BrickflowUI app and want to know what to validate before calling the upgrade done.

## General Upgrade Checklist

After every upgrade:

1. retest your main navigation shell on desktop and mobile
2. retest all user inputs that sync state back to Python
3. verify loading behavior on the controls that trigger backend work
4. verify custom branding, logos, and loading assets
5. run your app against the current [Examples](./EXAMPLES.md) and [API Reference](./API_REFERENCE.md)

## Upgrading To 0.1.12

Recheck these areas:

- theme behavior
  - the framework now expects light-first defaults unless dark is explicitly configured
- loading identity
  - confirm your custom loading title, message, asset, and mode-specific configuration still render correctly
- media
  - retest `Image`, `Video`, and `Embed` behavior if you use local assets
- examples and scaffolds
  - prefer the newer examples as reference instead of older ad hoc experiments

## Upgrading To 0.1.11

Recheck these areas:

- input sync strategy
  - `Input` and related controls moved toward smoother local-first behavior
- loading controls
  - verify component-level loading states rather than relying only on page-level cues
- responsive layouts
  - retest sidebars, tabs, dense control bars, and modal flows on narrow widths

## If You Built Local Workarounds

If you previously added app-level workarounds for:

- typing lag
- dark-mode defaults
- custom loading screens
- mobile shell behavior

review whether the framework now covers that behavior directly. Removing old workarounds can simplify your app code after upgrade.

## What To Compare During Migration

The best reference set during upgrades is:

1. [API Reference](./API_REFERENCE.md)
2. [Examples](./EXAMPLES.md)
3. [Local Development](./LOCAL_DEVELOPMENT.md)
4. [Troubleshooting](./TROUBLESHOOTING.md)

## When To Pause An Upgrade

Pause and inspect more carefully if:

- a custom theme suddenly looks different
- your app depends on very dense interaction patterns
- you rely on secured routes or custom auth integration
- you serve local media or embeds in stricter environments

That does not necessarily mean the upgrade is unsafe. It means those are the highest-value regression zones to validate first.
