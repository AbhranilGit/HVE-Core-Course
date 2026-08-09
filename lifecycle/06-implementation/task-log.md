# Stage 6 — Task log

One row per task, in sprint plan order. Fill the table in once at the start of
Stage 6, then work down it.

The four phase columns are your gates. Put your initials and the date in a cell
only after you have **opened and read** that phase's file. The point of this page
is to make you pause and look, while a mistake is still one paragraph rather
than three hundred lines of code.

Section 4 of [`README.md`](README.md) explains how to fill in the first five
columns, and can do it for you from the sprint plan.

## Tasks

| # | Issue | Task | Sprint | Slug | Research | Plan | Implement | Review | Closed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

The slug is what ties a task's four evidence files together. Use the same one
every time: `issue-NN-short-title`, for example `issue-01-user-can-log-in`.

## What each gate means

**Research** — the research file exists and is filled in with findings,
constraints, existing patterns, and open questions. No production code was
written. It understood the task correctly. There is enough here to plan against
the acceptance criteria.

**Plan** — the plan, phase details, and plan critique exist. The plan follows the
research, or explains where it deliberately differs. It respects your ADRs. It
stays inside this one task. Reading it, you can picture what will change. You
have read the critique and are satisfied with how its points were dispositioned.

**Implement** — the change record lists what changed and how each acceptance
criterion was addressed. The code actually runs. Nothing was built that this
task did not ask for. Work has not started on the next task.

**Review** — the review log records the exact test command, the result, and the
date. The tests passed, with no test weakened to get a pass. Execution status is
Complete and the outcome is Conformant, or you have read and accepted the stated
divergence. Every acceptance criterion is recorded as passing, with evidence.
Follow-up work was routed rather than quietly fixed.

**Closed** — the issue comment records how each acceptance criterion was met and
the issue is closed.

## Notes and deviations

Anything that did not go to plan, and what you decided about it. One line each.

| Task | What happened | What you decided |
| --- | --- | --- |
| | | |
