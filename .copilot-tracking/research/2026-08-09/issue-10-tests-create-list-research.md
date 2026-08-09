---
title: "Issue #10 research - tests for create status and list today board"
description: Research-only findings for PulseBoard TEMP-7 and GitHub issue #10 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-10
  - tests
  - create
  - list
  - research
  - rpi
estimated_reading_time: 8
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#10](https://github.com/AbhranilGit/HVE-Core-Course/issues/10) - tests: create status and list today board |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-7 |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete - ready for Plan gate |
| Production code | None (this phase) |
| Sprint | 1 of 3 (Sprint 2) |
| Depends on | Sprint 1 create/list behavior |

## Scope summary (authoritative)

From TEMP-7 and issue #10:

In scope:

* Pytest tests with isolated temp SQLite DB
* Cover create today status behavior
* Cover rejection of invalid empty fields and blank name where applicable
* Cover list today behavior and prior-day exclusion
* Cover upsert does not duplicate row for same name and day
* Document how to run tests (`pytest`) for release evidence

Out of scope:

* Full browser end-to-end suite
* Load/performance testing beyond smoke
* Product feature additions under `src/` unless strictly required for testability

Acceptance criteria to drive planning:

| ID | Criterion | Source |
|----|-----------|--------|
| AC-P-060 | Test suite on clean env exercises create status and list/view today board and passes | PRD AC-008.3, NFR-008 |
| AC-P-061 | Create then list today returns stored values for today under display name | PRD AC-002.1, AC-004.2 |
| AC-P-062 | Same name posts twice today results in one row with latest values | PRD AC-003.1, FR-004 |
| AC-P-063 | Prior-day fixture data is excluded from today list | PRD AC-004.3 |

## Evidence log

### Current Sprint 1 behavior status

| Slice | Status | Evidence |
|-------|--------|----------|
| #4 identity | In place | `tests/test_identity.py` |
| #5 create/upsert status | In place | `tests/test_status_upsert.py` |
| #3 list today API | In place | `tests/test_status_list_today.py` |
| #9 UI board flow | In place | `tests/test_ui_today_board.py` |

Blocker conclusion: no hard blocker found. Sprint 1 create/list capabilities exist and are testable in isolation.

### Existing test coverage versus TEMP-7 ACs

| TEMP-7 AC | Existing coverage signal | Gap assessment |
|-----------|--------------------------|----------------|
| AC-P-060 | Full suite passes with create/list tests already present | Partial process gap: release-evidence framing for issue #10 should be explicit and central |
| AC-P-061 | `test_status_upsert` + `test_status_list_today` + `test_ui_today_board` verify create and list values | Functional behavior covered; may need one explicit end-to-end create-then-list test anchored to TEMP-7 |
| AC-P-062 | `test_ac_p_032_second_submit_one_row` in `test_status_upsert.py` | Covered at API+DB level; can be mirrored in issue-10 specific suite for release traceability |
| AC-P-063 | `test_ac_p_042_prior_day_rows_are_excluded` in `test_status_list_today.py` and prior repo tests | Covered; issue-10 may consolidate evidence in one dedicated test module |

### Repo patterns relevant to test-only work

| Pattern | Current implementation |
|---------|------------------------|
| Test runner | `pytest` configured in [pyproject.toml](../../../../pyproject.toml) |
| Test location | `tests/` with focused modules per issue |
| DB isolation | `tmp_path` and `create_app(db_path=...)` fixture style |
| API test style | `fastapi.testclient.TestClient` context manager |
| Data seeding | route-based posts or repository direct `upsert_status` where setup is simpler |
| Day boundary handling | helper `default_status_day_str` and optional env control |

### Constraints from PRD and ADRs

| Source | Constraint for #10 |
|--------|--------------------|
| PRD AC-008.3 + NFR-008 | Automated tests must cover create and list before release tag |
| PRD AC-002.1 | Create stores today status under display name |
| PRD AC-003.1 | Upsert updates single row, no duplicate for same name/day |
| PRD AC-004.2/004.3 | List contains today rows with required fields and excludes prior-day rows |
| ADR status model | One row per name/day and at-least-one-field rule |
| ADR SQLite | Test isolation via temp DB files is preferred and supported |
| ADR today timezone | Today list membership follows instance day rule |

## Design options for planning

### Option A (recommended)

Add a dedicated issue-10 test module that explicitly maps AC-P-060..063 and reuses existing helpers/patterns.

* Pros:
  * Clear release-evidence traceability to TEMP-7
  * Low risk, no product changes
  * Avoids hidden reliance on cross-issue test names
* Cons:
  * Some overlap with existing tests

### Option B

Treat existing Sprint 1 tests as sufficient and add only a lightweight release-evidence document.

* Pros:
  * Minimal code churn
* Cons:
  * Weaker AC-level traceability inside issue-10 implementation artifacts
  * Might not satisfy expectation to "add automated tests" in issue language

### Option C

Refactor existing test files into a single consolidated create/list package.

* Pros:
  * Centralized maintenance
* Cons:
  * High churn and regression risk for little product value

Research recommendation: Option A. Add a compact issue-10 test module focused on release-bar ACs without deleting prior tests.

## Candidate tests for issue-10 planning

1. AC-P-060 smoke path: run create/list-focused tests in clean temp DB context and assert pass conditions.
2. AC-P-061 explicit create-then-list: set identity, post status, list today, assert display name and values returned.
3. AC-P-062 explicit same-day upsert: post twice for same identity, list today, assert one row with latest values.
4. AC-P-063 prior-day exclusion: seed prior-day row and assert default today list omits it.

These can be implemented as API-level tests with TestClient and optional repository fixtures for prior-day setup.

## Risks and mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Duplicate-test drift with existing files | Maintenance noise | Keep issue-10 tests concise and AC-focused; avoid broad duplication |
| Scope creep into product changes | Delay and risk | Restrict edits to `tests/` and docs unless blocker demands minimal `src/` change |
| Flaky day-boundary assertions | Intermittent failures | Use explicit seeded dates or immediate helper-based day comparisons |
| Ambiguous release evidence | Review friction | Map each test clearly to AC-P-060..063 in test names and implement docs |

## Explicit non-goals for this issue

* No UI feature work
* No API behavior changes unless testability blocker is proven
* No performance/load suite
* No Sprint 2 issue #8 or #7 work in this phase

## Open questions for planning (non-blocking)

1. Should issue-10 tests be in one file (for example `tests/test_release_create_list.py`) or split by API and repo layers?
2. Should AC-P-060 be represented as a meta test marker or satisfied through explicit implement evidence and command output?
3. Is minimal update to docs required in this issue for "how to run tests" or is implement artifact command evidence enough?

## Ready for plan?

- [x] TEMP-7 scope and AC-P-060..063 captured
- [x] Sprint 1 create/list behavior confirmed available
- [x] Repo testing patterns and constraints documented
- [x] Options and gaps captured for plan phase
- [x] No production code written in this phase
- [ ] User verifies Research checklist in [README.md](README.md) before Plan (`continue=2`)

## Next

After Research gate: run `/rpi continue=2` to write issue-10 plan only.
