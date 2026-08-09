---
title: "Issue #4 plan — display name identity with cookie continuity"
description: Implementation plan for PulseBoard TEMP-3 / GitHub #4 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-04
  - identity
  - cookie
  - plan
  - rpi
estimated_reading_time: 7
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4) — auth: display name identity with cookie continuity |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-3** |
| Phase | Plan only (`/rpi continue=2`) |
| Status | Complete — ready for Implement gate |
| Based on | [research.md](research.md) (complete; Status Complete — ready for Plan gate) |
| Production code | **None** (this phase) |
| Sprint | 3 of 6 (Sprint 1) |
| Depends on | Research Option B; #2/#6 already in place (not hard code deps for identity) |

## User requests (this phase)

1. Plan implementation of PulseBoard issue #4 (TEMP-3) only.
2. Do not implement yet.
3. Base the plan on completed `lifecycle/06-implementation/output/issue-04/research.md`.
4. Also use TEMP-3 / #4 scope from `backlog-snapshot.md`.
5. Leave full HTMX board chrome to #9.
6. Include steps, files to touch, acceptance checks, and risks.
7. Stay inside this issue’s scope.
8. Write the plan to `lifecycle/06-implementation/output/issue-04/plan.md`.

## Objectives

Introduce local display-name identity with HTTP cookie continuity on a minimal FastAPI surface so subsequent status create/update can attribute posts and reject blank or missing identity — without SSO, without full board/status UI (#9), and without full upsert product rules (#5).

## Alignment with research (no contradictory inventions)

| Research decision | Plan adoption |
|-------------------|---------------|
| Option B: FastAPI + cookie + minimal set-name + require identity | Yes |
| Reject pure helpers only / localStorage / session DB / full HTMX in #4 | Yes |
| Module `src/pulseboard/identity.py` | Yes |
| `normalize_display_name` public helper | Yes |
| Cookie name `pulseboard_display_name` | Yes |
| HttpOnly=True, Secure=False, SameSite=lax, Path=/ | Yes |
| Session cookie (no Max-Age) for simplest MVP | Yes (research open Q1 resolved) |
| Signing not required | Yes |
| `create_app()` factory + TestClient tests | Yes |
| Minimal HTML form POST (no HTMX board) | Yes (research open Q2 resolved) |
| Stub identity-guarded create route for AC-P-023 | Yes (research open Q4 resolved) |
| Optional repository refactor to shared normalize | **Defer** — leave `repository._require_display_name`; match behavior (research open Q3) |
| Board list must not require cookie | Yes — do not protect list routes (none added) |
| No SSO/OAuth routes or deps | Yes |
| Full chrome / upsert fields / list today HTTP out of scope | Yes |

**Intentional deltas from research:** none material. Open questions resolved as above toward the research-preferred defaults.

## Design summary

### Pure helpers (`identity.py`)

| Symbol | Behavior |
|--------|----------|
| `COOKIE_DISPLAY_NAME = "pulseboard_display_name"` | Constant cookie key |
| `normalize_display_name(raw: str) -> str` | `strip()`; if empty raise `ValueError` with clear message (e.g. display name must be non-empty) |
| `display_name_from_cookie_value(value: str \| None) -> str \| None` | None/blank after strip → `None`; else return normalized name (or None if normalize would fail — prefer try/return None for “read optional”) |
| `read_display_name(request) -> str \| None` | Read cookie by constant; optional identity (unset OK) |
| `require_display_name(request) -> str` | If missing/blank → raise FastAPI `HTTPException` **400** (or 401) with clear detail that display name is required; else return normalized name |
| `set_display_name_cookie(response, name: str) -> None` | After validate: `response.set_cookie(key=..., value=name, httponly=True, samesite="lax", path="/", secure=False)` — **session cookie** (omit max_age) |

Keep FastAPI types only where needed (`Request`/`Response`/`HTTPException`). Prefer pure `normalize_display_name` testable without ASGI.

**Exception type for missing identity:** use `HTTPException(status_code=400, detail="Display name required. Set your display name before creating a status.")` so AC-P-023 is a clear failure. (400 chosen over 401: not real auth credentials.)

### Minimal FastAPI app (`app.py`)

| Piece | Behavior |
|-------|----------|
| `create_app() -> FastAPI` | App factory for tests and uvicorn |
| `app = create_app()` | Module-level app for `uvicorn pulseboard.app:app` |
| `GET /identity` | Minimal HTML page: form `method=post action=/identity` field `display_name`; if cookie present, show current name + form to change |
| `POST /identity` | Form field `display_name`; on success set cookie and return **303** to `GET /identity` (or 200 HTML confirmation); on blank → **400** HTML or plain error, **do not** set blank cookie |
| `POST /status` (stub) | **Identity gate only** for AC-P-023. Depends on `require_display_name`. Does **not** implement doing/blocked/next upsert (#5). On success with identity: **501** or **200** JSON `{"ok": true, "display_name": "...", "status": "not_implemented"}` documenting stub — either is fine if tests assert: without cookie → 400; with cookie → not 400 for missing identity. Prefer **200 stub JSON** so “allowed past identity gate” is obvious; body states upsert not implemented. |
| No routes | `/oauth`, `/sso`, `/login` IdP, passwords, demo login |
| No board UI | No HTMX, no list-today page, no status form fields beyond stub |

Inline HTML strings are acceptable for #4 (avoid jinja2 dependency unless already wanted). Research allowed jinja2 only if needed — **plan: inline HTML, no jinja2**.

### Dependencies (`pyproject.toml`)

| Package | Role |
|---------|------|
| `fastapi` | App, Request, Response, cookies, HTTPException |
| `uvicorn` | Local ASGI run (documented in module docstring; full runbook #8) |
| `httpx` | Required by FastAPI/Starlette `TestClient` in modern stacks — add as **dev** optional or runtime; prefer **dev** extra alongside pytest if TestClient-only, but FastAPI often lists it — add `httpx` under **dev** for tests; runtime: `fastapi`, `uvicorn` |

Pin loosely, e.g. `fastapi>=0.115`, `uvicorn>=0.32`, dev `httpx>=0.27` (adjust to what install resolves on 3.12). Do **not** add authlib, python-jose OAuth stacks, or SSO SDKs.

### Repository / schema

| Item | Plan |
|------|------|
| `repository.py` | **No required change** — keep `_require_display_name` private |
| `db.py` / `models.py` / `today.py` | **No change** |
| Identity table | **None** |

### Sibling contracts (do not implement siblings)

| Sibling | Handoff from #4 |
|---------|-----------------|
| #5 | Import `require_display_name` / `read_display_name`; replace stub `/status` body with real upsert; keep identity gate |
| #9 | Link/form to `GET/POST /identity`; reuse cookie; build board chrome separately |
| #3 | List routes stay public (no cookie required) |
| #8 | Later document cookie name + set-name URL |

## Implementation steps

Execute in order during `/rpi continue=3`. Do **not** start #5, #3, #9, or Sprint 2.

### Step 1 — Dependencies

<!-- parallelizable: false -->

1. Edit `pyproject.toml`: add runtime `fastapi`, `uvicorn`; dev `httpx` (if not pulled transitively for tests).
2. Install into `hve-env` and confirm import.

### Step 2 — `identity.py`

<!-- parallelizable: false -->

1. Add `src/pulseboard/identity.py` with constants + normalize + cookie read/set helpers + `require_display_name`.
2. Unit-testable normalize without app.

### Step 3 — `app.py` minimal routes

<!-- parallelizable: false -->

1. Add `src/pulseboard/app.py` with `create_app()`, `GET/POST /identity`, stub `POST /status`.
2. Module docstring: `uvicorn pulseboard.app:app` (or `create_app` note).
3. No HTMX assets, no board templates, no DB wiring required for identity routes.

### Step 4 — Tests

<!-- parallelizable: false -->

1. Add `tests/test_identity.py` (name flexible).
2. Cases:
   * **normalize:** `"  Ada  "` → `"Ada"`; `""` / `"   "` → `ValueError`.
   * **AC-P-020:** TestClient POST `/identity` with `display_name=Ada` → response sets cookie `pulseboard_display_name=Ada` (or URL-encoded equivalent); subsequent GET `/identity` or call that reads identity shows Ada; cookie retained on client.
   * **AC-P-020 change name:** POST new non-empty name overwrites cookie.
   * **AC-P-021:** POST empty/whitespace → 400; cookie not set to blank (assert no Set-Cookie with empty value / cookie jar still empty).
   * **AC-P-022:** Enumerate `app.routes` path strings — none match oauth/sso/openid style; optional assert pyproject deps list has no oauth libraries.
   * **AC-P-023:** POST `/status` without cookie → 400 + clear detail; with cookie after set-name → not 400 for missing identity (200 stub or 501 as chosen).
3. Keep `test_status_repository.py` and `test_instance_today.py` green (no regressions).
4. Run pytest with `hve-env` Python 3.12.

### Step 5 — Implement summary

<!-- parallelizable: false -->

1. Write `lifecycle/06-implementation/output/issue-04/implement.md`.
2. Record files, install notes, pytest output, AC results, deviations.
3. `.copilot-tracking/changes/` entry when implementing.

### Step 6 — Validation gate

<!-- parallelizable: false -->

1. All tests pass.
2. No SSO/OAuth surface.
3. No board HTMX / full upsert / list-today HTTP.
4. No schema changes.

## Files to touch

| Path | Action | Notes |
|------|--------|-------|
| [pyproject.toml](../../../../pyproject.toml) | **Edit** | Add fastapi, uvicorn; httpx in dev |
| [src/pulseboard/identity.py](../../../../src/pulseboard/identity.py) | **Add** | Normalize + cookie helpers + require |
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | **Add** | `create_app`, identity routes, status stub |
| [tests/test_identity.py](../../../../tests/test_identity.py) | **Add** | AC-P-020–023 |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | **No change** | Keep private `_require_display_name` |
| [src/pulseboard/db.py](../../../../src/pulseboard/db.py) | **No change** | |
| [src/pulseboard/models.py](../../../../src/pulseboard/models.py) | **No change** | |
| [src/pulseboard/today.py](../../../../src/pulseboard/today.py) | **No change** | |
| [src/pulseboard/__init__.py](../../../../src/pulseboard/__init__.py) | **No change expected** | |
| Templates/static HTMX board | **Do not add** | #9 |
| [lifecycle/06-implementation/output/issue-04/implement.md](implement.md) | **Edit** | phase-3 summary |

## Acceptance checks

| ID | Criterion (TEMP-3) | How we will verify |
|----|--------------------|--------------------|
| AC-P-020 | Non-empty name accepted; used for subsequent status actions via cookie | TestClient: set-name sets cookie; follow-up request resolves same name; stub `/status` with cookie passes identity gate with that name |
| AC-P-021 | Empty/whitespace rejected; no blank attribution | TestClient POST blank → 400; no blank cookie; normalize unit tests |
| AC-P-022 | No SSO/OAuth sign-in path | Route inventory test + no OAuth deps in pyproject |
| AC-P-023 | Create blocked when identity missing; clear failure | POST `/status` without cookie → 400 clear detail; with cookie → past identity gate |

### Scope checks (negative)

| Check | Verify |
|-------|--------|
| No demo login / password / RBAC | Code review |
| No full HTMX board / status field form UI | No board templates; stub only |
| No doing/blocked/next upsert rules | Stub does not call `upsert_status` |
| No list-today HTTP | No list route added |
| Schema unchanged | `db.py` untouched |
| Board view not gated on cookie | No list protection added |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Scope creep into #5/#9 | Checklist above; stub `/status` explicitly not-implemented for fields |
| First FastAPI install issues on 3.8 system Python | Use **hve-env** 3.12 only (same as #2/#6) |
| TestClient cookie jar quirks | Use `TestClient(app)` and follow redirects carefully; assert cookie header and/or client.cookies |
| Duplicate name validation vs repository | Same strip+non-empty rule; shared refactor deferred |
| AC-P-023 wording vs stub | Stub is a deliberate create attempt path; detail message clear |
| Cookie special characters | MVP tests use simple ASCII names; value is trimmed plain text |
| 303 + TestClient | `follow_redirects=True` where needed; also assert Set-Cookie on POST response directly |
| Accidental Secure cookie on HTTP local | `secure=False` default |

## Out of scope (do not implement in #4)

* SSO, OAuth, passwords, demo login, RBAC, name ownership
* Full HTMX today board and status form chrome (#9)
* Real upsert of doing/blocked/next and field validation (#5)
* List statuses HTTP (#3)
* Schema/DDL changes; TZ changes
* Runbook body (#8); full suite expansion (#10) beyond identity tests
* Server-side session store; signed cookies (optional later)
* jinja2/HTMX CDN assets (unless absolutely required — plan says no)

## Open questions resolved in this plan

| # | Resolution |
|---|------------|
| Cookie max-age | **Session cookie** (omit max_age) |
| HTML vs JSON set-name | **HTML form** GET/POST `/identity` |
| Repository shared normalize | **Defer** — no repository edit required |
| AC-P-023 mechanism | **Stub `POST /status`** + `require_display_name` |
| Cookie name | `pulseboard_display_name` |

## Ready to implement?

- [x] Research complete and used as sole factual base
- [x] TEMP-3 AC-P-020–023 mapped to concrete steps/tests
- [x] Files, deps, risks, out-of-scope listed
- [x] Full HTMX board left to #9; upsert product left to #5
- [x] **No production code** in this phase
- [ ] User verifies Plan checklist in [`README.md`](README.md) before Implement (`continue=3`)

## Next

After Plan gate: `/rpi continue=3` implements this plan only; record results in `implement.md`.
