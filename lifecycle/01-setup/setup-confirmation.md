# Stage 1 — Setup confirmation

Fill this in as you work through [`README.md`](README.md). It is your proof that
the tooling works, so that when something misbehaves in week six you know it is
not the setup. It is also the first thing to hand a colleague who picks the
engagement up from you.

| Field | Value |
| --- | --- |
| **Engagement** | `<name, from the engagement brief>` |
| **Customer** | `<organisation>` |
| **Status** | Not started |
| **Confirmed by** | `<you>` |
| **Confirmed on** | `<YYYY-MM-DD>` |

---

## 1. Where the work lives

| Check | Value or result | Notes |
| --- | --- | --- |
| Working repository | | The one you will actually commit to |
| Existing repo, or new for this engagement? | | 3a or 3b in the README |
| Scaffolding merged into it | | PR link, if it went through review |
| Their `.gitignore` covers `.copilot-tracking/` | | |
| Merged with an existing `copilot-instructions.md`, rather than overwriting | | N/A if they had none |
| Their `docs/` layout differs from HVE defaults | | If yes, say how — later stages assume the defaults |

## 2. Access

| Check | Result | Notes |
| --- | --- | --- |
| Repository access, with push rights | | |
| Tracker access | | Azure DevOps, GitHub, or Jira |
| Tracker MCP server connected in VS Code | | Stage 4 is blocked without this |
| Environment or subscription access | | If the work needs it |
| Anything still pending | | What, requested from whom, on what date |

## 3. Copilot and the helpers

| Check | Result | Notes |
| --- | --- | --- |
| Copilot Chat replies | | |
| **HVE Core - All** installed | | `ise-hve-essentials.hve-core-all` |
| Installed via marketplace, or the installer skill? | | Skill path if their policy blocks extensions |
| VS Code reloaded | | |
| **Extension version** | | This kit targets `3.3.101` |

Write `Yes` or `No` for each helper in the mode dropdown. If your version names
one differently, record what you actually see.

| Helper | Visible? | Used in | Name in your version, if different |
| --- | --- | --- | --- |
| **BRD Builder** | | Stage 2 | |
| **RAI Planner** | | Stage 2, if required | |
| **Security Planner** | | Stage 2, if required | |
| **SSSC Planner** | | Stage 2, if required | |
| **PRD Builder** | | Stage 3 | |
| **ADR Creation** | | Stage 3 | |
| **ADO Backlog Manager** | | Stages 4, 5, 6 | |
| **GitHub Backlog Manager** | | Stages 4, 5, 6, if GitHub | |
| **Task Researcher** | | Stage 6 | |
| **Task Planner** | | Stage 6 | |
| **Task Implementor** | | Stage 6 | |
| **Task Reviewer** | | Stages 6 and 7 | |
| **Code Review Full** | | Stage 7 | |
| **Security Reviewer** | | Stage 7, if required | |
| **PR Review** | | Stage 8 | |
| **Doc Ops** | | Stage 9 | |

## 4. Slash commands

| Command | There? | Used in |
| --- | --- | --- |
| `/git-setup` | | Stage 1 |
| `/ado-discover-work-items` or `/github-discover-issues` | | Stage 4 |
| `/ado-update-wit-items` or `/github-execute-backlog` | | Stage 4 |
| `/ado-sprint-plan` or `/github-sprint-plan` | | Stage 5 |
| `/task-research` | | Stage 6 |
| `/task-plan` | | Stage 6 |
| `/task-implement` | | Stage 6 |
| `/task-review` | | Stages 6 and 7 |
| `/security-capture`, `/security-plan-from-prd` | | Stages 2 and 3, if required |
| `/rai-capture`, `/rai-plan-from-prd` | | Stages 2 and 3, if required |
| `/sssc-from-brd` | | Stage 2, if required |
| `/code-review-full` | | Stage 7 |
| `/security-review` | | Stage 7, if required |
| `/ado-create-pull-request` or `/pull-request` | | Stage 8 |
| `/git-merge` | | Stage 8 |
| `/doc-ops-update` | | Stage 9 |
| `/incident-response` | | Stage 9 |

## 5. Git identity

| Check | Result | Notes |
| --- | --- | --- |
| `/git-setup` ran without error | | |
| `user.email` is the identity the customer expects in their history | | |
| Signed commits required by the customer? | | If yes, signing configured and verified |
| `git status` runs cleanly on your branch | | Branch name: |

## 6. The stack you are inheriting

Read these out of the repository, not out of a conversation. Copy them into
`.github/copilot-instructions.md` when confirmed.

| Field | Value | Where you found it |
| --- | --- | --- |
| Language and version | | |
| Framework | | |
| Data storage | | |
| Install command | | |
| Run command | | |
| Test command | | |
| Application code path | | Theirs, not necessarily `src/` |
| Test path | | Theirs, not necessarily `tests/` |
| Documented coding conventions | | Or "none found" |
| CI system and pipeline file | | |

**Did you run their test command yourself?** `<yes / no>`
**Did it pass on a clean checkout?** `<yes / no — and what failed>`

> A failing or missing test suite on day one is not a blocker, but it is a
> finding. Record it here, raise it with the technical contact, and expect it to
> shape the first iteration.

## 7. Anything unusual

| What | Does it matter? | What you did about it |
| --- | --- | --- |
| _nothing, or describe_ | | |

## 8. Ready to continue?

| Gate | Met? |
| --- | --- |
| You can commit to the working repository | |
| The helpers needed for Stages 2 and 6 are visible | |
| The tracker's MCP server is connected | |
| Your commit identity is correct for this customer | |
| The inherited stack is recorded, and you have run their tests | |

**Stage 1 complete:** Yes / No — if No, fix the failures above first.

---

## 9. What next

| Step | Action |
| --- | --- |
| **Now** | Transcribe the statement of work into [`../02-discovery/scope-framing.md`](../02-discovery/scope-framing.md) |
| **Then** | Open [Stage 2 — Discovery](../02-discovery/README.md) |
| **Helper for Stage 2** | `BRD Builder` |
| **It will produce** | `docs/brds/<name>-brd.md` |
