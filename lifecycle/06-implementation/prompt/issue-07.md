# Stage 6 — Issue #7

| | |
| --- | --- |
| **Issue** | [#7](https://github.com/AbhranilGit/HVE-Core-Course/issues/7) — docs: v0.1.0 release evidence checklist |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-9** |
| **Sprint order** | 3 of 3 (Sprint 2) |
| **Depends on** | #10 evidence; Sprint 1 P0 |
| **RPI output** | [`../output/issue-07/`](../output/issue-07/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-07/README.md`](../output/issue-07/README.md).

---

## Agent

**`RPI Agent`**

Select **RPI Agent** in Copilot Chat. Invoke with **`/rpi`**.  
Syntax: `/rpi task=... continue={1|2|3|all}`  
Use `continue=1` (research), `continue=2` (plan), `continue=3` (implement). Do **not** use `continue=all` while gating phases.

Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for this step.

Before each phase: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-9** / issue #7).

---

## Phase 1 — Research

**Command:** `/rpi` · **`continue=1`**  
**Save to:** `lifecycle/06-implementation/output/issue-07/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-07/README.md` before Plan.

```text
/rpi continue=1 task=Research only for PulseBoard issue #7 (TEMP-9). Do not write production code. Do not plan or implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-9 / GitHub issue #7 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md and Sprint 1/2 evidence only where the issue requires them. Capture what release evidence already exists. Save the research write-up to lifecycle/06-implementation/output/issue-07/research.md
```

---

## Phase 2 — Plan

**Command:** `/rpi` · **`continue=2`**  
**Save to:** `lifecycle/06-implementation/output/issue-07/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-07/README.md` before Implement.

```text
/rpi continue=2 task=Plan documentation work for PulseBoard issue #7 (TEMP-9) only. Do not produce the final checklist yet unless the plan is trivial. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-9 / GitHub issue #7 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Base the plan on lifecycle/06-implementation/output/issue-07/research.md. Prefer lifecycle/08-delivery/output/ or the path stated in the issue. Save the plan to lifecycle/06-implementation/output/issue-07/plan.md
```

---

## Phase 3 — Implement

**Command:** `/rpi` · **`continue=3`**  
**Save to:** `lifecycle/06-implementation/output/issue-07/implement.md` (+ checklist path from the issue/plan)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-07/README.md` before Stage 7/8.

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #7 (TEMP-9) only. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-9 / GitHub issue #7 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Follow lifecycle/06-implementation/output/issue-07/plan.md. Produce only the v0.1.0 release evidence checklist required by the issue. Record RPI/session evidence under .copilot-tracking/ when applicable. Write an implement summary to lifecycle/06-implementation/output/issue-07/implement.md. Do not tag/release unless the issue explicitly requires it and Stage 7 review is done. Do not add product features under the guise of the checklist.
```
