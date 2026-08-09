---
title: "Issue #6 research — instance today helper and day defaulting"
description: Research-only findings for PulseBoard TEMP-2 / GitHub #6 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-06
  - timezone
  - instance-today
  - research
  - rpi
estimated_reading_time: 7
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6) — api: instance today helper and day defaulting |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-2** |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete — ready for Plan gate |
| Production code | **None** (this phase) |
| Sprint | 2 of 6 (Sprint 1); prefer after #2 |
| #2 dependency | **In place** — no blocker |

## Scope summary (authoritative)

From TEMP-2 / #6:

**In scope**

* `instance_today()` (or equivalent) returning calendar date in instance TZ
* Default TZ = host local; optional env override with IANA name
* All MVP create defaults and today-board filters use this helper
* Clock/date injectable or overrideable in tests

**Out of scope**

* Per-user timezones
* Multi-day history UI
* Geo detection

**Acceptance criteria (must drive plan)**

| ID | Criterion | PRD / ADR link |
|----|-----------|----------------|
| AC-P-010 | Given no TZ override, when computing today, then the date matches the host local calendar date | PRD §4.1 OQ-04, ADR today |
| AC-P-011 | Given `PULSEBOARD_TZ` (or documented equivalent) is set to a valid IANA zone, when computing today, then the date uses that zone | ADR today |
| AC-P-012 | Given status create without another day, when saved via domain rules, then `status_day` equals `instance_today()` | PRD AC-002.2 |
| AC-P-013 | Given rows only on a prior calendar day, when listing today, then those rows are excluded | PRD AC-004.3 |

## Evidence log

### Repo state after #2

| Finding | Evidence |
|---------|----------|
| Schema + repo exist | [src/pulseboard/db.py](../../../../src/pulseboard/db.py), [repository.py](../../../../src/pulseboard/repository.py), [models.py](../../../../src/pulseboard/models.py) |
| `status_day` storage | ISO `YYYY-MM-DD` **text**; callers must supply day — repository does **not** compute today |
| `upsert_status` / `list_statuses_for_day` | Require explicit `status_day: str`; filter is equality on stored day |
| Env pattern established | `PULSEBOARD_DB_PATH` in `db.py` — same style for `PULSEBOARD_TZ` |
| No today/TZ module yet | Grep: no `instance_today` / `PULSEBOARD_TZ` in `src/` |
| Tests | [tests/test_status_repository.py](../../../../tests/test_status_repository.py) uses fixed date strings |
| Runtime deps | [pyproject.toml](../../../../pyproject.toml) still `dependencies = []` — stdlib only preferred |
| FastAPI app | Still absent — #6 is pure helper, not HTTP |

### Product / architecture constraints

| Source | Constraint relevant to #6 |
|--------|---------------------------|
| ADR today-instance-timezone | Single instance TZ; default **host local**; optional IANA env (e.g. `PULSEBOARD_TZ`); persist calendar date; board = `status_day == instance_today()` |
| PRD FR-007 | Default day is today; board default today |
| PRD AC-002.2 | Create without choosing another day → day is instance today |
| PRD AC-004.3 | Prior calendar day rows excluded from today list |
| Status domain ADR | `status_day` default = instance today; edits when day == instance today (later API) |
| #2 research/plan | Explicitly deferred TZ logic out of repository |

### Explicit non-goals for this issue

* FastAPI routes, cookies, HTMX
* Changing SQLite schema
* Full product upsert validation (empty fields) — #5
* HTTP list endpoint — #3 (will **call** this helper)
* Runbook prose — #8 (document env name in module docstring)
* Per-user TZ, geo, multi-day history UI

## Semantic split of acceptance criteria

| AC | What #6 must deliver now | What may complete when callers land |
|----|--------------------------|-------------------------------------|
| AC-P-010 | Helper returns host-local calendar date when env unset | Unit tests with controlled “now” / TZ |
| AC-P-011 | Helper honors valid `PULSEBOARD_TZ` IANA name | Unit tests with fixed instants across zones |
| AC-P-012 | **Domain defaulting helper or thin wrapper** that supplies `instance_today()` as `status_day` when create omits day | Full HTTP create path is #5; #6 should still expose a clear default so #5 does not re-implement TZ |
| AC-P-013 | Document/contract: list today = `list_statuses_for_day(conn, instance_today())`; optional thin `list_statuses_for_today(conn)` | #3 wires board; #6 can add convenience + test that prior-day rows are excluded when filtering by `instance_today()` |

**Research recommendation:** Implement core `instance_today` (+ zone resolution + injectable clock) fully. For AC-P-012/013, add **small composition helpers** that use #2 repository without owning HTTP:

* e.g. `default_status_day() -> str` alias or ensure create-default is `instance_today().isoformat()`
* e.g. `list_statuses_for_today(conn, *, today: date \| None = None) -> list[Status]` calling `list_statuses_for_day(conn, day_str)` where `day_str` comes from `instance_today()`

That satisfies “all MVP create defaults and today-board filters use this helper” without starting #3/#5.

## Design options

### Return type

| Option | Pros | Cons | Fit |
|--------|------|------|-----|
| `datetime.date` | Type-safe; ADR “calendar date” | Callers need `.isoformat()` for SQLite text | **Preferred** — convert at repo boundary |
| `str` YYYY-MM-DD | Matches DB column directly | Easier to pass wrong format | Acceptable alternative |
| `datetime` | Too much | Time-of-day noise | Reject |

**Selected:** return `datetime.date` from `instance_today()`; provide `format_status_day(d: date) -> str` or use `date.isoformat()` at call sites (ISO is YYYY-MM-DD).

### Timezone resolution (stdlib)

Python 3.12+ (project requires >=3.12):

* `datetime.now().astimezone().tzinfo` — host local zone
* `ZoneInfo(key)` from `zoneinfo` (stdlib) for IANA names
* Invalid IANA: raise clear error or fall back? **Recommend raise `ValueError`** on invalid `PULSEBOARD_TZ` so misconfig is obvious (document in plan); optional fallback to host local is weaker for ops

### Clock injection (tests)

| Option | Notes |
|--------|-------|
| **A. Optional `now: datetime \| None` param** | `instance_today(*, now=None, tz=None)` — simple, explicit |
| **B. Module-level clock callable** | `get_now = datetime.now` overridable — global state |
| **C. Small `Clock` protocol / class** | Clean DI; slightly more code |

**Selected:** **A** with optional overrides:

```text
instance_today(*, now: datetime | None = None, tz: ZoneInfo | tzinfo | None = None) -> date
```

* If `tz` is None → resolve from env / host local
* If `now` is None → `datetime.now(tz=resolved_tz)` (aware)
* If `now` naive → treat carefully: prefer require aware in tests, or attach resolved tz

Also expose `resolve_instance_tz() -> ZoneInfo | tzinfo` for reuse and testing AC-P-010/011 without date math confusion.

### Env var

* Name: **`PULSEBOARD_TZ`** (ADR + issue text)
* Value: IANA string e.g. `America/Los_Angeles`, `UTC`, `Asia/Kolkata`
* Unset/empty → host local
* Mirror `PULSEBOARD_DB_PATH` style in docstrings for #8

### Module layout

| Option | Path | Fit |
|--------|------|-----|
| **A. New module** | `src/pulseboard/today.py` or `timeutil.py` | Clear separation from db/repository — **preferred** |
| B. Stuff into `db.py` | Couples path config with calendar | Avoid |
| C. Methods on repository | Mixes persistence with clock | Avoid |

**Selected:** `src/pulseboard/today.py` with:

* `ENV_TZ = "PULSEBOARD_TZ"`
* `resolve_instance_tz() -> tzinfo`
* `instance_today(...) -> date`
* optional `list_statuses_for_today(conn, ...)` in `today.py` or thin wrapper in `repository.py` that imports `instance_today` — prefer **wrapper in repository or today module** that imports list from repository to avoid circular imports: put pure TZ in `today.py`; put `list_statuses_for_today` in `repository.py` importing `instance_today`.

Circular-import note: `repository` must not import heavy app; `today` must not import `repository` if repository imports today — so:

* `today.py` — pure clock/TZ only
* `repository.py` — add optional `list_statuses_for_today` importing from `today`
* create default for #5: callers call `instance_today().isoformat()` or a one-liner in a future service layer

For AC-P-012 without #5: add a documented helper e.g. `default_status_day_str() -> str` in `today.py` returning `instance_today().isoformat()`, and a test that “domain default equals instance_today”. Full “when saved” path remains #5 wiring that helper.

### Dependencies

* **No new packages** — `zoneinfo` is stdlib on 3.12
* On some minimal platforms `tzdata` package is needed for IANA; Linux usually has system tz data. Note as risk; only add `tzdata` dep if tests fail in CI without it

## Testing strategy for #6

New file e.g. `tests/test_instance_today.py` (and optional extension of repository tests).

| Test idea | AC |
|-----------|-----|
| No env: `instance_today(now=fixed_local_aware)` matches `now.date()` in host/local tz | AC-P-010 |
| Monkeypatch/clear `PULSEBOARD_TZ`; compare to `datetime.now().astimezone().date()` for “live” smoke (optional flaky near midnight — prefer fixed `now`) | AC-P-010 |
| Set `PULSEBOARD_TZ=Pacific/Kiritimati` vs `UTC` with same UTC instant → different calendar dates when near boundary | AC-P-011 |
| Invalid TZ raises | ops clarity |
| `default_status_day_str()` == `instance_today().isoformat()` | AC-P-012 contract |
| Seed prior-day + today rows; `list_statuses_for_today` / filter by `instance_today()` excludes prior | AC-P-013 |

Use `monkeypatch.setenv` / `delenv` for `PULSEBOARD_TZ`.

## Dependencies on other issues

| Issue | Relationship |
|-------|----------------|
| #2 | **Done** — stores/filters by `status_day` text; no blocker |
| #5 | Will default create day via `instance_today()` |
| #3 | Will list with `instance_today()` |
| #9 | UI shows today board via #3 |
| #10 | May freeze clock in product tests |
| #8 | Documents `PULSEBOARD_TZ` |

## Risks and edge cases

| Risk | Mitigation |
|------|------------|
| Midnight flakiness in tests | Inject `now=`; never depend on wall clock alone for assertions |
| Invalid IANA name | Raise `ValueError` with clear message |
| Missing system tzdata | Document; add `tzdata` only if required |
| Host local in containers is UTC | Operator sets `PULSEBOARD_TZ`; docstring + later runbook |
| Naive datetime `now` | Prefer timezone-aware `now` in API docs; if naive, localize to resolved instance tz |
| AC-P-012/013 without HTTP | Composition helpers + unit tests; #5/#3 complete user journey |
| Scope creep into “edit only today” rules | Leave edit gate to #5 domain; #6 only provides the date |

## Open questions

| # | Question | Proposed default (no user ask) |
|---|----------|--------------------------------|
| Q1 | Return `date` or `str`? | **`date`** + `.isoformat()` at DB boundary |
| Q2 | Module name? | **`today.py`** |
| Q3 | Invalid `PULSEBOARD_TZ`? | **Raise `ValueError`** |
| Q4 | Implement `list_statuses_for_today` in #6? | **Yes** — thin wrapper for AC-P-013 |
| Q5 | Implement full create path for AC-P-012? | **No HTTP**; expose `default_status_day` / document that create uses `instance_today().isoformat()`; test the default helper |
| Q6 | New runtime deps? | **None** unless tzdata required |
| Q7 | FastAPI? | **No** |

**No blocking ambiguity.** No gap issue to file. #2 is not a blocker.

## Alternatives considered

| Alternative | Why not |
|-------------|---------|
| Always UTC date | ADR rejected for local standup mismatch |
| Browser-local today | Splits one board; ADR rejected |
| Compute today inside every SQL query | Harder to test; duplicates TZ rules |
| Third-party `pytz` | Unnecessary on 3.12 + zoneinfo |

## Success criteria for this research phase

* [x] TEMP-2 / #6 AC captured
* [x] ADR today + PRD links recorded
* [x] #2 patterns and non-coupling confirmed
* [x] Selected approach and test strategy documented
* [x] Open questions closed with defaults
* [x] No production code written
* [x] Artifact at `lifecycle/06-implementation/output/issue-06/research.md`

## Actionable next steps (Plan only)

1. Author `lifecycle/06-implementation/output/issue-06/plan.md` from this research.
2. Plan `today.py` API, env resolution, injection, tests for AC-P-010–013.
3. Plan thin `list_statuses_for_today` + default day string helper.
4. Exclude FastAPI, schema changes, #5/#3 HTTP, runbook.
5. User verifies Research in `issue-06/README.md` before `/rpi continue=2`.

## References

* [backlog-snapshot.md — TEMP-2](../../04-decomposition/output/backlog-snapshot.md)
* [ADR today timezone](../../03-product-definition/output/adr/2026-08-09-today-instance-timezone-v01.md)
* [ADR status domain](../../03-product-definition/output/adr/2026-08-09-status-domain-model-v01.md)
* [prd.md](../../03-product-definition/output/prd.md) — FR-007, AC-002.2, AC-004.3
* [issue-02 implement](../issue-02/implement.md) — repository contract
* [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py)
