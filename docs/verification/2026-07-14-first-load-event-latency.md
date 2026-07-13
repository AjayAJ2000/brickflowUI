# BrickflowUI First-Load And Event-Latency Optimization

Date: 2026-07-14
Branch: `codex/perf-first-load-event-latency`
Base: `codex/fix-patch-removal-order`

## Goal

Reduce work on the two paths users feel most directly:

- first page load through the SPA shell
- click/input/event dispatch through the WebSocket runtime

## Changes

- The packaged React `index.html` shell is now read, escaped, and injected once
  when the ASGI app is created. Individual page requests reuse the prepared
  shell instead of repeating disk IO and string replacement.
- WebSocket sessions now cache each event handler's call shape after the first
  event. Repeated clicks or input changes no longer rerun `inspect.signature()`
  for the same handler.

## Regression Coverage

- `test_spa_shell_is_prepared_once_per_asgi_app` proves repeated shell requests
  read the packaged frontend shell once per ASGI app instance.
- `test_event_handler_signature_is_cached_for_repeated_events` proves repeated
  events for the same handler perform one signature inspection while preserving
  event completion behavior.

## Verification

- Focused server performance tests: `2 passed`
- Server runtime suite: `35 passed`
- Full Python suite: `261 passed`

These are deterministic structural checks rather than noisy wall-clock
benchmarks. They prevent the optimized work from drifting back into the hot
paths.
