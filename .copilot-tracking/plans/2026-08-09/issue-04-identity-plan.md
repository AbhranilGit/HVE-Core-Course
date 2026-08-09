<!-- markdownlint-disable-file -->
# Plan pointer — Issue #4 display name identity

* Date: 2026-08-09
* Phase: Plan only (no production code)
* Canonical: lifecycle/06-implementation/output/issue-04/plan.md
* Based on: lifecycle/06-implementation/output/issue-04/research.md
* Status: Complete — ready for Implement gate

## Summary

* Option B: FastAPI + identity.py + GET/POST /identity cookie + stub POST /status
* Cookie: pulseboard_display_name, HttpOnly, session, SameSite=lax, Secure=False
* Deps: fastapi, uvicorn; httpx dev
* Tests: AC-P-020–023 via TestClient
* Out: HTMX board #9, upsert #5, list #3, SSO
