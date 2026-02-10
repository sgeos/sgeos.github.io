---
layout: post
mathjax: false
comments: true
title: "Safe Embedded Functional Control DSL"
date: 2026-02-13 00:00:00 +0000
categories: dsl embedded development safety
---

<!-- A83 -->

Embeddable scripting languages allow applications
to expose programmable behavior without recompiling the host.
Lua powers game scripting across the industry.
Rhai provides a small, safe scripting engine for Rust applications.
mruby brings Ruby syntax to embedded contexts.
These languages work well for general-purpose scripting,
but none of them were designed from the ground up
for mission-critical applications
where correctness, determinism, and formal verifiability are requirements.

Mission-critical systems such as robotics controllers,
safety-instrumented industrial processes,
and real-time game engines
need scripting that is not merely convenient
but provably safe.
The scripting layer must be deterministic,
must bound its own resource usage,
must make all side effects explicit,
and must support hot code updates
without risking system integrity.

This article proposes a safe embedded functional control
Domain-Specific Language (DSL)
designed to fill this gap.
The language draws inspiration from Elixir
for its syntax and concurrency philosophy,
targets seamless embedding in Rust
in the style of Rhai,
and prioritizes formal analyzability
so that programs written in it
can be subjected to the proof techniques
discussed in
{% post_url 2026-02-10-writing-proofs %}.
This is not a formal specification.
It is an informal proposal
for a bytecode-VM-based, hot-swappable scripting language
engineered for mission-critical work.

The proposed DSL assumes a trusted host application
and an untrusted or semi-trusted script author.
The VM, runtime, and host-provided native functions
form the trusted computing base.
The language and VM aim to prevent script-level code
from corrupting host memory,
accessing unauthorized resources,
or violating determinism guarantees.
The design does not attempt to defend
against malicious or incorrectly implemented host bindings.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-13 00:00:00 +0000

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
      Memory: 64 GB
```

## Why Existing Embeddable Languages Fall Short

Several embeddable scripting languages are widely used today.
Each makes tradeoffs that limit its suitability
for mission-critical applications.

**Lua** is the most widely deployed embeddable scripting language.
It is small, fast, and well understood.
However, Lua is dynamically typed,
making static analysis difficult or impossible.
Variables are global by default.
Garbage collection introduces non-deterministic pause times
that are problematic for real-time systems.
Luau, the Roblox derivative,
adds gradual typing and improved sandboxing,
but the fundamental dynamic semantics remain.

**Rhai** is an embedded scripting language for Rust
that is small, fast, and easy to integrate.
It supports dynamic typing with some runtime checks,
sandboxed execution, and a familiar syntax.
Rhai is well suited for configuration and light scripting,
but it does not provide static type checking,
formal effect tracking,
or deterministic resource bounds.
It was not designed for contexts
where formal verification is required.

**mruby** is a lightweight implementation of the Ruby language
designed for embedding.
It inherits Ruby's expressiveness
but also its complexity.
mruby lacks concurrency primitives,
does not support file loading at runtime,
and has significant limitations
in numeric handling and argument destructuring.
Attempting to constrain a full-featured language for embedding
introduces limitations
that a purpose-built DSL can avoid by design.

The common thread is that these languages
were designed for flexibility and convenience.
A mission-critical embeddable DSL
must be designed for safety and verifiability first,
accepting reduced expressiveness as the cost.

## Design Inspiration

The proposed language draws on
several established language designs.

**Elixir and the BEAM VM**
provide the primary syntactic and philosophical inspiration.
Elixir's pattern matching, pipeline operator,
immutable data, and "let it crash" supervision philosophy
have proven effective in telecommunications and financial systems
where uptime and fault tolerance are critical.
The Erlang/OTP (Open Telecom Platform) heritage
demonstrates that functional programming,
process isolation,
and hot code reloading
can serve mission-critical production systems.
The proposed DSL borrows Elixir's syntax
for pattern matching, pipelines, and multi-headed functions,
while replacing the dynamic type system
with static typing.

**Gleam** demonstrates
that static types can be added to BEAM-style concurrency
without sacrificing the benefits of the runtime.
Gleam's type-safe implementation of OTP patterns
shows that compile-time guarantees
and actor-model concurrency are compatible.

**Roc** introduces the platform architecture,
where all I/O primitives are provided
by a single, controlled interface.
The standard library provides no I/O operations.
This design enables safe execution of untrusted code
by constraining all side effects
through the host platform.
The proposed DSL adopts a similar model:
the host application controls all resource access.

**Koka** pioneers practical algebraic effect systems
where all side effects are tracked in the type signature.
Effect handlers generalize exception handling,
state management, iterators, and async patterns
into a single compositional abstraction.
The proposed DSL requires explicit effect annotations
for all host-bound operations,
enabling the compiler to distinguish
pure computation from effectful interaction.

## Design Goals

The language has seven high-level design goals.
Each goal reflects a constraint imposed
by mission-critical embedded environments.

**Maximum Safety.**
The language must be memory-safe with sandboxed execution.
There must be no undefined behavior and no hidden side effects.
All programs must execute deterministically.

**Formal Analyzability.**
The language must have fully defined operational semantics.
Evaluation must be deterministic and pure functional where possible.
State and effects must be explicit
to enable formal proofs, model checking,
and worst-case execution time analysis.
Programs should be amenable to verification
using techniques such as Hoare logic,
loop invariant analysis,
and bounded model checking.

**Embeddability.**
The language must integrate seamlessly into Rust
and other host systems.
The host manages concurrency and I/O.
Language execution is isolated.
The boundary between script logic and host resources
must be well defined
and enforced through a capability-based security model.

**Hot-Updatable Logic.**
Code updates must occur only at explicit tick or epoch boundaries.
Safe rollback to the prior version must be supported.
There must be no live stack rewriting.
Updates must be atomic and deterministic,
following the model established by Erlang/OTP
where explicit state migration callbacks
manage transitions between code versions.

**Functional, Lightweight Syntax.**
The language must support pattern matching,
pipelines with placeholder support,
multi-headed functions,
and algebraic data types.
The syntax should be familiar
to developers with Elixir or ML-family experience.

**Concurrency-Safe Design.**
Script-visible state must be immutable.
Each VM execution must be isolated.
Multiple scripts must be safe to run concurrently without locking.

**Bounded Resource Usage.**
Scripts must compile to bytecode for a stack-based VM.
Resource usage including stack depth, heap allocation,
and instruction counts must be deterministic and bounded.
The host must be able to enforce resource limits
and terminate scripts that exceed them.
The language design enables termination
and resource bounds to be established statically
or enforced at runtime.
Safety-critical configurations may restrict unbounded recursion
or require statically provable execution limits.

### Non-Goals

The language intentionally excludes certain capabilities.

- Not a general-purpose programming language.
- Not a replacement for Rust or C++.
- Not a real-time scheduler or concurrency runtime.
- Not an actor or message-passing system.

These boundaries are deliberate.
General-purpose computation, concurrency scheduling,
and message passing are host responsibilities.
The DSL provides a safe, verifiable control layer.

## Language Features

### Functional Programming

Expressions are pure by default.
Side effects must be explicit via host-bound functions
annotated with effect types.
The language supports immutability and total functions.
Partial functions must be explicitly marked
and are discouraged in mission-critical code paths.

### Pipelines

Pipelines use the `|>` operator to chain transformations,
following the convention established by Elixir.
The placeholder `_` indicates where the piped value is inserted.

```text
value |> f |> g(1)
value |> f |> g(1, _)
value |> f |> g(_, _)
value |> f |> g(_, _ / 2)
```

Zero or more placeholders are permitted per call.
If a placeholder is omitted, the pipeline targets the first parameter.
If more than one placeholder is used,
the piped value is substituted at each placeholder position.
The compiler rewrites pipelines for efficiency.
Multiple placeholders are syntactic sugar
and are desugared into explicit temporary bindings
prior to bytecode generation.
Resource usage and execution cost
are defined and analyzed at the bytecode level,
not the surface syntax level.

### Pattern Matching

Pattern matching must be exhaustive.
The compiler rejects non-exhaustive matches at compile time.
Matching is supported on algebraic data types, tuples, and literals.

### Multi-Headed Functions

Function bodies are selected
based on pattern matching of arguments,
following the Elixir convention.

```text
fn factorial(0) = 1
fn factorial(n) when n > 0 = n * factorial(n - 1)
```

Guard clauses (`when`) restrict which head is selected.

### Algebraic Data Types

The language supports sum types for variant types.
Tagged values with payloads are supported.
Exhaustive handling in match statements
is required for all code.

```text
type Result(ok, err) =
    | Ok(ok)
    | Err(err)

type SensorEvent =
    | Temperature(f32)
    | Pressure(f32)
    | Heartbeat
```

### Type System

The language is strongly and statically typed
with Hindley-Milner style type inference.
Explicit effect annotations are required
for all host-bound operations.
The type system tracks which effects a function may perform,
enabling the compiler to verify
that pure functions remain pure
and that effectful functions declare their effects.

```text
fn pure_compute(x: f32) -> f32 =
    x * 2.0 + 1.0

fn alert(msg: String) -> ! io =
    host_log(msg)
```

The `! io` annotation indicates
that the function performs an I/O effect.

Numeric semantics, including floating-point behavior,
must be explicitly specified by the language and runtime.
Safety-critical deployments may restrict
or replace floating-point arithmetic
with deterministic fixed-point representations.

### Hot Update Mechanism

Scripts can be replaced only at defined tick or epoch boundaries.
The old version remains available for rollback.
The VM maintains function tables with version indirection.
State migration between versions
is handled by an explicit `code_change` callback,
following the Erlang/OTP model.

```text
fn code_change(old_version, state) =
    state |> migrate_state(old_version, _)
```

### Concurrency Semantics

Script-visible state is immutable.
Each execution has an isolated stack and heap.
The language provides no internal concurrency primitives.
The host handles scheduling and inter-script communication.
This design follows the principle
that concurrency is a host concern,
not a script concern,
and eliminates data races by construction.

## Runtime and VM Architecture

### VM Design

The VM is stack-based, deterministic, and analyzable.
Scripts are compiled to bytecode.
Each invocation has a separate execution frame
with its own stack and heap allocation.
An optional trace mode records execution paths
for debugging and formal verification.

The bytecode instruction set is kept small
to simplify formal analysis.
All instructions have bounded execution time,
enabling worst-case execution time analysis
at the bytecode level.

The bytecode operational semantics
are the normative definition of program behavior.
All surface syntax,
including pipelines, pattern matching,
and multi-headed functions,
is desugared into the bytecode instruction set
prior to execution and analysis.

### Memory Model

Stack and heap allocation are controlled and bounded.
The host specifies maximum stack depth
and heap size per invocation.
Memory management uses arena-based allocation
with deterministic deallocation at frame boundaries,
avoiding garbage collection pauses entirely.
There are no shared mutable globals.

### Embedding and Host Integration

The host exposes functions to the script
through a registered function interface,
similar to the Rhai embedding model.
Each host function has explicit effect annotations.
The host controls which capabilities
each script invocation receives,
following the capability-based security model
used by WebAssembly System Interface (WASI).

A script cannot access any resource
that the host has not explicitly granted.
File handles, network sockets, hardware interfaces,
and other sensitive resources
are available only through capability tokens
provided by the host at invocation time.

### Safety and Formal Guarantees

All state and effects are explicit.
Evaluation is deterministic.
There are no hidden side effects.
Resource usage is bounded and predictable.

The combination of static typing,
explicit effects, bounded resources,
and deterministic evaluation
makes programs written in this DSL
amenable to formal verification techniques including
Hoare logic, bounded model checking,
and worst-case execution time analysis.
Ivory and Copilot, two Haskell-based embedded DSLs
developed for safety-critical avionics at NASA,
demonstrate that this combination of properties
is achievable in practice.
The language is designed to be amenable
to formal analysis and external proof tools.
It does not attempt to be a proof language itself,
nor does the runtime perform proofs.

## Use Cases

### Plugin Systems

Applications that support user-defined plugins
need a scripting layer
that cannot crash the host or access unauthorized resources.
The proposed DSL provides sandboxed, capability-controlled execution
that guarantees plugin scripts
cannot corrupt host state or exceed resource bounds.

### Game Programming

Game engines require scripting
for gameplay logic, AI behavior, and modding support.
The hot update mechanism allows developers
to modify game scripts without restarting the engine.
Bounded resource usage prevents
individual scripts from causing frame drops.
Deterministic evaluation ensures
that gameplay logic produces consistent results
across different hardware.

### Robotics Scripting

Robotic systems require control logic
that is deterministic, verifiable,
and updatable without system downtime.
The proposed DSL's formal analyzability
allows control scripts to be verified
against safety properties
before deployment to physical hardware.
Hot code updates allow behavior changes
in running systems
at defined safe points.

## Related Work

The synchronous dataflow languages Lustre and SCADE
represent the state of the art
in formally verified embedded control languages.
SCADE Suite is certified to DO-178C for avionics
and has been deployed in safety-critical systems
for over twenty years.
These languages achieve formal verifiability
through synchronous semantics
that eliminate non-determinism.
The proposed DSL shares the goal of deterministic execution
but targets a broader set of use cases
and prioritizes embedding in general-purpose host applications
over standalone deployment.

Ivory and Copilot are Haskell-based embedded DSLs
developed at Galois with support from NASA.
Ivory provides safer C programming
through type-system-enforced memory safety,
bounded loops, and no heap allocation.
Copilot compiles stream-based specifications
into constant-time, constant-memory C99 code
suitable for hard real-time systems.
Both demonstrate that strong type systems
can guarantee safety properties by construction
and support integration with external provers.

The proposed DSL differs from these systems
in targeting runtime embedding
rather than code generation.
Where Ivory and Copilot generate C code
for ahead-of-time compilation,
the proposed DSL executes on a bytecode VM
within a running host application,
enabling hot code updates
and dynamic capability management.

### Reference VM Architectures

Several established virtual machine architectures
inform the design of the proposed bytecode VM.

The SECD machine,
introduced by Peter Landin in 1964,
provides the theoretical foundation
for functional language virtual machines
with closures and explicit environments.

The Lua 5.1 VM demonstrates
how a small, fixed-width instruction set
can achieve simplicity, performance, and analyzability
in an embeddable scripting context.

The WebAssembly core specification
provides a formally specified bytecode format
where bytecode is the semantic ground truth,
sandboxing is built in,
and host integration is capability-oriented.

The JVM bytecode verification architecture
demonstrates how static analysis at the bytecode level
can enforce type safety, stack discipline,
and control flow constraints before execution.

## Design Tradeoffs

The language deliberately trades unrestricted expressiveness
for predictability, safety, and analyzability.
Deterministic execution and immutability
make scripts safe for concurrent use.
Hot code updates occur only at explicit boundaries
to guarantee safety.
Formal semantics allow offline proofs,
worst-case execution time analysis,
and simulation validation.

These constraints limit what can be expressed in the language.
Complex stateful logic, dynamic dispatch,
and unbounded computation
must be implemented in the host
rather than in the script.
This boundary is intentional.
The host provides the full power
of a general-purpose language.
The script provides a safe, verifiable control layer on top of it.

The tradeoff mirrors
the design philosophy of SCADE and Lustre,
where restricted expressiveness
enables the formal guarantees
that mission-critical systems require.

## Summary

This article has proposed a safe embedded functional control DSL
for mission-critical applications
including plugin systems, game scripting,
and robotics control.
The language draws syntactic inspiration from Elixir,
targets seamless embedding in Rust,
and is designed to be provable and certifiable
without being a proof language itself.

The key design decisions are
static typing with effect tracking,
deterministic evaluation with bounded resources,
capability-based host integration,
and hot code updates at explicit boundaries.
These properties make programs written in the language
amenable to formal verification
using the techniques described in
{% post_url 2026-02-10-writing-proofs %}.

The proposal is informal.
Future work includes defining formal operational semantics,
building a reference implementation targeting a Rust host,
and evaluating the language against real-world
mission-critical scripting requirements.

## Future Reading

- [Rhai Embedded Scripting for Rust][reference_rhai],
  a small, fast, easy-to-use scripting language and engine
  that integrates tightly with Rust applications.

- [Elixir Programming Language][reference_elixir],
  a dynamic, functional language
  for building scalable and maintainable applications
  on the Erlang VM.

- [Gleam Programming Language][reference_gleam],
  a friendly language for building type-safe systems
  on the Erlang VM and JavaScript runtimes.

- [Roc Programming Language][reference_roc],
  a fast, friendly, functional language
  with a platform-based architecture
  for controlling I/O access.

- [Koka Language][reference_koka],
  a function-oriented language
  with algebraic effect handlers
  as a primary abstraction.

- [Copilot Runtime Verification Framework][reference_copilot],
  a stream-based DSL
  for generating constant-time, constant-memory C99 monitors
  for safety-critical systems.

- [The Implementation of Lua 5.0][reference_lua_impl],
  a detailed description of the virtual machine design
  that powers Lua's compact and efficient bytecode interpreter.

- [WebAssembly Core Specification][reference_wasm_spec],
  the formal specification of the WebAssembly bytecode format,
  execution model, and validation rules.

## References

- [Reference, Copilot Runtime Verification Framework][reference_copilot]
- [Reference, Elixir Programming Language][reference_elixir]
- [Reference, Erlang/OTP Code Loading][reference_erlang_code_loading]
- [Reference, Gleam Programming Language][reference_gleam]
- [Reference, Ivory Embedded DSL][reference_ivory]
- [Reference, JVM Specification][reference_jvm_spec]
- [Reference, Koka Language][reference_koka]
- [Reference, Lua Programming Language][reference_lua]
- [Reference, Lustre Synchronous Dataflow Language][reference_lustre]
- [Reference, Rhai Embedded Scripting for Rust][reference_rhai]
- [Reference, Roc Programming Language][reference_roc]
- [Reference, SECD Machine][reference_secd]
- [Reference, The Implementation of Lua 5.0][reference_lua_impl]
- [Reference, WebAssembly Core Specification][reference_wasm_spec]
- [Reference, WebAssembly Security Model][reference_wasm_security]
- [Research, Copilot NASA Technical Report][reference_copilot_nasa]

[reference_copilot]: https://copilot-language.github.io/
[reference_copilot_nasa]: https://ntrs.nasa.gov/api/citations/20200003164/downloads/20200003164.pdf
[reference_elixir]: https://elixir-lang.org/
[reference_erlang_code_loading]: https://www.erlang.org/doc/system/code_loading.html
[reference_gleam]: https://gleam.run/
[reference_ivory]: https://ivorylang.org/
[reference_jvm_spec]: https://docs.oracle.com/javase/specs/jvms/se21/html/index.html
[reference_koka]: https://koka-lang.github.io/koka/doc/book.html
[reference_lua]: https://www.lua.org/
[reference_lua_impl]: https://www.lua.org/doc/jucs05.pdf
[reference_lustre]: https://www-verimag.imag.fr/The-Lustre-Programming-Language-and
[reference_rhai]: https://rhai.rs/
[reference_roc]: https://www.roc-lang.org/
[reference_secd]: https://en.wikipedia.org/wiki/SECD_machine
[reference_wasm_security]: https://webassembly.org/docs/security/
[reference_wasm_spec]: https://webassembly.github.io/spec/core/
