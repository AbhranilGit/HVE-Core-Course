# PulseBoard — Setup Confirmation

| Field | Value |
| --- | --- |
| **Product** | PulseBoard |
| **Document type** | Setup confirmation (setup output) |
| **Status** | Pending verification |
| **Source checklist** | [`../input/setup-checklist.md`](../input/setup-checklist.md) |
| **HVE stage** | Stage 1 — Setup output |
| **Confirmed by** | _name_ |
| **Confirmed on** | _YYYY-MM-DD_ |

---

## 1. Purpose of this document

Durable proof that Stage 1 is complete: the HVE crew is installed, the Python environment works, and the repo scaffolding is in place.

Do **not** start Discovery prompts until the checklist below is green (or exceptions are noted).

---

## 2. Verification results

### 2.1 Editor and Copilot

| Check | Result | Evidence / notes |
| --- | --- | --- |
| Repo open as VS Code workspace root | ☐ Pass / ☐ Fail | |
| GitHub Copilot Chat works | ☐ Pass / ☐ Fail | |
| **HVE Core - All** installed | ☐ Pass / ☐ Fail | Extension id: `ise-hve-essentials.hve-core-all` |
| VS Code reloaded after install | ☐ Pass / ☐ Fail | |

### 2.2 HVE helpers

| Helper | Visible in picker? | Notes |
| --- | --- | --- |
| `brd-builder` | ☐ Yes / ☐ No | Required for Stage 2 |
| `prd-builder` | ☐ Yes / ☐ No | Required for Stage 3 |
| `RPI Agent` | ☐ Yes / ☐ No | Required for Stage 6 |
| Other (backlog / review / docs) | ☐ Yes / ☐ No / ☐ N/A | List names if useful: |

### 2.3 Python environment

| Check | Result | Evidence / notes |
| --- | --- | --- |
| Env name | — | Expected: `hve-env` (or note alternative) |
| `python --version` | ☐ Pass / ☐ Fail | Must be **3.12.x** |
| Optional `pip install -e ".[dev]"` | ☐ Pass / ☐ Fail / ☐ Skipped | |

Commands used:

```bash
conda create -n hve-env python=3.12
conda activate hve-env
python --version
```

Paste or note actual output:

```text
_paste here_
```

### 2.4 Repository scaffolding

| Path | Present? |
| --- | --- |
| `src/pulseboard/` | ☐ Yes / ☐ No |
| `tests/` | ☐ Yes / ☐ No |
| `scripts/` | ☐ Yes / ☐ No |
| `docs/guides/` | ☐ Yes / ☐ No |
| `lifecycle/` | ☐ Yes / ☐ No |
| `.copilot-tracking/` | ☐ Yes / ☐ No |
| `pyproject.toml` | ☐ Yes / ☐ No |
| `README.md` | ☐ Yes / ☐ No |

### 2.5 Optional sanity

| Check | Result | Notes |
| --- | --- | --- |
| `git status` | ☐ Pass / ☐ Fail / ☐ Skipped | |

---

## 3. Exceptions and follow-ups

| Item | Impact | Follow-up |
| --- | --- | --- |
| _none / describe_ | | |

---

## 4. Stage gate

| Gate | Met? |
| --- | --- |
| HVE helpers required for Discovery + Implementation are visible | ☐ |
| Python 3.12 environment works | ☐ |
| Repo scaffolding present | ☐ |
| No blockers that prevent opening `brd-builder` | ☐ |

**Stage 1 complete:** ☐ Yes — proceed to Discovery · ☐ No — fix failures above first

---

## 5. HVE handoff (after confirmation)

| Step | Action |
| --- | --- |
| **Next stage** | Stage 2 — Discovery |
| **Input** | [`lifecycle/02-discovery/input/mvp-framing.md`](../../02-discovery/input/mvp-framing.md) |
| **Helper** | **`brd-builder`** (do **not** use RPI Agent yet) |
| **Output** | `lifecycle/02-discovery/output/brd.md` |

Guide: [docs/guides/README.md](../../../docs/guides/README.md) — Stage 2 prompt.
