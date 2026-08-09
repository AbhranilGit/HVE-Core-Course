<!-- markdownlint-disable-file -->
# Changes — Issue #2 SQLite schema and status repository

* Date: 2026-08-09
* Plan: lifecycle/06-implementation/output/issue-02/plan.md
* Implement summary: lifecycle/06-implementation/output/issue-02/implement.md
* Validation: pytest tests/test_status_repository.py — 5 passed (hve-env Python 3.12.13)

## Added

* src/pulseboard/models.py
* src/pulseboard/db.py
* src/pulseboard/repository.py
* tests/test_status_repository.py

## Modified

* (none required)

## Removed

* (none)

## Deviations

* No __init__.py re-exports (optional in plan)
