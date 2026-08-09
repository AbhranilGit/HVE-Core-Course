# Business requirements documents

Your **BRD** lands here. This is HVE Core's own default location — `BRD Builder`
writes to `docs/brds/` without being told to, and scans this folder to resume a
session you started earlier.

| File | Written by | Stage |
| --- | --- | --- |
| `<name>-brd.md` | `BRD Builder` | [Stage 2 — Discovery](../../lifecycle/02-discovery/README.md) |

`<name>` is a kebab-case short name for your product, chosen by the helper on its
first run and reused after that.

`BRD Builder` keeps its session state in
`.copilot-tracking/brd-sessions/<name>.state.json`. That is how it picks up where
it left off — leave it alone.

## Optional: your own template

If `docs/templates/brd-template.md` exists, `BRD Builder` uses it as the
skeleton. This kit does not ship one, so the helper falls back to its built-in
structure. Add one only if your organisation has a required BRD format.

Empty until you run Stage 2.
