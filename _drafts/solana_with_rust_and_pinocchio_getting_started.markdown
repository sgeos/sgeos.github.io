---
layout: post
mathjax: false
comments: true
title:  "Getting Started with Solana Using Rust and Pinocchio"
date:   2026-03-02 00:01:00 +0000
categories: solana rust
---

<!-- Axxx -->
<script>console.log("Axxx");</script>

Pinocchio is a zero-dependency Rust library for writing Solana programs
maintained by Anza, the team behind the Agave validator client.
It replaces the standard `solana-program` crate with zero-copy account access,
eliminating deserialization overhead and dramatically reducing
compute unit consumption and binary size.
Where frameworks like Anchor provide high-level abstractions
that handle account validation, serialization, and boilerplate automatically,
Pinocchio requires the developer to implement these operations manually
in exchange for maximum performance and minimal dependencies.

A [companion article][related_post_anchor] demonstrates the same toy contract
built with the Anchor framework.
That article covers the design rationale and off-chain business logic in detail.
This article rebuilds the same contract using Pinocchio
to illustrate the differences between the two approaches
and to serve as a starting point for developers
who prefer low-level control over their Solana programs.

This guide walks through creating a Pinocchio project from scratch,
writing a program that stores a public key and encrypted private key on-chain,
testing with the Mollusk test harness,
and deploying to a local Solana test validator.
A comparison with the Anchor implementation highlights
the tradeoffs between the two approaches.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
TODO

# OS and Version
$ uname -vm
TODO

# Rust
$ rustc --version
TODO

# Cargo
$ cargo --version
TODO

# Solana CLI
$ solana --version
TODO

# cargo-build-sbf
$ cargo build-sbf --version
TODO
```

## Prerequisites

This guide assumes [Rust][reference_rust_install] and
the [Solana CLI][reference_solana_cli] have been installed.
The `cargo build-sbf` command is included with the Solana CLI
and is used to compile Rust programs for the Solana virtual machine.

If you do not have a Solana wallet keypair yet, run the following command.

```sh
solana-keygen new --outfile ~/.config/solana/id.json
```

Verify that the Solana CLI is configured to use the local cluster.

```sh
solana config set --url localhost
```

## Toy Contract Overview

This section builds a simple Solana program that demonstrates
how encrypted data can be published on the blockchain.
The program takes a public key and an encrypted private key as input
and publishes both to the public ledger.
A service like this could facilitate confidential transactions
or secure decentralized authentication.

### Design Considerations

Solana operates in a deterministic environment with resource constraints.
The Solana runtime prioritizes efficiency and scalability,
meaning that heavy cryptographic work should be performed off-chain
before sending data to be stored on the blockchain.
The cryptographic logic is therefore externalized.
The on-chain program is effectively an "echo" service
that accepts and stores pre-computed data.

### Off-Chain Business Logic

The off-chain key generation and encryption logic
is identical to the [companion Anchor article][related_post_anchor].
The following shell script generates a keypair,
encrypts the private key with a one-time key,
and outputs the data needed for on-chain publication.

**generate.sh** full listing
```sh
#!/bin/sh
# generate.sh
# Run `DEBUG=true ./generate.sh` to print debug information.

DEBUG="${DEBUG:-false}"
ONE_TIME_KEY="$(openssl rand -base64 32)"

# Remove old files
rm -f my_keypair.json my_keypair.bin encrypted_private_key.enc

# Generate Keypair
OUTPUT="$(solana-keygen new --outfile my_keypair.json --no-passphrase)"
if [ "${?}" -ne 0 ]; then
    echo "Error: solana-keygen failed" >&2
    exit 1
fi

# Debug Printing
if [ "${DEBUG}" = "true" ]; then
    printf "\n--- solana-keygen OUTPUT ---\n"
    printf "%s\n" "${OUTPUT}"
fi

# Convert JSON Array to Binary
jq -r '.[]' my_keypair.json | while read -r num; do
    printf "$(printf '\\%03o' "${num}")"
done > my_keypair.bin

# Encrypt Binary Key
openssl enc -aes-256-cbc -salt -pbkdf2 -base64 \
    -pass pass:"${ONE_TIME_KEY}" \
    -in my_keypair.bin \
    -out encrypted_private_key.enc
if [ "${?}" -ne 0 ]; then
    echo "Error: Encryption failed"
    exit 1
fi

# Extract Data
PUBLIC_KEY="$(echo "${OUTPUT}" | sed -n 's/pubkey: //p')"
SEED_PHRASE="$(echo "${OUTPUT}" | sed -n '/Save this seed phrase/,/---/p' | sed -n '2p')"

# Verification
ORIGINAL_HEX="$(od -An -tx1 my_keypair.bin | tr -d ' \n')"
DECRYPTED_HEX="$(openssl enc -d -aes-256-cbc -pbkdf2 -base64 \
    -pass pass:"${ONE_TIME_KEY}" \
    -in encrypted_private_key.enc | od -An -tx1 | tr -d ' \n')"

# Final Output for Blockchain
printf "\n--- Publish to Blockchain ---\n"
printf "\nPUBLIC KEY:\n%s\n" "${PUBLIC_KEY}"
printf "\nENCRYPTED PRIVATE KEY:\n%s\n" "$(cat encrypted_private_key.enc)"

# Private Transmission Data
printf "\n--- Secure Private Transmit to Publisher ---\n"
printf "\nSEED PHRASE:\n%s\n" "${SEED_PHRASE}"
printf "\nONE TIME KEY:\n%s\n" "${ONE_TIME_KEY}"

# Debug Values
if [ "${DEBUG}" = "true" ]; then
    printf "\n--- Debug ---\n"
    printf "\nPRIVATE KEY ORIGINAL (HEX):\n%s\n" "${ORIGINAL_HEX}"
    printf "\nPRIVATE KEY DECRYPTED (HEX):\n%s\n" "${DECRYPTED_HEX}"
    printf "\nDECRYPTION:\n"
    if [ "${ORIGINAL_HEX}" = "${DECRYPTED_HEX}" ]; then
        printf "PASS\n"
    else
        printf "FAIL\n"
    fi
fi
```

## Smart Contract Implementation

Pinocchio is not a framework.
It is a library that provides zero-copy access to Solana account data
and helper types for building programs.
Unlike Anchor, which generates account validation code through derive macros,
Pinocchio programs implement all validation logic manually.
This requires more code but produces smaller binaries
with significantly lower compute unit consumption.

Pinocchio programs are built with `#![no_std]`,
meaning they do not depend on the Rust standard library.
The `pinocchio` crate provides its own allocator and panic handler
through the `entrypoint!` macro.

### Creating the Project

Create a new Rust library project.

```sh
cd path/to/my/projects # customize or omit this line
PROJECT_NAME="key_pegboard_pinocchio"
cargo init --lib "${PROJECT_NAME}"
cd "${PROJECT_NAME}"
```

Replace the generated `Cargo.toml` with the following configuration.

**Cargo.toml** full listing
```toml
[package]
name = "key_pegboard_pinocchio"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["lib", "cdylib"]

[dependencies]
pinocchio = "0.10"
pinocchio-system = "0.5"
pinocchio-log = "0.3"
pinocchio-pubkey = "0.3"

[dev-dependencies]
mollusk-svm = "0.0.14"
solana-sdk = "2.2"
```

The `cdylib` crate type is required for compilation to a Solana-compatible
shared object file.
The `pinocchio-system` crate provides zero-copy Cross-Program Invocation (CPI) helpers
for the System Program, which is needed to create accounts on-chain.
The `pinocchio-log` crate provides a lightweight `log!` macro
that uses fewer compute units than `format!`.
The `pinocchio-pubkey` crate provides the `declare_id!` macro.

The `mollusk-svm` and `solana-sdk` crates are development dependencies
used for testing.
Mollusk is a lightweight test harness
that invokes the BPF loader directly without spinning up a full validator.

The project structure is as follows.

```
key_pegboard_pinocchio/
  src/
    lib.rs          # Program entrypoint and instruction logic
  tests/
    test_publish.rs # Mollusk program tests
  Cargo.toml
```

### Program Code

Replace the contents of `src/lib.rs` with the following program.

**src/lib.rs** full listing
```rust
// src/lib.rs
#![no_std]

use pinocchio::{
    account_info::AccountInfo,
    entrypoint,
    program_error::ProgramError,
    pubkey::Pubkey,
    ProgramResult,
};
use pinocchio_log::log;
use pinocchio_pubkey::declare_id;

declare_id!("11111111111111111111111111111111");

// Account data layout constants.
// The on-chain account stores a public key followed by a length-prefixed
// encrypted private key.
//
// Offset  Size   Field
// 0       32     public_key
// 32      4      encrypted_private_key length (u32 LE)
// 36      N      encrypted_private_key bytes (max 128)
const PUBKEY_SIZE: usize = 32;
const LEN_PREFIX_SIZE: usize = 4;
const MAX_ENCRYPTED_KEY_SIZE: usize = 128;
const ACCOUNT_DATA_SIZE: usize = PUBKEY_SIZE + LEN_PREFIX_SIZE + MAX_ENCRYPTED_KEY_SIZE;

// PDA seed prefix.
const PDA_SEED: &[u8] = b"key-pegboard";

// Instruction discriminators.
const PUBLISH_KEY_PAIR: u8 = 0;

entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let (discriminator, data) = instruction_data
        .split_first()
        .ok_or(ProgramError::InvalidInstructionData)?;

    match *discriminator {
        PUBLISH_KEY_PAIR => process_publish_key_pair(program_id, accounts, data),
        _ => Err(ProgramError::InvalidInstructionData),
    }
}

fn process_publish_key_pair(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    data: &[u8],
) -> ProgramResult {
    // Validate account count.
    if accounts.len() < 3 {
        return Err(ProgramError::NotEnoughAccountKeys);
    }

    let key_pair_account = &accounts[0];
    let signer = &accounts[1];
    let system_program = &accounts[2];

    // Validate that the signer has signed the transaction.
    if !signer.is_signer() {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Parse instruction data.
    // Layout: [32 bytes public_key] [4 bytes length] [N bytes encrypted key]
    if data.len() < PUBKEY_SIZE + LEN_PREFIX_SIZE {
        return Err(ProgramError::InvalidInstructionData);
    }

    let public_key_bytes: &[u8; 32] = data[..PUBKEY_SIZE]
        .try_into()
        .map_err(|_| ProgramError::InvalidInstructionData)?;
    let encrypted_key_len = u32::from_le_bytes(
        data[PUBKEY_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE]
            .try_into()
            .map_err(|_| ProgramError::InvalidInstructionData)?,
    ) as usize;

    if encrypted_key_len > MAX_ENCRYPTED_KEY_SIZE {
        return Err(ProgramError::InvalidInstructionData);
    }

    let expected_data_len = PUBKEY_SIZE + LEN_PREFIX_SIZE + encrypted_key_len;
    if data.len() < expected_data_len {
        return Err(ProgramError::InvalidInstructionData);
    }

    let encrypted_key_data =
        &data[PUBKEY_SIZE + LEN_PREFIX_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE + encrypted_key_len];

    // Derive the expected PDA and verify the key_pair_account address.
    let (expected_pda, bump) =
        pinocchio::pubkey::find_program_address(&[PDA_SEED, public_key_bytes], program_id);

    if key_pair_account.key() != &expected_pda {
        return Err(ProgramError::InvalidAccountData);
    }

    // Verify the system program.
    if system_program.key() != &pinocchio_system::ID {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Calculate rent-exempt minimum lamports.
    let rent = pinocchio::sysvars::rent::Rent::get()?;
    let lamports = rent.minimum_balance(ACCOUNT_DATA_SIZE);

    // Create the account via CPI to the System Program.
    let bump_bytes = [bump];
    let signer_seeds = [PDA_SEED, public_key_bytes.as_ref(), bump_bytes.as_ref()];
    pinocchio_system::instructions::CreateAccount {
        from: signer,
        to: key_pair_account,
        lamports,
        space: ACCOUNT_DATA_SIZE as u64,
        owner: program_id,
    }
    .invoke_signed(&[&signer_seeds])?;

    // Write the public key and encrypted private key to the account.
    let mut account_data = key_pair_account.try_borrow_mut_data()?;
    account_data[..PUBKEY_SIZE].copy_from_slice(public_key_bytes);
    account_data[PUBKEY_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE]
        .copy_from_slice(&(encrypted_key_len as u32).to_le_bytes());
    account_data[PUBKEY_SIZE + LEN_PREFIX_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE + encrypted_key_len]
        .copy_from_slice(encrypted_key_data);

    log!("Published key pair to PDA");

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_account_data_size() {
        // Verify the account data size constant matches the layout.
        let expected = PUBKEY_SIZE + LEN_PREFIX_SIZE + MAX_ENCRYPTED_KEY_SIZE;
        assert_eq!(ACCOUNT_DATA_SIZE, expected);
        assert_eq!(ACCOUNT_DATA_SIZE, 164);
    }

    #[test]
    fn test_data_layout_roundtrip() {
        // Verify that writing and reading the account data layout
        // produces the original values.
        let mut buffer = [0u8; ACCOUNT_DATA_SIZE];

        let public_key = [42u8; 32];
        let encrypted_key = [1u8, 2, 3, 4, 5];
        let encrypted_key_len = encrypted_key.len() as u32;

        // Write.
        buffer[..PUBKEY_SIZE].copy_from_slice(&public_key);
        buffer[PUBKEY_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE]
            .copy_from_slice(&encrypted_key_len.to_le_bytes());
        buffer[PUBKEY_SIZE + LEN_PREFIX_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE + encrypted_key.len()]
            .copy_from_slice(&encrypted_key);

        // Read back.
        let read_pubkey = &buffer[..PUBKEY_SIZE];
        let read_len = u32::from_le_bytes(
            buffer[PUBKEY_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE]
                .try_into()
                .unwrap(),
        ) as usize;
        let read_encrypted =
            &buffer[PUBKEY_SIZE + LEN_PREFIX_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE + read_len];

        assert_eq!(read_pubkey, &public_key);
        assert_eq!(read_len, encrypted_key.len());
        assert_eq!(read_encrypted, &encrypted_key);
    }
}
```

### Code Explanation

The program code defines the complete on-chain logic for the key pegboard.

The `declare_id!` macro sets the program's public key.
The placeholder value `11111111111111111111111111111111` must be replaced
with the actual program ID after deployment.
Unlike Anchor, which uses `anchor keys sync` to manage this automatically,
Pinocchio programs require manual key management.

The constants at the top of the file define the account data layout.
The on-chain account stores 32 bytes for the public key,
4 bytes for the encrypted private key length as a little-endian `u32`,
and up to 128 bytes for the encrypted private key data.
The total account size is 164 bytes.

The `entrypoint!` macro registers `process_instruction` as the program entry point.
It also sets up the global allocator and panic handler
required for `#![no_std]` programs on Solana.

The `process_instruction` function reads the first byte of instruction data
as a discriminator and routes to the appropriate handler.
This single-byte discriminator convention supports up to 255 instructions
and is more compact than Anchor's 8-byte sighash discriminators.

The `process_publish_key_pair` function performs the following operations.

1. It validates that at least three accounts are provided
   and that the second account (the signer) has signed the transaction.
   In Anchor, these checks are declarative through the `Signer<'info>` type
   and `#[account(mut)]` attribute.
   In Pinocchio, they must be written explicitly.

2. It parses the instruction data manually.
   The first 32 bytes are the public key,
   the next 4 bytes are the encrypted key length,
   and the remaining bytes are the encrypted key data.
   Each field is validated for correct length and bounds.

3. It derives the expected Program Derived Address (PDA) using the seeds
   `["key-pegboard", public_key]` and verifies that the provided account
   matches the derived address.
   The PDA seeds are identical to those in the
   [Anchor implementation][related_post_anchor] for conceptual parity.

4. It creates the on-chain account via a Cross-Program Invocation (CPI)
   to the System Program using `pinocchio_system::instructions::CreateAccount`.
   The account is created with rent-exempt lamports
   and owned by the current program.
   The CPI is signed with the PDA's seeds,
   which authorizes the System Program to create an account at the derived address.

5. It writes the public key and encrypted private key to the newly created account
   using direct byte operations on the borrowed account data.
   This is the zero-copy approach that gives Pinocchio its performance advantage.
   Anchor programs serialize data through the Borsh encoding library,
   which allocates memory and copies data during the process.

## Tests

Pinocchio programs are typically tested with Mollusk,
a lightweight test harness maintained by the Solana ecosystem.
Mollusk invokes the BPF loader directly on compiled program binaries
without spinning up a full Solana validator.
This makes tests fast and deterministic
while still exercising the actual on-chain code path.

### Unit Tests

The unit tests in the `#[cfg(test)]` module within `src/lib.rs`
verify the account data layout constants and serialization roundtrip.
These tests run with `cargo test` without requiring a compiled BPF binary.

```sh
cargo test --lib
```

Expected output.

```
running 2 tests
test tests::test_account_data_size ... ok
test tests::test_data_layout_roundtrip ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

### Program Tests with Mollusk

Program-level tests exercise the compiled BPF binary
by constructing raw instructions and account states.
Create the following test file.

**tests/test_publish.rs** full listing
```rust
// tests/test_publish.rs
use mollusk_svm::result::Check;
use mollusk_svm::Mollusk;
use solana_sdk::account::Account;
use solana_sdk::instruction::{AccountMeta, Instruction};
use solana_sdk::pubkey::Pubkey;
use solana_sdk::rent::Rent;
use solana_sdk::system_program;

const PUBKEY_SIZE: usize = 32;
const LEN_PREFIX_SIZE: usize = 4;
const MAX_ENCRYPTED_KEY_SIZE: usize = 128;
const ACCOUNT_DATA_SIZE: usize = PUBKEY_SIZE + LEN_PREFIX_SIZE + MAX_ENCRYPTED_KEY_SIZE;
const PDA_SEED: &[u8] = b"key-pegboard";
const PUBLISH_KEY_PAIR: u8 = 0;

#[test]
fn test_publish_key_pair() {
    let program_id = Pubkey::new_unique();
    let mollusk = Mollusk::new(&program_id, "target/deploy/key_pegboard_pinocchio");

    let signer = Pubkey::new_unique();
    let test_public_key = Pubkey::new_unique();
    let encrypted_key = vec![10u8, 20, 30, 40, 50];
    let encrypted_key_len = encrypted_key.len() as u32;

    // Derive the PDA.
    let (pda, _bump) = Pubkey::find_program_address(
        &[PDA_SEED, test_public_key.as_ref()],
        &program_id,
    );

    // Build instruction data.
    // Layout: [1 byte discriminator] [32 bytes pubkey] [4 bytes len] [N bytes data]
    let mut instruction_data = vec![PUBLISH_KEY_PAIR];
    instruction_data.extend_from_slice(test_public_key.as_ref());
    instruction_data.extend_from_slice(&encrypted_key_len.to_le_bytes());
    instruction_data.extend_from_slice(&encrypted_key);

    let instruction = Instruction::new_with_bytes(
        program_id,
        &instruction_data,
        vec![
            AccountMeta::new(pda, false),
            AccountMeta::new(signer, true),
            AccountMeta::new_readonly(system_program::id(), false),
        ],
    );

    let rent = Rent::default();
    let signer_lamports = rent.minimum_balance(0) + rent.minimum_balance(ACCOUNT_DATA_SIZE);

    let result = mollusk.process_and_validate_instruction(
        &instruction,
        &[
            (
                pda,
                Account {
                    lamports: 0,
                    data: vec![],
                    owner: system_program::id(),
                    executable: false,
                    rent_epoch: 0,
                },
            ),
            (
                signer,
                Account {
                    lamports: signer_lamports,
                    data: vec![],
                    owner: system_program::id(),
                    executable: false,
                    rent_epoch: 0,
                },
            ),
            mollusk_svm::program::system_program(),
        ],
        &[Check::success()],
    );

    // Verify the account data after execution.
    let pda_account = &result.resulting_accounts[0].1;
    assert_eq!(pda_account.owner, program_id);
    assert_eq!(pda_account.data.len(), ACCOUNT_DATA_SIZE);

    // Verify the public key.
    let stored_pubkey = &pda_account.data[..PUBKEY_SIZE];
    assert_eq!(stored_pubkey, test_public_key.as_ref());

    // Verify the encrypted key length.
    let stored_len = u32::from_le_bytes(
        pda_account.data[PUBKEY_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE]
            .try_into()
            .unwrap(),
    ) as usize;
    assert_eq!(stored_len, encrypted_key.len());

    // Verify the encrypted key data.
    let stored_encrypted =
        &pda_account.data[PUBKEY_SIZE + LEN_PREFIX_SIZE..PUBKEY_SIZE + LEN_PREFIX_SIZE + stored_len];
    assert_eq!(stored_encrypted, encrypted_key.as_slice());
}

#[test]
fn test_publish_key_pair_missing_signer() {
    let program_id = Pubkey::new_unique();
    let mollusk = Mollusk::new(&program_id, "target/deploy/key_pegboard_pinocchio");

    let signer = Pubkey::new_unique();
    let test_public_key = Pubkey::new_unique();
    let encrypted_key = vec![10u8, 20, 30];

    let (pda, _bump) = Pubkey::find_program_address(
        &[PDA_SEED, test_public_key.as_ref()],
        &program_id,
    );

    let mut instruction_data = vec![PUBLISH_KEY_PAIR];
    instruction_data.extend_from_slice(test_public_key.as_ref());
    instruction_data.extend_from_slice(&(encrypted_key.len() as u32).to_le_bytes());
    instruction_data.extend_from_slice(&encrypted_key);

    // Set signer to false to trigger the missing signature error.
    let instruction = Instruction::new_with_bytes(
        program_id,
        &instruction_data,
        vec![
            AccountMeta::new(pda, false),
            AccountMeta::new(signer, false), // not a signer
            AccountMeta::new_readonly(system_program::id(), false),
        ],
    );

    mollusk.process_and_validate_instruction(
        &instruction,
        &[
            (
                pda,
                Account {
                    lamports: 0,
                    data: vec![],
                    owner: system_program::id(),
                    executable: false,
                    rent_epoch: 0,
                },
            ),
            (
                signer,
                Account {
                    lamports: 1_000_000_000,
                    data: vec![],
                    owner: system_program::id(),
                    executable: false,
                    rent_epoch: 0,
                },
            ),
            mollusk_svm::program::system_program(),
        ],
        &[Check::err(solana_sdk::instruction::InstructionError::MissingRequiredSignature)],
    );
}

#[test]
fn test_publish_key_pair_invalid_discriminator() {
    let program_id = Pubkey::new_unique();
    let mollusk = Mollusk::new(&program_id, "target/deploy/key_pegboard_pinocchio");

    let signer = Pubkey::new_unique();

    // Use an invalid discriminator byte.
    let instruction_data = vec![0xFF];

    let instruction = Instruction::new_with_bytes(
        program_id,
        &instruction_data,
        vec![AccountMeta::new(signer, true)],
    );

    mollusk.process_and_validate_instruction(
        &instruction,
        &[(
            signer,
            Account {
                lamports: 1_000_000_000,
                data: vec![],
                owner: system_program::id(),
                executable: false,
                rent_epoch: 0,
            },
        )],
        &[Check::err(solana_sdk::instruction::InstructionError::InvalidInstructionData)],
    );
}
```

Mollusk tests require a compiled BPF binary.
Build the program first, then run the tests.

```sh
cargo build-sbf
cargo test
```

Expected output.

```
running 2 tests
test tests::test_account_data_size ... ok
test tests::test_data_layout_roundtrip ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

running 3 tests
test test_publish_key_pair ... ok
test test_publish_key_pair_missing_signer ... ok
test test_publish_key_pair_invalid_discriminator ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

The first test verifies that the publish instruction correctly creates
a PDA account and stores the expected data.
The second test verifies that the program rejects transactions
where the signer has not signed.
The third test verifies that invalid instruction discriminators
are rejected.

## Deploying and Testing

### Building

Compile the program to a Solana-compatible shared object file.

```sh
cargo build-sbf
```

The compiled binary is written to `target/deploy/key_pegboard_pinocchio.so`.
Examine the output.

```sh
$ ls -la target/deploy/key_pegboard_pinocchio.so
$ file target/deploy/key_pegboard_pinocchio.so
```

### Local Test Validator

Start a local Solana test validator in a separate terminal.

```sh
solana-test-validator
```

### Deploying

Deploy the compiled program to the local validator.

```sh
solana program deploy target/deploy/key_pegboard_pinocchio.so
```

Note the program ID printed in the output.
Update the `declare_id!` macro in `src/lib.rs`
with the actual program ID returned by the deploy command.
Rebuild and redeploy after updating the ID.

```sh
# After updating declare_id! in src/lib.rs
cargo build-sbf
solana program deploy target/deploy/key_pegboard_pinocchio.so
```

### Invoking

The local test validator's log output can be monitored in a separate terminal.

```sh
solana logs --url localhost
```

Use the Solana CLI to verify the deployment.

```sh
PROGRAM_ID="your_program_id_here"
solana program show "${PROGRAM_ID}" --url localhost
```

For programmatic invocation, a Rust client can construct
and send transactions to the deployed program.
Client development is beyond the scope of this getting started guide.
The [Solana documentation][reference_solana_programs] covers
client-side transaction construction in detail.

## Comparison with Anchor

The following table compares the Pinocchio implementation in this article
with the Anchor implementation in the [companion article][related_post_anchor].

| Aspect | Anchor (A65) | Pinocchio |
|--------|-------------|-----------|
| Account validation | Declarative via `#[derive(Accounts)]` | Manual checks in handler function |
| Serialization | Automatic via Borsh | Manual byte operations |
| Discriminator | 8-byte sighash (automatic) | 1-byte (manual) |
| Standard library | `std` | `#![no_std]` |
| Project scaffolding | `anchor init` | Manual `cargo init --lib` |
| Build command | `anchor build` | `cargo build-sbf` |
| Test framework | `anchor test` with local validator | Mollusk (BPF loader, no validator) |
| Test setup | Integration tests send real transactions | Unit-style tests with direct BPF invocation |
| IDL generation | Automatic | Requires Shank and Codama |
| Key management | `anchor keys sync` | Manual `declare_id!` update |
| Dependencies | `anchor-lang` plus transitive `solana-program` | `pinocchio` (zero external dependencies) |
| Compute units | Higher due to abstraction overhead | Significantly lower |
| Binary size | Larger | Smaller |

Anchor is the pragmatic choice when development speed and team collaboration
are the primary concerns.
Pinocchio is appropriate when compute unit consumption, binary size,
or dependency minimization are the overriding priorities.

## Limitations

1. Pinocchio provides no automatic account validation.
Every signer check, ownership check, PDA derivation,
and constraint must be written by the developer.
This increases the risk of security vulnerabilities from missed checks.

2. No built-in Interface Definition Language (IDL) generation exists.
Programs that need an IDL for client generation
must add Shank attribute annotations
and use the separate `shank-cli` and Codama tooling.

3. No automatic client generation exists.
Anchor generates TypeScript and Rust clients from its IDL automatically.
Pinocchio programs require manual client construction
or the Shank plus Codama pipeline.

4. No `init` constraint equivalent exists for account creation.
Creating accounts requires explicit CPI to the System Program
with manual rent calculation.

5. The `#![no_std]` constraint prohibits the use of Rust standard library types
like `String`, `Vec`, and `HashMap` without a custom allocator.
The `pinocchio` entrypoint macro provides an allocator,
but heap usage increases compute unit consumption.

6. Pinocchio's ecosystem is smaller than Anchor's.
Fewer tutorials, production examples, and community patterns exist.
Debugging is harder without Anchor's structured error codes.

7. Error handling uses raw `ProgramError` variants.
Anchor provides `#[error_code]` for structured, numbered error types.
Pinocchio programs must define and manage their own error conventions.

8. Team collaboration can be more difficult.
The lack of standardized project structure and conventions
means different developers may organize Pinocchio programs very differently.

9. The `declare_id!` program address must be updated manually
after initial deployment.
Unlike Anchor's `anchor keys sync`,
there is no built-in command to synchronize keys.

## Conclusion

This guide demonstrated building a Solana program with Pinocchio
that performs the same function as the Anchor program
in the [companion article][related_post_anchor].
The key pegboard contract stores a public key
and an encrypted private key on the blockchain using a PDA,
with all cryptographic operations performed off-chain.

Pinocchio's zero-copy approach and minimal dependencies
produce smaller binaries with lower compute unit consumption
at the cost of more verbose code and manual validation.
Developers should evaluate the tradeoffs against their project requirements.
For applications approaching compute unit limits
or where binary size is a deployment constraint,
Pinocchio provides meaningful advantages.
For rapid development and team collaboration,
Anchor remains the more productive choice.

## Future Reading

The Helius blog post on building Solana programs with Pinocchio
provides a comprehensive walkthrough of a vault program
with deposit and withdraw instructions.
The QuickNode guide covers Pinocchio program development
including Shank IDL generation and Codama client generation.
The Solana Foundation's Pinocchio counter template
demonstrates an end-to-end project structure
with LiteSVM tests and a web frontend.
The Blueshift Pinocchio 101 course provides a structured curriculum
for learning the library from first principles.

## References

- [Reference, Agave CLI Documentation][reference_agave_cli]
- [Reference, Mollusk Documentation][reference_mollusk]
- [Reference, Pinocchio GitHub Repository][reference_pinocchio_github]
- [Reference, Pinocchio on crates.io][reference_pinocchio_crate]
- [Reference, Rust Installation Guide][reference_rust_install]
- [Reference, Solana CLI Installation][reference_solana_cli]
- [Reference, Solana Programs Documentation][reference_solana_programs]
- [Related Post, Getting Started with Solana Using Rust and Anchor][related_post_anchor]
- [Research, How to Build Solana Programs with Pinocchio][research_helius_pinocchio]
- [Research, How to Build and Deploy a Solana Program Using Pinocchio][research_quicknode_pinocchio]
- [Research, Pinocchio 101][research_pinocchio_101]
- [Research, Pinocchio Counter Template][research_pinocchio_counter]

[reference_agave_cli]: https://docs.anza.xyz/cli/
[reference_mollusk]: https://solana.com/docs/programs/testing/mollusk
[reference_pinocchio_crate]: https://crates.io/crates/pinocchio
[reference_pinocchio_github]: https://github.com/anza-xyz/pinocchio
[reference_rust_install]: https://www.rust-lang.org/learn/get-started
[reference_solana_cli]: https://docs.anza.xyz/cli/install
[reference_solana_programs]: https://solana.com/docs/core/programs
[related_post_anchor]: {% post_url 2025-12-17-solana_with_rust_and_anchor_getting_started %}
[research_helius_pinocchio]: https://www.helius.dev/blog/pinocchio
[research_pinocchio_101]: https://learn.blueshift.gg/en/courses/pinocchio-for-dummies/pinocchio-101
[research_pinocchio_counter]: https://solana.com/developers/templates/pinocchio-counter
[research_quicknode_pinocchio]: https://www.quicknode.com/guides/solana-development/pinocchio/how-to-build-and-deploy-a-solana-program-using-pinocchio
