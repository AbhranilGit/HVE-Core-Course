<!-- markdownlint-disable-file -->
# Changes - Issue #3 list statuses for today

| Field | Value |
|-------|-------|
| Related plan | `lifecycle/06-implementation/output/issue-03/plan.md` |
| Implementation date | 2026-08-09 |
| Issue | GitHub #3 / TEMP-5 |

## Summary

Added a read API for today board statuses and tests for AC-P-040 to AC-P-045. Implementation reuses existing repository today-list helper and preserves deterministic ordering.

## Added

* `tests/test_status_list_today.py`

## Modified

* `src/pulseboard/app.py` - added `GET /statuses/today`
* `lifecycle/06-implementation/output/issue-03/implement.md` - implementation evidence

## Removed

* None

## Validation

```text
33 passed, 1 warning
```

## Deviations

* None

## Release summary

Issue #3 TEMP-5 is complete. Sprint 1 API path now has write (#5) and list (#3). HTMX board remains in #9.
