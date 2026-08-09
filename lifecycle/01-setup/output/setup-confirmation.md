# Stage 1 — Setup confirmation

Fill this in as you work through [`../input/setup-checklist.md`](../input/setup-checklist.md). It is your proof that the tools work, so that when something misbehaves in Stage 6 you know it is not the setup.

Write short answers in the blank cells — `Pass`, `Fail`, `Yes`, `No`, or a note. You do not need to tick anything.

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

Write `Yes` or `No` for each helper you can see in the mode dropdown. Names vary slightly between versions — if yours differ, write down what you actually see.

| Helper | Visible? | Used in | Name in your version, if different |
| --- | --- | --- | --- |
| `BRD Builder` | | Stage 2 | |
| `PRD Builder` | | Stage 3 | |
| `ADR Creation` | | Stage 3 | |
| `GitHub Backlog Manager` | | Stages 4, 5, 6 | |
| `RPI Agent` | | Stage 6 | |
| `Task Reviewer` | | Stages 6, 7 | |
| `Functional code-review` | | Stage 7 | |
| `Doc Ops` | | Stage 9 | |

If `BRD Builder` or `RPI Agent` are missing, stop and fix that before going further. Those two are not optional.

## 3. The folders

| Path | There? |
| --- | --- |
| `lifecycle/` | |
| `lifecycle/02-discovery/input/mvp-framing.md` | |
| `src/` | |
| `tests/` | |
| `GLOSSARY.md` | |
| `.copilot-tracking/` | |

## 4. Git

| Check | Result | Notes |
| --- | --- | --- |
| `git status` runs without error | | |
| You are on your own branch, not `template` | | Branch name: |
| Repository exists on GitHub | | Needed for Stage 4 issues; there is a fallback if not |

Paste what `git status` printed:

```text
_paste here_
```

## 5. Anything unusual

| What | Does it matter? | What you did about it |
| --- | --- | --- |
| _nothing, or describe_ | | |

## 6. Ready to continue?

Write `Yes` only when each row is true.

| Gate | Met? |
| --- | --- |
| The helpers needed for Stages 2 and 6 are visible | |
| The folders are all present | |
| Git works and you are on your own branch | |
| Nothing is blocking you from opening `brd-builder` | |

**Stage 1 complete:** Yes / No — if No, fix the failures above first.

---

## 7. What next

| Step | Action |
| --- | --- |
| **Now** | Write your idea into [`../../02-discovery/input/mvp-framing.md`](../../02-discovery/input/mvp-framing.md). This is the only document you write by hand. |
| **Then** | Open [Stage 2 — Discovery](../../02-discovery/README.md) |
| **Helper for Stage 2** | `brd-builder` — not `RPI Agent` |
| **It will produce** | `lifecycle/02-discovery/output/brd.md` |

The map of all nine stages is in the [main README](../../../README.md).
