---
title: "Issue #2 research — SQLite schema and status repository"
description: Research-only findings for PulseBoard TEMP-1 / GitHub #2 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-02
  - sqlite
  - research
  - rpi
estimated_reading_time: 8
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#2](https://github.com/AbhranilGit/HVE-Core-Course/issues/2) — api: SQLite schema and status repository for today |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-1** |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete — ready for Plan gate |
| Production code | **None** (this phase) |
| Sprint | 1 of 6 (first Sprint 1 issue) |

## Scope summary (authoritative)

From TEMP-1 / #2:

**In scope**

* Status table (or equivalent) with: `display_name`, `status_day`, `doing`, `blocked`, `next`; optional `created_at` / `updated_at`
* Unique constraint on `(display_name, status_day)`
* Schema initialize on startup (simple path OK)
* Repository / data-access helpers for upsert and list-by-day (callers may land in sibling issues)
* Default / configurable DB file path suitable for local run and tests (temp DB in tests)

**Out of scope**

* Cloud DB, Postgres, multi-tenant schemas, replication
* Multi-day history UI
* Application UI (see #9)

**Acceptance criteria (must drive plan)**

| ID | Criterion | PRD / ADR link |
|----|-----------|----------------|
| AC-P-001 | Given a configured local DB path, when the app initializes, then the status schema exists and is usable for writes/reads | FR-008 |
| AC-P-002 | Given two writes with the same display_name and status_day, when persisted, then only one row exists for that pair (unique enforced) | FR-004, status domain ADR |
| AC-P-003 | Given data written to the DB file, when the process restarts against the same file, then prior rows remain readable | AC-006.1 |
| AC-P-004 | Persistence is file-local SQLite (or equivalent local file DB), not a required cloud database | AC-006.2 |

## Evidence log

### Repo layout and package state

| Finding | Evidence |
|---------|----------|
| App package is a stub | [`src/pulseboard/__init__.py`](../../../../src/pulseboard/__init__.py) — version only; no `db`, `models`, or routes |
| Tests empty | [`tests/`](../../../../tests/) — `.gitkeep` only |
| Scripts empty | [`scripts/`](../../../../scripts/) — `.gitkeep` only |
| Packaging | [`pyproject.toml`](../../../../pyproject.toml) — `requires-python >=3.12`, package under `src/`, **no runtime deps yet**; optional `dev`: `pytest>=8`; `pythonpath = ["src"]` for pytest |
| DB files ignored | [`.gitignore`](../../../../.gitignore) — `*.db`, `*.sqlite3` |
| Stack intent named | README + web-stack ADR: Python 3.12+, FastAPI, SQLite, HTMX; uvicorn for local run later |
| Sprint order | [#2 first](../../05-sprint-planning/output/sprint-plan.md); no hard deps on other issues |
| Sibling consumers | #5 upsert, #3 list-by-day, #10 tests, #6 day defaulting (status_day values) |

### Product / architecture constraints

| Source | Constraint relevant to #2 |
|--------|---------------------------|
| PRD FR-008 / US-006 | Status data survives process restart on same machine/DB file |
| PRD AC-006.1 / AC-006.2 | Restart retains rows; local file DB, not required cloud |
| PRD NFR-002 | Create/update either persists or clear failure (repo should not silent-drop) |
| ADR SQLite | Single host DB file; one process owns one file; default path or `PULSEBOARD_DB_PATH`; schema on startup OK; unique `(display_name, status_day)`; prefer smallest SQL access that keeps tests clear |
| ADR status domain | Entity fields + unique key; upsert semantics; optional audit timestamps; validation of empty fields is **domain/API** (sibling #5), not necessarily DB CHECK |
| ADR today TZ | Persist `status_day` as **calendar date**; day membership uses that column (instance_today from #6 supplies values; #2 stores/filters by date) |
| ADR web stack | Package under `src/pulseboard/`; FastAPI later; pytest for create/list (#10) |

### Explicit non-goals for this issue

* Implementing FastAPI routes, cookies, HTMX, or `instance_today()` logic
* Full product validation of empty-field rules (belongs with #5)
* Runbook prose (#8) — only leave a path hook env vars can document later
* Cloud/multi-tenant/history UI

## Domain model for persistence

Recommended column mapping (from status domain ADR + TEMP-1):

| Column | Type (SQLite) | Notes |
|--------|---------------|-------|
| `display_name` | `TEXT NOT NULL` | Part of unique key; trim/blank rules enforced by callers (#4/#5) |
| `status_day` | `TEXT NOT NULL` | ISO calendar date `YYYY-MM-DD` (portable; matches calendar-date ADR) |
| `doing` | `TEXT NOT NULL DEFAULT ''` | Plain text; empty allowed at DB layer |
| `blocked` | `TEXT NOT NULL DEFAULT ''` | Free text only; no boolean flag |
| `next` | `TEXT NOT NULL DEFAULT ''` | Plain text; empty allowed at DB layer |
| `created_at` | `TEXT` or `TEXT NOT NULL` | Optional but **recommended** (ADR); store UTC ISO timestamps |
| `updated_at` | `TEXT` or `TEXT NOT NULL` | Optional but **recommended**; bump on upsert |

**Unique constraint:** `UNIQUE (display_name, status_day)` — mechanical enforcement of AC-P-002.

**Primary key options:** composite PK on the unique pair, or surrogate `id INTEGER PRIMARY KEY` plus unique index. Surrogate is slightly nicer for debugging; composite is simpler. Either satisfies AC.

**No blocked flag column** in MVP (status domain ADR).

## Repository surface (for #2 and siblings)

TEMP-1 asks for helpers usable by later issues. Minimal surface that satisfies AC and unblocks #3/#5/#10:

| Operation | Purpose | Used by |
|-----------|---------|---------|
| `init_db` / `initialize_schema` | Create file path parent if needed; open connection; `CREATE TABLE IF NOT EXISTS`; enable useful PRAGMAs | App startup; tests |
| `get_connection` or connection factory | Open SQLite against configured path | Internal |
| `upsert_status(...)` | Insert or replace row for `(display_name, status_day)` | #5, #10 |
| `list_statuses_for_day(status_day)` | Return rows for one calendar day (stable order) | #3, #9, #10 |
| Optional: `get_status(display_name, status_day)` | Single-row read | Tests / #5 |

**Ordering:** ADR allows any deterministic order; research recommendation: `ORDER BY display_name COLLATE NOCASE` (or plain `display_name`) for stable boards.

**Upsert mechanics (options for plan):**

1. `INSERT ... ON CONFLICT(display_name, status_day) DO UPDATE SET ...`
2. Application-level select-then-insert/update

Prefer (1) with stdlib `sqlite3` — one round-trip, enforces uniqueness at DB.

**Validation boundary:** Repository may accept already-normalized strings. Rejecting “all three fields empty” and blank display names is product validation (#5 / #4). Plan should not overload #2 with full HTTP validation unless a thin guard is needed for internal safety.

## Configuration

| Concern | Finding | Recommendation for plan |
|---------|---------|-------------------------|
| Path env | ADR names `PULSEBOARD_DB_PATH` as example | Read env if set; else default relative path under project or cwd (e.g. `data/pulseboard.db` or `./pulseboard.db`) |
| Default path | Not fixed in docs yet (#8) | Pick one default; keep it overridable; document in module docstring for #8 |
| Tests | Temp DB required | Factory/`init_db(path)` accepting `pathlib.Path` or str; pytest can use `tmp_path` |
| Git | `*.db` ignored | Default path will not be committed — good |

## Access library options

ADR: prefer the smallest option that keeps create/list tests clear.

| Option | Pros | Cons | Fit for #2 |
|--------|------|------|------------|
| **stdlib `sqlite3`** | Zero new deps; matches empty `dependencies = []`; easy temp files; enough for one table | Manual SQL; no ORM models | **Selected** for MVP thinness |
| SQLAlchemy | Models, migrations later | New dependency; heavier for one table | Defer unless team standard forces it |
| raw SQL files + migrate tool | Formal migrations | Overkill vs ADR schema on startup | Not for MVP |

**Selected approach:** stdlib `sqlite3` + small repository module(s) under `src/pulseboard/`. Add FastAPI/uvicorn only when a later issue needs them (#4/#5/#9) — **not required to close #2 AC** if init + repo are unit-testable without ASGI.

## Package structure options

No existing modules beyond `__init__.py`. Candidate layouts for plan:

**Option A — flat (minimal)**

```text
src/pulseboard/
  __init__.py
  db.py          # path config, connect, init schema, repo functions
```

**Option B — split (clearer for siblings)**

```text
src/pulseboard/
  __init__.py
  db.py          # connection + init_schema
  models.py      # dataclass Status (optional)
  repository.py  # upsert + list_by_day
```

**Recommendation:** Option B if more than ~100 lines; Option A acceptable for first thin cut. Prefer a `Status` dataclass (or `NamedTuple`) so #3/#5 do not pass bare tuples forever.

**FastAPI lifespan:** Optional for #2. AC-P-001 says “when the app initializes” — a callable `init_db(path)` invoked from tests and later from app startup satisfies the criterion without shipping full ASGI yet. Plan may either:

1. Ship `init_db` only (+ note wiring in later issues), or
2. Add a minimal FastAPI app with lifespan that calls `init_db`.

Research preference: **(1)** keep #2 focused on persistence; document the startup hook. If implementor prefers a one-line FastAPI shell for realism, keep it empty of routes.

## Testing strategy for this issue (not full #10)

#10 owns the formal create/list product test suite. For #2, research recommends **narrow persistence tests** (can live under `tests/` now or wait until implement) that lock AC without stealing #10 scope:

| Test idea | Maps to |
|-----------|---------|
| init creates usable schema on a temp path | AC-P-001 |
| two upserts same name+day → one row, last values win | AC-P-002 |
| write, new connection/re-open same file, read back | AC-P-003 |
| path is a local file (not a network DSN API) | AC-P-004 (design + docs/assert file exists) |

Full HTTP create/list and prior-day board scenarios remain #10 / #3 / #5.

## Dependencies on other issues

| Issue | Relationship to #2 |
|-------|--------------------|
| #6 instance today | **Not a blocker.** #2 stores `status_day`; callers pass a date. Do not embed timezone logic in the repository. |
| #4 identity | Callers supply `display_name`; no cookie code here. |
| #5 upsert API | Will call repository upsert + validation. |
| #3 list API | Will call list-by-day. |
| #9 UI | No UI in #2. |
| #10 tests | Builds on repo; may extend tests started in #2. |
| #8 runbook | Documents `PULSEBOARD_DB_PATH` / default path later. |

## Risks and edge cases

| Risk | Mitigation in plan/implement |
|------|------------------------------|
| Display name case/spacing duplicates (`Ada` vs `ada`) | Product treats display name as plain text key; do not add case-fold uniqueness unless PRD says so. Document as trusted-team model. |
| Concurrent writers (shared lab) | ADR accepts SQLite locking at 5–15 users; enable `WAL` optional later, not required for AC. |
| Path directory missing | `init_db` should create parent directories for the DB file path. |
| Connection lifecycle | Prefer short-lived connections or documented single-connection rules; avoid leaking connections in tests. |
| Schema drift later | `CREATE TABLE IF NOT EXISTS` only — no alter migrations in MVP; acceptable per ADR. |
| Empty-string vs NULL | Prefer NOT NULL DEFAULT '' for text fields so list UI never sees NULL surprises. |
| Clock/timezone in repo | Do not compute “today” inside repository; accept `date` / ISO string from caller. |

## Open questions

Resolved by research where possible; remainder for Plan (no user block unless product change):

| # | Question | Proposed default (no user ask needed) |
|---|----------|----------------------------------------|
| Q1 | stdlib `sqlite3` vs SQLAlchemy? | **stdlib** |
| Q2 | Surrogate `id` vs composite PK? | Either; prefer `id INTEGER PRIMARY KEY AUTOINCREMENT` + UNIQUE(name, day) |
| Q3 | Must #2 add FastAPI app shell? | **No** for AC; `init_db` + repo enough |
| Q4 | Default DB path string? | e.g. `data/pulseboard.db` under cwd; overridable via `PULSEBOARD_DB_PATH` |
| Q5 | How much validation in repository? | Minimal: rely on UNIQUE; optional assert non-empty name at repo boundary; field emptiness → #5 |
| Q6 | Include persistence unit tests in #2? | **Yes, recommended** (narrow AC tests); does not replace #10 |
| Q7 | Table name? | `statuses` (plural, clear) |

**No blocking ambiguity** that requires asking the user before Plan. No gap issue needs filing.

## Alternatives considered (persistence design)

| Alternative | Why not selected |
|-------------|------------------|
| In-memory dict only | Fails AC-P-003 / US-006 |
| JSON file store | Weaker uniqueness; ADR chose SQLite |
| SQLAlchemy + Alembic | Heavier than ADR allows for MVP |
| Defer repository to #5/#3 | TEMP-1 explicitly includes helpers; would stall clear AC and thin path |

## Success criteria for this research phase

* [x] TEMP-1 / #2 AC captured as planning drivers
* [x] ADR + PRD constraints for SQLite and status shape recorded
* [x] Repo patterns (empty package, pyproject, gitignore) noted
* [x] Selected approach and options documented
* [x] Open questions closed with defaults or marked non-blocking
* [x] No production code written
* [x] Artifact saved to `lifecycle/06-implementation/output/issue-02/research.md`

## Actionable next steps (Plan phase only — do not implement yet)

1. Author `lifecycle/06-implementation/output/issue-02/plan.md` from this research.
2. Plan modules: connection/init, schema DDL, `Status` type, upsert, list-by-day, path config.
3. Plan narrow tests for AC-P-001–004.
4. Explicitly exclude FastAPI routes, cookies, `instance_today`, HTMX, runbook.
5. User verifies Research checklist in [`README.md`](README.md) before `/rpi continue=2`.

## References

* [backlog-snapshot.md — TEMP-1](../../04-decomposition/output/backlog-snapshot.md)
* [prd.md](../../03-product-definition/output/prd.md) — FR-008, US-006, AC-006.*, NFR-002
* [ADR SQLite](../../03-product-definition/output/adr/2026-08-09-sqlite-local-persistence-v01.md)
* [ADR status domain](../../03-product-definition/output/adr/2026-08-09-status-domain-model-v01.md)
* [ADR today timezone](../../03-product-definition/output/adr/2026-08-09-today-instance-timezone-v01.md) (status_day as calendar date only)
* [ADR web stack](../../03-product-definition/output/adr/2026-08-09-web-stack-fastapi-htmx-v01.md)
* [sprint-plan.md](../../05-sprint-planning/output/sprint-plan.md)
* [pyproject.toml](../../../../pyproject.toml), [src/pulseboard/__init__.py](../../../../src/pulseboard/__init__.py)
