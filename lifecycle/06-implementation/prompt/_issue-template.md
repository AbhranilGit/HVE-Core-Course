# Task #\<NN\> — \<title\>

> **This is a template.** You do not fill it in by hand. Step 0 in [README.md](README.md) generates one copy of this file per task, with the placeholders replaced. If you would rather do it manually, copy this file to `issue-NN.md` and replace every `<placeholder>`.

| | |
| --- | --- |
| **Task** | `<NN>` — `<title>` |
| **Its specification** | [`../../04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) — section `<backlog id>` |
| **Sprint** | `<1 or 2>`, task `<n>` of `<total>` |
| **Depends on** | `<earlier task numbers, or "nothing">` |
| **Notes folder** | [`../output/issue-<NN>/`](../output/issue-<NN>/) |

Finish and check each step before starting the next. Your gate checklist: [`../output/issue-<NN>/README.md`](../output/issue-<NN>/README.md).

**The chain:** Research → `research.md` → Plan → `plan.md` → Implement → `implement.md` and code.

---

## Which helper

1. Open Copilot Chat.
2. Choose **`RPI Agent`** from the mode dropdown.

Do not use `brd-builder`, `prd-builder`, or `github-backlog-manager` for building code.

Each prompt below already contains every path it needs. If the helper asks you to attach a file, tell it to read the path from the workspace.

---

## Step 1 — Research

**Save to:** `lifecycle/06-implementation/output/issue-<NN>/research.md`
**Before moving on:** read that file, then tick the Research boxes in [`../output/issue-<NN>/README.md`](../output/issue-<NN>/README.md).

```text
/rpi continue=1 task=Research only for task <NN> (<backlog id>). Do not write production code. Do not plan or implement yet. Read the authoritative scope from lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id> and use that section's acceptance criteria. Read lifecycle/03-product-definition/output/adr/ for locked technical decisions and follow them. Read lifecycle/03-product-definition/output/prd.md only where this task needs it. Capture existing repository patterns, constraints, options, and open questions needed to plan this task. Write the research to lifecycle/06-implementation/output/issue-<NN>/research.md. Do not ask me to attach files; read the paths from the workspace.
```

---

## Step 2 — Plan

**Save to:** `lifecycle/06-implementation/output/issue-<NN>/plan.md`
**Before moving on:** read that file, then tick the Plan boxes in the gate checklist.

```text
/rpi continue=2 task=Plan the implementation of task <NN> (<backlog id>) only. Do not implement yet. REQUIRED: read the completed research at lifecycle/06-implementation/output/issue-<NN>/research.md and base this plan on it. Also read the task scope from lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id>, and follow the decisions in lifecycle/03-product-definition/output/adr/. If lifecycle/06-implementation/output/issue-<NN>/research.md is missing or incomplete, stop and say so rather than guessing. Do not invent findings that contradict the research. Include the steps, the files you will touch, the acceptance checks taken from the backlog section, and the risks. Stay inside this task's scope. Write the plan to lifecycle/06-implementation/output/issue-<NN>/plan.md. Do not ask me to attach files; read the paths from the workspace.
```

---

## Step 3 — Implement

**Save to:** `lifecycle/06-implementation/output/issue-<NN>/implement.md`, plus code under `src/` and `tests/`
**Before moving on:** check the code runs, then tick the Implement boxes in the gate checklist.

```text
/rpi continue=3 task=Implement the approved plan for task <NN> (<backlog id>) only. REQUIRED: read and follow the approved plan at lifecycle/06-implementation/output/issue-<NN>/plan.md as the sole implementation guide. Use lifecycle/06-implementation/output/issue-<NN>/research.md for background only; do not re-plan. If lifecycle/06-implementation/output/issue-<NN>/plan.md is missing or incomplete, stop and say so. The acceptance criteria come from lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id>. Follow the technical decisions recorded in lifecycle/03-product-definition/output/adr/. Put application and test changes under src/ and tests/. Record session evidence under .copilot-tracking/ where applicable. Write a summary of what changed, which acceptance criteria passed, and any deviation from the plan, to lifecycle/06-implementation/output/issue-<NN>/implement.md. Do not start any other task in this session. Do not add anything beyond this task's scope and the accepted PRD. Do not ask me to attach files; read the paths from the workspace.
```

---

When the gate checklist is fully ticked, move to the next task in [README.md](README.md).
