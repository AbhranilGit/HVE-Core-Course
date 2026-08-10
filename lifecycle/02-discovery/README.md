# Stage 2 — Discovery

Turn the statement of work into a business requirements document you can hold people to.

| | |
| --- | --- |
| **Reads** | [`scope-framing.md`](scope-framing.md) and the scope source it points at |
| **Produces** | `docs/brds/<name>-brd.md`, plus any required planning documents |
| **Helper** | `BRD Builder`, then the planners your compliance obligations require |

---

## 1. What this stage is for

You are producing a **BRD** — a short write-up of *why* this engagement exists: the problem, who has it, what success looks like, and what is deliberately not being built.

The difference from a greenfield project is that most of this has already been decided. Somebody sold this work, and the terms are in a statement of work or an Architecture Design Session output. Your job is not to invent the problem statement. It is to make the existing one **precise enough to build against**, and to surface every place where it is not.

That reframing changes what a good outcome looks like here. A BRD that fluently restates the sales deck is a failure. A BRD that says "the statement of work does not define what 'near real time' means, and the three plausible readings imply different architectures" is worth the day it took.

## 2. Prerequisites

- [Stage 0](../00-engagement/README.md) is done and the engagement brief is filled in
- [`scope-framing.md`](scope-framing.md) is filled in, with ambiguities marked rather than resolved
- Section 6 of that file has been through the customer at least once
- Stage 1 is finished and the helpers appear in Copilot Chat

## 3. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`BRD Builder`**.

Do not use `PRD Builder` or the task helpers here. You are not deciding features and you are certainly not writing code.

## 4. Paste this prompt

```text
Create a business requirements document (BRD) for the engagement described in
lifecycle/02-discovery/scope-framing.md.

Read that file and the scope source it points at from the workspace. Also read
lifecycle/00-engagement/engagement-brief.md for the engagement's boundaries and
constraints. Do not ask me to attach any of them.

This scope was contracted, not invented. Work accordingly:
- Treat the scope source as authoritative. Where it is specific, use its terms.
- Do not resolve the items marked ambiguous in the framing. Carry each one
  forward as an open question with the readings it could bear and what each
  would imply for the build.
- Derive assumptions and risks from the framing and the engagement brief. Do not
  invent new scope, and do not quietly widen an in-scope item.
- Where the framing records an inherited constraint, treat it as fixed and note
  what it rules out.

Produce a BRD covering: problem statement, stakeholders, in and out of scope,
success measures, assumptions, inherited constraints, risks, and open questions.

Flag explicitly anything in the scope source that you believe cannot be
delivered within the stated constraints. That is more useful to me than a
document that reads smoothly.

Do not write a PRD, acceptance criteria, decision records, work items, or any
application code.

Save the BRD to your default location under docs/brds/ and tell me the exact
path you used.
```

`BRD Builder` writes to `docs/brds/<name>-brd.md` and keeps its session state in `.copilot-tracking/brd-sessions/<name>.state.json`, which is how it resumes if you come back to it tomorrow. Leave both alone.

## 5. What you should see afterwards

A new file under **`docs/brds/`** ending in `-brd.md`.

Read the open questions and the "cannot be delivered" flags first. Those are the parts you take back to the sponsor, and they are why you did this before writing any code rather than after.

Then read the scope sections against the statement of work, line by line. If the BRD has quietly grown a capability the contract does not mention, fix it now. Everything downstream — the PRD, the work items, the release evidence — inherits this scope, and a widening here becomes unpaid work in week nine.

## 6. Required planning documents

In the course variant of this template these planners are optional. Here they are not. Section 6 of your [engagement brief](../00-engagement/engagement-brief.md) records which obligations apply, and each one that applies turns into a required document at this stage.

| If the brief says | Helper | Command |
| --- | --- | --- |
| The system contains AI, or makes automated decisions about people | `RAI Planner` | `/rai-capture`, then `/rai-plan-from-prd` once Stage 3 exists |
| It handles personal data, credentials, payments, or health records | `Security Planner` | `/security-capture`, then `/security-plan-from-prd` |
| The customer requires supply-chain assurance | `SSSC Planner` | `/sssc-from-brd`, or `/sssc-from-prd` later |

The `-capture` commands work from what you have now. The `-from-prd` variants produce the fuller assessment and need Stage 3's PRD, so run those when you get there — but start the conversation here, because what they surface often changes the PRD.

`/sssc-from-brd` and `/rai-plan-from-security-plan` let these chain off each other rather than starting cold each time. Commit everything they produce.

**If none apply, record that decision rather than leaving it blank.** Add a line to the BRD naming who confirmed it and when. "Nobody raised compliance" and "compliance does not apply" look identical in an empty document, and they are very different positions to be in during a customer security review.

## 7. If the helper asks you a question

Answer from the [scope framing](scope-framing.md) or the scope source it points at. If the answer is in neither, **do not decide it yourself**. Add it to section 6 of the framing as an open question, tell the helper it is unresolved, and put it on the agenda for your next customer conversation.

This is the habit that separates delivery work from personal projects. On your own product, deciding an open question yourself is efficient. On someone else's, it is how you end up having built something nobody agreed to.

## 8. Done when

- A `-brd.md` file exists under `docs/brds/`
- Its scope matches the statement of work, with nothing added
- Every ambiguity from the framing survives as an open question rather than being silently resolved
- Anything undeliverable within the constraints is flagged in writing
- Every required planning document from section 6 exists, or the BRD records who confirmed none were needed
- The open questions have been sent to the customer

**Next:** [Stage 3 — Product definition](../03-product-definition/README.md)

---

## Optional — when a technical unknown blocks the BRD

If you cannot write the BRD because something about the customer's existing system is genuinely unknown, investigate before you guess:

```text
/task-research topic=<the unknown>
```

It writes what it finds to `.copilot-tracking/research/<date>/`. Use it for questions like "how does their current export actually work" — not for questions only the customer can answer.
