# Troubleshooting

This page collects the most common problems users hit while installing, running, publishing, and deploying BrickflowUI.

## I only see "Connecting to runtime..."

This means the HTML shell loaded, but the app did not finish its runtime connection.

Common causes:

- the frontend bundle was not present in the installed package
- the WebSocket route did not connect
- the browser is using a stale cached asset bundle
- the app process crashed before sending the first UI payload

## The page is blank in Databricks Apps

Recommended fixes:

- use `brickflowui>=0.1.3`
- hard refresh the page
- keep `app.yaml` minimal
- avoid relying on third-party frontend assets

## `pip install brickflowui` does not work

Try one of these:

```bash
pip install brickflowui
```

or:

```bash
pip install "brickflowui @ git+https://github.com/AjayAJ2000/brickflowUI.git@v0.1.3"
```

## I changed frontend code, but my package still behaves the same

You need to rebuild the frontend bundle before packaging.

```bash
cd frontend
npm install
npm run build
cd ..
python -m build
```

## `python -m build` fails around frontend assets

Before publishing, always verify the wheel contains:

- `brickflowui/frontend/dist/index.html`
- `brickflowui/frontend/dist/assets/...`
