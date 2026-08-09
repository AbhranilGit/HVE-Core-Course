# Task #\<NN\> — \<title\>

> **This is a template.** You do not fill it in by hand. Step 0 in [`../../README.md`](../../README.md) generates one copy per task — saved as the `README.md` inside that task's own folder — with every `<placeholder>` replaced by that task's real values.

| | |
| --- | --- |
| **Task** | `<NN>` — `<title>` |
| **Its folder** | `lifecycle/06-implementation/output/<folder>/` |
| **Its specification** | [`../../../04-decomposition/output/backlog-snapshot.md`](../../../04-decomposition/output/backlog-snapshot.md) — section `<backlog id>` |
| **Sprint** | `<1 or 2>`, task `<n>` of `<total>` |
| **Depends on** | `<earlier task numbers, or "nothing">` |
| **Your checks** | [`checks.md`](checks.md) |

Everything this one task produces stays in this one folder: the four files the AI writes, plus your checks page. Nothing from another task belongs here.

`<folder>` is this task's folder name — its number followed by a short slug of its title, for example `issue-01-user-can-log-in`.

Finish and confirm each step before starting the next.

**The chain:** Research → `research.md` → Plan → `plan.md` → Implement → `implement.md` and code → Review → `review.md` and a closed issue.

---

## Which helper

1. Open Copilot Chat.
2. Choose **`RPI Agent`** from the mode dropdown.

Steps 1 to 3 use `RPI Agent`. Step 4a switches to **`Task Reviewer`**, and Step 4b to **`GitHub Backlog Manager`** — closing issues is its job rather than the coding helper's. Do not use `BRD Builder` or `PRD Builder` anywhere in this stage.

Each prompt below already contains every path it needs. If the helper asks you to attach a file, tell it to read the path from the workspace.

## Clear the chat between every step

**Before you paste each prompt below, run `/clear` or start a new chat.** This is not optional housekeeping — each step is a separate phase, and a clean context is what lets the helper work from the files rather than from a half-remembered conversation.

Nothing is lost when you clear. Every step writes its findings to a file in this folder, and the next step reads that file. After clearing, it helps to open the previous step's file in your editor so the helper can see it.

---

## Step 1 — Research

**Save to:** `lifecycle/06-implementation/output/<folder>/research.md`
**Before moving on:** read that file, then confirm the Research checks in [`checks.md`](checks.md).

```text
/rpi continue=1 task=Research only for task <NN> (<backlog id>). Do not write production code. Do not plan or implement yet. Read the authoritative scope from lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id> and use that section's acceptance criteria. Read lifecycle/03-product-definition/output/adr/ for locked technical decisions and follow them. Read lifecycle/03-product-definition/output/prd.md only where this task needs it. Capture existing repository patterns, constraints, options, and open questions needed to plan this task. Write the research to lifecycle/06-implementation/output/<folder>/research.md. Do not write to any other task's folder. Do not ask me to attach files; read the paths from the workspace.
```

---

## Step 2 — Plan

**Save to:** `lifecycle/06-implementation/output/<folder>/plan.md`
**Before moving on:** read that file, then confirm the Plan checks in [`checks.md`](checks.md).

```text
/rpi continue=2 task=Plan the implementation of task <NN> (<backlog id>) only. Do not implement yet. REQUIRED: read the completed research at lifecycle/06-implementation/output/<folder>/research.md and base this plan on it. Also read the task scope from lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id>, and follow the decisions in lifecycle/03-product-definition/output/adr/. If lifecycle/06-implementation/output/<folder>/research.md is missing or incomplete, stop and say so rather than guessing. Do not invent findings that contradict the research. Include the steps, the files you will touch, the acceptance checks taken from the backlog section, and the risks. Stay inside this task's scope. Write the plan to lifecycle/06-implementation/output/<folder>/plan.md. Do not write to any other task's folder. Do not ask me to attach files; read the paths from the workspace.
```

---

## Step 3 — Implement

**Save to:** `lifecycle/06-implementation/output/<folder>/implement.md`, plus code under `src/` and `tests/`
**Before moving on:** check the code runs, then confirm the Implement checks in [`checks.md`](checks.md).

```text
/rpi continue=3 task=Implement the approved plan for task <NN> (<backlog id>) only. REQUIRED: read and follow the approved plan at lifecycle/06-implementation/output/<folder>/plan.md as the sole implementation guide. Use lifecycle/06-implementation/output/<folder>/research.md for background only; do not re-plan. If lifecycle/06-implementation/output/<folder>/plan.md is missing or incomplete, stop and say so. The acceptance criteria come from lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id>. Follow the technical decisions recorded in lifecycle/03-product-definition/output/adr/. Put application and test changes under src/ and tests/. Record session evidence under .copilot-tracking/ where applicable. Write a summary of what changed, which acceptance criteria passed, and any deviation from the plan, to lifecycle/06-implementation/output/<folder>/implement.md. Do not write to any other task's folder. Do not start any other task in this session. Do not add anything beyond this task's scope and the accepted PRD. Do not ask me to attach files; read the paths from the workspace.
```

---

## Step 4 — Review and close

Writing the code is not the end. Two things finish a task: a **review** that runs the tests and checks the work against what was asked, and **closing the issue** that asked for it. Skip this and Stage 8 has no evidence to cite, while your board still shows every task open even though the code is written.

Review is the fourth phase of RPI, so it gets its own step rather than being bolted onto the implementation.

### 4a — Review the task and run its tests

**Save to:** `lifecycle/06-implementation/output/<folder>/review.md`
**Before moving on:** the review must record a passing test run, with every acceptance criterion met.

This prompt works differently from steps 1 to 3, so read this before pasting:

1. Clear the chat, then choose **`Task Reviewer`** from the mode dropdown. Staying in `RPI Agent` also works.
2. Type **`/task-review`**. Placeholders appear in the box, looking like `[plan=...] [changes=...] [research=...] [scope=...]`.
3. **Replace those placeholders** with the values in the first line below. Do not leave any `...` in the text.
4. Paste the rest of the prompt after them, and send.

**Why not `/rpi continue=4`?** `RPI Agent` does understand reviewing — its own description covers Research, Plan, Implement, Review, and Discover. The `/rpi` *command* is narrower: its `continue=` only accepts `1`, `2`, `3`, or `all`, and `3` is Implement. So the review gets its own command, `/task-review`, which hands the work to the `Task Reviewer` helper.

```text
/task-review plan=lifecycle/06-implementation/output/<folder>/plan.md changes=lifecycle/06-implementation/output/<folder>/implement.md research=lifecycle/06-implementation/output/<folder>/research.md scope=task <NN> (<backlog id>) only

Review task <NN> (<backlog id>) only, and record the verdict.

Read from the workspace:
- lifecycle/06-implementation/output/<folder>/plan.md
- lifecycle/06-implementation/output/<folder>/implement.md
- lifecycle/06-implementation/output/<folder>/research.md, for background only
- lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id>, for the
  acceptance criteria
- lifecycle/03-product-definition/output/adr/, for the language, tools, and test command
  in force

Run the test command recorded in the ADRs. If no command is recorded there, that is a
gap in Stage 3: use the standard command for the language the ADRs name, say clearly
which one you used, and tell me to record it as an ADR.

Write one review record to lifecycle/06-implementation/output/<folder>/review.md
containing:
- A "Test run" section: the exact command you ran, the result (how many tests passed,
  how many failed, and any failure output verbatim), and the date
- One line per acceptance criterion in section <backlog id>, saying whether it passes,
  fails, or could not be verified, and citing the evidence for that verdict
- Anything that was built which this task did not ask for
- Any follow-up work, listed rather than fixed

Do not weaken, skip, or delete a test to make the run pass. Do not implement fixes in
this step; record what needs doing. If a test fails or a criterion is unmet, say so
plainly and stop rather than starting another task. Do not write to any other task's
folder. Do not ask me to attach files; read the paths from the workspace.
```

### 4b — Close the issue

Clear the chat, then open the mode dropdown and switch to **`github-backlog-manager`**.

```text
Close the GitHub issue for task <NN> (<backlog id>), now that it is implemented and reviewed.

Read from the workspace:
- lifecycle/06-implementation/output/<folder>/review.md, including its Test run section
- lifecycle/06-implementation/output/<folder>/implement.md, for what changed
- lifecycle/04-decomposition/output/backlog-snapshot.md section <backlog id>

Before closing, confirm the review records every acceptance criterion in section
<backlog id> as passing. If any criterion fails, is unverified, or the test run did not
pass, do not close the issue: comment what is still outstanding and tell me.

If it is safe to close:
- Comment on the issue with a short summary of what changed, the test command and its
  result, and one line per acceptance criterion saying how it was met
- Close the issue
- Mark that item as done in lifecycle/04-decomposition/output/backlog-snapshot.md

Do not close any other issue. Do not edit application code. Do not ask me to attach
files; read the paths from the workspace.
```

**Not using GitHub?** If Stage 4 numbered your backlog `TEMP-1`, `TEMP-2` and so on instead of creating issues, skip the closing part and ask it only to mark the item done in `lifecycle/04-decomposition/output/backlog-snapshot.md`. That snapshot is your source of truth.

---

When the Research, Plan, Implement, and Review and close checks all look good, move to the next task in [`../../README.md`](../../README.md).
