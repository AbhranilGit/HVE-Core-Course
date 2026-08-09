# Stage 6 — Issue #2

| | |
| --- | --- |
| **Issue** | [#2](https://github.com/AbhranilGit/HVE-Core-Course/issues/2) — api: SQLite schema and status repository for today |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-1** |
| **Sprint order** | 1 of 6 (Sprint 1) |
| **Depends on** | — |
| **RPI output** | [`../output/issue-02/`](../output/issue-02/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-02/README.md`](../output/issue-02/README.md).

---

## Agent

**`RPI Agent`**

Select **RPI Agent** in Copilot Chat. Invoke with **`/rpi`**.  
Syntax: `/rpi task=... continue={1|2|3|all}`  
Use `continue=1` (research), `continue=2` (plan), `continue=3` (implement). Do **not** use `continue=all` while gating phases.

Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for implementation.

Before each phase: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-1** / issue #2).

---

## Phase 1 — Research

**Command:** `/rpi` · **`continue=1`**  
**Save to:** `lifecycle/06-implementation/output/issue-02/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-02/README.md` before Plan.

```text
/rpi continue=1 task=Research only for PulseBoard issue #2 (TEMP-1). Do not write production code. Do not plan or implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-1 / GitHub issue #2 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Capture repo patterns, constraints, options, and open questions needed to plan this issue. Save the research write-up to lifecycle/06-implementation/output/issue-02/research.md
```

---

## Phase 2 — Plan

**Command:** `/rpi` · **`continue=2`**  
**Save to:** `lifecycle/06-implementation/output/issue-02/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-02/README.md` before Implement.

```text
/rpi continue=2 task=Plan implementation of PulseBoard issue #2 (TEMP-1) only. Do not implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-1 / GitHub issue #2 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Base the plan on lifecycle/06-implementation/output/issue-02/research.md. Include steps, files to touch, acceptance checks from the local issue spec, and risks. Stay inside this issue's scope. Save the plan to lifecycle/06-implementation/output/issue-02/plan.md
```

---

## Phase 3 — Implement

**Command:** `/rpi` · **`continue=3`**  
**Save to:** `lifecycle/06-implementation/output/issue-02/implement.md` (+ code under `src/` / `tests/` as applicable)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-02/README.md` before the next issue.

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #2 (TEMP-1) only. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-1 / GitHub issue #2 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Follow lifecycle/06-implementation/output/issue-02/plan.md. Put application/test changes under src/pulseboard/ and tests/ as needed. Record RPI/session evidence under .copilot-tracking/ when applicable. Write an implement summary (files changed, AC results, deviations) to lifecycle/06-implementation/output/issue-02/implement.md. Do not start issues #6, #4, #5, #3, #9, or Sprint 2 work in this session. Do not widen MVP beyond the local issue spec and accepted PRD in-scope.
```
