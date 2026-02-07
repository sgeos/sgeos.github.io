---
layout: post
mathjax: false
comments: true
title:  "Getting Started with Cargo Workspaces for Rust Development"
date:   2022-12-01 18:34:26 +0000
categories: rust no_std
---

<!-- A61 -->

A single Rust package can contain one library and multiple binaries.
Rust dependencies can only be specified at the package level, not for each
binary in a package.
If multiple binaries require different dependencies, using a cargo workspace
is the appropriate way to organize a project.

There are multiple ways to organize a workspace.
This post will cover workspace organization for a no_std library that is
called from both std and no_std binaries.
The library will accept an FFI-safe pointer to a logging function.
The binaries will call the library, and log command line arguments using the
same function without passing it to the library.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2022-12-01 18:34:26 +0000
$ uname -vm
Darwin Kernel Version 20.6.0: Thu Sep 29 20:15:11 PDT 2022; root:xnu-7195.141.42~1/RELEASE_X86_64 x86_64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
macOS 11.7.1
$ sysctl -n machdep.cpu.brand_string
Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
$ cargo --version
cargo 1.67.0-nightly (ba607b23d 2022-11-22)
{% endhighlight %}

## Instructions

#### Workspace

First, create workspace directory and add all of the member packages for
the project.

{% highlight sh %}
mkdir workspace
cd workspace
cargo new pc
cargo new embedded
cargo new core_library --lib
{% endhighlight %}

Next, add a top level **Cargo.toml** file that lists project level metadata
and all of member packages.

**Cargo.toml**
{% highlight toml %}
[workspace.package]
version = "0.1.0"
edition = "2021"

[workspace]
members = [
  "pc",
  "embedded",
  "core_library",
]
{% endhighlight %}

#### Core Library

Move into the **core_library** package.

{% highlight sh %}
cd core_library
{% endhighlight %}

Modify **Cargo.toml**.
Note that version and edition are inherited from the workspace.

**core_library/Cargo.toml**
{% highlight toml %}
[package]
name = "core_library"
version.workspace = true
edition.workspace = true

[dependencies]
{% endhighlight %}

Add the no_std library code.
It accepts an FFI-safe logging function and uses it to print a message.

**core_library/src/lib.rs**
{% highlight rust %}
#![no_std]
extern crate alloc;
use alloc::ffi::CString;
use core::ffi::c_char;

#[no_mangle]
pub extern "C" fn run(log: extern "C" fn(*const c_char)) {
  let message = CString::new("Hello, core_library!")
    .expect("CString::new failed");
  log(message.as_ptr());
}
{% endhighlight %}

It should now be possible to build but not run the library.

{% highlight sh %}
cargo build
{% endhighlight %}

#### std Rust Binary

Move into the **pc** package.

{% highlight sh %}
cd ../pc
{% endhighlight %}

Modify **Cargo.toml**.
Note the **core_library** sibling dependency,
in addition to inherited metadata.

**pc/Cargo.toml**
{% highlight toml %}
[package]
name = "pc"
version.workspace = true
edition.workspace = true

[dependencies]
core_library = { path = "../core_library" }
{% endhighlight %}

The code for the binary follows.
Note that the **core_library** sibling dependency can be used like any
other dependency.
The code defines an FFI-safe logging function for the library, and an
adapter to the logging function that takes a String for use in local code.
It then logs a message, calls the library, and echoes the command line
arguments.

**pc/src/main.rs**
{% highlight rust %}
use core_library::run;
use std::{ env, ffi::CStr, ffi::CString, os::raw::c_char, };

extern "C" fn log(message: *const c_char) {
  let cstr = unsafe { CStr::from_ptr(message) };
  let output = String::from_utf8_lossy(cstr.to_bytes()).to_string();
  println!("{}", output);
}

fn local_log(message: String) {
  let output = CString::new(message)
    .expect("CString::new failed");
  log(output.as_ptr());
}

fn main() {
  let message = String::from("Hello, pc!");
  local_log(message);
  run(log);
  let args: Vec<String> = env::args().collect();
  for i in 1..args.len() {
    local_log(format!("{}: {}", i, args[i]));
  }
}
{% endhighlight %}

Run the binary with and without arguments to make sure everything works.

{% highlight sh %}
cargo run
cargo run -- a bc def
{% endhighlight %}

#### no_std Rust Binary

Finally, move into the **embedded** package.

{% highlight sh %}
cd ../embedded
{% endhighlight %}

Modify **Cargo.toml**.
This binary depends on **libc_alloc** because it is
a core+alloc no_std binary.

**embedded/Cargo.toml**
{% highlight toml %}
[package]
name = "embedded"
version.workspace = true
edition.workspace = true

[dependencies]
core_library = { path = "../core_library" }
libc_alloc = "1.0.3"
{% endhighlight %}

The code for the binary does exactly the same thing as the std Rust code.
Lacking std results in more verbose code that is a little harder to follow.

**embedded/src/main.rs**
{% highlight rust %}
#![no_std]
#![no_main]
#![feature(lang_items)]
#![feature(rustc_private)]
#![feature(default_alloc_error_handler)]
#[global_allocator]
static ALLOCATOR: ::libc_alloc::LibcAlloc = ::libc_alloc::LibcAlloc;

#[macro_use]
extern crate alloc;
extern crate libc;

use alloc::{ ffi::CString, string::String, string::ToString };
use core::{ ffi::c_char, ffi::CStr, };
use core_library::run;
use libc::c_int;

pub extern "C" fn log(message: *const c_char) {
  let format = format!("%s\n\0");
  unsafe {
    libc::printf(
      format.as_ptr() as *const _,
      message,
    );
  }
}

fn local_log(message: String) {
  let output = CString::new(message)
    .expect("CString::new failed");
  log(output.as_ptr());
}

#[no_mangle]
pub extern "C" fn main(argc: c_int, argv: *const *const c_char) -> c_int {
  let message = String::from("Hello, embedded!");
  local_log(message);
  run(log);
  for i in 1..argc {
    let cstr = unsafe { CStr::from_ptr(*argv.offset(i as isize)) };
    let safe_string = String::from_utf8_lossy(cstr.to_bytes()).to_string();
    let output = format!("{}: {}", i, safe_string);
    local_log(output);
  }
  return 0;
}

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
  loop {}
}

#[lang = "eh_personality"]
extern "C" fn eh_personality() {}
{% endhighlight %}

It should run just like the std version, with slightly different output.

{% highlight sh %}
cargo run
cargo run -- a bc def
{% endhighlight %}

#### Specifying Targets in a Workspace

Commands like **cargo build** will operate on the curent package, or on all
package if in the top level of the workspace.
The **--workspace** command-line flag can be used to build all targets from
anywhere in the workspace, and the **-p** or **--package** flag can be used
to specify a particular package.

{% highlight sh %}
# return to the top level of the workspace
cd ..

# this is where built targets live
ls target/debug/

# remove all built targets to verify that they are rebuilt
cargo clean

# run the following commands from anywhere in the workspace
cargo build --workspace
cargo build -p core_library
cargo run --package pc
cargo run --package pc -- one two three
cargo run -p embedded
cargo run -p embedded -- one two three
{% endhighlight %}

#### More Information

The [Cargo][rust_cargo_workspaces]
and [Rust Programming Language][rust_programming_workspaces]
books have sections on workspaces.
The [documentation for std::ffi][rust_std_ffi]
can be useful for FFI work involving strings.
Note that the types are reexported to **std**, but they need to be pulled
in from **core** or **alloc** in no_std Rust.
The [Embedded Rust Book][rust_embedded] is a good place to get started with
no_std Rust.

## References:

- [Rust, Cargo Book, 3.3 Workspaces][rust_cargo_workspaces]
- [Rust, Embedded Rust Book][rust_embedded]
- [Rust, Rust Programming Language, 14.3 Cargo Workspaces][rust_programming_workspaces]
- [Rust, std::ffi Documentation][rust_std_ffi]

[rust_cargo_workspaces]: https://doc.rust-lang.org/cargo/reference/workspaces.html
[rust_embedded]: https://docs.rust-embedded.org/book/intro/no-std.html
[rust_programming_workspaces]: https://doc.rust-lang.org/book/ch14-03-cargo-workspaces.html
[rust_std_ffi]: https://doc.rust-lang.org/std/ffi/index.html

