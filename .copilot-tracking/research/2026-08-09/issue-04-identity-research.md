<!-- markdownlint-disable-file -->
# Research pointer — Issue #4 display name identity

* Date: 2026-08-09
* Phase: Research only (no production code)
* Canonical: lifecycle/06-implementation/output/issue-04/research.md
* Status: Complete — ready for Plan gate

## Summary

* TEMP-3 / #4: cookie-backed display name; reject blank; no SSO; block create without identity
* Selected approach: introduce FastAPI + identity helpers + minimal set-name path + require_display_name
* Full HTMX board deferred to #9; upsert product rules to #5
* Repo today: repository._require_display_name exists; no HTTP app; dependencies=[]

## AC

* AC-P-020 cookie continuity
* AC-P-021 reject blank
* AC-P-022 no SSO/OAuth
* AC-P-023 block create without identity
