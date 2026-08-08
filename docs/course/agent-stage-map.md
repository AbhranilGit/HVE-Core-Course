# HVE for beginners: lifecycle, jobs, and which agent to use

This guide assumes you know **nothing** about HVE yet.  
Read it top to bottom once. Then use the stage sections as a cheat sheet while we build PulseBoard.

---

## What is HVE in plain English?

**HVE Core** (Hypervelocity Engineering) is a toolkit for GitHub Copilot in VS Code.

Instead of one generic chat that tries to do everything, HVE gives you **specialized helpers**:

| Kind | What it is | Everyday analogy |
| --- | --- | --- |
| **Agent** | A Copilot mode with a specific job (pick it from the agent dropdown) | Calling the right teammate: BA, PM, engineer, reviewer |
| **Skill / slash command** | A focused recipe you start with `/something` | A checklist for one task |
| **Instructions** | Auto-applied coding rules | Team coding standards on the wall |

**HVE Core All** (`hve-core-all`) is the full bundle: you get essentially every stable helper.

Important idea:

> AI is fast at guessing. HVE is designed to make it **slow down at the right moments** — research before coding, plan before implementing, review before calling work “done.”

---

## The big picture: the project lifecycle

Building software is not “open chat → write code.”  
HVE organizes work into **9 stages**, like chapters of a project:

```text
1 Setup
   ↓
2 Discovery          ← what problem are we solving?
   ↓
3 Product definition ← what exactly will we build?
   ↓
4 Decomposition      ← break it into tickets
   ↓
5 Sprint planning    ← what do we do first?
   ↓
6 Implementation     ← write the code (with RPI)
   ↓
7 Review             ← is it actually good enough?
   ↓
8 Delivery           ← merge, release
   ↓
9 Operations         ← keep it running / document it
```

You can loop:

- Review finds bugs → go back to Implementation  
- Delivery finishes a sprint → next sprint’s Implementation  
- Ops finds an incident → hotfix via Implementation  

### Tiny story (PulseBoard)

Imagine your team’s daily status is scattered across chat.

1. **Setup** — install HVE so the helpers appear in Copilot  
2. **Discovery** — write down the business problem (“standup context is lost in chat”)  
3. **Product definition** — decide features for MVP (post doing/blocked/next, see today’s board)  
4. **Decomposition** — turn that into GitHub issues  
5. **Sprint planning** — pick the first vertical slice  
6. **Implementation** — build API + page using Research → Plan → Implement  
7. **Review** — check against the requirements  
8. **Delivery** — open PR, merge, tag `v0.1.0`  
9. **Operations** — write “how to run this” so others aren’t stuck  

That whole path is the lifecycle. Agents are just **the right helper for each chapter.**

---

## RPI in one minute (you will use this a lot)

**RPI** = Research → Plan → Implement → Review.

| Phase | Question it answers | Touches code? |
| --- | --- | --- |
| Research | What do we know / not know? | No (read-only) |
| Plan | What steps will we take? | No |
| Implement | Do the steps | Yes |
| Review | Did we meet acceptance criteria? | No (review-only) |

**RPI Agent** runs this lifecycle for a coding task.  
It is **not** the tool for writing a BRD or PRD. Those are earlier stages.

Memory hook:

```text
Builders (brd / prd / adr)  →  decide WHAT and WHY  (documents)
RPI Agent                   →  change the repo HOW  (code + evidence)
```

---

## Stage-by-stage map

For each stage below:

1. **Job** — what you are trying to accomplish  
2. **Purpose** — why this stage exists  
3. **HVE helpers** — which agent/skill to use and **why**  
4. **PulseBoard note** — what we do in this course  

---

### Stage 1 — Setup

**Job:** Get your tools working.  
**Purpose:** If agents don’t show up in Copilot, every later step fails in confusing ways. You are not building product yet.

| Use | Why |
| --- | --- |
| **`hve-core-installer`** (skill) | Helps install/configure HVE collections into a workspace the supported way |
| VS Code Marketplace: **HVE Core - All** | Fastest path to get all stable agents |

**Also do (human setup):** GitHub Copilot Chat installed, repo cloned, Python env ready (for us: conda `hve-env` with Python 3.12).

**PulseBoard:** Done. You can see RPI Agent; folders for docs/app exist.

---

### Stage 2 — Discovery

**Job:** Understand the **business problem**, who hurts, what “good” looks like, and what is out of scope.  
**Purpose:** Stops you from coding a clever solution to the wrong problem.

| Use | Why |
| --- | --- |
| **`brd-builder`** | Main agent here. Drafts a **Business Requirements Document** (problem, stakeholders, scope, success, risks) without jumping into UI widgets and API routes |
| **`dt-coach`** (optional) | If the problem is fuzzy and you need user-centered discovery (interviews, problem framing). Design Thinking before a BRD |
| **`/rpi-research`** (optional) | Only if you have a **specific unknown** that blocks decisions (e.g. “is SQLite enough for 15 users?”). Research is read-only evidence, not coding |
| **`security-planner`** / **`sssc-planner`** / **`rai-planner`** (optional early) | When security, supply-chain, or responsible-AI risk must shape requirements early. Skip for tiny MVPs unless relevant |
| **`experiment-designer`** (optional) | When you need a small experiment to validate an unknown before committing |

**PulseBoard:** Use **`brd-builder`** with our MVP framing. Save to `docs/project-planning/brd.md`.

---

### Stage 3 — Product definition

**Job:** Turn “we need a status board” into a concrete product spec and key design decisions.  
**Purpose:** The BRD says *why* and *what business outcome*. The PRD/ADRs say *what the product does* and *which technical choices we lock*.

| Use | Why |
| --- | --- |
| **`prd-builder`** | Builds a **Product Requirements Document**: features, user stories, acceptance criteria — still before big coding |
| **`product-manager-advisor`** | Helps prioritize and improve story quality if you’re unsure what is MVP vs later |
| **`adr-creation`** | Writes **Architecture Decision Records** (e.g. SQLite vs Postgres, how login works). Decisions stop being “lost in chat” |
| **`architecture-diagrams`** (skill) | Draws simple system pictures so everyone shares the same mental model |
| **`system-architecture-reviewer`** | Critiques the design for trade-offs before you invest in code |
| **`ux-ui-designer`** (optional) | Journeys, jobs-to-be-done, accessibility needs — research artifacts, not Figma pixels |

**PulseBoard:** `prd-builder` for MVP features; `adr-creation` for SQLite + simple identity; a small diagram.

---

### Stage 4 — Decomposition

**Job:** Break the PRD into trackable work items (issues/tickets).  
**Purpose:** A 20-page PRD does not get built. Small issues with acceptance criteria do.

| Use | Why |
| --- | --- |
| **`github-backlog-manager`** | Creates/triages GitHub issues from requirements; keeps backlog structured |
| **`ado-prd-to-wit`** / Azure DevOps backlog agents | Same idea if your team lives in Azure DevOps |
| **`jira-prd-to-wit`** / **`jira-backlog-manager`** | Same idea for Jira shops |

**PulseBoard:** Prefer **`github-backlog-manager`** (this course is on GitHub).

---

### Stage 5 — Sprint planning

**Job:** Choose what to build **now** vs later, in a sensible order.  
**Purpose:** Avoid starting with polish while the core board doesn’t work. Get a vertical slice first.

| Use | Why |
| --- | --- |
| **`github-backlog-manager`** | Orders issues, milestones, sprint-ish planning on GitHub |
| Agile coaching assets / **`product-manager-advisor`** | Helps you say no to scope creep and keep a thin MVP slice |

**PulseBoard:** Sprint 1 = post status + see today’s board. Sprint 2 = harden, tests, docs.

---

### Stage 6 — Implementation

**Job:** Actually change the codebase to deliver a planned slice.  
**Purpose:** This is where code appears — but still with evidence, not vibes.

| Use | Why |
| --- | --- |
| **`RPI Agent`** (or `/rpi` / `/rpi-quick`) | Coordinates Research → Plan → Implement → Review for a coding task, writing durable notes under `.copilot-tracking/` |
| **`/rpi-research`**, **`/rpi-plan`**, **`/rpi-implement`**, **`/rpi-review`** | Same lifecycle one phase at a time (great while learning) |
| **Coding standards instructions** (auto) | Keep Python/FastAPI style consistent without you restating rules every prompt |
| **`hve-builder`** (skill, optional) | Only when you want to create/improve custom HVE prompts/agents for your team |
| Data science generators (optional) | `gen-data-spec`, `gen-jupyter-notebook`, `gen-streamlit-dashboard` if the work is analytics/UI dashboards — not our MVP core |

**PulseBoard:** For each feature slice, use **RPI Agent** (or phase skills). Do **not** use `brd-builder` here.

---

### Stage 7 — Review

**Job:** Decide whether the work is acceptable, and route fixes.  
**Purpose:** “It runs on my machine” is not the same as “it meets the PRD / issue acceptance criteria.”

| Use | Why |
| --- | --- |
| **`/rpi-review`** | Compares implementation evidence to plan + acceptance criteria; records pass/fail style outcomes |
| **`code-review`** | Human-gated multi-perspective review (functional, standards, a11y, security, PR readiness) before you merge |
| **`security-reviewer`** | Looks for common vulnerabilities in the change (different from writing a full security plan) |

**PulseBoard:** `/rpi-review` against MVP AC, then `code-review` on the PR.

---

### Stage 8 — Delivery

**Job:** Land the change: commit, pull request, merge, tag/release.  
**Purpose:** Work isn’t delivered while it lives only on your laptop branch.

| Use | Why |
| --- | --- |
| Git prompts (`git-commit`, pull-request, `git-merge`, etc.) | Consistent commit/PR/merge hygiene instead of messy history |
| ADO build-info prompts (if ADO) | Check pipeline status when that’s your CI home |

**PulseBoard:** Open PR, merge MVP, tag `v0.1.0`.

---

### Stage 9 — Operations

**Job:** Keep the system understandable and recoverable after “it works.”  
**Purpose:** Future you (or a teammate) should start the app and fix common failures without archaeology.

| Use | Why |
| --- | --- |
| **`documentation`** | Audit/author/validate docs so README and runbooks don’t drift from reality |
| Incident-response style prompts | Practice “something broke — what do we do?” without waiting for a real outage |
| **`hve-builder`** (optional) | Codify repeatable ops prompts for your team |

**PulseBoard:** Write `docs/ops/runbook.md` (start/stop, DB file location, common errors).

---

## Quick picker: “I need to…” → use this

| I need to… | Use this | Stage |
| --- | --- | --- |
| Install HVE helpers | `hve-core-installer` / Marketplace **hve-core-all** | 1 |
| Write business requirements | **`brd-builder`** | 2 |
| Explore users/problems deeply | `dt-coach` | 2 |
| Research a technical unknown | `/rpi-research` | 2 or 6 |
| Write product/feature requirements | **`prd-builder`** | 3 |
| Record “we chose X over Y because…” | **`adr-creation`** | 3 |
| Draw the system | `architecture-diagrams` | 3 |
| Turn PRD into GitHub issues | **`github-backlog-manager`** | 4–5 |
| Build a feature in the repo | **`RPI Agent`** | 6 |
| Check if implementation matches the plan | `/rpi-review` | 7 |
| Get a pre-PR code review | **`code-review`** | 7 |
| Merge and release | git commit / PR / merge prompts | 8 |
| Write/maintain runbooks | **`documentation`** | 9 |

---

## Common beginner mistakes

1. **Using RPI Agent to write the BRD** — wrong tool; use `brd-builder`.  
2. **Using brd-builder to write FastAPI code** — wrong stage; finish Discovery/PRD first, then RPI.  
3. **Skipping Plan because “it’s a small change”** — small unclear changes create large messes; tiny *clear* edits can skip full RPI.  
4. **Treating chat history as memory** — HVE wants durable files (`docs/project-planning/`, `.copilot-tracking/`).  
5. **Installing only part of HVE and wondering where agents went** — for this course use **hve-core-all**.

---

## Where we are in the course right now

```text
[x] 1 Setup
[>] 2 Discovery   ← you are here → agent: brd-builder
[ ] 3 Product definition
[ ] 4 Decomposition
[ ] 5 Sprint planning
[ ] 6 Implementation   ← RPI Agent shows up here
[ ] 7 Review
[ ] 8 Delivery
[ ] 9 Operations
```

**Next action:** In VS Code, pick **`brd-builder`** (not RPI Agent), generate the PulseBoard BRD, save it under `docs/project-planning/`, then tell the coach `BRD DRAFTED`.

---

## Architecture of HVE Core (what happens when you enter a prompt)

This section is not “memorize folders.”  
It answers: **when I type something in Copilot at a lifecycle stage, which HVE files get loaded, why those files, and what gets written into my repo.**

### 60-second map: where the recipe files live

HVE helpers are ordinary files shipped by **hve-core-all**. Copilot loads them when you pick an agent or type `/something`.

| Kind | Lives in hve-core under | You meet it as… |
| --- | --- | --- |
| **Agent** | `.github/agents/{collection}/*.agent.md` | Name in the **agent picker** |
| **Prompt** | `.github/prompts/{collection}/*.prompt.md` | Often a `/slash` starter |
| **Skill** | `.github/skills/{collection}/{name}/SKILL.md` (+ optional `scripts/`) | `/rpi-research`, `/rpi-plan`, … |
| **Instruction** | `.github/instructions/{collection}/*.instructions.md` | Silent rules when file types match |
| **Collection** | `collections/*.collection.yml` | The shopping list (e.g. `hve-core-all`) |

```text
collections/hve-core-all.collection.yml  →  picks which of those files ship
        ↓
VS Code extension / plugin
        ↓
Copilot Chat can see them
        ↓
Your repo receives OUTPUTS (BRD, code, .copilot-tracking, …)
```

Paths below use the usual collection folders (`project-planning`, `hve-core`, `coding-standards`, …). Exact filenames can vary slightly by HVE version; the **roles** stay the same.

---

### Universal runtime: every prompt follows this pipe

No matter the stage, Copilot roughly does this:

```mermaid
flowchart TD
    A["1. You enter a prompt<br/>plain text and/or /skill<br/>+ optional agent selected"] --> B["2. Entry file chosen<br/>agent.md OR prompt.md OR SKILL.md"]
    B --> C["3. Why that file?<br/>You picked the agent, or<br/>slash matched a skill/prompt, or<br/>prompt frontmatter points to an agent"]
    C --> D["4. Behavior loaded<br/>tools allowed, handoffs,<br/>what NOT to do"]
    D --> E["5. Instructions may auto-attach<br/>if you touch matching files<br/>e.g. **/*.py → python instructions"]
    E --> F["6. Skills may run<br/>for specialized steps<br/>e.g. RPI phases"]
    F --> G["7. Outputs written to YOUR repo<br/>docs/ or apps/ or .copilot-tracking/"]
```

**Why not every file loads every time?**  
HVE is huge on purpose. Loading `brd-builder` + `security-planner` + `RPI Agent` for one chat would mix jobs. You (or the slash command) pick **one entry door**; that door decides the rest.

---

### Stage 1 — Setup

**Example you type:**  
`Install HVE Core All for this workspace` (or you click the Marketplace extension / run the installer skill)

**What should happen:** Make agents/skills visible. No product BRD, no app code.

```mermaid
flowchart LR
    U["You: install / configure HVE"] --> E["Marketplace extension<br/>ise-hve-essentials.hve-core-all"]
    U --> S["Skill: hve-core-installer<br/>.github/skills/.../hve-core-installer/SKILL.md"]
    E --> C["collections/hve-core-all.collection.yml<br/>WHY: shopping list of stable artifacts"]
    S --> C
    C --> REG["Registers agents/prompts/skills/instructions<br/>into Copilot Chat"]
    REG --> OUT["Output: agent picker populated<br/>RPI Agent, brd-builder, … appear"]
```

| File chosen | Why |
| --- | --- |
| `collections/hve-core-all.collection.yml` | Defines the full stable bundle |
| Extension package / installer skill | Delivers and registers those files |
| Not chosen: `brd-builder`, RPI skills | Wrong job — nothing to specify or code yet |

**Repo output:** tooling ready (maybe workspace settings). Not `apps/pulseboard` features.

---

### Stage 2 — Discovery

**Example you type (agent = `brd-builder`):**  
`Create a BRD for PulseBoard…` (seed with users, goal, out-of-scope)

**What should happen:** Business requirements document. Solution-light. No FastAPI yet.

```mermaid
flowchart TD
    U["You select agent: brd-builder<br/>+ paste seed prompt"] --> A["LOAD<br/>.github/agents/project-planning/brd-builder.agent.md"]
    A --> W["WHY this file?<br/>Job = business requirements<br/>Stage = Discovery<br/>Not a coding lifecycle"]
    W --> X["Explicitly NOT loaded as entry<br/>RPI Agent, prd-builder, /rpi-implement"]
    A --> R["May read your seed + mvp-framing.md<br/>for constraints"]
    R --> O["WRITE<br/>docs/project-planning/*brd.md"]

    opt["Optional other Discovery doors"]
    opt --> DT["dt-coach.agent.md<br/>WHY: problem still fuzzy / need DT"]
    opt --> RS["skills/.../rpi-research/SKILL.md<br/>WHY: one technical unknown blocks decisions"]
    opt --> SP["security-planner.agent.md<br/>WHY: security must shape requirements early"]
```

| File chosen | Why |
| --- | --- |
| `…/agents/project-planning/brd-builder.agent.md` | Owns BRD structure, stays solution-agnostic |
| Optional `dt-coach.agent.md` | User/problem discovery before a crisp BRD |
| Optional `…/skills/…/rpi-research/SKILL.md` | Read-only evidence for a named unknown |
| **Not** RPI implement / coding instructions as the driver | You are defining the problem, not shipping code |

**Repo output:** `docs/project-planning/brd.md` (and maybe `.copilot-tracking/research/…` if you ran research).

---

### Stage 3 — Product definition

**Example you type (agent = `prd-builder`):**  
`Create a PRD for PulseBoard MVP from docs/project-planning/brd.md`

**What should happen:** Features, stories, acceptance criteria. Then lock big tech choices with ADRs.

```mermaid
flowchart TD
    U["Prompt: build PRD from BRD"] --> P["LOAD<br/>prd-builder.agent.md<br/>WHY: product/feature altitude<br/>BRD is not detailed enough to build"]
    P --> BRD["READ<br/>docs/project-planning/brd.md"]
    P --> OUT1["WRITE<br/>docs/project-planning/*prd.md"]

    U2["Later prompt: decide SQLite vs Postgres"] --> ADR["LOAD<br/>adr-creation.agent.md<br/>WHY: durable architecture decision"]
    ADR --> OUT2["WRITE<br/>docs/project-planning/adr/0001-….md"]

    U3["Prompt: draw system context"] --> DIAG["LOAD skill<br/>architecture-diagrams/SKILL.md<br/>WHY: pictures beat long prose"]
    DIAG --> OUT3["WRITE diagram under docs/"]
```

| File chosen | Why |
| --- | --- |
| `prd-builder.agent.md` | Turns business needs into buildable product requirements |
| `adr-creation.agent.md` | Records “we chose X over Y because…” |
| `architecture-diagrams` skill | Shared mental model of components |
| **Not** `github-backlog-manager` yet | Tickets come after the PRD exists |
| **Not** `/rpi-implement` | Spec first; code later |

**Repo output:** PRD, ADRs, diagram — still little or no product code.

---

### Stage 4 — Decomposition

**Example you type (agent = `github-backlog-manager`):**  
`Create GitHub issues from the PulseBoard PRD with acceptance criteria`

**What should happen:** Backlog items, not a giant PR of code.

```mermaid
flowchart TD
    U["Prompt: PRD → issues"] --> A["LOAD<br/>github-backlog-manager.agent.md<br/>WHY: owns issue discovery/triage/creation"]
    A --> PRD["READ<br/>docs/project-planning/*prd.md"]
    A --> MCP["Uses GitHub MCP / gh tools<br/>WHY: issues live on GitHub, not only in markdown"]
    A --> OUT["CREATE GitHub issues<br/>labels, AC, links back to PRD"]
    A -.-> ALT["If team used ADO/Jira instead:<br/>ado-prd-to-wit / jira-prd-to-wit<br/>WHY: same job, different tracker"]
```

| File chosen | Why |
| --- | --- |
| `github-backlog-manager.agent.md` | This course uses GitHub; agent knows backlog workflows |
| PRD file in your repo | Source of truth for what becomes tickets |
| **Not** `brd-builder` | Business doc already done; now splitting work |
| **Not** RPI Agent | You are creating work items, not implementing one |

**Repo / GitHub output:** Issues (and maybe local planning notes). Still not the MVP feature code.

---

### Stage 5 — Sprint planning

**Example you type:**  
`From open PulseBoard issues, propose Sprint 1 as a vertical slice: post status + today’s board`

```mermaid
flowchart TD
    U["Prompt: plan Sprint 1"] --> A["LOAD<br/>github-backlog-manager.agent.md<br/>and/or product-manager-advisor.agent.md"]
    A --> W["WHY?<br/>Order and cut scope — do not start with polish"]
    A --> ISS["READ GitHub issues + PRD AC"]
    A --> OUT["Milestone / sprint ordering<br/>Sprint 1 vs Sprint 2 list"]
```

| File chosen | Why |
| --- | --- |
| `github-backlog-manager.agent.md` | Can reshuffle/milestone issues |
| `product-manager-advisor.agent.md` (optional) | Helps say no to scope creep |
| **Not** `/rpi-implement` | Planning the sprint ≠ writing the board UI yet |

**Output:** Ordered Sprint 1 slice. Implementation still next stage.

---

### Stage 6 — Implementation (RPI is the star)

**Example you type (agent = `RPI Agent` or skills):**  
`Implement Sprint 1 issue #12: POST /statuses and list today’s board`  
or phase-by-phase: `/rpi-research` → `/rpi-plan` → `/rpi-implement`

**What should happen:** Code changes **plus** durable evidence under `.copilot-tracking/`.

```mermaid
flowchart TD
    U["You enter coding task<br/>RPI Agent or /rpi-* "] --> ENTRY{"Entry door"}
    ENTRY -->|agent picker| RA["LOAD agents/.../RPI*.agent.md<br/>WHY: lifecycle wrapper for complex code work"]
    ENTRY -->|/rpi-research| S1["LOAD skills/.../rpi-research/SKILL.md<br/>WHY: evidence gap only"]
    ENTRY -->|/rpi-plan| S2["LOAD skills/.../rpi-plan/SKILL.md<br/>WHY: turn evidence into Pxx tasks"]
    ENTRY -->|/rpi-implement| S3["LOAD skills/.../rpi-implement/SKILL.md<br/>WHY: execute approved plan only"]

    RA --> S1
    RA --> S2
    RA --> S3

    S3 --> INST["AUTO-ATTACH instructions<br/>.github/instructions/coding-standards/*python*<br/>WHY: applyTo matches **/*.py you edit"]
    S1 --> TR["WRITE .copilot-tracking/research/..."]
    S2 --> TP["WRITE .copilot-tracking/plans/... + details + critique"]
    S3 --> TC["WRITE apps/pulseboard/** + .copilot-tracking/changes/..."]

    X["NOT chosen as entry<br/>brd-builder / prd-builder<br/>WHY: specs already exist; this stage changes the product"]
```

| File chosen | Why |
| --- | --- |
| RPI agent and/or `rpi-*` skills | Separates research/plan/implement so Copilot doesn’t “just vibe code” |
| Coding-standards instructions | Auto quality/style when Python (or other) files are touched |
| Prior plan/PRD/issues as inputs | Implementation must follow accepted AC |
| **Not** `brd-builder` / `prd-builder` | Wrong altitude — you’d regenerate docs instead of shipping the slice |

**Repo output:** `apps/pulseboard/…` + `.copilot-tracking/…` artifacts.

---

### Stage 7 — Review

**Example you type:**  
`/rpi-review` against the plan and issue AC  
or select **`code-review`**: `Review my local branch for PulseBoard Sprint 1`

```mermaid
flowchart TD
    U1["/rpi-review"] --> SR["LOAD rpi-review/SKILL.md<br/>WHY: reconcile evidence vs AC<br/>does not rewrite product code"]
    SR --> IN["READ plans + changes + PRD/issue AC"]
    SR --> OUT1["WRITE .copilot-tracking/reviews/logs/..."]

    U2["agent: code-review"] --> CR["LOAD code-review.agent.md<br/>WHY: multi-perspective pre-PR review"]
    CR --> SUB["May dispatch subagents/skills<br/>functional · standards · a11y · security · PR"]
    CR --> OUT2["ONE deduplicated review report"]

    U3["security on the diff"] --> SEC["LOAD security-reviewer.agent.md<br/>WHY: vuln lens on changes<br/>≠ full security-planner"]
```

| File chosen | Why |
| --- | --- |
| `rpi-review` skill | Acceptance vs plan/evidence |
| `code-review.agent.md` (+ subagents) | Human-gated quality pass before merge |
| `security-reviewer.agent.md` | Security on the diff |
| **Not** `/rpi-implement` as the reviewer | Reviewers shouldn’t “fix by rewriting” unless you send work back |

**Repo output:** review markdown / PR comments. Fixes go back to Stage 6.

---

### Stage 8 — Delivery

**Example you type:**  
`/create-pull-request` (or the HVE git/PR prompt your pack exposes):  
`Open a PR for Sprint 1 MVP with summary of validation`

```mermaid
flowchart TD
    U["Prompt: commit / open PR / merge"] --> P["LOAD<br/>.github/prompts/.../*pull-request* or git-*.prompt.md<br/>WHY: delivery mechanics, not feature design"]
    P --> A["May delegate to a small agent<br/>via prompt frontmatter agent: …"]
    A --> G["Uses git + GitHub tools"]
    G --> OUT["PR body, commits, merge, tag v0.1.0"]
    X["NOT brd-builder / RPI full rebuild<br/>WHY: you are shipping existing work"]
```

| File chosen | Why |
| --- | --- |
| Git / PR **prompts** (and any linked agent) | Standardize commit/PR/merge quality |
| Existing review + change logs | PR should cite how you validated |
| **Not** Discovery/Product builders | Specs are done; this stage lands the change |

**Output:** GitHub PR, merge, release tag.

---

### Stage 9 — Operations

**Example you type (agent = `documentation`):**  
`Author a runbook for PulseBoard: start, stop, DB path, common failures`

```mermaid
flowchart TD
    U["Prompt: write runbook / audit docs"] --> D["LOAD documentation.agent.md<br/>WHY: docs audit/author/validate modes"]
    D --> APP["READ apps/pulseboard + README"]
    D --> OUT["WRITE docs/ops/runbook.md"]
    U2["Optional: incident tabletop"] --> IR["LOAD incident-response prompt/skill<br/>WHY: practice recovery without a real outage"]
```

| File chosen | Why |
| --- | --- |
| `documentation.agent.md` | Keeps ops docs aligned with the real app |
| Incident-response prompt/skill | Ops readiness |
| **Not** `prd-builder` | You are maintaining a shipped system, not redefining MVP |

**Repo output:** `docs/ops/…`, updated README as needed.

---

### Side-by-side: same product, different stage ⇒ different files

```mermaid
flowchart TB
    Q["User prompt about PulseBoard"] --> ST{"Which stage job?"}
    ST -->|Discovery| F2["brd-builder.agent.md<br/>→ docs/project-planning/brd.md"]
    ST -->|Product definition| F3["prd-builder.agent.md + adr-creation.agent.md<br/>→ prd.md + adr/*.md"]
    ST -->|Decomposition / sprint| F45["github-backlog-manager.agent.md<br/>→ GitHub issues / milestone"]
    ST -->|Implementation| F6["RPI agent + rpi-* SKILL.md<br/>+ python instructions on *.py<br/>→ apps/ + .copilot-tracking/"]
    ST -->|Review| F7["rpi-review SKILL.md / code-review.agent.md<br/>→ review logs"]
    ST -->|Delivery| F8["git/PR prompt.md<br/>→ PR + merge"]
    ST -->|Operations| F9["documentation.agent.md<br/>→ docs/ops/runbook.md"]
```

### Remember

1. **You choose the entry door** (agent picker or `/skill`) — that choice selects the primary file.  
2. **That file’s job** decides what else may load (skills, subagents, instructions).  
3. **Instructions hitchhike** when matching files are edited; they are not a stage picker.  
4. **Outputs land in your repo** (`docs/`, `apps/`, `.copilot-tracking/`) — HVE’s `.agent.md` / `SKILL.md` files stay in the HVE package unless you customize them.

You do not need every path memorized.  
You need this reflex: *“What stage am I in → which entry file → why → where does the answer get written?”*
