---
title: "Issue #5 research — upsert today status (doing / blocked / next)"
description: Research-only findings for PulseBoard TEMP-4 / GitHub #5 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-05
  - upsert
  - status
  - research
  - rpi
estimated_reading_time: 8
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) — api: upsert today status (doing / blocked / next) |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-4** |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete — ready for Plan gate |
| Production code | **None** (this phase) |
| Sprint | 4 of 6 (Sprint 1) |
| Depends on | #2 schema/repo, #6 today default, #4 identity — **all in place; no blocker** |

## Scope summary (authoritative)

From TEMP-4 / #5:

**In scope**

* Endpoint or service method to upsert status for `(display_name, instance_today())`
* Fields: doing, blocked, next (plain text)
* Validation: require display name; require at least one of three fields non-empty after trim
* Same-day update replaces values; does not insert a second row
* No lock-after-standup control

**Out of scope**

* Multiple statuses per person per day
* Prior-day edit product / history journal
* Blocked flag, notifications, attachments
* UI markup (ui issue may call this API) — full HTMX form chrome is #9

**Acceptance criteria (must drive plan)**

| ID | Criterion | PRD / ADR link |
|----|-----------|----------------|
| AC-P-030 | Given valid display name and no status for today, when I submit doing/blocked/next with at least one non-empty, then a status for today is stored under my display name | PRD AC-002.1, field rule |
| AC-P-031 | Given create without choosing another day, when saved, then day is instance today | PRD AC-002.2 |
| AC-P-032 | Given an existing today status for my display name, when I submit new values, then the board data shows one updated row (not a second row) | PRD AC-003.1, FR-004 |
| AC-P-033 | Given update/create where all three fields are empty/whitespace, when submitted, then the app rejects the write | PRD US-002 field rule, AC-003.2 |
| AC-P-034 | Given MVP, when searching for lock-after-standup, then no such control exists | PRD AC-003.3 |

## Evidence log

### Dependency status (#2, #6, #4)

| Dep | Status | What #5 reuses |
|-----|--------|----------------|
| #2 | In place | `init_db`, `connect`, `upsert_status`, `get_status`, `list_statuses_for_day`; UNIQUE `(display_name, status_day)` |
| #6 | In place | `default_status_day_str()` / `instance_today()` for `status_day` when create omits another day |
| #4 | In place | `require_display_name(request)`; cookie identity; stub `POST /status` **ready to replace** |

**Blocker check:** None. Repository already performs mechanical upsert without field-content validation (intentionally deferred to API). Identity gate already returns 400 without cookie. Day default helper exists and is tested.

### Repo state (current code)

| Finding | Evidence |
|---------|----------|
| Stub status route | [app.py](../../../../src/pulseboard/app.py) `POST /status` — identity only; body `status: not_implemented` |
| No DB in app lifespan | `create_app()` does not call `init_db` or open connections yet |
| Upsert API | [repository.py](../../../../src/pulseboard/repository.py) `upsert_status(conn, display_name=, status_day=, doing=, blocked=, next=)` — ON CONFLICT updates fields; preserves `created_at` |
| Field validation absent at repo | Docstring: empty doing/blocked/next **not** enforced at DB layer |
| Display name at repo | `_require_display_name` still private; identity uses `normalize_display_name` |
| Today default | [today.py](../../../../src/pulseboard/today.py) `default_status_day_str()` |
| Model | [models.py](../../../../src/pulseboard/models.py) `Status` dataclass |
| Env | `PULSEBOARD_DB_PATH`, `PULSEBOARD_TZ` |
| Deps | fastapi, uvicorn, python-multipart; dev httpx + pytest |
| Tests | identity, repository, instance_today — no real status HTTP upsert tests yet |
| UI | Identity HTML only; no status form page (#9) |

### Product / architecture constraints

| Source | Constraint relevant to #5 |
|--------|---------------------------|
| Status domain ADR | Upsert on `(display_name, status_day)`; ≥1 of doing/blocked/next non-empty after trim; no lock-after-standup; no blocked flag column; same-day edits allowed |
| PRD FR-002 / FR-003 / FR-004 | Create today; update same day; one row per name per day |
| PRD AC-002.1–002.2, AC-003.1–003.3 | Create under name; day = today; update replaces; reject all-empty; no lock control |
| PRD AC-002.4 | Missing identity blocks create — **already #4**; #5 must keep `require_display_name` |
| PRD NFR-002 | Persist or clear failure — no silent drop |
| Identity ADR | Cookie supplies display name; case-sensitive as entered |
| Today ADR | Default day = instance today via helper |
| Web-stack ADR | FastAPI routes; form or JSON OK; full HTMX board is #9 |
| TEMP-4 out of scope | UI markup — API/service sufficient; #9 may POST same endpoint |

### Explicit non-goals for this issue

* HTMX board + polished status form chrome (#9)
* List-today HTTP endpoint (#3) — optional read-back via `get_status` / repo in tests is fine
* Prior-day edit product, history, multi-status per day
* Lock-after-standup, blocked workflow, notifications, attachments
* SSO/passwords; schema redesign
* Runbook (#8); full suite expansion (#10) beyond upsert tests

## Semantic split of acceptance criteria

| AC | What #5 must deliver now | Sibling notes |
|----|--------------------------|---------------|
| AC-P-030 | Valid identity + ≥1 non-empty field → row stored for today under cookie name | Board visibility of row is #3/#9; tests prove via `get_status` / DB |
| AC-P-031 | `status_day = default_status_day_str()` (no day picker) | Do not accept alternate day in MVP path |
| AC-P-032 | Second submit same name/today → one row, latest values | Repo UNIQUE + upsert already; HTTP must call same helper |
| AC-P-033 | All three empty/whitespace → reject; no write (or no blank row) | New validation layer (not in repo today) |
| AC-P-034 | No lock-after-standup control in API/UI surface added by #5 | Assert absence of lock routes/params/flags |

**AC-002.3** (see values on board without chat) is primarily #3/#9; #5 satisfies the **write** half. Research does not require full board UI in #5.

**AC-002.4** remains enforced by keeping identity dependency on the create path (already tested in #4; regression in #5 suite).

## Recommended design surface (for plan)

### Service / validation layer

Prefer a small pure-ish function (easy unit tests) before HTTP:

| Piece | Responsibility | Suggested location |
|-------|----------------|--------------------|
| `normalize_status_fields(doing, blocked, next) -> tuple[str,str,str]` | strip each field | `status_service.py` or in `app` helpers |
| `validate_status_fields(...)` | if all empty after trim → `ValueError` | same |
| `upsert_today_status(conn, *, display_name, doing, blocked, next, now=None, tz=None) -> Status` | day = `default_status_day_str(...)`; validate fields; call `repository.upsert_status` | `status_service.py` (recommended) or thin logic in route |

**Do not** add lock flags, day path params, or multi-row create.

### HTTP

| Piece | Recommendation |
|-------|----------------|
| Replace stub `POST /status` | Real upsert; keep path `/status` for #4 test continuity where possible |
| Auth | `name = require_display_name(request)` first |
| Body | **Form fields** `doing`, `blocked`, `next` (matches identity form style + future HTMX); JSON body optional but not required if form works |
| Success | **200 JSON** with stored status fields (`display_name`, `status_day`, `doing`, `blocked`, `next`) — simple for TestClient; #9 can later prefer redirect/HTML |
| Validation errors | **400** clear detail (all-empty fields) |
| Missing identity | **400** existing message from `require_display_name` |
| DB wiring | App needs a connection strategy: lifespan `init_db` + dependency `get_conn`, or open/close per request against `resolve_db_path()`. Prefer **app state / dependency** with overrideable path for tests (`tmp_path`) |

### App DB integration (first time)

#5 is the first issue that **must** touch SQLite from HTTP. Plan must choose:

| Option | Notes |
|--------|-------|
| A. Lifespan: `init_db()` at startup; `yield`; store path on `app.state` | Clean; tests pass custom path via factory `create_app(db_path=...)` |
| B. Per-request `init_db` + connect | Simple but heavier; still OK for local MVP |
| **Select A** for plan default | Matches FastAPI norms; testable with `create_app(db_path=tmp_path / "t.db")` |

Extend `create_app(*, db_path: Path | None = None)` — default `resolve_db_path()`; tests inject temp file. Call `init_db(db_path)` on startup.

### Repository changes

| Change | Needed? |
|--------|---------|
| `upsert_status` behavior | **No** — already correct |
| Field validation inside repo | **No** — keep at service/API (repo docstring already assigns ownership) |
| Shared `normalize_display_name` | Optional; not required for #5 AC |

## Test strategy (research)

| AC | Approach |
|----|----------|
| AC-P-030 | TestClient: set identity cookie → POST status with doing set → 200; `get_status(conn, name, today)` has values |
| AC-P-031 | Assert response/`get_status` `status_day == default_status_day_str(now=fixed)` with monkeypatched clock/env as needed |
| AC-P-032 | Two POSTs same name → `list_statuses_for_day` length 1; second values win |
| AC-P-033 | POST all empty / whitespace → 400; no row (or unchanged prior row if testing update-all-empty) |
| AC-P-034 | No route/query/body field named lock/standup_lock; code grep or route inventory |
| Identity regression | POST `/status` without cookie still 400 |
| Keep green | existing identity, repository, today tests |

Use `create_app(db_path=tmp_path / "x.db")` + TestClient; open same path with `connect` for assertions.

**Clock control for AC-P-031:** either inject `now` through service (test-friendly) or set `PULSEBOARD_TZ=UTC` and assert day equals `default_status_day_str()` at request time (slight flake risk at midnight — prefer injectable `now` on service used by route via app dependency override, or accept same-process `default_status_day_str()` comparison immediately after request).

## Options evaluated

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| A. Service + replace `POST /status` + app db_path factory | Clear layers; unblocks #9; reuses #2/#4/#6 | First HTTP+DB wiring | **Select** |
| B. Only service function, no HTTP | Misses endpoint scope; #4 stub remains | TEMP-4 asks endpoint or service — HTTP expected for thin slice | Reject as sole deliverable |
| C. Full HTMX status form page in #5 | Nice UX early | Out of scope (UI markup → #9) | Reject |
| D. Put ≥1-field validation only in SQLite CHECK | Awkward for trim/whitespace; harder tests | Less flexible | Reject |
| E. Accept `status_day` from client | Flexible | Contradicts MVP default-today; risk prior-day product creep | Reject for MVP path |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Scope creep into #3/#9 | No list route; no board HTML; JSON/form API only |
| Breaking #4 identity tests that expect stub body | Update tests that assert `not_implemented`; keep identity 400 behavior |
| DB path in tests polluting cwd | `create_app(db_path=tmp_path/...)` required |
| Midnight flake on “today” | Compare to `default_status_day_str()` in same test moment or inject `now` |
| Partial field update semantics | ADR/PRD: submit new values — treat POST as **full replace** of three fields (empty string clears a field) **if** ≥1 remains non-empty; document in plan |
| `next` SQL reserved word | Repo already quotes `"next"` — keep using repository |
| Concurrent writes | Single local process OK; SQLite default fine for MVP |

**Field replace rule (research recommendation):** Each successful upsert sets doing/blocked/next to the submitted (trimmed) values. Clearing two fields while leaving one is allowed. All three empty rejected. Matches repository upsert SET all three columns.

## Sibling handoff

| Sibling | Handoff from #5 |
|---------|-----------------|
| #3 list | Rows exist via upsert; list can read same DB; no dependency on #5 HTTP shape beyond data |
| #9 UI | POST `/status` with form fields + cookie; show success/errors |
| #10 tests | Create/upsert coverage expands here; #10 may broaden |
| #4 | Identity gate retained on `/status` |

## Open questions (for plan, non-blocking)

1. **JSON vs form-only body** — prefer form (HTMX-ready); JSON optional.
2. **Success response shape** — prefer JSON Status-like dict; HTML redirect deferred to #9.
3. **Injectable `now` on HTTP path** — nice for tests; can compare to helper without injection if careful.
4. **Whether to add `GET /status/me` for today** — not required by TEMP-4; skip.
5. **Update `test_identity` stub assertions** — required when replacing stub; plan should list that file edit.

## Instructions / skills discovered

| Item | Relevance |
|------|-----------|
| [issue-05.md](../../prompt/issue-05.md) | RPI gates; depends on #2/#6/#4 |
| Prior implement patterns #2/#4/#6 | Service + tests + implement.md |
| Status domain + identity + today ADRs | Validation and defaults |

## Ready for plan?

- [x] TEMP-4 scope and AC-P-030–034 captured
- [x] #2/#6/#4 confirmed in place; no blocker
- [x] Repo patterns: stub `/status`, upsert repo, today helper, no app DB yet
- [x] Selected approach: service validation + real `POST /status` + `create_app(db_path=...)`
- [x] Out-of-scope vs #3/#9 clear
- [x] Open questions listed (non-blocking)
- [x] **No production code** written in this phase
- [ ] User verifies Research checklist in [`README.md`](README.md) before Plan (`continue=2`)

## Next

After Research gate: `/rpi continue=2` for issue #5 plan only.
