---
title: PulseBoard Business Requirements Document
description: Business requirements for PulseBoard MVP, a local-first team status board for daily doing, blocked, and next updates
author: BRD Builder
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - brd
  - discovery
  - mvp
  - daily status
estimated_reading_time: 8
---

## Document control

| Field              | Value                                                                 |
|--------------------|-----------------------------------------------------------------------|
| Product            | PulseBoard                                                            |
| Document type      | Business Requirements Document (BRD)                                  |
| Status             | Accepted                                                  |
| HVE stage          | Stage 2 — Discovery                                                   |
| Source of truth    | [mvp-framing.md](../input/mvp-framing.md) (Accepted)                  |
| Related handoff    | Stage 3 PRD and ADRs after BRD acceptance; bound by in-scope list     |
| Stack intent       | Python, FastAPI, SQLite, HTMX (implementation detail, not BRD scope)  |

This BRD states business need, outcomes, boundaries, and constraints. It does not define product acceptance criteria, architecture decisions, work items, or application design.

## 1. Business context and background

Small teams exchange daily status in chat tools (Teams, Slack, WhatsApp, and similar). Status updates are mixed with other conversation, so they are easy to miss. Blockers are hard to see at a glance. People who join mid-day cannot reconstruct *today* without scrolling a noisy stream.

PulseBoard is a local-first team status board. Team members post **doing**, **blocked**, and **next** onto a shared **today’s board** so standup context lives in one day-scoped place instead of chat history.

**Business hypothesis:** If the team can post doing / blocked / next onto a shared today’s board on a local machine, they will replace ad-hoc standup chat for daily status within about two weeks of use after `v0.1.0`.

## 2. Problem statement and business drivers

### 2.1 Problem statement

Daily standup status is scattered in chat. The team lacks a single, glanceable, day-scoped view of who is doing what, who is blocked, and what is next. That raises the cost of facilitation, hides blockers, and leaves mid-day joiners without a reliable picture of today.

### 2.2 Business drivers

| Driver                         | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| Operational efficiency         | Reduce time spent reconstructing status from chat during and after standup |
| Blocker visibility             | Surface impediments that chat buries                                        |
| Team coordination at small scale | Support ~5–15 people on one shared local instance                         |
| Scope and delivery discipline  | Prove the thin slice (post + today’s board) before integrations             |
| Local-first operability        | Run without cloud identity, multi-tenant SaaS, or managed cloud database    |

### 2.3 Opportunity

A minimal shared board for today’s doing / blocked / next can become the facilitator’s primary standup surface and the IC’s fast path to publish status, without replacing chat for all communication or becoming a full project tracker.

## 3. Business objectives and success metrics

### 3.1 Objectives

| ID    | Objective                                                                 | Linked outcome                                      |
|-------|---------------------------------------------------------------------------|-----------------------------------------------------|
| BO-01 | Make today’s team status visible in one place without scrolling chat      | Facilitator can run standup from the board          |
| BO-02 | Enable fast posting and editing of doing / blocked / next for the day     | ICs adopt the board for daily status                |
| BO-03 | Improve discovery of real blockers relative to chat-only practice         | At least one missed-in-chat blocker found via board |
| BO-04 | Keep the MVP operable by a new teammate from documented start path        | Reduced tribal knowledge to run the tool            |
| BO-05 | Protect hypothesis validation by refusing out-of-scope expansion          | Ship thin slice without SSO, notifications, mobile  |

### 3.2 Success metrics

Validation window: about two weeks of team use after `v0.1.0`.

| ID    | Metric                 | Target                                                                 | Baseline (as-is)                          |
|-------|------------------------|------------------------------------------------------------------------|-------------------------------------------|
| SM-01 | Adoption               | ≥70% of active members post on ≥3 weekdays in a sample week            | Status lives in chat; no board baseline   |
| SM-02 | Standup replacement    | Facilitator runs standup from the board on ≥3 consecutive days         | Standup driven from chat scroll           |
| SM-03 | Blocker visibility     | ≥1 real blocker found via the board that chat would have missed        | Blockers often buried in stream           |
| SM-04 | Operability            | New teammate can start the app from docs/runbook without tribal knowledge | Start path not yet proven at scale     |
| SM-05 | Scope discipline       | Ship without SSO, notifications, or mobile                             | Framing explicitly excludes these         |

### 3.3 Decision rule after validation

| Result                         | Next step                                                                 |
|--------------------------------|---------------------------------------------------------------------------|
| Metrics largely met (Go)       | Deepen via PRD and next sprint; remain bound by current in-scope list until framing is updated |
| Low posting or weak replacement | Simplify experience or revisit the hypothesis before adding integrations |

## 4. Stakeholders and roles

### 4.1 Primary stakeholders

| Stakeholder                 | Role type        | Business interest                                                                 |
|-----------------------------|------------------|-----------------------------------------------------------------------------------|
| IC (poster)                 | Primary user     | Fast create/edit of today’s doing / blocked / next; see teammates on today’s board |
| Lead / facilitator (reader) | Primary user     | One today’s board to spot blockers and coverage without scrolling chat            |
| Product / delivery owner    | Sponsor-style    | Validate hypothesis within two weeks; keep MVP thin and local-first               |
| Teammate operator           | Operator         | Start and run the shared local instance from documentation                        |

### 4.2 Audience boundaries (MVP)

In audience:

* Individual contributors on the shared team instance
* Leads or facilitators who run daily standup from the board
* Small co-located or loosely distributed teams of about 5–15 people on one local instance

Out of audience for MVP:

* Enterprise IT admins
* Multi-tenant SaaS buyers
* Mobile-only users
* Anonymous public users

### 4.3 Scale

Approximately 5–15 people on one shared local instance (single developer machine or shared lab machine).

## 5. Scope

### 5.1 In scope (P0)

Only the following capabilities are in MVP scope. Anything not listed here is out until the framing is updated.

| ID     | Capability              | Business need                                                                 |
|--------|-------------------------|-------------------------------------------------------------------------------|
| IN-01  | Create status           | Capture doing / blocked / next with default day = today                       |
| IN-02  | View today’s board      | Provide a team list/board for the current day                                 |
| IN-03  | Simple local identity   | Identify posters via display name or demo login; no SSO                       |
| IN-04  | Local persistence       | Persist status on one machine (SQLite acceptable)                             |
| IN-05  | Runnable locally        | Documented start path; Python 3.12+ environment expectation                   |
| IN-06  | Thin first slice        | Post + today’s board as Sprint 1 / `v0.1.0` core                              |

### 5.2 Out of scope

Explicitly out of MVP:

* SSO / OAuth
* Notifications, email, or Slack bots
* Mobile application
* Multi-tenant SaaS
* Real-time websockets
* Historical analytics
* Role-based access control (RBAC)
* Rich media attachments
* Replacing chat for all communication
* Becoming a full project tracker

### 5.3 Business constraints

| Area        | Constraint                                                                 |
|-------------|----------------------------------------------------------------------------|
| Deployment  | Local-first; single developer or shared lab machine                        |
| Data        | Local datastore acceptable; no cloud database required                     |
| Experience  | Web UI suitable for HTMX-style interaction; API-capable backend expected   |
| Identity    | Simple local identity only                                                 |
| Quality     | Create/list behavior covered by tests; done judged later against PRD AC    |
| Tooling     | HVE Core All and Copilot; conda `hve-env` with Python 3.12                 |
| Process     | Durable decisions and artifacts live in `lifecycle/` and `.copilot-tracking/`, not chat |

## 6. Business requirements

Requirements below are solution-agnostic business needs. They do not prescribe UX chrome, schema design, or API shape.

| ID     | Requirement                                                                 | Objective | Stakeholders                         | Priority |
|--------|-----------------------------------------------------------------------------|-----------|--------------------------------------|----------|
| BR-001 | Team members can record today’s status as doing, blocked, and next          | BO-02     | IC                                   | P0       |
| BR-002 | Default status day is the current day (“today”)                             | BO-01     | IC, Lead / facilitator               | P0       |
| BR-003 | The team can view a shared board or list of statuses for today              | BO-01     | IC, Lead / facilitator               | P0       |
| BR-004 | A lead or facilitator can use today’s board as the primary standup surface  | BO-01     | Lead / facilitator                   | P0       |
| BR-005 | Blocked work is visible on today’s board without searching chat history     | BO-03     | Lead / facilitator, IC               | P0       |
| BR-006 | Posters can update their own today’s status (edit rules detailed later)     | BO-02     | IC                                   | P0       |
| BR-007 | Each poster is identifiable with simple local identity (no SSO)             | BO-02     | IC, Operator                         | P0       |
| BR-008 | Status data persists on the local instance across restarts                  | BO-01     | All primary users                    | P0       |
| BR-009 | A new teammate can start the local instance from documentation alone        | BO-04     | Teammate operator                    | P0       |
| BR-010 | MVP delivery excludes SSO, notifications, and mobile clients                | BO-05     | Product / delivery owner             | P0       |

## 7. Assumptions

Derived from the accepted MVP framing; not new product scope.

| ID    | Assumption                                                                 |
|-------|----------------------------------------------------------------------------|
| A-01  | Chat (Teams, Slack, WhatsApp, or similar) is the current primary channel for daily status |
| A-02  | A team of about 5–15 people will share one local PulseBoard instance       |
| A-03  | Running on a single developer machine or shared lab machine is acceptable for MVP validation |
| A-04  | Local SQLite-style persistence meets MVP data needs; cloud DB is not required |
| A-05  | Simple local identity is sufficient for a trusted small team; enterprise identity is out of audience |
| A-06  | “Today” is meaningful as a day-scoped board for the validation period, even if timezone edge cases remain open |
| A-07  | Replacing ad-hoc standup *status* chat is the goal; chat remains for other communication |
| A-08  | Two weeks of use after `v0.1.0` is a sufficient window to test the hypothesis |
| A-09  | Durable product truth will be kept in `lifecycle/` and `.copilot-tracking/`, not in chat threads |
| A-10  | Stack intent (Python, FastAPI, SQLite, HTMX) guides later design work but does not expand business scope |

## 8. Risks

| ID    | Risk                                                                 | Impact | Likelihood | Mitigation direction (business-level)                                      |
|-------|----------------------------------------------------------------------|--------|------------|----------------------------------------------------------------------------|
| R-01  | Low posting adoption; team stays in chat                             | High   | Medium     | Keep create/edit path minimal; if posting stays low, simplify or revisit hypothesis before integrations |
| R-02  | Facilitator does not switch standup to the board                     | High   | Medium     | Optimize for glanceable today’s board and blocker visibility               |
| R-03  | Single-machine local deployment is unavailable or awkward to share   | Medium | Medium     | Document start path; treat operability as a success metric                 |
| R-04  | Ambiguous local identity model slows trust or usability              | Medium | Medium     | Resolve display name vs demo login in ADR after BRD; keep SSO out          |
| R-05  | Unclear “today” boundary for remote teammates splits the board       | Medium | Medium     | Keep open; decide in PRD/ADR without adding multi-region product scope     |
| R-06  | Scope creep into notifications, SSO, bots, or tracker features       | High   | Medium     | Enforce out-of-scope list; measure scope discipline (SM-05)                |
| R-07  | Blocked field is free text only and remains hard to scan             | Medium | Low–Med    | Keep open whether blocked needs a filterable flag; do not expand to workflow engine |
| R-08  | Premature integrations before hypothesis is validated                | High   | Medium     | Go / low-posting decision rule after two-week validation                   |

## 9. Open questions

Carried from framing. Do not invent answers in implementation chat; resolve in BRD clarification, ADR, or PRD as appropriate.

| ID    | Question                                                                 | Likely home        |
|-------|--------------------------------------------------------------------------|--------------------|
| OQ-01 | Display name only vs demo login / shared password?                       | ADR / PRD          |
| OQ-02 | One status per person per day, or multiple?                              | PRD                |
| OQ-03 | Edit anytime same day, or lock after standup?                            | PRD                |
| OQ-04 | Timezone / “today” boundary for remote teammates?                        | PRD / ADR          |
| OQ-05 | Blocked: free text only, or also a filterable flag?                      | PRD                |
| OQ-06 | Minimum test/review evidence before tagging `v0.1.0`?                    | PRD / delivery     |

No additional open questions are required beyond the framing list for this BRD.

## 10. Out of document (explicit non-goals for this artifact)

This BRD does **not** include:

* Product requirements document (PRD) depth or acceptance criteria
* Architecture decision records (ADRs)
* GitHub issues, sprint tickets, or estimates
* Application code under `src/pulseboard/`
* Expansion of MVP beyond the framing in-scope list

## 11. Handoff

| Step                | Action                                                                 |
|---------------------|------------------------------------------------------------------------|
| Review              | Accept or amend this BRD against [mvp-framing.md](../input/mvp-framing.md) |
| On acceptance       | Stage 3: PRD builder and ADRs, still bound by §5 Scope                 |
| Implementation gate | No feature work that is not listed under in-scope P0                   |
| Source binding      | If framing and BRD diverge, update framing first, then this BRD        |

## 12. Traceability summary

| Framing section     | BRD section                                      |
|---------------------|--------------------------------------------------|
| §1 Problem          | §1 Context, §2 Problem statement                 |
| §2 Users            | §4 Stakeholders and roles                        |
| §3 In / out of scope| §5 Scope, §6 Business requirements               |
| §4 Constraints      | §5.3 Business constraints, §7 Assumptions        |
| §5 Success metrics  | §3 Objectives and success metrics                |
| §6 Open questions   | §9 Open questions                                |
| §7 HVE handoff      | §11 Handoff                                      |
