# Task #\<NN\> — your checks

> **This is a template.** Step 0 in [`../../prompt/README.md`](../../prompt/README.md) generates one copy per task, in a folder named `issue-NN/`.

| | |
| --- | --- |
| **Task** | `<NN>` — `<title>` |
| **Its prompts** | [`../../prompt/issue-<NN>.md`](../../prompt/issue-<NN>.md) |
| **Its specification** | `lifecycle/04-decomposition/output/backlog-snapshot.md` — section `<backlog id>` |

Check each step **before** starting the next. The point of this page is to make you pause and read what the AI produced, while a mistake is still one paragraph rather than three hundred lines of code.

---

## Step 1 — Research

The file: [`research.md`](research.md)

- [ ] The file exists and is filled in — findings, constraints, existing patterns, open questions
- [ ] No production code was written in this step
- [ ] It understood the task correctly — the description matches what you actually want
- [ ] There is enough here to plan against the acceptance criteria

**Checked by:** _your name_ · **Date:** _YYYY-MM-DD_

## Step 2 — Plan

The file: [`plan.md`](plan.md)

- [ ] The file exists and is filled in — steps, files to touch, acceptance checks, risks
- [ ] The plan follows the research, or explains where it deliberately differs
- [ ] It stays inside this one task
- [ ] It respects the decisions recorded in your ADRs
- [ ] Reading it, you can picture what will change

**Checked by:** _your name_ · **Date:** _YYYY-MM-DD_

## Step 3 — Implement

The files: [`implement.md`](implement.md), plus code under `src/` and `tests/`

- [ ] `implement.md` lists what changed and how each acceptance criterion was checked
- [ ] Every acceptance criterion for this task is met
- [ ] The code actually runs
- [ ] Nothing was built that this task did not ask for
- [ ] Work has not started on the next task

**Checked by:** _your name_ · **Date:** _YYYY-MM-DD_

---

## The gate

- [ ] Research checked → Plan may start
- [ ] Plan checked → Implement may start
- [ ] Implement checked → the next task in [`../../prompt/README.md`](../../prompt/README.md) may start

If a step went wrong, rerun that step's prompt rather than patching the result by hand — otherwise the files stop matching the code, and the review in Stage 7 becomes guesswork.
