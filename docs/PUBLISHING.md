# Publishing Guide

This project is set up so it can be published to GitHub and PyPI as `brickflowui`.

## Package identity

- PyPI package: `brickflowui`
- standard import path: `brickflowui`
- CLI command:
  - `brickflowui`

## Recommended release checklist

Use [Release Checklist](./RELEASE_CHECKLIST.md) as the authoritative end-to-end gate. The condensed publishing sequence is:

1. Install locked frontend dependencies and run frontend gates

```bash
cd frontend
npm ci
npm test -- --run
npm run lint
npm audit --audit-level=high
npm run build
cd ..
```

2. Run Python and documentation gates

```bash
python -m pytest -q -p no:cacheprovider
python scripts/generate_component_reference.py
git diff --exit-code -- docs/components/reference
python -m mkdocs build --strict
```

3. Build and inspect package artifacts

```bash
python -m build
python -m twine check dist/*
python -m zipfile -l dist/brickflowui-0.1.16-py3-none-any.whl
```

4. Publish through GitHub trusted publishing. Manual Twine upload is an emergency fallback only when a project-scoped PyPI token is available:

```bash
python -m twine upload dist/*
```

## Trusted Publishing with GitHub Actions

This repository includes a GitHub Actions workflow at:

`/.github/workflows/publish.yml`

When configuring a GitHub trusted publisher on PyPI, use:

- repository owner: your GitHub username or org
- repository name: your repository name
- workflow filename: `publish.yml`
- environment: `pypi`

The workflow is configured to:

- run tests
- build the package
- publish to PyPI with GitHub OIDC trusted publishing

It runs when a GitHub Release is published, and can also be started manually with `workflow_dispatch`.

For a manual workflow run, select the exact release branch or tag. Do not publish a version that is not committed and pushed.

## Post-publish smoke test

Users should be able to run:

```bash
python -m pip install --no-cache-dir brickflowui==0.1.16
```

Then:

```python
import brickflowui as db
assert db.__version__ == "0.1.16"
```

Finally verify the immutable version endpoint: `https://pypi.org/pypi/brickflowui/0.1.16/json`.

## Packaging notes

- bundled frontend assets are included in wheel and sdist builds
- the published distribution includes the `brickflowui` Python package
- docs and examples are included in the source distribution
