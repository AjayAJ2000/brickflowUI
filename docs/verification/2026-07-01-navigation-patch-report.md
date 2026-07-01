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
