# Stage 3 — Product definition

Decide what you are building, and lock in the big technical choices.

| | |
| --- | --- |
| **Reads** | [`../02-discovery/output/brd.md`](../02-discovery/output/brd.md) |
| **Produces** | [`output/prd.md`](output/prd.md) and files under [`output/adr/`](output/adr/) |
| **Helpers** | `prd-builder`, then `adr-creation` |

This stage has two parts. Do **A** first, then **B**.

---

## 1. What this stage is for

**Part A** produces a **PRD** — a product requirements document. Where the BRD said *why*, the PRD says *what*: a list of features written as user stories, each with acceptance criteria — the rules that decide when that feature is genuinely finished.

**Part B** produces **ADRs** — architecture decision records. Each is a one-page note capturing a technical decision, why you made it, and what it costs you. This is where your programming language, your data storage, and anything else structural gets decided and written down. Decide these once, here, rather than re-arguing them every time you open the chat.

---

## Part A — Features (the PRD)

## 2. Prerequisites

- `lifecycle/02-discovery/output/brd.md` exists and you have read it
- You are happy with its scope — if not, fix the framing and redo Stage 2 first

## 3. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`prd-builder`**.

Do **not** use `RPI Agent` or `brd-builder` for this part.

## 4. Paste this prompt

```text
Create a Product Requirements Document (PRD) for the first version of the product
defined in lifecycle/02-discovery/output/brd.md.

Read that file from the workspace, and read
lifecycle/02-discovery/input/mvp-framing.md for the original scope boundaries.
Do not ask me to attach either file.

Workflow:
- Use the accepted BRD to answer product-definition questions yourself.
- Only ask me where the BRD is silent or genuinely ambiguous.
- Stay inside the BRD's in-scope list; treat everything out of scope as excluded.
- Carry forward open questions that need a product decision; do not invent new
  features.

Produce a PRD with user stories and clear, checkable acceptance criteria for each
in-scope capability. Give every acceptance criterion an id so later stages can
refer to it.

Do not write ADRs, GitHub issues, sprint plans, or application code in this step.

Save the finished PRD to:
lifecycle/03-product-definition/output/prd.md
```

## 5. What you should see afterwards

A new file at **`lifecycle/03-product-definition/output/prd.md`**.

Read the acceptance criteria closely — this is the moment to catch a misunderstanding. Everything from here on is measured against them.

---

## Part B — Technical decisions (the ADRs)

## 6. Pick the helper

1. In Copilot Chat, open the mode dropdown again.
2. Choose **`adr-creation`**.

Run this after the PRD exists. Do not use `RPI Agent`.

## 7. Paste this prompt

```text
Create architecture decision records (ADRs) for the first version of this product.

Read from the workspace:
- lifecycle/02-discovery/output/brd.md
- lifecycle/03-product-definition/output/prd.md
- lifecycle/02-discovery/input/mvp-framing.md (for stated constraints)

Decide only what the BRD and PRD leave open and what the constraints require —
for example the programming language and framework, how and where data is stored,
and how users are identified. If the framing states a technology preference,
record it as a decision with its reasoning rather than re-opening it.

One of these decisions must cover testing. Record the test framework you have
chosen and, explicitly, the exact command someone types to run the whole test
suite — for example `pytest` or `npm test`. Stage 6 runs that command after every
task and Stage 8 cites its result, so it must be written down here rather than
guessed at later.

For each decision record: context, the decision, the alternatives considered,
the consequences, and when it would be worth revisiting.

Do not expand product scope. Do not write application code or tickets.

Name each file YYYY-MM-DD-<short-slug>-v01.md and save under:
lifecycle/03-product-definition/output/adr/

Then update lifecycle/03-product-definition/output/adr/README.md so its table
lists every ADR you created.
```

## 8. What you should see afterwards

One file per decision under **`lifecycle/03-product-definition/output/adr/`**, and an updated index at `adr/README.md`.

You should now be able to answer "what language is this written in, where does the data live, and what command runs the tests?" by pointing at a file. If the test command is missing, ask for it now — Stage 6 needs it after every single task.

---

## 9. If a helper asks you a question

Answer from your [framing document](../02-discovery/input/mvp-framing.md) or the BRD. If neither says, make the call yourself — this stage is exactly where those decisions belong. Technical questions you have no opinion on are fine to hand back: reply "you decide, and record why in the ADR."

## 10. Done when

- `lifecycle/03-product-definition/output/prd.md` exists
- Every feature in it has acceptance criteria you could actually check
- At least one ADR exists under `lifecycle/03-product-definition/output/adr/`
- Your language and data storage choices are written down somewhere
- One ADR names your test framework and the exact command that runs the tests
- Nothing appeared that was out of scope in the BRD

**Next:** [Stage 4 — Decomposition](../04-decomposition/README.md)

---

## Optional — a diagram

If your product has several moving parts, the `architecture-diagrams` skill can draw how they fit together. Save the result under `lifecycle/03-product-definition/output/`. Skip this if your first version is small.
