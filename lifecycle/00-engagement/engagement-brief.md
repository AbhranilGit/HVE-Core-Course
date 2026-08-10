# Engagement brief

> Fill this in during your first week. Where you do not know, write `unknown — asking <person> by <date>` rather than guessing. Delete the guidance quotes as you go.

| Field | Value |
| --- | --- |
| **Customer** | `<organisation>` |
| **Engagement name** | `<short name — used for repo, docs, and demos>` |
| **Status** | Draft |
| **Author** | `<you>` |
| **Last updated** | `<YYYY-MM-DD>` |

---

## 1. Why this engagement exists

> Two or three sentences, in the customer's words rather than the account team's. What is broken or missing for them today, and why now?

`<the business problem>`

**Source of truth for scope:** `<link or path to the SOW, ADS output, or scoping deck>`

> Everything downstream cites this. If it does not exist, say so — it is your first and largest risk.

---

## 2. People

| Role | Name | What you need from them |
| --- | --- | --- |
| **Sponsor** | `<name>` | Signs off the exit criteria, unblocks access, settles scope disputes |
| **Technical contact** | `<name>` | Answers architecture questions, owns the environment |
| **Product owner** | `<name>` | Owns the backlog and priority after you leave |
| **Your lead** | `<name>` | Escalation path on your side |

### Engineers you are enabling

> Name individuals, not teams. These are the people who must be able to run the loop without you on your last day. If this table is empty, raise it in section 7 as a risk — an engagement with nobody to enable is not an engagement.

| Name | Current level with this stack | What they need to own by handover |
| --- | --- | --- |
| `<name>` | `<new to it / competent / expert>` | `<the part of the system they will maintain>` |
| `<name>` | | |

---

## 3. Window and cadence

| Field | Value |
| --- | --- |
| Start date | `<YYYY-MM-DD>` |
| Last day | `<YYYY-MM-DD>` |
| Sprint length | `<one or two weeks>` |
| Number of sprints | `<count>` |
| Demo day | `<e.g. every second Thursday, to the sponsor and product owner>` |
| Your allocation | `<full time, or the days per week you are actually on this>` |

> The last day is the only fixed point in this table. Everything else bends around it, which is why Stage 5 plans backwards from it.

---

## 4. Exit criteria

> The most important section. What must be true for you to leave with the work genuinely finished rather than merely stopped?
>
> Write these so someone else could check them without asking you. "The platform is production ready" is not checkable. "The ingest pipeline runs nightly on their subscription, and two named engineers have each shipped a change to it unaided" is.

| # | Must be true on the last day | How it gets verified |
| --- | --- | --- |
| E1 | `<criterion>` | `<who checks, and how>` |
| E2 | `<criterion>` | |
| E3 | `<criterion>` | |

**In one sentence:** `<what "done" means for this engagement>`

> Say that sentence out loud to the sponsor in week one. Record the date you did and any correction they made:
>
> Confirmed with `<name>` on `<YYYY-MM-DD>`. Their correction: `<none, or what changed>`

---

## 5. What you are inheriting

> You are almost certainly not starting from an empty repository. Write down what already exists, because Stage 1 checks it and Stage 6 has to live inside it.

| Area | What is already there | Can you change it? |
| --- | --- | --- |
| Repository | `<where it lives, or "to be created">` | |
| Language and framework | `<what they already run>` | `<yes / no / needs a decision record>` |
| Cloud and subscription | `<whose tenant, which subscription>` | |
| Tracker | `<Azure DevOps project / GitHub repo / Jira>` | |
| CI and deployment | `<what exists today>` | |
| Test setup | `<framework and the exact command, or "none">` | |
| Coding standards | `<their documented conventions, if any>` | |

> Where a row says you cannot change something, that constraint belongs in a decision record in Stage 3 — recorded as an inherited constraint with its consequences, not re-argued.

---

## 6. Compliance obligations

> Tick what applies. Each ticked box turns an optional review into a required one, and Stages 2 and 7 will hold you to it.

| Applies | Obligation | Turns into |
| --- | --- | --- |
| `<yes/no>` | The system contains AI, or makes automated decisions about people | `RAI Planner` in Stage 2 — required |
| `<yes/no>` | It handles personal data, credentials, payments, or health records | `Security Planner` in Stage 2 and `/security-review` in Stage 7 — required |
| `<yes/no>` | The customer requires supply-chain assurance (SBOM, SLSA, provenance) | `SSSC Planner` in Stage 2 — required |
| `<yes/no>` | It is subject to a named regulation | `<which one, and who on the customer side owns it>` |
| `<yes/no>` | It processes data that cannot leave a region or tenant | A decision record in Stage 3, and a constraint on every later stage |

> If every row is "no", write down who told you that and when. "Nobody mentioned compliance" is not the same as "compliance does not apply", and the difference surfaces at the worst possible moment.

---

## 7. Risks and unknowns

> One line each. A named risk is manageable; an unnamed one is a surprise.

| # | Risk or unknown | Who can resolve it | By when |
| --- | --- | --- | --- |
| R1 | `<e.g. no named engineers to enable>` | `<name>` | `<date>` |
| R2 | `<e.g. no environment access yet>` | | |
| R3 | | | |

---

## 8. Handover destination

> Where does everything end up when you leave? Fill this in now, not in week ten.

| Field | Value |
| --- | --- |
| Repository owner after handover | `<team or individual>` |
| Who can merge after you go | `<names or team>` |
| Where the documentation lives | `<this repo's docs/, or somewhere of theirs>` |
| Where the runbook must end up | `<their wiki, their repo, or here>` |
| Support arrangement after the last day | `<none, best effort, or a contracted period>` |

---

## 9. What happens next

| Step | Action |
| --- | --- |
| **Now** | Walk sections 4, 2, and 8 past the sponsor and technical contact |
| **Then** | [Stage 1 — Setup](../01-setup/README.md), which checks the tooling and the repository you are inheriting |
| **Then** | [Stage 2 — Discovery](../02-discovery/README.md), which turns the statement of work into a BRD |
