# Project guidance

Repository conventions for every AI helper working in this project. Keep this file short — it is loaded into every request.

Stage 1 fills in the engagement and stack sections. On an existing codebase the stack is **recorded, not chosen**: read it out of the repository and confirm it by running the commands yourself.

## Engagement

| Field | Value |
| --- | --- |
| Customer | `<organisation>` |
| Engagement | `<short name>` |
| Last day | `<YYYY-MM-DD>` |
| Engagement boundaries | `lifecycle/00-engagement/engagement-brief.md` |
| Scope source of truth | `lifecycle/02-discovery/scope-framing.md` |
| Contracted scope originates from | `<link or path to the SOW or ADS output>` |
| HVE Core version this kit targets | `3.3.101` (`ise-hve-essentials.hve-core-all`) |

The version matters. HVE Core renames helpers and commands between releases, and every prompt in `lifecycle/` is written against 3.3.101. If you upgrade the extension and a command stops being offered, check the stage page against the new release before editing anything.

## Stack

Filled in during Stage 1 from the existing repository, and extended in Stage 3 for anything genuinely undecided. Mark each row as inherited or chosen.

| Field | Value | Inherited or chosen |
| --- | --- | --- |
| Language and version | | |
| Framework | | |
| Data storage | | |
| Install command | | |
| Run command | | |
| Test command | | |
| Application code path | | |
| Test path | | |

The test command above is authoritative. Stage 6 runs it after every task and Stage 8 cites its result. Do not record a command you have not run yourself.

## Their conventions

Fill this in from the existing codebase. It is what the standards half of `/code-review-full` checks against, and generic advice here produces review findings the customer's engineers will reject.

| Convention | How this codebase does it |
| --- | --- |
| Naming | |
| Error handling | |
| Logging | |
| Configuration | |
| Test structure and naming | |
| Anything else non-obvious | |

## Where artifacts belong

The first three are HVE Core's own defaults for 3.3.101. Do not relocate them.

| Artifact | Path |
| --- | --- |
| BRD | `docs/brds/<name>-brd.md` |
| PRD | `docs/prds/<name>.md` |
| Decision records | `docs/decisions/YYYY-MM-DD-<topic>-v01.md` |
| Sprint plan | `docs/planning/sprint-plan.md` |
| Review summaries | `docs/reviews/` |
| Release evidence and notes | `docs/releases/` |
| Runbook and handover | `docs/operations/` |
| Application code and tests | As recorded in the Stack table above |
| Research, plans, changes, review logs | `.copilot-tracking/` |

## Working rules

- Read files from the workspace. Do not ask the user to attach a file whose path is already in the prompt.
- Anything absent from `lifecycle/02-discovery/scope-framing.md` is out of scope. Say so rather than building it.
- This is the customer's codebase. Follow the conventions above rather than introducing new ones, and say so when you deliberately depart from one.
- Do not reformat, restructure, or tidy code the current task does not require.
- Do not weaken, skip, or delete a test to make a run pass.
- Do not reference `.copilot-tracking/` paths in application code, code comments, docstrings, commit messages, or work item comments.
- Write commit messages, pull request descriptions, and work item comments for the customer's engineers, who will read them without the surrounding conversation.
- Questions about *how* to build something are the engineer's to answer. Questions about *what* to build belong to the customer — surface them rather than deciding them.
