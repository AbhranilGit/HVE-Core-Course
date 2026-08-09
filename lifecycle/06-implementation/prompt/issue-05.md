# Stage 6 — Issue #5

| | |
| --- | --- |
| **Issue** | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) — api: upsert today status (doing / blocked / next) |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-4** |
| **Sprint order** | 4 of 6 (Sprint 1) |
| **Depends on** | #2, #6, #4 |
| **RPI output** | [`../output/issue-05/`](../output/issue-05/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-05/README.md`](../output/issue-05/README.md).

---

## Agent

**`RPI Agent`**

Select **RPI Agent** in Copilot Chat. Invoke with **`/rpi`**.  
Syntax: `/rpi task=... continue={1|2|3|all}`  
Use `continue=1` (research), `continue=2` (plan), `continue=3` (implement). Do **not** use `continue=all` while gating phases.

Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for implementation.

Before each phase: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-4** / issue #5).

---

## Phase 1 — Research

**Command:** `/rpi` · **`continue=1`**  
**Save to:** `lifecycle/06-implementation/output/issue-05/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-05/README.md` before Plan.

```text
/rpi continue=1 task=Research only for PulseBoard issue #5 (TEMP-4). Do not write production code. Do not plan or implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-4 / GitHub issue #5 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Assume #2, #6, and #4 are in place unless you find a blocker. Capture repo patterns, constraints, options, and open questions needed to plan this issue. Save the research write-up to lifecycle/06-implementation/output/issue-05/research.md
```

---

## Phase 2 — Plan

**Command:** `/rpi` · **`continue=2`**  
**Save to:** `lifecycle/06-implementation/output/issue-05/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-05/README.md` before Implement.

```text
/rpi continue=2 task=Plan implementation of PulseBoard issue #5 (TEMP-4) only. Do not implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-4 / GitHub issue #5 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Base the plan on lifecycle/06-implementation/output/issue-05/research.md. Include steps, files to touch, acceptance checks from the local issue spec, and risks. Stay inside this issue's scope. Leave list API to #3 and UI to #9. Save the plan to lifecycle/06-implementation/output/issue-05/plan.md
```

---

## Phase 3 — Implement

**Command:** `/rpi` · **`continue=3`**  
**Save to:** `lifecycle/06-implementation/output/issue-05/implement.md` (+ code under `src/` / `tests/` as applicable)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-05/README.md` before the next issue.

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #5 (TEMP-4) only. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-4 / GitHub issue #5 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Follow lifecycle/06-implementation/output/issue-05/plan.md. Put application/test changes under src/pulseboard/ and tests/ as needed. Record RPI/session evidence under .copilot-tracking/ when applicable. Write an implement summary (files changed, AC results, deviations) to lifecycle/06-implementation/output/issue-05/implement.md. Do not start issues #3, #9, or Sprint 2 work in this session. Do not widen MVP beyond the local issue spec and accepted PRD in-scope.
```
