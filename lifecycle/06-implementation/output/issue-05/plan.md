---
title: "Issue #5 plan — upsert today status (doing / blocked / next)"
description: Implementation plan for PulseBoard TEMP-4 / GitHub #5 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-05
  - upsert
  - status
  - plan
  - rpi
estimated_reading_time: 7
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) — api: upsert today status (doing / blocked / next) |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-4** |
| Phase | Plan only (`/rpi continue=2`) |
| Status | Complete — ready for Implement gate |
| Based on | [research.md](research.md) (complete; Status Complete — ready for Plan gate) |
| Production code | **None** (this phase) |
| Sprint | 4 of 6 (Sprint 1) |
| Depends on | #2, #6, #4 in place (no blocker per research) |

## User requests (this phase)

1. Plan implementation of PulseBoard issue #5 (TEMP-4) only.
2. Do not implement yet.
3. Base the plan on completed `lifecycle/06-implementation/output/issue-05/research.md`.
4. Also use TEMP-4 / #5 scope from `backlog-snapshot.md`.
5. Leave list API to #3 and UI to #9.
6. Include steps, files to touch, acceptance checks, and risks.
7. Stay inside this issue’s scope.
8. Write the plan to `lifecycle/06-implementation/output/issue-05/plan.md`.

## Objectives

Replace the identity-only `POST /status` stub with a real create-or-update of **today’s** status for the cookie display name: plain-text doing / blocked / next, ≥1 field non-empty after trim, day = `default_status_day_str()`, one row per name per day via existing repository upsert — without list HTTP (#3), HTMX board UI (#9), or lock-after-standup.

## Alignment with research (no contradictory inventions)

| Research decision | Plan adoption |
|-------------------|---------------|
| Option A: service + replace `POST /status` + `create_app(db_path=...)` | Yes |
| Reject service-only / full HTMX / SQLite CHECK-only / client `status_day` | Yes |
| Module `status_service.py` | Yes |
| `normalize_status_fields` + validate ≥1 non-empty | Yes |
| `upsert_today_status(...)` → `default_status_day_str` + `repository.upsert_status` | Yes |
| Full replace of three fields per successful POST | Yes |
| Form body `doing`, `blocked`, `next` | Yes (open Q1) |
| Success **200 JSON** Status-like dict | Yes (open Q2) |
| Lifespan `init_db` + app.state db path | Yes |
| No field validation inside repository | Yes |
| No list route; no board HTML | Yes |
| Keep `require_display_name` on `/status` | Yes |
| Update `test_identity` stub assertions | Yes (open Q5) |
| Skip `GET /status/me` | Yes (open Q4) |
| Injectable `now` on service (optional on HTTP) | Yes — service accepts `now`/`tz`; route uses defaults; tests call service and/or compare `default_status_day_str()` immediately (open Q3) |

**Intentional deltas from research:** none material.

## Design summary

### Service (`status_service.py`)

| Symbol | Behavior |
|--------|----------|
| `normalize_status_fields(doing: str, blocked: str, next: str) -> tuple[str, str, str]` | Strip each; return trimmed strings (may be empty individually) |
| `validate_status_fields(doing, blocked, next) -> tuple[str, str, str]` | Normalize then if all three empty → `ValueError` with clear message (e.g. at least one of doing, blocked, or next must be non-empty); else return triple |
| `upsert_today_status(conn, *, display_name: str, doing: str = "", blocked: str = "", next: str = "", now=None, tz=None) -> Status` | `doing, blocked, next = validate_status_fields(...)`; `day = default_status_day_str(now=now, tz=tz)`; return `upsert_status(conn, display_name=..., status_day=day, doing=..., blocked=..., next=...)` |

No lock parameters. No client-supplied `status_day` on the MVP HTTP path.

**Field replace rule:** Each successful call sets all three columns to the submitted trimmed values (empty string clears a field) provided ≥1 remains non-empty.

### App DB wiring (`app.py`)

| Piece | Behavior |
|-------|----------|
| `create_app(*, db_path: str \| Path \| None = None) -> FastAPI` | Resolve path: explicit arg else `resolve_db_path()`; store on `application.state.db_path` |
| Lifespan | On startup: `init_db(application.state.db_path)`; yield; no special shutdown required for SQLite file |
| `get_connection` dependency (or inline) | `connect(request.app.state.db_path)` per request; close after (contextlib / try/finally). Prefer short-lived connections. |
| Module `app = create_app()` | Unchanged entry for uvicorn; uses default DB path |

Identity routes (`GET/POST /identity`) unchanged in behavior.

### HTTP `POST /status` (replace stub)

| Concern | Behavior |
|---------|----------|
| Auth | `name = require_display_name(request)` first → 400 if missing |
| Input | Form: `doing: str = Form("")`, `blocked: str = Form("")`, `next: str = Form("")` |
| Persist | Open conn → `upsert_today_status(conn, display_name=name, doing=..., blocked=..., next=...)` |
| Success | **200** JSON: at least `display_name`, `status_day`, `doing`, `blocked`, `next` (optional `id`, timestamps). **Do not** return `status: not_implemented`. |
| Validation error | Catch `ValueError` from service → **400** JSON `detail` clear message |
| No day field | Do not accept `status_day` form field for MVP write path |
| No lock | Do not add lock query/body/route |

Helper to serialize `Status` → dict is fine inline or small function in `app.py` / service.

### Repository / schema / today / identity

| Module | Change |
|--------|--------|
| `repository.py` | **No required change** |
| `db.py` | **No schema change**; use `init_db` / `connect` / `resolve_db_path` |
| `today.py` | **No change** — call `default_status_day_str` |
| `identity.py` | **No change** — keep `require_display_name` |
| `models.py` | **No change** |
| New deps | **None expected** (fastapi/multipart already present) |

### Tests to update/add

| File | Action |
|------|--------|
| `tests/test_status_upsert.py` (new) | AC-P-030–034 + identity regression on real upsert |
| `tests/test_identity.py` | **Edit** — remove/adjust assertions that expect `not_implemented`; still assert no-cookie → 400; with cookie + valid fields → 200 and persisted fields (or move create-success to upsert tests only and leave identity test as: with cookie POST minimal valid doing → not 400 for identity). Prefer: identity tests keep AC-P-023 without cookie; change “with cookie stub” to POST `doing=x` and assert 200 + `display_name` (not `not_implemented`). |
| Existing repo/today tests | Must stay green |

## Implementation steps

Execute in order during `/rpi continue=3`. Do **not** start #3, #9, or Sprint 2.

### Step 1 — `status_service.py`

<!-- parallelizable: false -->

1. Add `src/pulseboard/status_service.py` with normalize/validate/`upsert_today_status` as above.
2. Unit-testable without HTTP (optional pure tests in upsert test module).

### Step 2 — App factory + lifespan + real `POST /status`

<!-- parallelizable: false -->

1. Extend `create_app(*, db_path=None)`.
2. Add lifespan `init_db`.
3. Replace stub `post_status` with form upsert + JSON response.
4. Update module docstring: status upsert is live; UI remains #9.
5. Keep identity routes; no list route; no HTMX board.

### Step 3 — Tests

<!-- parallelizable: false -->

1. Add `tests/test_status_upsert.py`:
   * **AC-P-030:** cookie Ada → POST doing non-empty → 200; `get_status` for `default_status_day_str()` has doing and display_name Ada.
   * **AC-P-031:** response `status_day == default_status_day_str()` (same process moment; optional `PULSEBOARD_TZ=UTC`).
   * **AC-P-032:** two POSTs different field values → `list_statuses_for_day` len 1; second values present.
   * **AC-P-033:** all empty / whitespace → 400; no row created; if prior row exists, unchanged when rejecting all-empty update.
   * **AC-P-034:** route paths / handler signature have no lock/standup_lock; optional source grep of app module.
   * **Identity:** POST `/status` without cookie → 400.
2. Update `tests/test_identity.py` for real upsert response (no `not_implemented`).
3. Fixture pattern: `db_path = tmp_path / "t.db"`; `app = create_app(db_path=db_path)`; `TestClient(app)`; assert via `connect(db_path)`.
4. Run full suite with hve-env 3.12.

### Step 4 — Implement summary

<!-- parallelizable: false -->

1. Write `lifecycle/06-implementation/output/issue-05/implement.md`.
2. `.copilot-tracking/changes/` entry.
3. Record AC results and any deviations.

### Step 5 — Validation gate

<!-- parallelizable: false -->

1. All tests pass.
2. No list-today HTTP; no HTMX board; no schema change; no lock control.
3. Stub `not_implemented` gone from `/status` success path.

## Files to touch

| Path | Action | Notes |
|------|--------|-------|
| [src/pulseboard/status_service.py](../../../../src/pulseboard/status_service.py) | **Add** | validate + upsert_today |
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | **Edit** | db_path factory, lifespan, real POST /status |
| [tests/test_status_upsert.py](../../../../tests/test_status_upsert.py) | **Add** | AC-P-030–034 |
| [tests/test_identity.py](../../../../tests/test_identity.py) | **Edit** | drop stub `not_implemented` expectations |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | **No change** | |
| [src/pulseboard/db.py](../../../../src/pulseboard/db.py) | **No change** | |
| [src/pulseboard/today.py](../../../../src/pulseboard/today.py) | **No change** | |
| [src/pulseboard/identity.py](../../../../src/pulseboard/identity.py) | **No change** | |
| [pyproject.toml](../../../../pyproject.toml) | **No change expected** | |
| List routes / HTMX board | **Do not add** | #3 / #9 |
| [lifecycle/06-implementation/output/issue-05/implement.md](implement.md) | **Edit** | phase-3 summary |

## Acceptance checks

| ID | Criterion (TEMP-4) | How we will verify |
|----|--------------------|--------------------|
| AC-P-030 | Valid name + ≥1 non-empty field → today status stored under name | TestClient + `get_status` |
| AC-P-031 | Create without other day → day is instance today | Response/`get_status` `status_day == default_status_day_str()` |
| AC-P-032 | Second submit → one updated row | Two POSTs; list-by-day length 1; latest values |
| AC-P-033 | All three empty/whitespace → reject write | 400; no blank row / prior unchanged |
| AC-P-034 | No lock-after-standup control | Route/source absence check |

### Scope checks (negative)

| Check | Verify |
|-------|--------|
| No list-today HTTP (#3) | No new GET list route |
| No HTMX board / status form page (#9) | No board templates |
| No client `status_day` / prior-day product | POST accepts only doing/blocked/next |
| No schema migration | `db.py` untouched |
| Identity still required | 400 without cookie |
| Repository field rules unchanged | validation only in service |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Scope creep #3/#9 | Explicit file/out-of-scope list |
| Break #4 tests on stub body | Step 3 updates `test_identity.py` |
| DB file in repo cwd during tests | Always `create_app(db_path=tmp_path/...)` |
| Midnight flake on today | Compare to `default_status_day_str()` in same test |
| Connection leaks | try/finally or context manager close |
| Lifespan + TestClient | Use `TestClient(app)` which runs lifespan in modern Starlette; verify in implement |
| Partial vs full field replace confusion | Document full replace; tests cover second POST overwriting fields |

## Out of scope (do not implement in #5)

* List statuses HTTP / board empty-state API (#3)
* HTMX today board and status form chrome (#9)
* Prior-day edit, history, multi-status per day
* Lock-after-standup, blocked flag/workflow, notifications, attachments
* SSO/passwords; schema redesign
* Runbook (#8); full #10 suite beyond upsert tests
* JSON-only alternate API (form is enough); `GET /status/me`

## Open questions resolved in this plan

| # | Resolution |
|---|------------|
| Body format | **Form** fields doing/blocked/next |
| Success shape | **200 JSON** status fields |
| Injectable now | Service supports `now`/`tz`; HTTP uses default clock |
| GET /status/me | **Skip** |
| test_identity | **Update** for real upsert |

## Ready to implement?

- [x] Research complete and used as sole factual base
- [x] TEMP-4 AC-P-030–034 mapped to concrete steps/tests
- [x] Files, risks, out-of-scope listed; list→#3, UI→#9
- [x] **No production code** in this phase
- [ ] User verifies Plan checklist in [`README.md`](README.md) before Implement (`continue=3`)

## Next

After Plan gate: `/rpi continue=3` implements this plan only; record results in `implement.md`.
