# Build Guide

## Fastest local setup

From the repo root:

```bash
pip install -e ".[dev]"
```

If you plan to work on the React frontend too:

```bash
cd frontend
npm install
npm run build
cd ..
```

## Run the test suite

```bash
python -m pytest -q
```

## Run a demo app

Auth portal:

```bash
cd examples/auth_portal
python app.py
```

Operations + finance portal:

```bash
cd examples/operations_finance_portal
python app.py
```

By default the server uses `http://127.0.0.1:8050`. To use another port:

```bash
# PowerShell
$env:DATABRICKS_APP_PORT=8061
python app.py
```

## Build a publishable package

Install the release tools once:

```bash
pip install build twine
```

Then from the repo root:

```bash
python -m build
python -m twine check dist/*
```

If the checks pass, upload to PyPI:

```bash
python -m twine upload dist/*
```

## Build the documentation site locally

Install docs tooling:

```bash
pip install -e ".[docs]"
```

Run the docs server:

```bash
mkdocs serve
```

Open:

```text
http://127.0.0.1:8000
```

Build the static docs site:

```bash
mkdocs build
```

## What needs rebuilding?

- Python-only changes: reinstall with `pip install -e ".[dev]"` if needed, then run tests.
- Frontend source changes under `frontend/src`: run `npm run build` so `brickflowui/frontend/dist` is updated before publishing.
- Docs, examples, and tests: no special build step required.
