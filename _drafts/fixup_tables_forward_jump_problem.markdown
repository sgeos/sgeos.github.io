---
layout: post
mathjax: true
comments: true
title:  "Fixup Tables and the Forward-Jump Problem"
date:   2026-04-12 09:00:00 +0000
categories: compilers streaming series
---

<!-- A194 -->
<script>console.log("A194");</script>

A single-pass compiler
that emits target code
as it recognises source syntax
faces
one fundamental engineering problem
that no amount of
language design can eliminate.
The problem
is the forward jump.
An `if` statement's
conditional jump
must skip
past the `then` branch
when the condition is false,
but
the address
just past the `then` branch
is not known
at the moment
the conditional jump
is emitted.
The `then` branch
has not yet
been parsed,
so its length
is not yet known.
The compiler
must
emit the jump
without a known target
and
return later
to fill the target in.

This is
the forward-jump problem.
It appears
in every compiler
that
emits target code
in a forward sweep,
regardless of
whether
the target
is stack-based bytecode,
register-based bytecode,
or native machine code.
The classical solution
is
the fixup table,
also called
the fixup buffer,
the patch table,
the backpatch list,
or
the fixup stack
depending on
the implementation choice.
The article A189
introduced the fixup table
briefly
in the worked PL/0 example.
This article
develops
the mechanism
in full,
argues
why
the fixup table's size
is
bounded by
the source nesting depth
rather than
by
the program size,
and shows
how
the mechanism
generalises
to
break statements,
early returns,
and
the other
non-linear
control-flow constructs
that
block-structured source languages admit.

## The Classical Solution

A fixup table
is
a data structure
that records
each
emitted-but-not-yet-resolved
forward reference.
Each entry
in the table
carries
two pieces of information.

The first piece
is
the location
in the emitted output
where
the target address
needs to be written.
This is
the address of
the operand field
of the emitted jump instruction,
called the
placeholder position.

The second piece
is
the identity
of the target
that
the placeholder
will eventually refer to.
For block-structured constructs
where the target
is
always
"the position
just past this block",
the target identity
is
implicit
in
the fixup entry's
position on
the fixup stack.
For more elaborate control flow,
the target identity
may include
a label name
or
a block-type tag.

Formally,
a fixup entry
is
a pair

$$
e = (a_{\text{placeholder}}, \iota_{\text{target}}),
$$

where
$a_{\text{placeholder}}$
is
the address
of the operand field
to be patched
and
$\iota_{\text{target}}$
is
the target identity.
For block-structured constructs,
$\iota_{\text{target}}$
is
often
just
the enclosing-block-index.

The compiler
maintains
a fixup buffer $F$
that holds
the currently unresolved fixup entries.
The buffer
supports
three operations.

**Enqueue.**
When
a forward jump
is emitted,
a new fixup entry
is appended
to
the buffer.
The placeholder position
is
the current output position
plus
the operand-field offset
within the emitted instruction.
The target identity
is
determined by
the syntactic context
that emitted the jump.
Formally,
enqueue transforms
the fixup buffer
by set union

$$
F' = F \cup \{(a_{\text{placeholder}}, \iota_{\text{target}})\}.
$$

**Resolve.**
When
the target address
becomes known,
the compiler
walks
the fixup buffer,
finds
all entries
whose target identity
matches
the newly known address,
and patches
the placeholder position
at each entry
with
the resolved address.
Resolved entries
are
removed
from the buffer.
Formally,
resolve
patches each matching entry
against
the resolved address
$a_{\text{resolved}}$
and then removes them,

$$
F' = F \setminus \{ e \in F : \iota_e = \iota_{\text{target}} \},
$$

where
each removed entry
$e = (a_e, \iota_e)$
has
its placeholder position $a_e$
patched
with $a_{\text{resolved}}$
before removal.

**Terminate.**
At the end of
compilation,
the fixup buffer
must be empty.
Any remaining entry
represents
an unresolved forward reference,
which is
a compile-time error.
The check
is
inexpensive.

## A Worked Example, `if-then-else` Compilation

Consider the Pascal-style
source fragment

```pascal
IF x > 0 THEN
  y := 1
ELSE
  y := 2
END
```

The single-pass compiler
processes this fragment
in three phases,
interleaving code emission
with fixup table operations.

**Phase 1: parse the condition.**
The compiler
parses `x > 0`
and emits
the load and compare instructions.
At the end of the condition,
the operand stack
carries
a boolean value
representing
the condition's result.
The compiler
emits
a conditional-jump-if-false instruction
with a placeholder
in its operand field.
Denote the placeholder position
by $a_1$.
The compiler
enqueues
the fixup entry
$(a_1, \text{else-branch})$
into the fixup buffer.

**Phase 2: parse the `then` branch.**
The compiler
parses `y := 1`
and emits
the corresponding
assignment instructions.
No fixup activity
occurs
during this phase
because
the `then` branch
has no
forward references
of its own.
After emitting
the `then` branch,
the compiler
emits
an unconditional jump
with a placeholder
in its operand field
to skip
over
the `else` branch.
Denote this placeholder
by $a_2$.
The compiler
enqueues
$(a_2, \text{end-of-if})$.

At this point,
the current output position
is
the address
just past
the unconditional jump.
The compiler
resolves
the first fixup entry
$(a_1, \text{else-branch})$
by
patching
the operand field at $a_1$
with
the current output position.
The first fixup entry
is removed
from the buffer.

**Phase 3: parse the `else` branch.**
The compiler
parses `y := 2`
and emits
the assignment instructions.
After the `else` branch,
the compiler
resolves
the second fixup entry
$(a_2, \text{end-of-if})$
by
patching
the operand field at $a_2$
with
the current output position.
The second fixup entry
is removed
from the buffer.

At the end of
the `if-then-else` compilation,
the fixup buffer
returns to
its state
at the start
of
the construct.
No fixup entries
persist
past
the construct's closer.
The two fixup entries
introduced
during
the compilation
were
retired
during
the same compilation
in strict
last-in-first-out order.

## Nesting and the Fixup Stack

The `if-then-else` worked example
generalises
to
arbitrary nesting depth.
Consider
an outer `if`
whose `then` branch
contains
an inner `if`.
When
the compiler
reaches the inner `if`,
the outer `if`'s
first fixup entry
is
already in the buffer,
awaiting
its
resolution
at the end of
the outer `then` branch.
The inner `if`
adds
its own
fixup entries
on top of
the outer's,
and
the compilation
proceeds
by
processing
the inner construct
completely
before
returning to
the outer.

The fixup buffer
therefore
behaves
as a stack
under block-structured compilation.
Fixup entries
are pushed
when
their forward references
are emitted
and popped
when
their targets
are resolved.
The stack discipline
is
enforced
by
the source language's
block structure,
not by
the compiler's
internal choice.
A source language
that admits
block-structured control flow
gives
the fixup buffer
a
stack discipline
by construction.

## The Bound on Active Entries

The stack discipline
combined with
the block-nesting bound
gives
a tight bound
on
the fixup buffer size.
Let
$d$
denote
the current syntactic nesting depth
of the parse cursor.
At any point
during compilation,
the number
of active fixup entries
satisfies

$$
\lvert F \rvert \le c \cdot d,
$$

where
$c$
is
a small constant
that depends on
the source language.
For Pascal-style
`if-then-else`
constructs,
$c = 2$
because
each nesting level
contributes
at most two fixup entries,
one for
the false-branch jump
and one for
the end-of-if jump.
For `loop` constructs
with
`break` statements,
$c$
may be
somewhat larger
because
multiple `break` statements
inside
the same loop
each contribute
their own
fixup entry.

The nesting depth $d$
is
bounded a priori
by
the language grammar
and by
the source program's
maximum nesting.
For realistic
Wirth-language programs,
$d$
rarely exceeds
several dozen
even for
large programs.
The fixup buffer size
is therefore
several orders of magnitude
smaller than
the program size
in
typical use.
For a concrete estimate,
using
a typical maximum nesting depth
of thirty
and a
per-nesting-level fixup constant
of five,

$$
\lvert F \rvert
\le c \cdot d
\le 5 \cdot 30
= 150 \text{ entries}.
$$

At eight to sixteen bytes
per entry,
the fixup buffer
occupies
under two kilobytes
of memory
regardless of
the source program size.
The buffer's memory footprint
is
$O(d)$
in the source nesting depth
and
$O(1)$
in the source program size.

## Per-Entry Cost and Total Compilation Cost

Each fixup entry
is enqueued
in constant time,
resolved
in constant time
once the target is known,
and terminated
implicitly
when
the enclosing block closes.
The per-entry cost is

$$
C_{\text{fixup}} = O(1).
$$

The total number
of fixup entries
generated
during compilation
is bounded by
the number of
forward-reference emissions
in the source,
which is
linear in
the source program size.
The total
fixup-management cost
is therefore

$$
C_{\text{fixup total}}(P) = O(\lvert P \rvert),
$$

which contributes
a constant factor
to
the linear-in-program-size
compilation cost
established
in article A189.

## Extensions to Non-If Constructs

The fixup mechanism
extends
straightforwardly
to
other block-structured control-flow constructs.

**`while` and `for` loops.**
A `while` loop
emits
a
condition check
followed by
a
conditional-jump-if-false
to a
placeholder
representing
the loop exit.
The body
is emitted next,
followed by
an
unconditional jump
back to
the condition check.
The unconditional jump's target
is known
at the time of emission,
so no fixup is needed
for the loop-back.
The conditional-jump-if-false
fixup
is resolved
when
the end of the loop
is recognised.
The mechanism
introduces
one fixup entry
per active loop
and
is fully
subsumed by
the block-nesting bound
above.

**`break` and `break_if`.**
A `break` statement
inside a loop
emits
an unconditional jump
to
a placeholder
representing
the enclosing loop's exit.
The jump's target
is not known
at the time
of the `break`'s
emission,
so a fixup entry
is added
to the buffer.
The fixup entry
carries
a target identity
that names
the enclosing loop
by relative index.
When the enclosing loop's `end`
is recognised,
the compiler
resolves
all
`break` fixup entries
that name
this loop
by
patching
their placeholder positions
with
the loop-exit address.
The number of
`break` fixup entries
active
at any point
is bounded
by the total number
of `break` statements
inside
the currently unclosed loops,
which is
in turn
bounded
by
the loop-body size,
which is
finite by
block-structured control flow.

**Early returns.**
An early return
inside a function
emits
an unconditional jump
to
a placeholder
representing
the function's exit.
The mechanism
is
identical to
`break`,
with
the enclosing function
playing the role of
the enclosing loop.
Early returns
typically
add
one fixup entry per early-return statement.

**Case and switch dispatch.**
A dispatch table
that
selects one of
several branches
based on
a discriminant value
emits
one conditional jump per case
plus
one unconditional jump per case
to
a shared exit placeholder.
Each unconditional jump
adds
a fixup entry
that is resolved
at
the end of the switch.
The number of
active entries
is bounded by
the number of cases,
which is
finite by
the source-level construct.

## What Block Structure Simplifies

The fixup table mechanism
becomes
substantially more complex
in the absence of
block-structured control flow.
An unstructured source language
with
free
`goto` statements
and
free
labels
admits
forward references
whose targets
may
lie
across arbitrary code sections.
A fixup entry
introduced
at
one point
in
the source
may remain
in the buffer
until
its target label
is defined,
which may occur
many source lines later
in
an arbitrary part of
the program.
The fixup buffer
under this discipline
does not
behave
as a stack.
It behaves
as a
label-indexed
dictionary
that
grows
with
the number of
outstanding forward-referenced labels.

The bound
on
active fixup entries
under
unstructured control flow
is
therefore

$$
\lvert F_{\text{unstructured}} \rvert
= O(\lvert L \rvert),
$$

where
$\lvert L \rvert$
is
the number of
labels
in the source program
with
forward references.
This bound
is
generally
proportional to
the program size,
not to
the nesting depth.
The fixup buffer
is
no longer
$O(1)$
in the program size
under
unstructured control flow.

The specific engineering choices
that unstructured compilers make
include
a hash-indexed
label dictionary
that maps
label names to
either
resolved addresses
or
lists of pending fixup entries.
The dictionary
lives
outside
the stack discipline
and
grows
with
the source program.
The compilation cost
per source line
increases
compared to
the block-structured case
because
each label reference
requires
a dictionary lookup
rather than
a stack index.

## Modern Realisations

Contemporary single-pass compilers
implement
the fixup table mechanism
under
several names
and
with
several
minor variations.

WebAssembly's block-structured discipline
admits
a stack-of-fixup-lists
data structure
that
matches
the block-nesting discipline directly.
Each block-opener
pushes
an empty fixup list
onto
a control stack.
Each forward reference
within the block
appends to
the top-of-stack list.
Each block-closer
pops
the top-of-stack list
and
patches
all
its entries
against
the block-closer's address.
Production WebAssembly implementations,
including V8
and the WebAssembly Binary Toolkit,
use
variations of this shape,
with
implementation-specific details
that trade
memory footprint
against
branch-resolution speed.
The construction
maps
one-to-one
with
the block-structured discipline
that
WebAssembly's
type system
requires.

Coroutine-based
embedded scripting bytecodes
that adopt
block-structured control flow
follow
the same pattern.
The fixup table
lives
inside
the compiler's
arena or heap
in
a fixed-capacity buffer
whose
maximum size
is a
compile-time property
of the source language grammar.

Older single-pass compilers
in
the Wirth line
used
the same mechanism
implemented in
their compiler source language.
The Wirth Oberon compiler
source
in
*Project Oberon*
implements
the fixup mechanism
concisely
across
a small number
of
Oberon procedures,
with
the actual line count
depending on
what is counted
as part of
the mechanism
versus
part of
the surrounding
code-emission scaffolding.
The Turbo Pascal
implementation of
the same mechanism
was written
directly
in
eight-oh-eight-six assembly language
and remains
closed-source,
as
article A190 discussed.

## Conclusion

The fixup table
is
the essential engineering technique
that
makes
single-pass code emission
possible
in
a source language
that admits
forward references.
The mechanism
is
straightforward,
has a
constant per-entry cost,
and
produces a
buffer size
bounded
by
the source nesting depth
rather than
by
the program size,
which
is
$O(1)$
in the program size
for
block-structured source languages.
The technique
generalises
to
break statements,
early returns,
and
case dispatch
without
substantive modification.
Article A195
covers
the second
foundational technique
of the trio,
namely
declare-before-use ordering
and
forward declarations
for
mutual recursion,
which
together
with
the fixup mechanism
close
the
forward-reference problem
at the identifier level.

## References

### Book

- [*Project Oberon, The Design of an Operating System and Compiler*][book_wirth_project_oberon], Niklaus Wirth and Jürg Gutknecht, revised edition 2013
- [*Compiler Construction*][book_wirth_compiler_construction], Niklaus Wirth, Addison-Wesley, 1996

[book_wirth_project_oberon]: https://people.inf.ethz.ch/wirth/ProjectOberon/
[book_wirth_compiler_construction]: https://en.wikipedia.org/wiki/Compiler_Construction_(Wirth_book)

### Reference

- [WebAssembly single-pass validator and its fixup structure][ref_webassembly]
- [Backpatching in the classical compiler-construction tradition][ref_backpatching]

[ref_webassembly]: https://en.wikipedia.org/wiki/WebAssembly
[ref_backpatching]: https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series
- [Block-Structured Control Flow and Single-Pass Validation][related_post_block_structured], article A192 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
[related_post_block_structured]: {% post_url 2026-04-10-block_structured_single_pass_validation %}

### Research

- [Haas and colleagues, Bringing the Web up to Speed with WebAssembly, PLDI 2017][research_haas_webassembly]

[research_haas_webassembly]: https://dl.acm.org/doi/10.1145/3062341.3062363
