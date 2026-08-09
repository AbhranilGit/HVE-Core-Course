---
title: "Issue #10 plan - tests for create status and list today board"
description: Implementation plan for PulseBoard TEMP-7 and GitHub issue #10 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
	- pulseboard
	- issue-10
	- tests
	- create
	- list
	- plan
	- rpi
estimated_reading_time: 7
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#10](https://github.com/AbhranilGit/HVE-Core-Course/issues/10) - tests: create status and list today board |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-7 |
| Phase | Plan only (`/rpi continue=2`) |
| Status | Complete - ready for Implement gate |
| Based on | [research.md](research.md) (complete and present) |
| Production code | None (this phase) |
| Sprint | 1 of 3 (Sprint 2) |
| Depends on | Sprint 1 create/list behavior present; no blocker |

## User requests (this phase)

1. Plan implementation of PulseBoard issue #10 (TEMP-7) only
2. Do not implement yet
3. Base this plan on completed [research.md](research.md)
4. Use TEMP-7 scope and acceptance criteria from [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md)
5. Include steps, files to touch, acceptance checks, and risks
6. Stay inside this issue scope
7. Write plan to [plan.md](plan.md)

## Objective

Provide explicit release-bar automated test evidence for create status and list today board behavior, mapped directly to AC-P-060 through AC-P-063, using isolated temp SQLite DB and existing app behavior.

## Alignment with research

| Research decision | Plan adoption |
|-------------------|---------------|
| Recommended option A: dedicated issue-10 AC-focused test module | Yes |
| No product feature additions while writing tests | Yes |
| Reuse existing TestClient and temp DB patterns | Yes |
| Keep scope to create/list release evidence | Yes |

Intentional deltas from research: none.

## Design summary

### Test strategy

| Piece | Decision |
|-------|----------|
| Primary deliverable | Add one focused test module for TEMP-7 acceptance mapping |
| Test layer | API-level integration tests with `TestClient(create_app(db_path=...))` |
| DB isolation | `tmp_path` SQLite files; explicit setup where direct repository seeding is used |
| Data setup | Use existing routes for create/upsert flow; repository helper only for prior-day fixture convenience |
| Evidence style | Each test name/docstring maps to AC-P-060..063 |

### Candidate implementation structure

| Path | Purpose |
|------|---------|
| `tests/test_release_create_list.py` | New TEMP-7 issue-10 focused suite |
| `lifecycle/06-implementation/output/issue-10/implement.md` | AC evidence and command output in continue=3 |

No changes are planned to core behavior in `src/` unless a testability blocker appears during implement.

## Implementation steps

Execute in order during `/rpi continue=3`. Do not start #8 or #7.

### Step 1 - Add issue-10 AC-focused tests

<!-- parallelizable: false -->

1. Create [tests/test_release_create_list.py](../../../../tests/test_release_create_list.py)
2. Add tests mapped to AC-P-060..063:
	 * AC-P-060: clean-env test run path exercises create/list behavior and passes
	 * AC-P-061: create then list today returns stored values for display name
	 * AC-P-062: same name posts twice today yields one row with latest values
	 * AC-P-063: prior-day fixture excluded from default today list
3. Keep tests concise and avoid broad duplication of existing modules

### Step 2 - Keep release evidence explicit

<!-- parallelizable: false -->

1. Ensure test names and docstrings cite the TEMP-7 AC they cover
2. Run targeted module plus full suite to record release evidence
3. Capture exact command(s) and pass results in implement artifact

### Step 3 - Regression verification

<!-- parallelizable: false -->

1. Run full `pytest` suite in hve-env Python 3.12
2. Confirm no regressions in prior Sprint 1 modules

### Step 4 - Implement artifact update

<!-- parallelizable: false -->

1. Write [implement.md](implement.md)
2. Add `.copilot-tracking/changes` entry for issue #10
3. Record AC-by-AC results and any deviations

## Files to touch

| Path | Action | Notes |
|------|--------|-------|
| [tests/test_release_create_list.py](../../../../tests/test_release_create_list.py) | Add | AC-P-060..063 evidence-focused tests |
| [lifecycle/06-implementation/output/issue-10/implement.md](implement.md) | Edit in continue=3 | Implementation evidence |
| [src/pulseboard/app.py](../../../../src/pulseboard/app.py) | No change expected | Only if testability blocker is proven |
| Existing test modules | Minimal/no edits expected | Avoid churn and duplicate overlap unless necessary |

## Acceptance checks

| ID | Criterion (TEMP-7) | How we will verify |
|----|--------------------|--------------------|
| AC-P-060 | Automated tests exercise create status and list/view today board and pass | Run issue-10 module and full pytest, capture pass output |
| AC-P-061 | Create then list returns today values for display name | TestClient flow: set identity, post status, list today, assert values |
| AC-P-062 | Same name posts twice today leaves one row with latest values | Two posts then list/assert single row latest values |
| AC-P-063 | Prior-day fixture excluded from default today list | Seed prior-day data and assert list-today omission |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Duplicate coverage creates maintenance noise | Keep issue-10 tests compact and AC-traceable only |
| Scope creep into product features | Restrict edits to tests/docs unless blocker forces minimal src tweak |
| Time-based flake around day boundary | Use explicit prior-day seed and deterministic helper comparisons |
| Weak release evidence linkage | Include AC labels in tests and implement summary command outputs |

## Out of scope (do not implement in #10)

* New product features beyond testability needs
* Full browser E2E suite
* Load/performance benchmarking
* Issue #8 or #7 work

## Ready to implement?

- [x] Research present and used as sole planning source
- [x] TEMP-7 AC-P-060 through AC-P-063 mapped to concrete checks
- [x] Steps and file touch list stay inside issue #10 scope
- [x] No production code in this phase
- [ ] User verifies Plan checklist in [README.md](README.md) before continue=3

## Next

After plan gate: run `/rpi continue=3` for issue-10 implementation only.
