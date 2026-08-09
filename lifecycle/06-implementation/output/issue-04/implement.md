---
title: "Issue #4 implement — display name identity with cookie continuity"
description: Implementation summary for PulseBoard TEMP-3 / GitHub #4 following the approved plan
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-04
  - identity
  - cookie
  - implement
  - rpi
estimated_reading_time: 4
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4) — auth: display name identity with cookie continuity |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-3** |
| Phase | Implement (`/rpi continue=3`) |
| Status | Complete |
| Based on | [plan.md](plan.md) |
| Background | [research.md](research.md) |

## Summary

Implemented cookie-backed display-name identity on a minimal FastAPI surface:

* `src/pulseboard/identity.py` — normalize, cookie read/set, `require_display_name`
* `src/pulseboard/app.py` — `create_app()`, `GET/POST /identity`, stub `POST /status`
* Session cookie `pulseboard_display_name` (HttpOnly, SameSite=lax, Secure=False)
* Runtime deps: `fastapi`, `uvicorn`, `python-multipart`; dev: `httpx`
* Tests AC-P-020–023; prior #2/#6 suites still green

No SSO/OAuth, no HTMX board (#9), no real upsert (#5), no list-today HTTP (#3), no schema changes.

## Files changed

| Path | Change |
|------|--------|
| [pyproject.toml](../../../../pyproject.toml) | **Edited** — fastapi, uvicorn, python-multipart; httpx in dev |
| [src/pulseboard/identity.py](../../../../src/pulseboard/identity.py) | **Added** |
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | **Added** |
| [tests/test_identity.py](../../../../tests/test_identity.py) | **Added** |
| [src/pulseboard/repository.py](../../../../src/pulseboard/repository.py) | Unchanged |
| [src/pulseboard/db.py](../../../../src/pulseboard/db.py) | Unchanged |
| [src/pulseboard/today.py](../../../../src/pulseboard/today.py) | Unchanged |

## Commands run

```bash
# hve-env Python 3.12
python -m pip install -e ".[dev]"
python -m pip install 'python-multipart>=0.0.9'
python -m pytest tests/test_identity.py tests/test_status_repository.py \
  tests/test_instance_today.py -v
```

Result: **18 passed** in ~0.39s (1 Starlette/httpx deprecation warning).

Local run (not required for AC; runbook is #8):

```bash
uvicorn pulseboard.app:app --reload
# open http://127.0.0.1:8000/identity
```

## Acceptance criteria results

| AC / check | Result | Evidence |
|------------|--------|----------|
| AC-P-020 cookie continuity | **Pass** | `test_ac_p_020_set_name_cookie_and_subsequent_use`, change-name test |
| AC-P-021 reject blank | **Pass** | `test_ac_p_021_reject_blank_name` + normalize unit test |
| AC-P-022 no SSO/OAuth | **Pass** | `test_ac_p_022_no_sso_oauth_routes_or_deps` |
| AC-P-023 block create without identity | **Pass** | `test_ac_p_023_create_blocked_without_identity` |
| #2 / #6 regression | **Pass** | 11 prior tests still green |

## `.copilot-tracking/` notes

* [.copilot-tracking/changes/2026-08-09/issue-04-identity-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-04-identity-changes.md)
* Prior: research + plan pointers under `.copilot-tracking/research|plans/2026-08-09/`

## Deviations from plan

| Item | Notes |
|------|-------|
| `python-multipart` | **Added** — required by FastAPI for `Form(...)`; not named in plan deps table but necessary for HTML form POST |
| `swagger_ui_oauth2_redirect_url=None` | Disabled default FastAPI `/docs/oauth2-redirect` so product surface has no oauth-named route (AC-P-022) |
| AC-P-022 test | Checks banned path prefixes/exact paths rather than substring `oauth` over all routes (avoids false positives) |
| Repository shared normalize | Deferred as planned |
| Otherwise | Matches plan (session cookie, stub `/status` 200 JSON, inline HTML, no jinja2) |

## Scope confirmation

* Did **not** start #5, #3, #9, or Sprint 2
* Did **not** implement doing/blocked/next upsert or board list UI
* Did **not** add SSO/OAuth/password paths
* Did **not** change SQLite schema

## Ready for next issue?

- [x] Implement summary written
- [x] AC-P-020–023 automated evidence green
- [ ] User verifies Implement + Gate in [`README.md`](README.md) before issue #5

## Next

Sprint 1 order: issue **#5** — upsert today status (doing / blocked / next), using `require_display_name` and replacing the `/status` stub body.
