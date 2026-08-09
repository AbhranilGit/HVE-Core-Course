# Stage 5 — Sprint planning

Put the tasks in order, and decide what you build first.

| | |
| --- | --- |
| **Reads** | Your backlog, your PRD, and your framing |
| **Produces** | `docs/planning/sprint-plan.md`, and milestones in your tracker |
| **Command** | `/github-sprint-plan`, or the equivalent for your tracker |

---

## 1. What this stage is for

You have a pile of tasks. This stage sorts them into batches:

- **Sprint 1** builds a **thin vertical slice** — the smallest complete path a real person could actually use, end to end. Not every screen half-built, but one thing that genuinely works.
- **Sprint 2** hardens it: tests, documentation, and anything needed to call it a release.

Two sprints is this template's default because it is the smallest number that
separates "make it work" from "make it shippable". Larger products need more — if
yours does, plan more milestones and keep the same rule: the first sprint is
always a thin slice.

Building the thin slice first is the single most useful habit here. It means that
when you run out of time or patience, you have something real rather than a pile
of unfinished parts.

## 2. Prerequisites

- Stage 4 is finished and your backlog exists
- Every item in it has acceptance criteria
- You have created two milestones in your tracker, named `Sprint 1` and `Sprint 2`. The command plans one milestone at a time and needs them to exist

## 3. Plan Sprint 1

`/github-sprint-plan` runs discovery and triage as one sequence: it works out
which issues belong in the milestone, checks the coverage for gaps, then applies
labels and milestone assignments.

```text
/github-sprint-plan milestone=Sprint 1 documents=docs/prds/<name>.md autonomy=partial

Plan Sprint 1 as a thin vertical slice.

Also read from the workspace:
- lifecycle/02-discovery/mvp-framing.md, for the in-scope list
- The open issues in this repository

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
- Any dependencies between items
- A definition of done for the sprint

Assign each of those issues to the Sprint 1 milestone.

Do not write application code. Do not create new issues unless a genuine gap
blocks the thin slice — ask me first if you think one is needed.
```

Its working notes land in `.copilot-tracking/github-issues/sprint/sprint-1/`.

## 4. Plan Sprint 2

Same command, clear the chat first.

```text
/github-sprint-plan milestone=Sprint 2 documents=docs/prds/<name>.md autonomy=partial

Plan Sprint 2: everything left after the Sprint 1 thin slice.

Sprint 2 hardens and packages the product — tests, documentation, and whatever
is needed to call it a release. It does not add new features.

Produce an ordered list with dependencies and a definition of done, and assign
those issues to the Sprint 2 milestone.
```

## 5. Commit the plan

The sprint planning notes live under `.copilot-tracking/`, which is not in Git.
Stages 6, 7, and 8 all read the sprint plan, so it needs a committed copy.

```text
Write the combined plan to docs/planning/sprint-plan.md.

List every item in build order with its issue number, title, and the sprint it
belongs to. Include, for each sprint, the definition of done and any
dependencies between items. For Sprint 1, include the one-sentence description
of what a user will be able to do end to end.

Read your own sprint planning notes under .copilot-tracking/github-issues/sprint/
for the content, but do not cite those paths in the file itself.
```

**You should see:** `docs/planning/sprint-plan.md`, and both milestones populated
in your tracker.

Check the one-sentence description of the Sprint 1 slice. If you cannot imagine a
person using what it describes, the slice is not thin — it is incomplete. Ask for
a rework.

## 6. Optional helpers

| Helper | Use it when |
| --- | --- |
| `Agile Coach` | Your stories or acceptance criteria are vague, and you want them tightened before you order them. Works with any tracker. |
| `Product Manager Advisor` | You want a second opinion on what should come first. |

Neither writes the plan. Run them before section 3 if you want them at all.

## 7. If the helper asks you a question

Answer from the backlog or the PRD. Questions about what matters most to you are
yours to answer — you are the one who knows which part of the idea you most want
to see working.

## 8. Done when

- `docs/planning/sprint-plan.md` exists and lists every item in build order
- Sprint 1 describes something a person could genuinely use
- Both sprints have a definition of done
- Every issue is assigned to a milestone
- Every item comes from the backlog — nothing new appeared

**Next:** [Stage 6 — Implementation](../06-implementation/README.md) — the long
one. Read its first section before you start.
