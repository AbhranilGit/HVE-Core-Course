<!-- markdownlint-disable-file -->
# Research pointer — Issue #5 upsert today status

* Date: 2026-08-09
* Phase: Research only (no production code)
* Canonical: lifecycle/06-implementation/output/issue-05/research.md
* Status: Complete — ready for Plan gate

## Summary

* TEMP-4 / #5: upsert today status for cookie display name; ≥1 field non-empty; day = instance today; no lock
* Deps #2/#6/#4 in place; replace POST /status stub; add create_app(db_path) + service validation
* Out: HTMX UI #9, list HTTP #3, prior-day edit, SSO
* AC-P-030–034

## Selected approach

Service validate + repository.upsert_status + FastAPI POST /status with form fields
