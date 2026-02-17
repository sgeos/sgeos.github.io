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
The Hello World program uses a `.rodata` section for string data
and the `lddw` instruction to load symbol addresses at runtime.
The article also discusses the current state of mixed Rust and assembly projects,
including a theoretical approach for linking sBPF assembly object files
into a Rust project using a Cargo build script.

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
The program declares the string "Hello, sBPF!" in a read-only data section
and invokes the `sol_log_` syscall to print it.

`src/main.s` full listing

```asm
.equ MESSAGE_LEN, 12 # length of "Hello, sBPF!"
.equ SUCCESS, 0       # successful program execution

.globl entrypoint
entrypoint:
    # Load the address of the message string into r1.
    lddw r1, message

    # Load the message length into r2.
    # sol_log_ takes a pointer in r1 and a length in r2.
    mov64 r2, MESSAGE_LEN
    call sol_log_

    # Exit with success (return code 0).
    mov64 r0, SUCCESS
    exit

.rodata
message:
    .ascii "Hello, sBPF!"
```

The program performs the following operations.

1. The `.equ` directive defines named constants at the top of the file.
`MESSAGE_LEN` holds the byte length of the string,
and `SUCCESS` represents the return code for successful execution.
These constants produce no object code and are resolved at assembly time.
The sbpf assembler supports the same `.equ` syntax as the GNU Assembler (GAS),
following the convention `.equ NAME, value` with an optional inline `#` comment.
Named constants use SCREAMING_SNAKE_CASE by convention.

2. The `.rodata` section declares read-only data that is embedded in the program binary.
The `message` label marks the start of the string,
and the `.ascii` directive stores the raw bytes of "Hello, sBPF!" without a null terminator.
A null terminator is not required because `sol_log_` uses an explicit length argument.
The sbpf assembler supports `.ascii`, `.byte`, `.short`, `.word`, `.int`, `.long`, and `.quad`
directives in `.rodata` sections but does not support `.asciz` or `.string`.

3. The `lddw r1, message` instruction loads the 64-bit address of the `message` label into register r1.
This is a wide immediate load that the assembler resolves
to the address of the string in the `.rodata` section of the compiled ELF binary.

4. The `sol_log_` syscall is invoked with two arguments.
Register r1 contains the pointer to the string in the `.rodata` section.
Register r2 receives `MESSAGE_LEN` as the length of the string in bytes.
The syscall prints the message to the Solana runtime log.

5. The program exits with return code `SUCCESS` in register r0,
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
A Cargo build script could invoke an assembler on `.s` files
and link the resulting object files into the Rust build.
This is analogous to how the `cc` crate integrates C code into Rust projects.
The subsection below demonstrates a theoretical solution
using the Solana SDK's LLVM tools in a `build.rs` script.

All three paths are experimental.
The Solana development ecosystem does not yet provide
first-class support for mixed-language program development.

#### Linking Assembly into a Rust Project with build.rs

The Solana SDK ships LLVM tools alongside `cargo build-sbf`,
including Clang and llvm-ar.
These tools can assemble `.s` files targeting the SBF architecture,
archive the resulting object files into a static library,
and link the library into the Rust build through standard Cargo directives.
This approach follows the same pattern that Rust projects use
to integrate C code through the `cc` crate,
adapted for the SBF target triple and the Solana SDK's toolchain paths.

The following example demonstrates this approach
with a Rust entrypoint that calls an sBPF assembly logging subroutine.
The Rust code passes a string argument to the assembly function,
which constructs a formatted message on the stack and logs it
through the `sol_log_` syscall.
This example is presented as a theoretical solution for manual verification.
No public example of this specific combination has been confirmed to work.

The project structure is as follows.

```
hello_mixed/
  src/
    lib.rs              # Rust entrypoint
    log_hello.s         # sBPF assembly logging subroutine
  build.rs              # Assembles .s and links .a
  Cargo.toml
```

The assembly file defines a `log_hello` function
that accepts a pointer and length for a name string,
constructs the message "Hello sBPF from {name}!" on the stack,
and calls `sol_log_` to print it.

`src/log_hello.s` full listing

````asm
# Return codes.
.equ SUCCESS, 0                # successful execution

# Callee-saved register save slots.
.equ SAVE_R6, -8               # r6 save position on stack
.equ SAVE_R7, -16              # r7 save position on stack
.equ SAVE_R8, -24              # r8 save position on stack

# Message prefix "Hello sBPF from " as little-endian 32-bit words.
.equ MESSAGE_0, 0x6c6c6548     # "Hell"
.equ MESSAGE_1, 0x4273206f     # "o sB"
.equ MESSAGE_2, 0x66204650     # "PF f"
.equ MESSAGE_3, 0x206d6f72     # "rom "

# Message suffix and length.
.equ MESSAGE_4, 0x21            # "!"
.equ BASE_MESSAGE_LEN, 17      # prefix (16) + suffix (1)

# Stack buffer layout offsets.
.equ PREFIX_OFFSET, -88        # message buffer start on stack
.equ PREFIX_OFFSET_4, -84      # prefix byte 4
.equ PREFIX_OFFSET_8, -80      # prefix byte 8
.equ PREFIX_OFFSET_12, -76     # prefix byte 12
.equ NAME_OFFSET, -72          # name start position in buffer

.globl log_hello
log_hello:
    # Arguments: r1 = pointer to name, r2 = length of name.
    # Logs "Hello sBPF from <name>!" to the Solana runtime.

    # Save callee-saved registers.
    stxdw [r10+SAVE_R6], r6
    stxdw [r10+SAVE_R7], r7
    stxdw [r10+SAVE_R8], r8

    # Save arguments.
    mov64 r6, r1
    mov64 r7, r2

    # Store prefix "Hello sBPF from " (16 bytes) on the stack.
    mov32 r1, MESSAGE_0
    stxw [r10+PREFIX_OFFSET], r1
    mov32 r1, MESSAGE_1
    stxw [r10+PREFIX_OFFSET_4], r1
    mov32 r1, MESSAGE_2
    stxw [r10+PREFIX_OFFSET_8], r1
    mov32 r1, MESSAGE_3
    stxw [r10+PREFIX_OFFSET_12], r1

    # Copy name bytes to the stack at NAME_OFFSET.
    mov64 r8, 0
copy_loop:
    jge r8, r7, copy_done
    mov64 r3, r6
    add64 r3, r8
    ldxb r1, [r3+0]
    mov64 r3, r10
    add64 r3, NAME_OFFSET
    add64 r3, r8
    stxb [r3+0], r1
    add64 r8, 1
    ja copy_loop
copy_done:

    # Store MESSAGE_4 ("!") after the name.
    mov64 r3, r10
    add64 r3, NAME_OFFSET
    add64 r3, r7
    mov32 r1, MESSAGE_4
    stxb [r3+0], r1

    # Call sol_log_ with the complete message.
    # Total length = BASE_MESSAGE_LEN + name_length.
    mov64 r1, r10
    add64 r1, PREFIX_OFFSET
    mov64 r2, BASE_MESSAGE_LEN
    add64 r2, r7
    call sol_log_

    # Restore callee-saved registers.
    ldxdw r6, [r10+SAVE_R6]
    ldxdw r7, [r10+SAVE_R7]
    ldxdw r8, [r10+SAVE_R8]

    mov64 r0, SUCCESS
    exit

.extern sol_log_
````

Named constants are defined at the top of the file using `.equ` directives.
The `MESSAGE_0` through `MESSAGE_3` constants hold the little-endian 32-bit words
that compose the 16-byte prefix "Hello sBPF from ".
`MESSAGE_4` holds the trailing exclamation mark,
and `BASE_MESSAGE_LEN` encodes the combined length of the prefix and suffix.
Stack frame offsets for callee-saved register slots (`SAVE_R6` through `SAVE_R8`)
and buffer layout positions (`PREFIX_OFFSET` through `NAME_OFFSET`)
replace numeric literals throughout the function body.
Memory operands use the form `[r10+CONSTANT]`
where the assembler evaluates the negative constant value at assembly time.

The function saves callee-saved registers r6 through r8 on entry
and restores them before returning,
following the sBPF calling convention.
The 16-byte prefix is stored on the stack
as four words using the `MESSAGE_0` through `MESSAGE_3` constants.
The name bytes are copied one at a time from the caller-provided pointer
using a loop with `ldxb` and `stxb` instructions.
After the name, `MESSAGE_4` is appended to complete the message.

The assembly file uses Clang syntax rather than `sbpf` tool syntax.
The `jge` and `ja` instructions use label-based branches,
which Clang's eBPF assembler supports.
If the Solana SDK's Clang version does not resolve label-based jumps correctly,
replace the label references with numeric offsets.
The `.extern sol_log_` directive declares the syscall as an external symbol,
which the Solana linker resolves during the final linking stage.

The Rust entrypoint declares the assembly function
as an `extern "C"` foreign function and calls it with a byte string argument.

`src/lib.rs` full listing

````rust
#![no_std]
#![no_main]

extern "C" {
    fn log_hello(ptr: *const u8, len: u64);
}

#[no_mangle]
pub unsafe extern "C" fn entrypoint(_input: *mut u8) -> u64 {
    let name = b"Rust";
    log_hello(name.as_ptr(), name.len() as u64);
    0
}

#[cfg(target_os = "solana")]
#[no_mangle]
fn custom_panic(_info: &core::panic::PanicInfo) -> ! {
    loop {}
}
````

The program uses `#![no_std]` and `#![no_main]`
to avoid pulling in the standard library.
The `entrypoint` function is the raw Solana program entrypoint,
exported with `#[no_mangle]` and C ABI calling convention.
The `custom_panic` handler is required for `#![no_std]` programs
targeting the Solana runtime.

The build script locates the Solana SDK's LLVM tools,
invokes Clang to assemble the `.s` file into an object file,
archives the object file into a static library with llvm-ar,
and emits Cargo directives to link the library.

`build.rs` full listing

````rust
use std::env;
use std::process::Command;

fn main() {
    let out_dir = env::var("OUT_DIR").unwrap();
    let home = env::var("HOME").unwrap();

    // Locate the Solana SDK LLVM tools.
    let sdk_base = format!(
        "{}/.local/share/solana/install/active_release\
         /bin/sdk/sbf/dependencies/platform-tools/llvm/bin",
        home
    );
    let clang = format!("{}/clang", sdk_base);
    let ar = format!("{}/llvm-ar", sdk_base);

    // Assemble the .s file to a .o object file.
    let status = Command::new(&clang)
        .args([
            "-target",
            "sbf",
            "-march=bpfel+solana",
            "-c",
            "src/log_hello.s",
            "-o",
        ])
        .arg(format!("{}/log_hello.o", out_dir))
        .status()
        .expect("Failed to run clang");
    assert!(status.success(), "Assembly failed");

    // Archive the object file into a static library.
    let status = Command::new(&ar)
        .arg("rcs")
        .arg(format!("{}/liblog_hello.a", out_dir))
        .arg(format!("{}/log_hello.o", out_dir))
        .status()
        .expect("Failed to run llvm-ar");
    assert!(status.success(), "Archive creation failed");

    println!("cargo:rustc-link-search=native={}", out_dir);
    println!("cargo:rustc-link-lib=static=log_hello");
    println!("cargo:rerun-if-changed=src/log_hello.s");
}
````

The `sdk_base` path assumes the default Solana CLI installation location.
If the Solana SDK is installed elsewhere,
this path must be adjusted to point to the `llvm/bin` directory
within the platform tools.

The `Cargo.toml` for this project is minimal.

`Cargo.toml` full listing

````toml
[package]
name = "hello_mixed"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]
````

No runtime dependencies are needed
because the program uses a raw entrypoint and calls the assembly function directly.
The `cdylib` crate type produces the shared object format
that `cargo build-sbf` expects.

Build the program and deploy it to a local test validator.

```sh
$ cargo build-sbf
$ solana program deploy target/deploy/hello_mixed.so
```

The test validator log should display "Hello sBPF from Rust!"
when the program is invoked.

This `build.rs` approach is a theoretical solution
that has not been tested against all versions of the Solana SDK.
The Solana SDK's linker handles syscall resolution
for the `sol_log_` reference in the assembly object file during final linking.
The `clang -target sbf -march=bpfel+solana` flags instruct Clang
to emit SBF-compatible object code.
If the build fails, verify that the Solana SDK's `platform-tools` directory
contains the expected Clang and llvm-ar binaries,
and that the `clang -target sbf` invocation produces valid object files
for the current SDK version.

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
and a `build.rs` approach using the Solana SDK's Clang
can theoretically assemble and link `.s` files into a Rust project.
Neither approach has been publicly confirmed with a working example.

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
The hello-solana-asm repository by Dean Little demonstrates
a complete sBPF assembly program built with Clang,
including `.rodata` usage and the Solana SDK's LLVM toolchain.
The Anchor framework provides a higher-level abstraction
over Rust-based Solana program development
for teams that do not require assembly-level control.
Reverse engineering sBPF bytecode from deployed programs
is a related skill that uses the same instruction set knowledge in the opposite direction.

## References

- [Reference, Agave CLI Documentation][reference_agave_cli]
- [Reference, hello-solana-asm][reference_hello_solana_asm]
- [Reference, sbpf Tool][reference_sbpf]
- [Reference, sbpf-assembler][reference_sbpf_assembler]
- [Reference, Solana Program Limitations][reference_solana_limitations]
- [Reference, Solana Programs Documentation][reference_solana_programs]
- [Reference, solana-upstream-bpf-template][reference_upstream_bpf_template]
- [Research, Assembly 101][research_assembly_101]
- [Research, How to Write Solana Programs with sBPF Assembly][research_helius_sbpf]
- [Research, sBPF Linker Breakpoint 2025][research_sbpf_linker]
- [Research, The Solana eBPF Virtual Machine][research_solana_ebpf_vm]

[reference_agave_cli]: https://docs.anza.xyz/cli/
[reference_hello_solana_asm]: https://github.com/deanmlittle/hello-solana-asm
[reference_sbpf]: https://github.com/blueshift-gg/sbpf
[reference_sbpf_assembler]: https://crates.io/crates/sbpf-assembler
[reference_solana_limitations]: https://solana.com/docs/programs/limitations
[reference_solana_programs]: https://solana.com/docs/core/programs
[reference_upstream_bpf_template]: https://github.com/blueshift-gg/solana-upstream-bpf-template
[research_assembly_101]: https://learn.blueshift.gg/en/courses/introduction-to-assembly/assembly-101
[research_helius_sbpf]: https://www.helius.dev/blog/sbpf-assembly
[research_sbpf_linker]: https://blueshift.gg/research/sbpf-linker-breakpoint-2025
[research_solana_ebpf_vm]: https://www.anza.xyz/blog/the-solana-ebpf-virtual-machine
