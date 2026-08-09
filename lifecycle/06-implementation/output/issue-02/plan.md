---
title: "Issue #2 plan — SQLite schema and status repository"
description: Implementation plan for PulseBoard TEMP-1 / GitHub #2 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-02
  - sqlite
  - plan
  - rpi
estimated_reading_time: 7
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#2](https://github.com/AbhranilGit/HVE-Core-Course/issues/2) — api: SQLite schema and status repository for today |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-1** |
| Phase | Plan only (`/rpi continue=2`) |
| Status | Complete — ready for Implement gate |
| Based on | [research.md](research.md) (complete; Status Complete — ready for Plan gate) |
| Production code | **None** (this phase) |
| Sprint | 1 of 6 (first Sprint 1 issue) |

## User requests (this phase)

1. Plan implementation of PulseBoard issue #2 (TEMP-1) only.
2. Do not implement yet.
3. Base the plan on completed `lifecycle/06-implementation/output/issue-02/research.md`.
4. Include steps, files to touch, acceptance checks from the local issue spec, and risks.
5. Stay inside this issue’s scope.
6. Write the plan to `lifecycle/06-implementation/output/issue-02/plan.md`.

## Objectives

Deliver local SQLite persistence and a small repository API so status rows survive process restart and siblings (#3, #5, #10) can upsert and list by day — without FastAPI routes, identity cookies, `instance_today`, HTMX, or runbook prose.

## Alignment with research (no contradictory inventions)

| Research decision | Plan adoption |
|-------------------|---------------|
| stdlib `sqlite3`; no new runtime deps | Yes |
| Table `statuses`; UNIQUE(display_name, status_day) | Yes |
| `status_day` ISO `YYYY-MM-DD` text | Yes |
| Optional but recommended `created_at` / `updated_at` (UTC ISO) | Yes — include both |
| Surrogate `id INTEGER PRIMARY KEY AUTOINCREMENT` + unique pair | Yes |
| Text fields `NOT NULL DEFAULT ''` | Yes |
| `init_db` + upsert + list-by-day (+ optional get) | Yes — include get for tests |
| Upsert via `INSERT ... ON CONFLICT DO UPDATE` | Yes |
| List order `ORDER BY display_name COLLATE NOCASE` | Yes |
| `PULSEBOARD_DB_PATH` + default `data/pulseboard.db` (cwd-relative) | Yes |
| No FastAPI app shell in #2 | Yes — callable `init_db` only |
| Minimal repo validation; empty-field rules → #5 | Yes — only reject blank `display_name` at repo boundary (optional thin guard) |
| Narrow persistence tests in #2; full suite → #10 | Yes |
| Package split Option B if clearer | Yes — `db.py`, `models.py`, `repository.py` |
| No timezone / today computation in repository | Yes — callers pass `status_day` |

**Intentional deltas from research:** none. Layout chooses Option B explicitly for sibling clarity.

## Design summary

### Schema (DDL)

```sql
CREATE TABLE IF NOT EXISTS statuses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  display_name TEXT NOT NULL,
  status_day TEXT NOT NULL,  -- YYYY-MM-DD
  doing TEXT NOT NULL DEFAULT '',
  blocked TEXT NOT NULL DEFAULT '',
  next TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  UNIQUE (display_name, status_day)
);
```

### Public API (planned)

| Symbol | Module | Behavior |
|--------|--------|----------|
| `DEFAULT_DB_FILENAME` / path helpers | `db.py` | Default relative path `data/pulseboard.db` |
| `resolve_db_path(path: str \| Path \| None = None) -> Path` | `db.py` | Explicit path wins; else `PULSEBOARD_DB_PATH`; else default |
| `connect(path: str \| Path) -> sqlite3.Connection` | `db.py` | `sqlite3.connect`; `row_factory = sqlite3.Row` optional |
| `init_db(path: str \| Path \| None = None) -> Path` | `db.py` | Resolve path; `mkdir` parents; connect; execute DDL; commit; return path used |
| `@dataclass Status` | `models.py` | `display_name`, `status_day`, `doing`, `blocked`, `next`, optional `id`, `created_at`, `updated_at` |
| `upsert_status(conn, *, display_name, status_day, doing="", blocked="", next="") -> Status` | `repository.py` | ON CONFLICT update fields + `updated_at`; set `created_at` on insert |
| `list_statuses_for_day(conn, status_day: str) -> list[Status]` | `repository.py` | Filter by day; stable name order |
| `get_status(conn, display_name, status_day) -> Status \| None` | `repository.py` | Single-row read |

Connection policy: callers (tests, later FastAPI deps) open via `connect` after `init_db`, or `init_db` may return path only and tests call `connect` — prefer **`init_db` ensures schema**, then **`connect(path)`** for short-lived connections; repository functions take an open `Connection` so tests control lifecycle.

Timestamps: `datetime.now(timezone.utc).isoformat()` (or equivalent) at write time.

### Configuration

* Env: `PULSEBOARD_DB_PATH` (string filesystem path).
* Default: `Path("data") / "pulseboard.db"` resolved against process cwd unless overridden.
* Module docstring notes env + default for #8 runbook later.
* No cloud DSN API.

## Implementation steps

Execute in order during `/rpi continue=3`. Do **not** start #6/#4/#5/#3/#9 or Sprint 2 work.

### Step 1 — Domain model

<!-- parallelizable: false -->

1. Add `src/pulseboard/models.py` with frozen or mutable `@dataclass Status`.
2. Fields match schema; `status_day` typed as `str` (ISO date) for simplicity at DB boundary.
3. Optional helper `status_from_row(row) -> Status` can live in `repository.py` or `models.py`.

### Step 2 — Connection and schema init

<!-- parallelizable: false -->

1. Add `src/pulseboard/db.py`.
2. Implement `resolve_db_path`, `connect`, `init_db` as above.
3. `init_db` creates parent directories; runs `CREATE TABLE IF NOT EXISTS`; commits.
4. Document `PULSEBOARD_DB_PATH` and default in module docstring.
5. Do not add WAL/PRAGMA beyond optional `foreign_keys` if desired — not required for AC.

### Step 3 — Repository

<!-- parallelizable: false -->

1. Add `src/pulseboard/repository.py`.
2. Implement `upsert_status` with `INSERT ... ON CONFLICT(display_name, status_day) DO UPDATE SET doing=excluded.doing, blocked=excluded.blocked, next=excluded.next, updated_at=excluded.updated_at` (keep original `created_at` on conflict — set `created_at=excluded.created_at` only on insert; on update do not overwrite `created_at`).
3. Implement `list_statuses_for_day` and `get_status`.
4. Thin guard: if `display_name` is empty/whitespace after strip, raise `ValueError` (helps AC clarity; full product validation remains #4/#5).
5. Do **not** reject all-empty doing/blocked/next here (#5).
6. Do **not** call `instance_today` or read cookies.

### Step 4 — Package exports (minimal)

<!-- parallelizable: false -->

1. Update `src/pulseboard/__init__.py` only if useful to re-export `init_db`, `Status`, repository functions — optional; avoid heavy public API churn. Prefer importing from submodules in tests.

### Step 5 — Narrow persistence tests

<!-- parallelizable: false -->

1. Add `tests/test_status_repository.py` (name flexible).
2. Use `tmp_path` for isolated DB files; call `init_db(tmp_path / "test.db")`.
3. Cases:
   * **AC-P-001:** after `init_db`, upsert + get or list succeeds (schema usable).
   * **AC-P-002:** two upserts same name+day → `COUNT(*) == 1` and latest field values.
   * **AC-P-003:** upsert; close connection; new `connect` same path; row still readable.
   * **AC-P-004:** resolved path is a filesystem path; after init, `Path.is_file()` true (local file DB).
4. Optional: list two different names same day → two rows; list other day → empty/not included (helps #3 without owning #10).
5. Run `pytest` (dev extra); fix until green.

### Step 6 — Implement summary and AC evidence

<!-- parallelizable: false -->

1. Write `lifecycle/06-implementation/output/issue-02/implement.md` with files changed, commands run, AC results, deviations.
2. Note `.copilot-tracking/` session evidence if written.
3. Confirm no FastAPI/UI/today/identity/runbook scope creep.

### Step 7 — Validation gate

<!-- parallelizable: false -->

1. `pytest` passes for new tests.
2. No new runtime dependencies in `pyproject.toml` unless absolutely required (plan expects **none**).
3. Mark Implement checklist in `issue-02/README.md` only after AC met.

## Files to touch

| Path | Action | Notes |
|------|--------|-------|
| [src/pulseboard/models.py](../../../../src/pulseboard/models.py) | **Add** | `Status` dataclass |
| [src/pulseboard/db.py](../../../../src/pulseboard/db.py) | **Add** | path resolve, connect, init_db, DDL |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | **Add** | upsert, list_by_day, get |
| [src/pulseboard/__init__.py](../../../../src/pulseboard/__init__.py) | **Maybe edit** | optional re-exports only |
| [tests/test_status_repository.py](../../../../tests/test_status_repository.py) | **Add** | AC-P-001–004 narrow tests |
| [lifecycle/06-implementation/output/issue-02/implement.md](implement.md) | **Edit** | phase-3 summary |
| [pyproject.toml](../../../../pyproject.toml) | **No change expected** | keep `dependencies = []`; pytest already in dev |
| FastAPI / templates / routes | **Do not add** | deferred |
| Runbook / README ops | **Do not add** | #8 |

## Acceptance checks

| ID | Criterion (TEMP-1) | How we will verify |
|----|--------------------|--------------------|
| AC-P-001 | Configured local DB path → init → schema usable for writes/reads | Test: `init_db(tmp_path/...)` then upsert + read; manual: inspect file exists |
| AC-P-002 | Two writes same display_name + status_day → one row | Test: double upsert; `SELECT COUNT(*)` == 1; values = second write |
| AC-P-003 | Data survives “restart” (new connection / re-open same file) | Test: write; close; reconnect same path; assert row |
| AC-P-004 | File-local SQLite, not required cloud DB | Design: `sqlite3` + filesystem path only; test: `Path.is_file()` after init; no network DSN |

### Scope checks (negative)

| Check | Verify |
|-------|--------|
| No cloud/Postgres | Code review: only `sqlite3` + path |
| No multi-day history UI | No UI modules |
| No app UI | No templates/HTMX |
| No `instance_today` | No TZ helper module in this issue |
| No identity cookies | No auth module |
| Empty doing/blocked/next still writable at DB | No CHECK rejecting empty triple in DDL |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Overwriting `created_at` on upsert | ON CONFLICT updates only doing/blocked/next/updated_at |
| Missing parent directory for DB path | `path.parent.mkdir(parents=True, exist_ok=True)` in `init_db` |
| Connection leaks in tests | `with connect(...) as conn:` or explicit close in fixtures |
| Case-variant display names as different people | Accept per research (trusted team); no COLLATE unique |
| Scope creep into FastAPI | Explicit non-goal; init callable satisfies “app initializes” |
| Stealing #10 test scope | Keep tests persistence-only; no HTTP client tests |
| `next` SQL keyword | Quote column as `"next"` in SQL identifiers |

## Out of scope (do not implement in #2)

* FastAPI routes, lifespan app shell, uvicorn wiring
* Display-name cookie / identity UI (#4, #9)
* `instance_today` / `PULSEBOARD_TZ` (#6)
* HTTP upsert/list endpoints (#5, #3)
* HTMX board (#9)
* Full create/list product suite and release docs (#10, #8, #7)
* SQLAlchemy, migrations frameworks, Postgres, cloud DB
* Blocked flag, multi-status-per-day, history UI

## Dependencies

| Depends on | Status |
|------------|--------|
| Research.md complete | Done |
| Other GitHub issues | **None** for #2 |
| Unblocks | #5 (upsert caller), #3 (list caller), #10 (tests extend), later app startup |

## Success criteria for Implement phase

* [ ] Schema + repository modules land under `src/pulseboard/`
* [ ] AC-P-001–004 covered by automated narrow tests and passing
* [ ] No new runtime dependencies required
* [ ] `implement.md` records evidence and any deviations
* [ ] No production work on sibling issues

## Ready for implement?

- [x] Plan filled (steps, files, AC checks, risks)
- [x] Plan matches `research.md` (no contradictory findings)
- [x] Scope is this issue only
- [ ] User verifies Plan section in [`README.md`](README.md) before `/rpi continue=3`

## Next command (after Plan gate)

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #2 (TEMP-1) only. ...
```

See [issue-02.md](../../prompt/issue-02.md) Phase 3 prompt for full text.

## References

* [research.md](research.md)
* [backlog-snapshot.md — TEMP-1](../../04-decomposition/output/backlog-snapshot.md)
* [sprint-plan.md](../../05-sprint-planning/output/sprint-plan.md)
