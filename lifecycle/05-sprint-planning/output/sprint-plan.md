---
title: PulseBoard MVP Sprint 1 and Sprint 2 plan
description: Ordered sprint split of open GitHub MVP issues for a thin vertical slice then release readiness
author: GitHub Backlog Manager
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - sprint-planning
  - github-issues
  - mvp
estimated_reading_time: 5
---

## Document control

| Field | Value |
|-------|-------|
| Product | PulseBoard MVP |
| Stage | 5 — Sprint planning |
| Source backlog | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) |
| Repository | [AbhranilGit/HVE-Core-Course](https://github.com/AbhranilGit/HVE-Core-Course) |
| Open issues verified | 2026-08-09 via GitHub list (9 OPEN: #2–#10) |
| Implementation code | Not in this step |
| New issues created | None |

## Goal

| Sprint | Outcome |
|--------|---------|
| Sprint 1 | Thin vertical slice: a user can set a display name, post doing/blocked/next for today, and see it on today’s board in the browser. |
| Sprint 2 | Harden and package the slice: automated create/list tests, local runbook, and v0.1.0 release evidence checklist. |

## Sprint 1 (ordered)

Thin path only. Complete in this order unless a later issue is unblocked earlier by finished deps.

| Order | Issue | Title | Label | Depends on |
|-------|-------|-------|-------|------------|
| 1 | [#2](https://github.com/AbhranilGit/HVE-Core-Course/issues/2) | api: SQLite schema and status repository for today | api | — |
| 2 | [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6) | api: instance today helper and day defaulting | api | — (pairs with #2; needed before day-scoped write/list) |
| 3 | [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4) | auth: display name identity with cookie continuity | auth | — (minimal request path OK; full chrome in #9) |
| 4 | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) | api: upsert today status (doing / blocked / next) | api | #2, #6, #4 |
| 5 | [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3) | api: list statuses for today board | api | #2, #6 |
| 6 | [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9) | ui: today board and status form (HTMX) | ui | #4, #5, #3 |

### Sprint 1 definition of done

* Local app starts with SQLite schema available.
* Display name can be set and retained via cookie; blank names rejected.
* User can create or update today’s doing/blocked/next under that name (one row per name per day).
* Today’s board lists today’s rows (empty state allowed) and excludes prior-day rows.
* Browser UI wires name + form + board so the poster sees their values without chat.

### Sprint 1 explicit deferrals

* Full automated test suite (#10)
* Operator runbook polish (#8)
* v0.1.0 release checklist (#7)
* Anything in PRD out of scope (SSO, notifications, mobile, multi-tenant, websockets, history UI, RBAC, rich media, full tracker)

## Sprint 2 (ordered)

Release readiness on the same MVP backlog. No new product features.

| Order | Issue | Title | Label | Depends on |
|-------|-------|-------|-------|------------|
| 1 | [#10](https://github.com/AbhranilGit/HVE-Core-Course/issues/10) | tests: create status and list today board | tests | #2, #6, #5, #3 (Sprint 1 behaviors) |
| 2 | [#8](https://github.com/AbhranilGit/HVE-Core-Course/issues/8) | docs: local-first runbook and start path | docs | Runnable Sprint 1 app; references pytest from #10 when present |
| 3 | [#7](https://github.com/AbhranilGit/HVE-Core-Course/issues/7) | docs: v0.1.0 release evidence checklist | docs | #10 evidence path; Sprint 1 P0 behaviors present |

### Sprint 2 definition of done

* Automated tests cover create/upsert status and list today’s board (temp DB), including prior-day exclusion and no duplicate row on upsert.
* Runbook documents prerequisites, start commands, URL, local-first model, DB path / TZ notes, and how to run tests.
* v0.1.0 checklist maps PRD AC-008.*, requires out-of-scope absences, test evidence, and reviewer sign-off before tag.

## Rationale for the split

* **Sprint 1 is the thinnest path that proves the product.** Schema (#2), calendar day (#6), identity (#4), write (#5), read (#3), and UI (#9) are all required for “post status and see today’s board.” None of those six is optional without breaking the slice.
* **#4 stays in Sprint 1** because upsert and the UI must attribute status to a display name and block blank identity (PRD AC-002.4). A cookie-backed name is in-scope MVP identity, not polish.
* **#3 stays in Sprint 1** because the board is the user-visible half of the slice; API-only write without list/UI does not meet the sprint goal.
* **Sprint 2 holds quality and packaging.** Tests (#10), runbook (#8), and release checklist (#7) gate v0.1.0 and teammate onboarding but are not required to manually demonstrate the thin slice once #9 works.
* **Order follows hard dependencies**, matching the Stage 4 thin path: foundation → day boundary → identity → write → read → UI, then tests → ops docs → release gate.

## Dependency graph

```text
#2 schema ─────────────┬──────────────► #5 upsert ──┐
                       │                 ▲          │
#6 instance today ─────┼─────────────────┤          ├──► #9 UI
                       │                 │          │
#4 display name ───────┴─────────────────┘          │
                                                    │
#2 + #6 ──────────────────────────────► #3 list ────┘

Sprint 2:
#5 + #3 (+ #2/#6) ──► #10 tests ──► #8 runbook
#10 + Sprint 1 P0 ──► #7 v0.1.0 checklist
```

## Parallelism notes

* After #2 lands, #6 and #4 can proceed in parallel.
* After #2 and #6, #3 can start in parallel with #4/#5 once day-scoped list helpers exist; #5 still needs #4.
* #9 should start only when #4, #5, and #3 expose enough behavior to wire the form and board (stubs risk rework).
* In Sprint 2, #8 can draft start/path sections while #10 finishes, then add the pytest section; #7 last.

## Coverage check (existing backlog only)

| Issue | Sprint | Role |
|-------|--------|------|
| #2 | 1 | Persistence foundation |
| #6 | 1 | Shared “today” boundary |
| #4 | 1 | Identity for post |
| #5 | 1 | Post / edit today status |
| #3 | 1 | Board data |
| #9 | 1 | User-visible slice |
| #10 | 2 | Automated create/list evidence |
| #8 | 2 | Local-first operator path |
| #7 | 2 | v0.1.0 gate |

All nine open MVP issues are assigned. No backlog item deferred past Sprint 2. No new issues required for the thin slice.

## Explicitly not planned

From PRD out of scope (do not pull into either sprint):

* SSO / OAuth
* Notifications, email, Slack bots
* Mobile application
* Multi-tenant SaaS
* Real-time websockets
* Historical analytics / multi-day history UI
* RBAC
* Rich media attachments
* Full project tracker

## Next steps

1. Optional: create GitHub milestones `Sprint 1` / `Sprint 2` and assign issue numbers (execution step; not done here).
2. Stage 6 implementation: start with #2 in Sprint 1 order.
3. Do not expand scope beyond PRD P0 while implementing.
