# Patch Removal Ordering Design

## Problem

When navigation renders a page with fewer children than the previous page, the
server currently emits removal patches in ascending child-index order. Applying
an early removal shifts every later child left, so a later patch can target an
index that no longer exists. The frontend correctly rejects that invalid patch
and reconnects with an error such as:

    Patch index 3 is outside the child list.

## Root Cause

The Python VDOM diff iterates to the maximum old/new child count from index zero
upward. Missing new children therefore produce paths such as [1], [2], [3],
[4]. Those paths are valid against the original tree but are not valid when
applied sequentially to the progressively shrinking tree.

## Chosen Design

Keep the incremental patch protocol and correct patch generation at its source:

1. Diff the child indexes shared by the old and new lists in ascending order.
2. When the new list is shorter, emit removal patches from the last old index
   down to the first removed index.
3. When the new list is longer, emit insertion patches from the first new index
   upward.
4. Preserve strict frontend patch validation and reconnect recovery. Invalid
   server messages must still fail closed rather than silently corrupting UI
   state.

This ordering makes every patch valid against the tree produced by the patches
before it. It also works recursively because each child diff applies the same
invariant to its own child list.

## Alternatives Rejected

- **Reorder patches in the browser:** this makes the client infer dependencies
  between arbitrary operations and can reorder legitimate replace/update work.
- **Send a full tree after every navigation:** safe but discards incremental
  rendering performance and hides protocol defects instead of fixing them.

## Data Flow

Navigation still marks the session dirty, the server renders the new page, and
the VDOM diff produces a patch list. Only surplus-child ordering changes. The
frontend continues to apply the list sequentially.

## Error Handling

No frontend guard is weakened. Negative, non-integer, missing-node, and
out-of-bounds paths remain protocol errors that close the socket and request a
fresh full tree.

## Test Strategy

Automated coverage will include:

- root lists shrinking from five children to one
- root lists shrinking completely to zero
- nested child lists shrinking
- mixed shared-child updates plus surplus removals
- list growth to confirm insertion order remains valid
- frontend application of the server-compatible descending removal sequence
- continued rejection of malformed and genuinely out-of-bounds patches
- WebSocket navigation between example pages with different tree sizes

After targeted tests pass, run the full Python and frontend suites, Ruff, mypy,
ESLint, the production frontend build, strict documentation build, and browser
navigation checks across multiple maintained examples.

## Scope

The fix is limited to patch ordering, regression tests, the generated frontend
bundle, and release-facing documentation if behavior changes are documented.
Unrelated runtime refactoring is out of scope.
