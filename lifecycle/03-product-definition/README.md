# Stage 3 — Product definition

Decide what you are building, and lock in the big technical choices.

| | |
| --- | --- |
| **Reads** | Your BRD under `docs/brds/` |
| **Produces** | `docs/prds/<name>.md` and decision records under `docs/decisions/` |
| **Helpers** | `PRD Builder`, then `ADR Creation` |

This stage has two parts. Do **A** first, then **B**.

---

## 1. What this stage is for

**Part A** produces a **PRD** — a product requirements document. Where the BRD
said *why*, the PRD says *what*: a list of features written as user stories, each
with acceptance criteria — the rules that decide when that feature is genuinely
finished.

**Part B** produces **decision records**, usually called ADRs. Each is a one-page
note capturing a technical decision, why you made it, and what it costs you. This
is where your programming language, your data storage, and anything else
structural gets decided and written down. Decide these once, here, rather than
re-arguing them every time you open the chat.

---

## Part A — Features (the PRD)

## 2. Prerequisites

- Your BRD exists under `docs/brds/` and you have read it
- You know its exact filename — the Stage 2 helper told you
- You are happy with its scope; if not, fix the framing and redo Stage 2 first

## 3. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`PRD Builder`**.

Do **not** use `BRD Builder` or any of the task helpers for this part.

## 4. Paste this prompt

```text
Create a Product Requirements Document (PRD) for the first version of the
product defined in the BRD under docs/brds/.

Read from the workspace:
- The BRD in docs/brds/ (the file ending in -brd.md)
- lifecycle/02-discovery/scope-framing.md, for the contracted scope boundaries
- lifecycle/00-engagement/engagement-brief.md, for the engagement's constraints

Do not ask me to attach either file.

Workflow:
- Use the accepted BRD to answer product-definition questions yourself.
- Only ask me where the BRD is silent or genuinely ambiguous.
- Stay inside the BRD's in-scope list; treat everything out of scope as excluded.
- Carry forward open questions that need a product decision; do not invent new
  features.

Produce a PRD with user stories and clear, checkable acceptance criteria for
every in-scope capability. Give each acceptance criterion a stable id so later
stages can refer to it.

Do not write decision records, issues, sprint plans, or application code in this
step.

Save the PRD to your default location under docs/prds/ and tell me the exact
path you used.
```

## 5. What you should see afterwards

A new file under **`docs/prds/`**, named after your product — "mobile expense
tracking app" becomes `mobile-expense-tracking-app.md`. The helper tells you the
exact path, and keeps its session state in
`.copilot-tracking/prd-sessions/<name>.state.json`.

Read the acceptance criteria closely — this is the moment to catch a
misunderstanding. Everything from here on is measured against them.

---

## Part B — Technical decisions (the ADRs)

## 6. Pick the helper

1. In Copilot Chat, open the mode dropdown again.
2. Choose **`ADR Creation`**.

Run this after the PRD exists.

`ADR Creation` is a coach rather than a form-filler. It works through four
phases — Discovery, Research, Analysis, and Documentation — and it does it by
asking you questions rather than presenting a template. Expect to be asked what
the real decision is, what constraints you are under, and what would have to be
true for an option you rejected to win. Answering those questions is the work;
the file is the by-product.

**Early on it will ask where the finished record should go. Answer
`docs/decisions/`.** That is the location this kit uses and the one the helper
recommends. While you are still talking it keeps a draft under
`.copilot-tracking/adrs/<topic>-draft.md` and moves it into place at the end.

## 7. Paste this prompt

```text
Create decision records (ADRs) for the first version of this product.

Read from the workspace:
- The BRD in docs/brds/ and the PRD in docs/prds/
- lifecycle/02-discovery/scope-framing.md, section 4, for inherited constraints
- lifecycle/00-engagement/engagement-brief.md, section 5, for what already exists
- .github/copilot-instructions.md, for the stack already recorded

Place the finished records in docs/decisions/.

Most of this system's technology is already chosen — it was chosen before I
arrived. Treat that as two different jobs:

- For anything inherited, write a record that captures the constraint, who
  imposed it, and what it rules out. Do not re-open it or present alternatives
  as though it were still open. A future reader needs to know the decision was
  inherited rather than made here.
- For anything genuinely open, decide it properly with alternatives and
  consequences.

One of these decisions must cover testing, even if the customer already has a
test suite. Record the framework, the exact command that runs the whole suite,
and — this is the part that matters on inherited codebases — what the current
suite does and does not actually cover. Stage 6 runs that command after every
task and Stage 8 cites its result. If Stage 1 found the suite failing or absent,
record what you are doing about it here rather than leaving it as folklore.

For each decision record: context, the decision, the alternatives considered,
the consequences, and when it would be worth revisiting.

Do not expand product scope. Do not write application code or tickets.

Tell me the exact path of each record you finalize.
```

Because it works one decision at a time, expect to run this conversation more
than once — once per decision, or once for a related cluster of them.

## 8. What you should see afterwards

One file per decision under **`docs/decisions/`**, named
`YYYY-MM-DD-descriptive-topic-v01.md` — for example
`2026-03-14-sqlite-for-local-storage-v01.md`.

You should now be able to answer "what language is this written in, where does
the data live, and what command runs the tests?" by pointing at a file. If the
test command is missing, ask for it now — Stage 6 needs it after every task.

## 9. Copy the decisions into your project guidance

This step takes a minute and saves you from repeating yourself for the rest of
the project.

Open [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md)
and fill in the **Stack** table from your new decision records: language and
version, framework, data storage, and the install, run, and test commands.

Every helper reads that file on every request. Once it is filled in, Stage 6
writes code in your stack without being reminded.

While you are there, add your language's throwaway files to `.gitignore` —
`__pycache__/` for Python, `target/` for Rust, and so on.

---

## 10. If a helper asks you a question

Technical questions are yours to answer — this stage is exactly where those
decisions belong, and the customer is paying for that judgement. Questions you
have no strong view on are fine to hand back: reply "you decide, and record why
in the decision record."

**Product questions are not yours.** If the helper asks what a feature should do
and neither the BRD nor the [scope framing](../02-discovery/scope-framing.md)
answers it, add it to section 6 of the framing and ask the customer. The line
between "how we build it" and "what we build" is the line between your call and
theirs.

## 11. Done when

- A PRD exists under `docs/prds/`
- Every feature in it has acceptance criteria you could actually check, each with an id
- At least one decision record exists under `docs/decisions/`
- Your language and data storage choices are written down
- One record names your test framework and the exact command that runs the tests
- `.github/copilot-instructions.md` has the Stack table filled in
- Nothing appeared that was out of scope in the BRD

**Next:** [Stage 4 — Decomposition](../04-decomposition/README.md)

---

## Optional — extras for bigger or riskier products

| Helper | Use it when |
| --- | --- |
| `Arch Diagram Builder` | Your product has several moving parts and a picture would help. It builds ASCII-art architecture diagrams you can paste into a decision record. |
| `System Architecture Reviewer` | You want a second opinion on the shape of the system before you commit to it. |
| `Product Manager Advisor` | You want a second opinion on requirement quality or priority before locking the PRD. |
| `UX UI Designer` | Your product has a user interface worth thinking about before it gets built. |
| `Security Planner`, `RAI Planner`, `SSSC Planner` | You ran one in Stage 2 and want its findings reflected as requirements. |
