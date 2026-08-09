# Stage 7 — Review

Check what you built against what you promised.

| | |
| --- | --- |
| **Reads** | Your sprint plan, your PRD, the Stage 6 evidence under `.copilot-tracking/`, and the code in `src/` |
| **Produces** | Review summaries under `docs/reviews/` |
| **Commands** | `/task-review`, `/code-review-full`, and optionally `/security-review` |

Do part **A**, then **B**, then **C**, and **D** if it applies to you.

---

## 1. What this stage is for

"It runs on my machine" is not the same as "it does what we agreed". This stage
compares the finished work to the acceptance criteria you wrote in Stage 3 and
the definition of done from Stage 5, and writes down the verdict.

Each task was already reviewed on its own in Stage 6. This stage is different: it
asks whether the sprint **as a whole** delivered what was promised, and whether
the codebase that resulted is sound. A pile of individually passing tasks can
still add up to a product that does not work end to end.

Two different questions get asked here:

- An **acceptance review** asks: does it do what was promised?
- A **code review** asks: is the code itself sound — correct, consistent, tested?

Expect to find problems. That is the point. Anything found here gets written down
as a defect or a follow-up rather than quietly fixed and forgotten.

## 2. Prerequisites

- Every Sprint 1 task went through all four phases and its issue is closed
- The Stage 6 evidence is still under `.copilot-tracking/` — do not empty it before this stage. `Task Reviewer` needs the plan and changes logs and will stop without them
- `docs/planning/sprint-plan.md` and your PRD exist
- The code runs, and every task's own review recorded a passing test run

---

## A. Did Sprint 1 deliver what was promised?

Clear the chat first. `/task-review` brings the `Task Reviewer` helper with it, so
you do not need the mode dropdown.

The `scope` argument is **time-based** — "today", "this week", "since last
review". Use whichever window covers your Sprint 1 work.

```text
/task-review scope=since last review

Review Sprint 1 as a whole, not one task.

Read from the workspace:
- docs/planning/sprint-plan.md, the Sprint 1 section
- The PRD in docs/prds/
- lifecycle/06-implementation/task-log.md, for the tasks in Sprint 1
- Every plan, changes log, and review log under .copilot-tracking/ belonging to
  a Sprint 1 task
- src/ and tests/

Take the list of things to validate from the Sprint 1 definition of done and the
PRD acceptance criteria. Do not invent your own criteria.

Also check:
- That the thin vertical slice described in the sprint plan actually works
  end to end
- That nothing was built which lifecycle/02-discovery/mvp-framing.md puts out of
  scope

Say clearly which criteria pass, which fail, and which you could not verify.
Route defects and residual work rather than fixing them here. Do not review
Sprint 2 except to note anything deferred into it.

Then write a committed summary of this review to
docs/reviews/sprint-1-review.md: the overall status, one line per criterion with
its verdict and evidence, and the full list of defects and follow-ups with the
decision still open on each. Keep .copilot-tracking paths out of that file and
describe the evidence instead.
```

**You should see:** a review log under `.copilot-tracking/reviews/<date>/`, and a
committed summary at `docs/reviews/sprint-1-review.md`.

The committed summary matters because `.copilot-tracking/` is not in Git by
default. Stage 8 cites the summary, not the log.

`Task Reviewer` reports an **overall status** of Complete, Needs Rework, or
Blocked, with counts of critical and major findings. When it finishes it offers
you handoff buttons — research the findings further, revise the plan, or
implement fixes straight away. Ignore those for now. Decide what to do with the
findings in section 4 first, and route anything you choose to fix back through
Stage 6 as a proper task.

---

## B. Did Sprint 2 deliver what was promised?

Run this after Sprint 2 is built. Same command, clear the chat first.

```text
/task-review scope=since last review

Review Sprint 2 as a whole, not one task.

Read from the workspace:
- docs/planning/sprint-plan.md, the Sprint 2 section
- The PRD in docs/prds/
- lifecycle/06-implementation/task-log.md, for the tasks in Sprint 2
- Every plan, changes log, and review log under .copilot-tracking/ belonging to
  a Sprint 2 task
- tests/
- docs/reviews/sprint-1-review.md, if it exists
- Any runbook or release checklist that Sprint 2 produced

Take the list of things to validate from the Sprint 2 definition of done. Also
confirm that Sprint 2 hardened and packaged the product rather than adding new
features.

Route defects and residual work rather than fixing them here.

Then write a committed summary to docs/reviews/sprint-2-review.md, in the same
shape as the Sprint 1 summary.
```

**You should see:** `docs/reviews/sprint-2-review.md`

---

## C. Is the code itself sound?

Clear the chat and run:

```text
/code-review-full story=#<issue>
```

`Code Review Full` is an orchestrator. It computes the diff for your current
branch, then runs two reviews over it through subagents — a **functional** one
looking at logic, edge cases, error handling, concurrency, and contracts, and a
**standards** one applying your project's coding conventions. It merges both into
a single report.

The `story` argument is optional. Give it the issue or work item this branch
delivers and the standards review adds an acceptance criteria coverage table.
Leave it out if the branch spans several issues.

It writes its own artifacts to
`.copilot-tracking/reviews/code-reviews/<branch>/`, as `review.md` plus a
`metadata.json` carrying the verdict, the head commit, and the finding counts. It
overwrites those on each run, so only the latest review per branch is kept.

Then commit a summary. In the same chat:

```text
Write the merged findings to docs/reviews/code-review.md, one row per finding
with its severity, location, and recommendation. Add a line at the top recording
the branch, the head commit, and the overall verdict.

Read for context and reflect anything relevant:
- docs/reviews/sprint-1-review.md and docs/reviews/sprint-2-review.md, if they exist
- docs/decisions/, for the technical decisions in force
- .github/copilot-instructions.md, for this project's conventions

Do not implement fixes.
```

**You should see:** `docs/reviews/code-review.md`

Want just one perspective? `/code-review-functional baseBranch=origin/main` runs
the functional half on its own, which is quicker on a small change.

---

## D. Security review (run it if your product touches anything sensitive)

`/code-review-full` does not cover security. That is a separate helper:

```text
/security-review mode=audit
```

`Security Reviewer` profiles your codebase, works out which OWASP skill set
applies, and assesses against it. You can aim it yourself with
`targetSkill=owasp-top-10`, `owasp-llm`, `owasp-agentic`, `owasp-mcp`,
`owasp-infrastructure`, `owasp-cicd`, or `secure-by-design`, and narrow it with
`scope=src/`.

Run this if your product handles credentials, personal data, payments, or
anything an attacker would want. Skip it for a personal habit tracker that stores
one file on your laptop.

> HVE Core is explicit about this and so is this kit: the security helper is an
> **assistive tool only**. It does not replace real security tooling or a
> qualified human reviewer, and its findings need validating before you act on
> them. Treat it as a prompt to think, not as a clearance.

Commit what it found to `docs/reviews/security-review.md` in the same shape as
the code review summary.

---

## 3. If a helper asks you a question

Point it at the sprint plan for the definition of done and the PRD for acceptance
criteria. If it asks whether a defect matters, that is your call — but write the
decision into the review file rather than leaving it in the chat.

## 4. What to do with what it found

Findings are not orders. For each one, decide:

- **Fix now** — go back to [Stage 6](../06-implementation/README.md) and run the four-phase loop on it, as a new task with its own slug
- **Fix later** — leave it recorded in the review as a follow-up
- **Will not fix** — say so in the review, with your reason

Write the decision next to the finding in the review file. Do not fix things ad
hoc in the review chat — it leaves your documents describing something other than
the code you have.

## 5. Done when

- `docs/reviews/sprint-1-review.md` exists and clearly states what passes and what fails
- `docs/reviews/sprint-2-review.md` exists
- `docs/reviews/code-review.md` exists
- `docs/reviews/security-review.md` exists, if part D applied to you
- Every defect has a decision written next to it: fix now, fix later, or will not fix
- Anything you chose to fix now has been through Stage 6 again

**Next:** [Stage 8 — Delivery](../08-delivery/README.md)
