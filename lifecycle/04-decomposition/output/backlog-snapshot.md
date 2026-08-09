---
title: PulseBoard MVP backlog snapshot
description: Decomposition backlog derived from the accepted PRD user stories and acceptance criteria for GitHub issue creation
author: GitHub Backlog Manager
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - backlog
  - github-issues
  - mvp
estimated_reading_time: 10
---

## Document control

| Field | Value |
|-------|-------|
| Product | PulseBoard MVP |
| Stage | 4 — Decomposition |
| Source PRD | [prd.md](../../03-product-definition/output/prd.md) (Accepted) |
| Source ADRs | [adr/](../../03-product-definition/output/adr/) |
| Repository | [AbhranilGit/HVE-Core-Course](https://github.com/AbhranilGit/HVE-Core-Course) |
| Sprint ordering | Not started (Stage 5) |
| Implementation code | Not in this step |
| GitHub create status | **9 issues created 2026-08-09** on AbhranilGit/HVE-Core-Course |

## Intent

Translate accepted PRD P0 user stories and AC into a small, finishable MVP backlog. Labels are limited to `api`, `ui`, `auth`, `docs`, and `tests`. No features outside PRD in-scope.

## Thin vertical slice path

Suggested implementation path only (not sprint assignment):

1. Schema/persistence (`api`)
2. Instance today (`api`)
3. Display name cookie (`auth`)
4. Upsert today status (`api`)
5. List today (`api`)
6. HTMX board + form (`ui`)
7. Create/list tests (`tests`)
8. Runbook (`docs`)
9. v0.1.0 checklist (`docs`)

## Issue index

| Temp ID | Title | Label | PRD trace | GitHub |
|---------|-------|-------|-----------|--------|
| TEMP-1 | api: SQLite schema and status repository for today | api | FR-008, US-006 | [#2](https://github.com/AbhranilGit/HVE-Core-Course/issues/2) |
| TEMP-2 | api: instance today helper and day defaulting | api | FR-007, AC-002.2, AC-004.3 | [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6) |
| TEMP-3 | auth: display name identity with cookie continuity | auth | US-001, FR-001, AC-001.* | [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4) |
| TEMP-4 | api: upsert today status (doing / blocked / next) | api | US-002, US-003, FR-002–004 | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) |
| TEMP-5 | api: list statuses for today board | api | US-004, US-005, FR-005–006 | [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3) |
| TEMP-6 | ui: today board and status form (HTMX) | ui | §5 UX, US-001–005 | [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9) |
| TEMP-7 | tests: create status and list today board | tests | AC-008.3, NFR-008, US-008 | [#10](https://github.com/AbhranilGit/HVE-Core-Course/issues/10) |
| TEMP-8 | docs: local-first runbook and start path | docs | US-007, FR-009, AC-007.* | [#8](https://github.com/AbhranilGit/HVE-Core-Course/issues/8) |
| TEMP-9 | docs: v0.1.0 release evidence checklist | docs | US-008, FR-010, AC-008.* | [#7](https://github.com/AbhranilGit/HVE-Core-Course/issues/7) |

## PRD coverage matrix

| PRD story | Covered by |
|-----------|------------|
| US-001 Identify display name | #4, #9 |
| US-002 Post today’s status | #5, #9 |
| US-003 Edit same day | #5, #9 |
| US-004 View today’s board | #3, #9 |
| US-005 Spot blockers | #3, #9 |
| US-006 Persist across restart | #2 |
| US-007 Run from docs | #8 |
| US-008 v0.1.0 bar | #10, #7 |

## Explicitly not backloged

From PRD out of scope (do not file as MVP features):

* SSO / OAuth
* Notifications, email, Slack bots
* Mobile application
* Multi-tenant SaaS
* Real-time websockets
* Historical analytics / multi-day history UI
* RBAC
* Rich media attachments
* Full project tracker

## Issue specs

Bodies below match the created GitHub issues. Index links are authoritative.

### TEMP-1 — api: SQLite schema and status repository for today

* **Label:** `api`
* **GitHub:** [#2](https://github.com/AbhranilGit/HVE-Core-Course/issues/2)

#### Body

## Summary

Add local SQLite persistence for PulseBoard status rows so today’s board survives process restart on one machine.

## Context

* PRD: FR-008, US-006 (AC-006.1, AC-006.2), NFR-002
* ADR: SQLite local persistence; status domain model unique key `(display_name, status_day)`
* Stack: Python 3.12+, DB file on host (configurable path documented later in docs issue)

## Scope

* Status table (or equivalent) with: display_name, status_day, doing, blocked, next; optional created_at/updated_at
* Unique constraint on `(display_name, status_day)`
* Schema initialize on startup (simple path OK)
* Repository/data-access helpers for upsert and list-by-day (callers may land in sibling issues)
* Default/configurable DB file path suitable for local run and tests (temp DB in tests)

## Out of scope

* Cloud DB, Postgres, multi-tenant schemas, replication
* Multi-day history UI
* Application UI (see ui issue)

## Acceptance criteria

* [ ] AC-P-001 Given a configured local DB path, when the app initializes, then the status schema exists and is usable for writes/reads. (PRD FR-008)
* [ ] AC-P-002 Given two writes with the same display_name and status_day, when persisted, then only one row exists for that pair (unique enforced). (PRD FR-004, ADR status domain)
* [ ] AC-P-003 Given data written to the DB file, when the process restarts against the same file, then prior rows remain readable. (PRD AC-006.1)
* [ ] AC-P-004 Persistence is file-local SQLite (or equivalent local file DB), not a required cloud database. (PRD AC-006.2)

### TEMP-2 — api: instance today helper and day defaulting

* **Label:** `api`
* **GitHub:** [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6)

#### Body

## Summary

Implement instance-level “today” as a calendar date in the instance timezone so status defaults and the today board share one day boundary.

## Context

* PRD: FR-007, AC-002.2, AC-004.3, Glossary “Today”
* ADR: today-instance-timezone (host local default; optional `PULSEBOARD_TZ`)

## Scope

* `instance_today()` (or equivalent) returning calendar date in instance TZ
* Default TZ = host local; optional env override with IANA name
* All MVP create defaults and today-board filters use this helper
* Clock/date injectable or overrideable in tests

## Out of scope

* Per-user timezones
* Multi-day history UI
* Geo detection

## Acceptance criteria

* [ ] AC-P-010 Given no TZ override, when computing today, then the date matches the host local calendar date. (PRD §4.1 OQ-04, ADR)
* [ ] AC-P-011 Given `PULSEBOARD_TZ` (or documented equivalent) is set to a valid IANA zone, when computing today, then the date uses that zone. (ADR today)
* [ ] AC-P-012 Given status create without another day, when saved via domain rules, then `status_day` equals `instance_today()`. (PRD AC-002.2)
* [ ] AC-P-013 Given rows only on a prior calendar day, when listing today, then those rows are excluded. (PRD AC-004.3)

### TEMP-3 — auth: display name identity with cookie continuity

* **Label:** `auth`
* **GitHub:** [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4)

#### Body

## Summary

Let a user set a non-empty display name and keep it for subsequent status actions via an HTTP cookie on the local instance.

## Context

* PRD: US-001, FR-001, AC-001.1–AC-001.3
* ADR: local-identity-display-name (cookie continuity; no passwords/SSO)

## Scope

* UI or request path to submit display name (minimal form OK; full page chrome may ship with ui issue)
* Reject empty/whitespace-only names after trim
* Set HTTP cookie with accepted display name for the app scope
* Read cookie on later status actions; allow explicit change of name
* No SSO/OAuth/password paths

## Out of scope

* Demo login, shared password, RBAC, SSO/OAuth
* Claiming exclusive ownership of a name across users (trusted team model)

## Acceptance criteria

* [ ] AC-P-020 Given no display name set, when I submit a non-empty display name, then the app accepts it and uses it for subsequent status actions in that browser via cookie. (PRD AC-001.1, ADR identity)
* [ ] AC-P-021 Given empty or whitespace-only display name, when I save it, then the app rejects it and does not attribute statuses to a blank name. (PRD AC-001.2)
* [ ] AC-P-022 Given the MVP build, when inspecting identity options, then there is no SSO/OAuth sign-in path. (PRD AC-001.3)
* [ ] AC-P-023 Given required identity is missing, when creating a status is attempted, then create is blocked with a clear prompt or failure. (PRD AC-002.4)

### TEMP-4 — api: upsert today status (doing / blocked / next)

* **Label:** `api`
* **GitHub:** [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5)

#### Body

## Summary

Implement create-or-update of today’s status for the current display name with doing, blocked, and next plain-text fields.

## Context

* PRD: US-002, US-003, FR-002, FR-003, FR-004, AC-002.*, AC-003.*
* ADR: status-domain-model (upsert; ≥1 field non-empty; no standup lock)

## Scope

* Endpoint or service method to upsert status for `(display_name, instance_today())`
* Fields: doing, blocked, next (plain text)
* Validation: require display name; require at least one of three fields non-empty after trim
* Same-day update replaces values; does not insert a second row
* No lock-after-standup control

## Out of scope

* Multiple statuses per person per day
* Prior-day edit product / history journal
* Blocked flag, notifications, attachments
* UI markup (ui issue may call this API)

## Acceptance criteria

* [ ] AC-P-030 Given valid display name and no status for today, when I submit doing/blocked/next with at least one non-empty, then a status for today is stored under my display name. (PRD AC-002.1, field rule)
* [ ] AC-P-031 Given create without choosing another day, when saved, then day is instance today. (PRD AC-002.2)
* [ ] AC-P-032 Given an existing today status for my display name, when I submit new values, then the board data shows one updated row (not a second row). (PRD AC-003.1, FR-004)
* [ ] AC-P-033 Given update/create where all three fields are empty/whitespace, when submitted, then the app rejects the write. (PRD US-002 field rule, AC-003.2)
* [ ] AC-P-034 Given MVP, when searching for lock-after-standup, then no such control exists. (PRD AC-003.3)

### TEMP-5 — api: list statuses for today board

* **Label:** `api`
* **GitHub:** [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3)

#### Body

## Summary

Provide a list of all statuses for `instance_today()` including display name, doing, blocked, and next for the facilitator board.

## Context

* PRD: US-004, US-005, FR-005, FR-006, AC-004.*, AC-005.*
* ADR: status-domain-model board projection; blocked free text only

## Scope

* Query/list API or service returning today’s statuses
* Each item includes display_name, doing, blocked, next
* Empty list is valid (not an error)
* Deterministic ordering (implementation choice; keep stable)
* Distinct display names remain distinct rows

## Out of scope

* Blocked-only filter chip, workflow states, SLA, notifications
* Historical days UI
* Real-time websocket push

## Acceptance criteria

* [ ] AC-P-040 Given zero statuses for today, when listing today, then the result is an empty collection suitable for an empty-state UI (not a hard failure). (PRD AC-004.1)
* [ ] AC-P-041 Given one or more statuses for today, when listing today, then each includes display name, doing, blocked, and next. (PRD AC-004.2, FR-006)
* [ ] AC-P-042 Given only prior-day statuses exist, when listing today, then they are not included. (PRD AC-004.3)
* [ ] AC-P-043 Given multiple distinct display names posted today, when listing, then each person has a distinguishable row (no silent cross-name overwrite). (PRD AC-004.4)
* [ ] AC-P-044 Given a non-empty blocked value on a today row, when listed, then blocked text is present for facilitator scan. (PRD AC-005.1)
* [ ] AC-P-045 Given blocked empty but doing or next filled, when listed, then the row still appears with blocked empty/absent. (PRD AC-005.2)

### TEMP-6 — ui: today board and status form (HTMX)

* **Label:** `ui`
* **GitHub:** [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9)

#### Body

## Summary

Ship a browser UI to set display name, submit/edit today’s doing/blocked/next, and view today’s team board using server-rendered HTML with HTMX-friendly progressive enhancement.

## Context

* PRD: §5 UX/UI, journeys, US-001–US-005 user-visible paths, AC-002.3
* ADR: web-stack-fastapi-htmx; no SPA/mobile/websockets required

## Scope

* Page(s) for: display name entry/confirm, status form (doing/blocked/next), today’s board table/list
* Empty board state copy that is not an error
* After successful save, user can see own values on today’s board without chat
* Keyboard-usable core form and board (PRD NFR-006 best effort)
* Wire to auth cookie + upsert + list behaviors from sibling issues

## Out of scope

* Design system / pixel-perfect branding
* Mobile native app
* Websocket live updates
* Multi-day history navigation
* SSO UI

## Acceptance criteria

* [ ] AC-P-050 Given a running local app, when I open the UI, then I can set display name, enter doing/blocked/next, and submit. (PRD §5 UX, US-001/US-002)
* [ ] AC-P-051 Given a successful save with valid identity, when I view today’s board, then my new/updated values appear without using chat. (PRD AC-002.3, AC-003.1)
* [ ] AC-P-052 Given zero posts today, when I open the board, then I see a clear empty state (not a crash/error page). (PRD AC-004.1)
* [ ] AC-P-053 Given multiple today posts, when I view the board, then each row shows display name, doing, blocked, and next. (PRD AC-004.2, AC-005.1)
* [ ] AC-P-054 Given MVP UI, when inspecting for SSO, lock-after-standup, blocked workflow, or notifications, then they are absent. (PRD AC-001.3, AC-003.3, AC-005.3)

### TEMP-7 — tests: create status and list today board

* **Label:** `tests`
* **GitHub:** [#10](https://github.com/AbhranilGit/HVE-Core-Course/issues/10)

#### Body

## Summary

Add automated tests that cover create (upsert) status and list/view today’s board behaviors required before tagging v0.1.0.

## Context

* PRD: AC-008.3, NFR-008, US-008
* BRD quality constraint: tests for create/list

## Scope

* Pytest tests using isolated temp SQLite DB
* Cover: create today status; reject invalid empty fields / blank name as applicable; list today; exclude prior day; upsert does not duplicate row
* Document how to run tests (`pytest`) for release evidence

## Out of scope

* Full browser E2E suite (optional later)
* Load testing beyond smoke

## Acceptance criteria

* [ ] AC-P-060 Given the test suite, when run on a clean env, then automated tests exercise **create status** and **list/view today’s board** and pass. (PRD AC-008.3, NFR-008)
* [ ] AC-P-061 Given create then list today, when tests run, then stored values are returned for today under the display name. (PRD AC-002.1, AC-004.2)
* [ ] AC-P-062 Given an upsert path test, when the same name posts twice today, then only one row exists with latest values. (PRD AC-003.1, FR-004)
* [ ] AC-P-063 Given prior-day data in the DB fixture, when listing today, then prior-day rows are not returned. (PRD AC-004.3)

### TEMP-8 — docs: local-first runbook and start path

* **Label:** `docs`
* **GitHub:** [#8](https://github.com/AbhranilGit/HVE-Core-Course/issues/8)

#### Body

## Summary

Document a tribal-knowledge-free start path so a new teammate can run PulseBoard locally on Python 3.12+ and open today’s board.

## Context

* PRD: US-007, FR-009, AC-007.1, AC-007.2, SM-04, OQ-PRD-02
* Preferred durable location: `lifecycle/09-operations/output/runbook.md` and/or README pointer (one canonical path required)

## Scope

* Prerequisites (Python 3.12+, env notes e.g. conda `hve-env`)
* Install/start commands
* URL/host/port to open
* Local-first deployment model statement
* DB file location / `PULSEBOARD_DB_PATH` if used
* Instance timezone / `PULSEBOARD_TZ` note
* How to run tests (`pytest`)

## Out of scope

* Cloud deploy guides
* SSO setup
* Mobile install

## Acceptance criteria

* [ ] AC-P-070 Given prerequisites in the runbook, when a new operator follows only the documented start path, then the app starts and today’s board UI is reachable. (PRD AC-007.1)
* [ ] AC-P-071 Given the runbook/docs, when read, then they state how to start, where to open the app, and that deployment is local-first. (PRD AC-007.2)
* [ ] AC-P-072 Given persistence/TZ config exists in the app, when reading docs, then DB path and today/TZ behavior are described at operator level. (PRD AC-006.2, ADR today/sqlite)

### TEMP-9 — docs: v0.1.0 release evidence checklist

* **Label:** `docs`
* **GitHub:** [#7](https://github.com/AbhranilGit/HVE-Core-Course/issues/7)

#### Body

## Summary

Create a release checklist that gates tagging `v0.1.0` on PRD P0 acceptance, automated create/list test evidence, and explicit out-of-scope absences.

## Context

* PRD: US-008, FR-010, AC-008.1–AC-008.4, SM-05, G-005

## Scope

* Checklist document (e.g. under lifecycle delivery/review output or ops) including:
  * US-001–US-007 P0 AC satisfied
  * No SSO/OAuth, notifications/email/Slack bots, or mobile clients
  * Automated create + today-list tests passed (link/log evidence)
  * Reviewer sign-off fields for AC-008.1–AC-008.3
* Does not implement product features

## Out of scope

* Sprint ordering (Stage 5)
* Tagging the release itself (execution at delivery time)

## Acceptance criteria

* [ ] AC-P-080 Checklist exists in-repo and maps to PRD AC-008.1–AC-008.4. (PRD US-008)
* [ ] AC-P-081 Checklist requires confirmation that SSO/OAuth, notifications/email/Slack bots, and mobile clients are absent. (PRD AC-008.2)
* [ ] AC-P-082 Checklist requires recorded evidence that automated tests cover create status and list/view today’s board. (PRD AC-008.3)
* [ ] AC-P-083 Checklist includes explicit reviewer confirmation step before tag. (PRD AC-008.4)

## Labels used

| Label | Issues |
|-------|--------|
| api | #2, #6, #5, #3 |
| auth | #4 |
| ui | #9 |
| tests | #10 |
| docs | #8, #7 |

## Planning artifacts

* Discovery folder: `.copilot-tracking/github-issues/discovery/pulseboard-mvp-prd/`
* Handoff (create checkboxes): `.copilot-tracking/github-issues/discovery/pulseboard-mvp-prd/handoff.md`

## Creation log

* Date: 2026-08-09
* Actor: AbhranilGit via GitHub MCP `issue_write`
* Result: **9/9 created**, labels applied (`api`, `ui`, `auth`, `docs`, `tests`)
* Pre-check: zero matching open duplicates
* Note: issue numbers are not sequential with TEMP order because parallel creates assigned IDs by completion time; titles and labels match the plan

## Next stage

Stage 5 (sprint planning): order work using the thin vertical slice path (#2 → #6 → #4 → #5 → #3 → #9 → #10 → #8 → #7).
