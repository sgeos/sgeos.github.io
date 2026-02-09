---
layout: post
mathjax: false
comments: true
title: "Safe Embedded Functional Control DSL"
date: 2026-02-13 00:00:00 +0000
categories: dsl embedded development safety
---

<!-- A83 -->

Safety-critical embedded systems such as aerospace drones
require control logic that is deterministic, verifiable, and hot-updatable.
General-purpose programming languages offer expressiveness
at the cost of unpredictable resource usage,
hidden side effects, and undefined behavior.
Existing domain-specific languages for embedded control
tend to be imperative, making formal analysis difficult.

This article proposes a safe embedded functional control DSL
designed for aerospace drone control logic and similar safety-critical applications.
The language prioritizes formal analyzability, deterministic execution,
and safe hot code updates over unrestricted expressiveness.
It is not a language for writing proofs,
but it is designed to be provable and certifiable.

The specification presented here is a draft.
It captures the core design goals, language features,
runtime architecture, and embedding model.
Future work will flesh out the formal semantics,
provide a reference implementation, and explore certification pathways.

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

## Design Goals

The language has seven high-level design goals.
Each goal reflects a constraint imposed by safety-critical embedded environments.

**Maximum Safety.**
The language must be memory-safe with sandboxed execution.
There must be no undefined behavior and no hidden side effects.
All programs must execute deterministically.

**Formal Analyzability.**
The language must have fully defined operational semantics.
Evaluation must be deterministic and pure functional where possible.
State and effects must be explicit
to enable formal proofs, model checking,
and worst-case execution time (WCET) analysis.

**Embeddability.**
The language must integrate cleanly into Rust and other host systems.
The host manages concurrency.
Language execution is isolated.
The boundary between script logic and host resources must be well defined.

**Hot-Updatable Logic.**
Code updates must occur only at explicit tick or epoch boundaries.
Safe rollback to the prior version must be supported.
There must be no live stack rewriting.
Updates must be atomic and deterministic.

**Functional, Lightweight Syntax.**
The language must support pattern matching,
pipelines with placeholder support,
multi-headed functions,
and algebraic data types.
The syntax must be minimal and readable.

**Concurrency-Safe Design.**
Script-visible state must be immutable.
Each VM execution must be isolated.
Multiple scripts must be safe to run concurrently without locking.

**Performance Considerations.**
Scripts must compile to bytecode for a stack-based VM.
Resource usage (stack, heap, instruction counts) must be deterministic.
Optional JIT or LLVM compilation may be supported
for offline analysis or simulation.

## Language Features

### Functional Programming

Expressions are pure by default.
Side effects must be explicit via host-bound functions.
The language supports immutability and total functions.

### Pipelines

Pipelines use the `|>` operator to chain transformations.
The placeholder `@` indicates where the piped value is inserted.

```text
value |> f |> g(1, @)
```

A single placeholder is permitted per call.
The compiler rewrites pipelines for efficiency.

### Pattern Matching

Pattern matching must be exhaustive.
Partial functions must be explicitly marked.
Matching is supported on algebraic data types and tuples.

### Multi-Headed Functions

Function bodies are selected based on pattern matching of arguments.

```text
fn foo(0) = "zero"
fn foo(n) = n |> bar
```

### Algebraic Data Types

The language supports sum types for variant types.
Tagged values with payloads are supported.
Exhaustive handling in match statements is encouraged
and may be required for certifiable code.

### Type System

The language is strongly typed with optional type inference.
Static type checking is preferred for certifiable code.
Explicit effect annotations are required for I/O or host-bound operations.

### Hot Update Mechanism

Scripts can be replaced only at defined tick or epoch boundaries.
The old version remains available for rollback.
The VM maintains function tables with version indirection.

### Concurrency Semantics

Script-visible state is immutable.
Each execution has an isolated stack and heap.
The language provides no internal concurrency primitives.
The host handles scheduling.

## Runtime and VM Architecture

### VM Design

The VM is stack-based, deterministic, analyzable, and certifiable.
Scripts are represented as bytecode.
Each invocation has a separate execution frame.
An optional debug and trace mode supports formal verification.

### Memory Model

Stack and heap allocation are controlled.
Garbage collection or arena-based lifetime management
is compatible with the Rust host.
There are no shared mutable globals.

### Embedding and Host Integration

The host can expose functions with explicit effect annotations.
The host manages concurrency and I/O.
Type marshalling between host and script is safe.
Resource access follows a capabilities-based model.

### Safety and Formal Guarantees

All state and effects are explicit.
Evaluation is deterministic.
There are no hidden side effects.
Resource usage (execution time and memory) is bounded and predictable.

## Example

The following illustrative script demonstrates
algebraic data types, pattern matching, pipelines,
and explicit host-bound effects.

```text
enum SensorEvent {
    Temperature(f32),
    Pressure(f32)
}

fn respond(SensorEvent.Temperature(t)) when t > 50.0 =
    log("High temperature detected") |> host_alert(@)

fn respond(SensorEvent.Pressure(p)) =
    p |> calculate_pressure_response |> host_set_actuator(@)
```

The functions `host_alert` and `host_set_actuator` are host-bound.
They represent explicit effects.
The script is fully analyzable
and safe to run concurrently
if multiple sensor events arrive in parallel.

## Design Tradeoffs

The language deliberately trades unrestricted expressiveness
for predictability, safety, and analyzability.
Deterministic execution and immutability make scripts safe for concurrent use.
Hot code updates occur only at explicit boundaries to guarantee safety.
Formal semantics allow offline proofs,
WCET analysis, and simulation validation.

These constraints limit what can be expressed in the language.
Complex stateful logic, dynamic dispatch, and unbounded computation
must be implemented in the host rather than in the script.
This boundary is intentional.
The host provides the full power of a general-purpose language.
The script provides a safe, verifiable control layer on top of it.

## Summary

This article has proposed a safe embedded functional control DSL
for safety-critical applications such as aerospace drone control.
The language is designed to be provable and certifiable
without being a proof language itself.
It prioritizes deterministic execution, explicit effects,
hot-updatable logic, and concurrency safety.

The specification is a draft.
Future work includes defining the formal operational semantics,
building a reference implementation (likely targeting a Rust host),
exploring certification pathways for aerospace applications,
and evaluating the language against real control system requirements.

## Future Reading

This is a draft specification.
Future reading will be added as the design matures
and related work is identified.

## References

No external references were consulted for this draft.
References will be added in future revisions
as the specification is developed and validated against related work.
