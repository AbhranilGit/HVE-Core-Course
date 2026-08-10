# Scope framing

> You are not inventing this. You are transcribing what the statement of work and the Architecture Design Session already decided, in a form the AI helpers can read, and marking every place where they were vague.
>
> The vague places are the valuable part. Fill them in with `ambiguous — <what is unclear>` rather than resolving them yourself, then take the list to the customer.

| Field | Value |
| --- | --- |
| **Engagement** | `<name, from the engagement brief>` |
| **Status** | Draft |
| **Scope source** | `<link or path to the SOW, ADS output, or scoping deck>` |
| **Next artifact** | `docs/brds/<name>-brd.md` via **`BRD Builder`** |
| **Last updated** | `<YYYY-MM-DD>` |

---

## How to fill this in

1. **Quote, do not paraphrase.** Where the statement of work says something specific, use its words. When scope is disputed in week eight, matching wording is what settles it.
2. **Mark every gap.** Anything the source documents do not answer gets `ambiguous — ...`. Do not fill it with your own reasonable assumption; your assumption is not what anyone signed.
3. **Be generous with section 3's "out" list.** Every engagement dies the same way: a series of small, individually reasonable additions. The out list is the only defence, and it is worth more than the in list.
4. **Come back and edit.** When scope legitimately changes, change it here first, then work forward from Stage 2 again. Changing the code without changing this is how the documents stop describing the system.

---

## 1. The problem

> In the customer's words. Two or three sentences from the statement of work or the discovery conversations.

`<the problem this engagement solves>`

**Who has it:** `<the users or operators who feel it today>`

**What they do today instead:** `<the manual process, spreadsheet, or workaround being replaced>`

> That last line matters more than it looks. It is what the customer will compare your work against, whatever the acceptance criteria say.

---

## 2. Users

| Role | What they need to be able to do | Named contact who can answer questions about them |
| --- | --- | --- |
| `<role>` | `<the one thing>` | `<name, or "none — ambiguous">` |
| `<role>` | | |

**Explicitly not served in this engagement:** `<groups deferred to later phases>`

**Scale:** `<users, volume, throughput — from the SOW if it says, otherwise ambiguous>`

---

## 3. In scope and out of scope

### In — contracted for this engagement

| Capability | Source | Notes or constraints |
| --- | --- | --- |
| `<capability>` | `<SOW section, or ADS decision>` | |
| `<capability>` | | |
| `<capability>` | | |

### Out — explicitly not this engagement

> List everything you are saying no to, separated by `·`. Include the things the customer will probably ask for anyway; writing them here now is much easier than declining them in week nine.

`<out-of-scope list>`

**Deferred to a later phase, if one is agreed:** `<things both sides expect to come back to>`

> The difference between "out" and "deferred" is worth keeping. Out means it was considered and rejected. Deferred means it was considered and postponed, and someone will raise it again.

---

## 4. Inherited constraints

> Pull these from section 5 of the [engagement brief](../00-engagement/engagement-brief.md). Anything you cannot change is a constraint the BRD, the PRD, and every decision record must respect.

| Area | Constraint | Negotiable? |
| --- | --- | --- |
| Language and framework | `<what they run>` | |
| Where it runs | `<their tenant, region, on-premises>` | |
| Data residency and retention | `<rules that cannot be broken>` | |
| Identity and access | `<their existing scheme>` | |
| Deployment | `<their pipeline, their release process>` | |
| Quality bar | `<what must pass before they accept a change>` | |

---

## 5. Success measures

> How the customer will judge this a few weeks after you leave. Take these from the statement of work where it states them. Where it does not, that is a real gap — an engagement with no agreed measure of success is one you cannot be shown to have completed.

Validation window: `<how long after handover before this is judged>`

| What gets measured | Target | Who measures it |
| --- | --- | --- |
| `<observable outcome>` | `<number or threshold>` | `<name>` |
| `<observable outcome>` | | |

---

## 6. Open questions for the customer

> Everything you marked `ambiguous` above, collected. This is your agenda for the next customer conversation, and it is the single most useful output of this document.

| # | Question | Who answers | Asked on | Answer |
| --- | --- | --- | --- | --- |
| Q1 | `<question>` | `<name>` | | |
| Q2 | | | | |
| Q3 | | | | |

> Record the answers here rather than only in the chat or a meeting note. Stage 2 reads this file, and an answer that lives only in your memory is an answer the AI helpers do not have.

---

## 7. What happens next

| Step | Action |
| --- | --- |
| **Helper to pick** | **`BRD Builder`** |
| **Reads** | This file, plus the scope source it points at |
| **Produces** | `docs/brds/<name>-brd.md` |
| **Not yet** | Features, technology choices, work items, or any code |

When this file is filled in and section 6 has been through the customer once, open **[Stage 2 — Discovery](README.md)**.
