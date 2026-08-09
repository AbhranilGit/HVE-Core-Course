<!-- markdownlint-disable-file -->

---
title: "PulseBoard MVP code review after Sprint 1 and Sprint 2"
description: Severity-ranked review of MVP readiness across identity, create/list correctness, security basics, tests, and docs consistency
author: Task Reviewer
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - mvp
  - code-review
  - sprint-1
  - sprint-2
estimated_reading_time: 8
---

## Findings

Severity counts:

* Critical: 0
* Major: 1
* Minor: 2

### Major

1. Sprint 2 release-checklist traceability drift weakens release-gate reliability.
Evidence:
[lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md](../../08-delivery/output/v0.1.0-release-evidence-checklist.md#L42)
through
[lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md](../../08-delivery/output/v0.1.0-release-evidence-checklist.md#L48)
labels US-001 through US-007 coverage, but row semantics are mismatched (example: US-001 row points to core persistence evidence instead of identity evidence).
Impact:
Release reviewers can mark AC-008.1 complete with ambiguous story-to-evidence mapping.
Sprint 2 done status:
This is a blocker for clean sign-off of checklist readiness as authoritative release evidence.

### Minor

1. Test stack has recurring deprecation warning that should be resolved before release hardening closure.
Evidence:
[lifecycle/07-review/output/sprint-2-rpi-review.md](sprint-2-rpi-review.md#L42)
and
[lifecycle/07-review/output/sprint-1-rpi-review.md](sprint-1-rpi-review.md#L40)
show passing suites with Starlette TestClient deprecation warning.
Impact:
No current functional failure, but dependency upgrades may break or increase maintenance churn.

2. Identity model remains intentionally non-authenticated and cookie-tamperable, which is acceptable for local trusted MVP but should be called out as residual risk.
Evidence:
[src/pulseboard/identity.py](../../../src/pulseboard/identity.py#L54)
through
[src/pulseboard/identity.py](../../../src/pulseboard/identity.py#L64)
sets plain display-name cookie without signature or server-side verification.
Impact:
Any local actor can impersonate another display name by editing cookies; this matches current MVP assumptions but is a known integrity limitation.

## What passes

1. Correctness of create and list today status is strong and covered.
Evidence:
[src/pulseboard/status_service.py](../../../src/pulseboard/status_service.py#L29)
through
[src/pulseboard/status_service.py](../../../src/pulseboard/status_service.py#L63),
[src/pulseboard/repository.py](../../../src/pulseboard/repository.py#L36)
through
[src/pulseboard/repository.py](../../../src/pulseboard/repository.py#L122),
[tests/test_status_upsert.py](../../../tests/test_status_upsert.py),
[tests/test_status_list_today.py](../../../tests/test_status_list_today.py),
[tests/test_release_create_list.py](../../../tests/test_release_create_list.py).

2. Display-name identity flow works for MVP behavior.
Evidence:
[src/pulseboard/app.py](../../../src/pulseboard/app.py#L214)
through
[src/pulseboard/app.py](../../../src/pulseboard/app.py#L333),
[tests/test_identity.py](../../../tests/test_identity.py).

3. Sprint 2 runbook content is consistent with running app behavior.
Evidence:
[lifecycle/09-operations/output/runbook.md](../../09-operations/output/runbook.md)
aligns with startup route in
[src/pulseboard/app.py](../../../src/pulseboard/app.py#L338),
DB path behavior in
[src/pulseboard/db.py](../../../src/pulseboard/db.py#L33),
and timezone behavior in
[src/pulseboard/today.py](../../../src/pulseboard/today.py#L24).

4. Scope discipline is maintained: no SSO, notifications, or mobile features added.
Evidence:
[tests/test_identity.py](../../../tests/test_identity.py#L99),
[tests/test_ui_today_board.py](../../../tests/test_ui_today_board.py#L108),
and Sprint review outputs
[lifecycle/07-review/output/sprint-1-rpi-review.md](sprint-1-rpi-review.md),
[lifecycle/07-review/output/sprint-2-rpi-review.md](sprint-2-rpi-review.md).

## Execution status vs acceptance status

1. Execution status:
Sprint 1 and Sprint 2 artifacts are implemented, tests pass, and no workspace diagnostics errors were reported.
2. Acceptance status:
Sprint 1 thin-slice acceptance remains pass.
Sprint 2 is near-complete but not cleanly ready for final release sign-off until checklist traceability labels are corrected.

## Follow-ups

1. ~~Fix AC-008.1 evidence-index row labels~~ — **Done** 2026-08-09: checklist US-001–US-007 rows now match PRD meanings and issue evidence; see updated [v0.1.0-release-evidence-checklist.md](../../08-delivery/output/v0.1.0-release-evidence-checklist.md) and [sprint-2-rpi-review.md](sprint-2-rpi-review.md).
2. Track and resolve the Starlette TestClient deprecation warning path in dependency maintenance.
3. Keep the current identity-cookie integrity limitation explicitly documented as MVP trusted-environment risk until a future scope change introduces stronger identity controls.
4. Before tag: fill candidate SHA / pytest run record / reviewer sign-off fields in the release checklist (AC-008.3–AC-008.4).
