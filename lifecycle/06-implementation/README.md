# Stage 6 — Implementation

Build it, one task at a time.

| | |
| --- | --- |
| **Reads** | `docs/planning/sprint-plan.md`, your issues, your PRD, and your decision records |
| **Produces** | Code in `src/` and `tests/`, evidence under `.copilot-tracking/`, and a closed issue per task |
| **Commands** | `/task-research`, `/task-plan`, `/task-implement`, `/task-review`, then `GitHub Backlog Manager` to close the issue |

This is the longest stage. Read sections 1 and 2 before you start — they explain
the loop you will repeat for every task.

---

## 1. What this stage is for

You now write the code. But not in one giant "build my app" request — that is
how AI produces something confident and wrong.

Instead, every task goes through four phases, known collectively as **RPI**. Each
phase is its own command, and each one writes a file you read before allowing the
next:

| Phase | Command | What happens | Evidence it leaves behind |
| --- | --- | --- | --- |
| **Research** | `/task-research` | The AI investigates and writes down what it found. No code. | `.copilot-tracking/research/<date>/<slug>-research.md` |
| **Plan** | `/task-plan` | It writes a plan, the phase details, and a validated planning log. Still no code. | `.copilot-tracking/plans/<date>/<slug>-plan.instructions.md` |
| **Implement** | `/task-implement` | It follows the plan and writes the actual code. | Code, plus `.copilot-tracking/changes/<date>/<slug>-changes.md` |
| **Review** | `/task-review` | It reconciles the plan against what changed, runs the tests, and records a status. | `.copilot-tracking/reviews/<date>/<slug>-plan-review.md` |

Each command carries its own helper. `/task-research` runs as `Task Researcher`,
`/task-plan` as `Task Planner`, `/task-implement` as `Task Implementor`, and
`/task-review` as `Task Reviewer`. You do not need to touch the mode dropdown —
typing the command switches helper for you.

**You read each file before running the next command.** That is the whole trick.
If the research misunderstood something, you catch it in a paragraph rather than
in three hundred lines of code.

Once the review passes, one last thing closes the task out: the issue that asked
for the work gets the evidence as a comment, and is closed. Without the review
record, Stage 8 has no evidence to cite. Without closing the issue, your board
keeps showing work that has already shipped.

You repeat this for every task in your sprint plan, in order. Do not run two
tasks at once, and do not skip ahead.

## 2. Where the evidence lives

The four commands write to fixed locations under `.copilot-tracking/`. Those
paths are HVE Core's own convention, and each phase finds the previous phase's
file there.

```text
.copilot-tracking/
├── research/<date>/<slug>-research.md               # /task-research
├── plans/<date>/<slug>-plan.instructions.md         # /task-plan
├── details/<date>/<slug>-details.md                 # /task-plan
├── plans/logs/<date>/<slug>-log.md                  # /task-plan, then /task-implement
├── changes/<date>/<slug>-changes.md                 # /task-implement
└── reviews/<date>/<slug>-plan-review.md             # /task-review
```

`<date>` is today's date, and `<slug>` is a short lowercase name for the task.
This kit uses the issue number and a short title: `issue-01-user-can-log-in`.

The phases chain together by **file path**, not by name. `/task-plan` takes
`research=<path>`, `/task-implement` takes `plan=<path>`, and `/task-review`
takes `plan=<path>`. Each command tells you the path it wrote; you paste that
path into the next one. Keeping the slug consistent is still worth doing, because
it is what makes the folders readable a month later.

Two things follow from all this:

- **`.copilot-tracking/` is ignored by Git by default**, because it is working evidence rather than product documentation. Stages 7 and 8 read it from your machine while you still have it. If your team wants the trail committed, remove the `.copilot-tracking/` lines from `.gitignore`.
- **Do not tidy it up mid-project.** Stage 7 reads it.

The durable, committed record of this stage is the code in `src/` and `tests/`,
your closed issues, and the running log in [`task-log.md`](task-log.md).

## 3. Prerequisites

- `docs/planning/sprint-plan.md` exists and lists the tasks in order
- Your issues exist in your tracker with acceptance criteria
- Your decision records say which language and tools you are using
- One of them names the exact command that runs the tests — step 4 runs it after every task
- `.github/copilot-instructions.md` has its Stack table filled in from those records
- You have installed whatever that language needs to run on your machine

## 4. Set up your task log (do this once)

Open [`task-log.md`](task-log.md) and copy your sprint plan's task order into the
table — one row per task, with the slug you will use. It takes two minutes and it
is the page you will come back to after every task.

You can have a helper do it. Use the **default Copilot Chat**, not one of the
task helpers:

```text
Read docs/planning/sprint-plan.md from the workspace.

Fill in the task table in lifecycle/06-implementation/task-log.md, one row per
task, in sprint plan order. For each row set the order number, the issue number,
the task title, the sprint, and a slug formed as issue-NN-<short-title>, where
NN is the issue number zero-padded to two digits and <short-title> is the title
in lowercase with spaces replaced by hyphens, punctuation removed, under about
six words. For example: issue-01-user-can-log-in.

Leave the four phase columns empty — I fill those in as I go.

Do not write any application code and do not start work on any task.
```

## 5. The loop, for each task

Run the four commands below in order, for one task at a time.

**Clear the chat between every phase.** Run `/clear` or start a new chat before
each command. Each phase writes what it learned to a file, and the next phase
reads that file — so nothing is lost, and the helper works from the evidence
rather than from a long, drifting conversation. This is the single habit that
keeps the loop honest.

Replace `<NN>`, `<slug>`, and `<issue>` with the values from your task log.

### Step 1 — Research

```text
/task-research topic=Task <NN> for issue #<issue>, slug <slug>

Read from the workspace:
- Issue #<issue> and its acceptance criteria
- docs/decisions/, for the locked technical decisions, and follow them
- The PRD in docs/prds/, only where this task needs it
- The existing code in src/ and tests/

Capture the existing repository patterns, constraints, options, and open
questions needed to plan this task. Stay inside this one task's scope.

Do not write production code. Do not plan or implement yet.
```

**Then:** open the research file it names, read it, and confirm the Research gate
in [`task-log.md`](task-log.md). **Copy the path down** — the next command needs
it.

### Step 2 — Plan

```text
/task-plan research=.copilot-tracking/research/<date>/<slug>-research.md

Plan the implementation of task <NN> for issue #<issue>.

Base the plan on that research document. If it is missing or incomplete, stop
and say so rather than guessing.

Follow the decisions recorded in docs/decisions/. Take the acceptance criteria
from issue #<issue>.

Include the steps, the files you will touch, the acceptance checks, and the
risks. Stay inside this task's scope.

Do not implement yet.
```

`Task Planner` runs a `Plan Validator` over its own work and records what that
found in a **planning log**, under `.copilot-tracking/plans/logs/`. Read the
discrepancy section of that log — it is where the real problems surface, and the
planner will have already reworked the plan in response to the serious ones.

**Then:** confirm the Plan gate in [`task-log.md`](task-log.md), and copy the
plan path down.

### Step 3 — Implement

```text
/task-implement plan=.copilot-tracking/plans/<date>/<slug>-plan.instructions.md phaseStop=true

Implement the approved plan for task <NN>, issue #<issue>.

Follow that plan as the sole implementation guide. Use its research for
background only; do not re-plan. If the plan is missing or incomplete, stop and
say so.

The acceptance criteria come from issue #<issue>. Follow the technical decisions
in docs/decisions/ and the conventions in .github/copilot-instructions.md.

Put application and test changes under src/ and tests/.

Do not start any other task in this session. Do not add anything beyond this
task's scope and the accepted PRD.
```

`phaseStop=true` makes it pause after each phase of the plan so you can look at
what it did before it carries on. Drop it if you would rather it run straight
through, but the pause is the cheapest place to catch a wrong turn.

**Then:** check the code runs, and confirm the Implement gate in
[`task-log.md`](task-log.md).

### Step 4 — Review

```text
/task-review plan=.copilot-tracking/plans/<date>/<slug>-plan.instructions.md

Review task <NN>, issue #<issue>.

Reconcile the plan, the phase details, the planning log, and the change evidence
against the acceptance criteria in issue #<issue>.

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

`Task Reviewer` finishes with an **overall status** of Complete, Needs Rework, or
Blocked, plus a count of critical and major findings. A task is only done when
the status is Complete — or when you have read a Needs Rework verdict and
consciously accepted what it found.

**Then:** confirm the Review gate in [`task-log.md`](task-log.md).

### Step 5 — Close the issue

Clear the chat and switch to **`GitHub Backlog Manager`** in the mode dropdown.

```text
Close issue #<issue> for task <NN>, now that it is implemented and reviewed.

Read the review log for <slug> under .copilot-tracking/reviews/ and the change
record under .copilot-tracking/changes/.

Before closing, confirm the review records every acceptance criterion in issue
#<issue> as passing and the test run as passed. If any criterion fails, is
unverified, or the tests did not pass, do not close the issue: comment what is
still outstanding and tell me.

If it is safe to close:
- Comment with a short summary of what changed, the test command and its result,
  and one line per acceptance criterion saying how it was met
- Close the issue

Do not include .copilot-tracking paths in the comment — summarize the evidence
instead. Do not close any other issue. Do not edit application code.
```

**Do not start the next task until the current one's tests have passed and its
issue is closed.**

## 6. The gates

- Research read and confirmed → Plan may start
- Plan and planning log read and confirmed → Implement may start
- Code runs and Implement confirmed → Review may start
- Review passed and issue closed → the next task may start

Clear the chat at each of those arrows.

If a step went wrong, rerun that step's command rather than patching the result
by hand — otherwise the evidence stops matching the code, and the Stage 7 review
becomes guesswork.

## 7. If the helper asks you a question

Answer from the issue, the PRD, or your decision records. If it asks you to
attach a file, tell it the path and say "read it from the workspace" — every
prompt here already contains the paths it needs.

If it says a file it needs is missing, check the path you passed in. The commands
chain by explicit file path, so a typo in `research=` or `plan=` is the usual
cause.

## 8. Done when

- Every Sprint 1 task has research, plan, changes, and review evidence under `.copilot-tracking/`
- Every review recorded a passing test run, with every acceptance criterion met
- Every task's issue is closed with that evidence summarized in the comment
- Every task's four gates are confirmed in [`task-log.md`](task-log.md)
- The code runs, and the thin slice from your sprint plan actually works
- The same is true for Sprint 2 tasks
- No features appeared that were not in the backlog

**Next:** [Stage 7 — Review](../07-review/README.md)

---

## In a hurry?

`/rpi task="..."` runs all five phases — research, plan, implement, review, and a
discovery step that suggests follow-up work — as one coordinated workflow under
the `RPI Agent` helper. It is faster and far less gated: you give up the chance
to catch a misunderstanding while it is still one paragraph long.

Its `continue` argument is easy to misread. `/rpi continue=2` does **not** mean
"run phase 2" — it means "carry on with suggested work item 2" from the discovery
step of a previous `/rpi` run. There is no way to ask `/rpi` for a single phase;
that is exactly what the four `/task-*` commands are for.

Use `/rpi` for a one-line fix. Use the four separate commands for anything you
would be annoyed to have to throw away.
