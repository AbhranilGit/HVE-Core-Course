# Product requirements documents

The **PRD** lands here. This is HVE Core's own default location — `PRD Builder`
writes to `docs/prds/` without being told to, and scans this folder to resume a
session you started earlier.

| File | Written by | Stage |
| --- | --- | --- |
| `<name>.md` | `PRD Builder` | [Stage 3, part A](../../lifecycle/03-product-definition/README.md) |

`<name>` is a kebab-case version of the title. "Batch reconciliation service"
becomes `batch-reconciliation-service.md`.

`PRD Builder` keeps its session state in
`.copilot-tracking/prd-sessions/<name>.state.json`. That is how it picks up where
it left off — leave it alone.

## Why this file matters more than the others

Every acceptance criterion here gets a stable id. Stage 4 cites those ids on each
work item, Stage 6 builds against them, and Stages 7 and 8 check the result
against them one row at a time.

On an engagement that chain does something beyond quality control. It is how you
answer "did we deliver what was contracted?" with evidence rather than
recollection, and it is what a scope dispute in week nine gets settled by. A
criterion that is vague here is a criterion you cannot demonstrate later.

Write each one so the customer's product owner could check it without asking you
what it meant. If they could not, it is not finished.

Empty until you run Stage 3.
