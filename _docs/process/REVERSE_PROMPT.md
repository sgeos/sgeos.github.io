# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P4 Getting Started with Claude Code on FreeBSD

---

## Verification

### Claude Code on FreeBSD Article

- New draft at `_drafts/claude_code_getting_started_on_freebsd.markdown`.
- Covers three installation methods: ports (preferred), packages, and npm.
- Documents shebang fix for `/bin/bash` vs `/usr/local/bin/bash`.
- Documents ripgrep configuration for npm installations. Port handles this automatically.
- Hello World section provides a single prompt that generates a curses-based system information dashboard using only FreeBSD base system (cc, make, ncurses).
- Limitations section documents unsupported platform status, Linux jail incompatibility, and version lag.
- 12 references across 4 categories (Claude, FreeBSD, GitHub, Related Post). All URLs verified (10 HTTP 200, 1 npmjs.com confirmed indexed via web search, 1 post_url).
- References companion post A74 via post_url.
- No article number assigned. Not slotted for publication. Pre-release candidate status.

---

## Questions for Human Review

- The misc/claude-code port version shown (2.0.58) is from the FreshPorts page as of December 2025. Verify the current port version on FreeBSD before publication.
- The shebang fix section notes that the port installation "may handle this automatically." Verify on FreeBSD whether the port creates the `/bin/bash` symlink or uses `#!/usr/bin/env bash`.
- The `USE_BUILTIN_RIPGREP` setting is documented as `"0"` (string) in settings.json. Some sources show it as `0` (number) or `false`. Verify which format works on FreeBSD.
- The Hello World prompt has not been tested on FreeBSD. Run it and verify that Claude Code can research sysctl MIBs, generate C code, and compile with base system tools.
- The article assumes `claude -p` (non-interactive mode) works on FreeBSD for the verification step. Verify this.
- Software Versions section needs output filled in on FreeBSD hardware.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
