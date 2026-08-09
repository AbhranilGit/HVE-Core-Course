---
title: "Issue #6 plan — instance today helper and day defaulting"
description: Implementation plan for PulseBoard TEMP-2 / GitHub #6 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-06
  - timezone
  - instance-today
  - plan
  - rpi
estimated_reading_time: 6
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6) — api: instance today helper and day defaulting |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-2** |
| Phase | Plan only (`/rpi continue=2`) |
| Status | Complete — ready for Implement gate |
| Based on | [research.md](research.md) (complete; Status Complete — ready for Plan gate) |
| Production code | **None** (this phase) |
| Sprint | 2 of 6 (Sprint 1) |
| Depends on | #2 in place (schema/repo) |

## User requests (this phase)

1. Plan implementation of PulseBoard issue #6 (TEMP-2) only.
2. Do not implement yet.
3. Base the plan on completed `lifecycle/06-implementation/output/issue-06/research.md`.
4. Include steps, files to touch, acceptance checks from the local issue spec, and risks.
5. Stay inside this issue’s scope.
6. Write the plan to `lifecycle/06-implementation/output/issue-06/plan.md`.

## Objectives

Provide a single instance-level “today” calendar date (host local by default, optional `PULSEBOARD_TZ`) so MVP create defaults and today-board listing share one day boundary — without HTTP, schema changes, or sibling feature work.

## Alignment with research (no contradictory inventions)

| Research decision | Plan adoption |
|-------------------|---------------|
| Module `src/pulseboard/today.py` | Yes |
| `instance_today() -> date` | Yes |
| `resolve_instance_tz()` | Yes |
| `PULSEBOARD_TZ` IANA via stdlib `zoneinfo` | Yes |
| Unset/empty env → host local | Yes |
| Invalid TZ → `ValueError` | Yes |
| Injectable `now` / `tz` kwargs | Yes |
| `default_status_day_str()` for AC-P-012 contract | Yes |
| `list_statuses_for_today` in `repository.py` (imports `today`) | Yes |
| No FastAPI / no schema change / no new deps | Yes |
| Tests with fixed `now`, monkeypatch env | Yes |

**Intentional deltas from research:** none.

## Design summary

### Public API (`today.py`)

| Symbol | Behavior |
|--------|----------|
| `ENV_TZ = "PULSEBOARD_TZ"` | Documented constant |
| `resolve_instance_tz() -> tzinfo` | If env set and non-empty after strip → `ZoneInfo(name)`; on `ZoneInfoNotFoundError` raise `ValueError` with clear message; else host local via `datetime.now().astimezone().tzinfo` |
| `instance_today(*, now: datetime \| None = None, tz: tzinfo \| None = None) -> date` | Resolve tz (arg or `resolve_instance_tz()`). If `now` is None → `datetime.now(tz=resolved)`. If `now` is naive → replace/attach resolved tz (`now.replace(tzinfo=resolved)`). If aware → convert with `.astimezone(resolved)`. Return `.date()`. |
| `default_status_day_str(*, now=None, tz=None) -> str` | `instance_today(now=..., tz=...).isoformat()` — domain default for create when no other day chosen (AC-P-012 contract for #5) |

Module docstring: describe `PULSEBOARD_TZ`, host-local default, and that runbook (#8) will document operators.

### Repository addition (`repository.py`)

| Symbol | Behavior |
|--------|----------|
| `list_statuses_for_today(conn, *, now=None, tz=None) -> list[Status]` | `day = default_status_day_str(now=now, tz=tz)` then `return list_statuses_for_day(conn, day)` |

Import `default_status_day_str` (or `instance_today`) from `pulseboard.today` only inside this function or at module top — `today.py` must **not** import `repository` (avoid cycles).

Do **not** change `upsert_status` signature to auto-default day in this issue unless trivial; research prefers callers (#5) pass `default_status_day_str()`. Optional convenience is out of scope if it blurs validation ownership — stick to list helper + today helpers only.

### Configuration

* Env: `PULSEBOARD_TZ` (IANA).
* No config file.
* No `pyproject.toml` dependency changes expected.

## Implementation steps

Execute in order during `/rpi continue=3`. Do **not** start #4/#5/#3/#9 or Sprint 2.

### Step 1 — `today.py` core

<!-- parallelizable: false -->

1. Add `src/pulseboard/today.py`.
2. Implement `resolve_instance_tz`, `instance_today`, `default_status_day_str` as above.
3. Docstring covers env + defaults for #8.
4. No I/O beyond reading env and system clock.

### Step 2 — `list_statuses_for_today`

<!-- parallelizable: false -->

1. Edit `src/pulseboard/repository.py`.
2. Add thin wrapper calling `list_statuses_for_day` with `default_status_day_str(...)`.
3. Pass through optional `now`/`tz` for tests.
4. Leave existing upsert/get/list-by-day behavior unchanged.

### Step 3 — Package exports (optional)

<!-- parallelizable: false -->

1. Leave `__init__.py` unchanged unless a single re-export is useful; prefer submodule imports in tests (same as #2).

### Step 4 — Tests

<!-- parallelizable: false -->

1. Add `tests/test_instance_today.py`.
2. Cases:
   * **AC-P-010:** `monkeypatch.delenv("PULSEBOARD_TZ", raising=False)`; fixed aware `now` in host-local (or explicit local tz); `instance_today(now=now)` equals `now.astimezone().date()` / expected local date. Also: with `tz` overridden to a known zone and fixed UTC instant, date matches that zone’s calendar date when env unset and tz passed explicitly — and/or compare `instance_today(now=now)` to `now.astimezone(resolve_instance_tz()).date()`.
   * **AC-P-011:** `monkeypatch.setenv("PULSEBOARD_TZ", "UTC")` vs `"Pacific/Kiritimati"` (or `America/Los_Angeles`) with the **same** fixed UTC `now` chosen near a date boundary so the two zones disagree on calendar date; assert different dates and each matches `now.astimezone(ZoneInfo(...)).date()`.
   * **Invalid TZ:** `PULSEBOARD_TZ=Not/A_Zone` → `ValueError`.
   * **AC-P-012:** `default_status_day_str(now=now, tz=tz) == instance_today(now=now, tz=tz).isoformat()`; optional: `upsert_status(..., status_day=default_status_day_str(now=...))` then `get_status` shows that day (proves default string is what persistence stores when create uses helper — without HTTP).
   * **AC-P-013:** `init_db(tmp_path)`; upsert prior day + today (today from helper with fixed now); `list_statuses_for_today(conn, now=fixed)` returns only today row(s).
3. Keep existing `tests/test_status_repository.py` green (no breakages).
4. Run pytest with Python 3.12 (`hve-env`).

### Step 5 — Implement summary

<!-- parallelizable: false -->

1. Write `lifecycle/06-implementation/output/issue-06/implement.md`.
2. Record files, pytest output, AC results, deviations.
3. Note `.copilot-tracking/` if written.

### Step 6 — Validation gate

<!-- parallelizable: false -->

1. All new + existing tests pass.
2. No new runtime deps unless `tzdata` proven necessary.
3. No FastAPI/schema/sibling scope creep.

## Files to touch

| Path | Action | Notes |
|------|--------|-------|
| [src/pulseboard/today.py](../../../../src/pulseboard/today.py) | **Add** | TZ resolve + `instance_today` + default day string |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | **Edit** | Add `list_statuses_for_today` only |
| [tests/test_instance_today.py](../../../../tests/test_instance_today.py) | **Add** | AC-P-010–013 |
| [src/pulseboard/db.py](../../../../src/pulseboard/db.py) | **No change** | |
| [src/pulseboard/models.py](../../../../src/pulseboard/models.py) | **No change** | |
| [pyproject.toml](../../../../pyproject.toml) | **No change expected** | |
| [lifecycle/06-implementation/output/issue-06/implement.md](implement.md) | **Edit** | phase-3 summary |
| FastAPI / auth / UI / runbook | **Do not add** | |

## Acceptance checks

| ID | Criterion (TEMP-2) | How we will verify |
|----|--------------------|--------------------|
| AC-P-010 | No TZ override → today = host local calendar date | Test: env unset; fixed `now`; result matches local/host calendar date for that instant |
| AC-P-011 | Valid `PULSEBOARD_TZ` → today in that zone | Test: env set to IANA; fixed UTC instant; date matches `ZoneInfo` conversion |
| AC-P-012 | Create without other day → `status_day` equals `instance_today()` | Test: `default_status_day_str` == isoformat of `instance_today`; upsert with that default and read back (domain contract; HTTP #5 later) |
| AC-P-013 | Prior-day-only rows excluded when listing today | Test: seed prior + today; `list_statuses_for_today` omits prior |

### Scope checks (negative)

| Check | Verify |
|-------|--------|
| No per-user TZ / geo / history UI | Code review |
| No schema migration | `db.py` untouched |
| No HTTP/cookies/HTMX | No new web modules |
| Repository still accepts explicit `status_day` | Existing tests pass |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Midnight / wall-clock flaky tests | Always inject `now=` for assertions |
| Invalid IANA | `ValueError` with zone name in message |
| Missing tzdata on bare images | Run tests on hve-env Linux first; add `tzdata` only if ZoneInfo fails |
| Naive `now` ambiguity | Document: naive treated as instance tz wall time via `replace(tzinfo=...)` |
| Circular imports | `today` pure; `repository` imports `today` |
| Over-claiming AC-P-012 without HTTP | Helper + upsert contract test; note #5 wires route |
| Changing upsert to auto-default day | **Do not** in #6 — keeps #5 validation ownership clear |

## Out of scope (do not implement in #6)

* FastAPI routes, lifespan, uvicorn
* Display-name cookies (#4)
* HTTP upsert/list (#5, #3)
* HTMX UI (#9)
* Schema/DDL changes
* Runbook body (#8)
* Full product test suite (#10)
* Per-user timezones, geo detection, multi-day history UI
* Edit-only-if-today enforcement (domain later)

## Dependencies

| Depends on | Status |
|------------|--------|
| Research.md complete | Done |
| #2 repository `list_statuses_for_day` / `upsert_status` | Done |
| Unblocks | #5 (default day), #3 (today list), #9 board, #10 clock freeze |

## Success criteria for Implement phase

* [ ] `today.py` with resolve + `instance_today` + default day string
* [ ] `list_statuses_for_today` on repository
* [ ] AC-P-010–013 covered by tests and passing
* [ ] Existing #2 tests still pass
* [ ] No new runtime deps unless required
* [ ] `implement.md` records evidence
* [ ] No sibling issue production work

## Ready for implement?

- [x] Plan filled (steps, files, AC checks, risks)
- [x] Plan matches `research.md` (no contradictory findings)
- [x] Scope is this issue only
- [ ] User verifies Plan section in [`README.md`](README.md) before `/rpi continue=3`

## Next command (after Plan gate)

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #6 (TEMP-2) only. ...
```

See [issue-06.md](../../prompt/issue-06.md) Phase 3 prompt for full text.

## References

* [research.md](research.md)
* [backlog-snapshot.md — TEMP-2](../../04-decomposition/output/backlog-snapshot.md)
* [issue-02 implement](../issue-02/implement.md)
* [ADR today timezone](../../03-product-definition/output/adr/2026-08-09-today-instance-timezone-v01.md)
