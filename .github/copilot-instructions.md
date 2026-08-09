# Project guidance

Repository conventions for every AI helper working in this project. Keep this
file short — it is loaded into every request.

Stage 1 fills in the project section. Stage 3 fills in the stack section once
the ADRs exist. Everything else is already correct for this template.

## Project

| Field | Value |
| --- | --- |
| Name | `<your project name>` |
| What it is | `<one line>` |
| Scope source of truth | `lifecycle/02-discovery/mvp-framing.md` |

## Stack

Filled in during Stage 3, from the accepted ADRs. Until then, do not assume a
language.

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

These are HVE Core's own default locations. Do not relocate them.

| Artifact | Path |
| --- | --- |
| BRD | `docs/project-planning/<name>-brd.md` |
| PRD | `docs/project-planning/<name>.md` |
| ADRs | `docs/planning/adrs/NNNN-kebab-case-title.md` |
| Research, plans, changes, review logs | `.copilot-tracking/` |
| Release notes | `docs/releases/` |
| Runbook | `docs/operations/runbook.md` |
| Application code | `src/` |
| Tests | `tests/` |

## Working rules

- Read files from the workspace. Do not ask the user to attach a file whose
  path is already in the prompt.
- Anything absent from `lifecycle/02-discovery/mvp-framing.md` is out of scope.
  Say so rather than building it.
- Do not reference `.copilot-tracking/` paths in application code, code
  comments, docstrings, or commit messages.
- Do not weaken, skip, or delete a test to make a run pass.
