# Project planning

Your **BRD** and **PRD** land here. This is HVE Core's own default location —
`BRD Builder` and `PRD Builder` write here without being told to, and they scan
this folder to resume a session you started earlier.

| File | Written by | Stage |
| --- | --- | --- |
| `<name>-brd.md` | `BRD Builder` | [Stage 2 — Discovery](../../lifecycle/02-discovery/README.md) |
| `<name>.md` | `PRD Builder` | [Stage 3 — Product definition](../../lifecycle/03-product-definition/README.md) |

`<name>` is a kebab-case short name for your product, chosen by the helper on
its first run and reused after that.

Both helpers also keep session state under `.copilot-tracking/brd-sessions/`
and `.copilot-tracking/prd-sessions/`. That is how they pick up where they left
off — leave it alone.

Empty until you run Stage 2.
