# Project guidance

Repository conventions for every AI helper working in this project. Keep this
file short — it is loaded into every request.

Stage 1 fills in the project section. Stage 3 fills in the stack section once
the decision records exist. Everything else is already correct for this template.

## Project

| Field | Value |
| --- | --- |
| Name | `<your project name>` |
| What it is | `<one line>` |
| Scope source of truth | `lifecycle/02-discovery/mvp-framing.md` |
| HVE Core version this kit targets | `3.3.101` (`ise-hve-essentials.hve-core-all`) |

The version matters. HVE Core renames helpers and commands between releases, and
every prompt in `lifecycle/` is written against 3.3.101. If you upgrade the
extension and a command stops being offered, check the stage page against the
new release before editing anything.

## Stack

Filled in during Stage 3, from the accepted decision records. Until then, do not
assume a language.

| Field | Value |
| --- | --- |
| Language and version | `<undecided until Stage 3>` |
| Framework | `<undecided until Stage 3>` |
| Data storage | `<undecided until Stage 3>` |
| Install command | `<undecided until Stage 3>` |
| Run command | `<undecided until Stage 3>` |
| Test command | `<undecided until Stage 3>` |

The test command above is authoritative. Stage 6 runs it after every task and
Stage 8 cites its result.

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
| Runbook | `docs/operations/runbook.md` |
| Application code | `src/` |
| Tests | `tests/` |
| Research, plans, changes, review logs | `.copilot-tracking/` |

## Working rules

- Read files from the workspace. Do not ask the user to attach a file whose
  path is already in the prompt.
- Anything absent from `lifecycle/02-discovery/mvp-framing.md` is out of scope.
  Say so rather than building it.
- Do not reference `.copilot-tracking/` paths in application code, code
  comments, docstrings, or commit messages.
- Do not weaken, skip, or delete a test to make a run pass.
