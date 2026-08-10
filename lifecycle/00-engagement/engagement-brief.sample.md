# Engagement brief (sample)

Example of a filled-in [`engagement-brief.md`](engagement-brief.md) for a fictional Contoso engagement. Copy the shape, not the facts — fill the real file during Stage 0.

| Field | Value |
| --- | --- |
| **Customer** | Contoso Manufacturing |
| **Engagement name** | nightly-ingest-enablement |
| **Status** | Confirmed |
| **Author** | A. Engineer |
| **Last updated** | 2026-08-10 |

---

## 1. Why this engagement exists

Plant operations still rebuild overnight batch files by hand when a supplier feed arrives late. Contoso wants the existing nightly ingest service to retry failed supplier drops automatically, surface failures to operators before the morning shift, and leave two plant engineers able to change the pipeline without the central platform team.

**Source of truth for scope:** `docs/contracts/contoso-nightly-ingest-sow-2026-q3.pdf` (SOW §3–4) and ADS notes from 2026-07-14

---

## 2. People

| Role | Name | What you need from them |
| --- | --- | --- |
| **Sponsor** | Jordan Hale | Signs off the exit criteria, unblocks access, settles scope disputes |
| **Technical contact** | Priya Nair | Answers architecture questions, owns Contoso-Dev / Contoso-Prod |
| **Product owner** | Sam Ortiz | Owns the backlog and priority after you leave |
| **Your lead** | Morgan Lee | Escalation path on your side |

### Engineers you are enabling

| Name | Current level with this stack | What they need to own by handover |
| --- | --- | --- |
| Chris Park | Competent | Ingest job definitions, retry policy, and Azure Pipelines for this repo |
| Riley Chen | New to it | Operator runbook, failure triage, and day-two config changes |

---

## 3. Window and cadence

| Field | Value |
| --- | --- |
| Start date | 2026-08-03 |
| Last day | 2026-10-31 |
| Sprint length | Two weeks |
| Number of sprints | Six |
| Demo day | Every second Thursday, to Jordan (sponsor) and Sam (product owner) |
| Your allocation | Full time on Contoso; Morgan covers other accounts |

---

## 4. Exit criteria

| # | Must be true on the last day | How it gets verified |
| --- | --- | --- |
| E1 | Failed supplier drops are retried automatically on Contoso-Prod according to the policy in the SOW, with operator-visible failure alerts before 06:00 plant local time | Priya confirms a failed drop in Contoso-Dev then Contoso-Prod; Sam confirms the alert appears in the operator channel |
| E2 | Chris and Riley have each shipped at least one change to the ingest retry path unaided (PR opened, reviewed, and merged by Contoso) | Two merged PRs with Chris and Riley as authors; Morgan spot-checks that coaching was not doing the work |
| E3 | Runbook and handover docs live in Contoso's wiki and the repo's `docs/operations/`, and Sam can find the on-call steps without asking you | Sam completes the Stage 9 walkthrough checklist without prompting |

**In one sentence:** The nightly ingest retries and alerts on their subscription, and two named Contoso engineers can change it without us.

> Confirmed with Jordan Hale on 2026-08-05. Their correction: none — kept "before 06:00 plant local time" explicit in E1

---

## 5. What you are inheriting

| Area | What is already there | Can you change it? |
| --- | --- | --- |
| Repository | `https://dev.azure.com/contoso/Manufacturing/_git/nightly-ingest` | No (stay in this repo) |
| Language and framework | Python 3.12, FastAPI 0.115, Pydantic v2 | No — needs a decision record if we propose otherwise |
| Cloud and subscription | Contoso tenant; Contoso-Dev (Contributor) and Contoso-Prod (read + gated deploy) | No for tenant; yes for app config within Dev |
| Tracker | Azure DevOps Boards, Manufacturing project | No |
| CI and deployment | Azure Pipelines via `azure-pipelines.yml`; Prod gated by Priya | Pipeline steps yes; gate owners no |
| Test setup | Pytest; command `pytest -q` | Yes within existing layout |
| Coding standards | Partial — `docs/architecture/conventions.md` plus patterns in `app/` | Prefer follow; departures need a decision record |

---

## 6. Compliance obligations

| Applies | Obligation | Turns into |
| --- | --- | --- |
| no | The system contains AI, or makes automated decisions about people | `RAI Planner` in Stage 2 — required |
| yes | It handles personal data, credentials, payments, or health records | `Security Planner` in Stage 2 and `/security-review` in Stage 7 — required |
| no | The customer requires supply-chain assurance (SBOM, SLSA, provenance) | `SSSC Planner` in Stage 2 — required |
| no | It is subject to a named regulation | Contoso Legal (Elena Vos) confirmed 2026-08-06 — manufacturing ops data only for this scope |
| yes | It processes data that cannot leave a region or tenant | A decision record in Stage 3, and a constraint on every later stage — data stays in `westeurope` on Contoso tenant |

---

## 7. Risks and unknowns

| # | Risk or unknown | Who can resolve it | By when |
| --- | --- | --- | --- |
| R1 | Prod deploy approvals still pending for A. Engineer | Priya Nair | 2026-08-15 |
| R2 | Integration tests skip without Cosmos emulator; local loops can look greener than CI | Priya Nair / Chris Park | Before first integration task in Stage 6 |
| R3 | SOW says "near real time" for failure alerts without a numeric SLA | Sam Ortiz / Jordan Hale | During Stage 2 customer pass of scope framing |

---

## 8. Handover destination

| Field | Value |
| --- | --- |
| Repository owner after handover | Contoso Manufacturing platform team (Priya Nair) |
| Who can merge after you go | Priya Nair, Chris Park, Riley Chen |
| Where the documentation lives | This repo's `docs/` plus Contoso Manufacturing wiki |
| Where the runbook must end up | Contoso Manufacturing wiki (primary) and `docs/operations/` (copy) |
| Support arrangement after the last day | Best effort for two weeks after 2026-10-31, then Contoso only |

---

## 9. What happens next

| Step | Action |
| --- | --- |
| **Now** | Walk sections 4, 2, and 8 past the sponsor and technical contact |
| **Then** | [Stage 1 — Setup](../01-setup/README.md), which checks the tooling and the repository you are inheriting |
| **Then** | [Stage 2 — Discovery](../02-discovery/README.md), which turns the statement of work into a BRD |
