# Stage 6 — Issue #9

| | |
| --- | --- |
| **Issue** | [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9) — ui: today board and status form (HTMX) |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-6** |
| **Sprint order** | 6 of 6 (Sprint 1) |
| **Depends on** | #4, #5, #3 |
| **RPI output** | [`../output/issue-09/`](../output/issue-09/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-09/README.md`](../output/issue-09/README.md).

---

## Agent

**`RPI Agent`**

Select **RPI Agent** in Copilot Chat. Invoke with **`/rpi`**.  
Syntax: `/rpi task=... continue={1|2|3|all}`  
Use `continue=1` (research), `continue=2` (plan), `continue=3` (implement). Do **not** use `continue=all` while gating phases.

Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for implementation.

Before each phase: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-6** / issue #9).

---

## Phase 1 — Research

**Command:** `/rpi` · **`continue=1`**  
**Save to:** `lifecycle/06-implementation/output/issue-09/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-09/README.md` before Plan.

```text
/rpi continue=1 task=Research only for PulseBoard issue #9 (TEMP-6). Do not write production code. Do not plan or implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-6 / GitHub issue #9 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Assume #4, #5, and #3 expose enough behavior to wire the UI; note blockers if missing. Capture repo patterns, constraints, options, and open questions needed to plan this issue. Save the research write-up to lifecycle/06-implementation/output/issue-09/research.md
```

---

## Phase 2 — Plan

**Command:** `/rpi` · **`continue=2`**  
**Save to:** `lifecycle/06-implementation/output/issue-09/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-09/README.md` before Implement.

```text
/rpi continue=2 task=Plan implementation of PulseBoard issue #9 (TEMP-6) only. Do not implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-6 / GitHub issue #9 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Base the plan on lifecycle/06-implementation/output/issue-09/research.md. Include steps, files to touch, acceptance checks from the local issue spec, and risks. Stay inside this issue's scope. Save the plan to lifecycle/06-implementation/output/issue-09/plan.md
```

---

## Phase 3 — Implement

**Command:** `/rpi` · **`continue=3`**  
**Save to:** `lifecycle/06-implementation/output/issue-09/implement.md` (+ code under `src/` / `tests/` as applicable)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-09/README.md` before the next issue.

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #9 (TEMP-6) only. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-6 / GitHub issue #9 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and adr/ only where the issue requires them. Follow lifecycle/06-implementation/output/issue-09/plan.md. Put application/test changes under src/pulseboard/ and tests/ as needed. Record RPI/session evidence under .copilot-tracking/ when applicable. Write an implement summary (files changed, AC results, deviations) to lifecycle/06-implementation/output/issue-09/implement.md. Do not start Sprint 2 (#10, #8, #7) work in this session until Sprint 1 is demoable. Do not widen MVP beyond the local issue spec and accepted PRD in-scope.
```
