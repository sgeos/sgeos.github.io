# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P6 Getting Started with Claude Code Over SSH

---

## Verification

### Claude Code Over SSH Article

- New draft at `_drafts/claude_code_getting_started_over_ssh.markdown`.
- SSH Background section covers the protocol, authentication methods, and client configuration for readers unfamiliar with or rusty regarding SSH.
- Instructions section walks through key generation, public key copying, SSH agent setup, host configuration, verification, remote execution patterns, and timeout configuration.
- Remote Execution section documents single command, multi-command with working directory, scp file transfer, and the stateless nature of Bash tool SSH invocations.
- Claude Code Desktop SSH section briefly describes the native SSH connection feature and notes it requires Claude Code on the remote machine.
- Hello World section demonstrates end-to-end remote workflow: OS detection, C code generation, scp transfer, remote compilation, and execution.
- Limitations section covers local-only file tools, stateless sessions, no interactive prompt support, timeout limits, and manual port forwarding.
- 10 references across 3 categories (Claude, Reference, Related Post). All URLs verified (7 HTTP 200, 3 post_url).
- No article number assigned. Not slotted for publication. Pre-release candidate status.

---

## Questions for Human Review

- The article assumes `ssh-copy-id` is available on the local machine. This utility ships with OpenSSH on most platforms but may not be present on minimal installations. Verify availability on your primary development machine.
- The Hello World prompt has not been tested against an actual remote target. Run it against a machine with SSH access and a C compiler to verify the workflow.
- The `BASH_DEFAULT_TIMEOUT_MS` and `BASH_MAX_TIMEOUT_MS` settings are documented as string values in settings.json. Verify this format is correct for the current Claude Code version.
- The Claude Code Desktop SSH section references the official Desktop documentation. Verify that the Desktop app's SSH connection feature works as described.
- The article does not cover SSH agent forwarding in detail. If you need Claude Code to use the remote machine's git credentials or other SSH-dependent services, agent forwarding may need a dedicated subsection.
- The article uses `myserver` as the example host alias throughout. Replace with a more descriptive example if preferred.
- Software Versions section needs output filled in on your local machine.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 4 pre-release candidates: Android Development on FreeBSD, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article (post_url reference).
- SSH article has no publication dependency on other articles. All three post_url references point to articles that will be published before or independently of this article.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
