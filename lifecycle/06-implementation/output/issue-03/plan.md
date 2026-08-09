---
title: "Issue #3 plan - list statuses for today board"
description: Implementation plan for PulseBoard TEMP-5 and GitHub issue #3 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
	- pulseboard
	- issue-03
	- list
	- today-board
	- plan
	- rpi
estimated_reading_time: 6
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3) - api: list statuses for today board |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-5 |
| Phase | Plan only (`/rpi continue=2`) |
| Status | Complete - ready for Implement gate |
| Based on | [research.md](research.md) (complete and present) |
| Production code | None (this phase) |
| Sprint | 5 of 6 (Sprint 1) |
| Depends on | #2, #6, and #5 in place; no blocker from research |

## User requests (this phase)

1. Plan implementation of PulseBoard issue #3 (TEMP-5) only
2. Do not implement yet
3. Require plan to be based on completed [research.md](research.md)
4. Require TEMP-5 scope and AC from [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md)
5. Leave HTMX UI work to #9
6. Include steps, files to touch, acceptance checks, and risks
7. Stay strictly inside this issue scope
8. Write plan to [plan.md](plan.md)

## Objective

Expose a read API for the facilitator board that returns all rows for instance today, with deterministic ordering and required board fields, while preserving current write behavior from #5 and deferring HTMX board UI to #9.

## Alignment with research

| Research decision | Plan adoption |
|-------------------|---------------|
| Use existing `list_statuses_for_today` as source of truth | Yes |
| Add HTTP list route for today only | Yes |
| Keep list read open (no identity requirement) | Yes |
| Empty result is success, not error | Yes |
| Deterministic ordering preserved from repository | Yes |
| No client day override for MVP list path | Yes |
| Keep HTMX board and templates out of this issue | Yes |

Intentional deltas from research: none.

## Design summary

### Route and response

| Piece | Decision |
|-------|----------|
| Method/path | Add `GET /statuses/today` |
| Data source | `repository.list_statuses_for_today(conn)` |
| Auth | No cookie required for read path |
| Success | HTTP 200 with JSON array |
| Empty state | `[]` with HTTP 200 |
| Item fields | Include at least display_name, doing, blocked, next; existing serializer may include status_day, id, timestamps |
| Ordering | Keep repository order (`display_name COLLATE NOCASE`) |
| Day input | Do not accept query/body day override |

### App integration

Use the same DB access pattern already present in app routes.

1. Open connection from `request.app.state.db_path`
2. Call list helper for today
3. Close connection in `finally`
4. Return JSON list of serialized rows

No schema changes, no today helper changes, and no identity behavior changes are planned.

### Optional service wrapper

If needed for readability only, a tiny list wrapper may be added to `status_service.py` that delegates to repository list-today. This is optional and not required for acceptance criteria.

## Implementation steps

Execute in order during `/rpi continue=3`. Do not start #9, #10, #8, or #7 here.

### Step 1 - Add today-list HTTP route in app

<!-- parallelizable: false -->

1. Edit [src/pulseboard/app.py](../../../../src/pulseboard/app.py)
2. Add `GET /statuses/today`
3. Reuse existing status serialization shape
4. Ensure no identity gate on this route
5. Ensure empty list returns 200 with empty array

### Step 2 - Add issue-focused tests for list API

<!-- parallelizable: false -->

1. Add [tests/test_status_list_today.py](../../../../tests/test_status_list_today.py)
2. Cover AC-P-040 through AC-P-045
3. Seed data with existing write path (#5) or repository helpers where setup is simpler
4. Use `create_app(db_path=tmp_path / "*.db")` and TestClient context manager

### Step 3 - Keep regression safety

<!-- parallelizable: false -->

1. Run full test suite in hve-env Python 3.12
2. Confirm no regressions for #2, #4, #5, #6 tests

### Step 4 - Implement artifact update

<!-- parallelizable: false -->

1. During continue=3, write [implement.md](implement.md)
2. Add or update `.copilot-tracking/changes` entry for issue #3
3. Record AC-by-AC evidence and any deviations

## Files to touch

| Path | Action | Notes |
|------|--------|-------|
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | Edit | Add GET list route only |
| [tests/test_status_list_today.py](../../../../tests/test_status_list_today.py) | Add | AC-P-040..045 coverage |
| [lifecycle/06-implementation/output/issue-03/implement.md](implement.md) | Edit in continue=3 | Implementation summary |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | No change expected | Reuse existing list helpers |
| [src/pulseboard/status_service.py](../../../../src/pulseboard/status_service.py) | Optional tiny wrapper | Only if it improves readability |
| HTMX templates/pages | Do not touch | Reserved for #9 |

## Acceptance checks

| ID | Criterion (TEMP-5) | How we will verify |
|----|--------------------|--------------------|
| AC-P-040 | Zero today statuses returns empty collection | GET route returns 200 and empty array |
| AC-P-041 | Listed rows include display_name, doing, blocked, next | Assert keys per item |
| AC-P-042 | Prior-day rows are excluded | Seed yesterday rows only; today list is empty |
| AC-P-043 | Distinct names remain distinct rows | Seed two names today; list includes both names |
| AC-P-044 | Non-empty blocked is visible in list | Seed blocked text; assert listed blocked value |
| AC-P-045 | Empty blocked does not hide row | Seed doing/next with blocked empty; row still present |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Scope creep into HTMX board (#9) | Keep output JSON-only and avoid UI/template changes |
| Accidentally requiring identity on read | Do not call `require_display_name` in GET list route |
| Returning 404 on empty board | Lock expected behavior to 200 plus empty array in tests |
| Adding client day override accidentally | No day parameter in route signature |
| Re-implementing query logic | Reuse `list_statuses_for_today` from repository |

## Out of scope (do not implement in #3)

* HTMX board page, partial rendering, or styling (#9)
* Blocked-only filters or workflow semantics
* Historical day browsing
* Websocket real-time updates
* Schema redesign or identity model changes
* Sprint 2 and release-doc issues

## Ready to implement?

- [x] Research present and used as the planning source
- [x] TEMP-5 AC-P-040 through AC-P-045 mapped to concrete checks
- [x] Steps and file touch list stay inside issue #3 scope
- [x] No production code in this phase
- [ ] User verifies Plan checklist in [README.md](README.md) before continue=3

## Next

After plan gate: run `/rpi continue=3` for issue #3 implementation only.
