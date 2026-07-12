---
layout: post
mathjax: false
comments: true
title: "Getting Started with Keleusma 0.2.0"
date:   2026-05-28 09:00:00 +0000
categories: rust embedded programming
series: keleusma_getting_started
series_title: Keleusma Getting Started
series_index: 2
---
<!-- A110 -->
<script>console.log("A110");</script>

[Keleusma][kel_github] is a total functional stream-processing language
that compiles to bytecode and runs on a stack-based virtual machine.
It is an embedded language in the sense described in
[the first chapter of its guide][kel_guide_ch1].
A Keleusma program is not a whole application.
It is the small, exact, predictable part inside a larger host program,
and it is built so that several things can be proved
before the program ever runs, namely that every turn finishes
within a bounded amount of time and a bounded amount of memory.
This makes it a fit for embedded targets,
real-time audio, game logic, and any setting
where deterministic, bounded execution is a hard requirement.

Version 0.2.0 is the first publicly released line.
It introduces cryptographic module signing,
[information-flow labels][kel_guide_ifc],
[newtypes with refinement predicates][kel_guide_refinement],
and a reset instruction-set architecture.
This article is a practical tour of the 0.2.0 release.
Every code listing below was run with the version shown
in the Software Versions section, and the output shown
is the actual output produced.
This article is an on-ramp, not a complete reference.
The language ships with a
[forty-chapter guide][kel_guide]
that teaches Keleusma from first principles using music as its on-ramp,
and a separate embedding track for Rust hosts.
Readers who want the deep dive should start there.
A previous article covered
[the earlier 0.1.1 pre-release][related_post_keleusma_011],
and a companion article uses Keleusma to build
[a verifiable control kernel][related_post_control_kernel].

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-05-28 09:00:00 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 25.5.0: Mon Apr 27 20:38:56 PDT 2026; root:xnu-12377.121.6~2/RELEASE_ARM64_T6000 arm64

# Keleusma
$ keleusma --version
keleusma 0.2.0
```

## Installation

Keleusma is published on [crates.io][kel_crate] as a library,
with the command-line tool distributed as a separate crate,
[`keleusma-cli`][kel_cli_crate].
The source lives on [GitHub][kel_github],
and the API documentation is on [docs.rs][kel_docs_rs].

The [installation chapter][kel_guide_install] documents the canonical path,
which is to install the command-line tool from a source checkout.

```sh
git clone https://github.com/sgeos/keleusma
cd keleusma
cargo install --path keleusma-cli --bin keleusma
```

Confirm the installation.

```sh
$ keleusma --version
keleusma 0.2.0
```

To embed the runtime in a Rust program rather than use the tool,
add the library crate to a project instead.

```toml
[dependencies]
keleusma = "0.2"
```

## A First Program

The smallest unit of Keleusma is the `fn`, an atomic total function.
Atomic means it runs start to finish without pausing.
Total means it always finishes.
A `fn` takes its inputs, computes, and returns a result.

```keleusma
fn double(n: Word) -> Word {
    n + n
}

fn main() -> Word {
    double(21)
}
```

The command-line tool calls `main` and prints the returned value.

```sh
$ keleusma run 01_first_program.kel
42
```

## Values and Types

Keleusma has a small set of primitive types.
`Word` is the machine integer and is signed.
`Byte`, `Fixed`, and `Float` cover byte-width integers,
fixed-point numbers, and IEEE 754 floating point.
`bool` is a truth value, and `Text` is textual data.
A binding is introduced with `let` and is immutable.

```keleusma
fn main() -> Word {
    let count: Word = 6;
    let factor: Word = 7;
    let enabled: bool = true;
    if enabled {
        count * factor
    } else {
        count + factor
    }
}
```

```sh
$ keleusma run 02_values.kel
42
```

A function may return `Text`, and the tool prints it directly.

```keleusma
fn main() -> Text {
    "Keleusma"
}
```

```sh
$ keleusma run 03_text.kel
Keleusma
```

## Making Decisions

Keleusma has `if` and `else`, and it has `match` for pattern dispatch
over the variants of an `enum`.

```keleusma
enum Signal {
    Red,
    Yellow,
    Green,
}

fn delay(s: Signal) -> Word {
    match s {
        Signal::Red => 30,
        Signal::Yellow => 3,
        Signal::Green => 25,
    }
}

fn main() -> Word {
    delay(Signal::Red) + delay(Signal::Green)
}
```

```sh
$ keleusma run 04_decisions.kel
55
```

## Bounded Repetition

Keleusma has `for`, and every repetition has a count
that is known before the loop begins.
There are no unbounded loops, and there is no recursion.
These omissions are the price of the bounded-execution promise.
Because local bindings are immutable, a `for` loop inside a `fn`
does not accumulate a result. Iteration that updates state
belongs in the `loop` and `yield` function categories,
which are covered below. The example returns a value
computed by direct indexing.

```keleusma
fn main() -> Word {
    let steps = [2, 4, 8, 16];
    for s in steps {
        let _scaled = s * 10;
    }
    for i in 0..4 {
        let _i2 = i * i;
    }
    steps[3] + steps[0]
}
```

```sh
$ keleusma run 05_repetition.kel
18
```

## Structs

A `struct` groups named fields.

```keleusma
struct Note {
    pitch: Word,
    velocity: Word,
}

fn loudness(n: Note) -> Word {
    n.pitch + n.velocity
}

fn main() -> Word {
    let middle_c = Note { pitch: 60, velocity: 100 };
    loudness(middle_c)
}
```

```sh
$ keleusma run 06_structs.kel
160
```

## Multiheaded Functions and Guards

A function name may have several heads, each with its own
parameter pattern. The runtime tries the heads in source order
and dispatches to the first one whose pattern matches.
A head may carry a `when` guard after its return type.

```keleusma
fn classify(0)        -> Word           { 100 }
fn classify(n: Word)  -> Word when n > 0 { 1 }
fn classify(n: Word)  -> Word           { 0 }

fn main() -> Word {
    classify(0) + classify(5) + classify(0 - 3)
}
```

The first call matches the literal head and returns 100.
The second matches the guarded head and returns 1.
The third fails the guard and falls to the final head, returning 0.

```sh
$ keleusma run 07_multiheaded.kel
101
```

## The Pipeline Operator

The pipeline operator `|>` threads the value on its left
as the first argument to the call on its right.
It reads left to right and reduces nesting in transformation chains.

```keleusma
fn inc(x: Word) -> Word { x + 1 }
fn triple(x: Word) -> Word { x * 3 }

fn main() -> Word {
    13
    |> inc()
    |> triple()
}
```

```sh
$ keleusma run 08_pipeline.kel
42
```

## Traits and Methods

Methods are declared in a `trait` and implemented for concrete types
in `impl` blocks. The [generics and traits chapter][kel_guide_generics]
covers the full surface, including generic type parameters with bounds.

```keleusma
trait Doubler {
    fn double(x: Word) -> Word;
}

impl Doubler for Word {
    fn double(x: Word) -> Word {
        x + x
    }
}

fn main() -> Word {
    let n: Word = 21;
    n.double()
}
```

```sh
$ keleusma run 09_traits.kel
42
```

## Newtypes and Refinement Types

A [newtype][kel_guide_refinement] gives an underlying type
a distinct name, and it may carry a
[refinement][ref_refinement_type], a rule that every value must satisfy.
The rule is an ordinary predicate function, and it is checked
at every construction. A construction that provably breaks the rule
is rejected before the program runs.

```keleusma
fn in_range(x: Word) -> bool { x >= 0 and x <= 127 }

newtype Velocity = Word where in_range;

fn raw(v: Velocity) -> Word {
    v as Word
}

fn main() -> Word {
    let soft = Velocity(40);
    raw(soft)
}
```

```sh
$ keleusma run 10_newtype.kel
40
```

The value of the refinement is what it refuses.
A literal that violates the predicate is a compile-time error,
not a runtime surprise.

```keleusma
fn main() -> Word {
    raw(Velocity(200))
}
```

```sh
$ keleusma run 10b_newtype_reject.kel
error: compile: 4:25: refinement check `in_range` provably fails for newtype `Velocity` at compile time on argument 200
```

## Information-Flow Labels

Version 0.2.0 adds [information-flow labels][kel_guide_ifc].
A type can carry a label, written `T@Label`, that marks a value.
The operator `classify` attaches a label,
and `declassify` removes one. The language follows the label
and refuses, before the program runs, to let a labelled value
flow into a place that does not accept the label.
A reviewer can find every release of confidential data
by searching for `declassify`.

```keleusma
fn publish(x: Word) -> Word {
    x
}

fn main() -> Word {
    let secret = classify 42@Private;
    publish(declassify secret@Private)
}
```

```sh
$ keleusma run 11_info_flow.kel
42
```

Remove the `declassify`, and the leak is proved and rejected.

```keleusma
fn main() -> Word {
    let secret = classify 42@Private;
    publish(secret)
}
```

```sh
$ keleusma run 11b_info_flow_reject.kel
error: compile: 4:13: type error: argument to `publish` expects Word, got Word@Private
```

## Checked Arithmetic

Keleusma arithmetic on `Word` can be matched against
its overflow behavior. The construct binds the result through
an `ok` arm when it fits, and through `overflow` or `underflow` arms
when it does not, each exposing the high and low halves
of the wider intermediate result. This is the building block
for multi-word and big-number arithmetic.

```keleusma
fn add_checked(a: Word, b: Word) -> Word {
    a + b {
        ok(v) => v,
        overflow(_, l) => l,
        underflow(_, l) => l,
    }
}

fn main() -> Word {
    add_checked(20, 22)
}
```

```sh
$ keleusma run 12_checked.kel
42
```

## The Three Function Categories

Every Keleusma function is exactly one of three kinds,
fixed by the word that begins its declaration.
The [function categories chapter][kel_guide_categories]
develops this in full.

- `fn` is an atomic total function. It runs straight through
  and returns. Every example above is an `fn`.
- `yield` is a non-atomic total function. It may pause,
  hand a value to the host, and resume when the host resumes it,
  and it must eventually finish.
- `loop` is a productive divergent function. It never finishes
  and must hand a value to the host on every cycle.

A `yield` or `loop` program compiles and passes the verifier,
but it is meant to be driven by a host through a call-and-resume
protocol rather than run to a single value. On the 0.2.0
command-line tool, `keleusma run` drives `fn` programs.
The `yield` and `loop` programs are driven by an embedding host,
which the next section introduces. The tool can still confirm
that such a program lexes, type-checks, and passes the
bounded-execution verifier by compiling it to bytecode.

```keleusma
yield main(tick: Word) -> Word {
    let reply = yield tick;
    reply
}
```

```sh
$ keleusma compile 14_yield.kel -o out.bin
wrote out.bin (204 bytes)
```

## What the Verifier Guarantees

Before a program runs, the language proves a worst-case
[execution-time][ref_wcet] bound and a worst-case memory bound,
and it proves that every `fn` finishes.
The [budgets chapter][kel_guide_budgets] explains the two budgets.
A program whose bounds cannot be proved is rejected.
Recursion is one such construct, because it admits unbounded depth.

```keleusma
fn countdown(n: Word) -> Word {
    if n <= 0 { 0 } else { countdown(n - 1) }
}

fn main() -> Word {
    countdown(5)
}
```

```sh
$ keleusma run 13_recursion_reject.kel
error: verify: VerifyError("countdown: recursive call detected during WCMU topological sort")
```

The rejection is the safety property. A program the verifier accepts
is one whose time and memory bounds are proved,
not merely one whose bounds happen to exist.

## Signed Modules

Version 0.2.0 can sign compiled bytecode with Ed25519,
described in the [signed modules chapter][kel_guide_signing].
The signature proves origin and integrity for a module
delivered to a device in the field.
A program opts in with the `signed` modifier on its entry function.

```keleusma
signed fn main() -> Word {
    21 + 21
}
```

Generate a key pair, compile and sign, then run against the public key.

```sh
$ keleusma keygen --seed seed.bin --public pub.bin
wrote seed to seed.bin (32 bytes; keep secret)
wrote public key to pub.bin (32 bytes; distribute to verifiers)

$ keleusma compile signed_demo.kel --signing-key seed.bin -o signed_demo.bin
wrote signed_demo.bin (304 bytes)

$ keleusma run signed_demo.bin --verifying-key pub.bin
42
```

Run the signed bytecode without the key, and it refuses to load.

```sh
$ keleusma run signed_demo.bin
error: load_signed_bytes: LoadError("bytecode signature did not verify against any registered key")
```

## Embedding Keleusma in Rust

The command-line tool is one host. The runtime library is the product,
and the intended use is to embed it in a larger Rust program.
The [embedding guide][kel_embedding] documents the full surface.
A minimal host lexes, parses, and compiles a script,
constructs a virtual machine over an arena, and calls it.

`Cargo.toml`

```toml
[dependencies]
keleusma = "0.2"
```

`src/main.rs`

```rust
use keleusma::compiler::compile;
use keleusma::lexer::tokenize;
use keleusma::parser::parse;
use keleusma::vm::{Vm, VmState, DEFAULT_ARENA_CAPACITY};
use keleusma::{Arena, Value};

const SOURCE: &str = "fn main() -> Word { 21 + 21 }";

fn main() {
    let tokens = tokenize(SOURCE).expect("lex error");
    let program = parse(&tokens).expect("parse error");
    let module = compile(&program).expect("compile error");

    let arena = Arena::with_capacity(DEFAULT_ARENA_CAPACITY);
    let mut vm = Vm::new(module, &arena).expect("vm construction");

    match vm.call(&[]).expect("vm call") {
        VmState::Finished(Value::Int(n)) => println!("script returned {n}"),
        other => println!("unexpected VM state: {:?}", other),
    }
}
```

```sh
$ cargo run --quiet
script returned 42
```

`Vm::call` starts execution and returns a `VmState`.
An `fn` program returns `VmState::Finished`.
A `yield` program returns `VmState::Yielded`, and the host
calls `Vm::resume` with a value to continue.
A `loop` program yields on every cycle and resets at the end of its body,
where a host may hot-swap the module.
This call-and-resume protocol is how a host drives
the `yield` and `loop` programs from the previous sections.

## The Interactive Prompt

The tool also provides a read-evaluate-print loop
for trying expressions interactively.

```sh
$ keleusma repl
```

## Going Deeper

This tour covers enough to read and write Keleusma programs,
but it is deliberately shallow. The
[forty-chapter guide][kel_guide] is the place to go next.
Its learner track teaches the language from first principles,
and its embedding track addresses Rust hosts in depth.
The [instruction-set reference][kel_isa] documents the bytecode,
and the [example scripts][kel_examples] in the repository
are the seed material the guide builds on.

## Conclusion

Keleusma 0.2.0 trades the unbounded constructs of a general-purpose
language for a promise that no other small scripting language makes,
namely that every program it accepts is proved, before it runs,
to finish within bounded time and bounded memory.
Around that core it adds refinement types, information-flow labels,
and signed modules, and it is built to be embedded in a Rust host.
For a script author, the path forward is the learner track of the guide.
For a systems programmer, it is the embedding track.

## References

- [Keleusma, Crate on crates.io][kel_crate]
- [Keleusma, Command-Line Crate on crates.io][kel_cli_crate]
- [Keleusma, API Documentation on docs.rs][kel_docs_rs]
- [Keleusma, Embedding Guide][kel_embedding]
- [Keleusma, Example Scripts][kel_examples]
- [Keleusma, GitHub Repository][kel_github]
- [Keleusma, Guide][kel_guide]
- [Keleusma, Guide Chapter 1, What Keleusma Is][kel_guide_ch1]
- [Keleusma, Guide Chapter 2, Installing and Running][kel_guide_install]
- [Keleusma, Guide Chapter 15, The Three Function Categories][kel_guide_categories]
- [Keleusma, Guide Chapter 20, Time and Memory Budgets][kel_guide_budgets]
- [Keleusma, Guide Chapter 21, Generics and Traits][kel_guide_generics]
- [Keleusma, Guide Chapter 22, Newtypes and Refinement Types][kel_guide_refinement]
- [Keleusma, Guide Chapter 24, Information-Flow Labels][kel_guide_ifc]
- [Keleusma, Guide Chapter 26, Signed Modules and Hot Code Swap][kel_guide_signing]
- [Keleusma, Instruction Set Reference][kel_isa]
- [Reference, Refinement Type][ref_refinement_type]
- [Reference, Worst-Case Execution Time][ref_wcet]
- [Related Post, Getting Started with Keleusma 0.1.1][related_post_keleusma_011]
- [Related Post, A Verifiable Control Kernel in Keleusma][related_post_control_kernel]

[kel_crate]: https://crates.io/crates/keleusma
[kel_cli_crate]: https://crates.io/crates/keleusma-cli
[kel_docs_rs]: https://docs.rs/keleusma
[kel_embedding]: https://github.com/sgeos/keleusma/blob/main/docs/guide/EMBEDDING.md
[kel_examples]: https://github.com/sgeos/keleusma/tree/main/examples/scripts
[kel_github]: https://github.com/sgeos/keleusma
[kel_guide]: https://github.com/sgeos/keleusma/blob/main/docs/guide/README.md
[kel_guide_ch1]: https://github.com/sgeos/keleusma/blob/main/docs/guide/01_what_keleusma_is.md
[kel_guide_install]: https://github.com/sgeos/keleusma/blob/main/docs/guide/02_installing_and_running.md
[kel_guide_categories]: https://github.com/sgeos/keleusma/blob/main/docs/guide/15_three_function_categories.md
[kel_guide_budgets]: https://github.com/sgeos/keleusma/blob/main/docs/guide/20_time_and_memory_budgets.md
[kel_guide_generics]: https://github.com/sgeos/keleusma/blob/main/docs/guide/21_generics_and_traits.md
[kel_guide_refinement]: https://github.com/sgeos/keleusma/blob/main/docs/guide/22_newtypes_and_refinement.md
[kel_guide_ifc]: https://github.com/sgeos/keleusma/blob/main/docs/guide/24_information_flow_labels.md
[kel_guide_signing]: https://github.com/sgeos/keleusma/blob/main/docs/guide/26_signed_modules_and_hot_swap.md
[kel_isa]: https://github.com/sgeos/keleusma/blob/main/docs/spec/INSTRUCTION_SET.md
[ref_refinement_type]: https://en.wikipedia.org/wiki/Refinement_type
[ref_wcet]: https://en.wikipedia.org/wiki/Worst-case_execution_time
[related_post_keleusma_011]: {% post_url 2026-03-14-keleusma_getting_started %}
[related_post_control_kernel]: {% post_url 2026-05-27-verifiable_control_kernel_in_keleusma %}
