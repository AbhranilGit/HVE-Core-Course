---
title: "Issue #4 research — display name identity with cookie continuity"
description: Research-only findings for PulseBoard TEMP-3 / GitHub #4 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-04
  - identity
  - cookie
  - display-name
  - research
  - rpi
estimated_reading_time: 8
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4) — auth: display name identity with cookie continuity |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-3** |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete — ready for Plan gate |
| Production code | **None** (this phase) |
| Sprint | 3 of 6 (Sprint 1); after #2 and #6 |
| Hard deps | None for identity helpers; HTTP needs FastAPI (first web surface) |

## Scope summary (authoritative)

From TEMP-3 / #4:

**In scope**

* UI or request path to submit display name (minimal form OK; full page chrome may ship with #9)
* Reject empty/whitespace-only names after trim
* Set HTTP cookie with accepted display name for the app scope
* Read cookie on later status actions; allow explicit change of name
* No SSO/OAuth/password paths

**Out of scope**

* Demo login, shared password, RBAC, SSO/OAuth
* Claiming exclusive ownership of a name across users (trusted team model)

**Acceptance criteria (must drive plan)**

| ID | Criterion | PRD / ADR link |
|----|-----------|----------------|
| AC-P-020 | Given no display name set, when I submit a non-empty display name, then the app accepts it and uses it for subsequent status actions in that browser via cookie | PRD AC-001.1, identity ADR |
| AC-P-021 | Given empty or whitespace-only display name, when I save it, then the app rejects it and does not attribute statuses to a blank name | PRD AC-001.2 |
| AC-P-022 | Given the MVP build, when inspecting identity options, then there is no SSO/OAuth sign-in path | PRD AC-001.3 |
| AC-P-023 | Given required identity is missing, when creating a status is attempted, then create is blocked with a clear prompt or failure | PRD AC-002.4 |

## Evidence log

### Repo state after #2 and #6

| Finding | Evidence |
|---------|----------|
| Persistence ready | [db.py](../../../../src/pulseboard/db.py), [models.py](../../../../src/pulseboard/models.py), [repository.py](../../../../src/pulseboard/repository.py) |
| Today helper ready | [today.py](../../../../src/pulseboard/today.py) — `default_status_day_str`, `list_statuses_for_today` |
| Display-name trim already at repo layer | `repository._require_display_name` strips and raises `ValueError` on blank — **not** cookie/session identity |
| No HTTP app yet | No `app.py`, routes, templates, or FastAPI import under `src/pulseboard/` |
| Runtime deps still empty | [pyproject.toml](../../../../pyproject.toml) — `dependencies = []`; only optional `pytest` |
| Package surface | `__init__.py` version only; no re-exports |
| Tests | [test_status_repository.py](../../../../tests/test_status_repository.py), [test_instance_today.py](../../../../tests/test_instance_today.py) — no cookie/HTTP tests |
| Env pattern | `PULSEBOARD_DB_PATH`, `PULSEBOARD_TZ` — cookie name can be a module constant (not necessarily env) |
| Sprint position | [sprint-plan.md](../../05-sprint-planning/output/sprint-plan.md): #4 order 3; #5 depends on #4; full chrome in #9 |

### Product / architecture constraints

| Source | Constraint relevant to #4 |
|--------|---------------------------|
| Identity ADR | Poster = non-empty **display name** only; **HTTP cookie** continuity after valid submit; no passwords/SSO/OAuth/demo login; trim + reject blank; case-sensitive as entered; trusted local team (spoofing accepted); signed cookies optional not required |
| PRD FR-001 / US-001 | Set/confirm non-empty display name; AC-001.1–001.3 |
| PRD AC-002.4 | Create blocked when identity missing — clear prompt/failure |
| PRD NFR-004 / NFR-005 | No OAuth/SSO paths; only local display name + status text |
| Web-stack ADR | **FastAPI** under `src/pulseboard/`; server-rendered HTML + HTMX later; cookies/forms fit FastAPI; template engine is implementation detail; pytest TestClient style expected later |
| Status domain ADR | `display_name` is identity key for uniqueness with `status_day`; blank name rejected at domain; rename does not merge rows |
| SQLite ADR | No identity table required — name is plain text on status rows |
| Sprint plan | Minimal request path OK for #4; full board chrome deferred to #9 |

### Explicit non-goals for this issue

* SSO, OAuth, passwords, demo login, RBAC, name ownership claims
* Full HTMX board + status form chrome (#9)
* Upsert of doing/blocked/next product rules (#5) beyond a **hook** that refuses missing identity
* List-today HTTP (#3)
* Schema changes, TZ logic, runbook prose (#8)
* Multi-browser shared session / server-side session store

## Semantic split of acceptance criteria

| AC | What #4 must deliver now | What may complete with siblings |
|----|--------------------------|--------------------------------|
| AC-P-020 | Accept non-empty name; set cookie; subsequent requests in same client read that cookie as current identity | #5/#9 use `current_display_name` for status actions |
| AC-P-021 | Reject empty/whitespace after trim; do not set cookie to blank; do not attribute under blank | Repo already rejects blank on upsert; identity layer must reject before cookie set |
| AC-P-022 | No SSO/OAuth routes, templates, or deps in MVP surface introduced by #4 | Release checklist #7 / #9 also assert absence |
| AC-P-023 | **Contract + minimal enforcement:** missing cookie/name blocks create with clear failure (HTTP 4xx or redirect/prompt). Full status form UX can improve in #5/#9 | #5 must call the same identity resolver before upsert |

**Research recommendation:** Treat identity as a **small FastAPI-first slice**: pure helpers (normalize/validate name, cookie read/write constants) + minimal HTTP (GET form or POST set-name + cookie) + TestClient tests. Do **not** implement full board UI. For AC-P-023, either (a) a stub create route that only checks identity, or (b) a documented `require_display_name(request)` dependency that #5 will attach — prefer **(a) or both** so AC-P-023 is testable without completing #5 product validation.

## Recommended module / API surface (for plan)

Keep pure logic separate from FastAPI so unit tests stay light (same pattern as `today.py` vs repository).

| Piece | Responsibility | Suggested location |
|-------|----------------|--------------------|
| `normalize_display_name(raw) -> str` | strip; raise `ValueError` if empty | `src/pulseboard/identity.py` (new) |
| Cookie constants | cookie name e.g. `pulseboard_display_name`; path `/`; httponly recommended; samesite=lax; max-age optional (session or long-lived local) | `identity.py` |
| `read_display_name(cookies/request) -> str \| None` | Read cookie; treat missing/blank as unset | `identity.py` and/or FastAPI dependency |
| `set_display_name_cookie(response, name)` | Set cookie after successful validate | FastAPI response helper |
| `require_display_name(...)` | Raise/return clear failure when missing (AC-P-023) | dependency used by create path |
| Minimal routes | `POST` (and optional `GET`) to set/change name; optional identity-guarded stub for “create attempted without name” | `src/pulseboard/app.py` or `routes/identity.py` + thin `create_app()` |
| Explicit change | Same POST with new non-empty name overwrites cookie (ADR: change via explicit control) | same set-name endpoint |

**Reuse note:** `repository._require_display_name` already encodes trim+non-empty. Plan should either:

1. Move/share one canonical `normalize_display_name` used by identity + repository, or
2. Keep identity validation independent and leave repository as-is (duplicate one-liner OK for MVP thinness).

**Preference for plan:** single public `normalize_display_name` in `identity.py`; repository may import it later (optional small refactor in #4 or leave private `_require_display_name` until #5 — either is fine if behavior matches).

## Cookie design defaults (plan-time choices)

| Concern | Recommendation | Rationale |
|---------|----------------|-----------|
| Cookie name | `pulseboard_display_name` (constant) | Clear, app-scoped; ADR leaves name free |
| Value | Raw accepted display name (after trim); URL-safe plain text | Trusted local; signing optional per ADR |
| HttpOnly | **True** | Reduces XSS cookie theft; form still sets via server response |
| Secure | **False** default for local HTTP | Local uvicorn often http://127.0.0.1 |
| SameSite | `lax` | Sensible default for form POSTs |
| Path | `/` | App-wide on instance |
| Max-Age / Expires | Session cookie **or** long max-age (e.g. 30d) | ADR: continuity during workday; session cookie is enough; long max-age is nicer across restarts of browser session — **open option**, pick one in plan |
| Signing | Not required for MVP | Identity ADR: allowed but not required |

## HTTP / FastAPI introduction (first in repo)

#4 is the **first issue that inherently needs HTTP** (cookie + request path). That implies:

| Decision | Recommendation |
|----------|----------------|
| Add runtime deps | `fastapi`, `uvicorn` (and likely `httpx` or use Starlette TestClient via fastapi) — **jinja2** only if serving HTML form in #4 |
| Minimal HTML vs JSON | Prefer **simple HTML form POST** (works without HTMX) so AC-P-020 is browser-real; JSON POST also OK for tests. Full HTMX board stays #9 |
| App factory | `create_app() -> FastAPI` for TestClient and future uvicorn entry |
| Entrypoint | Optional `python -m pulseboard` or document `uvicorn pulseboard.app:app` — full runbook is #8; a one-line module docstring is enough |
| AC-P-022 proof | Grep/test: no routes named oauth/sso/login-provider; no authlib/OIDC deps |

**Scope guard:** Adding FastAPI for identity only is in scope. Adding status upsert fields, board templates, or HTMX partials is **out** of #4.

## Test strategy (research)

| AC | Suggested test approach |
|----|-------------------------|
| AC-P-020 | TestClient: POST valid name → response `Set-Cookie`; follow-up request carries cookie → resolved identity equals name |
| AC-P-021 | POST `""`, `"   "` → 4xx or error body; cookie not set to blank; optional assert no status row if any write attempted |
| AC-P-022 | Static/assert: app routes list has no SSO/OAuth; pyproject has no oauth libraries |
| AC-P-023 | Attempt create (stub or real path) without cookie → blocked with clear message/status code; with cookie → allowed past identity gate (stub may 501/not-implemented for full upsert body if #5 not done) |

Use temp DB only if create path touches DB; pure identity tests need no SQLite.

## Options evaluated

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| A. Pure helpers only (no FastAPI yet) | No new deps; matches #2/#6 style | **Cannot** meet cookie AC or HTTP continuity without a request/response | Reject for #4 AC |
| B. FastAPI + cookie + minimal set-name form/API + identity dependency | Meets all AC; unblocks #5/#9; ADR-aligned | First dep add; careful not to build #9 | **Select** |
| C. Full HTMX identity+board in #4 | Completes UX early | Violates issue split / prompt (“leave full chrome to #9”) | Reject |
| D. Client-only localStorage identity | No server cookie | Contradicts identity ADR (HTTP cookie) | Reject |
| E. Server session store (DB/redis) | Stronger session | Overkill; ADR is cookie value = display name | Reject |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Scope creep into #5/#9 | Plan checklist: no doing/blocked/next upsert product rules; no board list UI |
| Duplicate validation vs repository | Document single normalize rule; optional shared helper |
| Cookie encoding of special characters | Restrict or encode; tests with simple ASCII names first (MVP team names) |
| AC-P-023 incomplete without #5 | Ship `require_display_name` + stub create OR document dependency + test the dependency alone with a tiny route |
| First FastAPI dep breaks “stdlib only” habit | Explicit pyproject update; pin loosely compatible versions in plan |
| Case-sensitive `Ada` vs `ada` confusion | ADR accepted; no normalize-case in MVP |

## Sibling handoff contracts

| Sibling | What #4 should leave them |
|---------|---------------------------|
| #5 upsert | `require_display_name` / cookie reader; validated non-empty name string for `upsert_status(..., display_name=...)` |
| #9 UI | Set-name endpoint or form action; cookie already set so status form can omit re-typing name; change-name control can POST same endpoint |
| #3 list | No identity required to **view** board (PRD board is shared); do not force cookie on list |
| #8 runbook | Cookie name + “set display name first” note (document later) |
| #10 tests | Identity fixtures via TestClient cookie jar |

**Important:** Board list (#3) should remain usable without identity; only **create/update status** requires name (AC-P-023 / AC-002.4).

## Open questions (for plan, not blockers)

1. **Cookie max-age:** session vs multi-day — either satisfies AC-P-020; recommend **session cookie** for simplest MVP unless plan prefers 7–30d continuity.
2. **HTML vs JSON-only for set-name:** recommend HTML form + 303 redirect or 200 with confirmation for manual browser check; TestClient works either way.
3. **Refactor repository to import `normalize_display_name`:** optional in #4; not required for AC if both reject blank identically.
4. **Stub create route for AC-P-023 vs dependency-only tests:** recommend a minimal protected route so AC language (“creating a status is attempted”) is literally testable without implementing #5 field validation.
5. **Exact cookie name string** — bike-shed only; `pulseboard_display_name` is fine.

## Instructions / skills discovered

| Item | Relevance |
|------|-----------|
| Stage 6 issue prompt [issue-04.md](../../prompt/issue-04.md) | Research → plan → implement gates; leave HTMX chrome to #9 |
| Prior research style [issue-02/research.md](../issue-02/research.md), [issue-06/research.md](../issue-06/research.md) | Same document structure and AC tables |
| Markdown / writing-style instructions (hve-core) | Front matter + tables for lifecycle docs |
| No new skills required beyond FastAPI knowledge at plan/implement time |

## Ready for plan?

- [x] Authoritative TEMP-3 scope and AC-P-020–023 captured
- [x] Identity + web-stack ADRs consulted
- [x] Repo patterns: no app yet; `_require_display_name` exists; FastAPI must be introduced
- [x] Selected approach: Option B (FastAPI + cookie + minimal set-name + require identity)
- [x] Out-of-scope boundaries vs #5/#9 clear
- [x] Open questions listed (non-blocking)
- [x] **No production code** written in this phase
- [ ] User verifies Research checklist in [`README.md`](README.md) before Plan (`continue=2`)

## Next

After Research gate: `/rpi continue=2` for issue #4 plan only — steps, files, AC checks, risks; still no implement until Plan gate.
