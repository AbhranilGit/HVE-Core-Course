# Stage 9 — Handover and enablement

Make yourself unnecessary, on purpose, before your last day.

| | |
| --- | --- |
| **Reads** | The code, the decision records, the release notes, and the engagement brief |
| **Produces** | `docs/operations/runbook.md`, `docs/operations/handover.md`, and engineers who can keep going |
| **Commands** | Default Copilot Chat to write, `/doc-ops-update` to check |

Do **A** through **E**. Start in your second-to-last iteration, not your last week.

---

## 1. What this stage is for

Everything before this produced software. This stage decides whether the software survives contact with your departure.

It is worth being blunt about the failure mode, because it is common and it does not look like failure at the time. An engagement ships working, well-tested, well-documented software. The FDE leaves. Six months later the system is unchanged, because nobody on the customer's team can safely modify it. Every individual artefact was good. The engagement still failed.

What prevents that is not more documentation. It is that people on the customer's team have already **done** the work, with you watching, and hit problems while you were still there to help. If your enablement plan is a session in the final week, it is not an enablement plan.

The measure of this stage is not what you produced. It is what they can do.

## 2. Prerequisites

- Stage 8 is finished, so a tagged release exists
- Section 4 of the [engagement brief](../00-engagement/engagement-brief.md) lists your exit criteria
- Section 2 names the engineers being enabled
- Section 8 says where everything ends up

**Timing matters here more than anywhere else in this template.** Part D needs your presence while the customer's engineers do real work, and you cannot compress that into a final afternoon. Start this stage one iteration before the end.

---

## A. Write the runbook

Use the **default Copilot Chat**. HVE Core's documentation helper is a quality checker rather than a first-draft writer, so it comes in at part B.

```text
Write an operator runbook for version v0.1.0.
If docs/operations/runbook.md already exists, verify and update it in place
rather than rewriting it from scratch.

Read from the workspace:
- The application and test code, at the paths named in
  .github/copilot-instructions.md — especially how it starts, where it stores
  data, and what configuration it reads
- docs/decisions/ — the decisions and inherited constraints in force
- .github/copilot-instructions.md — the recorded install, run, and test commands
- docs/releases/v0.1.0-release-notes.md

The runbook must cover:
- What must be installed first, with versions
- How to install dependencies and start the application — the exact commands
  that work in this repository
- How to reach it once running
- Where its data is stored, including defaults and environment variables
- How to run the tests
- How to deploy it, and how to roll back
- How to check it is working, in steps someone can follow blind
- The failures most likely to happen and how to fix each one
- What this version deliberately cannot do, from the scope framing

Write it for an engineer at the customer who has not worked on this and cannot
ask me. Do not assume any context from our conversations.

Rules:
- Every command must match what is actually in this repository. Do not invent
  flags, paths, or environment variables — read them from the code.
- Do not reference me, this engagement's chat history, or any Microsoft-internal
  tool the customer will not have.
- Where you cannot verify something, say so rather than guessing.

Save to:
docs/operations/runbook.md
```

**You should see:** `docs/operations/runbook.md`

---

## B. Check it against the real repository

Clear the chat and run `/doc-ops-update` — it brings the `Doc Ops` helper with it:

```text
/doc-ops-update scope=docs
```

`Doc Ops` reads every markdown file under `docs/`, then checks whether the writing follows the project's conventions, whether the **example commands and file paths actually exist and work**, and whether anything in the repository is undocumented. That middle check is the one that matters — it is exactly how a runbook goes stale, and exactly what you cannot spot by rereading your own words.

It keeps a session file under `.copilot-tracking/doc-ops/<date>-session.md`. Add `validate-only=true` for findings without edits.

Then do the test that actually counts: **have one of the customer's engineers follow the runbook on their own machine, from scratch, while you say nothing.** Every place they get stuck is a defect in the runbook. Fix it and repeat.

Doing this yourself proves nothing. You already know the answers.

---

## C. Write the handover document

The runbook says how to operate the system. The handover document says everything else the customer needs and cannot reconstruct from the repository.

Use the **default Copilot Chat** (not `Doc Ops`) and paste:

```text
Write a handover document for this engagement.

Read from the workspace:
- lifecycle/00-engagement/engagement-brief.md
- docs/decisions/ — every decision record
- docs/reviews/ — every review, including deferred and will-not-fix findings
- docs/releases/ — the release notes and evidence
- docs/planning/sprint-plan.md, including anything listed as not delivered
- docs/operations/runbook.md

Produce docs/operations/handover.md covering:
1) What was delivered, mapped to the engagement's exit criteria, and how each
   was verified.
2) What was not delivered, and why: unscheduled backlog, deferred findings, and
   anything accepted as will-not-fix. Be direct about this.
3) The decisions that shape the system, summarised, each pointing at its record.
   Separate the ones inherited from the customer from the ones made during this
   engagement.
4) Known risks and weak points — where this system is most likely to bite
   whoever maintains it next.
5) What to do first if something is wrong, pointing at the runbook.
6) The recommended next steps, ordered, with the reasoning for that order.
7) Who did what, and who now owns each part.

Write for the customer's engineering team and their product owner. Assume they
were not in most of the meetings.

Be honest about the weak points. A handover that reads as a success story is
less useful than one that says where the bodies are buried.
```

**You should see:** `docs/operations/handover.md`

Point 4 is the section people soften, and the one that is worth the most. If you know a module is fragile, or a test suite has a gap, or a decision was made under time pressure and should be revisited, say so plainly. You will not be there to warn them later.

---

## D. Enable the engineers

This is the part with no command, and the part that determines whether the engagement mattered.

For each engineer named in section 2 of the engagement brief, work through a progression. Do not skip to the end.

| Stage | What happens | You are |
| --- | --- | --- |
| **Watch** | They observe you running the four-phase loop on a real task | Driving |
| **Pair** | They drive, you sit with them | Advising |
| **Solo with review** | They take a task alone; you review the pull request | Reviewing |
| **Solo** | They take a task and one of their own colleagues reviews it | Not involved |

The last row is the actual goal, and the one most engagements never reach. An engineer who can only work with you reviewing has not been enabled; they have been temporarily assisted.

Use real backlog items, never exercises. Contrived tasks teach the tool and hide everything difficult about the codebase.

Track this as work items in their tracker, with acceptance criteria like any other work. Enablement that is not tracked is enablement that gets dropped the first week things get busy — and it will be a busy week, because it is the last one.

Record in the handover document where each engineer actually got to. If someone never made it past pairing, that is a real risk to write down, not a failure to hide.

---

## E. Confirm the exit criteria

Take section 4 of the engagement brief and go through it with the sponsor, line by line, before your last day. Not on your last day — you want time to fix something small.

| For each criterion | Record |
| --- | --- |
| Met | The evidence, and where it lives |
| Partly met | What is missing, and what it would take |
| Not met | Why, and what you recommend |

Put the outcome at the top of `docs/operations/handover.md`, with the date and who confirmed it. This is the document that says the engagement is complete, and it is the one people will look for a year from now.

If a criterion is not met, say so plainly. An engagement that closes with a documented gap is in far better shape than one that closes with a gap nobody wrote down.

---

## F. When something breaks later

You may not be there, but the customer will be. HVE Core has a command for working an incident. Clear the chat and run `/incident-response` — it brings the incident-response helper with it:

```text
/incident-response severity=3 phase=triage
```

`severity` runs from 1 (worst) to 4, and `phase` steps through `triage`, `diagnose`, `mitigate`, and `rca`. Keep the reports under `docs/operations/incidents/`.

Show the customer's engineers this during part D, on a past incident or a simulated one. It is worth ten minutes, and it is the command they will reach for on their worst day.

Once the cause is known, fix it as a normal task through [Stage 6](../06-implementation/README.md). Hotfixes get the same discipline as features, which is exactly why the record stays honest.

---

## 3. Done when

- `docs/operations/runbook.md` exists, and a customer engineer followed it unaided
- `Doc Ops` has checked it and you have dealt with what it flagged
- `docs/operations/handover.md` exists, including an honest weak-points section
- Every named engineer has at least paired on a real task, and where they got to is recorded
- At least one of them has shipped a change reviewed by a colleague rather than by you
- The exit criteria have been walked through with the sponsor and the outcome is recorded
- Everything is in the repository the customer owns, at the location section 8 of the brief specifies
- Nothing critical exists only in your notes, your laptop, or your memory

---

## You are finished

The measure of this engagement is not what you built. It is what they can build next week without you.

| Situation | What to do |
| --- | --- |
| **They are continuing the work** | The lifecycle is theirs now. They start at [Stage 2](../02-discovery/README.md) for a new increment, or [Stage 6](../06-implementation/README.md) for the next item in the backlog |
| **A defect turns up** | Through [Stage 6](../06-implementation/README.md) like anything else |
| **A follow-on engagement is agreed** | Start again at [Stage 0](../00-engagement/README.md). Different contract, different boundaries, new brief |
| **You are leaving for good** | The runbook, the handover document, and the release notes are what you hand over. Everything else is context they can read in the repository |
