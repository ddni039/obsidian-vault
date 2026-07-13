---
title: "NousResearch/hermes-agent GitHub Raw Source v0.18.0"
created: "2026-07-04"
source: "git clone https://github.com/nousresearch/hermes-agent.git (bare, /tmp/hermes-agent-git)"
tags: [raw, github, hermes-agent, source]
---

# NousResearch/hermes-agent — GitHub Raw Source v0.18.0

## Repository Info

- **URL**: https://github.com/nousresearch/hermes-agent
- **Default branch**: main (confirmed via HEAD)
- **Clone**: Bare clone at `/tmp/hermes-agent-git`
- **Total commits** (main branch): ~50 visible, from 2026-03-12 to 2026-07-03
- **Version range analyzed**: v0.2.0 (2026-03-12) → v0.18.0 (2026-07-01)

---

## All Tags (19 releases)

| Tag | Semantic Ver | Date |
|-----|-------------|------|
| v2026.3.12 | v0.2.0 | 2026-03-12 |
| v2026.3.17 | v0.3.0 | 2026-03-17 |
| v2026.3.23 | v0.4.0 | 2026-03-23 |
| v2026.3.28 | v0.5.0 | 2026-03-28 |
| v2026.3.30 | v0.6.0 | 2026-03-30 |
| v2026.4.3  | v0.7.0 | 2026-04-03 |
| v2026.4.8  | v0.8.0 | 2026-04-08 |
| v2026.4.13 | v0.9.0 | 2026-04-13 |
| v2026.4.16 | v0.10.0 | 2026-04-16 |
| v2026.4.23 | v0.11.0 | 2026-04-23 |
| v2026.4.30 | v0.12.0 | 2026-04-30 |
| v2026.5.7  | v0.13.0 | 2026-05-07 |
| v2026.5.16 | v0.14.0 | 2026-05-16 |
| v2026.5.28 | v0.15.0 | 2026-05-28 |
| v2026.5.29 | v0.15.1 | 2026-05-28 |
| v2026.5.29.2 | v0.15.2 | 2026-05-29 |
| v2026.6.5  | v0.16.0 | 2026-06-05 |
| v2026.6.19 | v0.17.0 | 2026-06-19 |
| v2026.7.1  | v0.18.0 | 2026-07-01 |

Non-release (backup) tags: `backup/opentui-prestrip-20260616-1950`, `backup/precopystrip-20260616-2058`, `clean-before-remerge`, `desktop-pr20059-installers`, `merge-commit-backup`, `premerge-oh-god`

---

## Branches (partial — feature branches only)

Notable active branches visible in refs:
- `bb/skills-renovate` — skills renovation
- `ethie/ts-desktop` — TypeScript desktop refactor
- `remove-brew-pip-publishing` — remove brew/pip publishing
- `deprecate-brew-pip` — deprecate brew/pip install paths
- `hermes/hermes-fe37d0d6` — gateway feature
- `salvage/vision-image-source-resolver` — vision fix salvage
- `ethie/ts-desktop` — desktop TypeScript conversion

---

## Commit Log (Last 50, chronological from earliest)

```
2026-05-26 Jiahui-Gu: fix(agent): prefer native vision over auxiliary fallback in auto mo...
2026-05-31 Maxim Esipov: fix: route gateway images by session model override
2026-06-06 liuhao1024: fix(image_routing): check stripped custom:<name> provider key for v...
2026-06-22 Jacky Zeng: fix(vision): forward custom-endpoint credentials in vision auto-de...
2026-06-26 LeonSGP43: fix(model): preserve named custom provider slug
2026-06-28 liuhao1024: fix(vision): read auxiliary model from config.yaml before env var
2026-06-29 ethernet: feat(desktop): ts-ify everything
2026-06-30 Shannon Sands: Add dashboard Hermes console websocket
2026-06-30 Shannon Sands: Add safe Hermes console REPL
2026-07-01 Shannon Sands: Add dashboard Hermes console UI
2026-07-02 Eugeniusz Gilewski: fix(security): remove model-controlle...
2026-07-02 ethernet: feat(install): warn pip/Homebrew installs are u...
2026-07-02 ethernet: feat: print install method when running --version
2026-07-02 ethernet: fix(nix): make `hermes` in developement environ...
2026-07-02 ethernet: fix: correct detect install method when running...
2026-07-03 Brooklyn Nicholson: fix(desktop,gateway,mcp): post-merge ...
2026-07-03 Brooklyn Nicholson: fix(tts): coerce direct-only OpenAI m...
2026-07-03 Brooklyn Nicholson: refactor(desktop): adopt shared utils...
2026-07-03 Jai Suphavadeeprasit: Keep Harbor eval tunnel healthy
2026-07-03 Jonny Kovacs: fix(cron): run jobs under the profile secre...
2026-07-03 Que0x: fix(matrix): isolate per-event failures in _dispat...
2026-07-03 SHL0MS: add `cdp`: launch/detect operator chrome over CDP...
2026-07-03 SHL0MS: blocked-tail pass: blind opt-out default, email f...
2026-07-03 SHL0MS: field-report fixes: dob pre-warn, .env creds, sho...
2026-07-03 Sabin Iacob: test(web_tools): regression for plugin-regis...
2026-07-03 Shannon Sands: Use shared ANSI stripping in Hermes Console
2026-07-03 Teknium: fix(moa): restore prompt caching for the aggrega...
2026-07-03 Teknium: fix(update): harden #57659 follow-ups — task res...
2026-07-03 dsad: fix(browser): block Camofox input on private pages
2026-07-03 dsad: fix(image-gen): guard local provider inputs against...
2026-07-03 emozilla: fix(vision): unified image-source resolver + te...
2026-07-03 emozilla: security(ci): pass untrusted refs through env, ...
2026-07-03 ethernet: time to cook
2026-07-03 kshitijk4poor: chore(release): map iacobs@webflakes.com -...
2026-07-03 kshitijk4poor: chore: add AUTHOR_MAP entry for PR #57692 ...
2026-07-03 kshitijk4poor: fix(image-gen): route local-input credenti...
2026-07-03 kshitijk4poor: fix(web_tools): delegate backend availabil...
2026-07-03 kshitijk4poor: fix(xai): route video-gen local inputs thr...
2026-07-03 kshitijk4poor: perf(console): cache CLI-surface summaries...
2026-07-03 kshitijk4poor: refactor(web_tools): single registry autho...
2026-07-03 kshitijk4poor: test(cron): regression test for run_one_jo...
2026-07-03 liuhao1024: fix(dashboard): block .env files from managed...
2026-07-03 liuhao1024: fix(dashboard): use pattern match for .env se...
2026-07-03 srojk34: fix(browser): apply private-page guard to browse...
2026-07-03 srojk34: security(gateway): anchor api_server MEDIA tag r...
2026-07-03 teknium1: chore: add suninrain086 to AUTHOR_MAP for salva...
2026-07-03 teknium1: feat(gateway): add /sessions search <query>
2026-07-03 teknium1: fix(dashboard): make .env sensitive-file guard ...
2026-07-03 teknium1: test(gateway): accept kwargs in _decide_image_i...
2026-07-03 teknium1: test(vision): adapt salvaged config-priority te...
```

---

## Diff Stats Between Key Versions

| Version Diff | Files Changed | Insertions | Deletions |
|------------|-------------|-----------|----------|
| v0.4.0 → v0.18.0 | ~5957 | +1,817,479 | -118,260 |
| v0.3.0 → v0.4.0 | 467 | +82,865 | -7,991 |

---

## README (v0.18.0 / HEAD)

Self-improving AI agent built by Nous Research. Built-in learning loop — creates skills from experience, improves during use, persists knowledge across sessions.

Key features:
- TUI with multiline editing, slash-command autocomplete, conversation history
- 20+ platforms: Telegram, Discord, Slack, WhatsApp, Signal, CLI
- Closed learning loop: agent-curated memory, autonomous skill creation, FTS5 session search
- Scheduled automations (cron)
- Delegates/subagents
- 6 terminal backends: local, Docker, SSH, Singularity, Modal, Daytona

Install:
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
Windows: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`

---

## Notable File Count (v0.18.0 tree)

Total files in repo: large monorepo with `agent/`, `hermes_cli/`, `apps/desktop/`, `ui-tui/`, `website/`, `optional-skills/`, `acp_adapter/`, `acp_registry/`, `agent/` directories. Python + TypeScript + Node.js.

No CHANGELOG.md file committed to repo (changelog managed via git tags + release notes).
