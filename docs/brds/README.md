# Business requirements documents

The **BRD** lands here. This is HVE Core's own default location — `BRD Builder`
writes to `docs/brds/` without being told to, and scans this folder to resume a
session you started earlier.

| File | Written by | Stage |
| --- | --- | --- |
| `<name>-brd.md` | `BRD Builder` | [Stage 2 — Discovery](../../lifecycle/02-discovery/README.md) |

`<name>` is a kebab-case short name, chosen by the helper on its first run and
reused after that.

`BRD Builder` keeps its session state in
`.copilot-tracking/brd-sessions/<name>.state.json`. That is how it picks up where
it left off — leave it alone.

## What a good one looks like here

On an engagement the problem was defined before you arrived, so a BRD that
fluently restates the sales deck has added nothing. The value is in the parts
that are uncomfortable to write:

- Every ambiguity in the statement of work, carried forward as an open question rather than quietly resolved
- Anything you believe cannot be delivered within the stated constraints, flagged in writing
- The scope, matching the contract exactly, with nothing helpfully added

A BRD that says "the statement of work does not define what 'near real time'
means, and the three plausible readings imply different architectures" is worth
the day it took. Everything downstream inherits this scope, so a widening here
becomes unpaid work in week nine.

## Optional: their own template

If `docs/templates/brd-template.md` exists, `BRD Builder` uses it as the
skeleton. This template does not ship one, so the helper falls back to its
built-in structure. Add one if the customer has a required BRD format — some
enterprises do, and matching it saves an argument at review.

Empty until you run Stage 2.
