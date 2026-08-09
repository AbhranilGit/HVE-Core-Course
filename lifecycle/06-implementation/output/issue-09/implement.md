---
title: "Issue #9 implement - today board and status form UI (HTMX)"
description: Implementation summary for PulseBoard TEMP-6 and GitHub issue #9 based on approved plan
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-09
  - ui
  - htmx
  - today-board
  - implement
  - rpi
estimated_reading_time: 6
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9) - ui: today board and status form (HTMX) |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-6 |
| Phase | Implement (`/rpi continue=3`) |
| Status | Complete |
| Based on | [plan.md](plan.md) |
| Background | [research.md](research.md) |

## Summary

Implemented a server-rendered MVP board page and UI form flow wired to existing identity, upsert, and list behaviors.

* Added `GET /` board page with:
  * display-name section and form
  * status entry form (`doing`, `blocked`, `next`)
  * today board table/list rendering
* Added explicit empty-state copy when there are no statuses today
* Added UI submit routes:
  * `POST /ui/identity` to set cookie and return to board
  * `POST /ui/status` to upsert and return to board
* Kept existing JSON API routes intact (`POST /status`, `GET /statuses/today`)
* Added TEMP-6 UI acceptance tests (AC-P-050..054)

No Sprint 2 work was started, and no scope beyond TEMP-6 was added.

## Files changed

| Path | Change |
|------|--------|
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | Edited - board page rendering helpers, `GET /`, `POST /ui/identity`, `POST /ui/status` |
| [tests/test_ui_today_board.py](../../../../tests/test_ui_today_board.py) | Added - AC-P-050..054 UI tests |
| [lifecycle/06-implementation/output/issue-09/implement.md](implement.md) | Edited - implementation evidence |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | Unchanged |
| [src/pulseboard/status_service.py](../../../../src/pulseboard/status_service.py) | Unchanged |

## Commands run

```bash
/home/abhranil/Installation/miniconda3/envs/hve-env/bin/python -m pytest tests/test_ui_today_board.py -q --tb=short
/home/abhranil/Installation/miniconda3/envs/hve-env/bin/python -m pytest tests/ -q --tb=short
```

Result:

* `5 passed, 1 warning` (UI tests)
* `38 passed, 1 warning` (full suite)

## Acceptance criteria results

| AC / check | Result | Evidence |
|------------|--------|----------|
| AC-P-050 open UI, set name, enter fields, submit | Pass | `test_ac_p_050_ui_can_set_name_enter_fields_and_submit` |
| AC-P-051 successful save visible on board without chat | Pass | `test_ac_p_051_successful_save_visible_on_today_board` |
| AC-P-052 zero posts shows clear empty state | Pass | `test_ac_p_052_empty_board_has_clear_empty_state` |
| AC-P-053 multiple posts show display_name/doing/blocked/next | Pass | `test_ac_p_053_multiple_rows_show_required_columns` |
| AC-P-054 no SSO/lock/workflow/notifications in MVP UI | Pass | `test_ac_p_054_absence_of_sso_lock_workflow_notifications` |

## Scope checks

| Check | Result |
|-------|--------|
| No Sprint 2 implementation (#10/#8/#7) | Pass |
| No websocket live updates | Pass |
| No SSO/OAuth UI | Pass |
| No lock-after-standup control | Pass |
| No blocked workflow/timer/notifications | Pass |
| No multi-day history navigation | Pass |

## `.copilot-tracking/` notes

* [changes/2026-08-09/issue-09-ui-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-09-ui-changes.md)

## Deviations from plan

* None.

## Ready for next issue?

- [x] Yes - verification checklist in README.md can be completed
