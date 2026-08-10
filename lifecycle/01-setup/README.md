# Stage 1 — Setup

Get the tooling working, and get this scaffolding into the repository you will
actually be working in.

| | |
| --- | --- |
| **What you do** | Install the helpers, decide where the code lives, and record what you are inheriting |
| **Produces** | [`setup-confirmation.md`](setup-confirmation.md) filled in, and [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) describing the customer's project |
| **Helpers** | None yet — this stage is by hand, plus one slash command |
| **Takes** | Half a day, most of it waiting for access |

---

## 1. What this stage is for

Two jobs. Install the specialist AI helpers everything else depends on, and work
out where this scaffolding lives relative to the customer's code.

Nothing about the product happens here. No requirements, no code.

## 2. Prerequisites

| Thing | Why |
| --- | --- |
| **[Stage 0](../00-engagement/README.md) done** | Section 5 of the engagement brief tells you what you are inheriting, and this stage checks it |
| **VS Code** | The editor everything runs inside |
| **GitHub Copilot** | The AI, with Chat enabled and signed in |
| **Git** | Obviously |
| **Access to the customer's repository** | Usually the long pole. Ask on day one |
| **Access to their tracker** | Azure DevOps project, GitHub repo, or Jira, as recorded in the brief |

## 3. Decide where this scaffolding lives

This is the decision that shapes the rest of the engagement, and it comes down
to whether the code already exists.

### 3a. You are joining an existing repository

The common case. The customer has a codebase and you are adding to it.

Do not restructure their repository around this template. Copy in only the parts
that carry the process, and leave everything else exactly as you found it:

```bash
# From a clone of this template, into a clone of theirs
cp -r lifecycle/            <their-repo>/
cp -r docs/                 <their-repo>/
cp    .github/copilot-instructions.md <their-repo>/.github/
```

Three things to check before you commit that:

- **They may already have `.github/copilot-instructions.md`.** If so, merge rather than overwrite. Their conventions win on anything that conflicts with this template's defaults; you are a guest in their standards.
- **They may already have a `docs/` folder with a different shape.** Keep theirs. Add only the subfolders you need, and note the divergence from HVE's defaults in your setup confirmation so later stages do not surprise you.
- **Their `.gitignore` needs the `.copilot-tracking/` rules** from this template's, or the AI's working notes will end up in their history.

Open a pull request for this scaffolding on its own, before any product work.
It is small, it is easy to review, and it is the customer's first chance to
object to the process rather than discovering it embedded in a feature branch.

### 3b. The engagement creates a new repository

Less common, but simpler. Use this template as the starting point:

```bash
git clone <this-repo-url> <engagement-name>
cd <engagement-name>
git checkout template-fde
git checkout -b main
```

Then push it to wherever section 8 of the engagement brief says the repository
will live. Do that on day one, not at handover — a repository that has lived in
the customer's organisation from the start avoids an awkward migration later.

## 4. Install and check

Work top to bottom. Record what happened in
[`setup-confirmation.md`](setup-confirmation.md) as you go.

### 4.1 Copilot

- Open the working repository as the folder in VS Code — **File → Open Folder**, at the top level
- Open Copilot Chat: the chat icon in the left Activity Bar, or `Ctrl+Alt+I` (`Cmd+Alt+I` on a Mac)
- Confirm it replies

### 4.2 Install the helpers

- Open the Extensions panel, or press `Ctrl+Shift+X`
- Search for **HVE Core - All**, or [install it from the marketplace](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)
- Install, then **reload VS Code** — the helpers do not appear until you do

**HVE Core - All** is the full bundle and is what this kit assumes. There is also
a smaller **HVE Core** package. Install one or the other, never both.

If the customer's policy blocks marketplace extensions — which happens more often
than you would like — HVE Core ships an installer skill for clone-based adoption.
Ask any helper:

```text
Help me customize hve-core installation for this repository.
```

That path commits the prompts and agents into the repository itself, which has
the side benefit that the customer's engineers get them without installing
anything. Weigh that against the noise it adds to their tree.

### 4.3 Check the version

This kit is written against **3.3.101**. Helper names and slash commands move
between HVE Core releases, and that is the most common reason a stage page stops
matching what you see. Record your version in the confirmation file.

### 4.4 Confirm the helpers appear

| Helper | Used in | How you reach it |
| --- | --- | --- |
| **BRD Builder** | Stage 2 | Mode dropdown |
| **RAI Planner**, **Security Planner**, **SSSC Planner** | Stage 2, where your obligations require them | Mode dropdown |
| **PRD Builder** | Stage 3 | Mode dropdown |
| **ADR Creation** | Stage 3 | Mode dropdown |
| **ADO Backlog Manager** | Stages 4, 5, 6 | Dropdown, or any `/ado-*` command |
| **GitHub Backlog Manager** | Stages 4, 5, 6, if they use GitHub | Dropdown, or any `/github-*` command |
| **Task Researcher**, **Task Planner**, **Task Implementor**, **Task Reviewer** | Stages 6 and 7 | The `/task-*` commands |
| **Code Review Full** | Stage 7 | `/code-review-full` |
| **Security Reviewer** | Stage 7, where required | `/security-review` |
| **PR Review** | Stage 8 | Mode dropdown |
| **Doc Ops** | Stage 9 | `/doc-ops-update` |

Most of these you never pick by hand — a slash command carries its own helper.
Only `BRD Builder`, `PRD Builder`, `ADR Creation`, `PR Review`, and the Stage 2
planners need the dropdown.

### 4.5 Confirm the slash commands

Type `/` in the chat box. This kit uses:

`/git-setup` · `/ado-discover-work-items` · `/ado-update-wit-items` ·
`/ado-sprint-plan` · `/ado-create-pull-request` · `/task-research` ·
`/task-plan` · `/task-implement` · `/task-review` · `/code-review-full` ·
`/security-review` · `/pull-request` · `/git-merge` · `/doc-ops-update` ·
`/incident-response`

Swap the `/ado-*` commands for `/github-*` if the customer uses GitHub Issues.

Where your compliance obligations apply, you will also need `/security-capture`,
`/security-plan-from-prd`, `/rai-capture`, `/rai-plan-from-prd`, and
`/sssc-from-brd`.

If you see `/rpi-research` and `/rpi-plan` instead of the `/task-*` commands, you
are on a newer HVE Core than this kit targets. The four phases are unchanged;
only the names moved.

### 4.6 Connect the tracker

Stages 4 and 5 work entirely through MCP tools, so the relevant MCP server has to
be connected in VS Code before you get there:

- **Azure DevOps** — the Azure DevOps MCP server, authenticated against their organisation
- **GitHub** — the GitHub MCP server
- **Jira** — the Jira integration

Customer tenants frequently require an access request for this. Start it now;
Stage 4 is blocked without it.

### 4.7 Configure Git

```text
/git-setup
```

It reads your Git configuration, shows a table of what is set, and **asks before
changing anything**. Note that it proposes **global** settings, so your answers
affect every project on this machine.

Two things matter more than usual on customer work. Check that your `user.email`
is the identity the customer expects to see in their history — a personal address
in a corporate repository causes awkward questions at audit time. And if the
customer requires signed commits, this is where you sort that out; tell
`/git-setup` you want signing and it will walk you through GPG or SSH.

### 4.8 Record what you are inheriting

Open [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md)
and fill in the **Project** and **Stack** tables.

This differs from a greenfield project in an important way. On a new product the
stack is undecided until Stage 3. Here, most of it already exists and you are
**recording** it, not choosing it. Read it out of the repository rather than
asking the customer:

- The language and version, from their build or dependency files
- The framework, from their imports and project layout
- The test command that actually works, from their CI configuration — and run it yourself before you write it down
- Their coding conventions, if documented

Anything genuinely undecided gets a decision record in Stage 3. Anything already
decided gets recorded here as inherited, and Stage 3 documents it as a constraint
rather than reopening it.

### 4.9 Check the folders

- `lifecycle/` — the stage pages, including [Stage 0](../00-engagement/README.md)
- `lifecycle/02-discovery/scope-framing.md` — you fill this in next
- `docs/brds/`, `docs/prds/`, `docs/decisions/` — HVE Core's default locations
- `docs/planning/`, `docs/reviews/`, `docs/releases/`, `docs/operations/`
- `.copilot-tracking/` — the helpers' working notes

In an existing repository, the application code lives wherever it already lives.
Do not create `src/` and `tests/` alongside their equivalents; record their real
paths in `copilot-instructions.md` instead.

---

## 5. Done when

| Finished | Not yet |
| --- | --- |
| The scaffolding is in the working repository, merged or in review | Any requirements written |
| HVE Core - All is installed and the helpers appear | Any code written |
| You have recorded which version you have | Any work items created |
| The tracker's MCP server is connected | Any use of the task helpers |
| `/git-setup` has run and your commit identity is the one the customer expects | |
| `copilot-instructions.md` records the inherited stack, and you have run their test command yourself | |
| [`setup-confirmation.md`](setup-confirmation.md) is filled in | |

## 6. What next

| Step | Action |
| --- | --- |
| **Now** | Fill in [`setup-confirmation.md`](setup-confirmation.md) |
| **Then** | Transcribe the statement of work into [`../02-discovery/scope-framing.md`](../02-discovery/scope-framing.md) |
| **Then** | Open [Stage 2 — Discovery](../02-discovery/README.md) and pick `BRD Builder` |

The map of the whole lifecycle is in the [main README](../../README.md).
