# Stage 3 — Product definition

Decide what you are building, and lock in the big technical choices.

| | |
| --- | --- |
| **Reads** | Your BRD under `docs/project-planning/` |
| **Produces** | `docs/project-planning/<name>.md` and ADRs under `docs/planning/adrs/` |
| **Helpers** | `PRD Builder`, then `ADR Creator` |

This stage has two parts. Do **A** first, then **B**.

---

## 1. What this stage is for

**Part A** produces a **PRD** — a product requirements document. Where the BRD
said *why*, the PRD says *what*: a list of features written as user stories,
each with acceptance criteria — the rules that decide when that feature is
genuinely finished.

**Part B** produces **ADRs** — architecture decision records. Each is a one-page
note capturing a technical decision, why you made it, and what it costs you.
This is where your programming language, your data storage, and anything else
structural gets decided and written down. Decide these once, here, rather than
re-arguing them every time you open the chat.

---

## Part A — Features (the PRD)

## 2. Prerequisites

- Your BRD exists under `docs/project-planning/` and you have read it
- You know its exact filename — the Stage 2 helper told you
- You are happy with its scope; if not, fix the framing and redo Stage 2 first

## 3. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`PRD Builder`**.

Do **not** use `RPI Agent` or `BRD Builder` for this part.

## 4. Paste this prompt

```text
Create a Product Requirements Document (PRD) for the first version of the
product defined in the BRD under docs/project-planning/.

Read from the workspace:
- The BRD in docs/project-planning/ (the file ending in -brd.md)
- lifecycle/02-discovery/mvp-framing.md, for the original scope boundaries

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

Do not write ADRs, issues, sprint plans, or application code in this step.

Save the PRD to your default location under docs/project-planning/ and tell me
the exact path you used.
```

## 5. What you should see afterwards

A new file under **`docs/project-planning/`**, named after your product. The
helper tells you the exact path, and keeps its session notes under
`.copilot-tracking/prd-sessions/`.

Read the acceptance criteria closely — this is the moment to catch a
misunderstanding. Everything from here on is measured against them.

---

## Part B — Technical decisions (the ADRs)

## 6. Pick the helper

1. In Copilot Chat, open the mode dropdown again.
2. Choose **`ADR Creator`**.

Run this after the PRD exists. Do not use `RPI Agent`.

`ADR Creator` is phase-gated: it walks you through *Frame*, *Decide*, and
*Govern* for each decision, and asks you to confirm before advancing. It will
ask early on whether you want `ascii` or `mermaid` diagrams and whether the
repository is public or private. Answer those and keep going.

## 7. Paste this prompt

```text
Create architecture decision records (ADRs) for the first version of this
product.

Read from the workspace:
- The BRD and PRD in docs/project-planning/
- lifecycle/02-discovery/mvp-framing.md, for stated constraints

Decide only what the BRD and PRD leave open and what the constraints require —
for example the programming language and framework, how and where data is
stored, and how users are identified. If the framing states a technology
preference, record it as a decision with its reasoning rather than re-opening it.

One of these decisions must cover testing. Record the test framework you have
chosen and, explicitly, the exact command someone types to run the whole test
suite — for example `pytest` or `npm test`. Stage 6 runs that command after
every task and Stage 8 cites its result, so it must be written down here rather
than guessed at later.

For each decision record: context, the decision, the alternatives considered,
the consequences, and when it would be worth revisiting.

Do not expand product scope. Do not write application code or tickets.

Save the ADRs to your default location under docs/planning/adrs/ and tell me
the exact paths you used.
```

## 8. What you should see afterwards

One file per decision under **`docs/planning/adrs/`**, named
`NNNN-kebab-case-title.md` — for example `0001-sqlite-for-local-storage.md`.

You should now be able to answer "what language is this written in, where does
the data live, and what command runs the tests?" by pointing at a file. If the
test command is missing, ask for it now — Stage 6 needs it after every task.

## 9. Copy the decisions into your project guidance

This step takes a minute and saves you from repeating yourself for the rest of
the project.

Open [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md)
and fill in the **Stack** table from your new ADRs: language and version,
framework, data storage, and the install, run, and test commands.

Every helper reads that file on every request. Once it is filled in, Stage 6
writes code in your stack without being reminded.

While you are there, add your language's throwaway files to `.gitignore` —
`__pycache__/` for Python, `target/` for Rust, and so on.

---

## 10. If a helper asks you a question

Answer from your [framing document](../02-discovery/mvp-framing.md) or the BRD.
If neither says, make the call yourself — this stage is exactly where those
decisions belong. Technical questions you have no opinion on are fine to hand
back: reply "you decide, and record why in the ADR."

## 11. Done when

- A PRD exists under `docs/project-planning/`
- Every feature in it has acceptance criteria you could actually check, each with an id
- At least one ADR exists under `docs/planning/adrs/`
- Your language and data storage choices are written down
- One ADR names your test framework and the exact command that runs the tests
- `.github/copilot-instructions.md` has the Stack table filled in
- Nothing appeared that was out of scope in the BRD

**Next:** [Stage 4 — Decomposition](../04-decomposition/README.md)

---

## Optional — extras for bigger or riskier products

| Helper or skill | Use it when |
| --- | --- |
| `architecture-diagrams` skill | Your product has several moving parts and a picture would help. Ask `ADR Creator` to use it. |
| `Product Manager Advisor` | You want a second opinion on requirement quality or priority before locking the PRD. |
| `Security Planner`, `RAI Planner`, `SSSC Planner` | You ran one in Stage 2 and want its findings reflected as requirements. |
