<!-- markdownlint-disable-file -->
# Changes — Issue #6 instance today helper

* Date: 2026-08-09
* Plan: lifecycle/06-implementation/output/issue-06/plan.md
* Implement summary: lifecycle/06-implementation/output/issue-06/implement.md
* Validation: pytest test_instance_today + test_status_repository — 11 passed (hve-env 3.12.13)

## Added

* src/pulseboard/today.py
* tests/test_instance_today.py

## Modified

* src/pulseboard/repository.py — list_statuses_for_today

## Removed

* (none)

## Deviations

* No __init__.py re-exports
* tz param on list_statuses_for_today left unannotated
