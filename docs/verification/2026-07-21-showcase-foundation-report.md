# Showcase Foundation Verification Report

## Verification status

```text
Status: LOCAL AUTOMATED AND BROWSER GATES PASS — LIVE DATABRICKS VALIDATION REQUIRED
Foundation commit: 397e02a829c9197688f8bae83b44e141764d1a57
Implementation commits tested: 9e443bd160e2115c7d03cd38e28beccd5be93378, a18722f15f0e98028bb176a6a3dbac4b36394698, f2f0ae1
Branch: codex/production-data-apps-02
Automated result: mandated local commands pass in the repaired working tree
Browser result: six examples and the flagship responsive/accessibility flow pass
External result: live Databricks Apps workspace validation was not available
```

This report covers the six retained examples and the flagship browser flow. Browser verification found local defects during the run; those defects were repaired with regression tests before the automated suite was rerun. No known reproducible local defect remains in this milestone's scope.

## Environment

| Item | Exact value |
| --- | --- |
| Verification date/time | 2026-07-22, Asia/Calcutta (UTC+05:30) |
| Operating system | Windows 11, `10.0.26200`, AMD64 |
| Python | CPython 3.13.1 |
| Node.js | 24.18.0 |
| npm | 11.16.0 |
| Git | 2.36.1.windows.1 |
| pytest | 8.4.2 |
| MkDocs | 1.6.1 |
| build | 1.4.2 |
| Twine | 6.2.0 |
| Vite | 7.3.6 |
| Vitest | 3.2.7 |
| ESLint | 8.57.1 |
| TypeScript | 5.9.3 |
| Browser harness | Codex in-app browser against locally served examples; engine version and User-Agent are not exposed by this runtime |

The friendly Windows edition probe was denied by local WMI permissions; `platform.platform()` and the OS version API both identified Windows build `10.0.26200`.

## Automated verification

| Command | Result and exact evidence |
| --- | --- |
| `python -m pytest -q -p no:cacheprovider` | Passed: **345 passed** in 5.43s on the final `0.1.16` commit-candidate run. |
| `python scripts/smoke_examples.py` | Passed: all **6 manifest examples** passed smoke checks. |
| `python scripts/generate_component_reference.py` | Passed with exit 0. |
| `git diff --exit-code -- docs/components/reference` | Passed: no generated reference drift. Git emitted Windows CRLF-to-LF checkout warnings only. |
| `python -m mkdocs build --strict -d .site_validation_showcase` | Passed in 3.98s. Existing pages outside `nav` were reported as informational notices. |
| `python -m build` | Passed: built `brickflowui-0.1.16.tar.gz` and `brickflowui-0.1.16-py3-none-any.whl`. |
| `python -m twine check dist/*` | Passed: **2/2 artifacts**. |
| `npm --prefix frontend test -- --run` | Passed on the latest frontend run: **43 tests across 11 files**. |
| `npm --prefix frontend run lint` | Passed with zero ESLint errors. |
| `npm --prefix frontend run typecheck` | Passed with zero TypeScript errors. |
| `npm --prefix frontend audit --audit-level=high` | Passed: **0 vulnerabilities**. |
| `npm --prefix frontend run build` | Passed with Vite 7.3.6: **2,196 modules transformed**. |
| `git diff --exit-code -- brickflowui/frontend/dist` | Pre-commit check passed with no unstaged dist drift. After follow-up implementation commit `a18722f15f0e98028bb176a6a3dbac4b36394698`, a fresh Vite build again transformed 2,196 modules and this command exited 0 against the commit. |
| `git diff --check` | Passed: no whitespace errors in unstaged changes. |

The final frontend entry bundle produced by the latest build is `index-BFhsc6B7.js` (797.38 kB, 161.58 kB gzip); the CSS entry is `index-B7sm3Upf.css` (62.27 kB, 10.69 kB gzip). The Plotly chunk remains 7,213.37 kB uncompressed and is not a new regression in this milestone.

### Execution constraints and observed failures

Failures encountered during verification were retained as evidence rather than hidden:

- The first exact pytest invocation reported `309 passed, 32 errors` because the restricted runner could not scan `C:\Users\ajays\AppData\Local\Temp\pytest-of-ajays`. The unchanged command passed outside that filesystem restriction.
- The first exact Python build could not create `build-env-*` under the Windows temp directory. The unchanged command passed with normal temp-directory access.
- The first exact frontend test invocation stopped before test collection because the sandbox denied esbuild child-process creation with `spawn EPERM`. The unchanged command passed with local process-spawn permission.
- A frontend rebuild replaced content-hashed distribution filenames. Before the rebuilt dist was staged, the tracked-file integrity test correctly reported three indexed files as missing. Staging only `brickflowui/frontend/dist` reconciled the index with the generated artifact set; the full Python suite then passed.
- npm advisory data reported one high-severity `brace-expansion` issue, [GHSA-3jxr-9vmj-r5cp](https://github.com/advisories/GHSA-3jxr-9vmj-r5cp). A non-forced `npm audit fix` updated only compatible transitive releases (`1.1.13` to `1.1.16` and `2.0.3` to `2.1.2`); the final audit reports zero vulnerabilities.

## Browser verification by retained example

| Example | Routes and interaction evidence | Refresh, reconnect, theme, and console evidence |
| --- | --- | --- |
| Quickstart Counter | `/` loaded; `+` changed `Count 0` to `Count 1`. | Reload/reconnect returned the documented initial `Count 0`; zero console errors. |
| Component Studio | `/` loaded; Visuals navigation changed the rendered section. The badge now reads `Supported surface`; no `0.1.14`, `astellas`, or `inspired` copy remained. | Reload/reconnect from Visuals established a new page/WebSocket session and restored the documented Overview state; zero console errors. |
| Data Pipeline Command Center | `/` loaded; all five state-driven views rendered distinct markers: Operational pulse, Pipeline flow, Reliability signals, Triage queue, and Pipeline assistant. | After switching to Reliability, direct reload/reconnect returned the documented default Overview and `Operational pulse`; zero runtime or console errors. |
| Clinical Trial Command Center | `/`, `/overview`, `/safety`, and `/dataops` loaded through an authenticated static-principal browser harness. Site selection changed to Toyama; the safety marker was `Safety review`; Light changed to Dark. | Direct-route reload/reconnect re-established the page and static-principal WebSocket content; zero console errors. Normal HTTP requests with manifest headers returned 200 for every route. This does not establish anonymous or live Databricks identity behavior. |
| Authentication Portal | Viewer, analyst, and admin sign-in forms worked; analyst received the admin-denied state; admin reached Admin Console; sign-out and app-ops app identity worked. Browser title/body now use `BrickflowUI Access Portal`; no forbidden borrowed branding remained. | Direct reload/reconnect of the analyst workspace retained the signed-in workspace and re-established WebSocket content. Theme toggle worked; zero console errors. |
| Chatbot Workspace | `/` loaded; submitting `What needs attention?` rendered the user message and assistant context. | Reload/reconnect worked; zero console errors. |

The in-app browser cannot inject the clinical example's manifest headers. The browser harness therefore used the same app/provider contract with a static authenticated principal, while separate normal HTTP route checks used the declared headers. Neither check is represented as live Databricks authentication.

Here, reconnect evidence means that a deliberate browser reload/direct-route navigation established a new page and WebSocket session. The run did not simulate a server outage and does not claim automatic recovery from one.

## Flagship responsive and accessibility evidence

| Check | Evidence |
| --- | --- |
| `390x844` | Document `clientWidth == scrollWidth == 385`. All six navigation buttons had x-coordinates at or above 12px and were reachable; controls wrapped into two rows. |
| `768x1024` | Document `clientWidth == scrollWidth == 762`. |
| `1280x800` | Document `clientWidth == scrollWidth == 1274`; all flagship navigation controls remained on one row. |
| `1440x900` | Document `clientWidth == scrollWidth == 1434`. |
| Dialog semantics | Executive brief exposes `role="dialog"`, an accessible name through `aria-labelledby`, and `aria-modal="true"`; the close icon is named `Close Executive brief`. |
| Dialog focus entry/trap | Focus enters the close button. Shift+Tab wraps to `Simulated acknowledge`; Tab wraps back. Escape closes the dialog. |
| Focus restoration | Before open, focus was on the Executive brief button. After Escape and the server-driven replacement, focus returned to the replacement `BUTTON` named `Executive brief` with its new server event/focus key. |
| Reduced motion | Static/runtime bundle CSS plus the automated theme test verifies the `prefers-reduced-motion: reduce` override makes animation/transition durations effectively immediate, limits animation iterations to one, and disables smooth scrolling without hiding content. The in-app browser cannot emulate or mutate `matchMedia`, so live media-query emulation was unavailable and is not claimed. |
| Visible focus and control reachability | Executive brief displayed a solid 1.6px primary-color outline with 0.8px offset. Native semantic controls and the complete modal keyboard cycle were verified by keyboard. Nav/modal/chat/auth/clinical actions were in-viewport and functional; some non-modal actions were exercised by browser click rather than keyboard. Hierarchy was readable in captured screenshots/DOM; light/dark toggles passed where exposed (clinical and auth). |

## Defects found and repaired during verification

| ID | Finding | Repair and regression evidence |
| --- | --- | --- |
| SF-01 | Grid intrinsic sizing caused document overflow at 390px and 768px. | Every responsive track now uses `minmax(0, 1fr)` and grid children/cards can shrink with `min-width: 0`; CSS regression added; all four live widths now match. |
| SF-02 | Right-justified, non-wrapping flagship navigation placed early actions off-screen at 390px. | Inner navigation explicitly wraps from the left with a shrinkable desktop row; Python serialization regression added; live mobile controls are reachable and desktop remains one row. |
| SF-03 | Modal lacked dialog semantics, focus entry/trap, Escape close, and focus restoration. | Dedicated Modal component adds semantics, labelled close, keyboard containment, Escape dispatch, logical-VDOM-path trigger restoration across callback regeneration, and hidden/inert/non-rendered control filtering; six DOM regressions and the final live flow pass. |
| SF-04 | No `prefers-reduced-motion` override existed. | Added global reduced-motion durations/iteration/scroll override and a CSS regression. |
| SF-05 | Component Studio advertised stale version `0.1.14`. | Replaced it with version-neutral `Supported surface` copy and added a no-embedded-SemVer guard. |
| SF-06 | Authentication Portal borrowed Astellas branding and imitation copy. | Replaced all retained-example occurrences with generic BrickflowUI security UI language and added a tracked-file raw-byte scan for `astellas` and `inspired`. |
| SF-07 | Current npm advisory data identified high-severity vulnerable transitive `brace-expansion`. | Applied compatible non-forced transitive updates; final audit reports zero vulnerabilities. |

## External Databricks boundary

No authenticated Databricks Apps workspace was available for this run. The local examples, mock records, static-principal browser harness, manifest-header HTTP checks, and SQL fallback tests do **not** prove live workspace behavior.

Still external and unverified:

- Databricks Apps deployment and routing.
- Workspace OAuth consent, forwarded user identity, token lifetime, and reconnect behavior.
- Unity Catalog permissions and data visibility for real users.
- SQL warehouse discovery, startup, query execution, and resource permissions.
- Jobs API permissions, execution, audit records, and multi-user isolation.
- Service-principal configuration, secrets, network policy, and production concurrency.

No deployment, live query, job run, workspace mutation, package publication, push, tag, or release was performed.

## Exact verification commands

```text
python -m pytest -q -p no:cacheprovider
python scripts/smoke_examples.py
python scripts/generate_component_reference.py
git diff --exit-code -- docs/components/reference
python -m mkdocs build --strict -d .site_validation_showcase
python -m build
python -m twine check dist/*
npm --prefix frontend test -- --run
npm --prefix frontend run lint
npm --prefix frontend run typecheck
npm --prefix frontend audit --audit-level=high
npm --prefix frontend run build
git diff --exit-code -- brickflowui/frontend/dist
git diff --check
```

## Verdict

All locally reproducible automated, example, responsive, console, and accessibility checks in the milestone scope pass. The only unavailable browser sub-check was live reduced-motion media emulation; the rule is present in the runtime bundle and covered by an automated CSS regression. Real Databricks Apps behavior remains an explicit external validation boundary and is the only reason this report does not make an unrestricted production-deployment claim.
