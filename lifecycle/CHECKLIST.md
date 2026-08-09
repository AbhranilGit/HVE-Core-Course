# Your progress

Keep this page open. Work top to bottom and tick a box only when the file in the last column actually exists on disk.

New here? Read the [main README](../README.md) first. Confused by a word? See the [glossary](../docs/guides/glossary.md).

---

## Before anything else

- [ ] **Stage 1 — Setup.** Install the helpers and confirm they appear in Copilot Chat.
      Page: [01-setup/input/setup-checklist.md](01-setup/input/setup-checklist.md)
      Proof: [01-setup/output/setup-confirmation.md](01-setup/output/setup-confirmation.md) filled in

- [ ] **Write your idea down.** This is the only document you write by hand. Everything else reads it.
      File: [02-discovery/input/mvp-framing.md](02-discovery/input/mvp-framing.md)

---

## The nine stages

| Done | Stage | Helper to pick | Page to open | File that must exist afterwards |
| --- | --- | --- | --- | --- |
| ☐ | 1 — Setup | *(none — you do this by hand)* | [checklist](01-setup/input/setup-checklist.md) | `01-setup/output/setup-confirmation.md` |
| ☐ | 2 — Discovery | `brd-builder` | [Stage 2](02-discovery/prompt/README.md) | `02-discovery/output/brd.md` |
| ☐ | 3a — Features | `prd-builder` | [Stage 3](03-product-definition/prompt/README.md) | `03-product-definition/output/prd.md` |
| ☐ | 3b — Technical decisions | `adr-creation` | [Stage 3](03-product-definition/prompt/README.md) | files under `03-product-definition/output/adr/` |
| ☐ | 4 — Decomposition | `github-backlog-manager` | [Stage 4](04-decomposition/prompt/README.md) | `04-decomposition/output/backlog-snapshot.md` |
| ☐ | 5 — Sprint planning | `github-backlog-manager` | [Stage 5](05-sprint-planning/prompt/README.md) | `05-sprint-planning/output/sprint-plan.md` |
| ☐ | 6 — Implementation | `RPI Agent` | [Stage 6](06-implementation/prompt/README.md) | `06-implementation/output/issue-NN/` per task, plus code in `src/` |
| ☐ | 7 — Review | `RPI Agent`, then `code-review` | [Stage 7](07-review/prompt/README.md) | `07-review/output/sprint-1-rpi-review.md` |
| ☐ | 8 — Delivery | default Copilot Chat | [Stage 8](08-delivery/prompt/README.md) | `08-delivery/output/v0.1.0-release-notes.md` |
| ☐ | 9 — Operations | `Doc Ops` | [Stage 9](09-operations/prompt/README.md) | `09-operations/output/runbook.md` |

---

## Stage 6 has an inner loop

Stage 6 is the long one. You build **one task at a time**, and each task takes three prompts in this order:

- [ ] Research — produces `research.md`
- [ ] Plan — produces `plan.md`
- [ ] Implement — produces `implement.md` and the actual code

Do not start a task's Plan before its Research file exists, and do not start the next task before the current one's Implement file exists. Copy this three-line list once per task.

---

## Three ways people get stuck

1. **Skipping a stage.** Each stage reads the previous stage's output file. If it is missing, the helper has nothing to work from.
2. **Adding features mid-way.** If you want something new, edit [mvp-framing.md](02-discovery/input/mvp-framing.md) first, then continue. Otherwise the documents and the code drift apart.
3. **Trusting the chat instead of the files.** Chat history disappears. If it matters, it belongs in a file under `lifecycle/`.
