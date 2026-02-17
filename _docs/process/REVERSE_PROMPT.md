# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P7 Revise Claude Code Over SSH — Agent Forwarding

---

## Verification

### Claude Code Over SSH Article Revision

- Agent Forwarding section added between Instructions and Claude Code Desktop SSH.
- Seven subsections: How Agent Forwarding Works, Enabling Agent Forwarding, Verifying Agent Forwarding, Use with Claude Code, Security Considerations, ProxyJump Alternative.
- Mechanism explained through temporary Unix domain socket and `SSH_AUTH_SOCK` forwarding.
- Configuration documented via `ForwardAgent yes` in `~/.ssh/config` (per-host) and `-A` flag (one-off).
- Verification command: `ssh -A myserver "ssh-add -l"` with troubleshooting guidance.
- Claude Code usage explained with example prompt for remote Git clone via agent forwarding.
- Security considerations prominently warn about root access on remote hosts accessing the forwarded agent socket.
- ProxyJump documented as safer alternative for untrusted intermediate hosts, with both config file and `-J` flag examples.
- Opening prose updated from three to four topics.
- ssh-agent manual reference added (HTTP 200 verified). Article now has 11 references across 3 categories.
- All existing content preserved. No structural changes to other sections.

---

## Questions for Human Review

- The article states that Claude Code's Bash tool inherits `SSH_AUTH_SOCK` from the shell environment. Verify this by running `ssh -A myserver "ssh-add -l"` from within a Claude Code Bash tool invocation.
- The `ForwardAgent yes` directive is documented per-host. Verify that this works correctly with the host alias configured in the Host Configuration section.
- The ProxyJump section documents OpenSSH 7.3 as the minimum version. Verify that your remote targets have OpenSSH 7.3 or later if you plan to use ProxyJump.
- The security considerations warn against enabling `ForwardAgent yes` with `Host *`. Review your existing `~/.ssh/config` to ensure agent forwarding is not globally enabled.
- The Hello World section still uses the original prompt without agent forwarding. Consider whether a second Hello World prompt demonstrating agent forwarding with a Git clone would be useful.
- Software Versions section still needs output filled in on your local machine.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 4 pre-release candidates: Android Development on FreeBSD, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article (post_url reference).
- SSH article has no publication dependency on other articles.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
