# Stage 7 — Review

Check what you built against what you promised.

| | |
| --- | --- |
| **Reads** | Your sprint plan, your PRD, the notes under [`../../06-implementation/output/`](../../06-implementation/output/), and the code in `src/` |
| **Produces** | Review files under [`../output/`](../output/) |
| **Helpers** | `RPI Agent` with `/task-review`, then `code-review` |

Do part **A**, then **B**, then **C**.

---

## 1. What this stage is for

"It runs on my machine" is not the same as "it does what we agreed". This stage compares the finished work to the acceptance criteria you wrote in Stage 3 and the definition of done from Stage 5, and writes down the verdict.

Two different checks happen here:

- An **acceptance review** asks: does it do what was promised?
- A **code review** asks: is the code itself sound — correct, safe, tested?

Expect to find problems. That is the point. Anything found here gets written down as a defect or a follow-up rather than quietly fixed and forgotten.

## 2. Before you start

- [ ] Every Sprint 1 task has `implement.md` in its folder under `../../06-implementation/output/`
- [ ] The code runs
- [ ] `lifecycle/05-sprint-planning/output/sprint-plan.md` and `lifecycle/03-product-definition/output/prd.md` exist

---

## How to run `/task-review`

This one works a little differently from the other prompts, so read this before pasting.

1. Open Copilot Chat and choose **`RPI Agent`** from the mode dropdown (or **Task Reviewer**, if your version lists it).
2. Type **`/task-review`**. Placeholders appear in the box, looking like `[plan=...] [changes=...] [research=...] [scope=...]`.
3. **Replace those placeholders** with the values from the prompt below. Do not leave any `...` in the text.
4. Paste the rest of the prompt after them, and send.

You do not need `/rpi-review`.

---

## A. Did Sprint 1 deliver what was promised?

```text
/task-review plan=lifecycle/05-sprint-planning/output/sprint-plan.md changes=.copilot-tracking/changes/ research=.copilot-tracking/research/ scope=Sprint 1 only, as listed in lifecycle/05-sprint-planning/output/sprint-plan.md

Review Sprint 1 against the Sprint 1 definition of done in the sprint plan and the
acceptance criteria in the PRD.

Read from the workspace:
- lifecycle/05-sprint-planning/output/sprint-plan.md (Sprint 1 section)
- lifecycle/03-product-definition/output/prd.md
- lifecycle/04-decomposition/output/backlog-snapshot.md
- lifecycle/06-implementation/output/ (every task folder belonging to Sprint 1)
- src/ and tests/

Take the list of things to validate from the Sprint 1 definition of done and the
PRD acceptance criteria. Do not invent your own criteria.

Also check:
- That the thin vertical slice described in the sprint plan actually works
  end to end
- That nothing was built which the framing in
  lifecycle/02-discovery/input/mvp-framing.md puts out of scope

Workflow:
- Compare the implementation evidence to each criterion, one by one.
- Say clearly which criteria pass, which fail, and which you could not verify.
- Keep "the work was done" separate from "the work is acceptable".
- List defects and follow-ups. Do not rewrite features; record what needs doing.
- Do not review Sprint 2 work except to note anything deferred into it.

Save the review to:
lifecycle/07-review/output/sprint-1-rpi-review.md
```

**You should see:** `lifecycle/07-review/output/sprint-1-rpi-review.md`

---

## B. Did Sprint 2 deliver what was promised?

Run this after Sprint 2 is built. Same helper, same `/task-review` steps.

```text
/task-review plan=lifecycle/05-sprint-planning/output/sprint-plan.md changes=.copilot-tracking/changes/ research=.copilot-tracking/research/ scope=Sprint 2 only, as listed in lifecycle/05-sprint-planning/output/sprint-plan.md

Review Sprint 2 against the Sprint 2 definition of done in the sprint plan and any
related PRD acceptance criteria.

Read from the workspace:
- lifecycle/05-sprint-planning/output/sprint-plan.md (Sprint 2 section)
- lifecycle/03-product-definition/output/prd.md
- lifecycle/04-decomposition/output/backlog-snapshot.md
- lifecycle/06-implementation/output/ (every task folder belonging to Sprint 2)
- tests/
- lifecycle/07-review/output/sprint-1-rpi-review.md, if it exists
- Any runbook or release checklist that Sprint 2 produced

Take the list of things to validate from the Sprint 2 definition of done. Also
confirm that Sprint 2 hardened and packaged the product rather than adding new
features.

Workflow:
- Compare the evidence to each criterion, one by one.
- Keep "the work was done" separate from "the work is acceptable".
- List defects and follow-ups; do not rewrite features.

Save the review to:
lifecycle/07-review/output/sprint-2-rpi-review.md
```

**You should see:** `lifecycle/07-review/output/sprint-2-rpi-review.md`

---

## C. Is the code itself sound?

1. Open the mode dropdown and choose **`code-review`**.
2. If your version does not list it, use the default Copilot Chat with the same prompt.

```text
Review this codebase for first-release readiness, after Sprint 1 and Sprint 2.

Read from the workspace:
- src/ and tests/
- lifecycle/07-review/output/sprint-1-rpi-review.md, if it exists
- lifecycle/07-review/output/sprint-2-rpi-review.md, if it exists
- lifecycle/05-sprint-planning/output/sprint-plan.md
- lifecycle/03-product-definition/output/adr/ for the technical decisions in force

Focus on:
- Whether the main paths actually do what they claim
- Correct use of the language and framework recorded in the ADRs
- Obvious security problems, especially around user input, stored data, and
  how users are identified
- Test gaps that would make it dishonest to call this done
- Whether the documentation matches how the code really behaves

Do not implement fixes unless I ask. Report findings with a severity for each.

Save the review notes to:
lifecycle/07-review/output/code-review.md
```

**You should see:** `lifecycle/07-review/output/code-review.md`

---

## 3. If a helper asks you a question

Point it at the sprint plan for the definition of done and the PRD for acceptance criteria. If it asks whether a defect matters, that is your call — but write the decision into the review file rather than leaving it in the chat.

## 4. What to do with what it found

Findings are not orders. For each one, decide:

- **Fix now** — go back to [Stage 6](../../06-implementation/prompt/README.md) and run the RPI loop on it
- **Fix later** — leave it recorded in the review as a follow-up
- **Will not fix** — say so in the review, with your reason

Do not fix things ad hoc in the review chat. It leaves your files describing something other than the code you have.

## 5. Done when

- [ ] `sprint-1-rpi-review.md` exists, and clearly states what passes and what fails
- [ ] `sprint-2-rpi-review.md` exists
- [ ] `code-review.md` exists
- [ ] Every defect has a decision: fix now, fix later, or will not fix
- [ ] Anything you chose to fix now has been through Stage 6 again

Tick Stage 7 in [CHECKLIST.md](../../CHECKLIST.md).

**Next:** [Stage 8 — Delivery](../../08-delivery/prompt/README.md)
