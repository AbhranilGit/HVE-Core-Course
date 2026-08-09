<!-- markdownlint-disable-file -->
<!-- markdown-table-prettify-ignore-start -->
# Discovery - Issue Planning Log

* **Repository**: AbhranilGit/HVE-Core-Course
* **Milestone**: none (Stage 5 owns sprint ordering)
* **Previous Phase**: N/A
* **Current Phase**: Phase-3 Handoff

## Status

PRD parsed; 9 Create candidates planned; duplicate search intended against repo; GitHub MCP tools unavailable in this session for live search/create.

**Summary**: Artifact-driven discovery from accepted PulseBoard MVP PRD and ADRs. Issues sized as thin vertical-slice backlog without sprint ordering.

## Discovered Artifacts and Related Files

* AT001 lifecycle/03-product-definition/output/prd.md - Complete - Processing
* AT002 lifecycle/03-product-definition/output/adr/ - Complete - Related
* AT003 lifecycle/02-discovery/output/brd.md - Complete - Related (scope bound only)

## Discovered GitHub Issues

* None retrieved (GitHub search MCP unavailable this session)

## Issue Progress

### **IS001** - api - Complete

* Working Search Keywords: "SQLite schema status" OR "status domain" OR "pulseboard db"
* Suggested Action: Create
* Title: api: SQLite schema and status repository for today

### **IS002** - api - Complete

* Working Search Keywords: "instance today" OR "timezone" OR "status_day"
* Suggested Action: Create
* Title: api: instance today helper and day defaulting

### **IS003** - auth - Complete

* Working Search Keywords: "display name" OR "identity cookie"
* Suggested Action: Create
* Title: auth: display name identity with cookie continuity

### **IS004** - api - Complete

* Working Search Keywords: "upsert status" OR "create today status"
* Suggested Action: Create
* Title: api: upsert today status (doing / blocked / next)

### **IS005** - api - Complete

* Working Search Keywords: "list today board" OR "today statuses"
* Suggested Action: Create
* Title: api: list statuses for today board

### **IS006** - ui - Complete

* Working Search Keywords: "HTMX board" OR "status form UI"
* Suggested Action: Create
* Title: ui: today board and status form (HTMX)

### **IS007** - tests - Complete

* Working Search Keywords: "create status test" OR "today board test"
* Suggested Action: Create
* Title: tests: create status and list today board

### **IS008** - docs - Complete

* Working Search Keywords: "runbook" OR "local start" OR "README run"
* Suggested Action: Create
* Title: docs: local-first runbook and start path

### **IS009** - docs - Complete

* Working Search Keywords: "v0.1.0 release checklist" OR "scope guardrail"
* Suggested Action: Create
* Title: docs: v0.1.0 release evidence checklist

## Doc Analysis - issue-analysis.md

### lifecycle/03-product-definition/output/prd.md

* Mapped US-001..US-008 and FR-001..FR-010 into IS001..IS009
* Excluded out-of-scope: SSO, notifications, mobile, websockets, history UI, RBAC, tracker
* No sprint ordering applied

## Notes

* Labels constrained to user request set: api, ui, auth, docs, tests (one primary label per issue)
* Thin slice path (suggested, not ordered as sprint): IS001 → IS002 → IS003 → IS004 → IS005 → IS006 → IS007 → IS008 → IS009
<!-- markdown-table-prettify-ignore-end -->
