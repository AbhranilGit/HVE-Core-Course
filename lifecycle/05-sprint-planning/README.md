# Stage 5 — Sprint planning

Put the tasks in order, and decide what you build first.

| | |
| --- | --- |
| **Reads** | [`../04-decomposition/output/backlog-snapshot.md`](../04-decomposition/output/backlog-snapshot.md) |
| **Produces** | [`output/sprint-plan.md`](output/sprint-plan.md) |
| **Helper** | `github-backlog-manager` |

---

## 1. What this stage is for

You have a pile of tasks. This stage sorts them into two batches:

- **Sprint 1** builds a **thin vertical slice** — the smallest complete path a real person could actually use, end to end. Not every screen half-built, but one thing that genuinely works.
- **Sprint 2** hardens it: tests, documentation, and anything needed to call it a release.

Building the thin slice first is the single most useful habit here. It means that when you run out of time or patience, you have something real rather than a pile of unfinished parts.

## 2. Prerequisites

- `lifecycle/04-decomposition/output/backlog-snapshot.md` exists
- Every item in it has acceptance criteria

## 3. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`github-backlog-manager`**.

Optional: `product-manager-advisor` can advise on priorities, but it does not write the plan. Do **not** use `RPI Agent` here.

## 4. Paste this prompt

```text
Using the backlog in this workspace, propose Sprint 1 and Sprint 2.

Read from the workspace:
- lifecycle/04-decomposition/output/backlog-snapshot.md
- lifecycle/03-product-definition/output/prd.md
- lifecycle/02-discovery/input/mvp-framing.md (for the in-scope list)
- The open GitHub issues in this repository, if you can reach them

Do not ask me to attach these files.

Workflow:
- Order work from the existing backlog only. Do not invent new features.
- Only ask me where an item's scope or dependencies are genuinely ambiguous.
- Sprint 1 must be a thin vertical slice: derive it from the framing's in-scope
  list and the PRD, and state in one sentence what a user will be able to do
  end to end when Sprint 1 is finished.
- Push polish, extra tests, and documentation to Sprint 2, unless Sprint 1's
  slice cannot work without them.

Return:
- An ordered list of items for Sprint 1, with the reason for that order
- An ordered list of items for Sprint 2
- Any dependencies between items
- A definition of done for each sprint

Do not write application code in this step.
Do not create new issues unless a genuine gap blocks the thin slice — ask me
first if you think one is needed.

Save the sprint plan to:
lifecycle/05-sprint-planning/output/sprint-plan.md
```

## 5. What you should see afterwards

A new file at **`lifecycle/05-sprint-planning/output/sprint-plan.md`**.

Check the one-sentence description of the Sprint 1 slice. If you cannot imagine a person using what it describes, the slice is not thin — it is incomplete. Ask for a rework.

## 6. If the helper asks you a question

Answer from the backlog snapshot or the PRD. Questions about what matters most to you are yours to answer — you are the one who knows which part of the idea you most want to see working.

## 7. Done when

- `lifecycle/05-sprint-planning/output/sprint-plan.md` exists
- Sprint 1 describes something a person could genuinely use
- Both sprints have a definition of done
- Every item comes from the backlog — nothing new appeared

**Next:** [Stage 6 — Implementation](../06-implementation/README.md) — the long one. Read its first section before you start.
