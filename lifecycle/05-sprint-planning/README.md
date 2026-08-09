# Stage 5 — Sprint planning

Put the tasks in order, and decide what you build first.

| | |
| --- | --- |
| **Reads** | Your backlog, your PRD, and your framing |
| **Produces** | `docs/project-planning/sprint-plan.md`, and milestones in your tracker |
| **Helper** | `GitHub Backlog Manager`, or the equivalent for your tracker |

---

## 1. What this stage is for

You have a pile of tasks. This stage sorts them into batches:

- **Sprint 1** builds a **thin vertical slice** — the smallest complete path a real person could actually use, end to end. Not every screen half-built, but one thing that genuinely works.
- **Sprint 2** hardens it: tests, documentation, and anything needed to call it a release.

Two sprints is this template's default because it is the smallest number that
separates "make it work" from "make it shippable". Larger products need more —
if yours does, ask for more and keep the same rule: the first sprint is always a
thin slice.

Building the thin slice first is the single most useful habit here. It means
that when you run out of time or patience, you have something real rather than a
pile of unfinished parts.

## 2. Prerequisites

- Stage 4 is finished and your backlog exists
- Every item in it has acceptance criteria

## 3. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`GitHub Backlog Manager`** — its sprint planning workflow handles this.

Optional: `Agile Coach` can tighten up story wording and acceptance criteria
before you order them, and `Product Manager Advisor` can advise on priority.
Neither writes the plan. Do **not** use `RPI Agent` here.

## 4. Paste this prompt

```text
Using the backlog in this workspace, plan Sprint 1 and Sprint 2.

Read from the workspace:
- The PRD in docs/project-planning/
- lifecycle/02-discovery/mvp-framing.md, for the in-scope list
- The open issues in this repository, and your own notes under
  .copilot-tracking/github-issues/

Do not ask me to attach these files.

Workflow:
- Order work from the existing backlog only. Do not invent new features.
- Only ask me where an item's scope or dependencies are genuinely ambiguous.
- Sprint 1 must be a thin vertical slice: derive it from the framing's in-scope
  list and the PRD, and state in one sentence what a user will be able to do
  end to end when Sprint 1 is finished.
- Push polish, extra tests, and documentation to Sprint 2, unless Sprint 1's
  slice cannot work without them.

Produce:
- An ordered list of items for Sprint 1, with the reason for that order
- An ordered list of items for Sprint 2
- Any dependencies between items
- A definition of done for each sprint

Assign each issue to a milestone in the tracker so the sprints are visible there.

Do not write application code in this step.
Do not create new issues unless a genuine gap blocks the thin slice — ask me
first if you think one is needed.

Also write the plan to docs/project-planning/sprint-plan.md, listing every item
in order with its issue number, title, and the sprint it belongs to. Stages 6,
7, and 8 read that file, so it must be committed rather than left in tracking
notes.
```

## 5. What you should see afterwards

A new file at **`docs/project-planning/sprint-plan.md`**, and milestones in your
tracker.

Check the one-sentence description of the Sprint 1 slice. If you cannot imagine
a person using what it describes, the slice is not thin — it is incomplete. Ask
for a rework.

## 6. If the helper asks you a question

Answer from the backlog or the PRD. Questions about what matters most to you are
yours to answer — you are the one who knows which part of the idea you most want
to see working.

## 7. Done when

- `docs/project-planning/sprint-plan.md` exists and lists every item in build order
- Sprint 1 describes something a person could genuinely use
- Both sprints have a definition of done
- Every item comes from the backlog — nothing new appeared

**Next:** [Stage 6 — Implementation](../06-implementation/README.md) — the long
one. Read its first section before you start.
