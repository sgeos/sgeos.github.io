---
layout: post
mathjax: false
comments: true
title: "Information-Flow Control, A Deep Dive with Keleusma"
date:   2026-05-29 09:00:00 +0000
categories: security rust programming
series: truthful_machines
series_title: Truthful Machines
series_index: 3
---
<!-- A111 -->
<script>console.log("A111");</script>

Most programmers have met access control.
A file has permissions, a database row has an owner,
an endpoint checks a token.
Access control answers one question,
namely who is allowed to read a piece of data.
It says nothing about a second question
that matters just as much,
namely where that data is allowed to go
after an authorized party has read it.
A function that is permitted to read a password
is not thereby permitted to write that password
into a log file, a response body, or an analytics event.
Governing that second question is the job of
[information-flow control][ref_taint], or IFC,
and it is a tool most working programmers have never used.

This article is a deep dive.
It covers the theory of IFC from the ground up,
then explains what a first-class language feature
can do that the usual alternatives cannot,
and ends with a mechanical section
on doing the heavy lifting in
[Keleusma][kel_github],
a total functional language whose 0.2.0 release
makes information-flow labels part of the type system.
The Keleusma examples were run with the version
shown in the Software Versions section,
and the output shown is the actual output.
A getting-started tour of the language is available in
[a companion article][related_post_keleusma_020],
and a worked use of IFC as a governance gate appears in
[the control-kernel article][related_post_control_kernel].

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-05-29 09:00:00 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 25.5.0: Mon Apr 27 20:38:56 PDT 2026; root:xnu-12377.121.6~2/RELEASE_ARM64_T6000 arm64

# Keleusma
$ keleusma --version
keleusma 0.2.0
```

## The Theory

### Access Control Stops at the Door

Access control is a gate at the door.
It decides whether a principal may read or write a resource.
Once the principal is inside with the data in hand,
access control has nothing more to say.
The data can be copied, transformed, combined with other data,
and written anywhere the principal can write.
The classic failure is the program that is authorized
to read a secret and also authorized to write a public channel,
and that, through a bug, copies the one into the other.
No access-control check is violated.
The leak happens entirely on the authorized side of the gate.

Information-flow control governs the propagation of data
rather than the act of reading it.
It tracks where information goes,
and it enforces a policy on the paths data may take
from its sources to its sinks.

### Labels and the Lattice

The foundational model is due to
[Dorothy Denning (1976)][research_denning_lattice].
Each piece of data carries a security class, or label,
and the labels form a lattice,
a partial order with a least upper bound for any pair.
A simple lattice has two points,
public below secret.
A realistic system has many,
one per compartment or category of sensitivity,
and the order captures which classes are more restrictive.
The rule of secure flow is then stated on the lattice.
Information may flow from a lower class to an equal or higher class,
never from a higher class to a lower one.
Combining two values yields a value
labelled with the least upper bound of their labels,
so a computation that touches a secret produces a secret.
[Denning and Denning (1977)][research_denning_certification]
showed that a compiler could certify these flows mechanically.
[Lattice-based access control][ref_lattice_ac]
is the same lattice applied to the access question.

### Noninterference

The formal goal that IFC aims at is
[noninterference][ref_noninterference],
introduced by [Goguen and Meseguer (1982)][research_goguen_noninterference].
A system is noninterfering when its public outputs
do not depend on its secret inputs.
Vary the secret inputs however you like,
and an observer of the public outputs sees no difference.
If that holds, no information about the secrets
can be inferred from the public behavior,
which is exactly the confidentiality property wanted.
Noninterference is the yardstick against which
an information-flow mechanism is judged sound.

### Explicit and Implicit Flows

There are two ways information moves,
and the second is the one that catches people out.
An explicit flow is a direct assignment of data,
copying a secret into a public variable.
An implicit flow carries information through control flow.
Branch on a secret, and the path taken reveals something about it,
so any public value written differently on the two branches
leaks a bit of the secret without ever copying it directly.
The work of
[Volpano, Smith, and Irvine (1996)][research_volpano]
recast Denning's analysis as a type system
and proved that a well-typed program is noninterfering,
which requires accounting for both kinds of flow.
The survey by
[Sabelfeld and Myers (2003)][research_sabelfeld_survey]
is the standard map of the field that grew from this.

### Static Versus Dynamic Enforcement

An information-flow policy can be enforced at run time
or before the program runs.
Dynamic enforcement, the family that includes
[taint tracking][ref_taint],
attaches a taint bit to values as the program executes
and checks it at sinks.
Static enforcement, the language-based approach,
encodes labels in the type system
and rejects an offending program at compile time.
[Jif][ref_jif], the information-flow extension of Java
built on the decentralized label model of
[Myers and Liskov][research_myers_dlm],
is the best-known static system.
Keleusma is a static, type-based system in this lineage.

### Declassification

A policy of pure noninterference is too strict to be useful.
A password checker must reveal one bit,
namely whether the password matched.
A statistics service must reveal an aggregate
computed from private records.
Every real system deliberately releases some information,
and the controlled release is called declassification.
Declassification is also the dangerous part,
because it is the one place the noninterference guarantee is broken on purpose,
and an attacker who can influence it can widen the leak.
[Sabelfeld and Sands (2009)][research_declassification]
organized the question into dimensions,
namely what is released, who releases it,
where in the system, and when.
A sound IFC design makes declassification rare, explicit, and auditable.

A first Keleusma example shows a labelled value.
The operator `classify` attaches a label,
written after the value with an `@`.

```keleusma
fn main() -> Word@Master {
    classify 42@Master
}
```

```sh
$ keleusma run 01_classify.kel
42
```

`Word@Master` is a `Word` carrying the label `Master`.
In the lattice, an unlabelled value is the public bottom,
and adding a label moves up to a more restrictive class.
The label exists only during checking.
It is erased before the program runs and costs nothing at run time.

## What First-Class IFC Can Do That Other Approaches Cannot

A team that wants to control information flow today
reaches for one of a few tools.
Each falls short in a way a first-class language feature does not.

### It Catches Implicit Flows

Taint-tracking libraries, the most common approach,
follow explicit flows well.
They tend to miss implicit flows,
because tracking information through control flow at run time
is expensive and is often skipped.
A type-based system checks every path at compile time.
Here a public output is computed on two branches
selected by a secret, an implicit flow that copies nothing.

```keleusma
fn broadcast(x: Word) -> Word {
    x
}

fn main() -> Word {
    let secret = classify 1@Master;
    let derived = if secret > 0 { 100 } else { 200 };
    broadcast(derived)
}
```

```sh
$ keleusma run 04_implicit.kel
error: compile: 8:15: type error: argument to `broadcast` expects Word, got Word@Master
```

The comparison `secret > 0` produces a labelled boolean,
the `if` over a labelled condition produces a labelled result,
and the attempt to broadcast that result is rejected
before the program runs.
A label in Keleusma is not a fence at a single point.
It is a dye that stains every value derived from a labelled one,
through arithmetic, comparison, and branching alike.

### It Costs Nothing at Run Time

Dynamic taint tracking pays for itself on every operation,
carrying and checking taint bits as the program runs.
Keleusma labels are part of the type
and are erased after checking,
so the running program is identical to one written without labels.
The guarantee is bought entirely at compile time.

### It Cannot Be Bypassed by Convention

A common lightweight approach wraps secret data in a newtype,
a `Secret<T>` that the type checker will not let you pass
where a plain `T` is expected.
This stops one mistake, the direct substitution,
but the protection ends the moment the value is unwrapped.
A newtype tracks nothing through a value derived by unwrapping,
computing, and rewrapping, and nothing through control flow.
It is a fence at the wrapper boundary, not a property of the data.
A first-class label propagates through the computation,
so the only way out is the explicit release operator,
not an unwrap method that any caller can invoke.

### It Makes Every Release Auditable

Manual code review and scattered sanitization
depend on a human noticing every path.
Humans miss implicit flows and derived leaks reliably.
With a first-class feature, the release of confidential data
happens at exactly one operator, `declassify`,
and a reviewer finds every release by searching for that one word.

```keleusma
fn broadcast(x: Word) -> Word {
    x
}

fn main() -> Word {
    let take = classify 42@Master;
    broadcast(declassify take@Master)
}
```

```sh
$ keleusma run 03_declassify.kel
42
```

Remove the `declassify`, and the same program is rejected,
because the labelled value reaches a plain `Word` parameter.

```sh
$ keleusma run 02_leak.kel
error: compile: 7:15: type error: argument to `broadcast` expects Word, got Word@Master
```

The contrast with access control is worth restating.
Access control would have permitted both the read and the write.
The leak is on the authorized side of the gate,
and only a flow-aware check sees it.

## The Mechanical Section

This section is the working reference
for doing IFC heavy lifting with the Keleusma grammar.
The [information-flow chapter of the guide][kel_guide_ifc]
covers the same surface for the script author.

### Attaching a Label

`classify expr@Label` adds a label to a value.
Adding a label only tightens flow restrictions,
so it is always admitted.
A label set is written in braces,
and the empty set is the public bottom of the lattice.

```keleusma
fn store(x: Word@{Secret, Pii}) -> Word@{Secret, Pii} {
    x
}

fn main() -> Word@{Secret, Pii} {
    let record = classify 7@{Secret, Pii};
    store(record)
}
```

```sh
$ keleusma run 05_label_set.kel
7
```

`Word@{Secret, Pii}` carries two labels.
The labels are user-defined names, and their meaning is the programmer's.
More labels mean a more restrictive class,
which is the powerset lattice of the chosen label names.

### Labels Ride on Types and Propagate

A label is part of the type, written `T@Label`.
The type checker propagates it through operations,
so the result of any expression that touches a labelled value
is itself labelled, as the implicit-flow example showed.
This is what makes the guarantee hold without the programmer
threading the label through by hand.

### Boundaries Are Where Flow Is Checked

A flow is checked when a value crosses a boundary.
The boundaries are function parameter and return types,
`shared` data fields that the host reads and writes,
and `private` data fields that survive across a yield and resume.
A plain `Word` parameter accepts only an unlabelled `Word`,
so handing it a `Word@Master` is the rejected leak seen above.
Declaring a parameter or return with a label
states the policy at that boundary directly.

### Releasing a Label

`declassify expr@Label` removes a label.
It is always admitted, but it is the one visible point
where confidential data is released,
and it is the place a review process must scrutinize,
consistent with the dimensions of
[Sabelfeld and Sands][research_declassification].
Keep declassification rare and push it to a single chokepoint.
A label set is released the same way,
naming the labels to remove.

### Negative Labels at Boundaries

The positive label says what a value carries.
The negative label, written with a `!` prefix,
says what a boundary refuses.
A parameter typed `Word@!Secret` accepts any value
that does not carry the `Secret` label.

```keleusma
fn publish(x: Word@!Secret) -> Word {
    x
}

fn main() -> Word {
    let value = classify 5@Public;
    publish(value)
}
```

```sh
$ keleusma run 06_negative.kel
5
```

A value that does carry the forbidden label is rejected,
with a diagnostic that names the offending label.

```sh
$ keleusma run 06b_negative_reject.kel
error: compile: 7:13: type error: argument 1 to `publish` carries the label `Secret` which the parameter's `!`-prefix declaration forbids
```

Negative labels are admitted only at boundary positions,
namely function parameters and returns and the `shared` and `private`
data fields, and only at the top level of a type,
not nested inside a tuple, array, or option.
A single position may not mix positive and negative labels.
Negative labels are a boundary clause rather than a propagating type,
so unlike positive labels they do not stain derived values.

### A Working Pattern

The pattern that does most of the work is small.
Classify confidential data at its source.
Let the labels propagate untouched through the computation.
Type every output boundary so it refuses the labels,
either by leaving the boundary unlabelled
so it accepts only public data,
or by giving it a negative label that names what it forbids.
Release through a single `declassify` at one reviewed chokepoint.
The compiler then proves, before the program runs,
that no other path carries confidential data to an output.

## Honest Limitations

A few boundaries of the Keleusma model are worth stating plainly.
The labels are user-defined and abstract.
The language enforces the lattice discipline,
but the meaning of each label, and whether it models
confidentiality or integrity, is a convention the programmer supplies.
Positive labels propagate through values,
including through branches, which is the strong part.
Negative labels are checked only at boundaries
and do not propagate through derived values in the 0.2.x line,
so they express what a position refuses rather than tracking absence
through a computation.
And declassification remains trusted.
The compiler guarantees that release happens only at a `declassify`,
but it cannot judge whether a given release is wise.
That judgment is the reviewer's,
which is the reason the operator is made so visible.

## Conclusion

Information-flow control answers a question access control cannot,
namely where data may go after it is read.
The theory is fifty years old,
from Denning's lattice through noninterference
to the language-based type systems that enforce it,
yet it remains absent from most working programmers' toolkits.
A first-class language feature catches the implicit flows
that taint libraries miss, costs nothing at run time,
cannot be bypassed by unwrapping a value,
and reduces every release of a secret to one auditable keyword.
Keleusma 0.2.0 puts that feature in the type system,
where the guarantee is proved before the program runs.

## References

- [Reference, Jif, Java Information Flow][ref_jif]
- [Reference, Lattice-Based Access Control][ref_lattice_ac]
- [Reference, Noninterference, Security][ref_noninterference]
- [Reference, Taint Checking][ref_taint]
- [Keleusma, GitHub Repository][kel_github]
- [Keleusma, Guide Chapter 24, Information-Flow Labels][kel_guide_ifc]
- [Related Post, A Verifiable Control Kernel in Keleusma][related_post_control_kernel]
- [Related Post, Getting Started with Keleusma 0.2.0][related_post_keleusma_020]
- [Research, Certification of Programs for Secure Information Flow][research_denning_certification]
- [Research, Declassification, Dimensions and Principles][research_declassification]
- [Research, Language-Based Information-Flow Security][research_sabelfeld_survey]
- [Research, A Lattice Model of Secure Information Flow][research_denning_lattice]
- [Research, Protecting Privacy Using the Decentralized Label Model][research_myers_dlm]
- [Research, Security Policies and Security Models][research_goguen_noninterference]
- [Research, A Sound Type System for Secure Flow Analysis][research_volpano]

[ref_jif]: https://www.cs.cornell.edu/jif/
[ref_lattice_ac]: https://en.wikipedia.org/wiki/Lattice-based_access_control
[ref_noninterference]: https://en.wikipedia.org/wiki/Non-interference_(security)
[ref_taint]: https://en.wikipedia.org/wiki/Taint_checking
[kel_github]: https://github.com/sgeos/keleusma
[kel_guide_ifc]: https://github.com/sgeos/keleusma/blob/main/docs/guide/24_information_flow_labels.md
[related_post_control_kernel]: {% post_url 2026-05-27-verifiable_control_kernel_in_keleusma %}
[related_post_keleusma_020]: {% post_url 2026-05-28-keleusma_0_2_0_getting_started %}
[research_denning_certification]: https://dl.acm.org/doi/10.1145/359636.359712
[research_declassification]: https://www.cse.chalmers.se/~andrei/sabelfeld-sands-jcs07.pdf
[research_sabelfeld_survey]: https://www.cs.cornell.edu/andru/papers/jsac/sm-jsac03.pdf
[research_denning_lattice]: https://dl.acm.org/doi/10.1145/360051.360056
[research_myers_dlm]: https://www.cs.cornell.edu/andru/papers/iflow-tosem.pdf
[research_goguen_noninterference]: https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf
[research_volpano]: https://people.mpi-sws.org/~dg/teaching/lis2014/modules/ifc-1-volpano96.pdf
