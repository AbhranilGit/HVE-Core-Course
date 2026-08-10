# Stage 1 — Setup confirmation (sample)

Example of a filled-in [`setup-confirmation.md`](setup-confirmation.md) for a fictional Contoso engagement. Copy the shape, not the facts — fill the real file as you work through [`README.md`](README.md).

| Field | Value |
| --- | --- |
| **Engagement** | nightly-ingest-enablement |
| **Customer** | Contoso Manufacturing |
| **Status** | Complete |
| **Confirmed by** | A. Engineer |
| **Confirmed on** | 2026-08-10 |

---

## 1. Where the work lives

| Check | Value or result | Notes |
| --- | --- | --- |
| Working repository | `https://dev.azure.com/contoso/Manufacturing/_git/nightly-ingest` | The one you will actually commit to |
| Existing repo, or new for this engagement? | Existing (3a) | Joining their ingest service repo |
| Scaffolding merged into it | [PR #412](https://dev.azure.com/contoso/Manufacturing/_git/nightly-ingest/pullrequest/412) | Scaffolding-only PR, merged 2026-08-08 |
| Their `.gitignore` covers `.copilot-tracking/` | Yes | Added in PR #412 |
| Merged with an existing `copilot-instructions.md`, rather than overwriting | Yes | Kept their naming notes; added Engagement and Stack tables from this kit |
| Their `docs/` layout differs from HVE defaults | Partially | They already had `docs/architecture/`; HVE folders added alongside, not relocated |

## 2. Access

| Check | Result | Notes |
| --- | --- | --- |
| Repository access, with push rights | Yes | Contributor on `Manufacturing` project |
| Tracker access | Yes | Azure DevOps Boards on the same project |
| Tracker MCP server connected in VS Code | Yes | Azure DevOps MCP; can list work items |
| Environment or subscription access | Yes | Read on Contoso-Prod; Contributor on Contoso-Dev |
| Anything still pending | Prod deploy approvals | Requested from Priya (tech contact) on 2026-08-09 — not blocking Stages 2–6 |

## 3. Copilot and the helpers

| Check | Result | Notes |
| --- | --- | --- |
| Copilot Chat replies | Yes | |
| **HVE Core - All** installed | Yes | `ise-hve-essentials.hve-core-all` |
| Installed via marketplace, or the installer skill? | Marketplace | Contoso allowlists the publisher |
| VS Code reloaded | Yes | |
| **Extension version** | 3.3.101 | This kit targets `3.3.101` |

Write `Yes` or `No` for each helper in the mode dropdown. If your version names one differently, record what you actually see.

| Helper | Visible? | Used in | Name in your version, if different |
| --- | --- | --- | --- |
| **BRD Builder** | Yes | Stage 2 | |
| **RAI Planner** | Yes | Stage 2, if required | |
| **Security Planner** | Yes | Stage 2, if required | |
| **SSSC Planner** | Yes | Stage 2, if required | |
| **PRD Builder** | Yes | Stage 3 | |
| **ADR Creation** | Yes | Stage 3 | |
| **ADO Backlog Manager** | Yes | Stages 4, 5, 6 | |
| **GitHub Backlog Manager** | Yes | Stages 4, 5, 6, if GitHub | Not used — tracker is ADO |
| **Task Researcher** | Yes | Stage 6 | |
| **Task Planner** | Yes | Stage 6 | |
| **Task Implementor** | Yes | Stage 6 | |
| **Task Reviewer** | Yes | Stages 6 and 7 | |
| **Code Review Full** | Yes | Stage 7 | |
| **Security Reviewer** | Yes | Stage 7, if required | |
| **PR Review** | Yes | Stage 8 | |
| **Doc Ops** | Yes | Stage 9 | |

## 4. Slash commands

| Command | There? | Used in |
| --- | --- | --- |
| `/git-setup` | Yes | Stage 1 |
| `/ado-discover-work-items` or `/github-discover-issues` | Yes (`/ado-discover-work-items`) | Stage 4 |
| `/ado-update-wit-items` or `/github-execute-backlog` | Yes (`/ado-update-wit-items`) | Stage 4 |
| `/ado-sprint-plan` or `/github-sprint-plan` | Yes (`/ado-sprint-plan`) | Stage 5 |
| `/task-research` | Yes | Stage 6 |
| `/task-plan` | Yes | Stage 6 |
| `/task-implement` | Yes | Stage 6 |
| `/task-review` | Yes | Stages 6 and 7 |
| `/security-capture`, `/security-plan-from-prd` | Yes | Stages 2 and 3, if required |
| `/rai-capture`, `/rai-plan-from-prd` | Yes | Stages 2 and 3, if required |
| `/sssc-from-brd` | Yes | Stage 2, if required |
| `/code-review-full` | Yes | Stage 7 |
| `/security-review` | Yes | Stage 7, if required |
| `/ado-create-pull-request` or `/pull-request` | Yes (`/ado-create-pull-request`) | Stage 8 |
| `/git-merge` | Yes | Stage 8 |
| `/doc-ops-update` | Yes | Stage 9 |
| `/incident-response` | Yes | Stage 9 |

## 5. Git identity

| Check | Result | Notes |
| --- | --- | --- |
| `/git-setup` ran without error | Yes | |
| `user.email` is the identity the customer expects in their history | Yes | `a.engineer@contoso.com` (guest on Contoso tenant) |
| Signed commits required by the customer? | No | Contoso does not require signed commits on this repo |
| `git status` runs cleanly on your branch | Yes | Branch name: `main` |

## 6. The stack you are inheriting

Read these out of the repository, not out of a conversation. Copy them into `.github/copilot-instructions.md` when confirmed.

| Field | Value | Where you found it |
| --- | --- | --- |
| Language and version | Python 3.12 | `.python-version`, `pyproject.toml` |
| Framework | FastAPI 0.115, Pydantic v2 | `requirements.txt`, `app/main.py` |
| Data storage | Azure Cosmos DB (SQL API) + Azure Blob Storage | `app/dependencies.py`, `docs/architecture/data.md` |
| Install command | `python -m pip install -r requirements.txt` | `README.md`, CI job `install` |
| Run command | `uvicorn app.main:app --reload --port 8000` | `README.md` local-dev section |
| Test command | `pytest -q` | `azure-pipelines.yml` test stage; confirmed locally |
| Application code path | `app/` | Repository layout |
| Test path | `tests/` | Repository layout (`tests/unit/`, `tests/integration/`) |
| Documented coding conventions | Partial — error and logging notes in `docs/architecture/conventions.md`; rest inferred from code | Copied into `.github/copilot-instructions.md` |
| CI system and pipeline file | Azure Pipelines — `azure-pipelines.yml` | |

**Did you run their test command yourself?** `yes` **Did it pass on a clean checkout?** `yes — 142 passed, 3 skipped (integration, need Cosmos emulator)`

> A failing or missing test suite on day one is not a blocker, but it is a finding. Record it here, raise it with the technical contact, and expect it to shape the first iteration.

## 7. Anything unusual

| What | Does it matter? | What you did about it |
| --- | --- | --- |
| Integration tests skip without Cosmos emulator; CI runs them only on `main` | Yes — Stage 6 local loops will look greener than CI | Noted in `copilot-instructions.md`; will use emulator before claiming an integration task done |
| Repo still has a second, unused `src/` stub from an abandoned layout | No for Stage 1 | Left alone; recorded application path as `app/` only |

## 8. Ready to continue?

| Gate | Met? |
| --- | --- |
| You can commit to the working repository | Yes |
| The helpers needed for Stages 2 and 6 are visible | Yes |
| The tracker's MCP server is connected | Yes |
| Your commit identity is correct for this customer | Yes |
| The inherited stack is recorded, and you have run their tests | Yes |

**Stage 1 complete:** Yes

---

## 9. What next

| Step | Action |
| --- | --- |
| **Now** | Transcribe the statement of work into [`../02-discovery/scope-framing.md`](../02-discovery/scope-framing.md) |
| **Then** | Open [Stage 2 — Discovery](../02-discovery/README.md) |
| **Helper for Stage 2** | `BRD Builder` |
| **It will produce** | `docs/brds/<name>-brd.md` |
