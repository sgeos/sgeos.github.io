# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P11 Draft Getting Started with Solana Using Rust and Pinocchio

---

## Verification

### Getting Started with Solana Using Rust and Pinocchio Article

- New article mirroring A65 "Getting Started with Solana Using Rust and Anchor" using the Pinocchio zero-dependency library instead of Anchor.
- File: `solana_with_rust_and_pinocchio_getting_started.markdown`.
- Title: "Getting Started with Solana Using Rust and Pinocchio."
- Front matter: `mathjax: false`, categories `solana rust`, date `2026-03-02 00:01:00 +0000`.
- Same key pegboard toy contract concept as A65. Stores a public key and encrypted private key on-chain using a PDA.
- Same off-chain `generate.sh` script as A65 included in full for self-containedness.
- Program uses `#![no_std]`, `pinocchio::entrypoint!`, manual account validation, raw byte parsing, and single-byte discriminator routing.
- Account data layout: 32 bytes public key, 4 bytes length prefix (u32 LE), up to 128 bytes encrypted private key. Total 164 bytes.
- PDA seeds `[b"key-pegboard", public_key.as_ref()]` identical to A65 for conceptual parity.
- Account creation via CPI to System Program using `pinocchio_system::instructions::CreateAccount` with PDA signer seeds.
- Rent calculation via `pinocchio::sysvars::rent::Rent::get()`.
- Unit tests in `src/lib.rs`: account data size validation and serialization roundtrip.
- Program tests with Mollusk in `tests/test_publish.rs`: successful publish, missing signer rejection, invalid discriminator rejection.
- Deploying and Testing section covers `cargo build-sbf`, `solana-test-validator`, `solana program deploy`, and `declare_id!` key management.
- Comparison with Anchor table covering 13 aspects (account validation, serialization, discriminator, std lib, scaffolding, build, test, IDL, key management, dependencies, compute units, binary size).
- 9 limitations documented including no automatic account validation, no IDL generation, no client generation, no init constraint, no_std constraints, smaller ecosystem, raw ProgramError, team collaboration, and manual key management.
- References A65 via `post_url`.
- 12 references across 3 categories (Reference, Related Post, Research).
- No article number assigned. Not slotted for publication. `<!-- Axxx -->` placeholder used.

---

## Questions for Human Review

- Software Versions section has TODO placeholders that need to be filled in on the development machine after installing the Solana CLI and running `cargo build-sbf --version`.
- The `declare_id!` macro uses `pinocchio_pubkey::declare_id!`. Verify that this is the correct import path for the current `pinocchio-pubkey` crate version. Some examples use `pinocchio::declare_id!` directly.
- Verify that `pinocchio::sysvars::rent::Rent::get()` is the correct API for reading the Rent sysvar in Pinocchio 0.10.x. The sysvar access pattern may differ from the `solana-program` crate.
- Verify that `pinocchio_system::instructions::CreateAccount` accepts the fields shown (from, to, lamports, space, owner) and that `.invoke_signed(&[&signer_seeds])` is the correct CPI invocation pattern.
- The Mollusk test uses `mollusk_svm::program::system_program()` to provide the System Program account in the test fixture. Verify this function exists in mollusk-svm 0.0.14.
- Verify that `mollusk_svm::result::Check::err(InstructionError::MissingRequiredSignature)` is the correct pattern for asserting instruction failures.
- The `Cargo.toml` specifies `pinocchio = "0.10"`, `pinocchio-system = "0.5"`, `pinocchio-log = "0.3"`, `pinocchio-pubkey = "0.3"`, `mollusk-svm = "0.0.14"`, and `solana-sdk = "2.2"`. Verify these version constraints resolve correctly and are compatible.
- The `generate.sh` script is identical to A65's version. Verify that reproducing the full script is preferred over referencing A65 with a link.
- Verify that the PDA signer seeds pattern `[PDA_SEED, public_key_bytes.as_ref(), bump_bytes.as_ref()]` works correctly with `invoke_signed` in Pinocchio. The bump byte must be passed as a slice reference.
- The article states Pinocchio programs use `#![no_std]`. Verify that the unit tests (which use `assert_eq!`) compile correctly in `#[cfg(test)]` mode, as the test runner provides the standard library.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 8 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH, Phoenix JSON API Authentication with Guardian and Ueberauth, Solana sBPF Assembly Example, Getting Started with Solana Using Rust and Pinocchio.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article.
- Publication order dependency: Android FreeBSD article and CLMM Mathematics (A91) before Android Unit Testing article.
- SSH article has no publication dependency on other articles.
- Phoenix Guardian article has no publication dependency on other unpublished articles. References published article A27 via post_url.
- Solana sBPF article has no publication dependency on other unpublished articles.
- Solana Pinocchio article has no publication dependency on other unpublished articles. References published article A65 via post_url.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
