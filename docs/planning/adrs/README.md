# Architecture decision records

Each file here records one technical decision: what you chose, why, what it
costs you, and when it would be worth changing your mind.

Written by the **`ADR Creator`** helper in
[Stage 3, part B](../../../lifecycle/03-product-definition/README.md). This is
HVE Core's own default location for ADRs, so the helper writes here without
being told to. Empty until you run that stage.

## Why bother

Six months from now, someone — probably you — will ask "why is this built this
way?" Without these files the answer is lost, and the AI helpers have no way to
stay consistent with choices you already made. Stages 6, 7, and 9 all read this
folder so they work with your language and your tools rather than guessing.

## Naming

`NNNN-kebab-case-title.md`, where `NNNN` is a four-digit zero-padded number in
decision order. For example `0001-sqlite-for-local-storage.md`. This is the
MADR convention that `ADR Creator` follows.

## The decisions every project needs

Whatever else you record, these three must be answerable from this folder,
because later stages read them rather than asking you again:

| Question | Who reads the answer |
| --- | --- |
| What language and framework is this built in? | Stage 6, so it writes code in your stack |
| Where does the data live? | Stage 6, and the Stage 9 runbook |
| What exact command runs the tests? | Stage 6 after every task, and Stage 8 at release |

The test command is the one people forget. Write it as something you could
paste into a terminal — `pytest`, `npm test`, `go test ./...` — not as "run the
unit tests". Copy it into `.github/copilot-instructions.md` when it is decided.

## What does not belong here

- Application code
- Tasks or sprint plans
- New product features — an ADR records *how* you build, never *what* you build
