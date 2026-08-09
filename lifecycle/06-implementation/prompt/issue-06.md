# Stage 6 — Issue #6

| | |
| --- | --- |
| **Issue** | [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6) — api: instance today helper and day defaulting |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-2** |
| **Sprint order** | 2 of 6 (Sprint 1) |
| **Depends on** | Prefer after #2 |
| **RPI output** | [`../output/issue-06/`](../output/issue-06/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-06/README.md`](../output/issue-06/README.md).

---

## Agent

**`RPI Agent`**

Select **RPI Agent** in Copilot Chat. Invoke with **`/rpi`**.  
Syntax: `/rpi task=... continue={1|2|3|all}`  
Use `continue=1` (research), `continue=2` (plan), `continue=3` (implement). Do **not** use `continue=all` while gating phases.

Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for implementation.

Before each phase: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-2** / issue #6).

---

## Phase 1 — Research

**Command:** `/rpi` · **`continue=1`**  
**Save to:** `lifecycle/06-implementation/output/issue-06/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-06/README.md` before Plan.

```text
/rpi continue=1 task=Research only for PulseBoard issue #6 (TEMP-2). Do not write production code. Do not plan or implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-2 / GitHub issue #6 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Assume #2 schema work is in place unless you find a blocker. Capture repo patterns, constraints, options, and open questions needed to plan this issue. Save the research write-up to lifecycle/06-implementation/output/issue-06/research.md
```

---

## Phase 2 — Plan

**Command:** `/rpi` · **`continue=2`**  
**Save to:** `lifecycle/06-implementation/output/issue-06/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-06/README.md` before Implement.

```text
/rpi continue=2 task=Plan implementation of PulseBoard issue #6 (TEMP-2) only. Do not implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-2 / GitHub issue #6 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Base the plan on lifecycle/06-implementation/output/issue-06/research.md. Include steps, files to touch, acceptance checks from the local issue spec, and risks. Stay inside this issue's scope. Save the plan to lifecycle/06-implementation/output/issue-06/plan.md
```

---

## Phase 3 — Implement

**Command:** `/rpi` · **`continue=3`**  
**Save to:** `lifecycle/06-implementation/output/issue-06/implement.md` (+ code under `src/` / `tests/` as applicable)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-06/README.md` before the next issue.

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #6 (TEMP-2) only. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-2 / GitHub issue #6 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Follow lifecycle/06-implementation/output/issue-06/plan.md. Put application/test changes under src/pulseboard/ and tests/ as needed. Record RPI/session evidence under .copilot-tracking/ when applicable. Write an implement summary (files changed, AC results, deviations) to lifecycle/06-implementation/output/issue-06/implement.md. Do not start issues #4, #5, #3, #9, or Sprint 2 work in this session. Do not widen MVP beyond the local issue spec and accepted PRD in-scope.
```
