<!-- markdownlint-disable-file -->
<!-- markdown-table-prettify-ignore-start -->
# PulseBoard MVP - Product Requirements Document (PRD)
Version 0.1.0 | Status Draft | Owner Product / delivery owner | Team PulseBoard | Target v0.1.0 | Lifecycle Stage 3 — Product definition

## Progress Tracker
| Phase | Done | Gaps | Updated |
|-------|------|------|---------|
| Context | Yes | None | 2026-08-09 |
| Problem & Users | Yes | None | 2026-08-09 |
| Scope | Yes | None | 2026-08-09 |
| Requirements | Yes | None | 2026-08-09 |
| Metrics & Risks | Yes | None | 2026-08-09 |
| Operationalization | Yes | Runbook path may land with delivery docs | 2026-08-09 |
| Finalization | Yes | Awaiting PRD acceptance | 2026-08-09 |
Unresolved Critical Questions: 1 (identity session mechanism → ADR) | TBDs: 0 blocking MVP stories

## 1. Executive Summary
### Context
PulseBoard is a local-first team status board for small teams (~5–15 people) who currently scatter daily standup status in chat. The MVP delivers a thin slice: post **doing / blocked / next** and view a shared **today’s board** on one machine, with simple local identity and SQLite persistence.

Authoritative business source: [brd.md](../../02-discovery/output/brd.md) (Accepted). Framing: [mvp-framing.md](../../02-discovery/input/mvp-framing.md).

### Core Opportunity
If ICs can publish today’s status quickly and facilitators can run standup from one glanceable board, the team can replace ad-hoc standup *status* chat within about two weeks after `v0.1.0`, without SSO, notifications, mobile, or tracker scope.

### Goals
| Goal ID | Statement | Type | Baseline | Target | Timeframe | Priority |
|---------|-----------|------|----------|--------|-----------|----------|
| G-001 | ICs post today’s doing / blocked / next on a shared board | Outcome | Status only in chat | ≥70% active members post ≥3 weekdays in a sample week (SM-01) | ~2 weeks after v0.1.0 | P0 |
| G-002 | Facilitator runs standup from today’s board | Outcome | Standup from chat scroll | ≥3 consecutive days from board (SM-02) | ~2 weeks after v0.1.0 | P0 |
| G-003 | Blockers are visible without searching chat | Outcome | Blockers buried in stream | ≥1 real blocker found via board that chat would have missed (SM-03) | ~2 weeks after v0.1.0 | P0 |
| G-004 | New teammate can start the app from docs alone | Outcome | Tribal start knowledge | Docs/runbook start without tribal knowledge (SM-04) | By v0.1.0 tag | P0 |
| G-005 | Ship thin slice only | Guardrail | Pressure to add integrations | No SSO, notifications, or mobile in v0.1.0 (SM-05) | Through v0.1.0 | P0 |

### Objectives (Optional)
| Objective | Key Result | Priority | Owner |
|-----------|------------|----------|-------|
| Validate post + today’s board hypothesis | Meet SM-01–SM-03 in validation window or explicitly revisit hypothesis | P0 | Product / delivery owner |
| Keep delivery operable and testable | Create/list covered by automated tests; PRD AC reviewed before tag | P0 | Delivery owner |

## 2. Problem Definition
### Current Situation
Daily status lives in Teams, Slack, WhatsApp, or similar. Updates mix with other conversation, blockers are hard to spot, and mid-day joiners cannot reconstruct *today* without scrolling a noisy stream.

### Problem Statement
The team lacks a single, glanceable, day-scoped view of who is doing what, who is blocked, and what is next. Facilitation cost is high, blockers hide in chat, and coverage is unclear.

### Root Causes
* Status is ephemeral and interleaved with non-status chat
* No shared day boundary artifact for “today”
* No lightweight local tool optimized only for standup status

### Impact of Inaction
Standups stay chat-driven, blockers stay easy to miss, and any later tooling investment risks building integrations before the core board habit is proven.

## 3. Users & Personas
| Persona | Goals | Pain Points | Impact |
|---------|-------|------------|--------|
| IC (poster) | Publish today’s doing / blocked / next quickly; see teammates | Chat is slow to update and hard to scan; edits get lost in thread | Primary writer of status; drives SM-01 |
| Lead / facilitator (reader) | Run standup from one board; spot blockers and coverage gaps | Scrolls chat; misses silent or buried blockers | Primary reader; drives SM-02, SM-03 |
| Teammate operator | Start and share one local instance from documentation | Setup tribal knowledge blocks trial | Enables SM-04 |
| Product / delivery owner | Validate thin-slice hypothesis; refuse scope creep | Pressure to add SSO, bots, mobile early | Owns G-005 / SM-05 |

### Journeys (Optional)
1. **Morning post (IC):** Open app → set/confirm display name → create or update today’s doing / blocked / next → see own row on today’s board.
2. **Standup (facilitator):** Open today’s board → scan each person and non-empty blocked fields → facilitate from board instead of chat.
3. **First run (operator):** Follow runbook on Python 3.12+ env → start app → confirm empty or seeded today board loads.

## 4. Scope
### In Scope
* Create status with doing, blocked, and next (default day = today) — BRD IN-01 / BR-001, BR-002
* View today’s board (team list/board for current day) — IN-02 / BR-003, BR-004, BR-005
* Simple local identity (display name; no SSO) — IN-03 / BR-007
* Local persistence (SQLite on one machine) — IN-04 / BR-008
* Runnable locally with documented start path (Python 3.12+) — IN-05 / BR-009
* Thin first slice: post + today’s board = `v0.1.0` core — IN-06 / BR-010

### Out of Scope (justify if empty)
* SSO / OAuth
* Notifications, email, Slack bots
* Mobile application
* Multi-tenant SaaS
* Real-time websockets
* Historical analytics / multi-day history UI
* RBAC
* Rich media attachments
* Replacing chat for all communication
* Full project tracker (assignments, sprints, backlog)
* Anything not listed under In Scope until BRD/framing is updated

### Assumptions
* Trusted small team on one shared local instance (BRD A-02, A-03, A-05)
* Chat remains for non-status communication (A-07)
* Stack intent: Python, FastAPI, SQLite, HTMX-friendly UI (guides design; does not add features)
* Product defaults in §4.1 apply for MVP unless a later accepted change revises this PRD

### Constraints
* Local-first deployment only
* No cloud DB required
* Simple local identity only
* Automated tests for create and list/today board required before “done”
* Durable truth in `lifecycle/` and `.copilot-tracking/`, not chat

### 4.1 MVP product defaults (resolved from BRD open questions)
These defaults make AC testable. They do not add capabilities beyond the BRD in-scope list.

| Source OQ | MVP product default | Rationale |
|-----------|---------------------|-----------|
| OQ-01 | **Display name** identity: user supplies a non-empty display name to post; no SSO, no OAuth. Session/cookie vs re-entry mechanism is an ADR concern, not a new feature. | Thinest local identity; matches IN-03 |
| OQ-02 | **One status record per display name per calendar day** (create or replace/update that day’s row) | Keeps board glanceable for facilitators |
| OQ-03 | **Edit allowed anytime on the same calendar day**; no standup lock in MVP | Supports fast correction; lock would add process scope |
| OQ-04 | **“Today” = calendar date in the instance’s configured local timezone** (default: host local time). No per-user timezone matrix in MVP. | Day-scoped board without multi-region product |
| OQ-05 | **Blocked is a free-text field**; non-empty blocked text is how blockers show on the board. No separate filterable blocked flag in MVP. | Meets BR-005 without workflow engine |
| OQ-06 | **Before tagging `v0.1.0`:** automated tests for create status + list/view today’s board; manual checklist pass against this PRD’s P0 AC; no SSO/notifications/mobile in the build | Matches BRD quality constraint + SM-05 |

## 5. Product Overview
### Value Proposition
One local board where the team posts today’s doing / blocked / next and the facilitator runs standup without scrolling chat.

### Differentiators (Optional)
* Day-scoped and standup-only (not a tracker)
* Local-first and SQLite-backed (no cloud tenant required)
* Intentionally thin: post + today’s board before integrations

### UX / UI (Conditional)
Browser-based UI suitable for HTMX-style progressive enhancement; FastAPI backend. MVP UX must support: identify with display name, submit/edit today’s three fields, view today’s team board including blocked text. Pixel-perfect design system is out of scope. | UX Status: Conceptual only

## 6. Functional Requirements
| FR ID | Title | Description | Goals | Personas | Priority | Acceptance | Notes |
|-------|-------|------------|-------|----------|----------|-----------|-------|
| FR-001 | Identify with display name | User can set or confirm a non-empty display name used to attribute status posts | G-001 | IC, Operator | P0 | AC-001 | No SSO; mechanism ADR |
| FR-002 | Create today’s status | User can create a status for today with doing, blocked, and next fields | G-001, G-003 | IC | P0 | AC-002 | Default day = today |
| FR-003 | Update today’s status | User can change doing, blocked, and/or next on their existing today status | G-001 | IC | P0 | AC-003 | Same-day only |
| FR-004 | One status per name per day | At most one status row per display name for a given calendar day | G-002 | IC, Lead | P0 | AC-004 | Upsert semantics |
| FR-005 | View today’s board | Any user of the instance can open a board/list of all statuses for today | G-002, G-003 | IC, Lead | P0 | AC-005 | Includes empty-board state |
| FR-006 | Show status fields on board | Each board row shows display name, doing, blocked, next for today | G-002, G-003 | Lead | P0 | AC-006 | Blocked free text visible |
| FR-007 | Default day is today | New posts without an explicit other day target today; board default is today | G-001, G-002 | IC, Lead | P0 | AC-007 | No multi-day history UI |
| FR-008 | Persist statuses locally | Status data survives process restart on the same machine/DB file | G-001, G-002 | All | P0 | AC-008 | SQLite acceptable |
| FR-009 | Local run documented | Documented start path enables run on Python 3.12+ local environment | G-004 | Operator | P0 | AC-009 | Runbook/docs |
| FR-010 | Scope guardrails present in delivery bar | v0.1.0 does not implement SSO, notifications, or mobile clients | G-005 | Delivery owner | P0 | AC-010 | Review gate |

### Feature Hierarchy (Optional)
```plain
PulseBoard v0.1.0
├── Local identity
│   └── Display name (FR-001)
├── Status for today
│   ├── Create (FR-002, FR-007)
│   ├── Update same day (FR-003)
│   └── One per name per day (FR-004)
├── Today’s board
│   ├── List all today’s statuses (FR-005)
│   └── Show doing / blocked / next (FR-006)
├── Local persistence (FR-008)
└── Runnable locally + docs (FR-009)
```

### 6.1 User stories and acceptance criteria

#### US-001 — Identify myself with a display name
**As an** IC  
**I want to** set a display name on the shared instance  
**So that** my today’s status is attributed to me on the board  

**Maps to:** FR-001, BR-007, IN-03  

**Acceptance criteria**
* **AC-001.1** Given I open the app and have no display name set, when I submit a non-empty display name, then the app accepts it and uses it for subsequent status actions in that usage session (session persistence mechanism deferred to ADR).
* **AC-001.2** Given I submit an empty or whitespace-only display name, when I try to save it, then the app rejects it and does not create a status under a blank name.
* **AC-001.3** Given the MVP build, when I inspect identity options, then there is no SSO/OAuth sign-in path.

#### US-002 — Post today’s doing / blocked / next
**As an** IC  
**I want to** create today’s status with doing, blocked, and next  
**So that** the team can see what I am working on without reading chat  

**Maps to:** FR-002, FR-007, BR-001, BR-002, IN-01  

**Acceptance criteria**
* **AC-002.1** Given I have a valid display name and no status for today, when I submit doing, blocked, and next (each field may be empty string except as constrained below), then a status for **today** is stored and attributed to my display name.
* **AC-002.2** Given I create a status without choosing another day, when it is saved, then its day is the instance’s current calendar **today**.
* **AC-002.3** Given I submit a create with a valid display name, when save succeeds, then I can see my new values on today’s board without using chat.
* **AC-002.4** Given required identity is missing, when I attempt to create a status, then the app blocks create and prompts for display name (or equivalent clear failure).

*Field rule for MVP:* doing, blocked, and next are plain text. At least one of doing, blocked, or next must be non-empty on create/update so empty spam rows are not stored.

#### US-003 — Edit my status later the same day
**As an** IC  
**I want to** update my today’s doing / blocked / next anytime the same day  
**So that** I can correct mistakes or reflect mid-day changes  

**Maps to:** FR-003, FR-004, BR-006  

**Acceptance criteria**
* **AC-003.1** Given I already have a status for today under my display name, when I submit new doing / blocked / next values, then today’s board shows the updated values and not a second row for me for today.
* **AC-003.2** Given I update today’s status, when the update succeeds, then at least one of doing, blocked, or next is non-empty (same rule as create).
* **AC-003.3** Given MVP, when I look for a “lock after standup” control, then none exists (edits remain allowed all day).

#### US-004 — View today’s team board
**As a** lead / facilitator  
**I want to** open one board of everyone’s status for today  
**So that** I can run standup without scrolling chat  

**Maps to:** FR-005, FR-006, BR-003, BR-004, IN-02  

**Acceptance criteria**
* **AC-004.1** Given zero statuses for today, when I open today’s board, then I see an empty state that clearly indicates no posts yet for today (not an error).
* **AC-004.2** Given one or more statuses for today, when I open today’s board, then each status appears with display name, doing, blocked, and next.
* **AC-004.3** Given statuses exist only for a prior calendar day, when I open the default today’s board, then those prior-day rows do not appear as today’s posts.
* **AC-004.4** Given multiple distinct display names posted today, when I view the board, then I can distinguish each person’s row (no silent overwrite across different names).

#### US-005 — Spot blockers on the board
**As a** lead / facilitator  
**I want to** see blocked text on today’s board  
**So that** I can find impediments without searching chat  

**Maps to:** FR-006, BR-005, G-003  

**Acceptance criteria**
* **AC-005.1** Given a teammate saved a non-empty blocked value today, when I view today’s board, then that blocked text is visible on their row without opening chat.
* **AC-005.2** Given a teammate left blocked empty and filled doing or next, when I view today’s board, then their row still appears and blocked is shown empty/absent (no separate blocked-only filter required in MVP).
* **AC-005.3** Given MVP scope, when I look for blocked workflow states, SLA timers, or notification of blockers, then none are implemented.

#### US-006 — Data survives restart
**As a** teammate using a shared local instance  
**I want** today’s statuses to persist across app restarts  
**So that** standup data is not lost if the process stops  

**Maps to:** FR-008, BR-008, IN-04  

**Acceptance criteria**
* **AC-006.1** Given I created today’s status and the app process is stopped and started again against the same local database, when I open today’s board, then the previously saved statuses for today are still present.
* **AC-006.2** Given MVP, when persistence is described in docs, then it is local to the machine (SQLite or equivalent local file DB), not a required cloud database.

#### US-007 — Run locally from documentation
**As a** teammate operator  
**I want** a documented start path on Python 3.12+  
**So that** I can run PulseBoard without tribal knowledge  

**Maps to:** FR-009, BR-009, IN-05, SM-04  

**Acceptance criteria**
* **AC-007.1** Given a clean environment meeting documented prerequisites (Python 3.12+ and listed steps), when I follow the start path in project docs/runbook only, then the app starts and I can open the UI for today’s board.
* **AC-007.2** Given the docs/runbook, when I read them, then they state how to start, where the app is reached (URL/host/port as applicable), and that the deployment model is local-first.

#### US-008 — Thin-slice release bar for v0.1.0
**As a** product / delivery owner  
**I want** a clear done bar for `v0.1.0`  
**So that** we ship post + today’s board without scope creep  

**Maps to:** FR-010, BR-010, IN-06, OQ-06, SM-05  

**Acceptance criteria**
* **AC-008.1** Given the candidate `v0.1.0` build, when reviewed against this PRD, then US-001 through US-007 P0 AC are met.
* **AC-008.2** Given the candidate build, when checked for out-of-scope items, then SSO/OAuth, notifications/email/Slack bots, and mobile clients are absent.
* **AC-008.3** Given the candidate build, when quality evidence is reviewed, then automated tests cover **create status** and **list/view today’s board**, and results are recorded for the release review.
* **AC-008.4** Given tagging `v0.1.0`, when the release checklist is completed, then a reviewer has explicitly confirmed AC-008.1–AC-008.3.

## 7. Non-Functional Requirements
| NFR ID | Category | Requirement | Metric/Target | Priority | Validation | Notes |
|--------|----------|------------|--------------|----------|-----------|-------|
| NFR-001 | Performance | Today’s board load for up to 15 rows feels immediate on local machine | Board renders in ≤2s on local dev hardware with ≤15 statuses | P0 | Manual timing on local instance | Scale per BRD |
| NFR-002 | Reliability | Status create/update either persists or returns a clear failure | No silent drop of accepted submits | P0 | Tests + manual fault check | |
| NFR-003 | Scalability | Support ~5–15 users on one local instance | 15 today-rows usable without multi-node setup | P0 | Manual with sample data | No horizontal scale story |
| NFR-004 | Security | No SSO; trusted-network / local-machine assumption | No OAuth/SSO code paths in MVP | P0 | Review AC-001.3, AC-008.2 | Not hardened multi-tenant security |
| NFR-005 | Privacy | Only display name + status text stored for MVP status use | No third-party identity provider data | P1 | Design/review | |
| NFR-006 | Accessibility | Core flows usable via keyboard in browser for form + board | Can complete create and view board without mouse-only traps | P1 | Manual keyboard pass | Full WCAG audit not MVP gate |
| NFR-007 | Observability | Failures on create/list are visible to operator (log or error response) | Error not silent on failed write/read | P1 | Manual | No SaaS telemetry required |
| NFR-008 | Maintainability | Create and today-list covered by automated tests | Tests exist and pass before v0.1.0 tag | P0 | CI or local test run evidence | BRD quality constraint |
| NFR-009 | Operability | Documented local start on Python 3.12+ | AC-007 met | P0 | Docs dry-run | SM-04 |
| NFR-010 | Compliance | N/A for MVP local trusted team | — | P3 | — | No regulated workload claimed |

Categories: Performance, Reliability, Scalability, Security, Privacy, Accessibility, Observability, Maintainability, Localization (if), Compliance (if).

## 8. Data & Analytics (Conditional)
### Inputs
* Display name (plain text)
* doing, blocked, next (plain text)
* Status day (calendar date, default today in instance timezone)

### Outputs / Events
* Today’s board rows for standup facilitation
* No product analytics pipeline required for MVP

### Instrumentation Plan
| Event | Trigger | Payload | Purpose | Owner |
|-------|---------|--------|---------|-------|
| N/A MVP | — | — | Hypothesis validated via manual SM-01–SM-05, not product telemetry | Product owner |

### Metrics & Success Criteria
| Metric | Type | Baseline | Target | Window | Source |
|--------|------|----------|--------|--------|--------|
| Adoption (SM-01) | Leading | Chat-only | ≥70% active members post ≥3 weekdays in a sample week | ~2 weeks after v0.1.0 | Manual count |
| Standup replacement (SM-02) | Outcome | Chat standup | Facilitator uses board ≥3 consecutive days | Same | Facilitator attestation |
| Blocker visibility (SM-03) | Outcome | Buried in chat | ≥1 real blocker found via board missed in chat | Same | Facilitator note |
| Operability (SM-04) | Quality | Tribal knowledge | New teammate starts from docs/runbook only | By v0.1.0 / first onboard | Dry-run |
| Scope discipline (SM-05) | Guardrail | Creep risk | No SSO, notifications, mobile shipped | Through v0.1.0 | Release review |

## 9. Dependencies
| Dependency | Type | Criticality | Owner | Risk | Mitigation |
|-----------|------|------------|-------|------|-----------|
| Accepted BRD scope | Business | High | Product owner | Scope drift | Bind all FR to BRD IN/BR IDs |
| Python 3.12+ local env | Runtime | High | Operator | Env mismatch | Document prerequisites |
| SQLite (or equivalent local DB) | Data | High | Delivery | File path/permissions | Document DB location |
| FastAPI + HTMX-friendly UI intent | Tech | Medium | Delivery | Stack debate | Keep as intent; ADR if needed |
| Display-name session mechanism ADR | Decision | Medium | Architect / delivery | Inconsistent identity UX | ADR after PRD acceptance |
| Instance timezone configuration | Config | Medium | Delivery | “Today” confusion for remote users | Document instance TZ; no per-user TZ matrix |

## 10. Risks & Mitigations
| Risk ID | Description | Severity | Likelihood | Mitigation | Owner | Status |
|---------|-------------|---------|-----------|-----------|-------|--------|
| RK-001 | Low posting adoption | High | Medium | Optimize create/edit path; apply BRD go/low-posting rule | Product owner | Open |
| RK-002 | Facilitator stays on chat | High | Medium | Board must show name + doing/blocked/next clearly | Delivery | Open |
| RK-003 | Local share awkward | Medium | Medium | Strong runbook (US-007) | Operator | Open |
| RK-004 | Identity ambiguity | Medium | Medium | PRD default = display name; ADR for session mechanism | Architect | Open |
| RK-005 | Today boundary issues for remote teammates | Medium | Medium | Instance TZ documented; no multi-TZ feature creep | Delivery | Open |
| RK-006 | Scope creep (SSO, bots, mobile, tracker) | High | Medium | Out-of-scope list + AC-008.2 | Product owner | Open |
| RK-007 | Blocked free text hard to scan | Medium | Low–Med | Visible blocked field; flag deferred post-MVP | Product owner | Open |
| RK-008 | Shipping without create/list tests | Medium | Medium | NFR-008 + AC-008.3 gate | Delivery | Open |

## 11. Privacy, Security & Compliance
### Data Classification
Local operational team status text and display names. Treat as internal team working data on a trusted local machine.

### PII Handling
Display names may be personal identifiers. MVP stores them only on the local instance; no IdP integration; no requirement to export to third parties.

### Threat Considerations
MVP assumes a trusted small team and local/lab network exposure model. It is not a multi-tenant hardened service. No anonymous public access feature.

### Regulatory / Compliance (Conditional)
| Regulation | Applicability | Action | Owner | Status |
|-----------|--------------|--------|-------|--------|
| None claimed for MVP | Not positioned as regulated workload | Revisit if deployment context changes | Product owner | N/A |

## 12. Operational Considerations
| Aspect | Requirement | Notes |
|--------|------------|-------|
| Deployment | Local-first on single developer or shared lab machine | No cloud deploy requirement |
| Rollback | Replace/stop process; restore prior DB file if needed | Keep ops simple |
| Monitoring | Process logs / error responses sufficient for MVP | No SaaS APM required |
| Alerting | Not in MVP | Out of scope notifications |
| Support | Team self-support via docs/runbook | SM-04 |
| Capacity Planning | Size for ≤15 concurrent team members’ daily posts | BRD scale |

## 13. Rollout & Launch Plan
### Phases / Milestones
| Phase | Date | Gate Criteria | Owner |
|-------|------|--------------|-------|
| PRD acceptance | TBD | This PRD accepted; scope unchanged from BRD | Product owner |
| ADRs (identity session, key tech choices) | After PRD | OQ-01 mechanism decided without adding SSO | Architect |
| v0.1.0 implementation | After ADRs / planning | US-001–US-007 implemented | Delivery |
| v0.1.0 tag | TBD | AC-008.* satisfied | Delivery + product owner |
| Hypothesis validation | ~2 weeks post tag | SM-01–SM-05 measured | Product owner |

### Feature Flags (Conditional)
| Flag | Purpose | Default | Sunset Criteria |
|------|---------|--------|----------------|
| None required for MVP | — | — | Thin slice always on |

### Communication Plan (Optional)
Team uses the board for daily status; chat remains for discussion. Facilitator announces standup-from-board trial at tag.

## 14. Open Questions
| Q ID | Question | Owner | Deadline | Status |
|------|----------|-------|---------|--------|
| OQ-PRD-01 | Exact session/persistence mechanism for display name (cookie, header, re-entry each visit, etc.) | Architect (ADR) | Before implementation start | Open — product default is display name only |
| OQ-PRD-02 | Canonical docs path for runbook (README vs lifecycle ops doc) | Delivery | Before AC-007 verification | Open — non-blocking if one documented path exists |
| OQ-BRD-01 | Display name only vs demo login / shared password (deeper auth) | ADR | If display name proves insufficient | Deferred — MVP uses display name |
| OQ-BRD-04 residual | Per-user timezone support | Product | Post-MVP unless validation fails | Deferred — instance TZ only |
| OQ-BRD-05 residual | Filterable blocked flag | Product | Post-MVP | Deferred — free text only |

Resolved in this PRD (see §4.1): OQ-02 one-per-name-per-day; OQ-03 edit anytime same day; OQ-05 blocked free text; OQ-06 v0.1.0 evidence bar; OQ-04 instance-local today.

## 15. Changelog
| Version | Date | Author | Summary | Type |
|---------|------|-------|---------|------|
| 0.1.0 | 2026-08-09 | PRD Builder | Initial MVP PRD from accepted BRD; user stories + AC for in-scope capabilities only | Create |

## 16. References & Provenance
| Ref ID | Type | Source | Summary | Conflict Resolution |
|--------|------|--------|---------|--------------------|
| REF-001 | BRD | [brd.md](../../02-discovery/output/brd.md) | Accepted business requirements, scope, metrics, OQs | BRD wins on scope; PRD only adds product defaults inside scope |
| REF-002 | Framing | [mvp-framing.md](../../02-discovery/input/mvp-framing.md) | Original MVP framing | Framing/BRD bound PRD; no widening |

### Citation Usage
Goals and metrics map to BRD SM-01–SM-05 and BO-01–BO-05. FR/US map to BR-001–BR-010 and IN-01–IN-06. Out-of-scope list copied from BRD §5.2.

## 17. Appendices (Optional)
### Glossary
| Term | Definition |
|------|-----------|
| Today | Calendar date in the PulseBoard instance’s configured local timezone |
| Status | One person’s doing / blocked / next for a single calendar day |
| Today’s board | UI list/board of all statuses for today |
| Display name | Local plain-text name attributing a status; not SSO identity |
| v0.1.0 | First shippable thin slice: post + today’s board + local identity + persistence + docs |

### Traceability (BRD → PRD)
| BRD ID | PRD coverage |
|--------|--------------|
| BR-001 | US-002, FR-002 |
| BR-002 | FR-007, AC-002.2 |
| BR-003 | US-004, FR-005 |
| BR-004 | US-004, G-002 |
| BR-005 | US-005, FR-006 |
| BR-006 | US-003, FR-003 |
| BR-007 | US-001, FR-001 |
| BR-008 | US-006, FR-008 |
| BR-009 | US-007, FR-009 |
| BR-010 | US-008, FR-010 |
| IN-01–IN-06 | §4 In Scope + feature hierarchy |

### Additional Notes
This PRD does **not** include ADRs, GitHub issues, sprint plans, or application code. Implementation must not widen MVP beyond §4 In Scope.

Generated 2026-08-09 by PRD Builder (mode: full)
<!-- markdown-table-prettify-ignore-end -->
