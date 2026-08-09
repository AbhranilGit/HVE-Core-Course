# Stage 7 — Review

Check what you built against what was contracted, and produce evidence someone
else can audit.

| | |
| --- | --- |
| **Reads** | The sprint plan, the PRD, the Stage 6 evidence under `.copilot-tracking/`, and the code |
| **Produces** | Review summaries under `docs/reviews/` |
| **Commands** | `/task-review`, `/code-review-full`, and `/security-review` where required |

Do part **A** at the end of every iteration, then **B**, then **C** and **D**
where your obligations require them.

---

## 1. What this stage is for

"It runs on my machine" is not the same as "it does what we contracted for".
This stage compares the finished work to the PRD's acceptance criteria and the
iteration's definition of done, and writes down the verdict.

Each task was already reviewed on its own in Stage 6. This stage asks whether the
iteration **as a whole** delivered what was promised, and whether the codebase
that resulted is sound. A pile of individually passing tasks can still add up to
something that does not work end to end.

On an engagement there is a second audience for all of this. The review files are
not just your quality gate — they are the evidence the customer's own governance
process will ask for, and the record that shows what state you left the system
in. Write them for someone who was not in the room.

Three questions get asked here:

- An **acceptance review** asks: does it do what was contracted?
- A **code review** asks: is the code sound, and does it fit this codebase?
- A **security review** asks: what did we introduce that an attacker would want?

Expect to find problems. That is the point. Anything found gets written down as a
defect with a decision beside it rather than quietly fixed and forgotten — and
"will not fix" is a legitimate decision, provided it is recorded and the customer
has seen it.

## 2. Prerequisites

- Every task in the iteration went through all four phases and its work item is closed
- The Stage 6 evidence is still under `.copilot-tracking/` — do not empty it before this stage. `Task Reviewer` needs the plan and changes logs and will stop without them
- `docs/planning/sprint-plan.md` and the PRD exist
- The code runs, and every task's own review recorded a passing test run

---

## A. Did the iteration deliver what was promised?

Run this at the end of **every** iteration, not just the last one. An engagement
that reviews once at the end discovers its problems when there is no time left to
fix them.

Clear the chat first. `/task-review` brings the `Task Reviewer` helper with it,
so you do not need the mode dropdown. The `scope` argument is **time-based** —
"today", "this week", "since last review".

```text
/task-review scope=since last review

Review iteration <name> as a whole, not one task.

Read from the workspace:
- docs/planning/sprint-plan.md, the section for this iteration
- The PRD in docs/prds/
- lifecycle/06-implementation/task-log.md, for the tasks in this iteration
- Every plan, changes log, and review log under .copilot-tracking/ belonging to
  a task in this iteration
- The code and test paths named in .github/copilot-instructions.md

Take the list of things to validate from this iteration's definition of done and
the PRD acceptance criteria. Do not invent your own criteria.

Also check:
- That what the sprint plan said would be demonstrated actually works end to end
- That nothing was built which lifecycle/02-discovery/scope-framing.md puts out
  of scope
- That no unrelated parts of the codebase were reformatted or restructured

Say clearly which criteria pass, which fail, and which you could not verify.
Route defects and residual work rather than fixing them here.

Then write a committed summary to docs/reviews/<iteration>-review.md: the overall
status, one line per criterion with its verdict and evidence, and the full list
of defects and follow-ups with the decision still open on each. Keep
.copilot-tracking paths out of that file and describe the evidence instead.
```

**You should see:** a review log under `.copilot-tracking/reviews/<date>/`, and a
committed summary at `docs/reviews/<iteration>-review.md`.

The committed summary matters because `.copilot-tracking/` is not in Git. Stage 8
cites the summary, not the log, and the customer keeps the summary after you go.

`Task Reviewer` reports an **overall status** of Complete, Needs Rework, or
Blocked, with counts of critical and major findings. When it finishes it offers
handoff buttons — research the findings, revise the plan, implement fixes. Ignore
those for now. Decide what to do with the findings in section 4 first, and route
anything you choose to fix back through Stage 6 as a proper task.

### Then run the demo

The review tells you what passes. The demo tells you whether the customer agrees,
and those are different things more often than you would expect.

Demonstrate against the review file, criterion by criterion, rather than showing
a happy path. Record what the sponsor and product owner said at the bottom of the
review, including anything they expected that was not there. A criterion you
believe passes and they believe does not is the single most valuable finding you
can get, and it only surfaces if you demo honestly.

---

## B. Is the code sound, and does it fit?

Clear the chat and run:

```text
/code-review-full story=<work-item-id>
```

`Code Review Full` is an orchestrator. It computes the diff for your current
branch, then runs two reviews over it through subagents — a **functional** one
looking at logic, edge cases, error handling, concurrency, and contracts, and a
**standards** one applying the project's coding conventions. It merges both into
a single report.

The `story` argument is optional. Give it the work item this branch delivers and
the standards review adds an acceptance criteria coverage table. Leave it out if
the branch spans several items.

It writes to `.copilot-tracking/reviews/code-reviews/<branch>/`, as `review.md`
plus a `metadata.json` carrying the verdict, the head commit, and finding counts.
It overwrites those on each run, so only the latest review per branch survives.

The standards half only works as well as the conventions you gave it. If
`.github/copilot-instructions.md` does not describe how this codebase actually
writes things, you will get generic advice that the customer's engineers will
reject in review. Go and fix the instructions file rather than arguing with the
output.

Then commit a summary. In the same chat:

```text
Write the merged findings to docs/reviews/code-review.md, one row per finding
with its severity, location, and recommendation. Add a line at the top recording
the branch, the head commit, and the overall verdict.

Read for context and reflect anything relevant:
- The iteration reviews under docs/reviews/
- docs/decisions/, for the decisions and inherited constraints in force
- .github/copilot-instructions.md, for this project's conventions

Separate findings about code I wrote from findings about pre-existing code my
changes touched. Those need different decisions and different conversations.

Do not implement fixes.
```

**You should see:** `docs/reviews/code-review.md`

That separation in the last instruction saves an argument. Findings in code you
did not write are the customer's to prioritise, not yours to silently fix — and a
pull request that quietly repairs unrelated legacy code is a pull request nobody
wants to review.

`/code-review-functional baseBranch=origin/main` runs the functional half alone,
which is quicker on a small change.

---

## C. Security review

**Not optional here.** If section 6 of your
[engagement brief](../00-engagement/engagement-brief.md) says the system handles
personal data, credentials, payments, health records, or anything a customer
security team would care about, this runs — and `/code-review-full` does not
cover it.

```text
/security-review mode=audit
```

`Security Reviewer` profiles the codebase, works out which OWASP skill set
applies, and assesses against it. Aim it yourself with `targetSkill=owasp-top-10`,
`owasp-llm`, `owasp-agentic`, `owasp-mcp`, `owasp-infrastructure`, `owasp-cicd`,
or `secure-by-design`, and narrow it with `scope=<their code path>`.

Where Stage 2 produced a threat model from `Security Planner`, review against it
explicitly rather than in the abstract — ask whether each mitigation the model
assumed is actually present in the code.

> HVE Core is explicit about this and so is this kit: the security helper is an
> **assistive tool only**. It does not replace real security tooling or a
> qualified human reviewer, and its findings need validating before you act on
> them. Treat it as a prompt to think, not as a clearance.
>
> That caveat matters more on an engagement than anywhere else. Do not let
> `docs/reviews/security-review.md` be read by a customer as a sign-off. Write a
> line at the top of the file saying exactly what it is and what it is not, and
> route anything real through their actual security process.

Commit what it found to `docs/reviews/security-review.md` in the same shape as
the code review summary.

---

## D. Responsible AI review

If the brief says the system contains AI or makes automated decisions about
people, review against the assessment `RAI Planner` produced in Stage 2. Clear
the chat, pick **`RAI Planner`** from the dropdown, and ask it to check the built
system against its own assessment — which mitigations landed, which did not, and
what changed since.

HVE Core has no dedicated RAI reviewer, so you are using a planning helper to
look backwards. It works, but be more sceptical of the output than you would be
with `Task Reviewer`, and check the mitigations yourself in the code.

Commit the result to `docs/reviews/rai-review.md`. Customers subject to AI
governance will ask for this, and reconstructing it after handover is much harder
than producing it now.

---

## 3. If a helper asks you a question

Point it at the sprint plan for the definition of done and the PRD for acceptance
criteria. If it asks whether a defect matters, that is your call — but write the
decision into the review file rather than leaving it in the chat.

## 4. What to do with what it found

Findings are not orders. For each one, decide:

- **Fix now** — go back to [Stage 6](../06-implementation/README.md) and run the four-phase loop on it, as a new task with its own slug
- **Fix later** — leave it recorded as a follow-up, and make sure it reaches their backlog rather than dying in a markdown file when you leave
- **Will not fix** — say so, with your reason

Write the decision next to the finding. Do not fix things ad hoc in the review
chat — it leaves your documents describing something other than the code you have.

Two decisions need the customer rather than you: anything you are deferring past
your last day, and anything in the "will not fix" column. Those become their
problem the moment you leave, so they get a say now. Raise them at the demo and
record the date.

## 5. Done when

- Every iteration has a review file under `docs/reviews/` stating what passes and what fails
- `docs/reviews/code-review.md` exists, with findings in your code separated from findings in theirs
- `docs/reviews/security-review.md` exists where the brief requires it, with its limits stated plainly
- `docs/reviews/rai-review.md` exists where the brief requires it
- Every defect has a decision written beside it
- Deferred and will-not-fix items have been through the customer, with the date recorded
- Anything you chose to fix now has been through Stage 6 again
- Each iteration was demonstrated, and what the customer said is recorded

**Next:** [Stage 8 — Delivery](../08-delivery/README.md)
