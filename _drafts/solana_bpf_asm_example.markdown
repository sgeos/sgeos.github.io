---
layout: post
mathjax: false
comments: true
title:  "Solana BPF ASM Example"
date:   2025-12-18 22:50:41 +0000
categories: 
---
Problem description here.

## Software Versions

```sh
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2025-12-18 22:50:41 +0000
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64
```

## Instructions

Instructions for solution here.

```sh
cargo install sbpf
```

```sh
PROJECT_NAME="solana_bpf_asm_example"
cargo new --lib "${PROJECT_NAME}"
cd "${PROJECT_NAME}"
cargo add solana-program
mkdir src/bpf_asm
```

Add `src/bpf_asm/get_bpf_string.s`.

**src/bpf_asm/get_bpf_string.s** full listing
```asm
.global get_bpf_string      # makes function available for external calls

.section .rodata            # read-only data (constants)
bpf_string:
    .string "BPM ASM"       # static C-string

.text
get_bpf_string:
    lea bpf_string, %rax    # load bpm_string address into %rax register
    ret                     # return to the caller, pointer to string in %rax
```

Add `build.rs`.

**build.rs** full listing
```
use std::env;
use std::process::Command;

fn main() {
    // Tell Cargo to rerun this build script if the assembly file changes
    println!("cargo:rerun-if-changed=src/bpf_asm/get_bpf_string.s");

    // Compile the BPF assembly file into an object file
    let out_dir = env::var("OUT_DIR").unwrap();
    let asm_file = "src/bpf_asm/get_bpf_string.s";
    let object_file = format!("{}/get_bpf_string.o", out_dir);

    Command::new("clang")
        .args(&["-target", "bpf", "-O2", "-c", asm_file, "-o", &object_file])
        .status()
        .expect("Failed to compile BPF assembly");

    // Link the object file with the Rust project
    println!("cargo:rerun-if-changed={}", asm_file);
    println!("cargo:rustc-link-search=native={}", out_dir);
    println!("cargo:rustc-link-lib=static=bpf_string");
}
```

## References:

- [sBPF, What the SBPF Linker enables][bpf_video_linker] Video Tutorial
- [sBPF, blueshift Introduction to Assembly][bpf_assembly_101]
- [sBPF, How to Write Solana Programs with SBPF Assembly][bpf_solana_howto]

[bpf_assembly_101]: https://learn.blueshift.gg/en/paths/advanced-low-level/courses/introduction-to-assembly/assembly-101
[bpf_solana_howto]: https://www.helius.dev/blog/sbpf-assembly
[bpf_video_linker]: https://www.youtube.com/watch?v=cpppeXf_R50

