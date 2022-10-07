---
layout: post
mathjax: false
comments: true
title:  "Using cc-rs to Mix Rust with C, C++, and ASM"
date:   2022-10-07 20:34:48 +0000
categories: rust c c++ asm
---
New projects often need to incorporate existing code.
Sometimes that code is written in a different programming language.
The post covers using the [cc-rs crate][rust_cc_rs] to compile C,
C++, and ASM code into a Rust project.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2022-10-07 20:34:48 +0000
$ uname -vm
Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000 arm64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
macOS 12.6
$ echo "${SHELL}"
/bin/bash
$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin21)
$ cat "${HOME}/Developer/PlaydateSDK/VERSION.txt"
1.12.3
$ cargo --version
cargo 1.66.0-nightly (0b84a35c2 2022-10-03)
{% endhighlight %}

## Instructions

First, create a new project.

{% highlight sh %}
PROJECT="rust_c_cpp_asm_interop_example"
cargo new "${PROJECT}"
cd "${PROJECT}"
{% endhighlight %}

Add **cc-rs** to the build dependencies.

**Cargo.toml** Partial Listing

{% highlight toml %}
[build-dependencies]
cc = "1.0"
{% endhighlight %}

Create a build script.

**build.rs**
{% highlight rust %}
fn main() {
  cc::Build::new()
    .file("src/hello_c.c")
    .compile("hello_c");

  cc::Build::new()
    .cpp(true)
    .file("src/hello_cpp.cpp")
    .compile("hello_cpp");

  cc::Build::new()
    .file("src/hello_asm.s")
    .compile("hello_asm");
}
{% endhighlight %}

Mixing ASM with either C or C++ is OK, but mixing C and C++ does not work.

{% highlight rust %}
  // OK
  cc::Build::new()
    .file("src/hello_c.c")
    .file("src/hello_asm.s")
    .compile("hello");

  // OK
  cc::Build::new()
    .cpp(true)
    .file("src/hello_cpp.cpp")
    .file("src/hello_asm.s")
    .compile("hello");

  // broken
  cc::Build::new()
    .file("src/hello_c.c")
    .file("src/hello_cpp.cpp")
    .compile("hello");

  // broken
  cc::Build::new()
    .file("src/hello_c.c")
    .cpp(true)
    .file("src/hello_cpp.cpp")
    .compile("hello");
{% endhighlight %}

Modify **src/main.rs** to call the external functions.

**src/main.rs**
{% highlight rust %}
extern {
  fn hello_c();
  fn hello_cpp();
  fn hello_asm();
}

#[no_mangle]
#[inline(never)]
fn hello_rust() {
  println!("Hello, Rust!");
}

fn main() {
  hello_rust();
  unsafe {
    hello_c();
    hello_cpp();
    hello_asm();
  }
}
{% endhighlight %}

Add the C file.

**src/hello_c.c**
{% highlight c %}
#include <stdio.h>

void hello_c(void) {
  printf("Hello, C!\n");
}
{% endhighlight %}

Add the C++ file.

**src/hello_cpp.cpp**
{% highlight cpp %}
#include <iostream>
using namespace std;

extern "C" {
  void hello_cpp() {
    cout << "Hello, C++!" << endl;
  }
}
{% endhighlight %}

Add the ASM file.
You will need the version of the .s file for your microarchitecture.

**src/hello_asm.s** 64-bit ARM for Apple Silicon
{% highlight nasm %}
        .set ALIGNMENT, 8

.text
        .balign ALIGNMENT
        .global _hello_asm
_hello_asm:
        stp     x29, x30, [sp, #-16]!
        mov     x29, sp
        adrp    x0, hello.format@PAGE
        add     x0, x0, hello.format@PAGEOFF
        bl      _printf
        ldp     x29, x30, [sp], #16
        ret

.data
        .balign ALIGNMENT
hello.format:
        .asciz "Hello, ASM!\n"
        .balign ALIGNMENT
{% endhighlight %}

**src/hello_asm.s** x86-64 (Untested)
{% highlight nasm %}
        .intel_syntax
        .set ALIGNMENT, 16
.text
        .global _hello_asm
_hello_asm:
        push    rbp
        mov     rbp, rsp
        lea     rdi, [rip + _hello.format]
        call    _printf
        pop     rbp
        ret
_hello.end:
_hello.format:
       .string "Hello, ASM!\n"
{% endhighlight %}

**src/hello_asm.s** 32-bit ARM (Untested)
{% highlight nasm %}
        .syntax unified
        .set ALIGNMENT, 8
.text
        .align ALIGNMENT
        .global hello_asm
hello_asm:
        push    {ip, lr}
        adr     r0, hello.format
        bl      printf
        popeq   {ip, pc}

@ Data needs to be in .text for PIE
@.data
hello.format:
        .asciz "Hello, ASM!\n"
        .align ALIGNMENT
{% endhighlight %}

The program should generate the following output.

{% highlight sh %}
$ cargo run
Hello, Rust!
Hello, C!
Hello, C++!
Hello, ASM!
{% endhighlight %}

#### Inspecting ASM with cargo-show-asm

The [cargo-show-asm subcommand][rust_cargo_show_asm] can be used to inspect
ASM code.
Install it with the following command.

{% highlight sh %}
cargo install cargo-show-asm
{% endhighlight %}

On macOS, the following command may need to be used instead.

{% highlight sh %}
cargo install cargo-show-asm --features vendored-openssl,vendored-libgit2
{% endhighlight %}

Use the following command to get a list of symbols that can be inspected.
Note that the **hello_rust** symbol is not listed.

{% highlight sh %}
PROJECT="rust_c_cpp_asm_interop_example"
cargo asm --bin "${PROJECT}"
{% endhighlight %}

Inspect the code from the main binary using the following command.

{% highlight sh %}
PROJECT="rust_c_cpp_asm_interop_example"
cargo asm --bin "${PROJECT}" main
{% endhighlight %}

Upon inspecting the code, note that **main** branches to **hello_rust**.
The function is not inlined and the name is not mangled.
If you know ASM, it might be possible to write a **hello_asm** routine
using this kind of output.

#### Generating and Inspecting ASM with the Godbolt Compiler Explorer

If none of the **hello_asm** routines work for your architecture, the
[Godbolt Compiler Explorer][godbolt] is likely a better tool for generating
one than inspecting Rust code.
Select "C" as the language in the lefthand panel, and enter the following code.

{% highlight c %}
void hello_asm() {
  printf("Hello, ASM!");
}
{% endhighlight %}

In the righthand panel, select a compiler that corresponds to your platform.
For example, **armv8-a clang 14.0.0** gives output that is very close to the
version of **src/hello_asm.s** that was tested on Apple Silicon.

{% highlight c %}
hello_asm:                              // @hello_asm
        stp     x29, x30, [sp, #-16]!           // 16-byte Folded Spill
        mov     x29, sp
        adrp    x0, .L.str
        add     x0, x0, :lo12:.L.str
        bl      printf
        ldp     x29, x30, [sp], #16             // 16-byte Folded Reload
        ret
.L.str:
        .asciz  "Hello, ASM!"
{% endhighlight %}

## References:

- [Godbolt Compiler Explorer][godbolt]
- [Rust Home Page][rust]
- [Rust, cargo-show-asm Subcommand][rust_cargo_show_asm]
- [Rust, cc-rs Crate][rust_cc_rs]

[godbolt]: https://godbolt.org
[rust]: https://www.rust-lang.org
[rust_cargo_show_asm]: https://crates.io/crates/cargo-show-asm
[rust_cc_rs]: https://crates.io/crates/cc

