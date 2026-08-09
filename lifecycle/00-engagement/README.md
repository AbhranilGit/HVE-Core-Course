# Stage 0 — Engagement framing

Write down the shape of the engagement before you write down the shape of the
product.

| | |
| --- | --- |
| **Reads** | The statement of work, the Architecture Design Session output, and whatever the account team handed you |
| **Produces** | [`engagement-brief.md`](engagement-brief.md) |
| **Helpers** | None — this one is yours |
| **Takes** | An hour, most of it asking other people questions |

---

## 1. Why this stage exists

The nine HVE stages describe how a product gets built. They do not describe how
an engagement starts and ends, and that omission is where delivery work goes
wrong.

An engagement has boundaries a product does not have. It has a last day. It has
someone who owns the code after you leave and who may not have written any of
it. It has a contract that says what "finished" means, and that definition is
usually narrower than what you would build if left alone. It has a customer
team whose ability to keep going is the actual deliverable, whatever the
statement of work says the deliverable is.

None of that fits in a BRD. Write it here instead, on day one, while you still
have the account team's attention and before anyone has opinions about the
architecture.

## 2. The question this stage answers

**What has to be true for you to leave?**

Everything in the brief exists to make that answerable. If you cannot say on day
one what your last day looks like, you will discover the answer in week ten,
when it is expensive.

## 3. Prerequisites

- You have been assigned to the engagement and can name the customer
- You have access to whatever pre-sales produced: a statement of work, an Architecture Design Session summary, a scoping deck, meeting notes, anything
- You have, or have asked for, a named technical contact on the customer side

You do not need repository access yet. Stage 1 handles that.

## 4. Fill in the brief

Open [`engagement-brief.md`](engagement-brief.md) and work through it. Most of
it you will not know on your own — that is the point. The gaps are your first
week's questions, and the brief is how you make them visible rather than
discovering them one at a time.

Where you genuinely do not know, write `unknown — asking <person> by <date>`
rather than guessing. An unknown you have named is a manageable risk. An unknown
you have papered over is a surprise.

## 5. Take it to the customer

Do not keep the brief to yourself. Walk the sponsor and the technical contact
through it in the first week, specifically:

- **The exit criteria.** This is the conversation people avoid and the one that matters most. If your definition of done and the sponsor's differ, you want to find out now.
- **Who is being enabled.** Name the individuals. "The customer team" is not a name. If nobody is named, you are not doing an engagement, you are doing outsourcing, and the handover in Stage 9 will fail.
- **What happens to the repository.** Who owns it, where it ends up, and who has permission to merge after you go.

Update the brief with what you learn. It is a living document for the first two
weeks and a stable one after that.

## 6. If something is refused

Sometimes you will ask who is being enabled and get no answer, or ask about exit
criteria and be told "just build it". That is information. Record it in the
brief's risk section in plain language, tell your lead, and carry on — but do
not quietly replace the missing answer with your own assumption. Your assumption
will not be the one you are held to.

## 7. Done when

- [`engagement-brief.md`](engagement-brief.md) has no unanswered fields, or each remaining gap names who you are asking and by when
- You can state your exit criteria in one sentence, and the sponsor has heard it
- You can name the customer engineers you are enabling
- You know who owns the repository after handover and who can merge to it
- You know your compliance obligations: whether this touches AI, personal data, payments, or regulated workloads. Stage 2 turns those into required reviews rather than optional ones

**Next:** [Stage 1 — Setup](../01-setup/README.md)

---

## Where this sits in HVE

HVE Core's lifecycle has nine stages and this is not one of them. It is numbered
zero deliberately: the nine keep their usual numbers so the mapping to the
framework stays intact, and the engagement framing sits in front of them.

If you are working on your own product rather than a customer's, you do not need
this stage. The [course variant](../../README.md#two-variants) of this template
drops it.
