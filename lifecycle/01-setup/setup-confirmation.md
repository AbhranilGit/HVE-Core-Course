# Stage 1 — Setup confirmation

Fill this in as you work through [`README.md`](README.md). It is your proof that
the tools work, so that when something misbehaves in Stage 6 you know it is not
the setup.

Write short answers in the blank cells — `Pass`, `Fail`, `Yes`, `No`, or a note.

| Field | Value |
| --- | --- |
| **Project** | `<your project name>` |
| **Status** | Not started |
| **Confirmed by** | `<your name>` |
| **Confirmed on** | `<YYYY-MM-DD>` |

---

## 1. The editor and Copilot

| Check | Result | Notes |
| --- | --- | --- |
| Repository opened as the folder in VS Code | | |
| Copilot Chat opens and replies | | |
| **HVE Core - All** installed | | Extension id: `ise-hve-essentials.hve-core-all` |
| VS Code reloaded after installing | | |

## 2. The helpers

Write `Yes` or `No` for each helper you can see in the mode dropdown. If your
extension version names one differently, write down what you actually see.

| Helper | Visible? | Used in | Name in your version, if different |
| --- | --- | --- | --- |
| **BRD Builder** | | Stage 2 | |
| **PRD Builder** | | Stage 3 | |
| **ADR Creator** | | Stage 3 | |
| **GitHub Backlog Manager** | | Stages 4, 5, 6 | |
| **RPI Agent** | | Stage 6 | |
| **Code Review** | | Stage 7 | |
| **Documentation** | | Stage 9 | |

If `BRD Builder` or `RPI Agent` are missing, stop and fix that before going
further. Those two are not optional.

## 3. The slash commands

Type `/` in the chat and write `Yes` or `No`.

| Command | There? | Used in |
| --- | --- | --- |
| `/git-setup` | | Stage 1 |
| `/rpi-research` | | Stage 6 |
| `/rpi-plan` | | Stage 6 |
| `/rpi-implement` | | Stage 6 |
| `/rpi-review` | | Stages 6 and 7 |
| `/pull-request` | | Stage 8 |
| `/pr-review` | | Stage 8 |
| `/git-merge` | | Stage 8 |
| `/incident-response` | | Stage 9 |

## 4. The folders

| Path | There? |
| --- | --- |
| `lifecycle/` | |
| `lifecycle/02-discovery/mvp-framing.md` | |
| `docs/project-planning/` | |
| `docs/planning/adrs/` | |
| `src/` | |
| `tests/` | |
| `.copilot-tracking/` | |

## 5. Git and project guidance

| Check | Result | Notes |
| --- | --- | --- |
| `/git-setup` ran without error | | |
| `git status` runs without error | | |
| You are on your own branch, not `template` | | Branch name: |
| Repository exists on your tracker | | GitHub, Azure DevOps, or Jira; there is a fallback if none |
| `.github/copilot-instructions.md` names your project | | |

Paste what `git status` printed:

```text
_paste here_
```

## 6. Anything unusual

| What | Does it matter? | What you did about it |
| --- | --- | --- |
| _nothing, or describe_ | | |

## 7. Ready to continue?

Write `Yes` only when each row is true.

| Gate | Met? |
| --- | --- |
| The helpers needed for Stages 2 and 6 are visible | |
| The `/rpi-*` commands are available | |
| The folders are all present | |
| Git works and you are on your own branch | |
| `.github/copilot-instructions.md` names your project | |

**Stage 1 complete:** Yes / No — if No, fix the failures above first.

---

## 8. What next

| Step | Action |
| --- | --- |
| **Now** | Write your idea into [`../02-discovery/mvp-framing.md`](../02-discovery/mvp-framing.md). This is the only document you write by hand. |
| **Then** | Open [Stage 2 — Discovery](../02-discovery/README.md) |
| **Helper for Stage 2** | `BRD Builder` — not `RPI Agent` |
| **It will produce** | `docs/project-planning/<name>-brd.md` |

The map of all nine stages is in the [main README](../../README.md).
