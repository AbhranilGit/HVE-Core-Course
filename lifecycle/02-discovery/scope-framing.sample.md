# Scope framing (sample)

Example of a filled-in [`scope-framing.md`](scope-framing.md) for a fictional Contoso engagement. Copy the shape, not the facts — fill the real file before Stage 2. Ambiguities are left marked on purpose.

| Field | Value |
| --- | --- |
| **Engagement** | nightly-ingest-enablement |
| **Status** | Ready for BRD Builder |
| **Scope source** | `docs/contracts/contoso-nightly-ingest-sow-2026-q3.pdf` (SOW §3–4); ADS notes 2026-07-14 |
| **Next artifact** | `docs/brds/nightly-ingest-brd.md` via **`BRD Builder`** |
| **Last updated** | 2026-08-10 |

---

## How to fill this in

1. **Quote, do not paraphrase.** Where the statement of work says something specific, use its words. When scope is disputed in week eight, matching wording is what settles it.
2. **Mark every gap.** Anything the source documents do not answer gets `ambiguous — ...`. Do not fill it with your own reasonable assumption; your assumption is not what anyone signed.
3. **Be generous with section 3's "out" list.** Every engagement dies the same way: a series of small, individually reasonable additions. The out list is the only defence, and it is worth more than the in list.
4. **Come back and edit.** When scope legitimately changes, change it here first, then work forward from Stage 2 again. Changing the code without changing this is how the documents stop describing the system.

---

## 1. The problem

"When a supplier drop lands late or fails validation, plant ops rebuild the overnight batch by hand before the morning shift. Contoso needs the existing nightly ingest service to retry failed drops automatically and make failures visible to operators in time to act." (SOW §1.2)

**Who has it:** Plant operators at Contoso's EU sites; the Manufacturing platform team that owns `nightly-ingest`

**What they do today instead:** On-call engineers download the supplier file, re-run a local script, and post status in Teams when something fails after 22:00

---

## 2. Users

| Role | What they need to be able to do | Named contact who can answer questions about them |
| --- | --- | --- |
| Plant operator | See failed ingest jobs and whether a retry is in progress before 06:00 plant local time | Sam Ortiz |
| Platform engineer (Chris / Riley) | Change retry policy and job config in this repo and ship via Contoso's pipeline | Priya Nair |
| Manufacturing platform lead | Confirm Prod behaviour without opening a bridge to the engagement team | Priya Nair |

**Explicitly not served in this engagement:** Supplier portal users · Contoso finance reporting · non-EU plants

**Scale:** ambiguous — SOW says "all EU supplier feeds on the current nightly schedule" but does not state feed count or peak file size

---

## 3. In scope and out of scope

### In — contracted for this engagement

| Capability | Source | Notes or constraints |
| --- | --- | --- |
| Automatic retry of failed supplier drops on the existing nightly ingest path | SOW §3.1 | Must use Contoso-Prod; no new runtime |
| Operator-visible failure alerts before 06:00 plant local time | SOW §3.2; exit criterion E1 | Channel already used by plant ops |
| Enablement so two named Contoso engineers can change the retry path unaided | SOW §4; engagement brief E2 | Chris Park, Riley Chen |
| Security review for credentials and personal data touched by ingest | Engagement brief §6 | `Security Planner` + Stage 7 `/security-review` |

### Out — explicitly not this engagement

Real-time (sub-minute) ingest · New supplier onboarding UI · Replacing Cosmos or Blob · Multi-region active-active · Mobile operator app · Changing Contoso's identity provider · Finance or inventory systems downstream of ingest

**Deferred to a later phase, if one is agreed:** Non-EU plants · Supplier self-serve re-upload portal · SLSA / SBOM pipeline hardening (Contoso said not required this engagement)

---

## 4. Inherited constraints

| Area | Constraint | Negotiable? |
| --- | --- | --- |
| Language and framework | Python 3.12, FastAPI, Pydantic v2 in `app/` | No |
| Where it runs | Contoso tenant, `westeurope`, Contoso-Dev / Contoso-Prod | No |
| Data residency and retention | Ingest payloads stay in Contoso tenant in `westeurope`; retention per Contoso data policy | No |
| Identity and access | Existing Contoso Entra ID app registration and Key Vault | No new IdP |
| Deployment | Azure Pipelines `azure-pipelines.yml`; Prod gated by Priya | Pipeline steps yes; gate no |
| Quality bar | `pytest -q` green; Contoso PR review before merge | No |

---

## 5. Success measures

Validation window: four weeks after handover (through 2026-11-28)

| What gets measured | Target | Who measures it |
| --- | --- | --- |
| Manual overnight rebuilds caused by failed supplier drops | Zero in the validation window on Contoso-Prod EU feeds | Sam Ortiz |
| Operator alert lead time before 06:00 plant local | Alert for every failed drop that exhausts retries | Priya Nair |
| Contoso-authored changes to retry path | At least two merged PRs by Chris or Riley without engagement pair-programming | Morgan Lee |

---

## 6. Open questions for the customer

| # | Question | Who answers | Asked on | Answer |
| --- | --- | --- | --- | --- |
| Q1 | SOW §3.2 says failure alerts must be "near real time" — is the acceptance bar "before 06:00 plant local" only, or is there a maximum minutes-after-failure target? | Sam Ortiz / Jordan Hale | 2026-08-07 | Pending — on agenda for 2026-08-12 |
| Q2 | How many EU supplier feeds are on the current nightly schedule, and what is the largest expected file size? | Priya Nair | 2026-08-07 | |
| Q3 | Which Teams channel (or other channel) is authoritative for operator alerts today? | Sam Ortiz | 2026-08-07 | |

---

## 7. What happens next

| Step | Action |
| --- | --- |
| **Helper to pick** | **`BRD Builder`** |
| **Reads** | This file, plus the scope source it points at |
| **Produces** | `docs/brds/nightly-ingest-brd.md` |
| **Not yet** | Features, technology choices, work items, or any code |

When this file is filled in and section 6 has been through the customer once, open **[Stage 2 — Discovery](README.md)**.
