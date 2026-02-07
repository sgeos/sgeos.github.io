---
layout: post
mathjax: false
comments: true
title:  "no_std Rust with bin and lib"
date:   2022-10-06 18:51:30 +0000
categories: rust no_std
---

<!-- A58 -->

Splitting [Rust][rust] programs into a binary and a library is a common pattern.
The binary has a **main()** entry point, and the library typically has a
**run()** function.
This post will cover setting up a project that uses this pattern, including
multiple binaries in one project.
The post will then convert the project to no_std Rust.
no_std Rust is used for embedded systems development, and getting a working
no_std project template may entail a few more headaches than someone getting
started wants to deal with.

## Software Versions

{% highlight sh %}
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2022-10-06 18:51:30 +0000
$ uname -vm
Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000 arm64
$ ex -s +'%s/<[^>].\{-}>//ge' +'%s/\s\+//e' +'%norm J' +'g/^$/d' +%p +q! /System/Library/CoreServices/SystemVersion.plist | grep -E 'ProductName|ProductVersion' | sed 's/^[^ ]* //g' | sed 'N; s/\n/ /g'
macOS 12.6
$ sysctl -n machdep.cpu.brand_string
Apple M1 Max
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

#### std Project with a Binary and Library

First, create a new project with **cargo**.

{% highlight sh %}
PROJECT="no_std_bin_lib_template"
cargo new "${PROJECT}"
cd "${PROJECT}"
{% endhighlight %}

Optionally, test the project.

{% highlight sh %}
$ cargo run
Hello, world!
{% endhighlight %}

Next, copy **main.rs** to **lib.rs**.

{% highlight sh %}
cp src/main.rs src/lib.rs
{% endhighlight %}

In **lib.rs**, rename **main** to **run** and make some boilerplate changes
so the library **run()** function can be called as if it were a C function.

**src/lib.rs**
{% highlight rust %}
#[no_mangle]
pub extern "C" fn run() {
  println!("Hello, world!");
}
{% endhighlight %}

Call the **run()** function in **main.rs**, 

**src/main.rs**
{% highlight rust %}
use lib::run;

fn main() {
  run();
}
{% endhighlight %}

Next, edit **Cargo.toml** and specify that the project contains a binary and
a library that can be built.

**Cargo.toml**
{% highlight toml %}
[package]
name = "no_std_bin_lib_template"
version = "0.1.0"
edition = "2021"

[lib]
name = "lib"
path = "src/lib.rs"

[[bin]]
name = "main"
path = "src/main.rs"

[dependencies]
{% endhighlight %}

Finally, build and run to make sure that the project works.
If the project was tested before changes were made,
the output should be the same.

{% highlight sh %}
$ cargo run
Hello, world!
{% endhighlight %}

That is all there is to splitting a std Rust project into a binary and library.

#### Multiple Binaries

A project can contain multiple binaries, but only one library.
If multiple binaries exist, **default-run** will need to be defined for
**cargo run** to work.

{% highlight sh %}
cp src/main.rs src/main_a.rs
cp src/main_a.rs src/main_b.rs
{% endhighlight %}

**Cargo.toml**
{% highlight toml %}
[package]
name = "no_std_bin_lib_template"
version = "0.1.0"
edition = "2021"
default-run = "main_a"

[lib]
name = "lib"
path = "src/lib.rs"

[[bin]]
name = "main_a"
path = "src/main_a.rs"

[[bin]]
name = "main_b"
path = "src/main_b.rs"

[dependencies]
{% endhighlight %}

Alternatively, the **--bin** flag can be used to specify which binary to run.

{% highlight sh %}
$ cargo run --bin main_b
Hello, world!
{% endhighlight %}

The extra main files will not be needed in the next steps.

{% highlight sh %}
rm src/main_?.rs
{% endhighlight %}

#### no_std Rust

First, convert **lib.rs** to no_std Rust that relies on libc to write
to stdout.  Feel free to later remove the libc dependency if it does not make
sense for your real project, but the terminal output is very handy for making
sure the project template works.

**src/lib.rs**
{% highlight rust %}
#![no_std]

extern crate libc;

#[no_mangle]
pub extern "C" fn run() {
  const MESSAGE: &'static str = "Hello, no_std Rust!\n\0";
  unsafe {
    libc::printf(MESSAGE.as_ptr() as *const _);
  }
}
{% endhighlight %}

Add libc to the dependencies in **Cargo.toml**.

**Cargo.toml**
{% highlight toml %}
[package]
name = "no_std_bin_lib_template"
version = "0.1.0"
edition = "2021"

[lib]
name = "lib"
path = "src/lib.rs"

[[bin]]
name = "main"
path = "src/main.rs"

[dependencies.libc]
version = "0.2"
default-features = false
features = ["extra_traits"]
{% endhighlight %}

At this point, the std Rust **main()** function should be able to call the
no_std Rust **run()** function.

{% highlight sh %}
$ cargo run
Hello, no_std Rust!
{% endhighlight %}

The next step is to convert **main()** to no_std Rust.

**src/main.rs**
{% highlight rust %}
#![no_std]
#![no_main]

use lib::run;

#[no_mangle]
pub extern "C" fn main(_argc: isize, _argv: *const *const u8) -> isize {
  run();
  0
}

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
  loop {}
}
{% endhighlight %}

Specify a panic setting in **Cargo.toml**.

{% highlight toml %}
[package]
name = "no_std_bin_lib_template"
version = "0.1.0"
edition = "2021"

[lib]
name = "lib"
path = "src/lib.rs"

[[bin]]
name = "main"
path = "src/main.rs"

[profile.dev]
panic = "abort"

[profile.release]
panic = "abort"

[dependencies.libc]
version = "0.2"
default-features = false
features = ["extra_traits"]
{% endhighlight %}

The no_std template is complete.
The no_std **main()** function is now calling the no_std **run()** function!

{% highlight sh %}
$ cargo run
Hello, no_std Rust!
{% endhighlight %}

#### Removing the libc Dependency

Remove the libc-related code from **src/lib.rs**.

**src/lib.rs**
{% highlight rust %}
#![no_std]

#[no_mangle]
pub extern "C" fn run() { }
{% endhighlight %}

Also, remove the libc dependency from **Cargo.toml**.

**Cargo.toml**
{% highlight toml %}
[package]
name = "no_std_bin_lib_template"
version = "0.1.0"
edition = "2021"

[lib]
name = "lib"
path = "src/lib.rs"

[[bin]]
name = "main"
path = "src/main.rs"

[profile.dev]
panic = "abort"

[profile.release]
panic = "abort"

[dependencies]
{% endhighlight %}

If you try building and running, an error will be generated because macOS
expects binaries to be linked to libc.
To build the binary, extra parameters will need to be passed to the linker.
Also, **cargo** needs to explicitly be told to build the binary.
See [this article][rust_freestanding] for more information.

{% highlight sh %}
BINARY="main"
cargo rustc --bin "${BINARY}" -- -C link-args="-e _main -static -nostartfiles"
./target/debug/${BINARY}
{% endhighlight %}

The library does not have an entry point, and there is only one in any given
project, so fewer parameters need to be passed to the linker.
**cargo** still needs to explicitly be told to build the library.

{% highlight sh %}
cargo rustc --lib -- -C link-args="-static -nostartfiles"
ls target/debug/lib*.rlib
{% endhighlight %}

Testing the program gives the following results.

{% highlight sh %}
$ ./target/debug/${BINARY}
Killed: 9
{% endhighlight %}

Something is clearly wrong.
A bare metal no_std program was compiled and run on an operating system.
The **start** entry point typically does things that the operating system
assumes are being handled, like initializing the stack.
In practice, a no_std Rust program that does not rely on libc will probably
be running on an embedded device without an operating system to kill it.
In any case, where this template goes is beyond the scope of this post.

#### More Information

The [Rust Embedded Workgroup][rust_embedded_workgroup] has produced useful
[documentation][rust_embedded] that is useful for programmers who need to
use no_std Rust.
The [Embedonomicon][rust_embedonomicon] and the
[Embedded Rust Book][rust_embedded_book] are two core resources.

## References:

- [Rust Homepage][rust]
- [Rust, A Freestanding Rust Binary][rust_freestanding]
- [Rust, Embedonomicon][rust_embedonomicon]
- [Rust, Embedded Rust Book][rust_embedded_book]
- [Rust, Embedded Rust Documentation][rust_embedded]
- [Rust, Rust Embedded Workgroup][rust_embedded_workgroup]

[rust]: https://www.rust-lang.org
[rust_embedded]: https://docs.rust-embedded.org
[rust_embedded_book]: https://docs.rust-embedded.org/book/index.html
[rust_embedded_workgroup]: https://github.com/rust-embedded
[rust_embedonomicon]: https://docs.rust-embedded.org/embedonomicon/
[rust_freestanding]: https://os.phil-opp.com/freestanding-rust-binary/#macos

