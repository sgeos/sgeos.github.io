---
layout: post
mathjax: true
comments: true
title:  "Declare-Before-Use and Forward Declarations"
date:   2026-04-13 09:00:00 +0000
categories: compilers streaming series
---

<!-- A195 -->
<script>console.log("A195");</script>

The fixup mechanism
of article A194
solves
the forward-jump problem
at the machine-code level.
A parallel problem
appears
at the identifier level.
When a source program
references
a function,
a type,
or a variable
before
the referenced entity
has been declared
in the source text,
the compiler
faces
the same question
that
the forward-jump problem
posed.
How can the compiler
emit code
that
references
an identifier
whose meaning
is not yet known?

Two solutions
are possible.
The first solution
is
to defer
identifier resolution
until
the whole program
has been parsed,
at which point
all identifiers
are known
and
all references
can be resolved.
This is
the multi-pass discipline.
It admits
forward references
freely
at the source level
and pays
the cost
in
whole-program state
and
non-linear compilation
that
article A189 discussed
as
the boundary between
single-pass and multi-pass
architectures.

The second solution
is
to require
the source language
to declare
every identifier
before
it is used.
The compiler
that reads
the source
in a single forward pass
finds
each identifier
already in
its symbol table
by the time
the identifier's use
appears.
Forward identifier references
are
syntactically forbidden.
This is
the declare-before-use
discipline
that
Wirth adopted
across his language line
and that
this article
develops
as
the second technique
of the trio.

## Declare-Before-Use as a Language Design Rule

The declare-before-use rule
states
that
every identifier
used in
a source expression
must have been
declared
at
an earlier point
in
the source file.
The rule
applies
uniformly
to
types,
constants,
variables,
functions,
procedures,
and modules.
The rule
is
a
lexical property
of the source text,
not
a semantic property
of the compiled program.
A program
that
uses
an identifier
whose declaration
appears later
in the source
is
rejected
at compile time
regardless of
whether
the program
would compute
a correct result
if the compiler
could resolve
the reference.

The rule
has two variants.
The strict variant,
applied
in
Wirth's Pascal and Modula-2,
requires
that
the declaration
precede
the use
in
the source file's
top-to-bottom order.
The scoped variant,
applied
in
some later languages,
requires
that
the declaration
precede
the use
within
the current lexical scope
but permits
outer scopes
to be
extended
after
inner scopes
that reference them
are parsed.
This article
concentrates on
the strict variant
because it is
the version
that most
directly enables
single-pass compilation.

## Why Declare-Before-Use Enables Single-Pass Compilation

At any point $i$
in
the source text,
the compiler
maintains
a symbol table
$T_i$
containing
all identifiers
that have been declared
in the source
up to position $i$.
The current-scope
symbol table
grows
monotonically
at the top level
as the compiler
advances through
the source.
Formally,
for positions $i$
inside
the outermost scope,

$$
T_i \subseteq T_{i+1}
\qquad \text{for all } i.
$$

Inside nested scopes,
the symbol table
grows
and shrinks
as
inner scopes
open and close.
Article A196
describes
the scope-popping discipline
that
returns
the nested-scope portion
to
the enclosing scope's state
whenever
an inner block closes.
The monotonic growth
of this article
applies to
the outermost scope,
which
holds
top-level declarations
and
does not
pop
during compilation.

The declare-before-use rule
states
that
every identifier
used
at position $i$
is
already in
$T_i$.
The compiler
resolves
the reference
by
looking up
the identifier
in $T_i$.
Identifier resolution
therefore
requires
only
the current symbol table state,
not
future symbol table state.
Formally,

$$
\operatorname{resolve}(\text{id}, i)
= \operatorname{lookup}(\text{id}, T_i).
$$

The resolution cost
is
the cost of
the lookup operation,
which
depends on
the symbol table's
data structure

$$
C_{\text{resolve}}(\text{id}, i) =
\begin{cases}
O(1) & \text{hash-indexed table,} \\
O(\log \lvert T_i \rvert) & \text{tree-indexed table.}
\end{cases}
$$

The lookup
does not
require
inspecting
any code
past position $i$.
The compiler
does not
maintain
any
whole-program state
to support
identifier resolution.

The alternative,
under which
forward references
are allowed
at the source level,
requires
the compiler
to
either
defer resolution
until
a whole-program pass
completes
or
maintain
a
pending-reference queue
that
is checked
at each new declaration.
Both alternatives
add
whole-program state
and increase
per-identifier cost.
Neither alternative
is compatible with
the strict
stream-processor discipline
that
this series develops.

## Forward Declarations for Mutual Recursion

The declare-before-use rule
has
one immediate consequence
that
Wirth's languages
address
through
a syntactic escape hatch.
Two procedures
that
call each other
mutually recursively
cannot both
satisfy
declare-before-use.
At least one call
must precede
the callee's declaration.

Wirth resolved this
by requiring
an explicit
forward declaration
that
introduces
the procedure's signature
into
the symbol table
before
the procedure body appears.
The syntax
in Pascal
uses the keyword
`forward`
in place of
the procedure body.
The compiler
treats the forward declaration
as
a promise
that
the body
will appear later
in the source.

The forward-declared procedure
occupies
one entry
in the symbol table
starting at
the position
of the forward declaration.
The full body,
when it appears,
does not add
a new symbol table entry.
It resolves
the forward declaration
by
providing
the compiled code
for the promised body.

Formally,
the symbol table
entry for
a forward-declared procedure
carries
a status flag
that
distinguishes
the two states.

$$
T_i(\text{id}) \in \{\text{forward-declared}, \text{defined}\}.
$$

The status transitions
at
the point
the body appears.
A call site
that
uses the identifier
during
the forward-declared phase
generates
a code emission
that
references
the procedure's future address
through
the same fixup mechanism
that
article A194
developed
for
forward jumps.

## A Worked Example, Mutual Recursion in Pascal

Consider two procedures
$P$ and $Q$
that call each other
mutually.
The Pascal code
uses
a forward declaration
to
satisfy
declare-before-use.

```pascal
PROCEDURE Q(x: integer); FORWARD;

PROCEDURE P(x: integer);
BEGIN
  IF x > 0 THEN
    Q(x - 1)
END;

PROCEDURE Q(x: integer);
BEGIN
  IF x > 0 THEN
    P(x - 1)
END;
```

The compiler processes
this source
in four phases.

**Phase 1: forward declaration of Q.**
The compiler
parses
`PROCEDURE Q(x: integer); FORWARD;`
and adds
the symbol table entry

$$
T_1(\text{Q}) = (\text{forward-declared}, \text{signature}: \text{integer} \to \text{unit}).
$$

The entry
carries
the procedure's signature
but no
compiled address yet.
The address
will be
supplied
when the body appears.

**Phase 2: body of P.**
The compiler
parses the body of $P$.
Inside the body,
the call `Q(x - 1)`
looks up
$Q$
in the symbol table
and finds it
in
the forward-declared state.
The compiler
emits
a `call` instruction
with
a placeholder
for
$Q$'s eventual address
and
adds
a fixup entry
for
this placeholder.
At the end of
$P$'s body,
$P$ receives
its own
symbol table entry
in the defined state.

**Phase 3: body of Q.**
The compiler
parses the body of $Q$.
The call `P(x - 1)`
looks up
$P$
in the symbol table
and finds it
in
the defined state
because $P$
was compiled
in phase 2.
The `call` instruction
receives
$P$'s known address
directly,
with no
fixup entry needed.
At the end of
$Q$'s body,
the compiler
resolves
$Q$'s forward declaration
by
supplying
$Q$'s
now-known address.
All fixup entries
that
reference $Q$
receive
their patched addresses.

**Phase 4: end of compilation.**
The compilation completes
with
both procedures
in the defined state
and
all fixup entries
retired.

The example demonstrates
that
declare-before-use
combined with
forward declarations
handles
mutual recursion
without
any
whole-program pass.
The forward declaration
supplies
the promise
that
the identifier
will have
a defined meaning
by
the end of
the compilation unit.
The fixup mechanism
supplies
the mechanical bridge
between
the call site
that emits
the reference
and
the definition site
that eventually
supplies
the referent's address.
The two techniques
compose
naturally.

## The Programmer's Cost

The declare-before-use rule
imposes
a
non-trivial burden
on the programmer.
Source code
must be
organised
so that
declarations
appear
before uses.
For programs
with
substantial cross-referencing
between
procedures
or types,
the ordering
is not
always
obvious.
Programmers
must
either
plan
the source layout
carefully
or
use
forward declarations
liberally.

The Wirth tradition
argued
that
the discipline
was itself
a
design benefit.
A source file
that
respects
declare-before-use
reads
naturally
from
top to bottom.
Every reference
resolves
against
material that
the reader
has already
encountered.
The reader
never needs
to
scan forward
to find
a definition.
The argument
holds
some empirical weight
for
academic programs
and
for
carefully organised
industrial code.
The argument
holds
less weight
for
rapidly evolving
industrial code
where
programmer time
dominates
compiler time.

Modern languages
have varied
in
their response
to
this trade-off.
Some languages,
including
Pascal,
Modula-2,
Oberon,
and
older C dialects,
maintain
the strict discipline.
Others,
including
Java,
Python,
Go,
and
modern C dialects
with
appropriate
forward declarations,
allow
scoped forward references
within
compilation units.
Still others,
including
early
functional languages
like ML
and
Haskell,
require
explicit
`let rec`
or equivalent
constructs
for
mutually recursive definitions
but
otherwise
follow
the declare-before-use rule.

## Interaction with Fixup Tables

Declare-before-use
and
fixup tables
together
form
the essential pair
of techniques
that
single-pass compilers
use
to handle
forward references.
Fixup tables
handle
forward references
to
code addresses.
Declare-before-use
handles
forward references
to
identifiers.
The forward-declaration escape hatch
bridges
the two mechanisms
by
allowing
an identifier
to be
introduced
into the symbol table
before
its
code address
is known,
and
using
the fixup mechanism
to
resolve
the code address
when
the body appears.

Formally,
if $\iota$
is
an identifier
declared as forward
at position $p_1$
and defined at position $p_2$
with $p_1 < p_2$,
then
between positions $p_1$
and $p_2$,
each use of $\iota$
at position $i$
generates
a fixup entry
with target identity $\iota$,

$$
T_i(\iota) = \text{forward-declared}
\implies F' = F \cup \{(a_i, \iota)\},
$$

where
$a_i$
is
the placeholder position
in the emitted output
for the reference at $i$.
At position $p_2$,
when
the body of $\iota$
completes emission,
the compiler
resolves
all fixup entries
whose target identity is $\iota$
against
the body's start address,

$$
\operatorname{resolve}(\iota, a_{\iota\text{-body}})
\quad \text{at position } p_2,
$$

and
the symbol table entry
transitions
to the defined state.

The composition
of
the two mechanisms
handles
mutual recursion
in
strict
single-pass
compilation
without
either
whole-program state
or
non-linear
compilation cost.

## Modern Language Choices

Contemporary language designers
face
the same trade-off
that
Wirth encountered.
Strict
declare-before-use
enables
single-pass compilation
and
simple compiler implementation
at the cost of
programmer flexibility
in
source organisation.
Free forward references
give
the programmer
freedom
at the cost of
compiler complexity
and
compilation-cost linearity.

Several
contemporary languages
have adopted
positions
between
the two extremes.

**Go**
requires
declare-before-use
within
a single function body
but
permits
forward references
between
top-level declarations
in
the same package.
The Go compiler
performs
a preliminary pass
over
the top-level declarations
to collect
identifier signatures,
then
compiles
the bodies
in
a subsequent pass
that
resolves references
against
the collected signatures.
The overall shape
is
cheaper than
a full multi-pass architecture
because
the preliminary pass
does not
need
to
type-check bodies
or
emit code.

**Rust**
allows
forward references
freely
within
a module.
The compiler
performs
name resolution
as a distinct phase
before
type checking
and
code generation.
Rust's compilation model
does not
attempt
strict single-pass
compilation.

**Zig**
permits
declaration order
to be
arbitrary
within
a container.
Compile-time evaluation
uses
lazy evaluation
with
dependency tracking,
so that
a compile-time expression
is evaluated
only when
its result
is needed
and
after
any expressions
it depends on
have completed.
Runtime code
is
compiled
after
compile-time evaluation completes
for
the declarations
it depends on.

**WebAssembly**
at
the bytecode level
uses
a
declare-signatures-before-any-body
discipline.
Every function reference
in
a WebAssembly module
uses
a function index
that must
be
statically resolvable.
The binary format
places
the function-index space
in
sections
that precede
the code section,
so
all function signatures
are known
before
any function body
is
verified or compiled.
Forward references
between functions
are resolved
through
the function index space,
which is
established
before
any function body
is
compiled.
This is
a
specific form of
the declare-before-use rule
adapted to
the requirements of
a portable
bytecode format.

## Header Files and Separate Compilation

The declare-before-use discipline
extends
across
compilation-unit boundaries
through
the mechanism of
declaration files.
In C and C-plus-plus,
declaration files
carry
the header extension
and contain
declarations
without
implementations.
A source file
that
uses
symbols
defined in
another compilation unit
includes
the declaration file
for that unit,
which
introduces
the symbol declarations
into
the current compilation unit's
symbol table
before
the uses appear.

Modula-2 formalised
this discipline
through
the definition-implementation module split.
A Modula-2 module
consists of
a definition module
and
an implementation module.
The definition module
contains
the exported declarations,
which is
what
importing modules see.
The implementation module
contains
the bodies.
The two modules
are separate files
and
can be compiled
independently.
The importer's compilation
depends only on
the definition module,
not on
the implementation module,
which
allows
the importer's compilation
to proceed
before
the exporter's implementation
is complete.

Oberon inherited
this discipline
in
a simpler form
through
the exported-marker convention.
A single module file
contains
both declarations
and implementations,
and
exports
are marked
with
a
single asterisk
after
the exported identifier.
The compiler,
when
importing a module,
scans
the exported declarations
without
reading
the implementations.
The imported module's
declarations
appear
in
the importing module's
symbol table
before
any use.

Modern module systems
in
Rust,
Zig,
and
recent C-plus-plus modules
continue
this pattern.
Each module
publishes
a
declaration interface
that
importing modules see.
The interface
supports
declare-before-use
across
module boundaries
without
requiring
the importer
to have
access to
the exporter's implementation.

## Conclusion

Declare-before-use
is
the language-design lever
that
brings
identifier resolution
into
the single-pass
discipline.
The rule
requires
the source
to
declare
every identifier
before
its use,
which reduces
identifier resolution
to
a lookup
in
the current symbol table.
Forward declarations
provide
the syntactic escape hatch
that
allows
mutual recursion
without
compromising
the rule.
The combination
of
declare-before-use,
forward declarations,
and
the fixup mechanism
of article A194
handles
every
forward reference
that
a block-structured
source language
admits,
without
requiring
whole-program state
or
non-linear compilation cost.
Article A196
covers
the third technique
of the trio,
namely
the symbol table
data structure itself
and
the scope-popping
discipline
that
keeps
the compiler's
working memory
bounded.

## References

### Book

- [*Compiler Construction*][book_wirth_compiler_construction], Niklaus Wirth, Addison-Wesley, 1996
- [*Project Oberon, The Design of an Operating System and Compiler*][book_wirth_project_oberon], Niklaus Wirth and Jürg Gutknecht, revised edition 2013

[book_wirth_compiler_construction]: https://en.wikipedia.org/wiki/Compiler_Construction_(Wirth_book)
[book_wirth_project_oberon]: https://people.inf.ethz.ch/wirth/ProjectOberon/

### Reference

- [Pascal programming language declaration ordering][ref_pascal]
- [Modula-2 definition and implementation module split][ref_modula2]
- [Go language declaration ordering][ref_go]
- [Rust name resolution model][ref_rust]
- [Zig compile-time ordering][ref_zig]

[ref_pascal]: https://en.wikipedia.org/wiki/Pascal_(programming_language)
[ref_modula2]: https://en.wikipedia.org/wiki/Modula-2
[ref_go]: https://en.wikipedia.org/wiki/Go_(programming_language)
[ref_rust]: https://en.wikipedia.org/wiki/Rust_(programming_language)
[ref_zig]: https://en.wikipedia.org/wiki/Zig_(programming_language)

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series
- [Fixup Tables and the Forward-Jump Problem][related_post_fixup_tables], article A194 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
[related_post_fixup_tables]: {% post_url 2026-04-12-fixup_tables_forward_jump_problem %}
