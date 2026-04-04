# FAQ

## What is the correct package name?

Use:

- PyPI package: `brickflowui`
- import: `import brickflowui as db`
- CLI: `brickflowui`

## How do I install directly from GitHub?

```bash
pip install "brickflowui @ git+https://github.com/AjayAJ2000/brickflowUI.git@v0.1.3"
```

## How do I put the GitHub version in `requirements.txt`?

```text
brickflowui @ git+https://github.com/AjayAJ2000/brickflowUI.git@v0.1.3
```

## How do I use it in Databricks Apps?

Use:

```yaml
command:
  - python
  - app.py
```

and:

```text
brickflowui>=0.1.3
```

## Does BrickflowUI depend on Nike's Brickflow?

No.

BrickflowUI is an independent project and is not affiliated with Nike's Brickflow workflow framework.
