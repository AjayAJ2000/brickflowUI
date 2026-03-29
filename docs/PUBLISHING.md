# Publishing Guide

This project is set up so it can be published to GitHub and PyPI as `bricksflowui`.

## Package identity

- PyPI package: `bricksflowui`
- standard import path: `brickflowui`
- compatibility import path: `bricksflowui`
- CLI commands:
  - `brickflowui`
  - `bricksflowui`

## Recommended release checklist

1. Run tests

```bash
python -m pytest -q
```

2. If frontend source changed, rebuild assets

```bash
cd frontend
npm install
npm run build
cd ..
```

3. Build package artifacts

```bash
python -m build
```

4. Validate artifacts

```bash
python -m twine check dist/*
```

5. Upload to PyPI

```bash
python -m twine upload dist/*
```

## Post-publish smoke test

Users should be able to run:

```bash
pip install bricksflowui
```

Then:

```python
import brickflowui as db
```

## Packaging notes

- bundled frontend assets are included in wheel and sdist builds
- both `brickflowui` and `bricksflowui` packages are included
- docs and examples are included in the source distribution
