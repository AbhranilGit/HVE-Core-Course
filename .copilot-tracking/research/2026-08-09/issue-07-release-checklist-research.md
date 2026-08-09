<!-- markdownlint-disable-file -->

---
title: "Issue #7 research - v0.1.0 release evidence checklist"
description: Research-only findings for PulseBoard TEMP-9 and GitHub issue #7 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-07
  - release
  - checklist
  - research
  - rpi
estimated_reading_time: 8
---

## Document control

| Field | Value |
| --- | --- |
| Issue | [#7](https://github.com/AbhranilGit/HVE-Core-Course/issues/7) - docs: v0.1.0 release evidence checklist |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-9 |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete - ready for Plan gate |
| Production code | None (this phase) |
| Sprint | 3 of 3 (Sprint 2) |
| Depends on | #10 evidence and completed Sprint 1 P0 AC |

## Scope summary (authoritative)

From TEMP-9 and issue #7:

In scope:

* Create an in-repo release checklist for `v0.1.0`
* Gate tag readiness on PRD US-008 AC-008.1 to AC-008.4
* Require explicit absence confirmations for out-of-scope items
* Require recorded automated create/list test evidence
* Include explicit reviewer confirmation before tag

Out of scope:

* Sprint ordering changes
* Performing the release tag itself
* Product feature work under src/tests

Acceptance criteria to drive planning:

| ID | Criterion | Source |
| --- | --- | --- |
| AC-P-080 | Checklist exists in-repo and maps to PRD AC-008.1 to AC-008.4 | TEMP-9 / PRD US-008 |
| AC-P-081 | Checklist requires confirmation that SSO/OAuth, notifications/email/Slack bots, and mobile are absent | TEMP-9 / PRD AC-008.2 |
| AC-P-082 | Checklist requires recorded evidence that tests cover create status and list/view today board | TEMP-9 / PRD AC-008.3 |
| AC-P-083 | Checklist includes explicit reviewer confirmation step before tag | TEMP-9 / PRD AC-008.4 |

## PRD constraints relevant to issue #7

From [lifecycle/03-product-definition/output/prd.md](../../03-product-definition/output/prd.md):

* US-008 defines thin-slice release bar for `v0.1.0`
* AC-008.1 requires US-001 through US-007 P0 acceptance at candidate build time
* AC-008.2 requires out-of-scope absences (SSO/OAuth, notifications/email/Slack bots, mobile)
* AC-008.3 requires automated create/list coverage with recorded results
* AC-008.4 requires explicit reviewer confirmation before tag
* G-005 and SM-05 reinforce no scope creep at release gate

## Release evidence already present

### Completed issue implementation artifacts

The following issue implement artifacts are present and marked complete:

* [lifecycle/06-implementation/output/issue-02/implement.md](../issue-02/implement.md)
* [lifecycle/06-implementation/output/issue-06/implement.md](../issue-06/implement.md)
* [lifecycle/06-implementation/output/issue-04/implement.md](../issue-04/implement.md)
* [lifecycle/06-implementation/output/issue-05/implement.md](../issue-05/implement.md)
* [lifecycle/06-implementation/output/issue-03/implement.md](../issue-03/implement.md)
* [lifecycle/06-implementation/output/issue-09/implement.md](../issue-09/implement.md)
* [lifecycle/06-implementation/output/issue-10/implement.md](../issue-10/implement.md)
* [lifecycle/06-implementation/output/issue-08/implement.md](../issue-08/implement.md)

These provide AC-mapped results, scope checks, and command evidence that can be referenced by the release checklist.

### Automated create/list evidence

Existing direct evidence for create/list coverage and execution results already exists:

* [tests/test_release_create_list.py](../../../../tests/test_release_create_list.py) introduced by issue #10
* [lifecycle/06-implementation/output/issue-10/implement.md](../issue-10/implement.md) records targeted (`4 passed`) and full-suite (`42 passed`) results
* Earlier complementary evidence exists in issue #5, #3, and #9 implement artifacts

### Out-of-scope absence evidence

Absence checks are already recorded in multiple implement artifacts:

* No SSO/OAuth assertions: issue #4, issue #9, issue #8
* No notifications/mobile/websocket checks: issue #9 and issue #8
* No product feature additions during docs-only issues: issue #8

### Tracking artifacts available

Evidence-style change logs already exist under:

* [.copilot-tracking/changes/2026-08-09/issue-02-sqlite-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-02-sqlite-changes.md)
* [.copilot-tracking/changes/2026-08-09/issue-03-list-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-03-list-changes.md)
* [.copilot-tracking/changes/2026-08-09/issue-04-identity-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-04-identity-changes.md)
* [.copilot-tracking/changes/2026-08-09/issue-05-upsert-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-05-upsert-changes.md)
* [.copilot-tracking/changes/2026-08-09/issue-06-today-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-06-today-changes.md)
* [.copilot-tracking/changes/2026-08-09/issue-09-ui-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-09-ui-changes.md)
* [.copilot-tracking/changes/2026-08-09/issue-10-tests-changes.md](../../../../.copilot-tracking/changes/2026-08-09/issue-10-tests-changes.md)
* [.copilot-tracking/changes/2026-08-09/issue-08-runbook-implement.md](../../../../.copilot-tracking/changes/2026-08-09/issue-08-runbook-implement.md)

## Gaps identified for issue #7

Current gap is document-level consolidation, not feature-level implementation.

Missing today:

* No release checklist document exists under delivery or review outputs
* No single checklist currently maps AC-008.1 through AC-008.4 in one place
* No unified reviewer sign-off block before tag is present yet

Evidence:

* [lifecycle/08-delivery/output](../../08-delivery/output) contains only `.gitkeep`
* [lifecycle/07-review/output](../../07-review/output) contains only `.gitkeep`
* No release checklist file found by repository search

## Repo patterns and placement constraints

Relevant repository patterns:

* Stage outputs are stored under `lifecycle/NN-*/output/`
* Issue prompt for #7 says to prefer `lifecycle/08-delivery/output/` or issue-stated path
* Existing implementation issue artifacts stay in `lifecycle/06-implementation/output/issue-07/`
* `.copilot-tracking/` keeps evidence-oriented change logs and session traces

## Design options for plan

### Option A (recommended)

Create a dedicated checklist file under delivery output, for example:

* `lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md`

Pros:

* Aligns with issue prompt preference for delivery path
* Clear release-gate ownership at stage 8
* Keeps issue #7 deliverable separate from issue-phase logs

Cons:

* Requires references to evidence spread across stage 6 artifacts

### Option B

Place checklist under review output (`lifecycle/07-review/output/`).

Pros:

* Fits review semantics for sign-off

Cons:

* Conflicts with issue #7 prompt preference toward delivery path

### Option C

Embed checklist only in `lifecycle/06-implementation/output/issue-07/implement.md`.

Pros:

* Minimal file count

Cons:

* Weak release discoverability
* Poor fit for stage-based handoff

Research recommendation: Option A with explicit links back to stage-6 evidence artifacts.

## Planning inputs required next

The plan should define:

1. Exact checklist file path under delivery output
2. Checklist structure mapped line-by-line to AC-P-080 through AC-P-083
3. Evidence link set for:
  * US-001 through US-007 completion checks
  * out-of-scope absence checks
  * automated create/list test execution records
4. Explicit reviewer confirmation fields for pre-tag gate
5. Scope controls that prevent feature additions in this issue

## Open questions (non-blocking for research)

1. Should AC-008.1 reference only issue implement artifacts, or also include a short PRD-to-issue matrix section in the checklist?
2. Should reviewer confirmation be a single signature/date row or per-AC sign-off rows?
3. Should checklist include a field for the exact candidate commit/tag SHA even though tagging itself is out of scope?

## Ready for plan?

- [x] TEMP-9 scope and AC-P-080 through AC-P-083 captured
- [x] PRD US-008 constraints captured for release gate
- [x] Existing release evidence inventory captured
- [x] Delivery/review output gaps identified
- [x] No production code written in this phase
- [ ] User verifies Research checklist in [README.md](README.md) before Plan (`continue=2`)

## Next

After Research gate: run `/rpi continue=2` to write issue-07 plan only.
