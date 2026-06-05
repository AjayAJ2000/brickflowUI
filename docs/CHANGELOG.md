# Changelog

This page tracks the highest-signal changes for evaluators and adopters. It is not meant to replace commit history. It is meant to explain what changed, why it matters, and what to recheck when you upgrade.

## 0.1.12

Focus: framework hardening, stronger product surfaces, enterprise-facing docs, and broader example coverage.

Highlights:

- broader dashboard and workflow surface including pipeline, chat, kanban, status, and media patterns
- stronger loading, theming, and branded runtime behavior
- responsive shell improvements and richer example apps
- auth-aware docs and deployment guidance
- landing page, docs portal, and reference content expanded to better support evaluation

Upgrade notes:

- review your theme config if you depend on older dark-mode assumptions
- prefer the latest examples when adopting loading, media, and preset-driven theming

## 0.1.11

Focus: responsiveness, polish, and reliability in day-to-day builder flows.

Highlights:

- smoother typing and local-first input behavior
- stronger loading-state handling across interactive components
- improved shell behavior for mobile and denser layouts
- more polished examples and better scaffolding experience

Upgrade notes:

- if you built custom workarounds for input lag, revisit them against the current runtime
- retest mobile layout behavior in your main apps

## 0.1.10

Focus: stabilization and scalability-oriented runtime improvements.

Highlights:

- deferred frontend tree updates and smoother rerender handling
- better guidance around performance and local testing
- stronger docs on runtime behavior

## 0.1.9 and Earlier

The project moved through several rapid polish and capability passes in the `0.1.x` line. If you are upgrading from an older `0.1.x` release, use:

- [Migration Guide](./MIGRATION_GUIDE.md)
- [Examples](./EXAMPLES.md)
- [API Reference](./API_REFERENCE.md)

## Release Discipline Going Forward

Every user-visible library change should update:

- package version
- docs references
- example requirements
- scaffolded template requirements
- release-facing upgrade guidance
