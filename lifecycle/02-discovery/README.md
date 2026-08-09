# Stage 2 — Discovery

Turn your idea into a clear written statement of the problem you are solving.

| | |
| --- | --- |
| **Reads** | [`mvp-framing.md`](mvp-framing.md) |
| **Produces** | `docs/brds/<name>-brd.md` |
| **Helper** | `BRD Builder` |

---

## 1. What this stage is for

You are about to produce a **BRD** — a business requirements document. It is a
short write-up of *why* this product should exist: the problem, who has it, what
success looks like, and what you are deliberately not building.

It deliberately says nothing about features or technology. That comes in
Stage 3. Getting the "why" written down first is what stops the next six stages
from drifting.

## 2. Prerequisites

- Stage 1 is finished and the helpers appear in Copilot Chat
- [`mvp-framing.md`](mvp-framing.md) is filled in with your idea — no `<placeholders>` left
- You have this repository open as the folder in VS Code

## 3. Pick the helper

1. Open Copilot Chat in VS Code (the chat icon in the left Activity Bar, or `Ctrl+Alt+I` / `Cmd+Alt+I`).
2. Click the mode dropdown at the bottom of the chat box — it usually says *Ask* or *Agent*.
3. Choose **`BRD Builder`**.

Do **not** use `PRD Builder` or any of the task helpers here. `Task Implementor`
writes code, and it will happily start building your app instead of thinking
about the problem.

Not in the list? See [If something goes wrong](../../README.md#if-something-goes-wrong).

## 4. Paste this prompt

Copy the whole block below and paste it into the chat. Change nothing — it
already knows where to find your idea.

```text
Create a business requirements document (BRD) for the product described in
lifecycle/02-discovery/mvp-framing.md.

Read that file from the workspace. Do not ask me to attach it.

Workflow:
- Use the framing to answer the discovery questions yourself.
- Only ask me where the framing is silent or genuinely ambiguous.
- Derive assumptions and risks from the framing; do not invent new scope.
- Carry forward the open questions the framing already lists; add new ones only
  if something important is missing.

Produce a BRD covering: problem statement, stakeholders, in and out of scope,
success metrics, assumptions, risks, and open questions.

Do not write a PRD, acceptance criteria, ADRs, tickets, or any application code.
Do not widen the scope beyond the framing's in-scope list.

Save the BRD to your default location under docs/brds/ and tell me the exact
path you used.
```

`BRD Builder` already knows to write to `docs/brds/<name>-brd.md`, and it keeps
its session state in `.copilot-tracking/brd-sessions/<name>.state.json`. That is
how it resumes if you come back tomorrow — leave both alone.

## 5. What you should see afterwards

A new file under **`docs/brds/`**, named after your product and ending in
`-brd.md`. The helper tells you the exact path.

Open it and skim. It should describe *your* problem in your terms. If it
describes a different product, or lists features you never mentioned, say so in
the chat and ask it to work only from the framing file.

Write the path down — Stage 3 asks for it.

## 6. If the helper asks you a question

`BRD Builder` works by guided question-and-answer, so expect a few. Answer from
your [framing document](mvp-framing.md). If the answer is not there, decide now,
tell the helper — and then **add that answer to the framing document**, so the
next stage inherits it instead of asking again.

## 7. Done when

- A `-brd.md` file exists under `docs/brds/`
- The problem it describes is recognisably yours
- Its out-of-scope list matches what you wrote in the framing
- Nothing in it surprised you — if something did, fix the framing and rerun

---

## Optional — if your domain needs it

HVE Core ships extra Discovery planners. Skip these unless your domain calls for
one; each produces its own plan document alongside the BRD.

| Helper | Use it when |
| --- | --- |
| `Security Planner` | The product handles credentials, personal data, or anything an attacker would want. Produces a STRIDE-based security model. |
| `RAI Planner` | The product contains AI or makes automated decisions about people. Produces a Responsible AI assessment. |
| `SSSC Planner` | You need supply-chain assurance — SBOM, SLSA, OpenSSF Scorecard. |
| `/task-research topic=...` | A genuine technical unknown blocks the BRD. Investigates and writes evidence under `.copilot-tracking/research/` before you commit to anything. |

Run them after the BRD exists, and tell each one to read the BRD from
`docs/brds/`.

**Next:** [Stage 3 — Product definition](../03-product-definition/README.md)
