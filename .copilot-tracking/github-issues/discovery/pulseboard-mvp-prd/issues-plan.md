<!-- markdownlint-disable-file -->
<!-- markdown-table-prettify-ignore-start -->
# Issues Plan

* **Repository**: AbhranilGit/HVE-Core-Course
* **Milestone**: none (Stage 5 owns sprint ordering)

## IS001 - Create - SQLite schema and status repository

Persistence foundation for local-first MVP. Enables FR-008 / US-006 and unique one-status-per-name-per-day.

IS001 - Similarity: none found (live search unavailable)

* IS001 - issue_number: {{TEMP-1}}
* IS001 - title: api: SQLite schema and status repository for today
* IS001 - state: open
* IS001 - labels: api
* IS001 - milestone: none
* IS001 - assignees: none

### IS001 - body

```markdown
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

## Label

`api`
```

### IS001 - Relationships

* none

## IS002 - Create - Instance today helper

Deterministic “today” for defaults and board queries.

IS002 - Similarity: none found

* IS002 - issue_number: {{TEMP-2}}
* IS002 - title: api: instance today helper and day defaulting
* IS002 - state: open
* IS002 - labels: api
* IS002 - milestone: none
* IS002 - assignees: none

### IS002 - body

```markdown
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

## Label

`api`
```

### IS002 - Relationships

* none

## IS003 - Create - Display name identity

Local identity without SSO.

IS003 - Similarity: none found

* IS003 - issue_number: {{TEMP-3}}
* IS003 - title: auth: display name identity with cookie continuity
* IS003 - state: open
* IS003 - labels: auth
* IS003 - milestone: none
* IS003 - assignees: none

### IS003 - body

```markdown
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

## Label

`auth`
```

### IS003 - Relationships

* none

## IS004 - Create - Upsert today status API/domain

Create/update doing/blocked/next for today.

IS004 - Similarity: none found

* IS004 - issue_number: {{TEMP-4}}
* IS004 - title: api: upsert today status (doing / blocked / next)
* IS004 - state: open
* IS004 - labels: api
* IS004 - milestone: none
* IS004 - assignees: none

### IS004 - body

```markdown
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

## Label

`api`
```

### IS004 - Relationships

* depends-on {{TEMP-1}}, {{TEMP-2}}, {{TEMP-3}} (logical; not sprint-ordered here)

## IS005 - Create - List today statuses

Read model for today’s board.

IS005 - Similarity: none found

* IS005 - issue_number: {{TEMP-5}}
* IS005 - title: api: list statuses for today board
* IS005 - state: open
* IS005 - labels: api
* IS005 - milestone: none
* IS005 - assignees: none

### IS005 - body

```markdown
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

## Label

`api`
```

### IS005 - Relationships

* depends-on {{TEMP-1}}, {{TEMP-2}} (logical)

## IS006 - Create - HTMX UI for board and form

Vertical UI slice on FastAPI + HTMX.

IS006 - Similarity: none found

* IS006 - issue_number: {{TEMP-6}}
* IS006 - title: ui: today board and status form (HTMX)
* IS006 - state: open
* IS006 - labels: ui
* IS006 - milestone: none
* IS006 - assignees: none

### IS006 - body

```markdown
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

## Label

`ui`
```

### IS006 - Relationships

* depends-on {{TEMP-3}}, {{TEMP-4}}, {{TEMP-5}} (logical)

## IS007 - Create - Automated tests create + list

Release quality gate tests.

IS007 - Similarity: none found

* IS007 - issue_number: {{TEMP-7}}
* IS007 - title: tests: create status and list today board
* IS007 - state: open
* IS007 - labels: tests
* IS007 - milestone: none
* IS007 - assignees: none

### IS007 - body

```markdown
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

## Label

`tests`
```

### IS007 - Relationships

* depends-on {{TEMP-4}}, {{TEMP-5}} (logical)

## IS008 - Create - Local runbook

Operability documentation.

IS008 - Similarity: none found

* IS008 - issue_number: {{TEMP-8}}
* IS008 - title: docs: local-first runbook and start path
* IS008 - state: open
* IS008 - labels: docs
* IS008 - milestone: none
* IS008 - assignees: none

### IS008 - body

```markdown
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

## Label

`docs`
```

### IS008 - Relationships

* none

## IS009 - Create - v0.1.0 release checklist

Thin-slice release bar.

IS009 - Similarity: none found

* IS009 - issue_number: {{TEMP-9}}
* IS009 - title: docs: v0.1.0 release evidence checklist
* IS009 - state: open
* IS009 - labels: docs
* IS009 - milestone: none
* IS009 - assignees: none

### IS009 - body

```markdown
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

## Label

`docs`
```

### IS009 - Relationships

* none
<!-- markdown-table-prettify-ignore-end -->
