# 🏰 Travian Agent — Claude Plays Travian

> An autonomous LLM agent that plays [Travian Legends](https://www.travian.com/) end-to-end: it reads the official game guides, builds its own automation library on the fly, keeps a persistent memory across sessions through plain Markdown files, and runs in a continuous loop of sensing, deciding, acting, and sleeping.

---

## ⚠️ Disclaimer

This is an **educational / research project**, born out of curiosity about how far LLM agents can go when given a long-horizon, open-ended goal in a "static" web environment.

**Automating gameplay violates [Travian's Terms & Conditions](https://www.travian.com/international/gamerules)** and can get an account permanently banned. This repo is meant to be run against a **local, sandboxed instance** of the game (or any environment you are explicitly authorized to test against) — never against a live server or a real account.

By using this code you take full responsibility for how and where you run it.

---

## 🧠 What this actually is

Travian is a browser-only strategy game: you manage four resources (wood, clay, iron, crop), upgrade buildings, train troops, raid, form alliances, and expand by founding new villages. Everything happens on static pages — no canvas, no real-time rendering — which makes it an ideal sandbox for testing how an LLM agent behaves when it has to:

- learn the rules of a system from documentation alone,
- act inside a real (simulated) browser via [Playwright](https://playwright.dev/),
- build its own tools/automation as it goes,
- maintain long-term plans and memory across sessions that have **no shared context**,
- and balance "play efficiently" against "behave like a believable, sandboxed agent."

The project went through two major iterations — both are documented here.

---

## 🗂 Project structure

```
.
│   ── Current version (v2: Claude + /goal) ──
├── AGENT.md                  # System prompt / operating manual for the current agent
├── Scripts/                  # JS snippets injected into the live browser session
│   └── INDEX.md              # Script catalog + automation coverage map (missing/partial/working/broken)
├── Guide/                    # Game knowledge distilled from the official Travian guides (atomic .md files)
│   └── Playbook.MD           # Strategic best practices — updated by the agent itself over time
├── GameState.MD              # Live snapshot: resources, buildings, queues, troops, villages
├── TODO.MD                   # Short/medium/long-term strategic plan, updated dynamically
├── errors.md                 # Recurring bugs, broken selectors, game quirks and how to avoid them
├── logs/                     # One Markdown log per session: {yyyy-mm-dd_hh-mi-ss}.md
├── chromium_profile/         # Persistent Playwright browser profile (cookies, login session)
│
└── legacy/                   # v1 — the opencode + GPT 5.5 setup, fully self-contained
    ├── AGENT.md              # v1 system prompt (Gameplay/Engineering modes, opencode-based)
    ├── autorun.py            # Re-launches the agent session in a loop, reading sleep.md
    ├── sleep.md              # Seconds of inactivity decided by the agent (fallback: 600s)
    ├── sleep_reason.md       # Why the agent chose to sleep
    ├── AutomationCoverage.MD # Automation status map: repetitive actions, priorities, status
    ├── GameState.MD          # v1 game-state snapshot (resources, buildings, progress)
    ├── TODO.MD               # v1 strategic plan (short/medium/long-term goals)
    ├── errors.md             # v1 error tracking
    ├── logs/                 # v1 session logs ({timestamp}.md)
    ├── Guide/                # v1 game knowledge (atomic .md files)
    │   └── Playbook.MD       # v1 strategies
    ├── Codebase/             # Python automation modules (one file per feature/action)
    │   └── README.md         # Codebase docs: module descriptions, parameters, usage examples
    └── chromium_profile/     # v1 persistent Playwright browser profile
```

---

## 🛠 Two versions, two philosophies

### v1 — "Legacy" (opencode + GPT 5.5)

Everything for this version lives under [`legacy/`](./legacy/), fully self-contained:

- One Python-driven loop (`legacy/autorun.py`) restarts the agent's session every time it ends, reading the sleep duration from `legacy/sleep.md` (and its reason from `legacy/sleep_reason.md`).
- Two distinct operating modes, driven by `legacy/AutomationCoverage.MD` (the automation status map — repetitive actions with priorities and `missing`/`partial`/`working`/`broken` status):
  - **Gameplay Mode** — plays the game via Playwright; whenever it spots a repetitive, un-automated action it adds it to `AutomationCoverage.MD` as `missing`.
  - **Engineering Mode** — when high-priority gaps pile up, the agent stops playing for a whole session and writes Python automation (`cloudscraper` + `bs4`) into `legacy/Codebase/`, documenting each module in `legacy/Codebase/README.md`.
- Long-term memory lives entirely in Markdown files under `legacy/` (`TODO.MD`, `GameState.MD`, `errors.md`, `logs/`, plus the `Guide/` knowledge base), since each session starts with a blank context.
- The full prompt for this version is [`legacy/AGENT.md`](./legacy/AGENT.md).

### v2 — Current (Claude + `/goal`)

- A **single, continuous session** — no restart script, no mode switching. Sensing, deciding, acting, automating, and sleeping all happen in one unified loop.
- Automation is written as **JavaScript snippets injected directly into the live Playwright page** (`./Scripts/`), rather than a standalone Python codebase — more accurate, easier to keep in sync with the game's DOM, and less prone to the agent "over-fitting" to its own scripts.
- The agent maintains its own `Scripts/INDEX.md` (automation catalog + coverage map), `GameState.MD`, `TODO.MD`, `errors.md`, and session logs.
- Sleep durations are computed adaptively from `GameState.MD` (e.g. "next building finishes in 1140s"), with a 600s fallback and a 10800s cap.

The full operating manual — including the operating loop, sleep policy, and script-writing discipline — lives in [`AGENT.md`](./AGENT.md).

---

## 🚀 Getting started

> Again: this is meant to run against a **local/sandboxed instance you own or are explicitly authorized to test** — never a live server or a real account.

### Current version (Claude Code)

1. **Install [Claude Code](https://docs.claude.com/en/docs/claude-code).**

2. **Clone the repo:**
   ```bash
   git clone https://github.com/danlig/travian-agent.git
   cd travian-agent
   ```

3. **Fill in your environment details in `AGENT.md`** (sandbox URL, user credentials).

4. **Start Claude Code** in the project folder and give it a single prompt:
   ```
   /goal read AGENT.md
   ```
   The `/goal` command keeps the agent running in one continuous session until the objective is reached, which is exactly what a long-horizon game like this needs.

   > **About `--dangerously-skip-permissions`:** Claude Code normally asks for confirmation before each tool action (running commands, editing files, etc.). You *can* launch it with `claude --dangerously-skip-permissions` to skip those prompts so the agent runs unattended — but, as the flag name screams, this lets it execute anything without asking. **Only ever use it inside an isolated, throwaway environment** (a container or VM you don't care about), never on your main machine. If in doubt, leave it off and approve actions manually.

5. Watch it learn the game from `Guide/`, start playing, and grow its own `Scripts/` library over time. Check `logs/` for the full audit trail of every decision.

### Legacy version (opencode + GPT 5.5)

```bash
python legacy/autorun.py   # requires opencode configured with your model, using legacy/AGENT.md as its prompt
```

### Pointing the agent at a sandbox (reverse proxy)

`AGENT.md` is written so the agent talks to `localhost:3000`. The intended way to provide that is a **self-hosted / sandboxed game instance** behind a local reverse proxy, so the agent never touches a production server. A reverse proxy (e.g. [Caddy](https://caddyserver.com/), nginx, …) just forwards `localhost:3000` to whatever sandbox host you control:

```caddyfile
# Caddyfile — forwards localhost:3000 to YOUR OWN sandbox/test host.
# Replace the placeholder. Do NOT point this at a live/production Travian server.
:3000 {
    reverse_proxy https://your-sandbox-host.example {
        header_up Host your-sandbox-host.example
        transport http {
            tls_server_name your-sandbox-host.example
        }
    }
}
```

```bash
caddy run --config Caddyfile
```

> ⚠️ **Read this before changing the placeholder.** Pointing this proxy at a real, public Travian server and running the agent against it violates [Travian's Terms & Conditions](https://www.travian.com/international/gamerules), can get the account permanently banned, and means the agent is interacting with real human players without disclosure. This repo does **not** support that. `your-sandbox-host.example` must be an environment you own or are explicitly authorized to test against.

---

## 📓 Files the agent maintains by itself

| File | Purpose |
|---|---|
| `GameState.MD` | Live snapshot of resources, buildings, queues, troops, villages |
| `TODO.MD` | Strategic plan — short/medium/long-term goals, updated every iteration |
| `Guide/Playbook.MD` | Best practices and "lessons learned", evolves as the agent plays |
| `Scripts/INDEX.md` | Catalog of all injected JS snippets + automation coverage map |
| `errors.md` | Recurring bugs, broken selectors, and how to avoid them next time |
| `logs/*.md` | Per-session log: what was observed, decided, done, and why |

---

## 🤝 Contributing

Suggestions, issues, and PRs are very welcome — especially around:

- improving the prompts (`AGENT.md`, `Guide/Playbook.MD`) to make the agent play better and reason more effectively
- making the whole loop more efficient — fewer tokens, smarter sleeping, better long-term planning
- new or improved sensor/action scripts for `./Scripts/`

If you have questions or run into issues, open a GitHub issue — happy to help.
