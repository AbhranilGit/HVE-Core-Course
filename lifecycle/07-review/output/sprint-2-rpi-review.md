<!-- markdownlint-disable-file -->

---
title: "Sprint 2 RPI review - PulseBoard harden and package"
description: Review of Sprint 2 implementation status and acceptance outcomes against sprint plan and PRD AC
author: Task Reviewer
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - sprint-2
  - review
  - release-readiness
  - acceptance
estimated_reading_time: 9
---

## Review metadata

| Field | Value |
| --- | --- |
| Review scope | PulseBoard Sprint 2 only (#10 #8 #7): tests, runbook, release checklist |
| Sprint plan | [lifecycle/05-sprint-planning/output/sprint-plan.md](../../05-sprint-planning/output/sprint-plan.md) |
| PRD source | [lifecycle/03-product-definition/output/prd.md](../../03-product-definition/output/prd.md) |
| Backlog source | [lifecycle/04-decomposition/output/backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) |
| Changes scope | [.copilot-tracking/changes/2026-08-09](../../../.copilot-tracking/changes/2026-08-09) |
| Research scope | [.copilot-tracking/research/2026-08-09](../../../.copilot-tracking/research/2026-08-09) |
| Sprint 2 implementation artifacts | [lifecycle/06-implementation/output/issue-10](../../06-implementation/output/issue-10), [lifecycle/06-implementation/output/issue-08](../../06-implementation/output/issue-08), [lifecycle/06-implementation/output/issue-07](../../06-implementation/output/issue-07) |
| Operational doc reviewed | [lifecycle/09-operations/output/runbook.md](../../09-operations/output/runbook.md) |
| Release checklist reviewed | [lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md](../../08-delivery/output/v0.1.0-release-evidence-checklist.md) |
| Prior sprint review | [lifecycle/07-review/output/sprint-1-rpi-review.md](sprint-1-rpi-review.md) |
| Review date | 2026-08-09 |

## Method

1. Compared Sprint 2 definition of done in sprint plan to Sprint 2 outputs (#10, #8, #7).
2. Cross-checked TEMP-7, TEMP-8, TEMP-9 issue AC against implementation artifacts.
3. Reviewed source tests and documentation artifacts for direct requirement coverage.
4. Ran targeted and full test execution checks.
5. Separated execution status from acceptance outcomes.

## Execution status

| Item | Status | Evidence |
| --- | --- | --- |
| Issue #10 implemented with AC-mapped tests | Complete | [lifecycle/06-implementation/output/issue-10/implement.md](../../06-implementation/output/issue-10/implement.md), [tests/test_release_create_list.py](../../../tests/test_release_create_list.py) |
| Issue #8 implemented with runbook output | Complete | [lifecycle/06-implementation/output/issue-08/implement.md](../../06-implementation/output/issue-08/implement.md), [lifecycle/09-operations/output/runbook.md](../../09-operations/output/runbook.md) |
| Issue #7 implemented with release checklist output | Complete | [lifecycle/06-implementation/output/issue-07/implement.md](../../06-implementation/output/issue-07/implement.md), [lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md](../../08-delivery/output/v0.1.0-release-evidence-checklist.md) |
| Targeted Sprint 2 test execution | Pass with warning | `4 passed, 1 warning` from `python -m pytest tests/test_release_create_list.py -q --tb=short` |
| Full suite execution status | Pass with warning | `42 passed, 1 warning` from `python -m pytest tests/ -q --tb=short` |
| Workspace diagnostics (src/tests) | Pass | No diagnostics errors |

## Acceptance outcomes

### 1) Automated tests cover create/upsert and list today board (#10)

Outcome: Pass

Evidence:

* Coverage and assertions present in [tests/test_release_create_list.py](../../../tests/test_release_create_list.py):
  * create and list exercised (`test_ac_p_060_create_and_list_release_bar_smoke`)
  * return values by display name (`test_ac_p_061_create_then_list_returns_today_values`)
  * same-name upsert no duplicate (`test_ac_p_062_same_name_twice_has_one_latest_row`)
  * prior-day exclusion (`test_ac_p_063_prior_day_fixture_excluded_from_today_list`)
* Execution evidence recorded in [lifecycle/06-implementation/output/issue-10/implement.md](../../06-implementation/output/issue-10/implement.md)

### 2) Runbook documents required operator path (#8)

Outcome: Pass

Evidence in [lifecycle/09-operations/output/runbook.md](../../09-operations/output/runbook.md):

* prerequisites (`Python 3.12+`, recommended `hve-env`)
* install command (`python -m pip install -e ".[dev]"`)
* start command (`uvicorn pulseboard.app:app --reload`)
* app URL (`http://127.0.0.1:8000/`)
* local-first model statement
* DB path behavior with `PULSEBOARD_DB_PATH`
* today/timezone behavior with `PULSEBOARD_TZ`
* pytest command (`python -m pytest tests/ -q`)

### 3) v0.1.0 checklist maps PRD AC-008.*, requires absences, test evidence, reviewer sign-off (#7)

Outcome: Pass (traceability defect corrected 2026-08-09)

What passes:

* Checklist has explicit AC-008.1, AC-008.2, AC-008.3, and AC-008.4 sections in [lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md](../../08-delivery/output/v0.1.0-release-evidence-checklist.md)
* Out-of-scope absence confirmations are present for SSO/OAuth, notifications/email/Slack bots, and mobile clients
* Automated create/list evidence references and run-record fields are present
* Reviewer sign-off rows before final pre-tag decision are present
* AC-008.1 evidence index now maps US-001–US-007 to PRD meanings and matching issue evidence (US-001→#4/#9 identity, US-006→#2 persistence, US-007→#8/runbook, etc.), plus a PRD→issue quick matrix

Closed defect:

* Previous mislabeling (e.g. US-001 paired with persistence/#2) was corrected in the checklist AC-008.1 section.

### 4) Sprint 2 scope discipline (harden/package only; no new MVP product features)

Outcome: Pass

Evidence:

* Sprint 2 issue outputs are docs/tests oriented: [lifecycle/06-implementation/output/issue-10/implement.md](../../06-implementation/output/issue-10/implement.md), [lifecycle/06-implementation/output/issue-08/implement.md](../../06-implementation/output/issue-08/implement.md), [lifecycle/06-implementation/output/issue-07/implement.md](../../06-implementation/output/issue-07/implement.md)
* No Sprint 2 requirement to add new endpoints/features; corresponding implement logs explicitly state no feature expansion
* Out-of-scope controls are explicitly represented in runbook and release checklist

## Findings

Severity counts:

* Critical: 0
* Major: 0 (AC-008.1 labeling defect closed)
* Minor: 1

### Minor

1. Minor - recurring Starlette/TestClient deprecation warning remains unresolved.
   * Evidence: targeted and full test runs both emit `StarletteDeprecationWarning` about `httpx` and `starlette.testclient`.
   * Impact: no current break, but future dependency updates may add friction.

## Defects and follow-ups

Open defects:

* None blocking Sprint 2 acceptance.

Follow-up work items:

1. Add final candidate run metadata (commit SHA, exact command outputs, operator, timestamp) in the checklist when executing pre-tag review (AC-008.3 / AC-008.4 fields).
2. Track and resolve the `httpx`/`starlette.testclient` deprecation warning in dependency maintenance.

## Overall status

✅ Complete for Sprint 2 acceptance review (harden/package + release checklist traceability).

Rationale:

* Sprint 2 execution status is green and all requested artifacts exist.
* AC-008.1 US→evidence mapping matches PRD story semantics after checklist correction.
* Remaining items are non-blocking pre-tag fill-ins and dependency hygiene, not Sprint 2 scope failures.
