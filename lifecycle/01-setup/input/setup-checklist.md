# Stage 1 — Setup

Get the tools working before you think about features.

| | |
| --- | --- |
| **What you do** | Install the AI helpers and confirm they appear |
| **Produces** | [`../output/setup-confirmation.md`](../output/setup-confirmation.md), filled in |
| **Takes** | About fifteen minutes |

---

## 1. What this stage is for

Everything else in this kit depends on a set of specialist AI helpers being available inside VS Code. This stage installs them and proves they are there.

Nothing about your product happens here. No requirements, no code — just tools.

## 2. Prerequisites

| Thing | Why |
| --- | --- |
| **VS Code** | The editor everything runs inside |
| **GitHub Copilot** | The AI, with Chat enabled and signed in |
| **This repository, on your machine** | You already have it if you can read this file |
| **Git** | To save your work and, later, publish a release |
| **A GitHub account** | Optional but recommended — Stage 4 creates tasks there |

You do **not** need to have chosen a programming language. That is decided in Stage 3, and written down as an ADR.

---

## 3. Install and check

Work top to bottom. Record what happened in [`../output/setup-confirmation.md`](../output/setup-confirmation.md) as you go.

### 3.1 The editor and Copilot

- Open this repository as the folder in VS Code — **File → Open Folder**, and choose the project's top-level folder, not a subfolder
- Open Copilot Chat: click the chat icon in the left Activity Bar, or press `Ctrl+Alt+I` (`Cmd+Alt+I` on a Mac)
- Type "hello" in the chat and confirm you get a reply — if not, you are not signed in to Copilot

### 3.2 Install the helpers

- Open the Extensions panel: the squares icon in the left Activity Bar, or `Ctrl+Shift+X`
- Search for **HVE Core - All**, or [install it from the marketplace](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)
- Click **Install**
- **Reload VS Code afterwards** — the helpers do not appear until you do. Open the Command Palette with `Ctrl+Shift+P` and run *Developer: Reload Window*

### 3.3 Confirm the helpers appear

In Copilot Chat, click the mode dropdown at the bottom of the chat box. You should see a longer list than before. Look for:

- `BRD Builder` — used in Stage 2
- `PRD Builder` — used in Stage 3
- `ADR Creation` — used in Stage 3
- `GitHub Backlog Manager` — used in Stages 4, 5, and 6
- `RPI Agent` — used in Stage 6
- `Task Reviewer` — used in Stages 6 and 7
- `Functional code-review` — used in Stage 7
- `Doc Ops` — used in Stage 9

Names vary slightly between versions of the extension, and the dropdown may show them in Title Case where this kit writes them in lowercase. If one is missing but something obviously equivalent is there, use that and note it in the confirmation file. If the list did not change at all, the extension is not installed or VS Code was not reloaded.

### 3.4 Check the folders are in place

These should already exist. You are just confirming nothing is missing:

- `lifecycle/` — the nine stages
- `lifecycle/02-discovery/input/mvp-framing.md` — the file you fill in next
- `src/` and `tests/` — empty for now; Stage 6 fills them
- `GLOSSARY.md` — plain-English definitions of every term
- `.copilot-tracking/` — where the helpers keep their working notes (you rarely open it; Stage 7 review reads it)

### 3.5 Check Git works

Open a terminal in VS Code (**Terminal → New Terminal**) and run:

```bash
git status
```

- It runs without an error and tells you which branch you are on
- You are on your own branch, not `template` — if you are still on `template`, run `git checkout -b my-project-main` first

### 3.6 Your language and tools — later, not now

You do not install a programming language yet. Stage 3 decides which one, and records the choice as an ADR. Stage 6 will tell you what to install before any code is written.

If you already know what you will use, note it in section 4 of your [framing document](../../02-discovery/input/mvp-framing.md) under "Stack intent". Stage 3 will take it into account rather than re-opening the question.

---

## 4. Done when

| Finished | Not yet |
| --- | --- |
| HVE Core - All is installed and the helpers appear in the dropdown | Any requirements written |
| `git status` runs cleanly and you are on your own branch | Any code written |
| The folders above all exist | Any tasks created |
| `../output/setup-confirmation.md` is filled in | Any use of `RPI Agent` |

## 5. What next

| Step | Action |
| --- | --- |
| **Now** | Fill in [`../output/setup-confirmation.md`](../output/setup-confirmation.md) |
| **Then** | Write your idea into [`../../02-discovery/input/mvp-framing.md`](../../02-discovery/input/mvp-framing.md) — the only document you write by hand |
| **Then** | Open [Stage 2 — Discovery](../../02-discovery/README.md) and pick `brd-builder` |

The full story of the kit, including why the process exists and the map of all nine stages, is in the [main README](../../../README.md).
