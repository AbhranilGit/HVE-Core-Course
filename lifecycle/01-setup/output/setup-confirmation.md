# Stage 1 — Setup confirmation

Fill this in as you work through [`../input/setup-checklist.md`](../input/setup-checklist.md). It is your proof that the tools work, so that when something misbehaves in Stage 6 you know it is not the setup.

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
| Repository opened as the folder in VS Code | ☐ Pass / ☐ Fail | |
| Copilot Chat opens and replies | ☐ Pass / ☐ Fail | |
| **HVE Core - All** installed | ☐ Pass / ☐ Fail | Extension id: `ise-hve-essentials.hve-core-all` |
| VS Code reloaded after installing | ☐ Pass / ☐ Fail | |

## 2. The helpers

Tick the ones you can see in the mode dropdown. Names vary slightly between versions — if yours differ, write down what you actually see.

| Helper | Visible? | Used in | Name in your version, if different |
| --- | --- | --- | --- |
| `brd-builder` | ☐ Yes / ☐ No | Stage 2 | |
| `prd-builder` | ☐ Yes / ☐ No | Stage 3 | |
| `adr-creation` | ☐ Yes / ☐ No | Stage 3 | |
| `github-backlog-manager` | ☐ Yes / ☐ No | Stages 4, 5 | |
| `RPI Agent` | ☐ Yes / ☐ No | Stage 6 | |
| A review helper | ☐ Yes / ☐ No | Stage 7 | |
| A documentation helper | ☐ Yes / ☐ No | Stage 9 | |

If `brd-builder` or `RPI Agent` are missing, stop and fix that before going further. Those two are not optional.

## 3. The folders

| Path | There? |
| --- | --- |
| `lifecycle/` | ☐ Yes / ☐ No |
| `lifecycle/02-discovery/input/mvp-framing.md` | ☐ Yes / ☐ No |
| `src/` | ☐ Yes / ☐ No |
| `tests/` | ☐ Yes / ☐ No |
| `docs/guides/` | ☐ Yes / ☐ No |
| `.copilot-tracking/` | ☐ Yes / ☐ No |

## 4. Git

| Check | Result | Notes |
| --- | --- | --- |
| `git status` runs without error | ☐ Pass / ☐ Fail | |
| You are on your own branch, not `template` | ☐ Pass / ☐ Fail | Branch name: |
| Repository exists on GitHub | ☐ Yes / ☐ No / ☐ Not using GitHub | Needed for Stage 4 issues; there is a fallback if not |

Paste what `git status` printed:

```text
_paste here_
```

## 5. Anything unusual

| What | Does it matter? | What you did about it |
| --- | --- | --- |
| _nothing, or describe_ | | |

## 6. Ready to continue?

| Gate | Met? |
| --- | --- |
| The helpers needed for Stages 2 and 6 are visible | ☐ |
| The folders are all present | ☐ |
| Git works and you are on your own branch | ☐ |
| Nothing is blocking you from opening `brd-builder` | ☐ |

**Stage 1 complete:** ☐ Yes — continue · ☐ No — fix the failures above first

---

## 7. What next

| Step | Action |
| --- | --- |
| **Now** | Write your idea into [`../../02-discovery/input/mvp-framing.md`](../../02-discovery/input/mvp-framing.md). This is the only document you write by hand. |
| **Then** | Open [Stage 2 — Discovery](../../02-discovery/prompt/README.md) |
| **Helper for Stage 2** | `brd-builder` — not `RPI Agent` |
| **It will produce** | `lifecycle/02-discovery/output/brd.md` |

Track your progress in [CHECKLIST.md](../../CHECKLIST.md).
