# Task #\<NN\> — your checks

> **This is a template.** Step 0 in [`../../README.md`](../../README.md) generates one copy per task, saved as `checks.md` inside that task's own folder.

| | |
| --- | --- |
| **Task** | `<NN>` — `<title>` |
| **Its prompts** | [`README.md`](README.md) — the page you paste from |
| **Its specification** | `lifecycle/04-decomposition/output/backlog-snapshot.md` — section `<backlog id>` |

Confirm each step **before** starting the next, and clear the chat between them. The point of this page is to make you pause and read what the AI produced, while a mistake is still one paragraph rather than three hundred lines of code.

---

## Step 1 — Research

The file: [`research.md`](research.md)

Before you start Plan, confirm:

- The file exists and is filled in — findings, constraints, existing patterns, open questions
- No production code was written in this step
- It understood the task correctly — the description matches what you actually want
- There is enough here to plan against the acceptance criteria

**Checked by:** _your name_ · **Date:** _YYYY-MM-DD_

## Step 2 — Plan

The file: [`plan.md`](plan.md)

Before you start Implement, confirm:

- The file exists and is filled in — steps, files to touch, acceptance checks, risks
- The plan follows the research, or explains where it deliberately differs
- It stays inside this one task
- It respects the decisions recorded in your ADRs
- Reading it, you can picture what will change

**Checked by:** _your name_ · **Date:** _YYYY-MM-DD_

## Step 3 — Implement

The files: [`implement.md`](implement.md), plus code under `src/` and `tests/`

Before you review, confirm:

- `implement.md` lists what changed and how each acceptance criterion was checked
- The code actually runs
- Nothing was built that this task did not ask for
- Nothing was written into another task's folder
- Work has not started on the next task

**Checked by:** _your name_ · **Date:** _YYYY-MM-DD_

## Step 4 — Review and close

The files: [`review.md`](review.md), and the closed issue on GitHub

Before you start the next task, confirm:

- `review.md` has a Test run section giving the exact command, the result, and the date
- The tests passed — no failure was left behind, and no test was weakened to get a pass
- Every acceptance criterion is recorded as passing, with the evidence cited
- Any follow-up work was written down rather than quietly fixed during the review
- The issue comment records how each acceptance criterion was met
- The issue is closed, and the item is marked done in the backlog snapshot
- If you are not using GitHub, the backlog snapshot alone is updated

**Checked by:** _your name_ · **Date:** _YYYY-MM-DD_

---

## The gate

- Research confirmed → Plan may start
- Plan confirmed → Implement may start
- Implement confirmed → Review may start
- Review and close confirmed → the next task in [`../../README.md`](../../README.md) may start

Clear the chat at each of those arrows.

If a step went wrong, rerun that step's prompt rather than patching the result by hand — otherwise the files stop matching the code, and the review in Stage 7 becomes guesswork.
