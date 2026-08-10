# Stage 5 — Sprint planning

Order the work against a fixed last day.

| | |
| --- | --- |
| **Reads** | The backlog, the PRD, the scope framing, and the engagement brief |
| **Produces** | `docs/planning/sprint-plan.md`, and iterations in the customer's tracker |
| **Command** | `/ado-sprint-plan`, or the equivalent for their tracker |

---

## 1. What this stage is for

You have a backlog and a deadline you did not choose. This stage reconciles them.

The difference from planning your own product is the direction you plan in. On a personal project you order the work and see how long it takes. Here the last day is fixed by a contract, so you plan backwards from it and find out what fits. The question is not "what should we build first" but **"what is the most valuable thing that can be genuinely finished before I leave"**.

Two rules follow, and they matter more than any sequencing technique.

**Sprint 1 is always a thin vertical slice.** The smallest complete path a real user could exercise, touching every layer. Not the foundations, not the data model, not "the platform work". A thin slice means that when something goes wrong in week five — and something will — you have something real rather than scaffolding.

**The last sprint is reserved for handover.** Not features. Documentation, enablement, the runbook, and the sessions where the customer's engineers drive while you watch. Teams that skip this find themselves writing the runbook on their final afternoon, and the quality shows.

That reservation is the single most commonly broken rule in delivery work, and breaking it is how an engagement produces working software that nobody can maintain.

## 2. Prerequisites

- Stage 4 is finished and the backlog exists
- Every item has acceptance criteria
- Section 3 of the [engagement brief](../00-engagement/engagement-brief.md) gives you the last day, the sprint length, and the demo cadence
- The iterations exist in their tracker, named as their project names them

## 3. Work out how many sprints you actually have

Before running anything, do this arithmetic honestly:

| | |
| --- | --- |
| Sprints between now and the last day | `<count>` |
| Minus the final handover sprint | `<count - 1>` |
| Your real allocation | `<full time, or the days per week from the brief>` |
| **Sprints available for building** | `<the number that matters>` |

Most engagements have fewer building sprints than people assume. Discovering that now is uncomfortable; discovering it in week eight is a conversation with the sponsor about what will not be delivered.

If the arithmetic says the contracted scope does not fit, that is a finding, not a failure. Raise it this week, while there is still time to cut something deliberately rather than run out of time accidentally.

## 4. Plan the first iteration

Clear the chat. `/ado-sprint-plan` brings the `ADO Backlog Manager` helper with it (or pick that helper from the mode dropdown). For GitHub or Jira, use their sprint-plan equivalent under the same Backlog Manager family.

```text
/ado-sprint-plan project=<their-project> iteration=<their-iteration-path> documents=docs/prds/<name>.md autonomy=partial

Plan the first iteration as a thin vertical slice.

Also read from the workspace:
- lifecycle/00-engagement/engagement-brief.md, for the window and the exit criteria
- lifecycle/02-discovery/scope-framing.md, section 3, for contracted scope
- The existing open work items in this project

Workflow:
- Order work from the existing backlog only. Do not invent new items.
- The first iteration must be a thin vertical slice: state in one sentence what
  a real user will be able to do end to end when it closes, and make sure that
  sentence would mean something to the sponsor at the demo.
- Push hardening, extra tests, and documentation later, unless the slice cannot
  work without them.
- Flag any item whose dependencies cannot be satisfied within this iteration.

Produce:
- An ordered list of items with the reason for that order
- Dependencies between items
- A definition of done for the iteration
- What will be demonstrated at the end of it

Assign those items to the iteration.

Do not write application code. Do not create new items unless a genuine gap
blocks the slice — ask me first.
```

Working notes land in `.copilot-tracking/workitems/sprint/<iteration-kebab>/`.

## 5. Plan the remaining iterations

Repeat for each building iteration, clearing the chat between them and staying on `ADO Backlog Manager` via `/ado-sprint-plan`. For the last one, plan handover rather than features:

```text
/ado-sprint-plan project=<their-project> iteration=<final-iteration-path> autonomy=partial

Plan the final iteration as handover, not feature work.

Read lifecycle/00-engagement/engagement-brief.md, sections 2 and 4, for the
engineers being enabled and the exit criteria.

This iteration exists to satisfy the exit criteria. Include:
- The runbook and any documentation the exit criteria require
- Enablement sessions with the named engineers, as tracked items with their own
  acceptance criteria
- Time for the customer's engineers to ship a change themselves, with me
  reviewing rather than driving
- Any residual defects from earlier reviews that were accepted as must-fix

Do not schedule new features here. If the backlog still contains unstarted
feature work at this point, list it separately as what will not be delivered,
so I can take that to the sponsor.
```

That last instruction is the useful one. An explicit list of what is not getting built, produced in week two rather than week ten, is what turns an awkward conversation into a planned one.

## 6. Commit the plan

The tracker's planning notes live under `.copilot-tracking/`, which is not committed. Stages 6, 7, and 8 all read the sprint plan, and so will whoever picks this up after you.

Use the **default Copilot Chat** (not `ADO Backlog Manager`) and paste:

```text
Write the combined plan to docs/planning/sprint-plan.md.

List every item in build order with its work item id, title, and iteration.
For each iteration include the definition of done, what gets demonstrated, and
the dependencies. For the first, include the one-sentence description of what a
user will be able to do end to end. For the last, show how each item maps to an
exit criterion from the engagement brief.

Add a section listing anything in the backlog that is not scheduled, and mark it
clearly as not planned for delivery in this engagement.

Read your own planning notes under .copilot-tracking/workitems/sprint/ for the
content, but do not cite those paths in the file.
```

**You should see:** `docs/planning/sprint-plan.md`, and populated iterations in their tracker.

## 7. Take it to the customer

The sprint plan is a commitment, so it needs the product owner and sponsor to see it. Walk them through three things specifically: what the first demo will show, which exit criterion each handover item satisfies, and the unscheduled list.

Record the date they agreed and any changes they asked for at the top of `sprint-plan.md`. When scope is disputed in week nine, a dated agreement is worth more than a recollection.

## 8. Optional helpers

| Helper | Use it when |
| --- | --- |
| `Agile Coach` | The customer's stories or acceptance criteria are vague and you want them tightened before ordering. Works with any tracker |
| `Product Manager Advisor` | You and the product owner disagree about priority and you want a structured second opinion |

Neither writes the plan.

## 9. Done when

- `docs/planning/sprint-plan.md` exists and lists every item in build order
- The first iteration describes something a user could genuinely exercise
- The final iteration is handover work, mapped to the exit criteria
- Every iteration has a definition of done and a demo
- Unscheduled backlog items are listed explicitly as not being delivered
- The sponsor and product owner have seen it, and the date is recorded

**Next:** [Stage 6 — Implementation](../06-implementation/README.md) — the long one. Read its first section before you start.
