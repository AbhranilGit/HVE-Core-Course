# Stage 6 — Implementation

Build it, one task at a time.

| | |
| --- | --- |
| **Reads** | `docs/planning/sprint-plan.md`, the work items, the PRD, and the decision records |
| **Produces** | Code in the customer's tree, evidence under `.copilot-tracking/`, and a closed work item per task |
| **Commands** | `/task-research`, `/task-plan`, `/task-implement`, `/task-review`, then `ADO Backlog Manager` to close the item |

This is the longest stage. Read sections 1 and 2 before you start — they explain the loop you will repeat for every task.

---

## 1. What this stage is for

You now write the code. But not in one giant "build my app" request — that is how AI produces something confident and wrong.

Instead, every task goes through four phases, known collectively as **RPI**. Each phase is its own command, and each one writes a file you read before allowing the next:

| Phase | Command | What happens | Evidence it leaves behind |
| --- | --- | --- | --- |
| **Research** | `/task-research` | The AI investigates and writes down what it found. No code. | `.copilot-tracking/research/<date>/<slug>-research.md` |
| **Plan** | `/task-plan` | It writes a plan, the phase details, and a validated planning log. Still no code. | `.copilot-tracking/plans/<date>/<slug>-plan.instructions.md` |
| **Implement** | `/task-implement` | It follows the plan and writes the actual code. | Code, plus `.copilot-tracking/changes/<date>/<slug>-changes.md` |
| **Review** | `/task-review` | It reconciles the plan against what changed, runs the tests, and records a status. | `.copilot-tracking/reviews/<date>/<slug>-plan-review.md` |

Each command carries its own helper. `/task-research` runs as `Task Researcher`, `/task-plan` as `Task Planner`, `/task-implement` as `Task Implementor`, and `/task-review` as `Task Reviewer`. You do not need to touch the mode dropdown — typing the command switches helper for you.

**You read each file before running the next command.** That is the whole trick. If the research misunderstood something, you catch it in a paragraph rather than in three hundred lines of code.

Once the review passes, one last thing closes the task out: the work item that asked for the work gets the evidence as a comment, and is closed. Without the review record, Stage 8 has no evidence to cite. Without closing the item, the customer's board keeps showing work that has already shipped — and their board, not your memory, is what the sponsor looks at.

You repeat this for every task in your sprint plan, in order. Do not run two tasks at once, and do not skip ahead.

### Why the research phase matters more here

On a greenfield product, research protects you from an AI that invents things confidently. That is still true. But on someone else's codebase it does something more valuable: it forces the model — and you — to learn how *this* system already works before changing it.

Every codebase has local conventions that are invisible until you violate one. An error-handling pattern, a naming scheme, a place where configuration is expected to live, a test helper everyone uses. Code that ignores those is code the customer's engineers will quietly rewrite after you leave, which means you were never really helping.

So read the research output with a specific question in mind: *does this describe their system accurately, or does it describe a generic one?* If it reads like it could have been written about any project, it is not finished.

### Enablement starts here, not in the final sprint

The four-phase loop is the most teachable thing you will do on this engagement. Once you have run it a few times, start running it **with** the engineers named in section 2 of your [engagement brief](../00-engagement/engagement-brief.md) — first watching you, then driving with you reading.

Do not save this for the handover sprint. Someone who has run the loop eight times over six weeks can keep using it; someone shown it once in a final-week session cannot.

## 2. Where the evidence lives

The four commands write to fixed locations under `.copilot-tracking/`. Those paths are HVE Core's own convention, and each phase finds the previous phase's file there.

```text
.copilot-tracking/
├── research/<date>/<slug>-research.md               # /task-research
├── plans/<date>/<slug>-plan.instructions.md         # /task-plan
├── details/<date>/<slug>-details.md                 # /task-plan
├── plans/logs/<date>/<slug>-log.md                  # /task-plan, then /task-implement
├── changes/<date>/<slug>-changes.md                 # /task-implement
└── reviews/<date>/<slug>-plan-review.md             # /task-review
```

`<date>` is today's date, and `<slug>` is a short lowercase name for the task. This kit uses the work item id and a short title: `wi-4821-operator-can-log-in`.

The phases chain together by **file path**, not by name. `/task-plan` takes `research=<path>`, `/task-implement` takes `plan=<path>`, and `/task-review` takes `plan=<path>`. Each command tells you the path it wrote; you paste that path into the next one. Keeping the slug consistent is still worth doing, because it is what makes the folders readable a month later.

Two things follow from all this:

- **`.copilot-tracking/` is ignored by Git by default**, because it is working evidence rather than product documentation. Stages 7 and 8 read it from your machine while you still have it. If your team wants the trail committed, remove the `.copilot-tracking/` lines from `.gitignore`.
- **Do not tidy it up mid-project.** Stage 7 reads it.

The durable, committed record of this stage is the code itself, the closed work items, and the running log in [`task-log.md`](task-log.md).

## 3. Prerequisites

- `docs/planning/sprint-plan.md` exists and lists the tasks in order
- The work items exist in their tracker with acceptance criteria
- `.github/copilot-instructions.md` records the inherited stack, including the real paths to their application code and tests
- The test command in it is one you have run yourself and seen pass
- You can build and run their system locally, or in whatever environment they expect you to work in
- You have a branch naming convention that matches theirs

## 4. Set up your task log (do this once)

Open [`task-log.md`](task-log.md) and copy your sprint plan's task order into the table — one row per task, with the slug you will use. It takes two minutes and it is the page you will come back to after every task.

Keep it in the repository rather than in your own notes. Whoever picks this engagement up after you needs to see which tasks were gated and which were rushed.

You can have a helper fill it in. Use the **default Copilot Chat**, not one of the task helpers:

```text
Read docs/planning/sprint-plan.md from the workspace.

Fill in the task table in lifecycle/06-implementation/task-log.md, one row per
task, in sprint plan order. For each row set the order number, the work item id,
the task title, the iteration, and a slug formed as wi-<id>-<short-title>, where
<short-title> is the title in lowercase with spaces replaced by hyphens,
punctuation removed, under about six words. For example:
wi-4821-operator-can-log-in.

Leave the four phase columns empty — I fill those in as I go.

Do not write any application code and do not start work on any task.
```

## 5. The loop, for each task

Run the four commands below in order, for one task at a time.

**Clear the chat between every phase.** Run `/clear` or start a new chat before each command. Each phase writes what it learned to a file, and the next phase reads that file — so nothing is lost, and the helper works from the evidence rather than from a long, drifting conversation. This is the single habit that keeps the loop honest.

Replace `<NN>`, `<slug>`, and `<id>` with the values from your task log.

### Step 1 — Research

Clear the chat and run `/task-research` — it brings the `Task Researcher` helper with it:

```text
/task-research topic=Task <NN> for work item <id>, slug <slug>

Read from the workspace:
- Work item <id> and its acceptance criteria
- docs/decisions/, for the decisions and inherited constraints in force
- The PRD in docs/prds/, only where this task needs it
- .github/copilot-instructions.md, for where the code and tests actually live
- The existing code in the paths it names

This is an existing codebase that I did not write. Before anything else,
establish how it already does things in the area this task touches:
- The patterns it uses for this kind of change, with file and line references
- How errors, logging, and configuration are handled here
- The test conventions: where tests live, how they are named, what helpers exist
- Anything nearby that looks like a deliberate constraint rather than an accident

Then capture the options and open questions needed to plan this task. Prefer the
approach that matches what is already here over the approach you would pick for
a new codebase, and say so explicitly where the two differ.

Stay inside this one task's scope. Do not write production code. Do not plan or
implement yet.
```

**Then:** open the research file it names, read it, and confirm the Research gate in [`task-log.md`](task-log.md) — in that task’s row, fill the **Research** column (typically your initials + date). That marks “I’ve read the research and it’s good enough to plan from.” You only tick a gate after you’ve opened and read that phase’s file. **Copy the path down** — the next command needs it.

### Step 2 — Plan

Clear the chat and run `/task-plan` — it brings the `Task Planner` helper with it:

```text
/task-plan research=.copilot-tracking/research/<date>/<slug>-research.md

Plan the implementation of task <NN> for work item <id>.

Base the plan on that research document. If it is missing or incomplete, stop
and say so rather than guessing.

Follow the decisions recorded in docs/decisions/, including the inherited
constraints. Take the acceptance criteria from work item <id>.

Match the existing patterns the research identified. Where you deliberately
depart from one, say which, and why it is worth the inconsistency.

Include the steps, the files you will touch, the acceptance checks, and the
risks. Stay inside this task's scope.

Do not implement yet.
```

`Task Planner` runs a `Plan Validator` over its own work and records what that found in a **planning log**, under `.copilot-tracking/plans/logs/`. Read the discrepancy section of that log — it is where the real problems surface, and the planner will have already reworked the plan in response to the serious ones.

**Then:** open the plan (and the planning log’s discrepancy section), read them, and confirm the Plan gate in [`task-log.md`](task-log.md) — fill the **Plan** column with your initials + date. That marks “I’ve read the plan and it’s good enough to implement from.” **Copy the plan path down** — the next command needs it.

### Step 3 — Implement

Clear the chat and run `/task-implement` — it brings the `Task Implementor` helper with it:

```text
/task-implement plan=.copilot-tracking/plans/<date>/<slug>-plan.instructions.md phaseStop=true

Implement the approved plan for task <NN>, work item <id>.

Follow that plan as the sole implementation guide. Use its research for
background only; do not re-plan. If the plan is missing or incomplete, stop and
say so.

The acceptance criteria come from work item <id>. Follow the technical decisions
in docs/decisions/ and the conventions in .github/copilot-instructions.md.

Put changes in the code and test paths recorded in copilot-instructions.md, and
follow the surrounding code's conventions rather than introducing new ones.

Do not reformat, restructure, or tidy code this task does not touch. This is
someone else's repository and unrelated changes make the review harder and the
handover worse.

Do not start any other task in this session. Do not add anything beyond this
task's scope and the accepted PRD.
```

`phaseStop=true` makes it pause after each phase of the plan so you can look at what it did before it carries on. Drop it if you would rather it run straight through, but the pause is the cheapest place to catch a wrong turn.

**Then:** check the code runs, open the change record, read it, and confirm the Implement gate in [`task-log.md`](task-log.md) — fill the **Implement** column with your initials + date. That marks “I’ve checked what changed and it stays inside this task.”

### Step 4 — Review

Clear the chat and run `/task-review` — it brings the `Task Reviewer` helper with it:

```text
/task-review plan=.copilot-tracking/plans/<date>/<slug>-plan.instructions.md

Review task <NN>, work item <id>.

Reconcile the plan, the phase details, the planning log, and the change evidence
against the acceptance criteria in work item <id>.

Run the test command recorded in .github/copilot-instructions.md and the
decision records. If no command is recorded, that is a gap in Stage 3: use the
standard command for the language the records name, say clearly which one you
used, and tell me to record it as a decision.

Record in the review:
- The exact test command you ran, the result, and any failure output verbatim
- One line per acceptance criterion, saying whether it passes, fails, or could
  not be verified, and citing the evidence
- Anything built that this task did not ask for
- Any follow-up work, listed and routed rather than fixed

Do not weaken, skip, or delete a test to make the run pass. Do not implement
fixes in this step. If a test fails or a criterion is unmet, say so plainly and
stop rather than starting another task.
```

`Task Reviewer` finishes with an **overall status** of Complete, Needs Rework, or Blocked, plus a count of critical and major findings. A task is only done when the status is Complete — or when you have read a Needs Rework verdict and consciously accepted what it found.

**Then:** open the review log, read the overall status and acceptance evidence, and confirm the Review gate in [`task-log.md`](task-log.md) — fill the **Review** column with your initials + date. That marks “tests passed (or I consciously accepted Needs Rework) and every acceptance criterion is evidenced.”

### Step 5 — Close the work item

Clear the chat and switch to <mark>**ADO Backlog Manager**</mark> in the mode dropdown, or their tracker's equivalent.

```text
Close work item <id> for task <NN>, now that it is implemented and reviewed.

Read the review log for <slug> under .copilot-tracking/reviews/ and the change
record under .copilot-tracking/changes/.

Before closing, confirm the review records every acceptance criterion in work
item <id> as passing and the test run as passed. If any criterion fails, is
unverified, or the tests did not pass, do not close it: comment what is still
outstanding and tell me.

If it is safe to close:
- Comment with a short summary of what changed, the test command and its result,
  and one line per acceptance criterion saying how it was met
- Close the work item

Write the comment for the customer's engineers, not for me. They will read it
after I have gone, without the conversation I had while building it.

Do not include .copilot-tracking paths in the comment — summarize the evidence
instead. Do not close any other item. Do not edit application code.
```

**Then:** confirm the Closed gate in [`task-log.md`](task-log.md) — fill the **Closed** column with your initials + date. That marks “the work item is closed and the comment records how each acceptance criterion was met.”

**Do not start the next task until the current one's tests have passed and its work item is closed.**

## 6. The gates

- Research read and confirmed → Plan may start
- Plan and planning log read and confirmed → Implement may start
- Code runs and Implement confirmed → Review may start
- Review passed and work item closed → the next task may start

Clear the chat at each of those arrows.

If a step went wrong, rerun that step's command rather than patching the result by hand — otherwise the evidence stops matching the code, and the Stage 7 review becomes guesswork.

## 7. If the helper asks you a question

Answer from the work item, the PRD, or your decision records. If it asks you to attach a file, tell it the path and say "read it from the workspace" — every prompt here already contains the paths it needs.

If it asks something only the customer can answer — what a rule should be, which of two behaviours is correct — stop and ask them. Guessing produces code that passes review and fails the demo.

If it says a file it needs is missing, check the path you passed in. The commands chain by explicit file path, so a typo in `research=` or `plan=` is the usual cause.

## 8. Done when

- Every task in the iteration has research, plan, changes, and review evidence under `.copilot-tracking/`
- Every review recorded a passing test run, with every acceptance criterion met
- Every task's work item is closed with that evidence summarized in the comment
- Every task's four gates are confirmed in [`task-log.md`](task-log.md)
- The code runs, and the thin slice from your sprint plan actually works
- No features appeared that were not in the backlog
- Nothing was reformatted or restructured that the tasks did not require
- At least one of the engineers you are enabling has watched the loop run end to end

**Next:** [Stage 7 — Review](../07-review/README.md)

---

## In a hurry?

`/rpi task="..."` runs all five phases — research, plan, implement, review, and a discovery step that suggests follow-up work — as one coordinated workflow under the `RPI Agent` helper. It is faster and far less gated: you give up the chance to catch a misunderstanding while it is still one paragraph long.

Its `continue` argument is easy to misread. `/rpi continue=2` does **not** mean "run phase 2" — it means "carry on with suggested work item 2" from the discovery step of a previous `/rpi` run. There is no way to ask `/rpi` for a single phase; that is exactly what the four `/task-*` commands are for.

Use `/rpi` for a one-line fix. Use the four separate commands for anything you would be annoyed to have to throw away.
