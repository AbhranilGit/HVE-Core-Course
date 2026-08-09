# The nine stages

This folder is where you spend your time. Each stage is one step of building your product, and each has the same three folders:

| Folder | What it holds |
| --- | --- |
| `input/` | What the stage reads. Usually the previous stage's output, so usually nothing for you to do. |
| `output/` | What the stage produces. Empty until you run it. |
| `prompt/` | The page telling you what to do — which helper to pick and what to paste. **Start here.** |

Tracking your progress: **[CHECKLIST.md](CHECKLIST.md)**
Unfamiliar words: **[glossary](../docs/guides/glossary.md)**

## The stages

| Stage | What it does | Helper | What you end up with |
| --- | --- | --- | --- |
| [1 Setup](01-setup/input/setup-checklist.md) | Install the helpers and check they work | *(by hand)* | `01-setup/output/setup-confirmation.md` |
| [2 Discovery](02-discovery/prompt/README.md) | State the problem clearly | `brd-builder` | `02-discovery/output/brd.md` |
| [3 Product definition](03-product-definition/prompt/README.md) | Decide the features and the technical choices | `prd-builder`, `adr-creation` | `03-product-definition/output/prd.md` and `output/adr/` |
| [4 Decomposition](04-decomposition/prompt/README.md) | Break features into small tasks | `github-backlog-manager` | GitHub issues and `04-decomposition/output/backlog-snapshot.md` |
| [5 Sprint planning](05-sprint-planning/prompt/README.md) | Order the tasks; pick what to build first | `github-backlog-manager` | `05-sprint-planning/output/sprint-plan.md` |
| [6 Implementation](06-implementation/prompt/README.md) | Build it, one task at a time | `RPI Agent` | Code in `src/` and notes in `06-implementation/output/issue-NN/` |
| [7 Review](07-review/prompt/README.md) | Check it against what you promised | `RPI Agent`, `code-review` | Reviews in `07-review/output/` |
| [8 Delivery](08-delivery/prompt/README.md) | Publish the first release | default Copilot Chat | Tag `v0.1.0` and `08-delivery/output/v0.1.0-release-notes.md` |
| [9 Operations](09-operations/prompt/README.md) | Explain how to run it | `Doc Ops` | `09-operations/output/runbook.md` |

## The one thing you write yourself

**[02-discovery/input/mvp-framing.md](02-discovery/input/mvp-framing.md)** — your idea, in your words. Every stage after it reads it, directly or through what it produced. Nothing else needs typing out twice.

## How the stages connect

One stage's output is the next one's input. That is why skipping a stage breaks the one after it — the helper opens the file it was told to read, finds nothing, and either stops or starts inventing.

```text
mvp-framing.md
   → brd.md
      → prd.md + adr/
         → backlog-snapshot.md
            → sprint-plan.md
               → code + issue-NN/ notes
                  → reviews
                     → release notes + tag
                        → runbook.md
```

Going backwards is fine and expected. If a review finds a problem, return to Stage 6. If you change your mind about what you are building, edit the framing document and work forward from Stage 2 again.
