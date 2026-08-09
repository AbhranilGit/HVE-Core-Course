---
title: "Issue #6 implement — instance today helper and day defaulting"
description: Implementation summary for PulseBoard TEMP-2 / GitHub #6 following the approved plan
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-06
  - timezone
  - implement
  - rpi
estimated_reading_time: 4
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6) — api: instance today helper and day defaulting |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-2** |
| Phase | Implement (`/rpi continue=3`) |
| Status | Complete |
| Based on | [plan.md](plan.md) |
| Background | [research.md](research.md) |

## Summary

Implemented instance-level calendar today:

* `src/pulseboard/today.py` — `resolve_instance_tz`, `instance_today` → `date`, `default_status_day_str`
* `PULSEBOARD_TZ` IANA override (stdlib `zoneinfo`); host local default; invalid → `ValueError`
* Injectable `now` / `tz` for tests
* `list_statuses_for_today` thin wrapper on repository
* Tests for AC-P-010–013; existing #2 tests still green

No FastAPI, schema changes, identity, HTTP upsert/list, UI, or Sprint 2 work.

## Files changed

| Path | Change |
|------|--------|
| [src/pulseboard/today.py](../../../../src/pulseboard/today.py) | **Added** |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | **Edited** — `list_statuses_for_today` |
| [tests/test_instance_today.py](../../../../tests/test_instance_today.py) | **Added** |
| [src/pulseboard/db.py](../../../../src/pulseboard/db.py) | Unchanged |
| [pyproject.toml](../../../../pyproject.toml) | Unchanged (`dependencies = []`) |

## Commands run

```bash
/home/abhranil/Installation/miniconda3/envs/hve-env/bin/python -m pytest \
  tests/test_instance_today.py tests/test_status_repository.py -v
```

Result: **11 passed** in ~0.08s.

## Acceptance criteria results

| AC / check | Result | Evidence |
|------------|--------|----------|
| AC-P-010 host local when no TZ override | **Pass** | `test_ac_p_010_no_tz_override_matches_host_local` |
| AC-P-011 `PULSEBOARD_TZ` IANA | **Pass** | `test_ac_p_011_pulseboard_tz_iana` (UTC vs Pacific/Kiritimati) |
| AC-P-012 default create day = `instance_today` | **Pass** | `test_ac_p_012_default_status_day_matches_instance_today` (helper + upsert) |
| AC-P-013 prior day excluded from today list | **Pass** | `test_ac_p_013_list_today_excludes_prior_day` |
| Invalid TZ raises | **Pass** | `test_invalid_pulseboard_tz_raises` |
| #2 regression | **Pass** | all 5 `test_status_repository` tests |

## `.copilot-tracking/` notes

* [.copilot-tracking/changes/2026-08-09/issue-06-today-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-06-today-changes.md)
* Prior: `.copilot-tracking/research/2026-08-09/issue-06-today-research.md`, `.copilot-tracking/plans/2026-08-09/issue-06-today-plan.md`

## Deviations from plan

| Item | Notes |
|------|-------|
| `__init__.py` re-exports | Skipped (optional; same as #2) |
| `list_statuses_for_today` `tz` annotation | Unannotated `tz=None` to avoid importing `tzinfo` only for a hint; behavior matches plan |
| Otherwise | None |

## Scope confirmation

* Did **not** start #4, #5, #3, #9, or Sprint 2
* Did **not** change schema or add FastAPI
* Did **not** auto-default `upsert_status` day (callers use `default_status_day_str`)

## Ready for next issue?

- [x] Implement summary written
- [x] AC-P-010–013 automated evidence green
- [ ] User verifies Implement + Gate in [`README.md`](README.md) before issue #4

## Next

Sprint 1 order: issue **#4** — display name identity with cookie continuity.
