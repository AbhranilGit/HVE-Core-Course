<!-- markdownlint-disable-file -->
# Plan pointer — Issue #5 upsert today status

* Date: 2026-08-09
* Phase: Plan only (no production code)
* Canonical: lifecycle/06-implementation/output/issue-05/plan.md
* Based on: lifecycle/06-implementation/output/issue-05/research.md
* Status: Complete — ready for Implement gate

## Summary

* status_service.py: validate ≥1 field; upsert_today_status via default_status_day_str + repository
* create_app(db_path=...) + lifespan init_db; replace POST /status stub with form upsert → 200 JSON
* Tests AC-P-030–034; update test_identity stub expectations
* Out: list #3, UI #9, lock, schema change
