---
layout: post
mathjax: true
comments: true
title:  "Block-Structured Control Flow and Single-Pass Validation"
date:   2026-04-10 09:00:00 +0000
categories: compilers streaming series
series: streaming_compilers
series_title: Streaming Compilers
series_index: 5
---
<!-- A192 -->
<script>console.log("A192");</script>

A bytecode format
that permits
arbitrary jumps
between arbitrary addresses
is
formally equivalent
to a directed graph
with no structural constraints.
Verifying such a format
requires
constructing a control-flow graph,
computing
a fixpoint
of the type-consistency relation
across every merge point,
and iterating
until the fixpoint stabilises.
The verification cost
in the worst case
is
super-linear
in the program size,
and the verification algorithm
is
non-trivial
to prove correct.

A bytecode format
that restricts control flow
to block-structured constructs,
namely
matched pairs of
`If` and `EndIf`,
`Loop` and `EndLoop`,
and `Break` statements
that reference
enclosing loops
by relative index,
admits
a single-pass validator.
The verifier
walks the instruction stream
once
from start to finish,
tracks
a small amount of state,
and produces
a definitive
accept-or-reject decision
without ever
constructing a graph
or iterating to a fixpoint.
This is
the single-pass-validation property
that WebAssembly
codified
and that
the [Haas et al. PLDI two thousand seventeen paper][research_haas_webassembly]
made
the design canonical
for portable bytecode.

The theory pair
of this series
opens
with block-structured control flow
because it is
the language-design lever
that most directly
enables
the stream-processor
compilation discipline.
A compiler
that emits
block-structured control flow
can also
verify it
in the same forward sweep.
A compiler
that emits
arbitrary jumps
cannot.
The productivity guarantee
that article A193
develops
in coalgebraic terms
would not
apply
to the compiled output
of an unstructured-control-flow language,
even if
the compiler itself
were structured
as a stream processor.

## Block-Structured Control Flow Defined

A block-structured
instruction stream
consists of
sequential instructions
interspersed with
block delimiters
that come in
matched pairs.
The typical
block-delimiter set
comprises

- `If` and `EndIf`,
  optionally with a middle `Else`,
  for conditional execution.
- `Loop` and `EndLoop`
  for iteration.
- `Break` and `BreakIf`
  for early exit from
  enclosing loops.

Every `If`
in a well-formed stream
matches
exactly one `EndIf`.
Every `Loop`
matches
exactly one `EndLoop`.
Every `Break`
appears
lexically inside
the loop
it exits.
The matching
respects nesting,
so the innermost
unclosed opener
matches
the next closer,
and the openers
form a stack
of currently open blocks.

The block structure
is a property
of the instruction stream itself,
not of the source language.
A source language
that admits
arbitrary
`goto` statements
can be compiled
to a block-structured target
only by
restricting the source
to eliminate
unstructured control flow,
or by
introducing
auxiliary state variables
that simulate
the unstructured jumps
inside a structured envelope.
The second option
is
formally possible
in theory,
following the classical
result of
Böhm and Jacopini,
but produces
inefficient
target code
in practice.
Most block-structured bytecode formats
therefore
constrain
the source languages
they target
rather than
simulating
unstructured control flow.

## The Validation Problem

A bytecode verifier
is
a program
that inspects
a bytecode module
and accepts or rejects it
based on
whether the module
satisfies
a set of
structural safety properties.
The typical properties
include the following.

**Type consistency.**
Every instruction
that consumes values
from a stack
finds values
of the correct type.
Every instruction
that produces values
onto a stack
leaves them
in the state
that subsequent instructions
expect.
At every merge point
in the control-flow graph,
the type-stack states
arriving from
different predecessors
agree.

**Control-flow integrity.**
Every jump target
is
a valid instruction address
within the module.
Every conditional branch
falls through
or takes its jump
based on
the runtime value
of its condition,
but never
transfers control
to
an out-of-bounds address
or
into the middle of
another instruction.

**Resource bounds.**
The verifier
may impose
additional constraints
on
the maximum stack depth,
the maximum local-variable count,
or the memory footprint
of the module.
These constraints
support
resource-bounded execution
in embedded or
safety-critical contexts.

The verifier's problem
is
to decide
whether
a given module
satisfies
these properties.
The cost
of the decision procedure
depends on
the shape of
the input's control flow.

## How Block Structure Enables Single-Pass Validation

For a block-structured instruction stream
of length $n$,
the verifier
walks the stream
once
from position zero
to position $n$.
At each position,
the verifier
maintains
three pieces of state.

- A block-nesting stack $B$
  that records
  the currently open blocks
  and their block types.
- A type stack $S$
  that records
  the values that have been produced
  by executed instructions
  but not yet consumed.
- A block-depth counter $d = \lvert B \rvert$.

At each instruction,
the verifier
updates these three pieces of state
in constant time
based on
the instruction's opcode
and its operands.
An arithmetic instruction
consumes a fixed number of stack entries
and produces
a fixed number.
A block opener
pushes an entry onto $B$
and increments $d$.
A block closer
pops the matching entry
from $B$
and decrements $d$.
A `Break`
references
a relative loop index
that the verifier
resolves
against $B$
by counting from
the top of the stack.

The correctness invariants
enforced at each step
include the following.

**Block-nesting invariant.**
At every position,
the block-nesting stack
matches
the sequence of
opened but unclosed blocks
in the instruction stream:

$$
B_{\text{at } i}
= \operatorname{stack}(\text{unclosed openers in } [0, i)).
$$

**Type-consistency invariant.**
At every position,
the type stack
matches
the actual stack state
that any execution
reaching this position
would produce:

$$
S_{\text{at } i}
= \operatorname{type-of}(\text{runtime stack at } i).
$$

**Block-closer type-check.**
At every block closer,
the type stack
at the closer
matches
the type stack
at the corresponding opener,
adjusted for the block's
declared type signature.
Formally,
for a block opened at position $o$
with declared type signature
$\sigma_{\text{in}} \to \sigma_{\text{out}}$
and closed at position $c$,
the type stacks at the two positions
share a common base $R$
and differ only in the top portion:

$$
S_o = R \cdot \sigma_{\text{in}},
\qquad
S_c = R \cdot \sigma_{\text{out}}.
$$

The base $R$
records
the values on the stack
below the block's operating region,
which the block's execution
does not touch.

The three invariants
compose.
An instruction
that satisfies
them locally
at position $i$
produces a state
that satisfies
them at position $i+1$
by the same local check.
The single-pass sweep
verifies
each position's local check
in constant time.
The overall
verification cost
is therefore

$$
C_{\text{verify}}(\text{module}) = O(n),
$$

where $n$
is the total instruction count.
This is
the best possible
asymptotic cost
for
any verification algorithm
that must inspect
every instruction
at least once.
No fixpoint iteration
is required
because
block-structured control flow
has no
non-trivial merge points.
Every merge
is
the join at a block closer,
and the type states
that merge there
are determined
by
the block's declared type signature,
not
by iterative propagation.

## The WebAssembly Realization

WebAssembly
is
the modern canonical example
of a block-structured bytecode format
designed for
single-pass validation.
The [Haas et al. two thousand seventeen paper][research_haas_webassembly]
documents
the design rationale.
The paper
received the
Programming Language Design and Implementation
Distinguished Paper Award
of that year
in part
for the observation
that block-structured control flow
enables
single-pass validation
with linear cost.

WebAssembly's block constructs
include
`block`,
`loop`,
`if` with optional `else`,
`br` and `br_if`
for structured branches,
`br_table` for
switch-style multi-way branches,
and the closing `end` marker
for each opener.
The `br` instruction
takes
a relative label index
that references
an enclosing block by nesting position,
matching
the abstract structure
described above.
The type of each block
is declared
at the opener,
which fixes
the type-stack signature
that the block closer
must produce.
The declared type
serves as
the contract
that the verifier
uses to reject
non-conforming block bodies
in a single sweep.

Reference implementations
of the WebAssembly single-pass validator,
including
the `wasm-validate` tool
in the WebAssembly Binary Toolkit
and the type-checker portion
of the specification's
reference interpreter,
run on the order of
one to three thousand lines
of source code
depending on
the target language
and the metrics used.
Comparable Java Virtual Machine
bytecode verifier implementations,
in production runtimes,
run substantially larger.
The size difference
reflects
the algorithmic simplification
that block structure enables.
A verifier
that does not construct
a control-flow graph,
does not iterate to fixpoint,
and does not resolve
polymorphism through subtyping
is
fundamentally smaller than
one that must do all three.

## What Block Structure Prohibits

Block-structured control flow
excludes
several patterns
that are
common in
unstructured bytecode formats.

**Unconditional jumps
to arbitrary addresses.**
An unconditional
`goto` instruction
that transfers control
to an arbitrary target
cannot be verified
in a single sweep
because
the verifier
would need
to know
the type-stack state
at the target
before it has been
computed.

**Backward jumps
that are not loop-backs.**
A backward jump
that lands
outside
the current loop
would require
the verifier
to re-examine
the intervening code
under
the potentially different
type-stack state
that arrives from
the new source.
Block-structured formats
prohibit this
by construction.

**Fallthrough
between distant labels.**
Labels
outside
the block structure,
which appear
in
switch-fallthrough patterns
in C
and in
computed-goto patterns
in some Fortran dialects,
cannot be expressed
in the block-structured discipline
without
introducing an
auxiliary state variable.

**Exception handlers
that catch across
arbitrary regions.**
Exception handling
in
Java and dot-NET
uses
try-catch blocks
whose scopes
may nest arbitrarily
but whose control flow
crosses
the block boundaries
in ways that
break the block-structured discipline.
WebAssembly
addressed this
by adding
a structured exception mechanism
as
a language extension
rather than
as
an unstructured jump.

These prohibitions
are
sometimes cited
as
limitations of
block-structured formats.
The alternative view,
which WebAssembly's success
supports,
is that
the prohibited patterns
are
themselves
liabilities
that
the bytecode format
should not encourage,
because their absence
is what makes
the linear-cost verifier possible.
The trade-off
is real
but
substantially favours
the block-structured side
for
the portable-bytecode use case.

## Contrast with Unstructured Bytecode

The Java Virtual Machine bytecode format
predates
the block-structured design
and permits
arbitrary control flow.
The Java bytecode verifier
therefore
must construct
a control-flow graph
and iterate
a type-consistency computation
to fixpoint
across every merge point.

The complexity
of the Java bytecode verifier
is
higher than
the WebAssembly verifier
by a factor
that depends on
the number of merge points
and the depth of
the type subtyping lattice.
In the worst case,
the fixpoint iteration
can require
a number of passes
proportional to
the depth of
the subtyping lattice.
For a module
with
$n$ instructions
and
$m$ merge points,
the Java bytecode verifier's
worst-case cost
is
on the order of

$$
C_{\text{JVM verify}} = O(n \cdot m \cdot h),
$$

where $h$
is the maximum
subtype-lattice height
encountered during verification.
This is
an order-of-magnitude estimate
rather than
a tight complexity bound,
because the actual verifier
uses dataflow analysis
whose per-instruction cost
depends on
implementation details.
The order-of-magnitude claim
is
that
the cost
is
super-linear in $n$
under the fixpoint discipline,
which
the block-structured verifier
avoids by construction.
For programs that use
deep class hierarchies,
$h$
is not small.
Expressed as a ratio
against
the block-structured baseline,
the multiplicative overhead
of unstructured control flow
is

$$
\frac{C_{\text{JVM verify}}}{C_{\text{verify}}}
= O(m \cdot h),
$$

which is
the cost paid
for
admitting arbitrary jumps
in the bytecode format.

The Java bytecode verifier
has also
had
a significant number of
security-relevant bugs
over its history.
These bugs
partly reflect
the intrinsic difficulty
of implementing
the fixpoint algorithm
correctly.
A verifier
whose algorithm is
a single forward sweep
has
fewer opportunities
to introduce
subtle bugs.
The block-structured discipline
therefore has
a security advantage
that is
independent of
its performance advantage.

## Watt's Mechanized Specification

Conrad Watt's
[two thousand eighteen mechanised WebAssembly specification][research_watt_wasm]
in the Isabelle proof assistant
provides
a machine-checked proof
that
the WebAssembly type system
is sound.
The proof
establishes that
well-verified WebAssembly modules
cannot get stuck
during execution
because of
a type error.
This is
a soundness guarantee
that the informal
specification alone
does not provide.

The formal statement
that Watt proved
is
the type-soundness property.
For every module $M$
and every execution trace $\tau$
of $M$,

$$
\operatorname{verify}(M) = \text{accept}
\implies
\neg \operatorname{stuck}(\tau).
$$

A verified module
does not
encounter
a type error
at run time.
The predicate
$\operatorname{stuck}$
denotes
runtime execution states
that
cannot make progress
because of
a type mismatch
between an instruction
and the values on the stack.

Watt's work
also
identified
several issues
in the official
WebAssembly specification
that had been
missed by
the human reviewers.
The identified issues
were subsequently
corrected
in the WebAssembly standard.
The Watt result
demonstrates
two properties
that matter
for the theory pair
of this series.

The first property
is
that
formal verification
of a block-structured bytecode
specification
is
feasible
with current mechanization tools.
The Watt proof
required
substantial effort
in the Isabelle framework,
as any
mechanization of
a production specification does,
but the effort
was within reach
of a single-researcher project.
The comparable
mechanization
of an unstructured bytecode
would require
substantially more work
because
the fixpoint algorithm
would need to be
formalised
as well.

The second property
is
that
the WebAssembly specification,
even after
careful human review,
contained
subtle errors
that a mechanization
uncovered.
This finding
is a datum
in favour of
the position
that
critical specifications
should be
mechanized.
For safety-critical or
security-critical bytecode,
mechanization
should be
part of
the specification process,
not
an optional
post-hoc verification exercise.

## Legacy and Modern Adoption

Block-structured control flow
predates
WebAssembly
by decades.
The Wirth-line languages
of article A189
used
block-structured control flow
at the source level
for the same reasons
that make it
attractive
at the bytecode level.
Wirth's target machines
for Oberon
also
used block-structured control flow
at the instruction-set-architecture level,
avoiding
arbitrary jumps
in the compiled output.
The WebAssembly design
made the bytecode-level
block-structure discipline
explicit and universal
for a modern
portable-bytecode format.

Several
subsequent bytecode formats
have adopted
the block-structured discipline.

- **Move**,
  the bytecode format
  originally developed for Diem
  and subsequently adopted by
  the Aptos and Sui blockchains,
  uses
  block-structured control flow
  for
  the resource-safety verifier.
- **Wasm-inspired embedded scripting bytecodes**,
  including
  several coroutine-based
  research systems,
  adopt
  block-structured control flow
  for
  the same
  verification-cost reasons.
- **Source-language intermediate representations**
  that were designed
  for
  fast-compilation targets,
  including
  Dart's Kernel format,
  favour
  structured control flow constructs
  even where
  formal single-pass validation
  is not the primary concern.

The pedagogical tradition
around
compiler construction
has been
slower to adopt
the block-structured framing
at the bytecode level.
Standard textbooks
still
present
bytecode verification
in the Java Virtual Machine style
with
control-flow graph construction
and fixpoint iteration
as the default.
The block-structured alternative,
which is
substantially simpler
to teach
and to implement,
merits
more prominent treatment
in
future editions.

## Conclusion

Block-structured control flow
at the bytecode level
enables
single-pass validation
with cost linear
in the instruction count.
The alternative,
arbitrary control flow,
requires
a control-flow-graph construction
and a fixpoint iteration
whose cost
is
super-linear
in the instruction count
and whose implementation
has historically
suffered from
subtle bugs.
The WebAssembly design
codified
the block-structured discipline
for
the modern
portable-bytecode use case
and
received
substantial
academic recognition
for the observation
that
the language-design constraint
enables
the verification-cost reduction.
Conrad Watt's
mechanized proof
of WebAssembly
soundness
provides
formal-methods evidence
that
the design
is
sound
and that
the specification
is
mechanizable.
Article A193
develops
the mathematical framework
that
formalises
the streaming discipline itself,
in coalgebraic terms,
and shows
why
block-structured control flow
is
the natural
syntactic constraint
that
places
a compiled program
inside
the decidable subclass
of productive
stream processors.

## References

### Book

- [*Compiler Construction*][book_wirth_compiler_construction], Niklaus Wirth, Addison-Wesley, 1996

[book_wirth_compiler_construction]: https://en.wikipedia.org/wiki/Compiler_Construction_(Wirth_book)

### Reference

- [WebAssembly specification and single-pass validator][ref_webassembly]
- [Java Virtual Machine bytecode format][ref_jvm]
- [Aho, Sethi, Ullman, and Lam Dragon Book on compiler construction][ref_dragon_book]

[ref_webassembly]: https://en.wikipedia.org/wiki/WebAssembly
[ref_jvm]: https://en.wikipedia.org/wiki/Java_bytecode
[ref_dragon_book]: https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series
- [Brinch Hansen's Pipeline-of-Processes Compilers][related_post_brinch_hansen], article A191 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
[related_post_brinch_hansen]: {% post_url 2026-04-09-brinch_hansen_pipeline_of_processes %}

### Research

- [Böhm and Jacopini, Flow Diagrams, Turing Machines and Languages with only Two Formation Rules, Communications of the ACM 9 number 5, 1966][research_bohm_jacopini]
- [Haas and colleagues, Bringing the Web up to Speed with WebAssembly, PLDI 2017][research_haas_webassembly]
- [Watt, Mechanising and Verifying the WebAssembly Specification, CPP 2018][research_watt_wasm]

[research_bohm_jacopini]: https://doi.org/10.1145/355592.365646
[research_haas_webassembly]: https://dl.acm.org/doi/10.1145/3062341.3062363
[research_watt_wasm]: https://dl.acm.org/doi/10.1145/3167082
