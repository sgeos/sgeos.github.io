---
layout: post
mathjax: true
comments: true
title:  "Symbol Tables, Scope Popping, and Bounded Working Memory"
date:   2026-04-14 09:00:00 +0000
categories: compilers streaming series
---

<!-- A196 -->
<script>console.log("A196");</script>

The symbol table
is
the third
foundational technique
of the single-pass
compilation discipline.
Articles A194 and A195
developed
the fixup mechanism
that
handles
forward references
to
code addresses
and
the declare-before-use rule
that
handles
forward references
to
identifiers.
Both mechanisms
depend on
a specific
data structure
in
the compiler,
namely
the symbol table
that
holds
the identifiers
currently visible
to
the parser.
This article
develops
the symbol table
in
the specific form
that
supports
the single-pass discipline,
argues
why
scope-based popping
keeps
the compiler's
working memory
bounded
by
source nesting depth
rather than
program size,
and shows
how
the discipline
interacts with
the other
techniques
of the trio.

The single-pass discipline
requires
that
the compiler
hold
at most
the identifiers
visible in
the current scope stack.
Identifiers
declared
in
scopes
that have closed
are not
carried forward.
Identifiers
declared
in
scopes
that have not yet opened
have not
appeared yet.
The symbol table's
size
at any point
depends on
the current
scope stack,
not on
the total number
of identifiers
in the program.

## Scoping as a Stack Discipline

A block-structured source language
introduces
a new lexical scope
at each
scope-opening construct.
Scope-openers
include
function definitions,
procedure definitions,
block statements,
`begin` and `end` pairs,
and any other
construct
that admits
local declarations
that
should not leak
to
the enclosing context.

Each scope opener
pushes
a new empty scope
onto
a scope stack.
Each scope closer
pops
the current scope
off the stack,
discarding
all identifiers
declared
within it.
The scope stack
is
therefore
a stack
in
the strict data-structure sense,
with
scope openers
as push operations
and
scope closers
as pop operations.

The current symbol table
is
the concatenation
of
all scopes
currently on
the stack.
Formally,
if
the scope stack
at position $i$
is
$[S_1, S_2, \ldots, S_d]$
where $S_1$
is
the outermost scope
and
$S_d$
is
the innermost scope
of nesting depth $d$,
then
the symbol table
at position $i$
is

$$
T_i = S_1 \sqcup S_2 \sqcup \cdots \sqcup S_d,
$$

where
$\sqcup$
denotes
the merging operation
that combines
scopes
into
a single lookup table
with
the innermost scope
taking precedence
for
identifier lookups.

The merging operation
is
not
necessarily
implemented
as
an actual concatenation
in
the data structure.
Different implementation choices,
which
the *Implementation Choices*
section below discusses,
achieve
the same
logical
merging behaviour
through
different
concrete data structures.
The abstract shape
of
the symbol table
is
what matters
for
the working-memory bound.

## The Symbol Table Operations

The symbol table
supports
four operations.

**Enter scope.**
When
a scope opener
is recognised,
the compiler
pushes
an empty scope
onto
the scope stack.
Formally,

$$
\text{enter-scope}: [S_1, \ldots, S_d] \mapsto [S_1, \ldots, S_d, \emptyset].
$$

The new scope
starts empty.
As
the compiler
recognises declarations
inside
the new scope,
each declaration
adds
a new identifier
to
the top-of-stack scope.

**Exit scope.**
When
the corresponding scope closer
is recognised,
the compiler
pops
the top-of-stack scope
and discards it,
along with
all
identifiers
declared inside.
Formally,

$$
\text{exit-scope}: [S_1, \ldots, S_d] \mapsto [S_1, \ldots, S_{d-1}].
$$

The popped scope
is
not retained
in
any auxiliary data structure.
The memory
that
held
its identifiers
is
freed
for
reuse
by
subsequent
scopes.

**Declare identifier.**
When
a declaration
is recognised,
the compiler
adds
the identifier
to
the top-of-stack scope.
Formally,

$$
\text{declare}(\text{id}, e):
[S_1, \ldots, S_d] \mapsto [S_1, \ldots, S_d \cup \{(\text{id}, e)\}],
$$

where
$e$
is
the identifier's
symbol-table entry
containing
its type,
address,
or
other
attributes.

**Lookup identifier.**
When
a reference to
an identifier
is parsed,
the compiler
walks
the scope stack
from
innermost to outermost,
returning
the first
matching entry.
Formally,

$$
\operatorname{lookup}(\text{id}):
\bigcup_{k = d}^{1}
\{ (\text{id}, e) : (\text{id}, e) \in S_k \}
\quad \text{first match wins.}
$$

The innermost-first ordering
implements
the standard
lexical-scoping semantics
where
inner scopes
shadow
outer scopes.
An inner
declaration
of
an identifier
that also appears
in
an outer scope
takes precedence
inside
the inner scope
without
modifying
the outer entry.

## Memory Bounds

The symbol table
of a
single-pass compiler
following
the scope-popping discipline
has
memory bounds
that
depend only on
the source's
scope-nesting properties,
not on
the total program size.

Let
$d_{\max}$
denote
the maximum scope-nesting depth
of the source program
and
$s_{\max}$
denote
the maximum
per-scope declaration count.
Both quantities
are compile-time properties
of the source grammar
and
the specific program.
The maximum symbol table size
at any point
during compilation
is bounded by

$$
\lvert T \rvert_{\max} \le d_{\max} \cdot s_{\max}.
$$

For a
typical
block-structured language,
$d_{\max}$
is
in the tens
even for
large programs,
and
$s_{\max}$
is bounded by
the maximum
per-function
or
per-block
declaration count,
typically
in the low hundreds
for
carefully organised code.
For a concrete estimate,
using
a typical maximum nesting depth
of thirty
and a
maximum per-scope
declaration count
of two hundred,

$$
\lvert T \rvert_{\max}
\le d_{\max} \cdot s_{\max}
\le 30 \cdot 200
= 6000 \text{ entries}.
$$

At sixteen to sixty-four bytes
per entry,
depending on
the identifier length
and
the attribute payload,
the nested-scope portion
of the symbol table
occupies
several hundred kilobytes
of memory
in
the pessimistic worst case
and
substantially less
in
typical use.
The bound
on nested scopes
holds
regardless of
the source program size.

An important subtlety
distinguishes
the nested-scope portion
from
the outermost scope.
The scope-popping discipline
returns
the nested-scope working set
to
the enclosing scope's state
whenever
an inner block closes.
The outermost scope,
which
holds
top-level declarations
of
functions,
types,
constants,
and
module-level variables,
does not
pop
during compilation.
Its size
grows
monotonically
with
the number of
top-level declarations
that
the source program contains,
which is
proportional to
the source program size.

The correct
per-component bound
is therefore

$$
\lvert T \rvert
= \lvert T_{\text{nested}} \rvert
+ \lvert T_{\text{top-level}} \rvert,
$$

where
$\lvert T_{\text{nested}} \rvert = O(d_{\max} \cdot s_{\max})$
is
program-independent
under the assumption
that
$d_{\max}$
and
$s_{\max}$
are bounded
by
the source language's
grammatical constraints
or by
programming discipline,
and
$\lvert T_{\text{top-level}} \rvert = O(\lvert D_{\text{top}} \rvert)$
grows
with
the top-level declaration count
$\lvert D_{\text{top}} \rvert$.
For a
separately compiled
module language,
$\lvert D_{\text{top}} \rvert$
is
bounded per module
by the largest compilation unit
rather than
by the whole program.

The single-pass discipline
therefore
bounds
the per-declaration working set
independently of
the source program size,
while
the accumulating top-level environment
grows
with
the top-level declaration count.
The alternative,
under which
the symbol table
accumulates
all identifiers
declared anywhere
in the program
and retains
their attribute payloads
throughout
compilation,
requires
memory
linear in
the program size
with
substantially larger constants.
The multi-pass discipline
that
article A188
identified as
the counterpoint
to
the single-pass discipline
generally
takes this
alternative,
because
multi-pass compilers
build
whole-program abstract syntax trees
that
carry
their own
identifier bindings
throughout
the compilation.

## Lookup Cost and Shadowing

The lookup cost
depends on
both
the per-scope lookup cost
and
the number of
scopes
that must be walked.

For
a hash-indexed
per-scope lookup,
each scope's lookup
is
$O(1)$.
The overall lookup cost
across
the scope stack
is
therefore

$$
C_{\text{lookup}} = O(d_{\max}).
$$

For
a tree-indexed
per-scope lookup,
each scope's lookup
is
$O(\log s_{\max})$
and
the overall cost
across
the scope stack
is

$$
C_{\text{lookup, tree}} = O(d_{\max} \cdot \log s_{\max}).
$$

In practice,
most identifier references
resolve
in
the innermost few scopes
because
of
programming convention.
The average lookup cost
is
much
smaller than
the worst case.
The compiler's
overall
compilation cost
therefore
remains
linear
in
the program size
even under
the pessimistic
worst-case
lookup bound.

Shadowing
of
identifiers
across scopes
is
handled
by
the innermost-first
lookup order.
An inner declaration
of
an identifier
inserts
into
the top-of-stack scope
without
disturbing
outer entries.
When
the inner scope
exits,
the inner entry
is discarded
with
the popped scope,
and
subsequent lookups
resolve
against
the outer entry
that
was hidden
during the inner scope's
lifetime.
The mechanism
is
purely structural,
requiring
no
explicit
shadowing bookkeeping
in
the symbol table
data structure.

## A Worked Example, Nested Procedure Compilation

Consider a Pascal-style
source
with
a nested procedure declaration.

```pascal
PROGRAM Example;
VAR x: integer;

PROCEDURE Outer(a: integer);
VAR y: integer;

  PROCEDURE Inner(b: integer);
  VAR z: integer;
  BEGIN
    z := a + b + y;
    x := z
  END;

BEGIN
  y := a * 2;
  Inner(y);
  x := x + a
END;

BEGIN
  x := 0;
  Outer(x + 1)
END.
```

The compiler's scope stack
walks through
five states
during compilation.

**State 0: at the program's outer scope.**
After parsing
`PROGRAM Example`
and
`VAR x: integer`,
the scope stack is
$[S_1]$
with
$S_1 = \{x\}$.

**State 1: entering `Outer`.**
Upon entering
`Outer`'s procedure body,
the compiler
pushes
a new scope.
The scope stack becomes
$[S_1, S_2]$.
The compiler
adds
the parameter $a$
and
the local $y$
to $S_2$,
which becomes
$S_2 = \{a, y\}$.

**State 2: entering `Inner`.**
Upon entering
`Inner`'s procedure body,
the compiler
pushes
another new scope.
The scope stack becomes
$[S_1, S_2, S_3]$
with
$S_3 = \{b, z\}$.
References inside
`Inner`'s body
resolve
against
this combined table.
The reference to $a$
inside `Inner`
finds
$a$
in $S_2$,
because
$S_3$
does not
contain $a$.
The reference to $y$
finds
$y$
in $S_2$.
The reference to $x$
finds
$x$
in $S_1$.
The reference to $z$
finds
$z$
in $S_3$.

**State 3: exiting `Inner`.**
When
`Inner`'s body
finishes,
the compiler
pops
$S_3$
from
the scope stack.
The scope stack
returns to
$[S_1, S_2]$.
The identifiers
$b$
and $z$
are
no longer
visible
in
subsequent
parsing.

**State 4: exiting `Outer`.**
When
`Outer`'s body
finishes,
the compiler
pops
$S_2$.
The scope stack
returns to
$[S_1]$.
The identifiers
$a$
and $y$
are
no longer visible.

**State 5: the main program.**
After parsing
the main program body,
the compiler
pops
$S_1$
as well
when
the `END.`
of
the program
is recognised.
The scope stack
is empty
at
the end of
compilation.

At no point
during
this compilation
does
the symbol table
hold
more than
seven identifiers
total.
The maximum
occurs
during
`Inner`'s body
compilation,
where
the combined table
holds
$\{x, a, y, b, z\}$
plus
two procedure names
in the enclosing scopes.
The bound
is
independent of
the total size
of
the compilation unit.

## Interaction with the Wirth Techniques

The three
techniques of the trio,
namely
fixup tables
from
article A194,
declare-before-use
from
article A195,
and
scoped symbol tables
from
this article,
compose
to
form
the complete
single-pass
implementation
of
forward-reference handling.

The scoped symbol table
provides
the current
identifier context
against which
identifier references
resolve.
The declare-before-use rule
ensures
that
every use
finds
its declaration
in
the current symbol table
without
future lookahead.
The fixup mechanism
handles
the remaining case
where
an identifier's
declaration
exists
in
the symbol table
but
its
compiled-code address
is not yet
known,
which occurs
for
forward-declared procedures
and
mutually recursive definitions.

The three mechanisms
share
a common
structural property.
Each maintains
a
stack-shaped data structure
whose depth
is bounded by
the source's
syntactic nesting depth.
The fixup stack
in
article A194
tracks
forward jumps
per
enclosing block.
The scope stack
in
this article
tracks
identifier scopes
per
enclosing lexical scope.
The two stacks
grow and shrink together
under
the source language's
block-structured discipline,
because
scope entries
and
block entries
tend to coincide
in
Wirth-style languages.

Formally,
the total working memory
of the compiler
for
these three techniques
is bounded by
the sum

$$
M_{\text{compiler}} \le M_{\text{fixup}} + M_{\text{symtab}} + M_{\text{other}},
$$

where
$M_{\text{fixup}}$
is bounded by
the fixup-buffer nesting bound
established in
article A194,
$M_{\text{symtab}}$
decomposes as
$M_{\text{symtab}} = M_{\text{nested}} + M_{\text{top-level}}$
per the earlier section,
and
$M_{\text{other}}$
is
a small constant
covering
the parser stack,
the emission buffer,
and
other
compilation state.
The per-declaration working set
$M_{\text{fixup}} + M_{\text{nested}} + M_{\text{other}}$
is
$O(1)$
in
the program size.
The accumulating term
$M_{\text{top-level}}$
grows
with
the top-level declaration count,
which
is bounded per module
under
separate compilation.

## Implementation Choices

The abstract symbol table
described above
admits
several concrete
implementation choices.

**Linked list of hash maps.**
The most direct implementation
uses
a linked list
of
hash maps.
Each list element
represents
one scope.
The head
of the list
is
the innermost scope.
Scope entry
prepends
a new empty hash map
to
the list.
Scope exit
removes
the head element.
Lookup
walks
the list
from head to tail,
returning
the first match.
This implementation
is
simple
to write
and
easy to reason about.
The lookup cost
is
$O(d_{\max})$
in the worst case.

**Single hash map with scope IDs.**
A more efficient implementation
maintains
a single hash map
whose keys
are
identifier names
and
whose values
are
stacks
of
scope-tagged entries.
Each entry
carries
a scope ID
that
records
which
scope
declared it.
Scope entry
increments
the current scope ID
counter.
Scope exit
iterates
the hash map
and removes
all entries
whose scope ID
matches
the exiting scope.
Lookup
returns
the top-of-stack entry
for
the queried name.
This implementation
gives
$O(1)$
lookup cost
at
the cost of
slightly more complex
scope-exit accounting.

**Vector of vectors.**
The simplest
in-arena implementation
uses
a vector of vectors,
with
each inner vector
holding
the identifiers
of one scope.
Scope entry
appends
a new empty vector
to
the outer vector.
Scope exit
truncates
the outer vector.
Lookup
walks
the outer vector
from end to start
and
searches
each inner vector
linearly.
This implementation
has
$O(d_{\max} \cdot s_{\max})$
lookup cost
in
the worst case
but
uses
the minimum
memory overhead
and
is
straightforward
to implement
in
constrained environments.

The choice
among
these implementations
depends on
the compiler's
performance requirements
and
the source language's
scope characteristics.
For
most
Wirth-style languages,
where
nesting depth
is
modest
and
per-scope identifier count
is
small,
the linked-list-of-hash-maps
implementation
is
adequate.

## Modern Language Practice

Contemporary language implementations
follow
several
variants
of
the scoped symbol table.

**Interactive-development-oriented compilers.**
Compilers designed for
interactive development,
including
language servers,
tend to
maintain
whole-program
identifier information
in
richer data structures
that
support
features like
cross-file navigation,
find-usages queries,
and
incremental recompilation.
These data structures
are
larger than
the pure single-pass
symbol table
but
still
respect
the scope-based visibility rules
at compile time.
The trade-off
sacrifices
strict
single-pass
compilation
for
tooling
functionality.

**Bytecode-compilation-oriented compilers.**
Compilers designed for
producing bytecode
efficiently,
including
WebAssembly toolchains
and
embedded scripting compilers,
tend to
follow
the pure
single-pass
scoped-symbol-table discipline.
The compilation cost
matters
more than
the tooling functionality
in these contexts.
The single-pass discipline
delivers
the low compilation cost.

**Whole-program-optimisation-oriented compilers.**
Compilers designed for
maximum
run-time performance,
including
production
GNU Compiler Collection
and
Clang implementations,
use
scoped symbol tables
during
parsing and semantic analysis
but
retain
identifier information
in
a persistent
whole-program
abstract syntax tree
and
intermediate representation
beyond parse-time.
The persistent structures
enable
optimisations
across
scope boundaries
at
the cost of
compilation memory
and time.
The scope-popping discipline
of
this article
applies to
the parse-time symbol table
but not to
the persistent
whole-program structures
that
these compilers
carry forward.

The three categories
correspond
roughly to
the three
architectural quadrants
of
the two-axis design space
introduced in
article A188.
Interactive language servers
sit in
the pipeline-and-AST-materialised
quadrant.
Bytecode compilers
sit in
the integrated-or-pipeline-and-AST-free
quadrant.
Whole-program optimising compilers
sit in
the multi-pass-and-AST-materialised
quadrant.

## Conclusion

The scoped symbol table
with
the scope-popping discipline
completes
the
foundational trio
of
single-pass
compilation techniques.
The compiler's
working memory
for
identifier tracking
is
bounded by
the source's
scope-nesting depth
and
per-scope declaration count,
which are
program-independent
under
the assumption
that
these quantities
are bounded
by
the source language's
grammatical constraints
or
programming discipline.
The three techniques,
fixup tables,
declare-before-use,
and
scoped symbol tables,
compose
to
maintain
the compiler's
total working memory
at
$O(1)$
in
the program size.
Article A197
opens
the synthesis pair
of the series
with
the comparison of
integrated single-pass
against
decomposed pipeline
architectures,
using
Keleusma's V0.3.0
self-hosting roadmap
as
a modern
worked example
of
the decomposed pipeline
approach.

## References

### Book

- [*Compiler Construction*][book_wirth_compiler_construction], Niklaus Wirth, Addison-Wesley, 1996
- [*Project Oberon, The Design of an Operating System and Compiler*][book_wirth_project_oberon], Niklaus Wirth and Jürg Gutknecht, revised edition 2013

[book_wirth_compiler_construction]: https://en.wikipedia.org/wiki/Compiler_Construction_(Wirth_book)
[book_wirth_project_oberon]: https://people.inf.ethz.ch/wirth/ProjectOberon/

### Reference

- [Symbol table data structures in compiler construction][ref_symbol_table]
- [Lexical scoping in programming languages][ref_lexical_scoping]

[ref_symbol_table]: https://en.wikipedia.org/wiki/Symbol_table
[ref_lexical_scoping]: https://en.wikipedia.org/wiki/Scope_(computer_science)

### Related Post

- [Compilation as a Streaming Discipline][related_post_streaming_discipline], article A188 in this series
- [Wirth's Single-Pass Line, PL/0 through Oberon][related_post_wirth], article A189 in this series
- [Fixup Tables and the Forward-Jump Problem][related_post_fixup_tables], article A194 in this series
- [Declare-Before-Use and Forward Declarations][related_post_declare_before_use], article A195 in this series

[related_post_streaming_discipline]: {% post_url 2026-04-06-compilation_as_streaming_discipline %}
[related_post_wirth]: {% post_url 2026-04-07-wirth_single_pass_line %}
[related_post_fixup_tables]: {% post_url 2026-04-12-fixup_tables_forward_jump_problem %}
[related_post_declare_before_use]: {% post_url 2026-04-13-declare_before_use_forward_declarations %}

## Erratum

An earlier revision of this article
stated
that the symbol table's
memory footprint
was
$O(1)$ in the program size
via
the scope-popping discipline.
This was
overstated.
Scope popping
bounds
the nested-scope portion
of the symbol table
but
does not bound
the outermost scope,
which
accumulates
top-level declarations
monotonically
as the compiler
advances through the source.
The corrected framing
distinguishes
the per-declaration working set,
which
is $O(1)$
in the program size,
from
the accumulating top-level environment,
which
grows with
the top-level declaration count
and
is bounded per module
under separate compilation.
Article A195
carries
a compatible clarification
about
the monotonic growth
of
the outermost scope.
