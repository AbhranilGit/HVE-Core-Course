# Stage 1 — Setup

Get the tools working before you think about features.

| | |
| --- | --- |
| **What you do** | Install the AI helpers, confirm they appear, and record your project's conventions |
| **Produces** | [`setup-confirmation.md`](setup-confirmation.md) filled in, and [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) with your project name |
| **Helpers** | None yet — this stage is by hand, plus one slash command |
| **Takes** | About fifteen minutes |

---

## 1. What this stage is for

Everything else in this kit depends on a set of specialist AI helpers being
available inside VS Code. This stage installs them, proves they are there, and
writes down the handful of conventions every later helper will read.

Nothing about your product happens here. No requirements, no code — just tools.

## 2. Prerequisites

| Thing | Why |
| --- | --- |
| **VS Code** | The editor everything runs inside |
| **GitHub Copilot** | The AI, with Chat enabled and signed in |
| **This repository, on your machine** | You already have it if you can read this file |
| **Git** | To save your work and, later, publish a release |
| **A GitHub account** | Recommended — Stage 4 creates tasks there. Azure DevOps and Jira also work; see Stage 4 |
| **The GitHub MCP server** | Only if you use GitHub Issues. Stage 4 works entirely through it, so connect it in VS Code before you get there |

You do **not** need to have chosen a programming language. That is decided in
Stage 3 and recorded as an ADR.

---

## 3. Install and check

Work top to bottom. Record what happened in
[`setup-confirmation.md`](setup-confirmation.md) as you go.

### 3.1 The editor and Copilot

- Open this repository as the folder in VS Code — **File → Open Folder**, and choose the project's top-level folder, not a subfolder
- Open Copilot Chat: click the chat icon in the left Activity Bar, or press `Ctrl+Alt+I` (`Cmd+Alt+I` on a Mac)
- Type "hello" in the chat and confirm you get a reply — if not, you are not signed in to Copilot

### 3.2 Install the helpers

- Open the Extensions panel: the squares icon in the left Activity Bar, or `Ctrl+Shift+X`
- Search for **HVE Core - All**, or [install it from the marketplace](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)
- Click **Install**
- **Reload VS Code afterwards** — the helpers do not appear until you do. Open the Command Palette with `Ctrl+Shift+P` and run *Developer: Reload Window*

**HVE Core - All** is the full bundle and is what this kit assumes. There is
also a smaller **HVE Core** package. Install one or the other, never both —
they share content and will conflict.

Prefer not to use the extension? HVE Core ships an installer skill for
clone-based adoption. Ask any helper:

```text
Help me customize hve-core installation for this repository.
```

### 3.3 Check the version

Open the extension's page in VS Code and look at the **Version** field.

This kit is written against **3.3.101**. Helper names and slash commands change
between HVE Core releases — that is the single most common reason a stage page
stops matching what you see. Write your version into the confirmation file. If it
is not 3.3.101, work through the stages expecting some names to differ, and note
each difference as you find it.

### 3.4 Confirm the helpers appear

In Copilot Chat, click the mode dropdown at the bottom of the chat box. You
should see a much longer list than before. These are the ones this kit names,
spelled exactly as they appear in 3.3.101:

| Helper | Used in | How you reach it |
| --- | --- | --- |
| **BRD Builder** | Stage 2 | Mode dropdown |
| **PRD Builder** | Stage 3 | Mode dropdown |
| **ADR Creation** | Stage 3 | Mode dropdown |
| **GitHub Backlog Manager** | Stages 4, 5, 6 | Dropdown, or any `/github-*` command |
| **Task Researcher** | Stage 6 | `/task-research` |
| **Task Planner** | Stage 6 | `/task-plan` |
| **Task Implementor** | Stage 6 | `/task-implement` |
| **Task Reviewer** | Stages 6 and 7 | `/task-review` |
| **Code Review Full** | Stage 7 | `/code-review-full` |
| **Security Reviewer** | Stage 7, if it applies | `/security-review` |
| **PR Review** | Stage 8 | Mode dropdown |
| **Doc Ops** | Stage 9 | `/doc-ops-update` |

Most of these you never pick by hand. A slash command carries its own helper, so
typing `/task-plan` switches to `Task Planner` for you. Only `BRD Builder`,
`PRD Builder`, `ADR Creation`, and `PR Review` need the dropdown.

If the list did not change at all, the extension is not installed or VS Code was
not reloaded.

### 3.5 Confirm the slash commands work

Type `/` in the chat box. You should see a list of commands. This kit uses:

`/git-setup` · `/github-discover-issues` · `/github-execute-backlog` ·
`/github-sprint-plan` · `/task-research` · `/task-plan` · `/task-implement` ·
`/task-review` · `/code-review-full` · `/pull-request` · `/git-merge` ·
`/doc-ops-update` · `/incident-response`

You do not need to run any of them yet. You are only confirming they exist.

If you see `/rpi-research`, `/rpi-plan`, or `/rpi-implement` instead of the
`/task-*` commands, you are on a newer HVE Core than this kit targets. The four
phases are the same; only the names moved.

### 3.6 Configure Git

Run this in the chat, with any helper selected:

```text
/git-setup
```

It reads your Git configuration, shows you a table of what is set and what is
missing, and then **asks before changing anything**. Expect a yes/no question per
group of fixes; anything other than an explicit yes is treated as no.

Two things to know before you answer:

- It proposes **global** settings, so your answers affect every project on this machine, not just this one.
- It only volunteers help with your identity (`user.name` and `user.email`, which Git will not let you commit without) and with wiring VS Code up as your editor and diff tool. Commit signing and `safe.directory` are shown in the table but left alone unless you bring them up.

It will not touch this repository — no commits, no branches, no remotes.

Then open a terminal in VS Code (**Terminal → New Terminal**) and run:

```bash
git status
```

- It runs without an error and tells you which branch you are on
- You are on your own branch, not `template` — if you are still on `template`, run `git checkout -b my-project-main` first

### 3.7 Record your project's conventions

Open [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md)
and fill in the **Project** table: your project's name and a one-line
description. Leave the **Stack** table alone — Stage 3 fills that in once your
ADRs exist.

This is the file every helper reads on every request. It is how a template
becomes *your* project.

### 3.8 Check the folders are in place

These should already exist. You are just confirming nothing is missing:

- `lifecycle/` — the nine stage pages
- `lifecycle/02-discovery/mvp-framing.md` — the file you fill in next
- `docs/brds/`, `docs/prds/`, and `docs/decisions/` — where your BRD, PRD, and decision records will land
- `docs/planning/` — where your sprint plan will land
- `src/` and `tests/` — empty for now; Stage 6 fills them
- `.copilot-tracking/` — where the helpers keep their working notes

### 3.9 Your language and tools — later, not now

You do not install a programming language yet. Stage 3 decides which one and
records the choice as an ADR. Stage 6 tells you what to install before any code
is written.

If you already know what you will use, note it in the **Stack intent** row at
the top of your [framing document](../02-discovery/mvp-framing.md). Stage 3 will
take it into account rather than re-opening the question.

---

## 4. Done when

| Finished | Not yet |
| --- | --- |
| HVE Core - All is installed and the helpers appear in the dropdown | Any requirements written |
| You have written down which version you have | Any code written |
| The slash commands appear when you type `/` | Any tasks created |
| `/git-setup` has run and `git status` is clean on your own branch | Any use of the task helpers |
| `.github/copilot-instructions.md` names your project | |
| [`setup-confirmation.md`](setup-confirmation.md) is filled in | |

## 5. What next

| Step | Action |
| --- | --- |
| **Now** | Fill in [`setup-confirmation.md`](setup-confirmation.md) |
| **Then** | Write your idea into [`../02-discovery/mvp-framing.md`](../02-discovery/mvp-framing.md) — the only document you write by hand |
| **Then** | Open [Stage 2 — Discovery](../02-discovery/README.md) and pick `BRD Builder` |

The full story of the kit, including the map of all nine stages, is in the
[main README](../../README.md).
