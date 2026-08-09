# Stage 9 — Operations

Write the page that tells the next person how to run this.

| | |
| --- | --- |
| **Reads** | Your code, your ADRs, and the Stage 8 release notes |
| **Produces** | [`output/runbook.md`](output/runbook.md), and optionally [`output/ops-confirmation.md`](output/ops-confirmation.md) |
| **Helper** | `Doc Ops` |

---

## 1. What this stage is for

A **runbook** is the page someone opens when they need to start your app, find its data, or work out why it will not run. That someone is usually you, six months from now, having forgotten everything.

This is the stage people skip, and it is the reason projects become unusable within a year. It takes about ten minutes.

A runbook may already exist if one of your Sprint 2 tasks produced one. If so, this stage checks and updates it rather than starting again.

## 2. Prerequisites

- The app runs, and you know the commands that start it
- Stage 8 is finished, so `v0.1.0` exists

---

## A. Write the runbook

1. Open Copilot Chat.
2. Choose **`Doc Ops`** from the mode dropdown — this is the documentation helper.
3. If it is not listed, use the default Copilot Chat with the same prompt.

Do **not** use `brd-builder`, `prd-builder`, or `RPI Agent` here. You are not building anything in this stage.

```text
Write an operator runbook for version v0.1.0 of this product. If
lifecycle/09-operations/output/runbook.md already exists, verify and update it in
place rather than rewriting it from scratch.

Read from the workspace:
- src/ and tests/ — especially how the application starts, where it stores data,
  and any configuration it reads
- lifecycle/03-product-definition/output/adr/ — the technical decisions in force
- lifecycle/08-delivery/output/v0.1.0-release-notes.md
- README.md and any dependency or build configuration files in the repository

The runbook must cover:
- What must be installed first, with versions, taken from the ADRs and the
  repository's own configuration
- How to install dependencies and start the application — the exact commands
  that work in this repository
- How to reach it once running, for example the address to open
- Where its data is stored, including any defaults and environment variables
- How to run the tests
- How to check it is working, in a few steps someone can follow blind
- The failures most likely to happen and how to fix each one
- What this version deliberately cannot do, from the framing's out-of-scope list

Rules:
- Every command must match what is actually in this repository. Do not invent
  flags, paths, or environment variables — read them from the code.
- Where you cannot verify something, say so rather than guessing.
- Do not add features.

Save to:
lifecycle/09-operations/output/runbook.md
```

**You should see:** `lifecycle/09-operations/output/runbook.md`

---

## B. Prove the runbook works (recommended)

The only real test of a runbook is following it exactly, as though you knew nothing.

```text
Produce a short operations confirmation showing that someone new could start this
product from the runbook alone.

Read from the workspace:
- lifecycle/09-operations/output/runbook.md
- src/
- lifecycle/08-delivery/output/v0.1.0-release-notes.md

Record:
1) The exact commands to install, start, use, and test the product
2) Pass or fail for each check: does it install, does it start, does the main
   feature work, do the tests pass. Say plainly if a check was not actually run
   in this session.
3) Anything unclear, missing, or wrong in the runbook
4) Confirmation that nothing in these documents adds features beyond the release

Do not change application code, except to correct a factual error in the runbook.

Save to:
lifecycle/09-operations/output/ops-confirmation.md
```

**You should see:** `lifecycle/09-operations/output/ops-confirmation.md`

Better still, follow the runbook yourself on a clean machine, or a fresh copy of the repository. Every gap you find now is a gap the next person would have hit.

---

## 3. If a helper asks you a question

Anything about how the app starts should come from the code — say "read it from `src/`". If it asks about something only you know, such as where the app will run in future, answer briefly and let it record your answer.

## 4. Done when

- `lifecycle/09-operations/output/runbook.md` exists
- Its commands match how the app really starts — you have tried them
- Someone who has never seen this project could follow it
- No new features appeared under the heading of "operations"

---

## You are finished

You have a working release, and the documents explaining what it does, why it exists, and how to run it.

What next:

- **Building more?** Go back to [Stage 2](../02-discovery/README.md), update your [framing document](../02-discovery/input/mvp-framing.md) with what you learned, and run the lifecycle again for the next version.
- **Found a bug?** Add it to your backlog and take it through [Stage 6](../06-implementation/README.md), so the record stays honest.
- **Handing it over?** The runbook and the release notes are what you send.
