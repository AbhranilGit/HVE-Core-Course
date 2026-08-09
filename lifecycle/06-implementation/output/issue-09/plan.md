---
title: "Issue #9 plan - today board and status form UI (HTMX)"
description: Implementation plan for PulseBoard TEMP-6 and GitHub issue #9 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
	- pulseboard
	- issue-09
	- ui
	- htmx
	- today-board
	- plan
	- rpi
estimated_reading_time: 8
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9) - ui: today board and status form (HTMX) |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-6 |
| Phase | Plan only (`/rpi continue=2`) |
| Status | Complete - ready for Implement gate |
| Based on | [research.md](research.md) (complete and present) |
| Production code | None (this phase) |
| Sprint | 6 of 6 (Sprint 1) |
| Depends on | #4 identity, #5 upsert, #3 list API in place |

## User requests (this phase)

1. Plan implementation of PulseBoard issue #9 (TEMP-6) only
2. Do not implement yet
3. Base plan on completed [research.md](research.md)
4. Use TEMP-6 scope and acceptance criteria from [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md)
5. Include steps, files to touch, acceptance checks, and risks
6. Stay inside this issue scope
7. Write plan to [plan.md](plan.md)

## Objective

Deliver a server-rendered, HTMX-friendly browser UI that allows a user to set display name, submit/update doing-blocked-next, and view today board rows including clear empty state, while reusing existing identity, upsert, and list behaviors.

## Alignment with research

| Research decision | Plan adoption |
|-------------------|---------------|
| Option A baseline: single server-rendered board page | Yes |
| Reuse #4/#5/#3 behavior rather than redesigning APIs | Yes |
| Keep HTMX progressive enhancement optional and thin | Yes |
| Keep out-of-scope items excluded (SSO, lock, workflow, notifications) | Yes |
| Keep keyboard-usable core flow and semantic markup | Yes |

Intentional deltas from research: none.

## Design summary

### UI route and flow

| Piece | Decision |
|-------|----------|
| Primary page | Add `GET /` as the MVP board page |
| Identity input | Inline display-name form posting to `/identity` |
| Status input | Inline doing/blocked/next form posting to `/status` |
| Board view | Render rows for today from existing list behavior |
| Empty state | Show explicit empty-state copy when no rows exist |
| Save-to-view path | After successful save, user lands/refreshes on board page and sees current values |

### Response model

| Route | Behavior |
|-------|----------|
| `GET /` | Returns HTML page with identity section, status form, and board section |
| `POST /identity` | Keep current behavior; redirect flow should return user to board page for UX continuity |
| `POST /status` | Keep current JSON API for compatibility; board page flow can use standard POST + redirect or HTMX trigger in implementation |

### Rendering strategy

Use simple server-rendered HTML in `app.py` for this slice, matching existing inline HTML pattern.

* Helper to render board rows/table from status list
* Helper to render page-level shell and forms
* Semantic labels and controls for keyboard use
* HTMX attributes may be added minimally if they do not expand scope

Template engine introduction is deferred unless implementation complexity forces it.

## Implementation steps

Execute in order during `/rpi continue=3`. Do not start #10, #8, or #7.

### Step 1 - Build MVP board page route

<!-- parallelizable: false -->

1. Edit [src/pulseboard/app.py](../../../../src/pulseboard/app.py)
2. Add `GET /` returning server-rendered HTML for:
	 * display name section
	 * status form section
	 * today board section
3. Read today statuses using existing behavior from issue #3
4. Add explicit empty-state copy when rows are absent

### Step 2 - Wire submit and refresh UX

<!-- parallelizable: false -->

1. Ensure identity update is reachable from the board page
2. Ensure status submit from UI path results in board visibility of submitted values
3. Keep core flow working without requiring HTMX JavaScript execution
4. Optionally add minimal HTMX attributes for progressive enhancement

### Step 3 - Add issue-focused UI tests

<!-- parallelizable: false -->

1. Add [tests/test_ui_today_board.py](../../../../tests/test_ui_today_board.py)
2. Cover AC-P-050 through AC-P-054
3. Use `TestClient(create_app(db_path=tmp_path / "ui.db"))` in context manager
4. Seed where needed through existing routes/repository helpers

### Step 4 - Regression and artifact updates

<!-- parallelizable: false -->

1. Run full suite in hve-env Python 3.12
2. Confirm no regressions in #4/#5/#3 tests
3. Write [implement.md](implement.md) with AC evidence and deviations
4. Add `.copilot-tracking/changes` entry for issue #9

## Files to touch

| Path | Action | Notes |
|------|--------|-------|
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | Edit | Add board HTML route and UI wiring |
| [tests/test_ui_today_board.py](../../../../tests/test_ui_today_board.py) | Add | AC-P-050..054 coverage |
| [lifecycle/06-implementation/output/issue-09/implement.md](implement.md) | Edit in continue=3 | Implementation summary |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | No change expected | Reuse existing list behavior |
| [src/pulseboard/status_service.py](../../../../src/pulseboard/status_service.py) | No change expected | Reuse existing upsert behavior |
| New frontend build files | Do not add | Out of scope for TEMP-6 |

## Acceptance checks

| ID | Criterion (TEMP-6) | How we will verify |
|----|--------------------|--------------------|
| AC-P-050 | UI allows set name + enter fields + submit | Integration test checks presence of forms/inputs and successful submit path |
| AC-P-051 | After successful save, own values visible on today board | UI flow test validates posted values appear in board content |
| AC-P-052 | Zero posts shows clear empty state | Fresh DB GET page contains empty-state copy and no error |
| AC-P-053 | Multiple posts show full row fields | Seed two rows; verify page includes display_name/doing/blocked/next for each |
| AC-P-054 | No SSO/lock/workflow/notifications in MVP UI | Assertions on rendered markup/routes for absence of those controls/terms |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Scope creep into visual design-system work | Keep markup plain and functional; prioritize behavior ACs |
| Coupling page rendering to API self-calls | Use direct app-side list retrieval where straightforward |
| Failing AC-P-051 due to redirect/refresh mismatch | Define deterministic post-save return path to board page |
| Keyboard accessibility gaps | Use labels, semantic headings, predictable tab flow, and test checks |
| Hidden feature creep for SSO/lock/workflow | Add explicit negative assertions in tests |

## Out of scope (do not implement in #9)

* Pixel-perfect branding and design system migration
* Mobile app
* Websocket live updates
* Multi-day history navigation
* SSO or OAuth UI
* Lock-after-standup or blocked workflow states
* Notifications
* Sprint 2 work (#10, #8, #7)

## Ready to implement?

- [x] Research present and used as sole planning basis
- [x] TEMP-6 AC-P-050 through AC-P-054 mapped to checks
- [x] Steps and file touch list stay inside issue #9 scope
- [x] No production code in this phase
- [ ] User verifies Plan checklist in [README.md](README.md) before continue=3

## Next

After plan gate: run `/rpi continue=3` for issue #9 implementation only.
