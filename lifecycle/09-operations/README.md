# Stage 9 — Operations

Write the page that tells the next person how to run this.

| | |
| --- | --- |
| **Reads** | Your code, your decision records, and the Stage 8 release notes |
| **Produces** | `docs/operations/runbook.md`, checked by `Doc Ops` |
| **Commands** | Default Copilot Chat to write it, then `/doc-ops-update` to check it |

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

Use the **default Copilot Chat** for this part. HVE Core's documentation helper
is a quality checker rather than a first-draft writer, so it comes in at part B.

Do **not** use `BRD Builder`, `PRD Builder`, or the task helpers here. You are not
building anything in this stage.

```text
Write an operator runbook for version v0.1.0 of this product.
If docs/operations/runbook.md already exists, verify and update it in place
rather than rewriting it from scratch.

Read from the workspace:
- src/ and tests/ — especially how the application starts, where it stores data,
  and any configuration it reads
- docs/decisions/ — the technical decisions in force
- .github/copilot-instructions.md — the recorded install, run, and test commands
- docs/releases/v0.1.0-release-notes.md
- README.md and any dependency or build configuration files in the repository

The runbook must cover:
- What must be installed first, with versions, taken from the decision records
  and the repository's own configuration
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

## B. Check the runbook against the real repository

This is what `Doc Ops` is for. Clear the chat and run:

```text
/doc-ops-update scope=docs
```

`Doc Ops` reads every markdown file under `docs/`, then checks three things:
whether the writing follows the project's documentation conventions, whether the
**example commands and file paths actually exist and work**, and whether anything
in the repository is undocumented. That middle check is the one that matters
here — it is exactly how a runbook goes stale, and exactly what you cannot spot
by rereading your own words.

It keeps a session file under `.copilot-tracking/doc-ops/<date>-session.md`
recording what it found, what it fixed, and what it left for you.

Want the findings without the edits? Add `validate-only=true`.

**You should see:** corrections applied to `docs/operations/runbook.md`, and a
list of anything it could not verify.

Better still, follow the runbook yourself on a clean machine, or a fresh copy of
the repository. Every gap you find that way is a gap the next person would have
hit.

---

## C. When something breaks later

You do not need this today, but this is where it lives. When the product
misbehaves in production, HVE Core has a command for working the incident:

```text
/incident-response severity=3 phase=triage
```

Describe what you are seeing and when it started. `severity` runs from 1 (worst)
to 4, and `phase` steps through `triage`, `diagnose`, `mitigate`, and `rca` — the
root cause analysis. Work the phases in order across the life of the incident.
Keep the resulting reports under `docs/operations/incidents/`.

Once you know the cause, fix it as a normal task: go back to
[Stage 6](../06-implementation/README.md) and run the four-phase loop on it.
Hotfixes get the same discipline as features, which is exactly why the record
stays honest.

---

## 3. If a helper asks you a question

Anything about how the app starts should come from the code — say "read it from
`src/`". If it asks about something only you know, such as where the app will run
in future, answer briefly and let it record your answer.

## 4. Done when

- `docs/operations/runbook.md` exists
- `Doc Ops` has checked it and you have dealt with what it flagged
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
