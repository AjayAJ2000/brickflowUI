# Branch Strategy

BrickflowUI now follows a staged delivery flow:

- `dev` for active integration work
- `test` for release-candidate validation
- `main` for production-ready code and public release

This model is better aligned with product-style development than pushing every change straight to `main`.

## Intended Flow

1. Land working changes in `dev`.
2. Open a pull request from `dev` to `test`.
3. Validate the candidate in `test`.
4. Open a pull request from `test` to `main`.
5. Release from `main` only after validation is complete.

## What Each Branch Means

### `dev`

Use `dev` for:

- active feature work
- reliability fixes
- docs updates that are still evolving
- dependency updates that still need validation

CI, security checks, and CodeQL should run here so issues are caught early.

### `test`

Use `test` for:

- integrated release candidates
- validation across examples and docs
- final QA before public release

This branch should feel stable enough for broader internal review.

### `main`

Use `main` for:

- production-ready code
- GitHub Pages docs deployment
- tagged releases
- PyPI publishing

Keep `main` protected and conservative.

## Workflow Behavior

The repository workflows are set up so that:

- `CI` runs on pushes and pull requests for `dev`, `test`, and `main`
- `Security` runs on pushes and pull requests for `dev`, `test`, and `main`
- `CodeQL` runs on pushes and pull requests for `dev`, `test`, and `main`
- docs are deployed only from `main`

That keeps earlier branches validated without accidentally publishing unfinished work.

## Recommended GitHub Branch Protection

Recommended protections:

### `dev`

- require pull requests for merge if your team wants stricter review
- require `CI`
- require `Security`

### `test`

- require pull requests before merge
- require `CI`
- require `Security`
- require `CodeQL`

### `main`

- require pull requests before merge
- require approval
- require `CI`
- require `Security`
- require `CodeQL`
- require `Deploy Docs`
- block force pushes
- block deletions

## Release Discipline

Only publish from `main`.

That means:

- docs site should represent `main`
- PyPI releases should come from `main`
- public tags should be created from `main`

This avoids confusion between what is experimental and what is actually supported.

## Practical Local Flow

If your current worktree contains the changes you want to ship next:

```bash
git switch -c dev
git add -A
git commit -m "..."
git push -u origin dev
```

Then open:

1. `dev -> test`
2. after validation, `test -> main`

If `dev` and `test` already exist remotely, use:

```bash
git fetch origin
git switch dev
```

or:

```bash
git switch -c dev --track origin/dev
```

depending on whether the branch already exists locally.
