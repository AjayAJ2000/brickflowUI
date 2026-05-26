# Contributing to BrickflowUI

BrickflowUI is meant to feel dependable for app builders, so every contribution should improve either reliability, usability, documentation clarity, or platform coverage.

## Development Flow

1. Branch from `dev` for normal contribution work unless a maintainer says otherwise.
2. Make the smallest change that fully solves the problem.
3. Update docs and examples when public behavior changes.
4. Run the validation suite before opening a pull request.
5. Open pull requests toward `dev`, then promote `dev -> test -> main` through the staged release flow.

## Required Validation

```bash
python -m pytest -q
cd frontend
npm run build
cd ..
python -m mkdocs build --strict
python -m build
```

If one of these fails because of an environment-specific Windows permission issue, note that clearly in the pull request.

## Pull Request Expectations

- Explain the problem and the user impact.
- Describe the fix in product terms, not only code terms.
- Link updated docs or examples when the API surface changes.
- Keep generated frontend assets in sync with the frontend source.
- Avoid breaking changes unless they are planned and documented.

## Docs Are Part of the Product

When you change:

- a component signature
- state behavior
- loading behavior
- theming or branding behavior
- Databricks deployment behavior

you should update:

- the relevant component reference page
- any affected tutorials or examples
- root markdown files if installation or release guidance changed

## Release Discipline

- Bump the package version for each publishable update.
- Keep `pyproject.toml` and `brickflowui/version.py` aligned.
- Check built artifacts locally before publishing to PyPI.

## Security

- Do not commit secrets, tokens, workspace credentials, or customer data.
- Prefer minimal permissions in examples and workflows.
- If you find a security issue, follow the process in [SECURITY.md](./SECURITY.md) instead of opening a public issue with exploit details.
