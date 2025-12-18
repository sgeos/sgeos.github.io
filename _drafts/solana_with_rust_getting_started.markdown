---
layout: post
mathjax: false
comments: true
title:  "Getting Started with Solana Using Rust"
date:   2025-12-17 18:56:49 +0000
categories: 
---

Solana is a high-performance blockchain that focuses on scalability and fast
transaction processing.
It has become a popular choice for decentralized applications (dApps) and
decentralized finance (DeFi) projects.
Rust’s combination of safety and speed makes it ideal for developing on
a blockchain like Solana where performance is critical.

Not everyone who know Rust has a DeFi background, and not everyone with a
DeFi background knows Rust.
This guide acts as a starting point for readers in either camp who want to
get started with Solana using Rust.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2025-12-17 18:56:49 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Rust and Solana Installation Versions
$ rustc --version && \
  solana --version && \
  anchor --version && \
  surfpool --version && \
  printf "node " && node --version && \
  printf "yarn " && yarn --version
rustc 1.92.0 (ded5c06cf 2025-12-08)
solana-cli 3.0.13 (src:90098d26; feat:3604001754, client:Agave)
anchor-cli 0.32.1
surfpool 1.0.0-rc1
node v24.11.0
yarn 1.22.22
rustc 1.92.0 (ded5c06cf 2025-12-08)
```

## Prerequisites

This guide assumes [Rust][rust_install] and
the [Solana CLI][solana_cli_install] have been installed.

If you do not have a Solana wallet keypair yet, run the following command.

```sh
solana-keygen new --outfile ~/.config/solana/id.json
```

Make sure to set the `ANCHOR_WALLET` environment variable.
Consider adding this to your `~/.profile` or equivalent.

```sh
export ANCHOR_WALLET="${HOME}/.config/solana/id.json"
```

## Toy Contract Overview

In this section, we will build a simple Solana contract that demonstrates how
encrypted data can be published on the blockchain.
The contract will take a public key and an encrypted private key as input,
and it will publish both to the public ledger.
A service like this could be used to facilitate confidential transactions,
including secure decentralized authentication.

### Design Considerations

While Solana is an ideal platform for high-performance blockchain applications,
it is not well-suited for direct cryptographic operations like encrypting and
decrypting data.
This is because Solana, like most blockchains, operates in a deterministic
environment with resource constraints.
The Solana runtime prioritizes efficiency and scalability, meaning that heavy
cryptographic work should be done outside the chain, before sending data to be
stored on the blockchain.
Thus, the cryptographic logic will be externalized.
The astute reader will recognize that this means we are essentially developing
an "echo" service.

### Off-Chain Business Logic

To implement this toy contract, we will generate a one-time key,
a public/private key pair, and encrypt the private key using the one-time key.
The party who requests publication will get a copy of the one time key and the
pass phrase so that they can decrypt the private key.
The one time key will not be published to the block chain.
An alternative transmission method will be used.
Everyone who needs to encrypt or decrypt anything using this keypair will be
referred to the public ledger, including the recipient of the one time key.

While the logic for generating and encrypting the keys lies outside the scope
of the Solana program itself, it is crucial for understanding how the contract
will operate.
A proof of concept shell script is included below.
A production solution would implement a more robust solution.

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

# Smart Contract Implementation

Anchor is a framework for building smart contracts on Solana.
It simplifies the development process by providing a set of conventions,
abstractions, and libraries that handle much of the boilerplate code required
for Solana programs.
Anchor's overhead is minimal, and it is designed to be idiomatic, allowing
developers to write clean and maintainable Rust code.
This post does not cover writing contracts with raw Rust, including `no_std`
Rust, which provides more low-level control but comes with added complexity.

Create a new anchor project with the following command.

```sh
cd path/to/my/projects # customize or omit this line
PROJECT_NAME="key_pegboard"
anchor init --test-template rust "${PROJECT_NAME}"
cd "${PROJECT_NAME}"
```

## Adding Rust Code

After initializing the Anchor project with the `anchor init` command, you
will have a basic folder structure for your project.
The Rust code for the smart contract will go inside the `src/lib.rs`
file within the `programs/${PROJECT_NAME}` directory of your Anchor project.
For this project, that file is `programs/key_pegboard/src/lib.rs`.

```sh
$ ls
Anchor.toml     node_modules        target
Cargo.toml      package.json        tests
app             programs            tsconfig.json
migrations      rust-toolchain.toml yarn.lock

$ tree programs
programs
└── key_pegboard
    ├── Cargo.toml
    └── src
        └── lib.rs
```

We will now implement a smart contract that uses Anchor to publish the public
and encrypted private keys to the Solana blockchain.
Since the encryption-related business logic is externalized, there is not a
whole lot to this particular contract.
Your Solana use-case will likely be more complex.

**programs/key_pegboard/src/lib.rs** initial full listing
```rust
// programs/key_pegboard/src/lib.rs
use anchor_lang::prelude::*;

declare_id!("85xJ8TBXMgdHG4cfzADoa6sQNsQjcdJRcsY4GeViZou1");

#[program]
pub mod key_pegboard {
    use super::*;

    pub fn publish_key_pair(
        ctx: Context<KeyPairContext>,
        public_key: Pubkey,
        encrypted_private_key: Vec<u8>,
    ) -> Result<()> {
        let key_pair = &mut ctx.accounts.key_pair;
        key_pair.public_key = public_key;
        key_pair.encrypted_private_key = encrypted_private_key;
        Ok(())
    }
}

#[derive(Accounts)]
#[instruction(public_key: Pubkey)]
pub struct KeyPairContext<'info> {
    #[account(
        init,
        payer = signer,
        space = 8 + KeyPairAccount::INIT_SPACE,
        seeds = [
            b"key-pegboard",
            public_key.as_ref()
        ],
        bump
    )]
    pub key_pair: Account<'info, KeyPairAccount>,
    #[account(mut)]
    pub signer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[account]
#[derive(InitSpace)]
pub struct KeyPairAccount {
    pub public_key: Pubkey,
    #[max_len(128)]
    pub encrypted_private_key: Vec<u8>,
}
```

## Code Explanation

The `lib.rs` file defines the heart of a Solana program,
and it can be extended or modified to suit a specific use case.

- **`declare_id!` macro**: This declares the public key of the smart contract,
  which is generated when the contract is deployed to the Solana blockchain.
  This will be updated later with the actual program ID after deployment.
- **`#[program]` attribute**: This is an idiomatic Anchor declaration of the
  module that contains the core logic of the smart contract.
  It defines the program code that interacts with the Solana blockchain.
- **`publish_key_pair` function**: This is the main function of the contract
  that stores the public and encrypted private keys on the blockchain.
  It takes the public key and encrypted private key as inputs and saves them to
  the `key_storage` account.
- **`#[derive(Accounts)]` attribute**: This is an idiomatic Anchor definition
  of the accounts the smart contract will interact with during the execution
  of a function.
- **`KeyPairContext` struct**: This concretely defines the accounts involved in
  the transaction.
  It includes the `key_storage` account to hold the key data,
  the `user` account who is the signer submitting the transaction,
  and the `system_program` which is required for
  creating the `key_storage` account.
- **`#[account(init, ...)]` attribute**:
  Specifies that the signer pays for contract execution.
  The space calculation is 8 bytes for the account discriminator,
  64 bytes for the `public_key` and 512 bytes for `encrypted_private_key`.
  Less bytes would need to be allocated for the private key if the raw bytes
  were encrypted as opposed to ASCII representing an array of bytes.
- **`KeyPairAccount` struct**: This represents the account that will store the
  public key and the encrypted private key.
  It uses the `#[account]` attribute to tell Anchor that this struct will be
  stored on the Solana blockchain.

## Unit Tests

Just like regular development with Rust, unit tests and doc tests can be
added to any of the Rust modules in `programs/key_pegboard/src`.
For example, add the following unit tests after the contract code.

**programs/key_pegboard/src/lib.rs** partial listing
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_account_space_allocation() {
        // Ensure that 8 (discriminator) + INIT_SPACE is sufficient
        // for the maximum allowed encrypted key size (128 bytes).
        let expected_space = 8 + 32 + (4 + 128); // discriminator + pubkey + (vec prefix + data)
        assert_eq!(8 + KeyPairAccount::INIT_SPACE, expected_space);
        println!("Account space validation passed: {} bytes", expected_space);
    }

    #[test]
    fn test_key_pair_struct_initialization() {
        let test_pubkey = Pubkey::new_unique();
        let test_data = vec![1, 2, 3, 4, 5];

        let account = KeyPairAccount {
            public_key: test_pubkey,
            encrypted_private_key: test_data.clone(),
        };

        assert_eq!(account.public_key, test_pubkey);
        assert_eq!(account.encrypted_private_key.len(), 5);
        assert_eq!(account.encrypted_private_key, test_data);
    }
}
```

In Rust, a doc test is written inside triple-slash `///` comments.
When you run `cargo test`,
Rust compiles and executes the code blocks found in your documentation
to ensure your examples never go out of date.
Also, feel free to add the following doc test to the contract.

**programs/key_pegboard/src/lib.rs** partial listing
```rust
#[program]
pub mod key_pegboard {
    use super::*;

    /// Publishes a public key and its encrypted private key to the ledger.
    ///
    /// # Example (Doc Test)
    /// ```
    /// use anchor_lang::prelude::Pubkey;
    ///
    /// // Mocking data for doc test demonstration
    /// let pk = Pubkey::default();
    /// let encrypted = vec![1, 2, 3];
    ///
    /// assert_eq!(encrypted.len(), 3);
    /// assert_eq!(pk.to_bytes().len(), 32);
    /// ```
    pub fn publish_key_pair(
        ctx: Context<KeyPairContext>,
        public_key: Pubkey,
        encrypted_private_key: Vec<u8>,
    ) -> Result<()> {
        let key_pair = &mut ctx.accounts.key_pair;
        key_pair.public_key = public_key;
        key_pair.encrypted_private_key = encrypted_private_key;
        Ok(())
    }
}
```

For now, we only want to run the tests for this particular crate in the
umbrella project.
Anchor's integration tests, covered below, will fail without special setup.
Run the following command to test the `key_pegboard` crate.

```sh
cargo test -p key_pegboard
```

If you added all of the above tests, you should see output like the following.

```sh
running 3 tests
test test_id ... ok
test tests::test_account_space_allocation ... ok
test tests::test_key_pair_struct_initialization ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests key_pegboard

running 1 test
test programs/key_pegboard/src/lib.rs - key_pegboard::publish_key_pair (line 13) ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.30s
```

The `test_id ... ok` result is automatically generated by Anchor.
The `declare_id!()` macro at the top of the program generates several
helper functions to manage the program's unique address,
including a test that simply verifies the ID constant is
correctly formatted and matches the expected public key.

## Integration Tests

The integration tests are located in the `tests` directory in the project root.
Assuming the project was generated with
`anchor init --test-template rust "${PROJECT_NAME}"`,
this is a Rust crate that exists specifically for testing contracts written
with Anchor.
If the `--test-template rust` flag was omitted, it will contain TypeScript.
This guide only covers Rust-based integration tests.

The existing test no longer works because the contract has diverged from the
template code generated by `anchor init`.
We will delete the existing test code and replace it.

```sh
rm tests/src/*.rs
```

Proactively update `Cargo.toml`.
The new test code requires the following crates.

```sh
cargo add -p tests \
    base64 bip39 -F bip39/rand openssl rand solana-system-interface
```

Add `lib.rs` and `test_publish_key_pair.rs`.

**tests/src/lib.rs** full listing
```rust
#[cfg(test)]
mod test_publish_key_pair;
```

**tests/src/test_publish_key_pair.rs** full listing
```rust
// tests/src/test_publish_key_pair.rs
use anchor_client::{
    solana_sdk::{
        commitment_config::CommitmentConfig,
        pubkey::Pubkey,
        signature::{read_keypair_file, Keypair, SeedDerivable, Signature, Signer},
    },
    Client, Cluster,
};
use base64::{engine::general_purpose, Engine as _};
use bip39::{Language, Mnemonic};
use openssl::symm::{decrypt, encrypt, Cipher};
use rand::Rng;
use solana_system_interface::program;
use std::{thread, time::Duration};

struct KeypairPayload {
    instruction: key_pegboard::instruction::PublishKeyPair,
    seed_phrase: String,
    one_time_key_b64: String,
}

#[test]
fn test_publish_key_pair() -> Result<(), Box<dyn std::error::Error>> {
    let program_id = key_pegboard::ID;
    let anchor_wallet = std::env::var("ANCHOR_WALLET")?;
    let signer = read_keypair_file(&anchor_wallet)?;

    let client =
        Client::new_with_options(Cluster::Localnet, &signer, CommitmentConfig::confirmed());
    let program = client.program(program_id)?;

    let payload = create_publish_key_pair_instruction()?;
    let instruction = payload.instruction;
    let seed_phrase = payload.seed_phrase;
    let one_time_key_b64 = payload.one_time_key_b64;
    let expected_public_key = instruction.public_key;
    let expected_encrypted_private_key = instruction.encrypted_private_key.clone();
    let (new_keypair_account_pubkey, _bump) = Pubkey::find_program_address(
        &[b"key-pegboard", &instruction.public_key.as_ref()],
        &program_id,
    );

    // Debug logging
    println!("\n--- Request Data ---");
    println!("Using program ID: {}", program_id);
    println!("Signer public key: {}", signer.pubkey());
    println!(
        "New keypair account public key: {}",
        new_keypair_account_pubkey
    );
    println!("--------------------\n");

    let account = key_pegboard::accounts::KeyPairContext {
        key_pair: new_keypair_account_pubkey,
        signer: signer.pubkey(),
        system_program: Pubkey::from(program::ID.to_bytes()),
    };

    let tx = program
        .request()
        .accounts(account)
        .args(instruction)
        .signer(&signer)
        .send()?;
    assert_ne!(
        tx,
        Signature::default(),
        "Transaction signature should not be empty."
    );

    // Debug logging
    println!("\n--- Secure Private Transmission Data ---");
    println!("SEED PHRASE:\n{}", seed_phrase);
    println!("ONE TIME KEY:\n{}", one_time_key_b64);
    println!("TRANSACTION:\n{}", tx);
    println!("----------------------------------------\n");

    // Verify publication
    let actual: key_pegboard::KeyPairAccount = {
        let rpc = program.rpc();
        let sleep_time = 100; // ms
        let attempt_time = 30_000; // ms
        let max_attempts = attempt_time / sleep_time;
        let mut result = None;

        for _ in 0..max_attempts {
            thread::sleep(Duration::from_millis(sleep_time));
            let statuses = rpc.get_signature_statuses(&[tx])?.value;

            if let Some(Some(status)) = statuses.get(0) {
                if let Some(err) = &status.err {
                    return Err(format!("Transaction failed: {:?}", err).into());
                }

                if status.confirmation_status.is_some() {
                    // fetch state after tx has been confirmed
                    if let Ok(data) = program.account(new_keypair_account_pubkey) {
                        result = Some(data);
                        break;
                    }
                }
            }
        }
        result.ok_or_else(|| {
            format!(
                "Transaction confirmation timed out after {} seconds for tx {}",
                attempt_time / 1000,
                tx
            )
        })?
    };
    assert_eq!(expected_public_key, actual.public_key);
    assert_eq!(expected_encrypted_private_key, actual.encrypted_private_key);

    Ok(())
}

// the data is large and it detracts from the test setup
fn create_publish_key_pair_instruction() -> Result<KeypairPayload, Box<dyn std::error::Error>> {
    let mnemonic = Mnemonic::generate_in(Language::English, 12)?;
    let seed_phrase = mnemonic.to_string();
    let seed_bytes = mnemonic.to_seed("");
    let keypair = Keypair::from_seed(&seed_bytes[0..32])?;
    let public_key = keypair.pubkey();
    let secret_bytes = keypair.to_bytes();

    let mut one_time_key = [0u8; 32];
    rand::rng().fill(&mut one_time_key);
    let one_time_key_b64 = general_purpose::STANDARD.encode(one_time_key);

    let mut iv = [0u8; 16];
    rand::rng().fill(&mut iv);

    let cipher = Cipher::aes_256_cbc();
    let ciphertext = encrypt(cipher, &one_time_key, Some(&iv), &secret_bytes)?;

    let mut encrypted_private_key = iv.to_vec();
    encrypted_private_key.extend(ciphertext);

    let (extracted_iv, encrypted_data) = encrypted_private_key.split_at(16);
    let decrypted = decrypt(cipher, &one_time_key, Some(extracted_iv), encrypted_data)?;
    assert_eq!(secret_bytes.to_vec(), decrypted, "Integrity check failed.");

    Ok(KeypairPayload {
        instruction: key_pegboard::instruction::PublishKeyPair {
            public_key,
            encrypted_private_key,
        },
        seed_phrase,
        one_time_key_b64,
    })
}
```

It is a good idea to sync keys before running integration tests for
the first time, or if you have a reason to believe they are out of sync.
If code was copied into your local project, the keys probably do need to be synced.
Run the following command to fix any discrepancies.

```sh
anchor keys sync
```

Integration tests can be run with the following command.
Note that integration tests are not strictly deterministic,
and they can fail for a number of reasons even if the contract
and testing code is properly written.

```sh
anchor test
```

The test code generates a client that is used to communicate with the
specified Solana network.
In this case, it is the local network.
`cargo test` fails where `anchor test` succeeds because the latter spins
up the local Solana validator.

Next, the test calls the smart contract.
After that, it verifies publication and makes sure the expected values
were published.
The `create_publish_key_pair_instruction` routine exists because:
- dynamic instruction setup for this contract is involved
- the logic distracts from the general testing flow

The test code also includes many bells and whistles.

Note that you can manually start the local Solana test validator with the following command.

```sh
solana-test-validator
```

In a separate terminal, you can test against the running validator.

```sh
anchor test --skip-local-validator
```

Details are out of scope for this guide, but you can browse transactions on
your local validator using the [Solana Explorer][solana_explorer] web interface.
Alternatively, the local CLI tools can be used if you prefer the terminal.
Commands like the following can be used.

```sh
PDA_ADDRESS="valid_pda_address_here"
solana account "${PDA_ADDRESS}" --url localhost
TRANSACTION_SIGNATURE="valid_transaction_signature_here"
solana confirm -v "${TRANSACTION_SIGNATURE}" --url localhost
solana logs --url localhost
```

# Future Reading

This is enough to get started with Solana using Rust.
The [Solana Anchor Docs][solana_anchor] go into more detail and cover topics
like deployment beyond the local cluster, and using wallets for gas payments.
Although this toy app is simple, it is a lot closer to a production application
than apps in the Solana quick start guide.

DeFi developers looking for more in depth Rust material should read the Rust book,
[The Rust Programming Language][rust_book], if they have not already done so.
Rust is very well documented, and it has books dedicated to a variety of topics.

## References:

- [Rust, Installation Guide][rust_install]
- [Rust, The Rust Programming Language][rust_book]
- [Solana, Anchor][solana_anchor]
- [Solana, Explorer][solana_explorer]
- [Solana, CLI Installation Guide][solana_cli_install]

[rust_install]: https://www.rust-lang.org/learn/get-started
[solana_anchor]: https://www.anchor-lang.com/docs
[solana_explorer]: https://explorer.solana.com
[solana_cli_install]: https://docs.solana.com/cli/install-solana-cli-tools

