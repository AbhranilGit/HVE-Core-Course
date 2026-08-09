---
title: "Issue #8 plan - local-first runbook and start path"
description: Implementation plan for PulseBoard TEMP-8 and GitHub issue #8 based on completed research; no code in this phase
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-08
  - docs
  - runbook
  - local-first
  - plan
  - rpi
estimated_reading_time: 7
---

## Document control

| Field | Value |
| --- | --- |
| Issue | [#8](https://github.com/AbhranilGit/HVE-Core-Course/issues/8) - docs: local-first runbook and start path |
| Phase | Plan (`/rpi continue=2`) |
| Status | Ready for implement after Plan gate verification |
| Based on | [research.md](research.md) |
| Scope source | [lifecycle/04-decomposition/output/backlog-snapshot.md](../../../04-decomposition/output/backlog-snapshot.md) TEMP-8 |
| Canonical doc target | [lifecycle/09-operations/output/runbook.md](../../../09-operations/output/runbook.md) |

## Plan summary

Create one canonical local-operations runbook at [lifecycle/09-operations/output/runbook.md](../../../09-operations/output/runbook.md) that enables a new operator to start PulseBoard on Python 3.12+, open the today board UI, and understand local DB/timezone behavior. Add a minimal pointer from top-level docs only if needed for discoverability, while avoiding duplicate full instructions.

This plan stays inside issue #8 scope and does not add product features.

## User requests (this phase)

1. Plan implementation of PulseBoard issue #8 (TEMP-8) only
2. Do not implement yet
3. Base this plan on completed [research.md](research.md)
4. Use TEMP-8 scope from [lifecycle/04-decomposition/output/backlog-snapshot.md](../../../04-decomposition/output/backlog-snapshot.md)
5. Prefer [lifecycle/09-operations/output/runbook.md](../../../09-operations/output/runbook.md) if it matches issue scope
6. Include steps, files to touch, acceptance checks, and risks
7. Stay inside issue #8 scope only

## Steps

1. Reconfirm scope and AC mapping from TEMP-8 in [lifecycle/04-decomposition/output/backlog-snapshot.md](../../../04-decomposition/output/backlog-snapshot.md)
2. Reconfirm all operator facts from [research.md](research.md) and avoid contradictions
3. Create or replace [lifecycle/09-operations/output/runbook.md](../../../09-operations/output/runbook.md) as the canonical runbook
4. Author only these runbook sections: prerequisites, install, start, open URL, local-first model, DB path behavior, timezone behavior, and test command
5. Optionally add a short pointer in [README.md](../../../../README.md) to the canonical runbook without duplicating full instructions
6. Validate runbook coverage against AC-P-070, AC-P-071, and AC-P-072
7. Record implement-phase evidence and AC results in [implement.md](implement.md)

## Files to touch

| Path | Planned change | Why |
| --- | --- | --- |
| [lifecycle/09-operations/output/runbook.md](../../../09-operations/output/runbook.md) | Create canonical runbook content | Primary deliverable for AC-P-070 to AC-P-072 |
| [README.md](../../../../README.md) | Optional short pointer to runbook only | Improves discoverability while keeping one canonical source |
| [lifecycle/06-implementation/output/issue-08/implement.md](implement.md) | Implement-phase evidence only | Required issue traceability after docs update |

No production code files under src or tests are in scope for this issue.

## Acceptance checks

| AC / check | How we will verify during Implement |
| --- | --- |
| AC-P-070: New operator can start app and reach today board UI from docs-only path | From runbook-only instructions, confirm explicit prerequisites, install/start command, and open URL/path for board (`/`) are present and sequenced |
| AC-P-071: Docs state how to start, where to open app, and local-first deployment | Confirm runbook includes exact start command, reachability location, and an explicit local-first statement (no cloud DB requirement) |
| AC-P-072: Docs describe DB path and today/TZ behavior | Confirm runbook documents default DB path, `PULSEBOARD_DB_PATH` override, instance-today behavior, host-local default TZ, and `PULSEBOARD_TZ` override semantics |
| Scope guard | Confirm no cloud deploy, SSO, or mobile guidance added |
| Non-feature guard | Confirm no code changes under src/tests |

## Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Duplicate or conflicting instructions across docs | Operator confusion; AC-P-070 ambiguity | Keep [lifecycle/09-operations/output/runbook.md](../../../09-operations/output/runbook.md) canonical and keep any README update to pointer-only |
| Command drift from actual runtime behavior | Runbook fails in practice | Use only commands and behavior already verified in [research.md](research.md) |
| Incomplete DB/TZ operator detail | AC-P-072 failure | Include explicit env var names, defaults, and expected behavior in dedicated sections |
| Over-expanding scope into platform guidance | Delays and scope creep | Enforce out-of-scope list from TEMP-8 during review |

## Out of scope for this plan

* Cloud deployment playbooks
* SSO or identity provider setup
* Mobile install/use instructions
* Product behavior changes or new endpoints
* Work on issue #7 or any issue other than #8

## Ready to implement

- [x] Plan is based on completed [research.md](research.md)
- [x] Plan maps directly to TEMP-8 AC-P-070, AC-P-071, AC-P-072
- [x] Canonical target path selected: [lifecycle/09-operations/output/runbook.md](../../../09-operations/output/runbook.md)
- [x] Steps, file touch list, acceptance checks, and risks are defined
- [ ] Verification checklist in [README.md](README.md) is marked before starting Implement
