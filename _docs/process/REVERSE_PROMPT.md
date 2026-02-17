# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P5 Getting Started with Claude Code on OpenBSD

---

## Verification

### Claude Code on OpenBSD Article

- New draft at `_drafts/claude_code_getting_started_on_openbsd.markdown`.
- Covers npm-only installation (no port or package exists for OpenBSD).
- Documents bash installation and `/bin/bash` symlink requirement.
- Documents ripgrep configuration via `USE_BUILTIN_RIPGREP` setting.
- Critical warning against running native installer or `claude install` (downloads incompatible Linux binary, breaks npm installation).
- Documents Bun runtime incompatibility and removed Linux compatibility layer.
- Hello World section provides a single prompt that generates a curses-based system information dashboard using only OpenBSD base system (cc, make, curses).
- Limitations section more extensive than FreeBSD article due to harder platform.
- 12 references across 4 categories (Claude, GitHub, OpenBSD, Related Post). All URLs verified (9 HTTP 200, 1 npmjs.com confirmed indexed via web search, 2 post_url).
- References companion posts A74 and FreeBSD article via post_url.
- No article number assigned. Not slotted for publication. Pre-release candidate status.

---

## Questions for Human Review

- The OpenBSD article references the FreeBSD article via `post_url`. The FreeBSD article must be published before the OpenBSD article for the reference to resolve.
- Verify that `doas pkg_add node` installs a Node.js version between 18 and 24 on current OpenBSD. The article does not specify which LTS version is available.
- Verify that `npm install -g @anthropic-ai/claude-code` completes successfully on OpenBSD.
- The `USE_BUILTIN_RIPGREP` setting is documented as `"0"` (string) in settings.json. Verify this format works on OpenBSD.
- The Hello World prompt has not been tested on OpenBSD. Run it and verify that Claude Code can research sysctl MIBs, generate C code, and compile with base system tools.
- The article assumes `claude -p` (non-interactive mode) works on OpenBSD for the verification step. Verify this.
- OpenBSD uses `cc` in base. The article does not specify whether this is clang or gcc on the target architecture. Verify and update if needed.
- Software Versions section needs output filled in on OpenBSD hardware.
- The OpenBSD Linux compatibility removal reference links to an InfoWorld article about OpenBSD 6.0 (2016). Verify this is still the canonical reference.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 3 pre-release candidates: Android Development on FreeBSD, Claude Code on FreeBSD, Claude Code on OpenBSD.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article (post_url reference).
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
