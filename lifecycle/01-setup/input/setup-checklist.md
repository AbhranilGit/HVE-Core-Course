# PulseBoard — Setup Checklist

| Field | Value |
| --- | --- |
| **Product** | PulseBoard |
| **Document type** | Setup checklist (setup input) |
| **Status** | Ready to execute |
| **Audience** | Engineer starting the HVE journey |
| **HVE stage** | Stage 1 — Setup input |
| **Helper** | Marketplace **HVE Core - All** (`ise-hve-essentials.hve-core-all`) |
| **Next artifact** | `lifecycle/01-setup/output/setup-confirmation.md` |

---

## 1. Purpose of this document

Get the **crew and machine** ready before anyone talks features, writes a BRD, or opens the RPI Agent.

In HVE terms:

- This file is the **durable input** for Stage 1 — the checklist you follow.
- Completing it produces **confirmed setup notes** in `output/`.
- **Not yet:** BRD, PRD, tickets, API, or board UI.

---

## 2. Prerequisites (bring these)

| Requirement | Notes |
| --- | --- |
| **VS Code** | Current stable build |
| **GitHub Copilot** | Chat enabled and signed in |
| **This repository** | Cloned locally; you can open the workspace root |
| **Python 3.12+** | Prefer conda env named `hve-env` |
| **Git** | For later delivery; useful now for status sanity |
| **Browser** | To verify the app later (not required to finish setup) |

---

## 3. Tooling checklist

Work top to bottom. Record evidence in the output confirmation when done.

### 3.1 Editor and Copilot

- [ ] Open this repo as the VS Code workspace root
- [ ] Confirm GitHub Copilot Chat opens and responds
- [ ] Install extension **[HVE Core - All](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)**
- [ ] Reload VS Code after install

### 3.2 HVE helpers visible

In Copilot Chat agent / mode picker, confirm at least:

- [ ] `brd-builder` (Stage 2 — Discovery)
- [ ] `prd-builder` (Stage 3 — Product definition)
- [ ] `RPI Agent` (Stage 6 — Implementation)
- [ ] Related helpers appear as available (e.g. backlog / review / documentation — names may vary slightly by extension version)

### 3.3 Python environment

```bash
conda create -n hve-env python=3.12
conda activate hve-env
python --version   # expect 3.12.x
```

- [ ] `hve-env` (or equivalent) activates
- [ ] `python --version` reports **3.12.x** (matches `requires-python = ">=3.12"` in `pyproject.toml`)
- [ ] Optional: `pip install -e ".[dev]"` from repo root succeeds when you are ready to run tests

### 3.4 Repository scaffolding present

Confirm these paths exist (they should already be in the repo):

- [ ] `src/pulseboard/` (application package)
- [ ] `tests/`
- [ ] `scripts/`
- [ ] `docs/guides/` (HVE lifecycle guide)
- [ ] `lifecycle/` (stage input/output folders)
- [ ] `.copilot-tracking/` (durable RPI artifacts later)
- [ ] `pyproject.toml` and `README.md`

### 3.5 Sanity commands (optional but recommended)

```bash
git status
conda activate hve-env && python --version
```

- [ ] `git status` runs without error
- [ ] Python version check matches §3.3

---

## 4. Done means / not yet

| Done when | Explicitly not yet |
| --- | --- |
| HVE Core All installed; key helpers visible in Copilot | BRD / PRD written |
| Python 3.12 env works | FastAPI app or board UI |
| Repo folders above exist | GitHub issues / sprint plan |
| Confirmation written to `output/setup-confirmation.md` | Using **RPI Agent** to invent product scope |

---

## 5. HVE handoff

| Step | Action |
| --- | --- |
| **Now** | Execute §§3.1–3.4; fill `lifecycle/01-setup/output/setup-confirmation.md` |
| **Next stage** | Stage 2 — Discovery |
| **Next input** | `lifecycle/02-discovery/input/mvp-framing.md` |
| **Next helper** | Select **`brd-builder`** (not RPI Agent) |
| **Next output** | `lifecycle/02-discovery/output/brd.md` |

Guide: [docs/guides/README.md](../../../docs/guides/README.md) — Stage 1 and Stage 2.
