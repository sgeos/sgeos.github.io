---
layout: post
mathjax: false
comments: true
title:  "Getting Started with Keleusma 0.1.1"
date:   2026-03-14 10:31:00 +0000
categories: rust embedded programming
series: keleusma_getting_started
series_title: Keleusma Getting Started
series_index: 1
---
<!-- A107 -->
<script>console.log("A107");</script>

[Keleusma][ref_keleusma_github] is a Total Functional Stream Processor
that compiles to bytecode and runs on a stack-based virtual machine.
It targets `no_std + alloc` embedded environments
and provides definitive Worst-Case Execution Time
and Worst-Case Memory Usage guarantees through static verification.
The language enforces five guarantees at compile time.
Every function terminates.
Every stream produces output on every tick.
Every execution path has a bounded step count.
Every execution path has a bounded memory footprint.
Running code can be replaced at designated boundaries
without stopping the virtual machine.

The name derives from the Greek word *keleusma*,
meaning a command or rhythmic signal.
Ancient rowing masters used the keleusma
to synchronize oarsmen on warships.
The language applies the same principle to computation.
Scripts execute in bounded, predictable cycles
synchronized to a host-driven clock.

Keleusma targets applications
where deterministic execution is a hard requirement.
Audio engines must produce samples every tick
without buffer underruns.
Game scripting systems must complete logic updates
within a fixed frame budget.
Safety-critical embedded systems must guarantee
worst-case timing for certification.
The language addresses these domains
by making unbounded computation inexpressible
rather than merely discouraged.

This article provides a practical introduction
to the Keleusma language and toolchain.
It covers installation, the type system,
the three function kinds that encode the guarantee taxonomy,
pattern matching, the pipeline operator,
built-in functions, the interactive read-evaluate-print loop,
embedding the virtual machine in a Rust host application,
hot code swapping, worst-case analysis,
and bytecode compilation.
Readers familiar with
[no_std Rust programming][related_post_no_std_rust]
will find the embedding interface straightforward.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-03-14 10:31:00 +0000

# Keleusma Version
$ keleusma --version
keleusma 0.1.1

# Rust Version
$ cargo --version
cargo 1.88.0 (2025-06-25)

$ rustc --version
rustc 1.88.0 (2025-06-25)
```

## Installation

Keleusma is available on [crates.io][ref_keleusma_crate]
and as source on [GitHub][ref_keleusma_github].
The command-line interface is distributed
as a separate workspace crate called `keleusma-cli`.

### Install from Source

```sh
git clone https://github.com/sgeos/keleusma
cd keleusma
cargo install --path keleusma-cli --bin keleusma
```

### Verify Installation

```sh
$ keleusma --version
keleusma 0.1.1

$ keleusma --help
keleusma: command-line frontend for the Keleusma scripting language

Usage:
  keleusma <subcommand> [options]
  keleusma <file>.kel               (shorthand for `run`)

Subcommands:
  run <file>                        Compile and execute a script
  compile <file> [-o <output>]      Compile to bytecode
  repl                              Start interactive REPL
  help, --help, -h                  Show this help
  version, --version, -V            Show version

Examples:
  keleusma run hello.kel
  keleusma hello.kel
  keleusma compile hello.kel -o hello.kel.bin
  keleusma repl
```

## First Program

Create a file called `hello.kel` with the following contents.

```keleusma
fn square(x: i64) -> i64 { x * x }

fn main() -> i64 {
    let a: i64 = 3;
    let b: i64 = 4;
    let sum_of_squares = square(a) + square(b);
    sum_of_squares - 1
}
```

Run the program.

```sh
$ keleusma run hello.kel
24
```

The `main` function is the entry point.
It computes `3^2 + 4^2 - 1 = 9 + 16 - 1 = 24`.
The program compiles to bytecode,
passes through the structural verifier,
and executes on the stack-based virtual machine.
The verifier confirms that every execution path terminates
and that memory usage is bounded
before the virtual machine begins execution.

## Language Basics

### Primitive Types

Keleusma provides five primitive types.

| Type | Description |
|------|-------------|
| `i64` | 64-bit signed integer |
| `f64` | 64-bit floating-point number |
| `bool` | Boolean value |
| `String` | UTF-8 string |
| `()` | Unit type |

### Variables

All local bindings are immutable.
Rebinding a name shadows the previous binding
without mutating the original value.

```keleusma
let x: i64 = 42;
let y = 3.14;
let z = x + 1;
```

Type annotations are optional
when the type can be inferred from context.

### Operators

Keleusma supports standard arithmetic, comparison, and logical operators.

**Arithmetic:** `+`, `-`, `*`, `/`, `%`

**Comparison:** `==`, `!=`, `<`, `>`, `<=`, `>=`

**Logical:** `and`, `or`, `not`

**Type cast:** `as`

**Pipeline:** `|>`

Logical operators use short-circuit evaluation.
The `as` operator performs explicit type conversion
between numeric types.

```keleusma
let n: i64 = 42;
let f: f64 = n as f64;
```

### Conditionals

```keleusma
fn abs_value(x: i64) -> i64 {
    if x < 0 { 0 - x }
    else { x }
}
```

Conditionals are expressions and evaluate to a value.
Both branches must produce the same type.

### Bounded Iteration

The `for` loop iterates over ranges or arrays.
All `for` loops are bounded by construction
because ranges have a known size
and arrays have a known length.

```keleusma
fn main() -> i64 {
    let xs = [10, 20, 30, 40];

    for x in xs {
        let _doubled = x * 2;
    }

    for i in 0..4 {
        let _squared = i * i;
    }

    xs[3]
}
```

The range `0..4` produces values 0, 1, 2, and 3.
The upper bound is exclusive.
The `break` keyword exits a `for` loop early.

## Three Function Kinds

The central design of Keleusma organizes all functions
into three categories
that collectively guarantee bounded execution.
Each category has a dedicated keyword
and a distinct set of obligations.

### Atomic Total Functions

The `fn` keyword declares an atomic total function.
An atomic total function must terminate on every input.
It may not yield, may not recurse,
and must return a value.

```keleusma
fn clamp(val: i64, lo: i64, hi: i64) -> i64 {
    if val < lo { lo }
    else if val > hi { hi }
    else { val }
}
```

The verifier confirms termination statically.
Unbounded recursion and infinite loops
are syntactically impossible in `fn` bodies.

### Non-Atomic Total Functions

The `yield` keyword declares a non-atomic total function.
A non-atomic total function may yield control
back to the host one or more times
but must eventually return a final value.

```keleusma
yield prompt(question: String) -> String {
    let answer = yield question;
    answer
}
```

When the function executes `yield question`,
it suspends and sends `question` to the host.
The host provides a response,
which becomes the value of the `yield` expression.
The function must eventually reach a `return` point.

### Productive Divergent Functions

The `loop` keyword declares a productive divergent function.
A productive divergent function never returns.
It runs indefinitely, processing a stream of inputs
and producing a stream of outputs.
It must yield on every iteration.
Only one `loop` function may exist per script.

```keleusma
loop main(input: i64) -> i64 {
    let result = input * 2;
    let input = yield result;
    input
}
```

The verifier confirms that every control path
from the stream entry point to the reset boundary
contains at least one `yield`.
This guarantees [productivity][ref_productivity].
The host drives execution by providing inputs
and consuming outputs at each yield point.

### Why Three Kinds

The three-kind taxonomy ensures
that the verifier can assign a finite cost
to every execution path.
Atomic total functions have a fixed step count.
Non-atomic total functions have a fixed step count per segment.
Productive divergent functions have a fixed step count per tick.
Together, these properties enable
static computation of worst-case execution time
for any single tick of the system.

## Composite Types

### Structs

```keleusma
struct Point { x: i64, y: i64 }

fn manhattan_norm(p: Point) -> i64 {
    p.x + p.y
}

fn main() -> i64 {
    let origin_offset = Point { x: 3, y: 4 };
    manhattan_norm(origin_offset)
}
```

Structs group named fields into a single value.
Field access uses dot notation.

### Enums

```keleusma
enum Shape {
    Circle(i64),
    Rectangle(i64, i64),
    Square(i64),
}

fn area_estimate(s: Shape) -> i64 {
    match s {
        Shape::Circle(r) => 3 * r * r,
        Shape::Rectangle(w, h) => w * h,
        Shape::Square(side) => side * side,
    }
}

fn main() -> i64 {
    let shape = Shape::Rectangle(20, 5);
    area_estimate(shape)
}
```

Enums define a closed set of variants.
Each variant may carry associated data.
The `match` expression destructures enum values.
Match expressions must be exhaustive
or include a wildcard `_` arm.

### Tuples and Arrays

```keleusma
let pair: (i64, i64) = (1, 2);
let xs = [10, 20, 30, 40];
let repeated = [0.0; 8];
```

Tuples group heterogeneous values by position.
Arrays hold homogeneous values of fixed length.
The `[value; count]` syntax creates an array
filled with `count` copies of `value`.

### Option Type

```keleusma
let some_value: Option<i64> = Option::Some(42);
let no_value: Option<i64> = Option::None;
```

The `Option` type represents a value that may or may not exist.

## Pipeline Operator

The pipeline operator `|>` threads the result
of the left expression
as the first argument to the right function call.

```keleusma
fn double(x: i64) -> i64 { x + x }
fn add(x: i64, y: i64) -> i64 { x + y }
fn square(x: i64) -> i64 { x * x }

fn main() -> i64 {
    6 |> double() |> add(1) |> square()
}
```

This program produces 169.
The value 6 flows through `double` to produce 12,
then through `add(_, 1)` to produce 13,
then through `square` to produce 169.

For functions where the piped value
should not be the first argument,
use the underscore placeholder.

```keleusma
value |> insert(collection, _)
```

The underscore marks
where the piped value should be inserted.

## Multiheaded Functions and Guards

A single function name may have multiple heads,
each with its own parameter pattern.
The runtime tries the heads in source order
and dispatches to the first one whose pattern matches.

```keleusma
fn classify(0)            -> i64 { 0 }
fn classify(1)            -> i64 { 1 }
fn classify(n: i64)       -> i64 { n + 10 }

fn main() -> i64 {
    let a = classify(0);
    let b = classify(1);
    let c = classify(11);
    let d = classify(7);
    a + b + c + d - 28
}
```

This program produces 11.
The first head matches only the literal 0.
The second head matches only the literal 1.
The third head matches any other integer.

Guard clauses refine pattern matching
with additional conditions.

```keleusma
fn sign(x: i64) -> String when x > 0 { "positive" }
fn sign(x: i64) -> String when x < 0 { "negative" }
fn sign(x: i64) -> String { "zero" }
```

The `when` clause is evaluated
after the parameter pattern matches.
If the guard fails, dispatch continues
to the next head.

## Generics and Traits

Keleusma supports generic type parameters
and trait-based polymorphism.
Generics are monomorphized at compile time.

```keleusma
fn id<T>(x: T) -> T { x }
```

Traits declare a set of function signatures
that a type must implement.

```keleusma
trait Doubler {
    fn double(x: i64) -> i64;
}

impl Doubler for i64 {
    fn double(x: i64) -> i64 { x + x }
}

fn main() -> i64 {
    let n: i64 = 42;
    n.double()
}
```

This program produces 84.
Method dispatch uses dot notation.
The compiler resolves the concrete implementation
at compile time through monomorphization.

Trait bounds constrain type parameters.

```keleusma
fn use_doubler<T: Doubler>(x: T) -> i64 {
    x.double()
}
```

## Strings and Interpolation

Keleusma distinguishes two string categories.
Static strings are stored in the read-only data segment
and can flow anywhere in the program.
Dynamic strings are arena-allocated
and cannot cross yield boundaries.

String literals produce static strings.

```keleusma
let msg: String = "hello";
```

F-string interpolation provides formatted string construction.
The `f"..."` syntax desugars at lex time
into chains of `concat` and `to_string` calls.
Scripts that use f-strings must declare
their dependency on these native functions.

```keleusma
use to_string
use concat

fn add(a: i64, b: i64) -> i64 {
    a + b
}

fn main() -> String {
    let name = "Keleusma";
    let a: i64 = 7;
    let b: i64 = 2;
    f"hello, {name}! {a} plus {b} is {add(a, b)}"
}
```

```sh
$ keleusma run fstring.kel
hello, Keleusma! 7 plus 2 is 9
```

The `use` declarations inform the compiler
that these native functions are provided by the host.

## Built-in Functions

The CLI runner registers two sets
of native functions automatically.

### Utility Functions

| Function | Signature | Description |
|----------|-----------|-------------|
| `to_string` | `(i64 or f64) -> String` | Convert number to string |
| `length` | `(String or Array) -> i64` | Get length |
| `concat` | `(String, String) -> String` | Concatenate strings |
| `slice` | `(String, i64, i64) -> String` | Extract substring |
| `println` | `(String) -> ()` | Print to standard output |

### Math Functions

| Function | Signature | Description |
|----------|-----------|-------------|
| `math::sin` | `(f64) -> f64` | Sine |
| `math::cos` | `(f64) -> f64` | Cosine |
| `math::pow` | `(f64, f64) -> f64` | Exponentiation |
| `math::abs` | `(f64) -> f64` | Absolute value |
| `math::min` | `(f64, f64) -> f64` | Minimum |
| `math::max` | `(f64, f64) -> f64` | Maximum |
| `math::clamp` | `(f64, f64, f64) -> f64` | Clamp to range |
| `math::lerp` | `(f64, f64, f64) -> f64` | Linear interpolation |

### Audio Functions

| Function | Signature | Description |
|----------|-----------|-------------|
| `audio::midi_to_freq` | `(i64) -> f64` | MIDI note to frequency in Hz |
| `audio::freq_to_midi` | `(f64) -> i64` | Frequency to nearest MIDI note |
| `audio::db_to_linear` | `(f64) -> f64` | Decibels to linear amplitude |
| `audio::linear_to_db` | `(f64) -> f64` | Linear amplitude to decibels |

All math and audio functions accept both `i64` and `f64` arguments.
Integer arguments are widened to floating-point automatically.

## The REPL

The interactive read-evaluate-print loop
allows experimentation without creating script files.

```sh
$ keleusma repl
```

```
> 1 + 2
3
> fn double(x: i64) -> i64 { x + x }
defined: double
> double(21)
42
> :help
:help    Show this help
:quit    Exit the REPL
:reset   Clear all definitions
:show    Show defined functions
> :quit
```

The REPL supports function definitions, expressions,
and colon-prefixed meta-commands.
Definitions persist across evaluations
until `:reset` is issued.

## Embedding in Rust

Keleusma is designed to be embedded in Rust host applications.
The library crate provides the full compilation pipeline
and virtual machine as a library API.

### Minimal Example

```rust
use keleusma::compiler::compile;
use keleusma::lexer::tokenize;
use keleusma::parser::parse;
use keleusma::vm::{DEFAULT_ARENA_CAPACITY, Vm, VmState};
use keleusma::{Arena, Value};

fn main() {
    let source = r#"
        fn double(x: i64) -> i64 { x * x }
        fn main(n: i64) -> i64 { n |> double() }
    "#;

    let tokens = tokenize(source).expect("lex");
    let program = parse(&tokens).expect("parse");
    let module = compile(&program).expect("compile");
    let arena = Arena::with_capacity(DEFAULT_ARENA_CAPACITY);
    let mut vm = Vm::new(module, &arena).expect("verify");

    match vm.call(&[Value::Int(21)]).unwrap() {
        VmState::Finished(Value::Int(n)) => println!("{}", n),
        _ => unreachable!(),
    }
}
```

The host owns the [arena allocator][ref_arena_allocator].
The virtual machine borrows the arena
for its operand stack, call frames, and dynamic string storage.
The default arena capacity is 64 kilobytes.

### Registering Native Functions

Native functions allow scripts to call into host code.
The ergonomic typed interface is the recommended approach.

```rust
vm.register_fn("add", |a: i64, b: i64| -> i64 { a + b });
vm.register_fn("sin", |x: f64| -> f64 { libm::sin(x) });
```

For functions that may fail, use the fallible interface.

```rust
vm.register_fn_fallible("get_setting", |key: String| -> Result<String, VmError> {
    fetch(&key).map_err(|e| VmError::NativeError(format!("{}", e)))
});
```

Custom struct types can cross the host-guest boundary
using the `KeleusmaType` derive macro.

```rust
use keleusma::KeleusmaType;

#[derive(KeleusmaType, Debug, Clone)]
struct Point { x: f64, y: f64 }

vm.register_fn("midpoint", |a: Point, b: Point| -> Point {
    Point { x: (a.x + b.x) / 2.0, y: (a.y + b.y) / 2.0 }
});
```

### VM Lifecycle

The virtual machine transitions between states
as it executes scripts.

```rust
let state = vm.call(&[Value::Int(input)])?;

loop {
    match state {
        VmState::Yielded(output) => {
            let reply = host_process(output);
            state = vm.resume(reply)?;
        }
        VmState::Reset => {
            // Hot swap opportunity
            state = vm.resume(next_input)?;
        }
        VmState::Finished(value) => {
            break;
        }
    }
}
```

A `Yielded` state indicates
that the script has produced output
and awaits the next input.
A `Reset` state indicates a phase boundary
where hot code swapping is permitted.
A `Finished` state indicates
that the script has returned a final value.

## Hot Code Swapping

Keleusma supports replacing a running script
at designated reset boundaries
without stopping the virtual machine.
The data segment persists across the swap.

```rust
match vm.resume(input)? {
    VmState::Reset => {
        let new_module = recompile_or_load()?;
        let initial_data = vec![Value::Int(0); slot_count];
        vm.replace_module(new_module, initial_data)?;
        state = vm.call(&[fresh_input])?;
    }
    _ => { /* continue normal execution */ }
}
```

Hot code swapping is useful for live development workflows.
Audio engines can replace synthesis scripts
without interrupting playback.
Game scripting systems can reload behavior scripts
without restarting the game loop.

## Worst-Case Analysis

The structural verifier computes
worst-case execution time and worst-case memory usage
for every execution path before the virtual machine starts.
If the verifier cannot prove bounded execution,
the program is rejected.

### Cost Model

Each bytecode instruction has an assigned integer cost.
The verifier sums costs along the worst-case path
through each function and each stream iteration.

Common instruction costs include the following.

| Cost | Instructions |
|------|-------------|
| 1 | Constants, local variable access, stack operations, control flow delimiters |
| 2 | Arithmetic, comparisons, indexing, type casts, return |
| 3 | Division, modulo, field access by name, type tests |
| 5 | Struct and enum construction, array and tuple allocation |
| 10 | Function calls, native function calls |

### Arena Sizing

The host must provide an arena
large enough for the worst-case memory usage.
Three approaches are available.

**Default capacity** is 64 kilobytes.

```rust
let arena = Arena::with_capacity(DEFAULT_ARENA_CAPACITY);
```

**Automatic computation** sizes the arena
to the verified worst-case memory usage.

```rust
let cap = keleusma::vm::auto_arena_capacity_for(&module, &[])?;
let arena = Arena::with_capacity(cap);
```

**Static buffer** is suitable for embedded targets
without a heap allocator.

```rust
static mut ARENA_BUFFER: [u8; 16 * 1024] = [0; 16 * 1024];
let arena = unsafe {
    Arena::from_static_buffer(core::ptr::addr_of_mut!(ARENA_BUFFER))
};
```

## Compiling to Bytecode

Scripts can be compiled to bytecode files
for deployment without the source.

```sh
$ keleusma compile hello.kel -o hello.kel.bin
```

The host application loads precompiled bytecode
using zero-copy [deserialization][ref_zero_copy_serialization].

```rust
let bytes = std::fs::read("hello.kel.bin")?;
let mut vm = Vm::load_bytes(&bytes, &arena)?;
```

Precompiled bytecode is useful
in embedded deployments where source compilation
at runtime is undesirable or impossible.
The bytecode format uses [rkyv][ref_rkyv]
for zero-copy deserialization.

## Conclusion

Keleusma provides a scripting language
with static guarantees about termination,
memory usage, and execution time.
The three-function taxonomy of atomic total,
non-atomic total, and productive divergent functions
ensures that the verifier can assign
bounded costs to every execution path.
The `no_std + alloc` design,
arena-based memory management,
and precompiled bytecode support
make the virtual machine suitable
for resource-constrained embedded targets.

The language repository
contains additional [example scripts][ref_keleusma_examples]
demonstrating language features
and [Rust embedding examples][ref_keleusma_rust_examples]
demonstrating host integration patterns
including worst-case memory attestation,
yield-based coroutines,
string handling,
generics,
zero-copy bytecode loading,
and a full [SDL3][ref_sdl3] audio piano roll
with hot code swapping.

The [documentation directory][ref_keleusma_docs]
contains a complete language grammar specification,
instruction set reference,
type system documentation,
execution model description,
and a survey of related work
in synchronous reactive languages,
coalgebraic stream processing,
and worst-case execution time analysis.

## Future Reading

- [Keleusma, Documentation Directory][future_keleusma_docs]
- [Keleusma, Language Design][future_keleusma_language_design]
- [Keleusma, Grammar Specification][future_keleusma_grammar]
- [Keleusma, Related Work Survey][future_keleusma_related_work]
- [Rust, Embedded Rust Book][future_rust_embedded]
- [Turner, Total Functional Programming (2004)][future_turner]

## References

- [Reference, Arena Allocator][ref_arena_allocator]
- [Reference, Bytecode][ref_bytecode]
- [Reference, Coroutine][ref_coroutine]
- [Reference, Keleusma on crates.io][ref_keleusma_crate]
- [Reference, Keleusma on GitHub][ref_keleusma_github]
- [Reference, Keleusma Documentation][ref_keleusma_docs]
- [Reference, Keleusma Example Scripts][ref_keleusma_examples]
- [Reference, Keleusma Rust Examples][ref_keleusma_rust_examples]
- [Reference, Pattern Matching][ref_pattern_matching]
- [Reference, Productivity][ref_productivity]
- [Reference, rkyv Zero-Copy Serialization][ref_rkyv]
- [Reference, SDL3][ref_sdl3]
- [Reference, Stack Machine][ref_stack_machine]
- [Reference, Stream Processing][ref_stream_processing]
- [Reference, Total Functional Programming][ref_total_functional_programming]
- [Reference, Worst-Case Execution Time][ref_wcet]
- [Reference, Zero-Copy Serialization][ref_zero_copy_serialization]
- [Related Post, Getting Started with no_std Rust Programming][related_post_no_std_rust]
- [Research, Turner (2004), Total Functional Programming][research_turner]
- [Research, Rutten (2000), Universal Coalgebra][research_rutten]
- [Research, Wilhelm et al. (2008), WCET Survey][research_wilhelm]

[future_keleusma_docs]: https://github.com/sgeos/keleusma/tree/master/docs
[future_keleusma_grammar]: https://github.com/sgeos/keleusma/blob/master/docs/design/GRAMMAR.md
[future_keleusma_language_design]: https://github.com/sgeos/keleusma/blob/master/docs/architecture/LANGUAGE_DESIGN.md
[future_keleusma_related_work]: https://github.com/sgeos/keleusma/blob/master/docs/reference/RELATED_WORK.md
[future_rust_embedded]: https://docs.rust-embedded.org/book/
[future_turner]: https://doi.org/10.3217/jucs-010-07-0751
[ref_arena_allocator]: https://en.wikipedia.org/wiki/Region-based_memory_management
[ref_bytecode]: https://en.wikipedia.org/wiki/Bytecode
[ref_coroutine]: https://en.wikipedia.org/wiki/Coroutine
[ref_keleusma_crate]: https://crates.io/crates/keleusma
[ref_keleusma_docs]: https://github.com/sgeos/keleusma/tree/master/docs
[ref_keleusma_examples]: https://github.com/sgeos/keleusma/tree/master/examples/scripts
[ref_keleusma_github]: https://github.com/sgeos/keleusma
[ref_keleusma_rust_examples]: https://github.com/sgeos/keleusma/tree/master/examples
[ref_pattern_matching]: https://en.wikipedia.org/wiki/Pattern_matching
[ref_productivity]: https://en.wikipedia.org/wiki/Productivity_(computer_science)
[ref_rkyv]: https://crates.io/crates/rkyv

[ref_sdl3]: https://wiki.libsdl.org/SDL3/FrontPage

[ref_stack_machine]: https://en.wikipedia.org/wiki/Stack_machine
[ref_stream_processing]: https://en.wikipedia.org/wiki/Stream_processing
[ref_total_functional_programming]: https://en.wikipedia.org/wiki/Total_functional_programming

[ref_wcet]: https://en.wikipedia.org/wiki/Worst-case_execution_time
[ref_zero_copy_serialization]: https://en.wikipedia.org/wiki/Zero-copy
[related_post_no_std_rust]: {% post_url 2026-01-16-no_std_rust_getting_started %}
[research_rutten]: https://doi.org/10.1016/S0304-3975(00)00056-6
[research_turner]: https://doi.org/10.3217/jucs-010-07-0751
[research_wilhelm]: https://doi.org/10.1145/1347375.1347389
