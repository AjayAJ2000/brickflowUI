# BrickflowUI 0.1.14 Navigation Patch Verification

Date: 2026-07-01
Branch: `codex/fix-patch-removal-order`
Target: `main`
Version: `0.1.14`

## Confirmed Root Cause

The Python VDOM diff generated surplus-child removals in ascending order.
Applying an early removal shifted every later child left, so later paths could
become invalid. A five-child page changing to one child produced:

```text
[1], [2], [3], [4]
```

The frontend correctly rejected that stale sequence with
`Patch index 3 is outside the child list` and reconnected.

## Corrected Protocol Invariant

Shared children are diffed first. Surplus removals are emitted from the highest
index downward, while surplus insertions remain lowest-index first. Strict
frontend validation remains unchanged.

## Red-Green Evidence

Before the implementation change, the targeted Python and WebSocket run
reported five expected failures and 39 passes. Every failure showed ascending
removal paths where descending paths were required.

After the implementation change:

- Python VDOM and WebSocket navigation tests: `215 passed`
- frontend patch application tests: `9 passed`
- tested child-count transitions: every old/new pair from zero through twelve
- tested nesting: root lists and lists nested below a parent
- tested routing: large → compact → large → compact
- tested isolation: two simultaneous WebSocket sessions
- tested defensive behavior: the old ascending sequence still raises the exact
  protocol error instead of corrupting the client tree

## Registry Preflight

- `https://pypi.org/pypi/brickflowui/0.1.13/json`: HTTP 200
- `https://pypi.org/pypi/brickflowui/0.1.14/json`: HTTP 404 before release

This confirms `0.1.13` is immutable and `0.1.14` is the available patch
version for this fix.

## Full Automated Gates

- Python: `259 passed`
- frontend: `32 passed` across eight Vitest files
- Ruff: passed
- mypy: passed for 16 source files
- ESLint: passed
- npm audit: zero vulnerabilities
- Vite production build: passed with no committed-bundle drift
- component-reference regeneration: no content drift
- MkDocs strict build: passed

The first strict-docs rerun could not clean an older generated site directory
because Windows denied deletion of `404.html`. Building into a fresh ignored
site directory passed; this was an output-directory ACL issue, not a
documentation error.

## Maintained Example Matrix

A permanent runtime smoke test imports and serves these maintained examples,
opens `/`, connects to `/events`, receives a full serialized VDOM tree, and
verifies the payload is JSON-safe:

- Operations Finance Portal
- Weather Dashboard
- Component Studio
- Auth Portal
- Pipeline Observability 0.1.13 showcase

The example test file reported `7 passed`, including compilation and flagship
inventory checks.

## Browser Navigation

The Weather Dashboard was exercised live through the packaged React frontend:

- Current Weather → 7-Day Forecast
- Forecast → Current Weather → Forecast
- browser Back to Current Weather
- browser Forward to 7-Day Forecast
- protocol error banners: zero
- browser console errors: zero
- shell, JavaScript, CSS, vendor, and chart assets: HTTP 200

The Auth Portal was exercised signed out through Home → App Ops → Home with no
protocol error. Admin sign-in completed, redirected to `/admin`, and opened a
new authenticated WebSocket. The in-app browser inspection bridge timed out
while reading the large authenticated DOM and later the finance portal DOM.
Those inspection timeouts are recorded as harness limitations; the five-example
HTTP/WebSocket runtime smoke suite above provides deterministic coverage for
those applications.
