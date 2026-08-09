---
title: "Issue #5 implement — upsert status for today under display name"
description: Implementation summary for PulseBoard TEMP-4 / GitHub #5 following the approved plan
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-05
  - upsert
  - status
  - implement
  - rpi
estimated_reading_time: 4
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) — upsert status for today under display name |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-4** |
| Phase | Implement (`/rpi continue=3`) |
| Status | Complete |
| Based on | [plan.md](plan.md) |
| Background | [research.md](research.md) |

## Summary

Implemented today-status upsert on the FastAPI surface (service + HTTP), scoped to TEMP-4 only:

* `src/pulseboard/status_service.py` — normalize/validate (≥1 non-empty field after trim); `upsert_today_status` defaults day via `default_status_day_str` and calls repository upsert (full field replace)
* `src/pulseboard/app.py` — `create_app(*, db_path=)`; eager + lifespan `init_db`; `app.state.db_path`; real `POST /status` (cookie identity + Form doing/blocked/next → JSON row; ValueError → 400)
* No client `status_day`, no lock-after-standup, no list HTTP (#3), no HTMX board (#9)
* Tests AC-P-030–034 + identity continuity updates; full suite green

## Files changed

| Path | Change |
|------|--------|
| [src/pulseboard/status_service.py](../../../../src/pulseboard/status_service.py) | **Added** — validation + today upsert |
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | **Edited** — db_path factory, lifespan/init_db, real POST /status |
| [tests/test_status_upsert.py](../../../../tests/test_status_upsert.py) | **Added** — AC-P-030–034 |
| [tests/test_identity.py](../../../../tests/test_identity.py) | **Edited** — tmp db fixture; POST /status with fields (drop not_implemented) |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | Unchanged |
| [src/pulseboard/db.py](../../../../src/pulseboard/db.py) | Unchanged |
| [src/pulseboard/today.py](../../../../src/pulseboard/today.py) | Unchanged |
| [src/pulseboard/identity.py](../../../../src/pulseboard/identity.py) | Unchanged |
| [pyproject.toml](../../../../pyproject.toml) | Unchanged |

## Commands run

```bash
# hve-env Python 3.12
python -m pytest tests/ -q
```

Result: **27 passed** in ~0.62s (1 Starlette/httpx deprecation warning).

## Acceptance criteria results

| AC / check | Result | Evidence |
|------------|--------|----------|
| AC-P-030 create today under name | **Pass** | `test_ac_p_030_create_today_status` |
| AC-P-031 day = instance today | **Pass** | `test_ac_p_031_day_is_instance_today` |
| AC-P-032 second submit one row | **Pass** | `test_ac_p_032_second_submit_one_row` |
| AC-P-033 reject all-empty | **Pass** | `test_ac_p_033_reject_all_empty*` |
| AC-P-034 no lock control | **Pass** | `test_ac_p_034_no_lock_after_standup_control` |
| Identity without cookie → 400 | **Pass** | `test_status_requires_identity`, AC-P-023 |
| #2 / #6 / #4 regression | **Pass** | full suite 27 green |

## `.copilot-tracking/` notes

* Changes: `.copilot-tracking/changes/2026-08-09/issue-05-upsert-changes.md`
* Plan/research already under `lifecycle/06-implementation/output/issue-05/` and `.copilot-tracking/` from prior phases

## Deviations from plan

* Eager `init_db(resolved)` inside `create_app` in addition to lifespan — ensures schema when TestClient is used without entering lifespan CM; lifespan still re-inits (IF NOT EXISTS).
* TestClient fixtures use context manager (`with TestClient(...)`) for lifespan safety.
* AC-P-034 lock assertion avoids substring match on `blocked`.

## Ready for next issue?

- [x] Yes — after lifecycle README verification gate for issue-05
- Next Sprint 1 issue per order: **#3** (list today HTTP) research (`/rpi continue=1` on issue-03)
