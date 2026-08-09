# Stage 2 — Discovery

Turn your idea into a clear written statement of the problem you are solving.

| | |
| --- | --- |
| **Reads** | [`input/mvp-framing.md`](input/mvp-framing.md) |
| **Produces** | [`output/brd.md`](output/brd.md) |
| **Helper** | `brd-builder` |

---

## 1. What this stage is for

You are about to produce a **BRD** — a business requirements document. It is a short write-up of *why* this product should exist: the problem, who has it, what success looks like, and what you are deliberately not building.

It deliberately says nothing about features or technology. That comes in Stage 3. Getting the "why" written down first is what stops the next six stages from drifting.

## 2. Prerequisites

- Stage 1 is finished and the helpers appear in Copilot Chat
- [`input/mvp-framing.md`](input/mvp-framing.md) is filled in with your idea — no `<placeholders>` left
- You have this repository open as the folder in VS Code

## 3. Pick the helper

1. Open Copilot Chat in VS Code (the chat icon in the left Activity Bar, or `Ctrl+Alt+I` / `Cmd+Alt+I`).
2. Click the mode dropdown at the bottom of the chat box — it usually says *Ask* or *Agent*.
3. Choose **`brd-builder`**.

Do **not** use `RPI Agent` or `prd-builder` here. `RPI Agent` writes code, and it will happily start building your app instead of thinking about the problem.

Not in the list? See [If something goes wrong](../../README.md#if-something-goes-wrong).

## 4. Paste this prompt

Copy the whole block below and paste it into the chat. Change nothing — it already knows where to find your idea.

```text
Create a business requirements document (BRD) for the product described in
lifecycle/02-discovery/input/mvp-framing.md.

Read that file from the workspace. Do not ask me to attach it.

Workflow:
- Use the framing to answer the discovery questions yourself.
- Only ask me where the framing is silent or genuinely ambiguous.
- Derive assumptions and risks from the framing; do not invent new scope.
- Carry forward the open questions the framing already lists; add new ones only
  if something important is missing.

Produce a BRD containing: problem statement, stakeholders, in and out of scope,
success metrics, assumptions, risks, and open questions.

Do not write a PRD, acceptance criteria, ADRs, tickets, or any application code.
Do not widen the scope beyond the framing's in-scope list.

Save the finished BRD to:
lifecycle/02-discovery/output/brd.md
```

## 5. What you should see afterwards

A new file at **`lifecycle/02-discovery/output/brd.md`**.

Open it and skim. It should describe *your* problem in your terms. If it describes a different product, or lists features you never mentioned, say so in the chat and ask it to work only from the framing file.

## 6. If the helper asks you a question

Answer from your [framing document](input/mvp-framing.md). If the answer is not there, decide now, tell the helper — and then **add that answer to the framing document**, so the next stage inherits it instead of asking again.

## 7. Done when

- `lifecycle/02-discovery/output/brd.md` exists
- The problem it describes is recognisably yours
- Its out-of-scope list matches what you wrote in the framing
- Nothing in it surprised you — if something did, fix the framing and rerun

**Next:** [Stage 3 — Product definition](../03-product-definition/README.md)
