# Planning

| File | Written by | Stage |
| --- | --- | --- |
| `sprint-plan.md` | The tracker's backlog helper, via `/ado-sprint-plan` or its equivalent | [Stage 5 — Sprint planning](../../lifecycle/05-sprint-planning/README.md) |
| `backlog.md` | Default Copilot Chat, only if tracker access has not landed yet | [Stage 4 — Decomposition](../../lifecycle/04-decomposition/README.md) |

Unlike `docs/brds/`, `docs/prds/`, and `docs/decisions/`, this folder is **not** an HVE Core default. HVE Core keeps its sprint planning notes under `.copilot-tracking/workitems/sprint/`, which is working evidence and is not committed. This template asks for a committed copy as well, because Stages 6, 7, and 8 all read the sprint plan — and because it has to survive both a fresh clone and your departure.

That is why the Stage 5 prompt ends by asking for the plan to be written here explicitly. The helper will not do it on its own.

## What makes this plan different

It is planned backwards from a last day you did not choose, so it carries two things a normal sprint plan does not:

- **A final iteration reserved for handover**, not features. The most commonly broken rule in delivery work, and the one whose breakage is invisible until it is too late to fix.
- **An explicit list of what is not being delivered.** Produced in week two rather than week ten, which turns an awkward conversation into a planned one.

Record at the top of `sprint-plan.md` the date the sponsor and product owner agreed it, and any change they asked for. When scope is disputed later, a dated agreement is worth more than a recollection.

`backlog.md` exists only as a stopgap. Migrate it into the customer's tracker as soon as access lands — a backlog that lives in a markdown file will not survive the engagement.

Empty until you run Stage 4.
