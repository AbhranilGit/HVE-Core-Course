---
title: "Issue #3 research — list statuses for today board"
description: Research-only findings for PulseBoard TEMP-5 / GitHub #3 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-03
  - list
  - today-board
  - research
  - rpi
estimated_reading_time: 8
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3) — api: list statuses for today board |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-5** |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete — ready for Plan gate |
| Production code | **None** (this phase) |
| Sprint | 5 of 6 (Sprint 1) |
| Depends on | #2 schema/repo, #6 today helper — **in place**; #5 upsert **in place** (data path); #4 identity optional for list |
| Sprint order note | Thin slice path: #2 → #6 → #4 → #5 → **#3** → #9 |

## Scope summary (authoritative)

From TEMP-5 / #3:

**In scope**

* Query/list API or service returning **today’s** statuses
* Each item includes **display_name**, **doing**, **blocked**, **next**
* Empty list is valid (not an error)
* Deterministic ordering (implementation choice; keep stable)
* Distinct display names remain distinct rows

**Out of scope**

* Blocked-only filter chip, workflow states, SLA, notifications
* Historical days UI
* Real-time websocket push
* HTMX board chrome and status form UI (#9)
* Full automated suite expansion beyond this issue’s list tests (#10)

**Acceptance criteria (must drive plan)**

| ID | Criterion | PRD / ADR link |
|----|-----------|----------------|
| AC-P-040 | Given zero statuses for today, when listing today, then the result is an empty collection suitable for an empty-state UI (not a hard failure) | PRD AC-004.1 |
| AC-P-041 | Given one or more statuses for today, when listing today, then each includes display name, doing, blocked, and next | PRD AC-004.2, FR-006 |
| AC-P-042 | Given only prior-day statuses exist, when listing today, then they are not included | PRD AC-004.3 |
| AC-P-043 | Given multiple distinct display names posted today, when listing, then each person has a distinguishable row (no silent cross-name overwrite) | PRD AC-004.4 |
| AC-P-044 | Given a non-empty blocked value on a today row, when listed, then blocked text is present for facilitator scan | PRD AC-005.1 |
| AC-P-045 | Given blocked empty but doing or next filled, when listed, then the row still appears with blocked empty/absent | PRD AC-005.2 |

## Evidence log

### Dependency status (#2, #6, #5, #4)

| Dep | Status | What #3 reuses |
|-----|--------|----------------|
| #2 | **In place** | Schema `statuses`; `list_statuses_for_day(conn, status_day)`; UNIQUE `(display_name, status_day)` guarantees one row per name per day |
| #6 | **In place** | `default_status_day_str` / `instance_today`; `list_statuses_for_today(conn, now=, tz=)` already wraps day + list |
| #5 | **In place** | `POST /status` + `upsert_today_status` populate today rows under cookie name — preferred way to seed HTTP-level list tests |
| #4 | **In place** | Cookie identity for create; **list does not require identity** per TEMP-5 (facilitator board is shared glance) |

**Blocker check:** **None.** Repository and today helpers already implement the board projection query. Missing piece is **HTTP (or thin service façade) exposure** for the facilitator board and AC-mapped tests at the list surface. #9 will consume this list; do not build HTMX here.

### Repo state (current code — post #5)

| Finding | Evidence |
|---------|----------|
| List-by-day exists | [repository.py](../../../../src/pulseboard/repository.py) `list_statuses_for_day` — `WHERE status_day = ?` **ORDER BY display_name COLLATE NOCASE** |
| List-for-today exists | `list_statuses_for_today` → `default_status_day_str` then `list_statuses_for_day` |
| Upsert path live | [status_service.py](../../../../src/pulseboard/status_service.py) + [app.py](../../../../src/pulseboard/app.py) `POST /status` |
| App factory | `create_app(*, db_path=)`; eager + lifespan `init_db`; `app.state.db_path`; per-request `connect` / close |
| Serialization helper | `_status_to_dict(Status)` already maps id, display_name, status_day, doing, blocked, next, timestamps |
| No list HTTP yet | App docstring: “Board list HTTP and HTMX UI are later issues (#3, #9)” — only `GET/POST /identity`, `POST /status` |
| Model | [models.py](../../../../src/pulseboard/models.py) `Status` dataclass with required board fields |
| Prior-day exclusion | [tests/test_instance_today.py](../../../../tests/test_instance_today.py) already asserts `list_statuses_for_today` omits prior day (repo-level AC-P-013) |
| Multi-name / day filter | [tests/test_status_repository.py](../../../../tests/test_status_repository.py) list-by-day coverage |
| Env | `PULSEBOARD_DB_PATH`, `PULSEBOARD_TZ` |
| Deps | fastapi, uvicorn, python-multipart; dev pytest + httpx |
| UI | Identity HTML only; no board page (#9) |

### Product / architecture constraints

| Source | Constraint relevant to #3 |
|--------|---------------------------|
| Status domain ADR — Board projection | Today’s board = all statuses where `status_day == instance_today()`, each showing display name, doing, blocked, next; **empty board valid** |
| Status domain ADR — ordering | Ordering is implementation UX detail; **choose one deterministic order and keep stable** (repo already: display_name NOCASE) |
| Status domain ADR — blocked | Free text only; no filter chip; facilitators scan non-empty `blocked` on the board |
| Today ADR | Board query defaults to rows where `status_day == instance_today()`; instance TZ / `PULSEBOARD_TZ` |
| Web-stack ADR | FastAPI; JSON endpoints allowed if they simplify tests or HTMX partials; **no websockets**; HTMX board is #9 |
| Identity ADR | Display name attribution on posts; board is shared — list need not gate on cookie (spoofing already accepted on local instance) |
| PRD US-004 / FR-005 | Facilitator views today’s board |
| PRD US-005 / FR-006 | Blocked text visible on board rows; empty blocked still shows row |
| PRD NFR-001 | ≤15 rows local board feels immediate — trivial for SQLite list |
| PRD NFR-007 | List failures not silent (error response / log) |
| PRD NFR-008 / TEMP-7 | Broader create+list suite is #10; #3 still needs AC-P-040–045 coverage |
| TEMP-5 out of scope | Filter chip, history UI, websockets |

### Explicit non-goals for this issue

* HTMX board page, status form chrome, partials polish (#9)
* Blocked-only filter / workflow / notifications / SLA
* Historical day picker or multi-day board
* Websockets / live push
* Changing UNIQUE/upsert semantics or schema
* Requiring identity cookie to **read** the board (unless plan later documents a deliberate product change — research recommends **open read**)
* Runbook (#8); release checklist (#7); full #10 suite ownership

## Semantic split of acceptance criteria

| AC | What #3 must deliver now | Sibling notes |
|----|--------------------------|---------------|
| AC-P-040 | List today with no rows → **empty collection**, HTTP success (e.g. 200 + `[]`), not 404/500 | #9 empty-state UI copy |
| AC-P-041 | Non-empty today set → each element exposes display_name, doing, blocked, next | Extra fields (id, timestamps, status_day) OK if present |
| AC-P-042 | Prior-day-only data → list today returns empty (or omits those rows) | Repo already; HTTP must use **instance today**, not client-supplied day in MVP |
| AC-P-043 | Two+ distinct names today → two+ distinguishable rows | UNIQUE + list; seed via two upserts / repo inserts |
| AC-P-044 | Non-empty blocked on a today row → listed payload includes that blocked text | Facilitator scan |
| AC-P-045 | blocked empty, doing/next filled → row still listed; blocked empty string or equivalent | No drop when unblocked |

**Write half** of board data is #5; **read half** is #3; **glanceable HTML** is #9.

## Recommended design surface (for plan)

### Reuse first (do not reimplement query)

| Piece | Already exists | #3 action |
|-------|----------------|-----------|
| `list_statuses_for_day` | Yes — ordered NOCASE by name | Call as-is |
| `list_statuses_for_today` | Yes — day default + list | **Primary service entry** for board |
| `upsert_today_status` / POST /status | Yes | Seed data in integration tests |
| `_status_to_dict` | Yes in app | Reuse for JSON items |

**Optional thin wrapper** (only if plan wants symmetry with `status_service`):

* `list_today_statuses(conn, *, now=None, tz=None) -> list[Status]` in `status_service.py` that delegates to `repository.list_statuses_for_today`
* Not strictly required if HTTP calls repository helper directly; service wrapper keeps app thin and matches #5 layering

### HTTP (recommended)

| Piece | Recommendation |
|-------|----------------|
| Method/path | **`GET /statuses/today`** (clear, REST-ish, no clash with `POST /status`) |
| Alt path | `GET /status` or `GET /board` — avoid overloading POST collection semantics; prefer `/statuses/today` |
| Auth | **No** `require_display_name` for list (shared board). Identity remains on write only |
| Day param | **Do not** accept client `status_day` in MVP path (AC-P-042 / today ADR); always instance today |
| Success body | **200 JSON** array of status objects (same field shape as POST response items via `_status_to_dict`) **or** `{"status_day": "...", "items": [...]}` — array is simplest for AC empty-state; envelope optional |
| Empty | `[]` or `items: []` with 200 — **not** 404 |
| Errors | DB/path failures → non-silent 5xx (NFR-007); no special empty-error |
| Ordering | Preserve repository order (`display_name COLLATE NOCASE`) — satisfies “deterministic; keep stable” |
| HTML | Out of scope — #9 may add `GET /` board that calls same service |

### Selected default response shape

**Option A (select):** `200 application/json` body = **JSON array** of status dicts.

* Empty: `[]`
* Item keys at minimum: `display_name`, `doing`, `blocked`, `next` (plus existing `_status_to_dict` extras OK)

**Option B (alt):** Envelope `{"status_day": "<iso-date>", "items": [...]}` — slightly better for UI/debug; plan may pick if #9 benefits. Research default remains **A** for minimal AC surface.

### App wiring pattern (match #5)

```text
conn = connect(request.app.state.db_path)
try:
    rows = list_statuses_for_today(conn)  # or status_service.list_today_statuses
finally:
    conn.close()
return JSONResponse([_status_to_dict(r) for r in rows])
```

Use existing `create_app(db_path=)` + TestClient context-manager fixtures.

### Repository / schema changes

| Change | Needed? |
|--------|---------|
| New SQL | **No** |
| Change ORDER BY | **No** unless product picks different order later |
| Filter blocked-only | **No** (out of scope) |
| Auth tables | **No** |

## Test strategy (research)

| AC | Approach |
|----|----------|
| AC-P-040 | Fresh tmp DB → `GET` list → 200 + empty list |
| AC-P-041 | POST /status (or repo upsert) one row → GET list → length ≥1; keys present |
| AC-P-042 | Insert prior-day row only (repo `upsert_status` with yesterday) → GET list → empty / no that name |
| AC-P-043 | Two identities or two repo names today → GET list length 2; distinct `display_name` |
| AC-P-044 | Upsert with blocked="waiting on X" → listed item blocked equals text |
| AC-P-045 | Upsert blocked="" doing="work" → row present; blocked empty |
| Ordering smoke | Optional: Ada + Bea → names sorted case-insensitive |
| Regression | Full suite remains green (#2/#4/#5/#6) |

**Seeding tip:** For multi-name without cookie juggling, call `repository.upsert_status` / `upsert_today_status` with open `connect(db_path)` in test setup; still hit HTTP for the list assertion. For single-name, cookie + POST /status is enough.

**Clock / day:** Prefer same-process `default_status_day_str()` comparison; for AC-P-042 use explicit prior `status_day` string (e.g. today − 1 day) rather than relying on midnight boundaries.

## Options evaluated

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| A. `GET /statuses/today` JSON array via `list_statuses_for_today` | Minimal; reuses #2/#6; testable; unblocks #9 | Path naming choice only | **Select** |
| B. Service wrapper + same GET | Symmetric with #5 layering | Tiny extra file surface | Acceptable variant of A |
| C. HTML board in #3 | Facilitator UX early | Out of scope → #9 | **Reject** |
| D. Require cookie to list | Consistent “auth” | Not in TEMP-5; blocks anonymous facilitator glance on shared machine | **Reject** for MVP |
| E. Client-supplied `?day=` | Flexible history | Contradicts MVP today-only board; history out of scope | **Reject** MVP path |
| F. Repo-only, no HTTP | Meets “service” reading of scope literally | Weak for #9 HTMX/tests; TEMP-5 is **api** label | Reject as sole deliverable |
| G. Websocket push | Live board | Explicitly out of scope | **Reject** |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Scope creep into #9 HTMX | JSON list only; no board templates/static HTMX |
| Accepting `day` query “for testing” | Do not add; use repo helpers in tests for prior-day setup |
| Empty list as 404 | Spec empty-state; assert 200 + `[]` |
| Identity required accidentally | Do not call `require_display_name` on GET list |
| Duplicate query logic | Call existing `list_statuses_for_today` only |
| Ordering bikeshed | Keep repo NOCASE name order; document in implement.md |
| Response shape churn for #9 | Prefer stable `_status_to_dict` items; #9 can wrap later |
| Confusing `POST /status` vs list path | Use plural `/statuses/today` |

## Sibling handoff

| Sibling | Handoff from #3 |
|---------|-----------------|
| #5 upsert | Already provides write path; list reads same DB |
| #9 UI | `GET /statuses/today` (or chosen path) for board rows; empty `[]` → empty state; POST /status for form |
| #10 tests | Broader create+list evidence; #3 establishes list HTTP tests |
| #6 today | Day boundary already correct at repo; HTTP must not bypass |
| #4 identity | Write remains gated; list open |

## Open questions (for plan, non-blocking)

1. **Exact path** — research default `GET /statuses/today`; plan may choose `GET /board/today` if clearer for #9.
2. **Array vs envelope** — default array; envelope if #9 wants `status_day` echoed without a second call.
3. **Service wrapper** — optional `status_service.list_today_statuses`; not required for AC.
4. **Whether GET returns `status_day` on each item** — `_status_to_dict` already includes it; keep.
5. **Auth on list** — research: open; only revisit if product owner requires cookie (would be PRD-level).

## Instructions / skills discovered

| Item | Relevance |
|------|-----------|
| [issue-03.md](../../prompt/issue-03.md) | RPI gates; depends on #2, #6; leave HTMX to #9 |
| [issue-05 implement](../issue-05/implement.md) | App DB factory, TestClient CM, JSON patterns to mirror |
| Status domain + today + web-stack ADRs | Board projection, empty board, ordering, no websockets |
| Prior #2/#6 tests | Repo-level list/today already partially prove AC-P-042 mechanics |

## Ready for plan?

- [x] TEMP-5 scope and AC-P-040–045 captured
- [x] #2/#6 confirmed in place; #5 available for seeding; **no blocker**
- [x] Repo patterns: `list_statuses_for_today`, ordered list-by-day, no list HTTP yet, `_status_to_dict`
- [x] Selected approach: `GET /statuses/today` → `list_statuses_for_today` → JSON array (empty OK)
- [x] Out-of-scope vs #9 / filters / websockets / history clear
- [x] Open questions listed (non-blocking)
- [x] **No production code** written in this phase
- [ ] User verifies Research checklist in [`README.md`](README.md) before Plan (`continue=2`)

## Next

After Research gate: `/rpi continue=2` for issue #3 plan only (no implement until Plan verified).
