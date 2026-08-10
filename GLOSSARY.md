# Words you will see

Terms this template uses, and what they mean in a delivery context. Come back when a stage page uses one you do not recognise.

Start with the [main README](README.md) if you have not yet.

## Engagement terms

| Term | What it actually means |
| --- | --- |
| **Engagement** | A fixed-duration piece of delivery work in a customer's environment. It has a contract, a last day, and someone who owns the result afterwards. |
| **FDE** (forward deployed engineer) | An engineer who works inside the customer's environment and codebase for the duration of an engagement, rather than delivering to them from outside. |
| **SOW** (statement of work) | The contract defining what was sold. It is the authority on scope, and the thing your BRD reconciles against. |
| **ADS** (architecture design session) | The pre-sales workshop that usually produced the initial technical shape of the engagement. Its output is a scope input, not a design you are bound to. |
| **Engagement brief** | The document you write in Stage 0: window, people, exit criteria, what you are inheriting, and which compliance obligations apply. Lives at `lifecycle/00-engagement/engagement-brief.md`. |
| **Exit criteria** | What must be true for you to leave with the work genuinely finished rather than merely stopped. Written on day one, checked in Stage 9, and the single most important thing in the brief. |
| **Enablement** | Getting the customer's engineers to the point where they can do the work without you. Not a training session — a progression from watching to pairing to working alone. |
| **Handover** | Transferring ownership of the system, the knowledge, and the ability to change it. The Stage 9 deliverable, and the one that decides whether the engagement mattered. |
| **Brownfield** | Working in a codebase that already exists, with its own conventions and history. The default assumption in this template. |
| **Greenfield** | Starting from nothing. Rarer on engagements than people expect. |

## The documents

| Term | What it actually means |
| --- | --- |
| **Scope framing** | Your transcription of the contracted scope into a form the helpers can read, with every ambiguity marked rather than resolved. Lives at `lifecycle/02-discovery/scope-framing.md`. Written by hand. |
| **BRD** (business requirements document) | The *why*: the problem, who has it, what success looks like, and what is deliberately excluded. On an engagement it reconciles the statement of work with reality and surfaces what the contract left vague. Lands in `docs/brds/`. |
| **PRD** (product requirements document) | The *what*: features as user stories, each with acceptance criteria and a stable id. Lands in `docs/prds/`. |
| **User story** | "As a *someone*, I want to *do something*, so that *benefit*." |
| **Acceptance criteria** (**AC**) | The checklist that decides whether something is done. Each gets an id so work items, reviews, and release evidence can point back at it. That thread is what makes scope disputes settleable. |
| **Decision record** (also **ADR**) | A one-page note recording a technical decision, why, what it costs, and when to revisit. On an engagement, records split into **inherited** constraints and **chosen** decisions — a future reader needs to know which. Lands in `docs/decisions/`, named `2026-03-14-topic-v01.md`. |
| **Sprint plan** | The backlog ordered into iterations, planned backwards from the last day, with a definition of done and a demo for each. Lands at `docs/planning/sprint-plan.md`. |
| **Release evidence** | Row-by-row proof behind a release: every acceptance criterion, where its evidence lives, whether it passed, and who signed it off. |
| **Runbook** | How to start the system, where its data lives, how to deploy and roll back, and what to do when it breaks. Written for someone who cannot ask you. |
| **Handover document** | What was delivered, what was not, where the system is weak, and what to do next. The section people soften is the section that gets read. |

## How the work is organised

| Term | What it actually means |
| --- | --- |
| **Work item** (or **issue**) | One small task in the customer's tracker, with acceptance criteria citing the PRD ids they came from. |
| **Tracker** | Where the customer keeps work — usually Azure DevOps, sometimes GitHub Issues or Jira. Use theirs. A second tracker for the duration of an engagement loses half the history at handover. |
| **Iteration** (or **sprint**) | A batch of work with a definition of done and a demo at the end. Azure DevOps calls it an iteration. |
| **Thin vertical slice** | The smallest end-to-end path a real user could exercise, touching every layer. Always the first iteration, so that when something goes wrong in week five you have something real rather than scaffolding. |
| **Definition of done** | The agreed rules for calling an iteration finished. |
| **Demo** | Showing the iteration's result against the review file, criterion by criterion, to the sponsor and product owner. A criterion you think passes and they think does not is the most valuable finding you can get. |
| **In scope / out of scope** | What is contracted, and what is explicitly not. The out list is worth more than the in list. |
| **Deferred** | Considered and postponed, as opposed to considered and rejected. Someone will raise it again, so keep the distinction. |
| **Scope creep** | Additions nobody contracted for. On an engagement every one of them is unpaid, and they land in your final week. |

## The AI helpers

| Term | What it actually means |
| --- | --- |
| **HVE** (Hyper Velocity Engineering) | Microsoft's framework for AI-assisted delivery, and the nine-stage lifecycle this template follows. **HVE Core** is the tooling; **HVE Core - All** is the full bundle. This template targets `3.3.101`. |
| **Helper** (also **agent** or **mode**) | Copilot Chat configured for one job. Using the right one matters more than the wording of your prompt. Most arrive automatically with a slash command; a few you pick from the dropdown. |
| **Slash command** | An instruction starting with `/` that runs a specific routine, for example `/task-research` or `/ado-sprint-plan`. Most carry their own helper. |
| **Argument** | A `name=value` pair after a command, as in `/task-plan research=<path>`. The chat shows which ones a command accepts as you type. |
| **Skill** | A packaged capability a helper loads when needed — the OWASP checklists are skills. You rarely invoke these directly. |
| **Instructions** | Background rules applied automatically. `.github/copilot-instructions.md` is this project's set, and every helper reads it on every request. |
| **MCP server** | The connection that lets a helper reach an external system such as Azure DevOps or GitHub. Stages 4 and 5 work entirely through it, and access in a customer tenant often needs requesting in advance. |
| **RPI** (research, plan, implement, review) | The four-phase routine for writing code: `/task-research`, `/task-plan`, `/task-implement`, `/task-review`. Each writes a file you read before allowing the next. On an inherited codebase the research phase is also how you learn the conventions you are about to work inside. |
| **Slug** | The short lowercase name keeping a task's four evidence files recognisable, for example `wi-4821-operator-can-log-in`. The phases chain by file path, but a consistent slug is what makes the folders readable a month later. |
| **Gate** | A checkpoint you confirm before moving on. If the previous step's file does not exist or you have not read it, you do not proceed. |
| **Planning log** | What `Task Planner` writes after checking its own plan, listing discrepancies between the research and the plan. Reading its discrepancy section is the Plan gate. |
| **Overall status** | What `Task Reviewer` reports: Complete, Needs Rework, or Blocked, with critical and major finding counts. Only Complete means done. |

## Compliance

| Term | What it actually means |
| --- | --- |
| **RAI** (responsible AI) | Microsoft's framework for assessing AI systems for fairness, reliability, transparency, and harm. Required in Stage 2 if the system contains AI or makes automated decisions about people. |
| **Threat model** | A structured account of what an attacker would try and what stops them. `Security Planner` produces one using STRIDE; Stage 7 checks the built system against it. |
| **STRIDE** | The categories a threat model works through: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. |
| **SSSC** (secure software supply chain) | Assurance about what your dependencies and build process introduce. Produces an SBOM, SLSA, and OpenSSF Scorecard plan. |
| **SBOM** (software bill of materials) | The machine-readable inventory of everything your software is built from. |
| **OWASP** | The catalogue of common security weaknesses `Security Reviewer` assesses against, with different sets for web, LLM, agentic, MCP, infrastructure, and CI/CD systems. |

## Git and shipping

| Term | What it actually means |
| --- | --- |
| **Branch** | A separate line of work. Follow the customer's naming convention, not your own. |
| **Pull request** (PR) | A request to merge, and on an engagement the main surface where enablement actually happens — it is the one artefact the customer's engineers are already obliged to read. |
| **Tag** | A permanent label on one version. This template starts at `v0.1.0`; use the customer's scheme if they have one, and name the engagement in the tag message. |
| **Release notes** | What shipped, how it was checked, what was left out, and which known defects were accepted. Written for the customer. |

## Folders

| Folder | What it holds |
| --- | --- |
| `lifecycle/` | The stage pages you read, plus the two documents you write by hand and your Stage 6 task log. |
| `docs/` | Everything the customer keeps: `brds/`, `prds/`, and `decisions/` at HVE Core's default locations, plus `planning/`, `reviews/`, `releases/`, and `operations/`. |
| `.github/` | `copilot-instructions.md`, this project's conventions and inherited stack, plus the work item template. |
| `.copilot-tracking/` | Working evidence the helpers save as they research, plan, implement, and review. Not committed. Stage 7 reads it, so leave it in place while the engagement is live. |

In an existing repository the application code and tests stay where they already are. Their real paths are recorded in `.github/copilot-instructions.md`.
