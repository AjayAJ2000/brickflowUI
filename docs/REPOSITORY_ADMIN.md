# Repository Administration

This page is the maintainers' checklist for turning BrickflowUI into a stronger product-grade open-source repository on GitHub.

Some standards can be committed in the repo. Others live only in GitHub settings. This guide focuses on the settings side so the operational setup stays consistent with the codebase.

## Branch Model

BrickflowUI is expected to follow this staged flow:

- `dev` for active integration
- `test` for release validation
- `main` for production releases

Use GitHub settings to protect each branch according to its purpose instead of treating every branch the same.

See [Branch Strategy](./BRANCH_STRATEGY.md) for the operational flow.

## Branch Protection For `main`

Go to:

`Repository -> Settings -> Branches -> Add branch protection rule`

Recommended rule for `main`:

- Require a pull request before merging
- Require at least one approval
- Dismiss stale approvals when new commits are pushed
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Block force pushes
- Block deletions

Recommended required checks:

- `CI`
- `Security`
- `CodeQL`
- `Deploy Docs`

If a future workflow is experimental, do not make it required until it proves stable.

## Branch Protection For `test`

Recommended rule for `test`:

- Require a pull request before merging
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Block force pushes

Recommended required checks:

- `CI`
- `Security`
- `CodeQL`

## Branch Protection For `dev`

Recommended rule for `dev`:

- Require status checks to pass before merging if multiple people contribute actively
- Block force pushes unless your team has a very small controlled workflow

Recommended required checks:

- `CI`
- `Security`

## Security Features

Go to:

`Repository -> Settings -> Security`

Enable these if available on your GitHub plan:

- Dependabot alerts
- Dependabot security updates
- Secret scanning
- Push protection
- Private vulnerability reporting

These are important if the library is being pitched to firms that expect responsible supply-chain and secret-handling posture.

## GitHub Pages

Go to:

`Repository -> Settings -> Pages`

Set:

- Source: `GitHub Actions`

This keeps the deployed docs aligned with the committed MkDocs workflows instead of falling back to Jekyll-style branch publishing.

## Environments

For release confidence, create GitHub environments such as:

- `github-pages`
- `pypi`

Recommended controls:

- optional required reviewer for release workflows
- environment-scoped secrets only where absolutely needed
- no broad repository secrets unless unavoidable

## Dependabot Maintenance

Dependabot is useful, but an unmanaged queue of stale PRs creates noise.

Recommended rule:

- keep the latest PR for a dependency line
- close stale duplicates
- merge only after CI passes
- prefer grouped update PRs over many tiny ones

For BrickflowUI, grouped updates are already configured in `.github/dependabot.yml`.

## Open Pull Requests Triage Pattern

When you review dependency PRs:

1. Check whether a newer PR supersedes an older one.
2. Close the older duplicate PR.
3. Validate the newest one in CI.
4. Merge only if the change is low risk or clearly needed.

Low-risk examples:

- GitHub Actions patch/minor updates
- packaging/build tool fixes with passing CI

Higher-risk examples:

- React major upgrades
- charting library upgrades
- TypeScript major upgrades
- auth/security-sensitive dependency changes

## Release Readiness

Before publishing:

1. Confirm package version and docs references are aligned.
2. Confirm frontend `dist` matches source.
3. Confirm tests pass.
4. Confirm docs build passes.
5. Confirm package build passes.
6. Confirm `twine check` passes.

## Maintainer Habit Checklist

For each publishable update:

- keep the repo clean from generated junk and temp folders
- update docs alongside product behavior
- review dependency updates intentionally
- avoid merging broken or unreviewed generated asset drift
- leave a clear release trail through tags, notes, and version bumps

This keeps the repository credible both as an open-source project and as a product firms can evaluate seriously.
