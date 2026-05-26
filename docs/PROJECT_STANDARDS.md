# Project Standards

BrickflowUI is being shaped as a product-grade open-source framework, not just a code drop. This page explains the standards the repository is expected to follow and which parts are enforced in code versus GitHub repository settings.

## What Is Enforced In The Repository

The repository already carries these source-controlled standards:

- `MIT` license
- contributor guidance in `CONTRIBUTING.md`
- community expectations in `CODE_OF_CONDUCT.md`
- support guidance in `SUPPORT.md`
- vulnerability reporting guidance in `SECURITY.md`
- issue templates and pull request template under `.github`
- ownership metadata in `.github/CODEOWNERS`
- CI, docs deployment, package publishing, and security audit workflows
- Dependabot configuration with grouped dependency updates
- generated component reference drift checks in CI
- strict documentation build validation

## What Must Still Be Set In GitHub Settings

These standards cannot be guaranteed from source code alone. They should be configured in the GitHub repository settings:

1. Protect `dev`, `test`, and `main` according to their role.
2. Require pull requests before merging into `test` and `main`.
3. Require status checks to pass before merging.
4. Require up-to-date branches before merge.
5. Restrict force pushes and branch deletion on protected branches.
6. Enable Dependabot alerts and Dependabot security updates.
7. Enable secret scanning and push protection, if available on your plan.
8. Enable private vulnerability reporting.
9. Configure PyPI and Pages environments with approval rules if your release process needs them.

## Recommended Required Checks

For `main`, the most important required checks are:

- CI
- Security
- Deploy Docs, if docs are part of the release contract

If you later split CI into smaller workflows, require the stable, release-relevant ones rather than every experiment.

## Dependency Update Policy

Dependency PRs should not be merged just because they are available. The recommended rule is:

- merge only when CI passes
- merge the latest PR for a dependency line
- close stale duplicate PRs
- prefer grouped updates where possible
- avoid letting dozens of dormant dependency PRs accumulate

For BrickflowUI specifically, GitHub Actions updates are usually low risk, while frontend runtime upgrades such as `react`, `vite`, `recharts`, `plotly`, and `typescript` should be validated carefully because they can affect the shipped UI bundle.

## Documentation Standard

For this project, documentation is part of the product surface. A public change is not considered complete unless:

- the behavior is documented
- the examples are updated
- the component reference is accurate
- the docs build passes cleanly

This is especially important for:

- component props
- loading behavior
- branding and theming
- Databricks deployment behavior
- new charts, media, navigation, and auth patterns

## Release Standard

For a publishable release:

1. Source version, package version, and docs version references should agree.
2. Frontend `dist` assets should match the current frontend source.
3. Tests, docs build, frontend build, and package build should pass.
4. PyPI artifacts should be checked with `twine check`.
5. Old build artifacts should not be uploaded again.

## Security Standard

Security expectations for BrickflowUI:

- no secrets or tokens committed to the repo
- no example with unsafe default auth patterns presented as production-ready
- CSP-safe frontend behavior for Databricks-style restricted environments
- dependency scanning and timely update handling
- documented private reporting path for vulnerabilities

## Product Readiness Mindset

To pitch this as a serious product, the repo should communicate:

- the framework is maintained deliberately
- releases are test-backed
- docs are trustworthy
- vulnerabilities are handled responsibly
- contribution and support paths are clear

That confidence comes from both code quality and repository discipline. This page exists to make that standard explicit.
