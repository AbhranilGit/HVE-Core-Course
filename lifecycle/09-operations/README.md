# Stage 9 — Operations

Write the page that tells the next person how to run this.

| | |
| --- | --- |
| **Reads** | Your code, your ADRs, and the Stage 8 release notes |
| **Produces** | `docs/operations/runbook.md`, and optionally `docs/operations/ops-confirmation.md` |
| **Helper** | `Documentation` |

---

## 1. What this stage is for

A **runbook** is the page someone opens when they need to start your app, find
its data, or work out why it will not run. That someone is usually you, six
months from now, having forgotten everything.

This is the stage people skip, and it is the reason projects become unusable
within a year. It takes about ten minutes.

A runbook may already exist if one of your Sprint 2 tasks produced one. If so,
this stage checks and updates it rather than starting again.

## 2. Prerequisites

- The app runs, and you know the commands that start it
- Stage 8 is finished, so `v0.1.0` exists

---

## A. Write the runbook

1. Open Copilot Chat and clear it.
2. Choose **`Documentation`** from the mode dropdown — this is HVE Core's
   documentation helper. It works in modes; this task is **author** mode.
3. If it is not listed, use the default Copilot Chat with the same prompt.

Do **not** use `BRD Builder`, `PRD Builder`, or `RPI Agent` here. You are not
building anything in this stage.

```text
Use author mode. Write an operator runbook for version v0.1.0 of this product.
If docs/operations/runbook.md already exists, verify and update it in place
rather than rewriting it from scratch.

Read from the workspace:
- src/ and tests/ — especially how the application starts, where it stores data,
  and any configuration it reads
- docs/planning/adrs/ — the technical decisions in force
- .github/copilot-instructions.md — the recorded install, run, and test commands
- docs/releases/v0.1.0-release-notes.md
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
docs/operations/runbook.md
```

**You should see:** `docs/operations/runbook.md`

---

## B. Prove the runbook works (recommended)

The only real test of a runbook is following it exactly, as though you knew
nothing.

```text
Use validate mode. Produce a short operations confirmation showing that someone
new could start this product from the runbook alone.

Read from the workspace:
- docs/operations/runbook.md
- src/
- docs/releases/v0.1.0-release-notes.md

Record:
1) The exact commands to install, start, use, and test the product
2) Pass or fail for each check: does it install, does it start, does the main
   feature work, do the tests pass. Say plainly if a check was not actually run
   in this session.
3) Anything unclear, missing, or wrong in the runbook
4) Confirmation that nothing in these documents adds features beyond the release

Do not change application code, except to correct a factual error in the runbook.

Save to:
docs/operations/ops-confirmation.md
```

**You should see:** `docs/operations/ops-confirmation.md`

Better still, follow the runbook yourself on a clean machine, or a fresh copy of
the repository. Every gap you find now is a gap the next person would have hit.

---

## C. When something breaks later

You do not need this today, but this is where it lives. When the product misbehaves
in production, HVE Core has a command for working the incident:

```text
/incident-response
```

Describe what you are seeing, when it started, and how bad it is. It walks you
through triage and writes a structured incident report. Keep those under
`docs/operations/incidents/`.

Once you know the cause, fix it as a normal task: go back to
[Stage 6](../06-implementation/README.md) and run the RPI loop on it. Hotfixes
get the same discipline as features, which is exactly why the record stays
honest.

---

## 3. If a helper asks you a question

Anything about how the app starts should come from the code — say "read it from
`src/`". If it asks about something only you know, such as where the app will
run in future, answer briefly and let it record your answer.

## 4. Done when

- `docs/operations/runbook.md` exists
- Its commands match how the app really starts — you have tried them
- Someone who has never seen this project could follow it
- No new features appeared under the heading of "operations"

---

## You are finished

You have a working release, and the documents explaining what it does, why it
exists, and how to run it.

What next:

- **Building more?** Go back to [Stage 2](../02-discovery/README.md), update your [framing document](../02-discovery/mvp-framing.md) with what you learned, and run the lifecycle again for the next version.
- **Found a bug?** Add it to your backlog and take it through [Stage 6](../06-implementation/README.md), so the record stays honest.
- **Handing it over?** The runbook and the release notes are what you send.
