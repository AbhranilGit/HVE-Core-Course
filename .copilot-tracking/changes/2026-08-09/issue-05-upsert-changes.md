<!-- markdownlint-disable-file -->
# Changes — Issue #5 upsert today status

| Field | Value |
|-------|-------|
| Related plan | `lifecycle/06-implementation/output/issue-05/plan.md` |
| Implementation date | 2026-08-09 |
| Issue | GitHub #5 / TEMP-4 |

## Summary

Added status validation/service layer and wired `POST /status` to upsert instance-today status for the cookie display name. Full field replace; reject all-empty; no lock; no list/UI.

## Added

* `src/pulseboard/status_service.py`
* `tests/test_status_upsert.py`
* `lifecycle/06-implementation/output/issue-05/implement.md` (completed)

## Modified

* `src/pulseboard/app.py` — `create_app(db_path=)`, init_db/lifespan, real POST /status JSON
* `tests/test_identity.py` — tmp db + real upsert payloads

## Removed

* Stub `POST /status` body `{ok, status: not_implemented}`

## Deviations

* Eager `init_db` at factory time for reliable TestClient schema
* Context-manager TestClient fixtures

## Validation

```text
27 passed, 1 warning
```

## Release summary

Issue #5 TEMP-4 complete. Sprint 1 remaining: #3 list-today HTTP, then #9 HTMX board.
