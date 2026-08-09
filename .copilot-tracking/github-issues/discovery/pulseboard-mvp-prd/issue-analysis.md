<!-- markdownlint-disable-file -->
<!-- markdown-table-prettify-ignore-start -->
# Discovery Issue Analysis - PulseBoard MVP PRD Backlog

* **Artifact(s)**: lifecycle/03-product-definition/output/prd.md, lifecycle/03-product-definition/output/adr/
* **Repository**: AbhranilGit/HVE-Core-Course
* **Milestone**: none

## Planned Issues

### IS001 - Create - SQLite schema and status repository

* **Working Title**: api: SQLite schema and status repository for today
* **Key Search Terms**: "sqlite schema", "status repository", "pulseboard db"
* **Working Labels**: api
* **Suggested Issue Field Values**:
  * labels: api
  * milestone: none

#### Related Requirements

* PRD FR-008, US-006, NFR-008
* ADR sqlite-local-persistence; status-domain-model unique (display_name, status_day)

### IS002 - Create - Instance today helper

* **Working Title**: api: instance today helper and day defaulting
* **Key Search Terms**: "instance today", "timezone", "status_day"
* **Working Labels**: api
* **Related**: PRD FR-007, AC-002.2, AC-004.3; ADR today-instance-timezone

### IS003 - Create - Display name identity

* **Working Title**: auth: display name identity with cookie continuity
* **Key Search Terms**: "display name", "identity cookie"
* **Working Labels**: auth
* **Related**: PRD US-001, FR-001, AC-001.*; ADR local-identity-display-name

### IS004 - Create - Upsert today status

* **Working Title**: api: upsert today status (doing / blocked / next)
* **Key Search Terms**: "upsert status", "create today status"
* **Working Labels**: api
* **Related**: PRD US-002, US-003, FR-002..FR-004, AC-002.*, AC-003.*

### IS005 - Create - List today statuses

* **Working Title**: api: list statuses for today board
* **Key Search Terms**: "list today", "today board api"
* **Working Labels**: api
* **Related**: PRD US-004, US-005, FR-005, FR-006, AC-004.*, AC-005.*

### IS006 - Create - HTMX board and form UI

* **Working Title**: ui: today board and status form (HTMX)
* **Key Search Terms**: "htmx board", "status form"
* **Working Labels**: ui
* **Related**: PRD §5 UX, US-001..US-005 UI surfaces; ADR web-stack-fastapi-htmx

### IS007 - Create - Create/list automated tests

* **Working Title**: tests: create status and list today board
* **Key Search Terms**: "create status test", "today board test"
* **Working Labels**: tests
* **Related**: PRD AC-008.3, NFR-008, US-008

### IS008 - Create - Local runbook

* **Working Title**: docs: local-first runbook and start path
* **Key Search Terms**: "runbook", "local start"
* **Working Labels**: docs
* **Related**: PRD US-007, FR-009, AC-007.*, OQ-PRD-02

### IS009 - Create - v0.1.0 release checklist

* **Working Title**: docs: v0.1.0 release evidence checklist
* **Key Search Terms**: "v0.1.0 checklist", "scope guardrail"
* **Working Labels**: docs
* **Related**: PRD US-008, FR-010, AC-008.*

## Out of backlog (explicit)

* SSO/OAuth, notifications, mobile, websockets, multi-day history UI, RBAC, rich media, project tracker features
<!-- markdown-table-prettify-ignore-end -->
