# Stage 6 — Issue #4

| | |
| --- | --- |
| **Issue** | [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4) — auth: display name identity with cookie continuity |
| **Sprint order** | 3 of 6 (Sprint 1) |
| **Depends on** | — (UI chrome in #9) |
| **RPI output** | [`../output/issue-04/`](../output/issue-04/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-04/README.md`](../output/issue-04/README.md).

---

## Agent

**`RPI Agent`**, or run the matching `/rpi-*` skill for each phase below.  
Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for implementation.

Before each phase: attach / `#`-reference GitHub issue **#4**.

---

## Phase 1 — Research

**Skill:** `/rpi-research`  
**Save to:** `lifecycle/06-implementation/output/issue-04/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-04/README.md` before Plan.

```text
/rpi-research

Research only for PulseBoard GitHub issue #4.
Do not write production code. Do not plan or implement yet.

Authoritative scope: https://github.com/AbhranilGit/HVE-Core-Course/issues/4
(attach / #reference the issue).
Use PRD/ADRs only where the issue requires them.

Capture: repo patterns, constraints, options, and open questions
needed to plan this issue.

Save the research write-up to:
lifecycle/06-implementation/output/issue-04/research.md
```

---

## Phase 2 — Plan

**Skill:** `/rpi-plan`  
**Save to:** `lifecycle/06-implementation/output/issue-04/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-04/README.md` before Implement.

```text
/rpi-plan

Plan implementation of PulseBoard GitHub issue #4 only.
Do not implement yet.

Authoritative scope: https://github.com/AbhranilGit/HVE-Core-Course/issues/4
(attach / #reference the issue).
Base the plan on: lifecycle/06-implementation/output/issue-04/research.md

Include steps, files to touch, acceptance checks from the issue/PRD,
and risks. Stay inside this issue's scope.

Save the plan to:
lifecycle/06-implementation/output/issue-04/plan.md
```

---

## Phase 3 — Implement

**Skill:** `/rpi-implement`  
**Save to:** `lifecycle/06-implementation/output/issue-04/implement.md` (+ code under `src/` / `tests/` as applicable)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-04/README.md` before the next issue.

```text
/rpi-implement

Implement the approved plan for PulseBoard GitHub issue #4 only.

Authoritative scope: https://github.com/AbhranilGit/HVE-Core-Course/issues/4
(attach / #reference the issue).
Follow: lifecycle/06-implementation/output/issue-04/plan.md

Put application/test changes under src/pulseboard/ and tests/ as needed.
Record RPI/session evidence under .copilot-tracking/ when applicable.

Write an implement summary (files changed, AC results, deviations) to:
lifecycle/06-implementation/output/issue-04/implement.md

Do not start issues #5, #3, #9, or Sprint 2 work in this session.
Do not widen MVP beyond the issue and accepted PRD in-scope.
```
