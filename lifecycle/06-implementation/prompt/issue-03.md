# Stage 6 — Issue #3

| | |
| --- | --- |
| **Issue** | [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3) — api: list statuses for today board |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-5** |
| **Sprint order** | 5 of 6 (Sprint 1) |
| **Depends on** | #2, #6 |
| **RPI output** | [`../output/issue-03/`](../output/issue-03/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-03/README.md`](../output/issue-03/README.md).

---

## Agent

**`RPI Agent`**, or run the matching `/rpi-*` skill for each phase below.  
Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for implementation.

Before each phase: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-5** / issue #3).

---

## Phase 1 — Research

**Skill:** `/rpi-research`  
**Save to:** `lifecycle/06-implementation/output/issue-03/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-03/README.md` before Plan.

```text
/rpi-research

Research only for PulseBoard issue #3 (TEMP-5).
Do not write production code. Do not plan or implement yet.

Authoritative scope (in-repo):
lifecycle/04-decomposition/output/backlog-snapshot.md
— section TEMP-5 / GitHub issue #3
(attach / #reference the backlog snapshot; use that section's acceptance criteria).
Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them.

Capture: repo patterns, constraints, options, and open questions
needed to plan this issue.

Save the research write-up to:
lifecycle/06-implementation/output/issue-03/research.md
```

---

## Phase 2 — Plan

**Skill:** `/rpi-plan`  
**Save to:** `lifecycle/06-implementation/output/issue-03/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-03/README.md` before Implement.

```text
/rpi-plan

Plan implementation of PulseBoard issue #3 (TEMP-5) only.
Do not implement yet.

Authoritative scope (in-repo):
lifecycle/04-decomposition/output/backlog-snapshot.md
— section TEMP-5 / GitHub issue #3
(attach / #reference the backlog snapshot; use that section's acceptance criteria).
Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them.
Base the plan on: lifecycle/06-implementation/output/issue-03/research.md

Include steps, files to touch, acceptance checks from the local issue
spec, and risks. Stay inside this issue's scope.

Save the plan to:
lifecycle/06-implementation/output/issue-03/plan.md
```

---

## Phase 3 — Implement

**Skill:** `/rpi-implement`  
**Save to:** `lifecycle/06-implementation/output/issue-03/implement.md` (+ code under `src/` / `tests/` as applicable)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-03/README.md` before the next issue.

```text
/rpi-implement

Implement the approved plan for PulseBoard issue #3 (TEMP-5) only.

Authoritative scope (in-repo):
lifecycle/04-decomposition/output/backlog-snapshot.md
— section TEMP-5 / GitHub issue #3
(attach / #reference the backlog snapshot; use that section's acceptance criteria).
Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them.
Follow: lifecycle/06-implementation/output/issue-03/plan.md

Put application/test changes under src/pulseboard/ and tests/ as needed.
Record RPI/session evidence under .copilot-tracking/ when applicable.

Write an implement summary (files changed, AC results, deviations) to:
lifecycle/06-implementation/output/issue-03/implement.md

Do not start issue #9 or Sprint 2 work in this session.
Do not widen MVP beyond the local issue spec and accepted PRD in-scope.
```
