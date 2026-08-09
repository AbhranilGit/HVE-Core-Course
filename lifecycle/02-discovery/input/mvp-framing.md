# MVP Framing — write your idea here

> **This is the only document you write by hand.** Everything after this is generated from it. Delete the guidance quotes as you go, or leave them — the helpers ignore them.

## How to fill this in

1. **Describe the problem, not the solution.** Write what is painful today and for whom. Resist designing screens or picking a database — Stage 3 does that, with your input.
2. **Be brutal in section 3.** The "out of scope" list is the most valuable part of this file. Every prompt in this kit points back here to stop features creeping in.
3. **Do not leave a section blank.** If you are unsure, write your best guess and add the doubt to section 6. Stage 2 will ask you about it properly.
4. **Plain language is fine.** No one is grading the writing. Short and honest beats polished and vague.

Do not worry about getting this perfect. You can come back and edit it at any stage — in fact, that is exactly what you should do when you change your mind later.

The examples below are from a made-up habit tracker, purely to show the shape of a good answer. Replace them.

---

| Field | Value |
| --- | --- |
| **Product** | `<name — and one line on what it does>` |
| **Status** | Draft |
| **HVE stage** | Stage 2 — Discovery input |
| **Next artifact** | `lifecycle/02-discovery/output/brd.md` via **`brd-builder`** |
| **Stack intent** | `<optional: any technology you already know you want, or "undecided">` |

---

## 1. Problem

> What is painful today, and why do existing workarounds fall short? Two or three sentences.
>
> *Example: "People who want to build a habit lose track after a few days. They use notes apps or memory, so they cannot see whether they are actually improving, and they give up without knowing how close they came."*

`<your problem statement>`

**Hypothesis:** if `<the people you are helping>` can `<do the core thing>`, then `<the change you expect to see>` within `<a rough timeframe>`.

> *Example: "If someone can log a habit in under five seconds and see this week at a glance, they will keep logging for a full month."*

---

## 2. Users

> Who will actually use this? Two or three roles is plenty for a first version. If you only have one, that is fine.

| Role | What they need from it |
| --- | --- |
| `<role>` | `<the one thing they need to be able to do>` |
| `<role>` | `<the one thing they need to be able to do>` |

**Not for (in this version):** `<groups you are deliberately not serving yet>`

> *Example: "Not for teams, coaches, or anyone wanting to share progress publicly."*

**Rough scale:** `<how many people, how much data — a guess is fine>`

---

## 3. In scope / out of scope

> The most important section. Anything not listed under **In** is **out** until you come back and edit this file.

### In (must exist in the first version)

| Capability | Notes |
| --- | --- |
| `<capability>` | `<any constraint or default worth stating>` |
| `<capability>` | `<any constraint or default worth stating>` |
| `<capability>` | `<any constraint or default worth stating>` |

> *Example: "Log a habit once per day", "See this week's record at a glance", "Add and remove habits", "Data survives closing the app".*

### Out (not now — maybe never)

`<list everything you are saying no to, separated by ·>`

> *Example: "Reminders and notifications · sharing with friends · mobile app · accounts and login · charts and statistics · importing from other apps."*

Keep this list generous. Writing something here does not kill it forever; it just keeps it out of version one.

---

## 4. Constraints

> Anything that limits how this gets built. Skip rows that do not apply, and write "no constraint" where you genuinely do not care — that is useful information too.

| Area | Rule |
| --- | --- |
| Where it runs | `<e.g. on my own laptop / a shared machine / a server>` |
| Data | `<where data lives; anything you must not store>` |
| Users and access | `<login needed? or is a name enough?>` |
| Technology | `<languages or tools you must use or must avoid — "no preference" is a valid answer>` |
| Quality bar | `<what must be tested or reviewed before you call it done>` |
| Time or effort | `<any deadline or budget of hours>` |

---

## 5. Success metrics

> How will you know, a few weeks after launch, whether this worked? Pick two or three you can actually observe. Vague goals like "users love it" are not measurable; "I logged something on at least five days last week" is.

Validation window: `<how long you will watch before judging>`

| What you will measure | Target |
| --- | --- |
| `<observable behaviour>` | `<number or threshold>` |
| `<observable behaviour>` | `<number or threshold>` |

**If it works:** `<what you would build next>`
**If it does not:** `<what you would change or question first>`

---

## 6. Open questions

> Things you genuinely have not decided. Do not invent answers here — later stages will walk you through them. Listing a question is a decision to decide it later, which is fine. Leaving it unlisted and hoping is not.

1. `<question>`
2. `<question>`
3. `<question>`

> *Example: "Can a habit be logged more than once a day?", "What happens to a missed day — does the streak reset?", "Should old data be editable?"*

---

## 7. What happens next

You do not need to change anything in this table. It tells the next stage what to do.

| Step | Action |
| --- | --- |
| **Helper to pick** | **`brd-builder`** — not RPI Agent |
| **Reads** | This file |
| **Produces** | `lifecycle/02-discovery/output/brd.md` |
| **Not yet** | Features, technology choices, tasks, or any code |

When this file is filled in, open **[Stage 2 — Discovery](../README.md)**.
