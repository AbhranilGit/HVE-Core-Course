---
title: "Issue #3 implement - list statuses for today board"
description: Implementation summary for PulseBoard TEMP-5 and GitHub issue #3 based on approved plan
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-03
  - list
  - today-board
  - implement
  - rpi
estimated_reading_time: 5
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3) - api: list statuses for today board |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-5 |
| Phase | Implement (`/rpi continue=3`) |
| Status | Complete |
| Based on | [plan.md](plan.md) |
| Background | [research.md](research.md) |

## Summary

Implemented TEMP-5 list API for facilitator board by adding a today-list HTTP endpoint and focused acceptance tests.

* Added `GET /statuses/today` in FastAPI app
* Route reads from existing `list_statuses_for_today` and returns JSON array
* No identity requirement on read route
* Empty board returns `200` with `[]`
* Added list tests covering AC-P-040 through AC-P-045
* Kept HTMX UI and board page out of scope for #9

No schema changes, no repository query rewrites, and no new product surface outside TEMP-5.

## Files changed

| Path | Change |
|------|--------|
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | Edited - added `GET /statuses/today` |
| [tests/test_status_list_today.py](../../../../tests/test_status_list_today.py) | Added - AC-P-040..045 coverage |
| [lifecycle/06-implementation/output/issue-03/implement.md](implement.md) | Edited - implementation summary |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | Unchanged |
| [src/pulseboard/status_service.py](../../../../src/pulseboard/status_service.py) | Unchanged |

## Commands run

```bash
/home/abhranil/Installation/miniconda3/envs/hve-env/bin/python -m pytest tests/ -q --tb=short
```

Result: `33 passed, 1 warning`.

## Acceptance criteria results

| AC / check | Result | Evidence |
|------------|--------|----------|
| AC-P-040 zero today statuses returns empty collection | Pass | `test_ac_p_040_empty_today_list_returns_200_and_empty` |
| AC-P-041 listed rows include display_name, doing, blocked, next | Pass | `test_ac_p_041_each_item_includes_required_fields` |
| AC-P-042 prior-day rows are excluded | Pass | `test_ac_p_042_prior_day_rows_are_excluded` |
| AC-P-043 distinct names remain distinct rows | Pass | `test_ac_p_043_distinct_names_remain_distinct_rows` |
| AC-P-044 non-empty blocked is present | Pass | `test_ac_p_044_blocked_text_present_for_scan` |
| AC-P-045 empty blocked row still appears | Pass | `test_ac_p_045_empty_blocked_row_still_appears` |

## Scope checks

| Check | Result |
|-------|--------|
| No HTMX UI implementation (#9) | Pass |
| No day override added to list route | Pass |
| No identity gate on list read | Pass |
| No schema migration | Pass |
| No websocket or history scope | Pass |

## `.copilot-tracking/` notes

* [changes/2026-08-09/issue-03-list-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-03-list-changes.md)

## Deviations from plan

* None.

## Ready for next issue?

- [x] Yes - verification checklist in README.md can be completed
