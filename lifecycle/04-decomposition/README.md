# Stage 4 — Decomposition

Break the contracted features into work items the customer's tracker can carry.

| | |
| --- | --- |
| **Reads** | Your PRD in `docs/prds/` and your decision records in `docs/decisions/` |
| **Produces** | Work items in the customer's tracker |
| **Commands** | `/ado-discover-work-items`, then `/ado-update-wit-items` |

---

## 1. What this stage is for

A feature like "operators can reconcile a batch" is too big to build in one go.
This stage chops the PRD into **work items** small enough to finish in a sitting,
each carrying the id of the PRD acceptance criterion it came from.

That thread from criterion to work item to commit is what lets Stage 7 ask "did
we deliver what was contracted?" and get an answer that survives scrutiny. On a
personal project it is good hygiene. On an engagement it is how you get paid.

The work happens in two steps, and the gap between them is the point. The helper
first **proposes** a backlog into planning files. You read them, and so does the
customer's product owner. Only then does a second command write anything to
their tracker.

Resist the temptation to collapse those steps. Creating eighty work items in
someone else's Azure DevOps project without showing them first is a memorable way
to start an engagement badly.

## 2. This page assumes Azure DevOps

Most enterprise customers run Azure DevOps, so that is the worked example. The
shape is identical elsewhere; only the command names change.

| Their tracker | Helper | Discover | Apply |
| --- | --- | --- | --- |
| **Azure DevOps** | `ADO Backlog Manager` | `/ado-discover-work-items` | `/ado-update-wit-items` |
| **GitHub Issues** | `GitHub Backlog Manager` | `/github-discover-issues` | `/github-execute-backlog` |
| **Jira** | `Jira Backlog Manager` | `/jira-discover-issues` | `/jira-execute-backlog` |

Use whatever they already use. Introducing a second tracker for the duration of
an engagement guarantees that half the history is lost at handover.

## 3. Prerequisites

- Your PRD exists under `docs/prds/`, with acceptance criteria that have ids
- Your decision records exist under `docs/decisions/`
- **The Azure DevOps MCP server is connected and authenticated against their organisation.** Everything here runs through it
- You know the project name, and the area path you are allowed to write to
- The product owner knows this is coming and has agreed to review the proposal

## 4. Propose the backlog

```text
/ado-discover-work-items project=<their-project> documents=docs/prds/<name>.md

Propose the work item hierarchy for this engagement.

Also read from the workspace:
- docs/decisions/, for decisions and inherited constraints already recorded
- lifecycle/02-discovery/scope-framing.md, section 3, for the contracted scope
- .github/ISSUE_TEMPLATE/task.md, for the shape each item should take

Do not ask me to attach these files.

Workflow:
- Derive items from the PRD's user stories and acceptance criteria only.
- Check what already exists in the project before proposing anything new. This
  is an existing backlog, not an empty one, and duplicates are expensive.
- Only ask me where the PRD or the decision records are silent or ambiguous.
- Do not propose anything outside the contracted scope, however sensible it
  looks. Note it as a suggestion for the customer instead.
- Keep each item small enough to finish in one working session.
- Prefer an order that builds one thin end-to-end path first.

Each proposed item must have:
- A clear title
- Acceptance criteria citing the PRD acceptance criterion ids they come from
- A type and an area path consistent with what the project already uses

Do not create or modify anything in Azure DevOps yet, and do not write code.
Do not assign iterations — that is the next stage.
```

**You should see:** a tracking folder at
`.copilot-tracking/workitems/discovery/<scope>/` containing `issue-analysis.md`
with the coverage assessment, `issues-plan.md` with the proposed items, a
planning log, and `handoff.md`. The helper tells you the paths.

If your PRD has a deep hierarchy of epics and features, the helper may route this
through the `AzDO PRD to WIT` agent and write to
`.copilot-tracking/workitems/prds/<name>/` instead. Same idea, same review step.

## 5. Review it, and have the customer review it

Open `issues-plan.md` and read it properly. Then send it to the product owner
before you apply anything.

Two checks of your own first. Every item should trace to a PRD criterion id — an
item that traces to nothing is scope you invented. And the count should feel
plausible: five to fifteen per sprint's worth of work is normal, so eighty items
for a six-week engagement means they are too granular, and six means they are too
coarse to track.

The customer's check is different from yours and more important: they are looking
for the thing they assumed was included that is not on the list. Better to find
it here than in the final demo.

## 6. Apply the approved plan

```text
/ado-update-wit-items

Create the work items from the approved plan at
.copilot-tracking/workitems/discovery/<scope>/handoff.md.

Create only what is in that plan. Do not add, and do not modify existing items
that the plan does not mention.

When you are done, list every item you created with its id, title, and type, so
I can check the set against the PRD.
```

Where a command offers `autonomy`, use `partial` on a customer tenant so it stops
at review gates. `dryRun=true` shows you what it would do without writing
anything, which is worth one run the first time you do this on their project.

**You should see:** work items in their tracker, and an execution record under
`.copilot-tracking/workitems/execution/<date>/`.

Leave them open. Stage 6 closes each one as its task is built and reviewed, with
the evidence in the comment.

### No tracker access yet?

If access is still pending — and in Stage 1 you noted that it often is — do not
let it block you. Use the default Copilot Chat:

```text
Read the PRD in docs/prds/ and docs/decisions/ from the workspace.

Write the full backlog to docs/planning/backlog.md, numbering each item TASK-01,
TASK-02 and so on, each with its title, acceptance criteria citing the PRD
acceptance criterion ids, its type, and its dependencies. Keep each item small
enough to finish in one working session, and order them so one thin end-to-end
path is built first.

Do not invent anything outside the contracted scope. Do not write code.
```

Wherever a later stage says "the work item", read "the entry in
`docs/planning/backlog.md`". Migrate it into their tracker as soon as access
lands, because a backlog that lives only in a markdown file will not survive your
departure.

## 7. If the helper asks you a question

Answer from the PRD. Questions about item types, area paths, or how their
hierarchy is organised go to the technical contact — every organisation's Azure
DevOps has local conventions, and matching theirs matters more than matching
anyone's best practice.

## 8. Done when

- Every item exists in their tracker, or in `docs/planning/backlog.md` pending access
- Every item has acceptance criteria, not just a title
- Each criterion cites the PRD id it came from
- Nothing appeared that the contracted scope does not cover
- The product owner has seen the list and agreed it matches what they expect
- Each item looks finishable in a day or less

**Next:** [Stage 5 — Sprint planning](../05-sprint-planning/README.md)
