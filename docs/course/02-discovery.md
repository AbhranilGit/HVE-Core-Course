# Module 2 — Discovery

HVE Stage 2. Goal: turn the MVP framing into a Business Requirements Document (BRD) with explicit assumptions and out-of-scope.

## Why this module exists

Implementation without discovery invents requirements mid-coding. HVE’s `brd-builder` (and optional `/rpi-research`) force evidence and boundaries first.

## Steps

### 2.1 Problem brief (you → coach)

Answer four prompts in chat (short bullets are fine):

1. Who is the primary user?
2. What pain does PulseBoard remove?
3. What does “success” look like after two weeks of use?
4. What must we explicitly refuse to build in MVP?

### 2.2 Draft BRD with HVE (`brd-builder`)

In VS Code Copilot Chat, select **brd-builder** if available (or ask Copilot for the BRD builder agent from hve-core-all). Paste the coach-provided prompt. Save output to `docs/project-planning/brd.md`.

### 2.3 Research gap check (`/rpi-research` only if needed)

If the BRD has open technical unknowns that block Product Definition, run `/rpi-research`. Otherwise skip.

### 2.4 Module 2 exit

- [ ] `docs/project-planning/brd.md` exists
- [ ] In-scope / out-of-scope match MVP framing
- [ ] Open questions listed (if any)
- [ ] Coach marks Discovery complete

**Do not write FastAPI code in this module.**
