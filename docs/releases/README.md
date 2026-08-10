# Releases

Release paperwork, one set per version.

| File | What it holds |
| --- | --- |
| `v0.1.0-release-evidence.md` | The proof it was ready: every acceptance criterion, where its evidence lives, the test run, the required reviews, and who signed off |
| `v0.1.0-release-notes.md` | What shipped, how it was checked, what was left out, and which known defects were accepted |

Produced in [Stage 8 — Delivery](../../lifecycle/08-delivery/README.md). Empty until you run it.

`v0.1.0` is this template's default. Use the customer's versioning scheme if they have one — matching their existing tags matters more than matching this template — and keep the filenames consistent with whatever you choose.

## Why the evidence file exists

The release notes say what shipped. The evidence file is what someone reaches for when that claim is questioned: during a customer audit, at the start of a follow-on engagement, or when a defect surfaces months later and somebody asks whether it was known.

Two rules keep it useful. Tick a box only where the evidence supports it, leaving anything unproven visibly unticked with a note on what is blocking it. And record which engagement exit criteria the release contributes to, so the trail from a contract to a commit stays intact after everyone involved has moved on.

