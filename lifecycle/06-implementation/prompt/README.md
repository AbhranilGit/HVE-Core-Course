# Stage 6 — Implementation prompts

Implement **one issue at a time**, in the order below.  
**Authoritative scope (in-repo):** [`lifecycle/04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) (TEMP-N / issue #N section). GitHub links are for tracking only.  
For **each** issue, run and **persist** Research → Plan → Implement, and **verify** the gate before the next phase.

| Order | Issue | Prompt | RPI folder | Sprint |
| --- | --- | --- | --- | --- |
| 1 | [#2](https://github.com/AbhranilGit/HVE-Core-Course/issues/2) | [issue-02.md](issue-02.md) | [`../output/issue-02/`](../output/issue-02/) | 1 |
| 2 | [#6](https://github.com/AbhranilGit/HVE-Core-Course/issues/6) | [issue-06.md](issue-06.md) | [`../output/issue-06/`](../output/issue-06/) | 1 |
| 3 | [#4](https://github.com/AbhranilGit/HVE-Core-Course/issues/4) | [issue-04.md](issue-04.md) | [`../output/issue-04/`](../output/issue-04/) | 1 |
| 4 | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) | [issue-05.md](issue-05.md) | [`../output/issue-05/`](../output/issue-05/) | 1 |
| 5 | [#3](https://github.com/AbhranilGit/HVE-Core-Course/issues/3) | [issue-03.md](issue-03.md) | [`../output/issue-03/`](../output/issue-03/) | 1 |
| 6 | [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9) | [issue-09.md](issue-09.md) | [`../output/issue-09/`](../output/issue-09/) | 1 |
| 7 | [#10](https://github.com/AbhranilGit/HVE-Core-Course/issues/10) | [issue-10.md](issue-10.md) | [`../output/issue-10/`](../output/issue-10/) | 2 |
| 8 | [#8](https://github.com/AbhranilGit/HVE-Core-Course/issues/8) | [issue-08.md](issue-08.md) | [`../output/issue-08/`](../output/issue-08/) | 2 |
| 9 | [#7](https://github.com/AbhranilGit/HVE-Core-Course/issues/7) | [issue-07.md](issue-07.md) | [`../output/issue-07/`](../output/issue-07/) | 2 |

## How to invoke (RPI Agent)

1. Select **RPI Agent** in Copilot Chat.  
2. Paste the phase prompt as-is (paths are in the `task=` text — no manual attach).  
3. Run **`/rpi`** with:

```text
/rpi continue={1|2|3} task=...
```

| `continue` | Phase | Paths the prompt tells the agent to read | Persist to |
| --- | --- | --- | --- |
| `1` | Research | backlog snapshot | `output/issue-NN/research.md` |
| `2` | Plan | **`research.md`** + backlog snapshot | `output/issue-NN/plan.md` |
| `3` | Implement | **`plan.md`** (+ `research.md` for background) | `output/issue-NN/implement.md` + code |

Do **not** use `continue=all` while you are gating phases. Prefer a new chat or `/clear` between phases if context gets noisy.

## Per-issue RPI loop

1. **Research** — `/rpi continue=1` → fill `research.md` → verify Research  
2. **Plan** — `/rpi continue=2` (prompt requires reading `research.md`) → fill `plan.md` → verify Plan  
3. **Implement** — `/rpi continue=3` (prompt requires reading `plan.md`) → code + `implement.md` → verify Implement  
4. Only then open the **next** issue prompt

If `research.md` / `plan.md` is missing, the prompt tells the agent to **stop** rather than invent the prior phase. Do not ask the user to attach files.

Also keep agent session evidence under `.copilot-tracking/` when present.  
Convention details: [`../output/README.md`](../output/README.md).

**Rules:** do not skip phases; Plan must reference Research; Implement must reference Plan; do not skip ahead in Sprint 1; do not widen MVP.
