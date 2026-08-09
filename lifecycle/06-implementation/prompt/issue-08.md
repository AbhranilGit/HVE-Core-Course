# Stage 6 — Issue #8

| | |
| --- | --- |
| **Issue** | [#8](https://github.com/AbhranilGit/HVE-Core-Course/issues/8) — docs: local-first runbook and start path |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-8** |
| **Sprint order** | 2 of 3 (Sprint 2) |
| **Depends on** | Runnable Sprint 1; #10 when present |
| **RPI output** | [`../output/issue-08/`](../output/issue-08/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-08/README.md`](../output/issue-08/README.md).

---

## Agent

**`RPI Agent`**

Select **RPI Agent** in Copilot Chat. Invoke with **`/rpi`**.  
Syntax: `/rpi task=... continue={1|2|3|all}`  
Use `continue=1` (research), `continue=2` (plan), `continue=3` (implement). Do **not** use `continue=all` while gating phases.

Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for this step.

Before each phase: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-8** / issue #8).

---

## Phase 1 — Research

**Command:** `/rpi` · **`continue=1`**  
**Save to:** `lifecycle/06-implementation/output/issue-08/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-08/README.md` before Plan.

```text
/rpi continue=1 task=Research only for PulseBoard issue #8 (TEMP-8). Do not write production code. Do not plan or implement yet. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-8 / GitHub issue #8 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Optional: lifecycle/03-product-definition/output/prd.md only where the issue requires them. Capture how the app actually starts and where data lives. Save the research write-up to lifecycle/06-implementation/output/issue-08/research.md
```

---

## Phase 2 — Plan

**Command:** `/rpi` · **`continue=2`**  
**Save to:** `lifecycle/06-implementation/output/issue-08/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-08/README.md` before Implement.

```text
/rpi continue=2 task=Plan documentation work for PulseBoard issue #8 (TEMP-8) only. Do not write the final runbook yet unless the plan is trivial. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-8 / GitHub issue #8 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Base the plan on lifecycle/06-implementation/output/issue-08/research.md. Prefer lifecycle/09-operations/output/runbook.md if that matches the issue; otherwise follow the issue's stated path. Save the plan to lifecycle/06-implementation/output/issue-08/plan.md
```

---

## Phase 3 — Implement

**Command:** `/rpi` · **`continue=3`**  
**Save to:** `lifecycle/06-implementation/output/issue-08/implement.md` (+ runbook path from the issue/plan)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-08/README.md` before the next issue.

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #8 (TEMP-8) only. Authoritative scope (in-repo): lifecycle/04-decomposition/output/backlog-snapshot.md — section TEMP-8 / GitHub issue #8 (attach / #reference the backlog snapshot; use that section's acceptance criteria). Follow lifecycle/06-implementation/output/issue-08/plan.md. Write only the local-first runbook / start path docs required by the issue. Record RPI/session evidence under .copilot-tracking/ when applicable. Write an implement summary to lifecycle/06-implementation/output/issue-08/implement.md. Do not start issue #7 work in this session. Do not add product features under the guise of docs.
```
