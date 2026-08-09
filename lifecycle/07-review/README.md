# Stage 7 — Review

Check what you built against what you promised.

| | |
| --- | --- |
| **Reads** | Your sprint plan, your PRD, the Stage 6 evidence under `.copilot-tracking/`, and the code in `src/` |
| **Produces** | Review verdicts under `docs/reviews/` |
| **Helpers** | `RPI Agent` with `/rpi-review`, then the `Code Review` agent |

Do part **A**, then **B**, then **C**.

---

## 1. What this stage is for

"It runs on my machine" is not the same as "it does what we agreed". This stage
compares the finished work to the acceptance criteria you wrote in Stage 3 and
the definition of done from Stage 5, and writes down the verdict.

Each task was already reviewed on its own in Stage 6. This stage is different:
it asks whether the sprint **as a whole** delivered what was promised, and
whether the codebase that resulted is sound. A pile of individually passing
tasks can still add up to a product that does not work end to end.

Two different checks happen here:

- An **acceptance review** asks: does it do what was promised?
- A **code review** asks: is the code itself sound — correct, safe, tested?

Expect to find problems. That is the point. Anything found here gets written
down as a defect or a follow-up rather than quietly fixed and forgotten.

## 2. Prerequisites

- Every Sprint 1 task went through all four RPI phases and its issue is closed
- The Stage 6 evidence is still under `.copilot-tracking/` — do not empty it before this stage
- `docs/project-planning/sprint-plan.md` and your PRD exist
- The code runs, and every task's own review recorded a passing test run

---

## A. Did Sprint 1 deliver what was promised?

Select **`RPI Agent`** from the mode dropdown. Clear the chat first.

```text
/rpi-review Review Sprint 1 as a whole, using the slug sprint-1.

Read from the workspace:
- docs/project-planning/sprint-plan.md, the Sprint 1 section
- The PRD in docs/project-planning/
- lifecycle/06-implementation/task-log.md, for the tasks in Sprint 1
- The plan, changes, and review evidence under .copilot-tracking/ for every
  Sprint 1 task slug
- src/ and tests/

Take the list of things to validate from the Sprint 1 definition of done and the
PRD acceptance criteria. Do not invent your own criteria.

Also check:
- That the thin vertical slice described in the sprint plan actually works
  end to end
- That nothing was built which lifecycle/02-discovery/mvp-framing.md puts out of
  scope

Keep execution status separate from outcome. Say clearly which criteria pass,
which fail, and which you could not verify. Route defects and residual work
rather than fixing them here. Do not review Sprint 2 except to note anything
deferred into it.

Then write a committed summary of this review to
docs/reviews/sprint-1-review.md: the outcome, one line per criterion with its
verdict and evidence, and the full list of defects and follow-ups with the
decision still open on each. Keep .copilot-tracking paths out of that file and
describe the evidence instead.
```

**You should see:** a review log under `.copilot-tracking/reviews/logs/`, and a
committed summary at `docs/reviews/sprint-1-review.md`.

The committed summary matters because `.copilot-tracking/` is not in Git by
default. Stage 8 cites the summary.

---

## B. Did Sprint 2 deliver what was promised?

Run this after Sprint 2 is built. Same helper, same command, clear the chat
first.

```text
/rpi-review Review Sprint 2 as a whole, using the slug sprint-2.

Read from the workspace:
- docs/project-planning/sprint-plan.md, the Sprint 2 section
- The PRD in docs/project-planning/
- lifecycle/06-implementation/task-log.md, for the tasks in Sprint 2
- The plan, changes, and review evidence under .copilot-tracking/ for every
  Sprint 2 task slug
- tests/
- docs/reviews/sprint-1-review.md, if it exists
- Any runbook or release checklist that Sprint 2 produced

Take the list of things to validate from the Sprint 2 definition of done. Also
confirm that Sprint 2 hardened and packaged the product rather than adding new
features.

Keep execution status separate from outcome. Route defects and residual work
rather than fixing them here.

Then write a committed summary to docs/reviews/sprint-2-review.md, in the same
shape as the Sprint 1 summary.
```

**You should see:** `docs/reviews/sprint-2-review.md`

---

## C. Is the code itself sound?

1. Clear the chat and choose **`Code Review`** from the mode dropdown.
2. It is a human-gated orchestrator: it will confirm the scope, ask which
   perspectives to run, and ask how deep to go before it starts. Answer those
   questions — that is the intended flow, not an obstacle.

For a first release, ask for the **functional**, **security**, and **standards**
perspectives. Add **accessibility** if your product has a user interface.

```text
Review this codebase for first-release readiness, after Sprint 1 and Sprint 2.

Scope: all of src/ and tests/ on the current branch.
Perspectives: functional, security, and standards. Add accessibility if this
product has a user interface.

Read for context:
- docs/reviews/sprint-1-review.md and docs/reviews/sprint-2-review.md, if they exist
- docs/project-planning/sprint-plan.md
- docs/planning/adrs/, for the technical decisions in force
- .github/copilot-instructions.md, for this project's conventions

Focus on:
- Whether the main paths actually do what they claim
- Correct use of the language and framework recorded in the ADRs
- Security problems, especially around user input, stored data, and how users
  are identified
- Test gaps that would make it dishonest to call this done
- Whether the documentation matches how the code really behaves

Do not implement fixes unless I ask. Report findings with a severity for each.

Then write the merged findings to docs/reviews/code-review.md, one row per
finding with its severity, location, and recommendation.
```

**You should see:** `docs/reviews/code-review.md`

If your extension version does not list `Code Review`, use the default Copilot
Chat with the same prompt. You lose the multi-perspective dispatch but the
review still happens.

---

## 3. If a helper asks you a question

Point it at the sprint plan for the definition of done and the PRD for
acceptance criteria. If it asks whether a defect matters, that is your call —
but write the decision into the review file rather than leaving it in the chat.

## 4. What to do with what it found

Findings are not orders. For each one, decide:

- **Fix now** — go back to [Stage 6](../06-implementation/README.md) and run the RPI loop on it, as a new task with its own slug
- **Fix later** — leave it recorded in the review as a follow-up
- **Will not fix** — say so in the review, with your reason

Write the decision next to the finding in the review file. Do not fix things ad
hoc in the review chat — it leaves your documents describing something other
than the code you have.

## 5. Done when

- `docs/reviews/sprint-1-review.md` exists and clearly states what passes and what fails
- `docs/reviews/sprint-2-review.md` exists
- `docs/reviews/code-review.md` exists
- Every defect has a decision written next to it: fix now, fix later, or will not fix
- Anything you chose to fix now has been through Stage 6 again

**Next:** [Stage 8 — Delivery](../08-delivery/README.md)
