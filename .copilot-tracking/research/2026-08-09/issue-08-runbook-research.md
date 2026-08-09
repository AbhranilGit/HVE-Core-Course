<!-- markdownlint-disable-file -->

---
title: "Issue #8 research - local-first runbook and start path"
description: Research-only findings for PulseBoard TEMP-8 and GitHub issue #8 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-08
  - docs
  - runbook
  - local-first
  - research
  - rpi
estimated_reading_time: 9
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#8](https://github.com/AbhranilGit/HVE-Core-Course/issues/8) - docs: local-first runbook and start path |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-8 |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete - ready for Plan gate |
| Production code | None (this phase) |
| Sprint | 2 of 3 (Sprint 2) |
| Depends on | Runnable Sprint 1 behavior |

## Scope summary (authoritative)

From TEMP-8 and issue #8:

In scope:

* Prerequisites for local run (Python 3.12+, env notes)
* Install/start commands
* URL/host/port to open
* Local-first deployment model statement
* DB file location details and `PULSEBOARD_DB_PATH`
* Instance timezone behavior and `PULSEBOARD_TZ`
* How to run tests (`pytest`)
* Canonical runbook path, preferably under operations output

Out of scope:

* Cloud deployment guides
* SSO setup
* Mobile installation

Acceptance criteria to drive planning:

| ID | Criterion | Source |
|----|-----------|--------|
| AC-P-070 | New operator can start app and reach today board UI by following docs only | PRD AC-007.1 |
| AC-P-071 | Docs state how to start, where to open app, and that deployment is local-first | PRD AC-007.2 |
| AC-P-072 | Docs explain DB path and today/timezone behavior at operator level | PRD AC-006.2, sqlite/today ADRs |

## Evidence log

### How the app actually starts now

| Fact | Evidence |
|------|----------|
| ASGI app entrypoint is `pulseboard.app:app` | `src/pulseboard/app.py` module-level `app = create_app()` |
| Local run command appears in app docstring | `uvicorn pulseboard.app:app --reload` |
| Primary UI route exists | `GET /` in `src/pulseboard/app.py` |
| Identity and status routes are present | `/identity`, `/ui/identity`, `/status`, `/ui/status`, `/statuses/today` |
| Python requirement is 3.12+ | `pyproject.toml` `requires-python = ">=3.12"` |
| Runtime dependencies include FastAPI/Uvicorn | `pyproject.toml` dependencies |

Operator implication for docs:

* Start path can be documented as `uvicorn pulseboard.app:app --reload` after dependency install and environment activation.
* Reachability target should include opening the board at `/` on default Uvicorn host/port unless overridden.

### Where data lives now

| Fact | Evidence |
|------|----------|
| Persistence is SQLite local file | `src/pulseboard/db.py` module docstring and ADR sqlite |
| DB path precedence is explicit path > env > default | `resolve_db_path` in `src/pulseboard/db.py` |
| Env override is `PULSEBOARD_DB_PATH` | `src/pulseboard/db.py` |
| Default DB path is `data/pulseboard.db` relative to current working directory | `DEFAULT_DB_PATH` in `src/pulseboard/db.py` |
| Schema auto-init happens on app creation/startup | `init_db` call in `create_app` and lifespan |

Operator implication for docs:

* Runbook must state default local DB location and optional env override.
* Local-first statement should explicitly say no cloud DB required.

### Timezone and "today" behavior

| Fact | Evidence |
|------|----------|
| Day boundary uses instance timezone | `src/pulseboard/today.py` and ADR today timezone |
| Env override is `PULSEBOARD_TZ` with IANA timezone names | `resolve_instance_tz` in `today.py` |
| Default timezone is host local if env is unset | `resolve_instance_tz` behavior |
| Invalid timezone fails fast with ValueError | `today.py` error handling |

Operator implication for docs:

* Runbook must document timezone default and override semantics.
* Troubleshooting note should include invalid timezone value behavior.

### Current docs and operations path state

| Item | Current state |
|------|---------------|
| `lifecycle/09-operations/output/` | Contains only `.gitkeep` (no runbook yet) |
| `lifecycle/09-operations/README.md` | Missing file |
| Lifecycle index guidance | `lifecycle/README.md` states stage 9 output is `output/runbook.md` |
| Root README | Mentions Python 3.12 and conda `hve-env` but not full canonical run path yet |

Blocker conclusion:

* No code blocker for docs issue.
* Documentation gap exists: canonical operations runbook file is not yet authored.

## Constraints from PRD and ADRs

| Source | Constraint for #8 |
|--------|-------------------|
| PRD FR-009 / US-007 | Must provide local start path from docs only |
| PRD AC-007.1 | A new operator can start and reach board UI from docs alone |
| PRD AC-007.2 | Docs must include start method, where app is reached, and local-first model |
| PRD AC-006.2 | Persistence docs must describe local-machine DB model |
| PRD OQ-PRD-02 | One canonical runbook path should be documented |
| ADR sqlite | DB is local file, default path and env override should be documented |
| ADR today timezone | Today boundary and TZ override should be documented |
| ADR web stack | Uvicorn/FastAPI local run posture should be reflected |

## Repo patterns relevant to implementation planning

| Pattern | Observation |
|---------|-------------|
| Lifecycle artifacts | Stage output docs live under `lifecycle/NN-*/output/` |
| RPI verification | Issue folder has `README.md` gate checklists |
| Existing docs style | Frontmatter + tabular control metadata in issue artifacts |
| Test command | `pytest` is standard and should be documented with env context |

## Design options for planning

### Option A (recommended)

Create canonical runbook at `lifecycle/09-operations/output/runbook.md` and add/adjust pointers from README and issue artifacts as needed.

* Pros:
  * Matches lifecycle stage intent exactly
  * Resolves PRD canonical path ambiguity cleanly
  * Keeps operational detail in stage 9 output
* Cons:
  * Requires maintaining a pointer from root docs for discoverability

### Option B

Make root README the canonical runbook and skip stage-9 runbook file.

* Pros:
  * Single top-level entry
* Cons:
  * Conflicts with lifecycle convention that operations output holds runbook
  * Harder to keep stage-specific evidence in one place

### Option C

Duplicate full run instructions in multiple files.

* Pros:
  * Convenience in each location
* Cons:
  * Drift risk and conflicting instructions

Research recommendation: Option A with one canonical runbook and lightweight pointers elsewhere.

## Candidate runbook content blocks for plan

1. Prerequisites section:
   * Python 3.12+
   * Optional/recommended conda env (`hve-env`)
2. Install section:
   * `python -m pip install -e ".[dev]"`
3. Start section:
   * `uvicorn pulseboard.app:app --reload`
4. Reachability section:
   * default URL and board path (`/`)
5. Data section:
   * default DB file path and `PULSEBOARD_DB_PATH`
6. Timezone section:
   * host local default and `PULSEBOARD_TZ` override
7. Test section:
   * `python -m pytest tests/ -q` (or equivalent)
8. Local-first model statement:
   * single-machine local deployment and no cloud DB requirement

## Risks and mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Conflicting instructions across docs | Operator confusion | Declare one canonical runbook path and add pointers only |
| Startup command mismatch with actual app | AC-P-070 failure | Source commands directly from app/pyproject and validate in implement phase |
| DB/TZ details omitted | AC-P-072 failure | Include explicit env var and default path/timezone behavior sections |
| Unclear URL/port guidance | AC-P-071 failure | Document concrete open URL and route |

## Explicit non-goals for this issue

* No code feature additions
* No cloud deployment tutorial
* No SSO/mobile guidance
* No Sprint 2 issue #7 work in this phase

## Open questions for planning (non-blocking)

1. Should README contain only a short pointer or a minimal quickstart plus pointer to canonical runbook?
2. Should host/port guidance mention only defaults or include optional override examples?
3. Should troubleshooting include a brief invalid `PULSEBOARD_TZ` example now or defer to later operations hardening?

## Ready for plan?

- [x] TEMP-8 scope and AC-P-070..072 captured
- [x] Startup and data-location behavior verified from current code
- [x] DB and timezone operator semantics captured
- [x] Canonical-path gap identified with recommended approach
- [x] No production code written in this phase
- [ ] User verifies Research checklist in [README.md](README.md) before Plan (`continue=2`)

## Next

After Research gate: run `/rpi continue=2` to write issue-08 plan only.
