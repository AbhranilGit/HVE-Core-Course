# Product requirements documents

Your **PRD** lands here. This is HVE Core's own default location — `PRD Builder`
writes to `docs/prds/` without being told to, and scans this folder to resume a
session you started earlier.

| File | Written by | Stage |
| --- | --- | --- |
| `<name>.md` | `PRD Builder` | [Stage 3, part A](../../lifecycle/03-product-definition/README.md) |

`<name>` is a kebab-case version of your product's title. "Mobile expense
tracking app" becomes `mobile-expense-tracking-app.md`.

`PRD Builder` keeps its session state in
`.copilot-tracking/prd-sessions/<name>.state.json`. That is how it picks up where
it left off — leave it alone.

## Why this file matters more than the others

Every acceptance criterion in the PRD gets a stable id. Stage 4 cites those ids
on each task, Stage 6 builds against them, and Stages 7 and 8 check the finished
product against them one row at a time. If a criterion here is vague, that
vagueness travels all the way to your release evidence.

Empty until you run Stage 3.
