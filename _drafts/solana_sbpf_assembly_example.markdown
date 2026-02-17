---
layout: post
mathjax: false
comments: true
title:  "Solana sBPF Assembly Example"
date:   2026-03-01 00:01:00 +0000
categories: solana assembly
---

<!-- Axxx -->

Solana programs execute inside a virtual machine that implements the Solana Berkeley Packet Filter
instruction set, commonly abbreviated sBPF.
This instruction set is a fork of the extended Berkeley Packet Filter (eBPF) architecture
originally developed for Linux kernel packet filtering,
adapted for deterministic smart contract execution on a blockchain.
Every Solana program, whether written in Rust, C, or assembly,
compiles to sBPF bytecode and runs inside the same virtual machine on every validator.

Writing Solana programs directly in sBPF assembly provides complete transparency
over the instructions that execute on-chain.
Assembly programs are dramatically smaller than their Rust equivalents,
reducing deployment costs and improving load times.
A single line of Rust can compile to hundreds of sBPF instructions,
and the compiled output is not always predictable.
Assembly programming eliminates this opacity
and enables precise control over compute unit consumption.

This article demonstrates writing, building, and deploying
a Solana program in sBPF assembly using standalone `.s` files.
The `sbpf` tool provides a lightweight assembler and linker
that compiles assembly files directly into deployable Solana programs
without requiring the full LLVM toolchain or Solana platform tools.
The article also discusses the current state of mixed Rust and assembly projects.

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

# sbpf
$ sbpf --version
TODO
```

## Background

### The sBPF Virtual Machine

Solana's virtual machine executes a custom variant of the eBPF instruction set.
Standard eBPF was designed for kernel-space operations with constraints
that would limit smart contract development,
including a prohibition on loops and a tiny 512-byte stack.
Solana's fork relaxes these constraints
while maintaining safety through compute unit budgets and deterministic execution requirements.

The key differences between sBPF and upstream eBPF include
support for loops, a larger 4KB stack frame per function call,
blockchain-specific syscalls for logging and cross-program invocation,
relocation-based syscall encoding rather than static syscalls,
and different `.rodata` symbol relocation behavior.
Every sBPF program must produce identical results on every validator,
which prohibits access to random sources, network resources, or system time from within the VM.

Solana uses rBPF, a Rust implementation of the sBPF virtual machine
maintained by Anza engineers.
The compilation target triple is `sbf-solana-solana`,
which replaced the legacy `bpfel-unknown-unknown` triple.
Programs compile to 64-bit ELF shared objects tagged for the SBF architecture.

### Registers and Memory

The sBPF instruction set provides eleven 64-bit registers.

| Register | Purpose |
|----------|---------|
| r0 | Return value |
| r1 | First argument and scratch |
| r2 | Second argument and scratch |
| r3 | Third argument and scratch |
| r4 | Fourth argument and scratch |
| r5 | Fifth argument and scratch |
| r6 | Callee-saved |
| r7 | Callee-saved |
| r8 | Callee-saved |
| r9 | Callee-saved |
| r10 | Frame pointer (read-only) |

Registers r1 through r5 are used for passing arguments to functions and syscalls.
Registers r6 through r9 are callee-saved,
meaning that called functions must preserve their values.
Register r10 is the stack frame pointer and cannot be written to.
The return value of a function or syscall is placed in r0.

The sBPF memory model divides the address space into four regions.

| Region | Base Address | Purpose |
|--------|-------------|---------|
| Code | 0x100000000 | Executable program instructions |
| Stack | 0x200000000 | Stack frames for local variables and function calls |
| Heap | 0x300000000 | Dynamically allocated memory |
| Input | 0x400000000 | Serialized transaction input data |

Each stack frame is 4KB.
Every function call allocates a new frame,
and the maximum call stack depth is 64 frames.
All memory access is bounds-checked by the virtual machine,
preventing out-of-bounds reads and writes.

### Instruction Set

The sBPF instruction set uses GNU Assembler (AT&T) syntax.
Instructions fall into several categories.

| Category | Examples | Description |
|----------|----------|-------------|
| Data movement | `mov r1, r2` / `mov r1, 42` | Copy between registers or load immediate |
| Wide immediate | `lddw r1, 0x1234567890` | Load 64-bit immediate value |
| Memory load | `ldxb r1, [r10-1]` | Load byte, halfword, word, or doubleword |
| Memory store | `stxb [r10-1], r1` | Store byte, halfword, word, or doubleword |
| Arithmetic | `add r1, r2` / `sub r1, 5` | Add, subtract, multiply, divide, modulo |
| Bitwise | `and r1, r2` / `lsh r1, 8` | AND, OR, XOR, left shift, right shift |
| Unconditional jump | `ja +4` | Jump to offset |
| Conditional branch | `jeq r1, 0, +4` | Branch if equal, not equal, greater, less |
| Function call | `call sol_log_` | Invoke syscall by name |
| Program exit | `exit` | Terminate program execution |

Load and store instructions use size suffixes to indicate access width.
The suffix `b` denotes a byte (8 bits), `h` a halfword (16 bits),
`w` a word (32 bits), and `dw` a doubleword (64 bits).
For example, `stxb` stores a byte and `ldxdw` loads a doubleword.

## Instructions

### Installing the Toolchain

The `sbpf` tool is a standalone assembler, linker, and build system
for sBPF assembly programs.
It installs as a single Rust binary of approximately 5MB,
replacing the multi-gigabyte LLVM-based Solana platform tools
for assembly development.

```sh
$ cargo install sbpf
```

The Solana CLI is also needed for local testing and deployment.

```sh
$ sh -c "$(curl -sSfL https://release.anza.xyz/stable/install)"
```

### Creating a Project

Initialize a new sBPF assembly project.

```sh
$ sbpf init hello_sbpf
$ cd hello_sbpf
```

The generated project structure includes the following files.

```
hello_sbpf/
  src/
    main.s          # sBPF assembly source
  deploy/           # compiled .so files (created by sbpf build)
  Cargo.toml        # for test dependencies
```

The `src/main.s` file contains a scaffold program.
The `deploy/` directory will contain the compiled `.so` files after building.

### Writing the Program

Replace the contents of `src/main.s` with a program
that logs a message to the Solana runtime.
The program stores the string "Hello, sBPF!" on the stack,
then invokes the `sol_log_` syscall to print it.

`src/main.s` full listing

```asm
.globl entrypoint
entrypoint:
    # Allocate space on the stack for the message.
    # r10 is the frame pointer (read-only).
    # Store "Hello, sBPF!" (12 bytes) at [r10-16] through [r10-5].

    # "Hell" = 0x6c6c6548
    mov32 r1, 0x6c6c6548
    stxw [r10-16], r1

    # "o, s" = 0x73202c6f
    mov32 r1, 0x73202c6f
    stxw [r10-12], r1

    # "BPF!" = 0x21465042
    mov32 r1, 0x21465042
    stxw [r10-8], r1

    # Null terminator is not required for sol_log_.
    # sol_log_ takes a pointer in r1 and a length in r2.
    mov64 r1, r10
    add64 r1, -16
    mov64 r2, 12
    call sol_log_

    # Exit with success (return code 0).
    mov64 r0, 0
    exit
```

The program performs the following operations.

1. The string "Hello, sBPF!" is stored on the stack in three 4-byte words
using `mov32` to load the little-endian encoded characters
and `stxw` to write each word to memory.
The frame pointer r10 provides the base address for stack access.

2. The `sol_log_` syscall is invoked with two arguments.
Register r1 receives a pointer to the start of the string on the stack.
Register r2 receives the length of the string in bytes.
The syscall prints the message to the Solana runtime log.

3. The program exits with return code 0 in register r0,
indicating successful execution.

### Building

Compile the assembly source into a deployable Solana program.

```sh
$ sbpf build
```

The build command assembles all `.s` files in the `src/` directory
and produces corresponding `.so` files in the `deploy/` directory.
The output file `deploy/hello_sbpf.so` is a 64-bit ELF shared object
containing sBPF bytecode ready for deployment.

Examine the compiled output.

```sh
$ ls -la deploy/
$ file deploy/hello_sbpf.so
```

### Deploying and Testing

Start a local Solana test validator in a separate terminal.

```sh
$ solana-test-validator
```

Configure the Solana CLI to use the local cluster.

```sh
$ solana config set --url localhost
```

Create a keypair for the program if one does not already exist.

```sh
$ solana-keygen new --outfile deploy/hello_sbpf-keypair.json --no-bip39-passphrase
```

Deploy the program to the local validator.

```sh
$ solana program deploy deploy/hello_sbpf.so --program-id deploy/hello_sbpf-keypair.json
```

The deploy command uploads the ELF binary to the Solana cluster
and registers it at the address derived from the keypair.
Note the program ID printed in the output.

Invoke the program to verify that it executes correctly.
The program logs "Hello, sBPF!" to the runtime log,
which is visible in the test validator output.

```sh
$ solana program invoke <PROGRAM_ID>
```

The test validator terminal should display a log line containing "Hello, sBPF!".

Alternatively, the `sbpf` tool provides a combined deploy command.

```sh
$ sbpf deploy
```

### Mixed Rust and Assembly Projects

A natural question is whether Rust and sBPF assembly can coexist
in the same Solana project,
allowing performance-critical sections to be written in assembly
while the rest of the program uses Rust.
As of early 2026, no stable workflow exists for this combination.

The `sbpf` tool is an assembly-only build system.
It cannot compile Rust code alongside `.s` files.
The standard Rust build tool `cargo build-sbf` has no documented mechanism
for incorporating standalone `.s` assembly files into the build pipeline.

Three potential paths forward exist, each with significant caveats.

**Inline assembly with nightly Rust.**
The `asm!()` and `global_asm!()` macros are stable in Rust
for most architectures,
but BPF target support remains behind the `asm_experimental_arch` feature gate
and requires a nightly Rust toolchain.
This path would allow embedding sBPF assembly directly in Rust source files
but is not suitable for production use on stable Rust.

```rust
#![feature(asm_experimental_arch)]

unsafe {
    core::arch::asm!(
        "mov64 r0, 0",
        "exit",
    );
}
```

**Separate compilation with sbpf-linker.**
The `sbpf-linker` tool successfully links object files
from different compilation pipelines into a single Solana program.
Projects such as clana (C), nimlana (Nim), and pylana (Python)
have demonstrated this approach with their respective languages.
The theoretical workflow for Rust and assembly would compile Rust
to object files with `cargo build-sbf`,
assemble `.s` files with the sbpf assembler,
and link both sets of object files with `sbpf-linker`.
However, no public example of this specific combination exists,
and the entrypoint management requires careful coordination.
The Rust `entrypoint!` macro and a hand-written assembly entrypoint
cannot coexist in the same binary.
Mixed projects would need to use the `no-entrypoint` Cargo feature
and define the entrypoint in assembly.

**The build.rs approach.**
A Cargo build script could invoke the sbpf assembler on `.s` files
and link the resulting object files into the Rust build.
This is analogous to how the `cc` crate integrates C code into Rust projects.
No documented example of this approach exists for the SBF target.

All three paths are experimental.
The Solana development ecosystem does not yet provide
first-class support for mixed-language program development.

## Limitations

1. The sBPF instruction set lacks a native signed division instruction.
Compilers must use software emulation for signed division and modulo operations,
which is less efficient than a hardware instruction.

2. Each stack frame is limited to 4KB.
Functions with large local variable requirements
must manage memory manually through the heap region.

3. The call stack is limited to a maximum depth of 64 frames.
Deeply recursive algorithms may exceed this limit.

4. Cross-program invocations are limited to a depth of 4.
Programs that chain multiple cross-program calls
must structure their invocation graph within this constraint.

5. All memory access is bounds-checked by the virtual machine.
While this prevents undefined behavior,
it adds overhead to every load and store instruction.

6. sBPF programs cannot access random number generators,
network resources, or system time from within the virtual machine.
All inputs must arrive through the serialized transaction data
in the input memory region.

7. The compute unit budget constrains program complexity.
Each instruction and syscall consumes a defined number of compute units,
and exceeding the budget causes the transaction to fail.
The default budget is 200,000 compute units per instruction.

8. sBPF programs must produce deterministic results on every validator.
Non-deterministic operations such as floating-point arithmetic
with rounding mode dependencies are prohibited.

9. No stable workflow exists for mixing Rust and sBPF assembly
in the same Solana project.
Inline assembly for the BPF target requires nightly Rust
with the `asm_experimental_arch` feature gate.
The sbpf-linker provides a theoretical path for linking
separately compiled object files,
but no public examples demonstrate this combination.

## Conclusion

This article demonstrated writing a Solana program in sBPF assembly
using the `sbpf` tool to assemble, build, and deploy standalone `.s` files.
The lightweight toolchain replaces the multi-gigabyte LLVM-based platform tools
with a single Rust binary,
making sBPF assembly accessible for experimentation and optimization.

Assembly programming on Solana is most appropriate
for performance-critical programs where compute unit savings justify
the loss of high-level language safety guarantees,
or for educational purposes where understanding the instruction set
provides insight into how compiled programs execute on-chain.
Mixed Rust and assembly workflows remain an open area of toolchain development.

## Future Reading

The Blueshift Introduction to Assembly course provides a structured curriculum
covering sBPF registers, memory, syscalls, and practical challenges.
The Helius blog post on sBPF assembly walks through a memo program
with detailed explanations of each instruction.
The Anchor framework provides a higher-level abstraction
over Rust-based Solana program development
for teams that do not require assembly-level control.
Reverse engineering sBPF bytecode from deployed programs
is a related skill that uses the same instruction set knowledge in the opposite direction.

## References

- [Reference, Agave CLI Documentation][reference_agave_cli]
- [Reference, sbpf Tool][reference_sbpf]
- [Reference, sbpf-assembler][reference_sbpf_assembler]
- [Reference, Solana Program Limitations][reference_solana_limitations]
- [Reference, Solana Programs Documentation][reference_solana_programs]
- [Research, Assembly 101][research_assembly_101]
- [Research, How to Write Solana Programs with sBPF Assembly][research_helius_sbpf]
- [Research, sBPF Linker Breakpoint 2025][research_sbpf_linker]
- [Research, The Solana eBPF Virtual Machine][research_solana_ebpf_vm]

[reference_agave_cli]: https://docs.anza.xyz/cli/
[reference_sbpf]: https://github.com/blueshift-gg/sbpf
[reference_sbpf_assembler]: https://crates.io/crates/sbpf-assembler
[reference_solana_limitations]: https://solana.com/docs/programs/limitations
[reference_solana_programs]: https://solana.com/docs/core/programs
[research_assembly_101]: https://learn.blueshift.gg/en/courses/introduction-to-assembly/assembly-101
[research_helius_sbpf]: https://www.helius.dev/blog/sbpf-assembly
[research_sbpf_linker]: https://blueshift.gg/research/sbpf-linker-breakpoint-2025
[research_solana_ebpf_vm]: https://www.anza.xyz/blog/the-solana-ebpf-virtual-machine
