# Stage 6 — Issue #7

| | |
| --- | --- |
| **Issue** | [#7](https://github.com/AbhranilGit/HVE-Core-Course/issues/7) — docs: v0.1.0 release evidence checklist |
| **Local spec** | [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — **TEMP-9** |
| **Sprint order** | 3 of 3 (Sprint 2) |
| **Depends on** | #10 evidence; Sprint 1 P0 |
| **RPI output** | [`../output/issue-07/`](../output/issue-07/) |

Persist and verify **each** phase before the next. Checklist: [`../output/issue-07/README.md`](../output/issue-07/README.md).

**Chain:** Research → [`research.md`](../output/issue-07/research.md) → Plan → [`plan.md`](../output/issue-07/plan.md) → Implement → [`implement.md`](../output/issue-07/implement.md).

---

## Agent

**`RPI Agent`**

Select **RPI Agent** in Copilot Chat. Invoke with **`/rpi`**.  
Syntax: `/rpi task=... continue={1|2|3|all}`  
Use `continue=1` (research), `continue=2` (plan), `continue=3` (implement). Do **not** use `continue=all` while gating phases.

Do **not** use `brd-builder`, `prd-builder`, or `github-backlog-manager` for implementation.

Paths in each prompt are enough — the agent should open those files from the workspace. Do not ask the user to attach documents.

---

## Phase 1 — Research

**Command:** `/rpi` · **`continue=1`**  
**Read:** `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-9** / issue #7)  
**Save to:** `lifecycle/06-implementation/output/issue-07/research.md`  
**Gate:** complete Research checks in `lifecycle/06-implementation/output/issue-07/README.md` before Plan.

```text
/rpi continue=1 task=Research only for PulseBoard issue #7 (TEMP-9). Do not write production code. Do not plan or implement yet. Read authoritative scope from lifecycle/04-decomposition/output/backlog-snapshot.md section TEMP-9 / GitHub issue #7 and use that section's acceptance criteria. Optionally read lifecycle/03-product-definition/output/prd.md and lifecycle/03-product-definition/output/adr/ only where the issue requires them. Capture what release evidence already exists. Capture repo patterns, constraints, options, and open questions needed to plan this issue. Write the research to lifecycle/06-implementation/output/issue-07/research.md. Do not ask the user to attach files; open paths from the workspace.
```

---

## Phase 2 — Plan

**Command:** `/rpi` · **`continue=2`**  
**Read:** `lifecycle/06-implementation/output/issue-07/research.md` (required) and `lifecycle/04-decomposition/output/backlog-snapshot.md` (section **TEMP-9**)  
**Save to:** `lifecycle/06-implementation/output/issue-07/plan.md`  
**Gate:** Research verified; complete Plan checks in `lifecycle/06-implementation/output/issue-07/README.md` before Implement.

```text
/rpi continue=2 task=Plan implementation of PulseBoard issue #7 (TEMP-9) only. Do not implement yet. REQUIRED: read completed research at lifecycle/06-implementation/output/issue-07/research.md and base this plan on it. Also read issue scope from lifecycle/04-decomposition/output/backlog-snapshot.md section TEMP-9 / GitHub issue #7. If lifecycle/06-implementation/output/issue-07/research.md is missing or incomplete, stop and say so. Do not invent findings that contradict lifecycle/06-implementation/output/issue-07/research.md. Prefer lifecycle/08-delivery/output/ or the path stated in the issue. Include steps, files to touch, acceptance checks from the local issue spec, and risks. Stay inside this issue's scope. Write the plan to lifecycle/06-implementation/output/issue-07/plan.md. Do not ask the user to attach files; open paths from the workspace.
```

---

## Phase 3 — Implement

**Command:** `/rpi` · **`continue=3`**  
**Read:** `lifecycle/06-implementation/output/issue-07/plan.md` (required); `lifecycle/06-implementation/output/issue-07/research.md` only for background  
**Save to:** `lifecycle/06-implementation/output/issue-07/implement.md` (+ code under `src/` / `tests/` as applicable)  
**Gate:** Plan verified; complete Implement checks in `lifecycle/06-implementation/output/issue-07/README.md` before the next issue.

```text
/rpi continue=3 task=Implement the approved plan for PulseBoard issue #7 (TEMP-9) only. REQUIRED: read and follow the approved plan at lifecycle/06-implementation/output/issue-07/plan.md as the sole implementation guide. Use lifecycle/06-implementation/output/issue-07/research.md only for background; do not re-plan. If lifecycle/06-implementation/output/issue-07/plan.md is missing or incomplete, stop and say so. Issue AC source: lifecycle/04-decomposition/output/backlog-snapshot.md section TEMP-9 / GitHub issue #7. Produce only the v0.1.0 release evidence checklist required by the issue. Do not add product features under the guise of the checklist. Record RPI/session evidence under .copilot-tracking/ when applicable. Write an implement summary (files changed, AC results, deviations from lifecycle/06-implementation/output/issue-07/plan.md) to lifecycle/06-implementation/output/issue-07/implement.md. Do not tag/release unless issue explicitly requires and Stage 7 is done work in this session. Do not widen MVP beyond the local issue spec and accepted PRD in-scope. Do not ask the user to attach files; open paths from the workspace.
```
