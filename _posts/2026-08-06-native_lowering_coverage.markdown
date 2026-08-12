---
layout: post
mathjax: true
comments: true
title: "Keleusma Research Spike: Blocking Frequency as the Ordering Principle for Instruction-Set Coverage"
date: 2026-08-06 09:00:00 +0000
categories: engineering compilers verification
series: keleusma_native
series_title: Keleusma Native Code Generation
series_index: 1
---
<!-- A369 -->
<script>console.log("A369");</script>

**A compiler was 87 percent finished. It could not compile two thirds of the programs it was for.**

Both numbers are correct. The first counts individual instructions the compiler knew how to translate. The
second counts whole programs that would actually go through.
**The gap between them is what this article is about**, and the reason it exists is simple enough to state
in one sentence. **A program needs every instruction it uses, not most of them.** One missing instruction
out of a hundred stops the whole thing, exactly as one missing link stops a chain.

**That gap then destroyed a carefully reasoned plan.** One working session before the measurement was taken,
the author of this article had formally recommended what the next piece of work should be. The reasoning had
no invalid step in it. The measurement showed the recommendation to be worth nothing at all, because the
thing it would have unblocked **does not occur even once** in any program the compiler is meant to serve.
The instrument that established this took about twenty minutes to build and two seconds to run.

**The article reports that, and then reports four errors made while writing it**, all four of which ran in
the direction of a more striking result, and one of which was committed inside the paragraph warning against
the other three.

### What this is a case study of

The setting is compiler engineering, and a reader who has never written a compiler can follow the argument,
because the shape of the problem is not specific to compilers.

**The concrete project is Keleusma**, whose compiler until now has emitted bytecode for a virtual machine,
as described in [the self-hosting strategy][related_post_keleusma_self_hosting] and its
[getting-started article][related_post_keleusma_022]. **Native code generation is the step after that one**,
and it is where the ordering question first became expensive enough to measure. The lineage of the design
sits in [the stream-based compilers series][related_post_compilers_streaming] and in
[the self-hosted silicon compiler][related_post_self_hosted_silicon].
**None of that background is needed to follow what follows**, and the measurement stands on its own.

A **compiler backend** translates a program from an intermediate form into instructions a machine can run.
The intermediate form has a fixed vocabulary of operations, here 66 of them. Translating each one is
separate work. **Bringing up a backend therefore means choosing an order**, and the question of which
operation to implement next is the ordering problem this article treats.

**The ordering principle in common use ranks the remaining work by how hard each item is to build and by how tidily it fits the architecture.**
This article argues that principle is systematically wrong, and that the correct one ranks by
**measured frequency of blocking** over a representative body of real programs. The argument is empirical,
and nothing here is asserted without measurement. An instrument was built over the 58 compilable programs of
the shipped corpus, comprising 73,434 instruction instances across 496 compilation units, and the resulting
distribution is reported in full, including the negative results and confidence bounds on them.

**Anywhere a customer needs a conjunction of features rather than any one of them, the same trap is available**,
and the Pattern Extraction section at the end states it without reference to compilers.

### Seven literatures touch this problem and none of them answers it

**That absence is the gap the article fills.** Each of the following traditions has something to say about
coverage, and none supplies an ordering principle.

| Tradition | Range surveyed here |
|---|---|
| Code generation and instruction selection | [Sethi and Ullman 1970][research_sethi_ullman_1970] to [Ertl 1999][research_ertl_1999] |
| Verified and validated compilation | [Necula 1997][research_necula_1997] to [Lopes and colleagues 2021][research_lopes_2021] |
| Abstract interpretation | [Cousot and Cousot 1977][research_cousot_1977] to [Blanchet and colleagues 2003][research_blanchet_2003] |
| Worst-case resource analysis | [Liu and Layland 1973][research_liu_layland_1973] to [Wilhelm and colleagues 2008][research_wilhelm_2008] |
| Corpus-based empirical study | [Knuth 1971][research_knuth_1971] to [Ray and colleagues 2014][research_ray_2014] |
| Test adequacy and mutation | [DeMillo and colleagues 1978][research_demillo_1978] to [Inozemtseva and Holmes 2014][research_inozemtseva_holmes_2014] |
| Submodular optimisation and prioritisation | [Nemhauser, Wolsey and Fisher 1978][research_nemhauser_1978] to [Buchbinder and colleagues 2015][research_buchbinder_2015] |

**The reason none of them answers the question is the same in every case.** They all reason about
instructions, and the quantity that governs delivered capability is a property of **programs**.

## The Coverage Ordering Problem

The ordering problem for instruction-set coverage during backend bring-up is the question of which subset of
an instruction set a partial code generator should implement first, given a fixed implementation budget and
a target population of programs that the generator is intended to serve. The problem permits several
formalizations depending on the engineering tradition consulted.

The compiler-construction tradition treats the coverage property as an instruction-selection completeness
question, where the generator must eventually cover the whole instruction set and the intermediate ordering
is a matter of developer convenience. The staged-delivery tradition, in the form
[Boehm 1988][research_boehm_1988] gave it, treats the coverage property as an incremental-capability
question, in which each increment should deliver a demonstrable capability to some consumer. The
verification tradition, which is the governing tradition for the present case because the Keleusma value
proposition is definitive worst-case execution time and worst-case memory usage in the sense surveyed by
[Wilhelm and colleagues 2008][research_wilhelm_2008] and by
[Puschner and Burns 2000][research_puschner_burns_2000], treats the coverage property as a
soundness-preservation question, in the sense [Leroy 2009][research_leroy_2009] establishes for a realistic
compiler and [Pnueli and colleagues 1998][research_pnueli_1998] formulate as translation validation, in
which every implemented instruction must be shown to preserve the semantics already proven on the bytecode
artefact and every unimplemented instruction must be refused, never approximated.

The three traditions agree that the instruction set must eventually be covered in full and disagree about
the intermediate ordering. The present article adopts the verification tradition for correctness obligations
and argues that none of the three supplies an adequate ordering principle, because all three reason about
instructions in isolation while the quantity that governs delivered capability is a property of programs,
not of instructions.

### Notation

**The formal machinery below is worth the four symbols it costs, because the central result is a comparison between two averages that look interchangeable and are not.**
A reader who prefers prose can take the following and skip to the results.
**One measure averages over instructions. The other averages over programs, and that one is what a user experiences. It is far lower.**

Let $I$ denote the instruction set, with $\lvert I \rvert = 66$ in the present case. Let $S \subseteq I$ denote the
subset the generator currently lowers, with $\lvert S \rvert = 39$ at the time of measurement. Let

$$C = \{c_1, c_2, \ldots, c_M\}, \qquad M = 496$$

denote the corpus of compilation units, with each unit $c_m$ a finite sequence of instruction instances
drawn from $I$ and $\lvert c_m \rvert$ its length. Write the total instance count

$$N = \sum_{m=1}^{M} |c_m| = 73{,}434$$

and the per-unit lowered count

$$n^{\text{ok}}(c_m, S) = \bigl| \{ \iota \in c_m : \iota \in S \} \bigr|.$$

### Two coverage measures

The instruction-level coverage is the proportion of instruction instances the generator handles,

$$\rho^{\text{inst}}(S) = \frac{1}{N} \sum_{m=1}^{M} n^{\text{ok}}(c_m, S).$$

The unit-level coverage is the proportion of compilation units in which every instruction is handled.
Writing the lowerability indicator

$$\chi(c_m, S) = \prod_{\iota \in c_m} \mathbf{1}[\iota \in S] = \mathbf{1}\bigl[ n^{\text{ok}}(c_m, S) = |c_m| \bigr]$$

the unit-level coverage is

$$\rho^{\text{unit}}(S) = \frac{1}{M} \sum_{m=1}^{M} \chi(c_m, S).$$

**The product is the whole difficulty.** A sum forgives a missing term, since ninety-nine present out of a
hundred still averages to 0.99. **A product does not forgive anything**, because a single zero anywhere sets
the entire result to zero. The first measure is a sum over instructions and the second is an average of
products over programs, which is why they can differ so widely while both being correct.

The product form of $\chi$ is the whole difficulty. The generator exploits structured control flow directly,
in the sense of the structured program theorem of [Bohm and Jacopini 1966][research_bohm_jacopini_1966], so
that basic blocks fall out of the instruction stream without the control-flow-graph reconstruction
[Allen 1970][research_allen_1970] formalised, and the conjunction is therefore a property of the instruction
multiset, and no recovered graph enters into it. Lowerability is a conjunction over the unit, so a single
unimplemented instruction sets the indicator to zero regardless of how many instances were handled. The
refusal is not a defect. It is the required behaviour under the verification tradition, since a generator
that approximated an unimplemented instruction would emit native code whose semantics were never proven. The
stance is the one [Necula 1997][research_necula_1997] formalises as proof-carrying code, under which the
artefact carries its own evidence, extended to a certifying compiler by
[Necula and Lee 1998][research_necula_lee_1998], and the bytecode-level analogue is the bytecode
verification treated by [Leroy 2003][research_leroy_2003] and specified for the Java virtual machine by the
[Oracle Java Virtual Machine Specification][ref_jvm_spec].

The two measures satisfy $\rho^{\text{unit}}(S) \le \rho^{\text{inst}}(S)$ with equality only in the
degenerate cases where $S \supseteq \bigcup_m c_m$ or where every unit has unit length. Define the coverage
gap

$$\Gamma(S) = \rho^{\text{inst}}(S) - \rho^{\text{unit}}(S)$$

which measures the extent to which an instance-level progress report overstates delivered capability.

### Blocking sets and marginal gain

Define the blocking set of an instruction $\iota \notin S$ as the set of units that would become lowerable
if and only if $\iota$ were added,

$$B(\iota, S) = \bigl\{ c_m \in C : \chi(c_m, S) = 0 \ \wedge\ \chi(c_m, S \cup \{\iota\}) = 1 \bigr\}$$

with the marginal unit-level gain

$$g(\iota, S) = \frac{|B(\iota, S)|}{M} = \rho^{\text{unit}}(S \cup \{\iota\}) - \rho^{\text{unit}}(S).$$

Let $n(\iota)$ denote the instance count of $\iota$ across the corpus,

$$n(\iota) = \sum_{m=1}^{M} \bigl| \{ \iota' \in c_m : \iota' = \iota \} \bigr|.$$

The central structural claim is that $g$ is not monotone in $n$. Formally, there exist instructions
$\iota_a, \iota_b \notin S$ with

$$n(\iota_a) > n(\iota_b) \qquad \text{and} \qquad |B(\iota_a, S)| < |B(\iota_b, S)|$$

The results section exhibits such a pair at WORKSTREAM granularity, with a ratio exceeding three in the
instance count and exceeding three in the opposite direction in the blocking count. It does not exhibit one
at instruction granularity, and cannot, because the supermodularity established below empties almost every
instruction-level blocking set, so an instruction-level comparison would compare zeroes. The existence claim
above is therefore stated for completeness of the formalism and is witnessed only after aggregation.

The ordering problem is therefore the selection

$$\iota^{\star} = \arg\max_{\iota \in I \setminus S} \lambda(\iota, S), \qquad \lambda(\iota, S) = \frac{|B(\iota, S)|}{\kappa(\iota)}$$

with $\kappa(\iota)$ the implementation cost and $\lambda$ the leverage ratio.

**That selection rule is not new, and naming it imports both a guarantee and the precise conditions under which the guarantee fails.**
Choosing repeatedly the candidate with the greatest newly covered mass per unit cost is the cost-weighted
greedy heuristic for set covering, analysed by [Johnson 1974][research_johnson_1974] and
[Chvatal 1979][research_chvatal_1979], which established the logarithmic approximation ratio, sharpened by
[Slavı́k 1997][research_slavik_1997] and shown to be essentially the best obtainable unless the complexity
classes collapse by [Lund and Yannakakis 1994][research_lund_yannakakis_1994] and
[Feige 1998][research_feige_1998].
**The ordering problem posed here is set cover with costs, and the leverage ratio is the classical greedy rule for it.**

**The guarantee attaches to the covering formulation, while the objective measured here falls outside it**,
a distinction the supermodularity section makes precise and which is the reason the greedy rule is offered
below as a heuristic rather than as an approximation algorithm.

The ordering principle in common use is the degenerate variant

$$\iota^{\star}_{\text{naive}} = \arg\min_{\iota \in I \setminus S} \kappa(\iota)$$

which minimises cost alone while leaving $\lvert B \rvert$ unmeasured and therefore implicitly assumed uniform across
instructions. The assumption is false in the case measured below.

### Supermodularity, and why greedy carries no guarantee here

The ordering principle advocated here is greedy, and the question is whether greediness admits the usual
formal justification. It does not, and the reason is structurally important.

Write $R_m \subseteq I$ for the set of distinct instructions appearing in unit $c_m$, so that $\chi(c_m, S)
= \mathbf{1}[R_m \subseteq S]$ and

$$\rho^{\text{unit}}(S) = \frac{1}{M} \sum_{m=1}^{M} \mathbf{1}[R_m \subseteq S].$$

The objective is monotone non-decreasing,

$$S \subseteq S' \implies \rho^{\text{unit}}(S) \le \rho^{\text{unit}}(S')$$

since adding an instruction can only turn indicators from zero to one. The marginal gain of adding $\iota$
has the explicit form

$$g(\iota, S) = \frac{1}{M} \Bigl| \bigl\{ m : \iota \in R_m \ \wedge\ R_m \setminus \{\iota\} \subseteq S \bigr\} \Bigr|$$

and for $S \subseteq S'$ the qualifying set for $S$ is contained in the qualifying set for $S'$, since $R_m
\setminus \{\iota\} \subseteq S$ implies $R_m \setminus \{\iota\} \subseteq S'$. Therefore

$$S \subseteq S' \subseteq I, \quad \iota \notin S' \implies g(\iota, S) \ \le\ g(\iota, S')$$

which is **increasing** marginal returns. The objective is supermodular, not submodular.

**The whole force of the error lies in a reversed inequality, so both forms belong side by side.** The two
properties, and the convex and concave structure that separates them, are set out in
[Lovasz 1983][research_lovasz_1983]. Submodularity, the property that was asserted, is diminishing returns,

$$S \subseteq S' \implies g(\iota, S) \ \ge\ g(\iota, S') \qquad \text{(submodular, and FALSE here)}$$

$$S \subseteq S' \implies g(\iota, S) \ \le\ g(\iota, S') \qquad \text{(supermodular, and true here)}$$

**And the guarantee that submodularity would have bought belongs here too**, since invoking it by name
without stating it is what let the error pass. For a monotone submodular objective under a cardinality
constraint the greedy algorithm satisfies

$$f(S_{\text{greedy}}) \ \ge\ \Bigl( 1 - \tfrac{1}{e} \Bigr) f(S_{\text{OPT}}) \approx 0.632 \, f(S_{\text{OPT}})$$

**No such bound is available here.** Under supermodularity the greedy choice can be arbitrarily bad, because
an instruction with zero marginal gain today may have large gain once its companions are present, which is
exactly the situation equation for $\lvert B(\iota, S) \rvert = 0$ above describes. An initial draft of this article
asserted the opposite and invoked the [Nemhauser, Wolsey and Fisher 1978][research_nemhauser_1978] result to
claim that greedy selection attains $\bigl(1 - \tfrac{1}{e}\bigr) \approx 0.632$ of the optimum under a
cardinality constraint. That claim is false. The classical guarantee requires diminishing returns, whose
tightness [Nemhauser and Wolsey 1978][research_nemhauser_wolsey_1978b] establish, whose dependence on
curvature [Conforti and Cornuejols 1984][research_conforti_cornuejols_1984] characterise, whose geometric
character [Lovasz 1983][research_lovasz_1983] develops, whose budgeted variant
[Khuller and colleagues 1999][research_khuller_1999] treat, and whose unconstrained non-monotone case
[Buchbinder and colleagues 2015][research_buchbinder_2015] settle at one half. Maximisation of a monotone
supermodular function admits no constant-factor approximation in general, the containment being of the
set-cover family whose completeness [Karp 1972][research_karp_1972] established and whose logarithmic
inapproximability threshold [Feige 1998][research_feige_1998] proved. The greedy ordering advocated here is
therefore an empirically justified heuristic with no approximation guarantee attached, and the article says
so rather than borrowing authority from a theorem that does not apply.

The correction is not merely a repair, because the increasing-returns structure explains an empirical fact
the erroneous version could not. Under increasing returns the singleton blocking sets are typically empty,

$$\bigl| B(\iota, S) \bigr| = 0 \quad \text{for most } \iota \notin S, \qquad \text{while} \qquad \bigl| B(W, S) \bigr| \gg 0$$

because a unit requiring several unimplemented instructions is unblocked by none of them individually and by
all of them jointly. This is precisely why instruction-level attribution is uninformative in this setting
and why the analysis must aggregate to workstreams. The conjunction that makes $\chi$ a product, the
conjunction that makes the objective supermodular, and the conjunction that empties the singleton blocking
sets are one observation viewed three ways.

### Workstream aggregation

Instructions that share a design prerequisite are implemented together, so the practically available choices
are workstreams, not individual instructions. Let $W \subseteq I \setminus S$ denote a workstream. The
workstream blocking set and counterfactual gain are

$$B(W, S) = \bigl\{ c_m : \chi(c_m, S) = 0 \ \wedge\ \chi(c_m, S \cup W) = 1 \bigr\}, \qquad \Delta\rho^{\text{unit}}(W) = \frac{|B(W, S)|}{M}.$$

Workstream-level counterfactuals are better identified than instruction-level ones, because the
co-occurrence that defeats instruction-level attribution is largely within workstreams instead of across
them. An instruction reading a data-segment slot co-occurs with an instruction writing one far more often
than either co-occurs with a coroutine suspension.

## The Code Generation Literature, and Where Ordering Is Absent From It

The instruction-selection literature is mature and supplies no ordering principle, which this section
establishes instead of asserting, because the absence is the gap this article addresses.

The tradition begins with optimality results for restricted shapes.
[Sethi and Ullman 1970][research_sethi_ullman_1970] gave optimal code generation for arithmetic expressions
under a register-count constraint, and the result is optimal with respect to a fixed and fully implemented
instruction set. [Glanville and Graham 1978][research_glanville_graham_1978] introduced table-driven
selection by parsing the intermediate representation against a machine grammar, and
[Fraser, Hanson and Proebsting 1992][research_fraser_1992] reduced the approach to a practical generator
generator. [Ertl 1999][research_ertl_1999] extended optimality from trees to directed acyclic graphs. At the
extreme, [Massalin 1987][research_massalin_1987] searched the instruction space exhaustively for the
shortest program computing a function.
**The tradition also learned to synthesise the rules rather than write them, which matters because it changes what a lowering costs without changing what this article measures.**
[Davidson and Fraser 1984][research_davidson_fraser_1984] generated peephole optimisations automatically
from a machine description, [Aho, Ganapathi and Tjiang 1989][research_aho_ganapathi_1989] reduced
instruction selection to tree matching with dynamic programming,
[Bansal and Aiken 2006][research_bansal_aiken_2006] harvested a peephole superoptimiser by enumeration over
the target, and [Schkufza, Sharma and Aiken 2013][research_schkufza_2013] replaced enumeration with
stochastic search over loop-free binaries. **Synthesis lowers $\kappa$ and leaves $\lvert B \rvert$ untouched**, so it
changes the leverage ratio through its denominator only and reorders nothing that the numerator determines.

Every one of these results presupposes that the target instruction set is available in its entirety. None
addresses the partial-implementation regime, because none has a reason to.

The supporting analyses are likewise complete-set analyses. [Allen 1970][research_allen_1970] established
control-flow analysis, [Kildall 1973][research_kildall_1973] the unified dataflow framework,
[Ferrante and colleagues 1987][research_ferrante_1987] the program dependence graph,
[Wegman and Zadeck 1991][research_wegman_zadeck_1991] conditional constant propagation, and
[Chaitin 1982][research_chaitin_1982] register allocation by graph colouring. Static single assignment form,
introduced by [Cytron and colleagues 1991][research_cytron_1991], given a functional reading by
[Appel 1998][research_appel_1998], and reduced to a simple construction by
[Braun and colleagues 2013][research_braun_2013], is the representation the present generator relies on,
since it models the operand stack as memory slots and delegates their promotion to registers to that
machinery. The generator targets the intermediate representation of
[Lattner and Adve 2004][research_lattner_adve_2004] specified in the
[LLVM Language Reference][ref_llvm_langref].

The observation to draw is that this literature optimises within a covered instruction set and is silent on
how to reach one. A backend author consulting it finds a great deal about how to lower an instruction well
and nothing about which instruction to lower next. The silence is not an oversight, because in the settings
these works address the instruction set is a fixed input, never a schedule. It becomes an oversight only
when the set is being covered incrementally, which is the universal condition of a backend under
construction and a condition the literature treats as a transient state not worth theorising.

## Verified and Validated Compilation as the Governing Constraint

The refusal discipline that makes $\chi$ a conjunction is inherited from the verified-compilation
literature, and the strength of the inheritance determines how much of the ordering problem is forced and
how much is chosen.

Two families of technique exist. The first proves the compiler correct once and for all, of which
[Leroy 2009][research_leroy_2009] is the canonical instance for a realistic C compiler and
[Kumar and colleagues 2014][research_kumar_2014] the analogous result for a functional language with a
verified implementation down to machine code. The second validates each compilation run instead of the
compiler, an approach [Pnueli and colleagues 1998][research_pnueli_1998] introduced as translation
validation, [Sewell and colleagues 2013][research_sewell_2013] applied to a verified operating-system
kernel, and [Kang and colleagues 2018][research_kang_2018] carried into the LLVM setting as credible
compilation. [Zhao and colleagues 2012][research_zhao_2012] formalised the LLVM intermediate representation
itself so that transformations over it may be verified, and [Lopes and colleagues 2021][research_lopes_2021]
built bounded translation validation for LLVM into a practical tool.

Where full verification is unavailable, differential and randomised testing carries the load.
[Yang and colleagues 2011][research_yang_2011] found hundreds of defects in production C compilers by random
program generation, [Le and colleagues 2014][research_le_2014] introduced equivalence modulo inputs as a
general oracle for compiler testing, and [Chen and colleagues 2016][research_chen_2016] applied
coverage-directed differential testing across virtual machine implementations. The present generator sits in
this second family. Its oracle is differential execution of the same bytecode on the reference virtual
machine and on the lowered native code, which is the equivalence-modulo-inputs pattern with the input space
supplied by hand rather than generated.

The consequence for the ordering problem is that partial implementation is not merely permitted but required
to be explicit. A generator in this tradition cannot silently approximate. Every unimplemented instruction
is a refusal, every refusal propagates to the whole compilation unit through the conjunction, and the
ordering problem therefore acquires its characteristic structure directly from the verification stance
rather than from any property of the instruction set. A generator willing to emit unverified approximations
would face a smooth ordering problem with diminishing returns and would be able to invoke the classical
greedy guarantee. The verification stance is what makes the objective supermodular and the guarantee
unavailable, which is a cost of that stance and belongs plainly beside its benefits.

## Static Analysis, Undecidability, and the Conservative Stance

The generator consumes shape information produced by an abstract interpretation in the sense of
[Cousot and Cousot 1977][research_cousot_1977], which is also the framework within which
[Blanchet and colleagues 2003][research_blanchet_2003] built a static analyser for large safety-critical
avionics software and within which [Regehr and colleagues 2005][research_regehr_2005] eliminated stack
overflow in embedded software by bounding stack depth statically. The last of these is the closest published
analogue to the native memory-bound problem the present workstream faces.

The conservative stance the language adopts, under which programs whose bounds cannot be proven are
rejected, is forced by classical undecidability. [Rice 1953][research_rice_1953] established that every
non-trivial semantic property of programs is undecidable, and [Landi 1992][research_landi_1992] sharpened
the consequence for static analysis specifically. A verifier that admits only what it can prove will
therefore reject some programs that are in fact well behaved, and the size of that gap is a design parameter
and not a defect.

This bears on the ordering problem in a way not immediately obvious. The corpus measured below consists of
programs the front end accepts, which is a population already shaped by the conservative stance.
Instructions associated with constructs the verifier rejects cannot appear in the corpus at any frequency,
so their measured blocking contribution is zero for a reason unrelated to demand. The measurement therefore
estimates blocking frequency conditional on admissibility, and an instruction whose frequency would be high
in an unconstrained population may measure at zero here. No such case is known to arise in the present data,
but the conditioning is a real limitation of the method and not a hypothetical one.

## Worst-Case Resource Analysis and the Native Transfer Problem

The reason the whole programme exists is the resource-bound guarantee, and the literature on that guarantee
is what determines whether native lowering can preserve it.

Hard real-time scheduling, in the form [Liu and Layland 1973][research_liu_layland_1973] established,
presupposes a worst-case execution time for each task. Obtaining that number is the subject of a substantial
literature surveyed by [Wilhelm and colleagues 2008][research_wilhelm_2008] and earlier by
[Puschner and Burns 2000][research_puschner_burns_2000]. The dominant bounding technique is implicit path
enumeration, introduced by [Li and Malik 1995][research_li_malik_1995], which expresses the worst-case path
as an integer linear program over basic-block execution counts. The precision of any such bound on real
hardware depends on microarchitectural modelling, for which
[Ferdinand and Wilhelm 1999][research_ferdinand_wilhelm_1999] gave cache behaviour prediction and
[Reineke and colleagues 2007][research_reineke_2007] characterised the predictability of cache replacement
policies themselves.

The memory-bound side draws on the region and arena literature.
[Tofte and Talpin 1997][research_tofte_talpin_1997] introduced region-based memory management with static
inference of region lifetimes, [Grossman and colleagues 2002][research_grossman_2002] carried regions into a
safe systems language, [Hanson 1990][research_hanson_1990] gave the practical arena discipline of allocation
by object lifetime, and [Berger and colleagues 2002][research_berger_2002] examined empirically when custom
allocation actually pays. Keleusma's arena model is of this family, and the native transfer question is
whether a bound proven over the arena survives lowering to code whose stack frames are chosen by a register
allocator in the tradition of [Chaitin 1982][research_chaitin_1982].

A companion measurement, recorded in the project's decision register rather than in a separate article,
establishes that the per-function frame size is recoverable from the emitted object file, that it folds to a
compile-time constant, and that it varies by a factor of roughly thirty depending on whether the middle-end
promotion pass of [Cytron and colleagues 1991][research_cytron_1991] has run. That measurement is what makes
the [Regehr and colleagues 2005][research_regehr_2005] approach applicable here, since it supplies the
per-function weights their longest-path analysis consumes. The ordering relevance is that none of this work
is unblocked by the instruction classes the naive ordering favoured.

## Corpus-Based Empirical Study of Programs

The method employed here belongs to a tradition with a clear origin. [Knuth 1971][research_knuth_1971]
collected and statically analysed a corpus of FORTRAN programs for the explicit reason that the profession's
beliefs about which language constructs mattered were untested, and found the distribution of constructs to
be sharply different from the folklore. The paper is the direct methodological ancestor of the instrument
described below, and its central move, which is to measure the population rather than reason about the
language, is the move this article recommends generalising.

The tradition has continued. [Basili and Weiss 1984][research_basili_weiss_1984] formalised the collection
of valid software engineering data and the failure modes of informal collection.
[Richards and colleagues 2010][research_richards_2010] measured the dynamic behaviour of deployed JavaScript
programs and found systematic divergence between what the language permits, what the literature assumed
programs did, and what programs actually did. [Allamanis and Sutton 2013][research_allamanis_sutton_2013]
and [Dyer and colleagues 2013][research_dyer_2013] built infrastructure for corpus mining at repository
scale, and [Ray and colleagues 2014][research_ray_2014] applied such infrastructure to language-level
questions about code quality.

Two lessons from this tradition bear directly on the present measurement. The first is that the gap between
permitted and actual is routinely large, which is exactly the gap the zero result below occupies, since the
four instructions in question are fully supported by the language and used by no program in the corpus. The
second concerns corpus composition, which dominates conclusions, a point
[Ray and colleagues 2014][research_ray_2014] and its subsequent reanalyses illustrate at length, and which
the threats-to-validity section below treats as the principal limitation of this work, never as a formality.

## Coverage Adequacy, Mutation, and What a Passing Suite Permits

The instrument reports a coverage figure, and the software-testing literature has spent decades establishing
what coverage figures do and do not mean. The parallel is close enough to draw explicitly.

[Zhu, Hall and May 1997][research_zhu_1997] surveyed test coverage and adequacy criteria and the
relationships among them. The decisive empirical result is
[Inozemtseva and Holmes 2014][research_inozemtseva_holmes_2014], which found that coverage is not strongly
correlated with test-suite effectiveness once suite size is controlled, and therefore that a coverage
percentage is a poor proxy for the property anyone actually wants. The structural analogy to the present
case is exact. Instruction-level coverage $\rho^{\text{inst}}$ is the attractive, easily computed, and
largely uninformative measure. Unit-level coverage $\rho^{\text{unit}}$ is the one that tracks delivered
capability, and the two differ here by $\Gamma = 0.534$.

**The testing literature also solved the selection problem this article poses, in its own setting and with the same formal object.**
Reducing a test suite to a subset preserving coverage is set cover, stated as such by
[Harrold, Gupta and Soffa 1993][research_harrold_1993], and the ordering variant is test-case
prioritisation, formalised by [Rothermel and colleagues 2001][research_rothermel_2001] and surveyed with
selection and minimisation by [Yoo and Harman 2012][research_yoo_harman_2012]. Safe selection, meaning
selection that cannot discard a test capable of exposing a difference, is due to
[Rothermel and Harrold 1997][research_rothermel_harrold_1997].
**The cautionary result belongs beside them.** [Wong and colleagues 1995][research_wong_1995] found that
minimising a suite while holding coverage constant can reduce fault-detection effectiveness, which is the
same warning the present article issues in the opposite direction.
**A coverage-preserving reduction and a coverage-maximising ordering are the same optimisation read forwards and backwards, and both are vulnerable to the measure standing in for the goal.**

The correctness discipline used throughout the development this article reports is mutation testing,
introduced by [DeMillo, Lipton and Sayward 1978][research_demillo_1978] and surveyed by
[Jia and Harman 2011][research_jia_harman_2011]. Every structural assertion in the generator's test suite
carries a must-fire case, meaning a deliberate defect injected into the lowering that the assertion is
required to detect, and a must-not-fire case, meaning a known-clean input on which it is required to stay
silent. The empirical justification for treating mutants as a proxy for real defects is given by
[Andrews and colleagues 2005][research_andrews_2005] and strengthened by
[Just and colleagues 2014][research_just_2014], which found mutant detection to be correlated with
real-fault detection to a degree that supports the practice.

The practice earned its place during this work instead of being adopted on authority. Of twenty-two
mutations run across the increments this article reports, five failed to fire on first execution, and those
five were of four distinct kinds.

One was a **null mutation**, where the mutated code is semantically identical to the original, so no test
could distinguish it and none should. Changing an arithmetic shift to a logical one before a truncation that
discards the differing bits is of this kind. A null mutation is not evidence of a coverage gap and treating
it as one leads to writing a test that can never fail.

One was a **real coverage gap** in a target-specific case, where the hardware happened to define the
behaviour that the undefined-behaviour rule permitted the compiler to exploit, so no behavioural test on
that target could observe the defect. The response is a structural assertion over the emitted code.

Two were **vacuous tests**, whose test data carried a symmetry that concealed the asymmetry under test. In
one, two branches of a differential case returned identical values. In the other, the callee of a
cross-function call performed a commutative operation, so exchanging its arguments changed nothing. The
response is redesigned input.

One was **genuinely unobservable**, a value no program in the language can read. The response is an explicit
statement that the property is untested and untestable, which is the only honest option.

The four demand different responses and were nearly conflated. Only the mutation runs distinguished them,
and the vacuous-test kind recurred three times across the work despite being actively watched for, which is
the strongest available evidence that the failure is structural, so inattention does not explain it.

## Submodular Optimisation, Coverage, and Prioritisation

The formal home of the ordering problem is the maximisation of a set function under a budget, and the
relevant results have been stated above in the course of establishing which of them apply. The complementary
literature is on prioritisation as an engineering practice rather than as an optimisation problem.

[Karlsson and Ryan 1997][research_karlsson_ryan_1997] introduced a cost-value approach to prioritising
requirements, in which candidate requirements are scored on value and on cost and ordered by the ratio,
which is structurally the leverage ratio $\lambda$ defined above. Their contribution for present purposes is
the observation that practitioners reliably estimate cost and reliably fail to estimate value, so that a
ratio-based method degenerates in practice to a cost-based one unless value is measured rather than
elicited. That is precisely the failure this article documents in the compiler setting.

The regression-testing literature supplies the closest analogue with an empirical base.
[Elbaum and colleagues 2002][research_elbaum_2002] studied test-case prioritisation across a family of
empirical studies and found that orderings informed by measured fault-detection history substantially
outperform orderings informed by structural properties of the tests. The transferable finding is that a
measured signal about outcomes beats a structural signal about artefacts, and that the margin is large
enough to justify the measurement cost.

## The Identification Problem for Blocking Attribution

The identification problem is the question of separating the blocking contribution of an individual
instruction from the contributions of the instructions that co-occur with it. A unit blocked by four
distinct unimplemented instructions is unblocked by none of them individually, so naive per-instruction
attribution overstates every contribution. The overstatement obeys

$$\sum_{\iota \in I \setminus S} |B(\iota, S)| \ \le\ \Bigl| \bigcup_{\iota \in I \setminus S} B(\iota, S) \Bigr| \ \le\ M \cdot \bigl(1 - \rho^{\text{unit}}(S)\bigr)$$

where the first inequality is an equality only when the blocking sets are pairwise disjoint, which is to say
only when no unit is blocked by two distinct instructions. In the corpus below the blocking sets are very
far from disjoint, and the singleton blocking sets are in fact mostly empty, for the supermodularity reason
established above.

The principled resolution of the attribution problem is the value of [Shapley 1953][research_shapley_1953],
which distributes the total unblocking across contributors by averaging each contributor's marginal gain
over all orders in which the contributors might be added.
**It is the only attribution satisfying efficiency, symmetry, the null-contributor property and additivity together**,
and [Young 1985][research_young_1985] showed that additivity may be replaced by a monotonicity requirement
without changing the answer, which matters here because monotonicity in the marginal gain is the property an
ordering argument actually wants. [Owen 1972][research_owen_1972] gave the multilinear extension that makes
the average tractable to reason about. Writing $\mathcal{W}$ for the set of workstreams, the Shapley
attribution of workstream $W$ is

$$\phi(W) = \sum_{T \subseteq \mathcal{W} \setminus \{W\}} \frac{|T|!\,\bigl(|\mathcal{W}| - |T| - 1\bigr)!}{|\mathcal{W}|!} \Bigl[ \rho^{\text{unit}}\bigl(S \cup \textstyle\bigcup T \cup W\bigr) - \rho^{\text{unit}}\bigl(S \cup \textstyle\bigcup T\bigr) \Bigr]$$

which satisfies the efficiency property

$$\sum_{W \in \mathcal{W}} \phi(W) = \rho^{\text{unit}}\bigl(S \cup \textstyle\bigcup \mathcal{W}\bigr) - \rho^{\text{unit}}(S) = 1 - \rho^{\text{unit}}(S)$$

so the attributions sum exactly to the total unblocking with no double counting, which is precisely the
property the naive per-instruction count lacks. With $\lvert \mathcal{W} \rvert = 6$ the exact computation requires
$2^{6} = 64$ evaluations of $\rho^{\text{unit}}$, each a linear pass over the corpus, so the exact Shapley
attribution is computationally trivial here and its omission is a matter of scope, since tractability was
never the obstacle.

The article therefore reports two statistics with different properties instead of attempting a single
attribution. The first is the instance count $n(\iota)$, an upper bound on effort saved that carries no
unblocking claim whatsoever. The second reports the first-blocker distribution, which assigns each blocked
unit to exactly one workstream and therefore partitions the blocked population without double counting,

$$\sum_{W} f(W) = M \cdot \bigl(1 - \rho^{\text{unit}}(S)\bigr), \qquad f(W) = \bigl| \{ c_m : \text{first blocking instance of } c_m \in W \} \bigr|.$$

The first-blocker assignment is order-dependent within a unit. Writing $\pi$ for the instruction-stream
order and $f_\pi(W)$ for the resulting partition, the article reports $f_\pi$ for the natural $\pi$ and does
not compute

$$\bar f(W) = \mathbb{E}_{\pi \sim \mathcal{U}}\bigl[ f_\pi(W) \bigr]$$

over the uniform distribution on orders, nor the full blocking lattice over subsets of $I \setminus S$. This
is stated outright, never left as an implicit claim to completeness. The first-blocker partition should be
read as a cheap surrogate for $\phi$, agreeing with it in ordering when one workstream dominates and
unreliable when several are comparable.

## Method

The instrument compiles every Keleusma source file in four corpus directories through the reference front
end, walks the resulting instruction streams, classifies each instance as lowered or blocking, attributes
blocking instances to a workstream by a total function over the instruction set, and classifies each
compilation unit by the lowerability indicator $\chi$.

Three properties bound the strength of the conclusions.

The instrument measures the reference compiler's output rather than source text, following the precedent
[Knuth 1971][research_knuth_1971] set in measuring what programs actually contain, not what their authors
assume, and the data-collection discipline [Basili and Weiss 1984][research_basili_weiss_1984] formalise.
This is the correct choice, because the generator consumes bytecode rather than source, and because the
relationship between surface syntax and emitted instructions is not obvious in this language. A prior
increment established that the four instructions named for ordinary arithmetic do not carry integer operands
at all, and that all integer arithmetic is emitted as a checked form followed by a discard of two of its
three results. Any instrument reasoning over source text would have miscounted that entirely.

The instrument excludes files the front end rejects. Five of the sixty-three files were rejected, all of
them real-time operating system scripts referring to host functions registered by the embedding application
rather than declared in the script. The exclusion is environmental and not linguistic, and including those
files would add instances to the native application binary interface class, reinforcing the reported
conclusion instead of qualifying it.

The instrument carries a guard assertion

$$\bigl(\text{files compiled} > 10\bigr) \ \wedge\ \bigl(N > 1000\bigr)$$

and fails loudly otherwise. The assertion exists because a path error in corpus discovery would silently
yield a small clean sample, and every proportion reported below would then be noise presented as a
measurement. The characteristic failure mode of a measurement instrument is a plausible number rather than
an obvious error, a point [Mytkowicz and colleagues 2009][research_mytkowicz_2009] make forcefully for
performance measurement, where bias from incidental factors such as link order and environment size was
found sufficient to reverse published conclusions.

## Results

The corpus comprises sixty-three files, of which fifty-eight compiled, yielding $M = 496$ compilation units
and $N = 73{,}434$ instruction instances. The implemented subset was $\lvert S \rvert = 39$ of $\lvert I \rvert = 66$.

**This is the headline result and everything else in the article is either support for it or a consequence of it.**

The two coverage measures diverge sharply.

$$\rho^{\text{inst}}(S) = \frac{64{,}116}{73{,}434} = 0.8731, \qquad \rho^{\text{unit}}(S) = \frac{168}{496} = 0.3387$$

$$\Gamma(S) = 0.8731 - 0.3387 = 0.5344$$

The generator handles the large majority of instruction instances and the minority of compilation units. A
programme reporting eighty-seven percent coverage would be reporting a number no consumer of the generator
can use, because no consumer executes an instruction instance in isolation.

### The measurement repeated at a larger implemented subset, and a third level

The figures above were taken at $\lvert S \rvert = 39$. The subset has since reached $\lvert S \rvert = 46$, and repeating the
measurement is instructive both because the numbers move and because it exposed a level of the conjunction
the original analysis missed.

$$\rho^{\text{inst}}(S') = \frac{71{,}948}{73{,}434} = 0.9798, \qquad \rho^{\text{unit}}(S') = \frac{432}{496} = 0.8710, \qquad \Gamma(S') = 0.1088$$

The gap between the two measures has closed from $0.534$ to $0.109$, which is the expected behaviour, since
as $S$ approaches the union of the corpus's requirement sets, both measures approach one and the gap between
them must vanish.

**But a compilation unit is not what a consumer deploys.** A consumer deploys a MODULE, and a module lowers
only if every one of its compilation units does. That is the same conjunction applied once more, and it had
been left out of the analysis entirely. Writing $\mathcal{P}$ for the corpus of programs and $u(P)$ for the
compilation units of program $P$,

$$\rho^{\text{prog}}(S) = \frac{1}{|\mathcal{P}|} \sum_{P \in \mathcal{P}} \prod_{c \in u(P)} \chi(c, S)$$

and measured at $\lvert S' \rvert = 46$,

$$\rho^{\text{prog}}(S') = \frac{12}{58} = 0.2069.$$

So the three measures at the same implemented subset are $0.980$, $0.871$ and $0.207$. The collapse from the
middle figure to the outer one is a factor of

$$\frac{\rho^{\text{unit}}(S')}{\rho^{\text{prog}}(S')} = \frac{0.8710}{0.2069} = 4.21$$

and the article as first drafted quoted the middle one. That is the same category of error the article was
written to describe, committed one level up, in the section reporting the error. The general form is that a
conjunction exists at every level of aggregation the consumer's requirement spans, and an analysis must find
the OUTERMOST one, not the first one that looks like a unit of work.

### Ground truth, and why the original instrument could not supply it

The figures above at $\lvert S \rvert = 39$ came from a classification function that mirrored the lowering by hand. That
mirror is a second implementation of the acceptance predicate, and it drifted, because the implemented set
moved three times, each move requiring an edit to a list the lowering itself never reads.

The $\lvert S' \rvert = 46$ figures for $\rho^{\text{prog}}$ come instead from calling the real entry point on every
corpus program and counting successes, which cannot drift by construction. Where the two disagree the second
is authoritative. **An instrument that mirrors the system under measurement measures the mirror**, and the
defence is to call the system.

The blocking instances and first-blocker partition distribute as follows.

| Workstream $W$ | $\sum_{\iota \in W} n(\iota)$ | $f_\pi(W)$ |
|---|---|---|
| Data segment | 7832 | 267 |
| Native application binary interface | 1057 | 9 |
| Composites | 331 | 28 |
| Sub-coroutines | 98 | 24 |
| Typed arithmetic | 0 | 0 |
| Floating point and fixed point | 0 | 0 |

At $\lvert S' \rvert = 46$, with the data segment implemented, the same table reads as follows.

| Workstream $W$ | $\sum_{\iota \in W} n(\iota)$ | $f_\pi(W)$ |
|---|---|---|
| Native application binary interface | 1057 | 11 |
| Composites | 331 | 28 |
| Sub-coroutines | 98 | 25 |
| Typed arithmetic | 0 | 0 |

The data segment has left the table entirely, which is what implementing the leading blocker is supposed to
look like. The native interface remains the instance-count leader and the blocked-unit laggard, so the
non-monotonicity the article exhibits is not an artefact of one measurement.

The data-segment workstream accounts for

$$\frac{267}{496 - 168} = \frac{267}{328} = 0.814$$

of blocked units. The five most frequent individual blocking instructions are the data-segment slot write at
$n = 3385$, the slot read at $n = 2109$, the indexed read at $n = 1456$, the verified native call at $n =
1057$, and the indexed write at $n = 882$.

The native application binary interface class instantiates the non-monotonicity claim at the workstream
level. Writing $W_a$ for the native-call workstream and $W_b$ for the composite workstream, and extending
$n$ additively to workstreams,

$$n(W_a) = 1057 > 331 = n(W_b), \qquad f_\pi(W_a) = 9 < 28 = f_\pi(W_b)$$

so ranking by instance count places the native interface second and ranking by blocked units places it
fourth. The instruction-level claim stated earlier is the same phenomenon one level down. It is exhibited
here at workstream granularity because, for the supermodularity reason given above, the instruction-level
blocking sets are mostly empty and the instruction-level comparison would be a comparison of zeroes. Its
instances concentrate in a small number of large units already blocked for other reasons.

The sub-coroutine class deserves separate comment because its blocking count of twenty-four understates its
architectural weight. Coroutines in the sense [Conway 1963][research_conway_1963] introduced, and in the
modern treatment of [Moura and Ierusalimschy 2009][research_moura_ierusalimschy_2009], are the load-bearing
primitive for the streaming execution model the language targets, so the workstream sits on the critical
path for reasons the blocking count does not express. The ordering principle advocated here is a claim about
marginal capability, leaving architectural sequencing untouched, and where a low-blocking workstream is a
prerequisite for a high-blocking one the dependency order dominates. No such dependency is known to hold
between coroutines and the data segment in the present case, and the data-segment lowering does not appear
to require suspension support. That is an engineering judgement about the two designs rather than a measured
result, and it is the one load-bearing step in this article's recommendation that rests on judgement rather
than on the instrument.

### The independence null and the clustering coefficient

The unit-level collapse invites an obvious explanation, that unimplemented instructions are simply spread
thinly across many units. That explanation is testable.
**Comparing an observed count structure against an independence null is standard practice**, and the general
statistic for departure from it is a test for overdispersion, treated by [Dean 1992][research_dean_1992].
**The expectation that the departure will be large is not a guess either.** Defects in software are known
empirically to concentrate rather than distribute evenly, established by
[Fenton and Ohlsson 2000][research_fenton_ohlsson_2000] and measured at scale by
[Ostrand and Weyuker 2002][research_ostrand_weyuker_2002] and
[Ostrand, Weyuker and Bell 2005][research_ostrand_weyuker_2005], who found small fractions of modules
carrying most faults.
**Unimplemented instructions are not defects, but the concentration argument transfers**, because both arise
from uneven use of a shared vocabulary across a corpus. Under an independence null in which each instruction
instance in a unit is lowered with probability $p = \rho^{\text{inst}}(S)$ independently, the expected
unit-level coverage is

$$\rho^{\text{unit}}_{0} = \frac{1}{M} \sum_{m=1}^{M} p^{|c_m|}$$

and the clustering coefficient is the ratio of observed to null,

$$\Phi = \frac{\rho^{\text{unit}}(S)}{\rho^{\text{unit}}_{0}}.$$

Evaluating with the measured length distribution gives

$$\rho^{\text{unit}}_{0} = 6.152 \times 10^{-2}, \qquad \Phi = \frac{0.3387}{0.06152} = 5.51$$

so the blocking instructions are clustered, and by a factor of roughly five and a half, which is moderate.
Repeating the calculation at $\lvert S' \rvert = 46$ gives $\rho^{\text{unit}}_{0} = 3.275 \times 10^{-1}$ and $\Phi =
2.66$, a weaker clustering, which is again the expected direction, since as fewer instructions block, those
that remain have less opportunity to concentrate. Unimplemented instructions concentrate in units that use
them repeatedly, which is the expected consequence of a data-segment-heavy workload, and the concentration
is real but moderate.

### A methodological near-miss worth reporting

The null above must be evaluated per unit, never at the mean unit length. Since $x \mapsto p^{x}$ is convex
for $0 < p < 1$, the inequality of [Jensen 1906][research_jensen_1906] gives

$$\frac{1}{M} \sum_{m=1}^{M} p^{|c_m|} \ \ge\ p^{\,\bar{L}}, \qquad \bar{L} = \frac{1}{M}\sum_{m=1}^{M} |c_m| = 148.05$$

and the two quantities differ enormously here because the length distribution is heavily right-skewed, with
mean $148.05$ against median $69$. Numerically,

$$p^{\,\bar{L}} = 0.8731^{148.05} = 1.884 \times 10^{-9} \qquad \text{against} \qquad \frac{1}{M}\sum_m p^{|c_m|} = 6.152 \times 10^{-2}$$

a discrepancy of more than seven orders of magnitude. Had the null been evaluated at the mean length, the
clustering coefficient would have been reported as

$$\Phi_{\text{wrong}} = \frac{0.3387}{1.884 \times 10^{-9}} = 1.80 \times 10^{8}$$

instead of $5.51$, and the article would have claimed an overwhelming clustering effect where the true
effect is moderate. The error would have been in the direction of a more striking finding, which is the
direction in which errors are least likely to be questioned.

### Confidence bounds on the zero counts

Two instruction classes occur zero times as blockers. A zero count is not an assertion of impossibility, and
the appropriate summary is an upper confidence bound and not a point estimate. For zero events observed in
$n$ independent trials, the rule of three stated by [Hanley and Lippman-Hand 1983][research_hanley_1983] and
examined by [Jovanovic and Levy 1997][research_jovanovic_levy_1997], a normal-approximation shortcut on the
exact interval of [Clopper and Pearson 1934][research_clopper_pearson_1934], gives the approximate
ninety-five percent upper bound

$$(1 - p)^{n} = 0.05 \implies p = 1 - 0.05^{1/n} \approx \frac{\ln 20}{n} = \frac{2.996}{n}$$

$$\hat{p}_{\text{upper}} \approx \frac{3}{n}$$

which follows from solving $(1 - p)^n = 0.05$ and using $\log(0.05) \approx -3$. Applied to the two units of
account,

$$\hat{p}^{\text{inst}}_{\text{upper}} = \frac{3}{73{,}434} = 4.09 \times 10^{-5}, \qquad \hat{p}^{\text{unit}}_{\text{upper}} = \frac{3}{496} = 6.05 \times 10^{-3}$$

so the true per-instance rate of typed arithmetic in this population is below roughly four in one hundred
thousand, and the per-unit rate is below roughly six in one thousand, each at the stated confidence. The
independence assumption underlying the rule of three is violated here, since instruction instances within a
unit are strongly dependent, and the per-unit bound is consequently the more defensible of the two. For a
boundary proportion of this kind the interval of [Wilson 1927][research_wilson_1927], or the adjusted
interval [Agresti and Coull 1998][research_agresti_coull_1998] recommend in preference to the exact method,
would be the more careful summary, and the rule of three is reported here because it is the form in which
such a result is conventionally communicated rather than because it is the tightest available.

## The Zero Result, and the Recommendation It Falsified

The second zero is the finding of consequence, because the working session immediately preceding the
measurement closed with a formal recommendation that the next research spike address exactly that class. The
reasoning was as follows. The four instructions are reachable only for byte, fixed-point and floating-point
operands. The byte representation had just been settled by a measurement contributed from a parallel
development line. The remaining obstacle was that the instruction does not record which of the three types
its operands carry, and the lowerings differ, since a byte addition must mask its result to eight bits while
a fixed-point addition must not. Recovering operand types would therefore unblock the class. The
recommendation observed further that the same type information is required by the composite workstream for
field offsets, and concluded that operand type recovery was the highest-leverage remaining work by a clear
margin.

Every step of that reasoning is correct. The conclusion is worthless. Writing $W_{\text{typed}}$ for the
class,

$$n(W_{\text{typed}}) = 0 \implies B(W_{\text{typed}}, S) = \varnothing \implies \Delta\rho^{\text{unit}}(W_{\text{typed}}) = 0$$

and the composite workstream it was partly justified by satisfies $f_\pi(W_{\text{composite}}) = 28$ against
the data segment's $267$, a ratio of

$$\frac{f_\pi(W_{\text{data}})}{f_\pi(W_{\text{composite}})} = \frac{267}{28} = 9.54.$$

The failure is not a reasoning error, and the distinction matters because the corrective differs. The
argument contained no invalid step. It reasoned carefully about the structure of a problem while never
asking how often the problem occurs. A dependency analysis answers what must be true before an instruction
can be implemented. It does not answer whether anyone needs the instruction, and the two questions are
independent. The recommendation was a well-constructed answer to a question nobody had asked.
[Meehl 1967][research_meehl_1967] observed the general form of this hazard in comparing theory-testing
practice across disciplines, namely that a methodology can be internally rigorous and systematically
uninformative about the question of interest.

### A refinement the same work later forced, which sharpens the lesson

The account above is correct and incomplete, and the missing part changes what a reader should take away.

Operand type recovery was dismissed on the strength of a zero. Some increments later, the composite
workstream turned out to require exactly that capability, for an unrelated reason, namely that
`Op::NewComposite` carries the composite kind, the field count and the total byte size, and NOT the
per-field widths, while packing is tight and in declaration order. Writing a composite body therefore needs
each field's width and no instruction records it. That is 18 compilation units, against the zero the
original assessment measured.

So the measurement was right and the inference from it was too broad. It established that type recovery was
worthless FOR THE INSTRUCTION CLASS PROPOSED, and the conclusion drawn was that type recovery was worthless.
A capability is not made valueless by the emptiness of one demand for it, and a frequency measurement that
redirects work away from a capability has said something about that demand rather than about the capability.

The sharpened statement is therefore in two parts rather than one. Measure demand before ordering by
structure, because a dependency argument cannot see frequency. And scope the negative result to what was
measured, because a zero counts occurrences of one thing and licenses no conclusion about anything else. The
first part saved the work described here. The second part was learned by getting it wrong in the same
programme, a few increments later, and having to correct a document that had recorded the over-broad version
as a finding.

The corpus check that falsified it cost approximately twenty minutes to build and two seconds to run. The
cost of the work it redirected cannot be stated with comparable confidence, because that work was never
performed. **The numerator below is measured and the denominator is an estimate of a counterfactual**, so
the ratio should be read as an order of magnitude and not as a quantity. Writing $\kappa_{\text{measure}}$
for the measured cost and $\kappa_{\text{spike}}$ for the estimated cost of the redirected spike,

$$\frac{\kappa_{\text{measure}}}{\kappa_{\text{spike}}} \sim 10^{-2}$$

so the measurement plausibly cost one or two orders of magnitude less than the work it redirected, and the
redirected work would have delivered $\Delta\rho^{\text{unit}} = 0$ exactly. Only the last of those three
statements is a measurement. An earlier draft gave this ratio as $0.019$ against a sixteen-hour denominator,
presenting an invented figure to two significant figures inside a formal expression, which lent it a
precision it had not earned.

## Measurement Error and the Direction of Bias

This article reports **four** errors made in the course of producing it, and their common direction is the
most transferable observation available.
**Three are described below and the fourth is described inside the description of the third**, which is not
an accident and is the point of the section.

The first is the convexity shortcut described above,
**which is [Jensen's inequality][research_jensen_1906] applied in the wrong direction**, since $p^{x}$ is
convex in $x$ and the mean of the powers therefore exceeds the power of the mean rather than equalling it.
It would have inflated a clustering coefficient by seven orders of magnitude. The second was a false
modularity theorem, where the coverage objective was asserted to be submodular so that a classical
approximation guarantee could be invoked, when the objective is supermodular and no such guarantee exists.
The third occurred while assembling this article's references. Of ninety-one candidate digital object
identifiers supplied from memory, four resolved to entirely different works and one did not resolve at all,
an error rate of five and a half percent. One resolved to a paper on record allocation for drum storage in
place of a paper on optimal code generation for expression trees, and one to a paper on a lambda calculus of
objects in place of a paper on lightweight bytecode verification. Each of the four would have returned a
successful response to a reachability check, so only comparison of the resolved title against the claimed
title detected them.

**A draft of this article reported this rate as near ten percent over forty-two candidates.** That figure is
the first three verification batches taken alone, which is the worse subsample, and the later batches were
run after the sentence was written and never folded into it. The effect was to report a more alarming number
than the data supported, in the section of the article devoted to the tendency to report more alarming
numbers than the data support. The error is left visible here instead of silently repaired, because a
corrected figure with no record of the correction would conceal the most instructive part of the episode.

All four errors ran toward a more striking or better-founded-looking result. The clustering error would have
produced a dramatic finding, the modularity error would have supplied a theoretical guarantee for the
article's central recommendation, the citation errors would have furnished authority, and the misstated
defect rate would have made the cautionary point more forcefully. None ran in the direction of weakening a
claim, and the fourth was committed while writing the paragraph warning against the first three.

This direction is documented at scale in the empirical-methods literature.
[Rosenthal 1979][research_rosenthal_1979] described the suppression of null results and estimated the number
of unpublished null studies required to overturn a published effect.
[Simmons, Nelson and Simonsohn 2011][research_simmons_2011] demonstrated that undisclosed flexibility in
data collection and analysis suffices to produce statistically significant evidence for false propositions
without any conscious dishonesty. [Ioannidis 2005][research_ioannidis_2005] derived the consequences for
base rates of published findings, and [Munafo and colleagues 2017][research_munafo_2017] set out the
corresponding reform programme. The mechanism in each case is not fraud but asymmetric scrutiny, in which a
result the author expects and welcomes receives less checking than one that surprises or disappoints.

The engineering translation is direct. An error that weakens a claim tends to be noticed because it is
unwelcome. An error that strengthens one is congenial and passes unexamined, and a formal apparatus is an
efficient way to manufacture such errors because its conclusions carry borrowed authority. Three defences
were used here and are recommended generally. Evaluate aggregates over the observed distribution, never at
its mean, whenever the aggregating function is not affine. Test a formal claim by brute-force enumeration
over instances small enough to check exhaustively before relying on it. Verify every citation against the
resolved record rather than against memory, since the failure mode is a plausible reference and not a broken
link.

## Threats to Validity

The corpus is drawn from one project's own examples, standard library and self-hosted compiler stages, and
is therefore not a sample of the programs the generator will eventually serve. Writing
$\mathcal{D}_{\text{corpus}}$ for the empirical distribution over units and $\mathcal{D}_{\text{target}}$
for the eventual target population, every quantity reported above estimates

$$\mathbb{E}_{c \sim \mathcal{D}_{\text{corpus}}}\bigl[ \cdot \bigr] \qquad \text{rather than} \qquad \mathbb{E}_{c \sim \mathcal{D}_{\text{target}}}\bigl[ \cdot \bigr]$$

and no importance weighting is applied because the target distribution is not yet observable. The corpus
over-represents the self-hosted compiler, a text-processing workload with heavy data-segment use, and
under-represents the signal-processing and embedded-control workloads the roadmap names as target
applications. A defensible reading is that the data segment leads for the near-term consumer and that the
ranking should be re-measured when the target population changes. The sensitivity of conclusions to corpus
composition is the standard caution of this literature, and
[Blackburn and colleagues 2006][research_blackburn_2006] made the point concrete in constructing a benchmark
suite specifically because prior suites had shaped conclusions unrepresentatively, while
[Blackburn and colleagues 2016][research_blackburn_2016] set out the corresponding evaluation discipline.

The first-blocker attribution is order-dependent, as formalised above, and the full blocking lattice is not
computed. For the leading result this is unlikely to matter, since

$$\frac{f_\pi(W_{\text{data}})}{\max_{W \ne W_{\text{data}}} f_\pi(W)} = \frac{267}{28} = 9.54$$

and an order-dependence artefact would have to be extreme to invert a margin approaching ten to one. For the
ordering of the second, third and fourth workstreams, at $28$, $24$ and $9$, the artefact could plausibly
reorder them, and no claim about that ordering should be read as established. The exact cost is derived here
instead of quoted, since it is the reason the shortcut is hard to defend. The
[Shapley value][research_shapley_1953] needs $\rho^{\text{unit}}$ evaluated on every subset of workstreams,

$$\bigl| 2^{\mathcal{W}} \bigr| = 2^{|\mathcal{W}|} = 2^{6} = 64$$

and each evaluation is one pass over 496 units. Since the exact Shapley attribution therefore requires only
sixty-four corpus passes, the honest characterisation is that the surrogate was used for scope reasons and
that the secondary ordering could be settled cheaply whenever it matters.

**The cheapness is a property of the aggregation, since the method itself does not become cheaper, and the distinction bounds how far the result generalises.**
Six workstreams give sixty-four subsets. The same attribution at instruction granularity ranges over subsets
of the unimplemented instruction set, which is not enumerable, and there the exact value is unavailable
rather than merely unattempted. **The literature has an answer for that regime**, in the sampling estimator
of [Castro, Gomez and Tejada 2009][research_castro_2009], which averages marginal gains over randomly drawn
permutations and converges at the usual rate in the number of samples, and in the closely related
attribution scheme of [Strumbelj and Kononenko 2013][research_strumbelj_kononenko_2013].
**Neither was needed here and both would be needed for any instruction-level restatement of the same question.**

The zero results are subject to the corpus caveat and are bounded above rather than asserted absent, as
quantified in the confidence-bound section. The correct inference is not that the typed arithmetic class
will never matter but that it does not matter now, which is the question an ordering principle asks.

The measurement is static. It counts instruction instances in compiled units, never executions, so it
estimates the difficulty of lowering a program and says nothing about the time a program spends in any
instruction. For the ordering question this is the correct unit, since a refusal is a static property, but
the resulting figures must not be read as execution profiles.
[Georges and colleagues 2007][research_georges_2007] set out why execution-time claims require a different
and considerably more careful methodology than the one applied here, and no such claim is made.

Finally, the measurement was performed by the same party that made the recommendation it falsifies, using an
instrument that party wrote. The guard assertion described in the method section addresses the most likely
failure mode of that arrangement, which is a silently empty sample, but it does not address the possibility
of a classification function whose workstream boundaries were drawn, unconsciously, to produce a tidy
result. The classification is a total function over sixty-six instructions and is available for inspection,
which is offered as mitigation rather than as a claim that the concern is closed.

## Pattern Extraction

The abstract mechanic generalises beyond compiler backends to any incremental capability programme in which
a consumer requires a conjunction of features rather than any one of them.

**The product form has a name as well, since it is the founding object of a mature discipline.** A system
that functions only when every one of its components functions is a series system, and the consequences of
that structure were worked out for reliability by [Esary and Proschan 1963][research_esary_proschan_1963].
**The attribution question this article poses has a direct counterpart there**, in the component importance
measure of [Birnbaum 1968][research_birnbaum_1968], which ranks components by the probability that the
system's functioning turns on that component alone. That is the same quantity as a blocking set, computed in
a different vocabulary.

The mechanic has three parts. First, when a consumer requires every element of a set to be present,
delivered capability is governed by the product form $\chi = \prod_i \mathbf{1}[\,\cdot\,]$ and not by the
sum form $\rho^{\text{inst}} = \frac{1}{N}\sum_i \mathbf{1}[\,\cdot\,]$, so per-element progress measures
overstate delivered capability by the gap $\Gamma$, which grows with the dispersion of the missing elements.
**That claim has computable extremes**, and the counting argument is the elementary one that underlies
covering problems generally, in [Karp 1972][research_karp_1972] and [Feige 1998][research_feige_1998]. With
$Q = N(1 - \rho^{\text{inst}})$ missing instances distributed over $M$ units, the number of blocked units is
bounded by

$$\Bigl\lceil Q / L_{\max} \Bigr\rceil \ \le\ \bigl| \{ m : \chi(c_m, S) = 0 \} \bigr| \ \le\ \min(Q, M)$$

**In the present case $Q = 9{,}318$ against $M = 496$, so maximal dispersion would block every unit**,
giving $\rho^{\text{unit}} = 0$ and $\Gamma = \rho^{\text{inst}} = 0.8731$. The observed 328 blocked units
and $\Gamma = 0.5344$ therefore sit well inside the dispersed extreme,
**which is the same fact the clustering coefficient of 5.51 reports and is an independent way of seeing it.**
Second, the natural ordering heuristics available to an implementer, which are implementation cost $\kappa$,
architectural elegance, and dependency depth, are all properties of elements considered in isolation, and
none carries information about $\lvert B(\iota, S) \rvert$. Third, the corrective is a frequency measurement over a
representative population of consumers, and the measurement satisfies

$$\kappa_{\text{measure}} \ll \kappa_{\text{work}}$$

characteristically by one to two orders of magnitude, because the cost of counting occurrences is nearly
independent of the cost of the work being ordered.

The observation is old. [Knuth 1971][research_knuth_1971] measured a corpus of FORTRAN programs precisely
because the profession's assumptions about which constructs mattered were untested, and
[Amdahl 1967][research_amdahl_1967] had already given the arithmetic showing that effort spent outside the
dominant term is bounded above by a small number regardless of how well it is spent. Writing $f$ for the
fraction of the work the improvement touches and $s$ for how much faster that fraction becomes,

$$\text{speedup} = \frac{1}{(1 - f) + f/s} \ \xrightarrow[\ s \to \infty\ ]{} \ \frac{1}{1 - f}$$

so an improvement addressing half the work cannot exceed a factor of two **however good it is**, a bound
[Gustafson 1988][research_gustafson_1988] later reframed without dissolving.
**The parallel to the present case is exact.** An instruction that blocks nothing is a term with $f = 0$,
and no quality of implementation raises its contribution above zero. The present article adds only that the
same asymmetry applies to feature ordering under a conjunctive consumer, that the dominant term is not
visible from the structure of the work, and that the conjunction makes the objective supermodular so that no
approximation guarantee is available to substitute for the measurement.

The mechanic carries a self-application. An implementer reasoning carefully about dependency structure
produces recommendations that feel well-founded, because they are well-founded with respect to the question
of what is required. The recommendation acquires unearned authority from the rigour of the dependency
argument, and the missing question is not visible from inside that argument. The defence is procedural and
not intellectual. Before accepting an ordering derived from structure, measure the frequency, and treat the
structural argument as establishing feasibility rather than priority.

A second self-application concerns the analysis itself, and this article contains four instances of it,
comprising a convexity shortcut, a false modularity theorem, a defect rate in citations supplied from
memory, and a misstatement of that rate over the worse subsample. All ran toward a more striking or
better-supported result, which is the direction least likely to attract scrutiny, and none was caught by
reading. Each was caught by an execution, respectively a numerical evaluation whose answer was implausible,
a brute-force enumeration over small instances, a query against an authoritative record, and a recount over
the full sample rather than the remembered one. That the fourth was committed inside the passage cautioning
against the first three is the clearest evidence available that awareness of a bias does not confer immunity
to it. The general defence is to test the apparatus on cases small enough to enumerate before trusting it on
the case of interest.

The general statement is that dependency analysis and demand measurement answer different questions, that
the first is more intellectually satisfying and more readily available to an implementer, and that ordering
decisions made on the first alone are unreliable in a direction the analysis itself cannot reveal.

## The Contemporary Literature

The seven traditions above are the ones the argument sits inside, and they were surveyed for what they
establish. **This section surveys what has happened lately**, on the standing expectation that an article of
this kind should double as a review of the contemporary literature. The reading is not neutral, since each
body of work is placed by what it says about the ordering question.

**The short version is that the question has become more urgent since it was posed, and no more answered.**

### The number of targets multiplied

**Backend bring-up used to be a rare activity performed by a few vendors, and it is now routine.** An open
instruction set with a ratified extension mechanism means anyone can add instructions, and the surrounding
literature covers custom extension design, automatic extension identification, application-specific
processors, accelerator compilation and vectorisation.

- [A proposed synthesis method for Application-Specific...][research_horvath_2015]
- [Accelerating H.264/HEVC video slice processing using...][research_mandal_2015]
- [Automatic complex instruction identification for...][research_nery_2015]
- [Efficient Compilation for Application Specific...][research_sohl_2015]
- [FPGA-based SHA-3 acceleration on a 32-bit processor via...][research_wang_2015]
- [Fast and accurate power estimation for...][research_hesselbarth_2015]
- [ISA customization for application specific instruction...][research_singh_2015]
- [Implementing an Application-Specific Instruction-Set...][research_heo_2015]
- [Timing speculation-aware instruction set extension for...][research_ahmed_2015]
- [A Domain-Specific Compiler for a Parallel Multiresolution...][research_rajbhandari_2016]
- [A RISC-V instruction set processor-micro-architecture...][research_raveendran_2016]
- [A basic linear algebra compiler for structured matrices][research_spampinato_2016]
- [An Application-Specific Instruction Set Processor for...][research_vaas_2016]
- [Application specific instruction set processor for sensor...][research_sisto_2016]
- [Development of a Code Generation Support System in...][research_kwon_2016]
- [Exploring Compiler Optimization Opportunities for the...][research_hayashi_2016]
- [Hardware implementation of a SHA-3 application-specific...][research_elmohr_2016]
- [Matlab to C Compilation Targeting Application Specific...][research_latifis_2016]
- [Oolong: A Baseband processor extension to the RISC-V ISA][research_melo_2016]
- [Outer-Loop Auto-Vectorization for SIMD Architectures...][research_dong_2016]
- [Regression Test Suites Optimization for...][research_zachariaova_2016]
- [SHA-3 Instruction Set Extension for A 32-bit RISC...][research_eissa_2016]
- [Vectorization in PyPy's Tracing Just-In-Time Compiler][research_plangger_2016]
- [Video SIMDBench: Benchmarking the Compiler Vectorization...][research_alvanos_2016]
- [A Domain-Specific Language and Compiler for...][research_yu_2017]
- [A MATLAB Vectorizing Compiler Targeting...][research_latifis_2017]
- [Application-Specific Instruction Set Processors for Video...][research_kim_2017]
- [Automatic generation of fast BLAS3-GEMM: A portable...][research_su_2017]
- [Compiler Techniques for Efficient MATLAB to OpenCL Code...][research_reis_2017]
- [Compiler auto-vectorization of matrix multiplication...][research_lambert_2017]
- [Design of an Application Specific Instruction Set...][research_xiao_2017]
- [Domain specific compiler for coordinated signal...][research_li_2017]
- [Instruction set extension and hardware acceleration for...][research_pang_2017]
- [Intermediate-Code Generation][research_mogensen_2017]
- [Machine-Code Generation][research_mogensen_2017_b]
- [Metacasanova: an optimized meta-compiler for...][research_digiacomo_2017]
- [Metamodeling and Code Generation in the Hardware/Software...][research_ecker_2017]
- [Polyhedral Compiler Technology in Collaboration with...][research_hall_2017]
- [SuperGraph-SLP Auto-Vectorization][research_porpodas_2017]
- [A compiler for cyber-physical digital microfluidic...][research_curtis_2018]
- [A low-cost synthesizable RISC-V dual-issue processor core...][research_patsidis_2018]
- [An application specific instruction set processor (ASIP)...][research_hu_2018]
- [Automatic Configurable Hardware Code Generation for...][research_tsoeunyane_2018]
- [CAnDL: a domain specific language for compiler analysis][research_ginsbach_2018]
- [COpt: A High Level Domain-Specific Language to Generate...][research_venkat_2018]
- [Design and Simulation Of 64-Bit Hybrid Processor...][research_ms_2018]
- [Design of RLWE Cryptoprocessor Based on...][research_zhang_2018]
- [Dominance-based duplication simulation (DBDS): code...][research_leopoldseder_2018]
- [Optimization of Specific Instruction Set Processor for...][research_lei_2018]
- [System on Chip Implementation of Compiler Stack with a...][research_ismael_2018]
- [A compiler architecture for domain-specific type error...][research_serrano_2019]
- [An Application-Specific VLIW Processor with Vector...][research_bytyn_2019]
- [An Application-specific Instruction Set Processor for...][research_brenes_2019]
- [An Efficient Application Specific Instruction Set...][research_huang_2019]
- [Application Specific Instruction Set Processor Design for...][research_samal_2019]
- [Compiler-Assisted Selection of Hardware Acceleration...][research_zacharopoulos_2019]
- [Compiler-support for Critical Data Persistence in NVM][research_elkhouly_2019]
- [Enhancing Python Compiler Error Messages via Stack][research_thiselton_2019]
- [Proposal of Scalable Vector Extension for Embedded RISC-V...][research_kimura_2019]
- [Research on Instruction Set Architecture of 40-Bit...][research_anon_2019]
- [Translating CUDA to OpenCL for Hardware Generation using...][research_kim_2019]
- [A Compiler Comparison in the RISC-V Ecosystem][research_poorhosseini_2020]
- [Agile Autotuning of a Transprecision Tensor Accelerator...][research_diamantopoulos_2020]
- [BOSON - Application-Specific Instruction Set Processor...][research_mazurek_2020]
- [Lightweight Cryptographic Instruction Set Extension on...][research_eisenkraemer_2020]
- [Really Embedding Domain-Specific Languages into C++][research_finkel_2020]
- [A RISC-V Post Quantum Cryptography Instruction Set...][research_nannipieri_2021]
- [An Agile Instruction Set Extension Method Based on the...][research_hu_2021]
- [An Interval Compiler for Sound Floating-Point Computations][research_rivera_2021]
- [Compact native code generation for dynamic languages on...][research_jamieson_2021]
- [Development of RISC-V Based Soft-core Processor with...][research_kimura_2021]
- [Exploring the RISC-V Vector Extension for the Classic...][research_pircher_2021]
- [MLIR: Scaling Compiler Infrastructure for Domain Specific...][research_lattner_2021]
- [RISC-VTF: RISC-V Based Extended Instruction Set for...][research_jiao_2021]
- [Relaxed Peephole Optimization: A Novel Compiler...][research_liu_2021]
- [SSA Form and Code Generation][research_dupontdedinech_2021]
- [Variable Bit-Precision Vector Extension for RISC-V Based...][research_rk_2021]
- [A Compiler for Sound Floating-Point Computations using...][research_rivera_2022]
- [A Pluggable Vector Unit for RISC-V Vector Extension][research_maisto_2022]
- [A Trigonometric Function Instruction Set Extension Method...][research_gao_2022]
- [An Efficient Application Specific Instruction Set...][research_liu_2022]
- [Audio Denoising Coprocessor Based on RISC-V Custom...][research_yuan_2022]
- [Automatic compiler/interpreter generation from programs...][research_kovacevic_2022]
- [Automating Cryptographic Code Generation][research_yarom_2022]
- [Backward Graph Construction and Lowering in DL Compiler...][research_kwon_2022]
- [Bratter: An Instruction Set Extension for Forward...][research_park_2022]
- [Communications Signal Processing Using RISC-V Vector...][research_razilov_2022]
- [Design of RISC Processor with IEEE754 Standard...][research_ozkilbac_2022]
- [Effective Performance Modeling and Domain-Specific...][research_xu_2022]
- [Efficient Support of the Scan Vector Model for RISC-V...][research_lai_2022]
- [Just-In-Time Compiler System in Aspect-Oriented...][research_ishimura_2022]
- [Lowering Barriers to Application Development With...][research_perezalvarez_2022]
- [MLIR-based code generation for GPU tensor cores][research_katel_2022]
- [OpenASIP 2.0: Co-Design Toolset for RISC-V...][research_hepola_2022]
- [RVVRadar: A Framework for Supporting the Programmer in...][research_klemmer_2022]
- ["A Multi-Pass Compiler with Code Optimized Abstract...][research_odim_2023]
- [A RISC-V Instruction Set Extension for Flexible...][research_lozachmeur_2023]
- [A buffer overflow detection and defense method based on...][research_liu_2023]
- [An extension to the RISC-V instruction set architecture...][research_jones_2023]
- [Artifact for Lifting Code Generation of Cardiac...][research_thangamani_2023]
- [Automatically Localizing Dynamic Code Generation Bugs in...][research_lim_2023]
- [Building a domain-specific compiler for emerging...][research_li_2023]
- [Design and Implementation of a Compiler Supporting RISC-V...][research_zou_2023]
- [Design, development and testing of a 16-bit reduced...][research_jain_2023]
- [Efficient Compiler Design for a Geometric Shape...][research_gupta_2023]
- [Evaluating RISC-V Vector Instruction Set Architecture...][research_li_2023_b]
- [Flexible and Efficient Implementation of CRYSTALS-KYBER...][research_zhang_2023]
- [FlowPix: Accelerating Image Processing Pipelines on an...][research_choudhury_2023]
- [Implementation and Reliability Evaluation of a RISC-V...][research_imianosky_2023]
- [Integration of a Real-Time CCSDS 410.0-B-32...][research_kuo_2023]
- [JIT Compiler Security through Low-Cost RISC-V Extension][research_ducasse_2023]
- [Lifting Code Generation of Cardiac Physiology Simulation...][research_thangamani_2023_b]
- [PEMBANGUNAN COMPILER DOMAIN SPECIFIC LANGUAGE SEBAGAI...][research_adiyoso_2023]
- [PIMFlow: Compiler and Runtime Support for CNN Models on...][research_shin_2023]
- [RISC-V Instruction Set Architecture Extensions: A Survey][research_cui_2023]
- [Resource-efficient RISC-V Vector Extension Architecture...][research_islam_2023]
- [The Design of Optimized RISC Processor for Edge...][research_oh_2023]
- [Vectorized Nonlinear Functions with the RISC-V Vector...][research_bavier_2023]
- [A Tensor Algebra Compiler for Sparse Differentiation][research_shaikhha_2024]
- [An FPGA-Based RISC-V Instruction Set Extension and Memory...][research_ibrahim_2024]
- [An MLIR-Based Compiler for Hardware Acceleration with...][research_li_2024]
- [Compile-Time Analysis of Compiler Frameworks for Query...][research_engelke_2024]
- [Compiler Testing with Relaxed Memory Models][research_geeson_2024]
- [Configurable Loop Shuffling via Instruction Set Extensions][research_cui_2024]
- [Convex: A RISC-V Instruction Set Extension Scheme for...][research_liu_2024]
- [Designing RISC-V Instruction Set Extensions for...][research_balasubramania_2024]
- [Enabling Fine-Grained Incremental Builds by Making...][research_han_2024]
- [Evaluating and optimising compiler code generation for...][research_jesus_2024]
- [Fast Template-Based Code Generation for MLIR][research_drescher_2024]
- [Fully Automatic Compiler Retargeting and CV-X-IF Hardware...][research_hepola_2024]
- [High Performance Instruction-Data Level Parallelism Based...][research_israel_2024]
- [Implementation of Application Specific Instruction set...][research_deole_2024]
- [Improving the Accuracy of Batik Classification using Deep...][research_dzulqarnain_2024]
- [Intermediate-Code Generation][research_mogensen_2024]
- [LLVM Library for a Dedicated Processor Instruction Set –...][research_zubert_2024]
- [Machine-Code Generation][research_mogensen_2024_b]
- [RVCE-FAL: A RISC-V Scalar-Vector Custom Extension for...][research_yu_2024]
- [Special Session: Reliability and Performance Evaluation...][research_imianosky_2024]
- [Whose Baseline Compiler is it Anyway?][research_titzer_2024]
- [eCC++ : A Compiler Construction Framework for Embedded...][research_tallada_2024]
- [A Domain-Specific Compiler for Embedded DSP Development...][research_zhu_2025]
- [A Graph-Based Learning Framework for Compiler Loop...][research_xiao_2025]
- [A RISC-V Vector Extension for Multi-word Arithmetic][research_lan_2025]
- [A Way to Identify Potential Functions for Vectorization...][research_stojkovic_2025]
- [AI Edge Processor Using RISC - V Instruction Set...][research_borade_2025]
- [Accelerating Machine Learning using RISC-V Vector...][research_nunes_2025]
- [Accelerating Machine Learning with RISC-V Vector...][research_nunes_2025_b]
- [Accelerating NTT with RISC-V Vector Extension for Fully...][research_rodrigues_2025]
- [Acceleration of McEliece Cryptosystem with Instruction...][research_kennedy_2025]
- [Analysis of the RISC-V Vector Extension for Vulkan...][research_troiber_2025]
- [Application-Specific Instruction Set Processor][research_chakravarthi_2025]
- [Compiler-Like Code Generation for fUML: Reducing Overhead...][research_hammer_2025]
- [Efficient TinyML Inference on a Fault-Tolerant RISC-V SoC...][research_imianosky_2025]
- [Eight-Bit Vector SoftFloat Extension for the RISC-V Spike...][research_marcelli_2025]
- [Fast Interpreter-Based Instruction Set Simulation for...][research_schlagl_2025]
- [Finding Bugs in MLIR Compiler Infrastructure via Lowering...][research_liang_2025]
- [Functional Validation of the RISC-V Unlimited Vector...][research_fernandes_2025]
- [Key Operator Vectorization for LeNet and ResNet Based on...][research_chen_2025]
- [Logic Gate Network Inference Acceleration with RISC-V...][research_wang_2025]
- [Low-Power Implementation of DSP Instruction Set Extension...][research_li_2025]
- [Microarchitecture Design and Benchmarking of Custom SHA-3...][research_bolat_2025]
- [Optimizing TinyEngine for the RISC-V Vector Extension][research_tan_2025]
- [Performance Evaluation of CNN using RISC-V Vector...][research_okawara_2025]
- [RI-MAC: Optimising MAC Operation Using Custom RISC-V...][research_longchar_2025]
- [RISC-TAE: Instruction Set Extension for Transformer Model...][research_liu_2025]
- [RISC-V SIMD Instructions - Vector Extension (Load/Store)][research_b_2025]
- [RISC‐V Processor Hardware Modelling with Custom...][research_antony_2025]
- [Research on RISC-V-based Edge Convolution Acceleration...][research_luan_2025]
- [SySTeC: A Symmetric Sparse Tensor Compiler][research_patel_2025]
- [Tensor Program Optimization for the RISC-V Vector...][research_peccia_2025]
- [TinyML Unleashed: Accelerating TensorFlow Lite Micro...][research_mahmoudi_2025]
- [A Reinforcement Learning Environment for Automatic Code...][research_tirichine_2026]
- [An Embedded RISC-V Vector Extension for Edge-Oriented...][research_corral_2026]
- [CKTI: A Domain-Specific Compiler for Lowering CUDA...][research_shi_2026]
- [CREF-Lang: A domain-specific language and compiler for...][research_undheim_2026]
- [Compiler-ASR: Bridging the IR-to-Assembly Gap for...][research_zhang_2026]
- [Compiler-Assisted Instruction Fusion][research_reddy_2026]
- [Design Space Exploration of RISC-V Vector Extension...][research_nunes_2026]
- [Enabling Automatic Compiler-Driven Vectorization of...][research_alladi_2026]
- [Evaluation and Benefit Modeling of Auto-Vectorization...][research_yao_2026]
- [Exploring Instruction Set Extension Emulation for...][research_gorius_2026]
- [FPGA-Based ORB Accelerator: Effects of Compiler...][research_rostum_2026]
- [FWHT-RVV: A RISC-V vector processor with FWHT instruction...][research_lv_2026]
- [Hikami: A Lightweight Hypervisor for Emulating RISC-V...][research_takana_2026]
- [Instruction Set Optimization for FM-Type Digital Signal...][research_ayeoribe_2026]
- [PERFORMANCE EVALUATION OF THE UETRV-PCORE USING RISC-V...][research_zia_2026]
- [TPDE: A Fast Adaptable Compiler Back-End Framework][research_schwarz_2026]
- [Thinking Fast and Correct: Automated Rewriting of...][research_qian_2026]
- [TinyGen: Portable and Compact Code Generation for Tiny...][research_ko_2026]
- [Vmxdotp: A RISC-V Vector ISA Extension for Efficient...][research_wipfli_2026]

**Every one of those projects faces the ordering question and none of the papers answers it.** The
extension-identification work comes closest, since it selects instructions by measured frequency over a
corpus,
**but it selects instructions to ADD TO A COMPLETE MACHINE for speed, not instructions to implement next in an incomplete compiler for capability.**
The objective is a sum in that setting and a product in this one, which is the whole difference.

### And one target the entire industry had to bring up at once

WebAssembly is the closest thing to a natural experiment. A new target appeared, and a great many
implementations were brought up against it more or less simultaneously, producing work on runtimes, formal
semantics, binary size, ahead-of-time compilation and runtime bugs.

- [Adjustable-Cost Overlays for Runtime Compilation][research_coole_2015]
- [Augmenting JavaScript JIT with ahead-of-time compilation][research_zhuykov_2015]
- [Bytecode-to-C Ahead-of-Time Compilation for Android...][research_oh_2015]
- [Error-tolerant processors: Formal specification and...][research_golnari_2015]
- [Executable Semantics for the Formal Specification and...][research_qasim_2015]
- [Formal Semantics of Runtime Monitoring, Verification...][research_chen_2015]
- [Is dynamic compilation possible for embedded systems?][research_charles_2015]
- [Javascript ahead-of-time compilation for embedded web...][research_park_2015]
- [Runtime Value Numbering: A Profiling Technique to...][research_wen_2015]
- [Automated formal verification of the refined...][research_maron_2016]
- [Modular specification and verification of a...][research_mcmillan_2016]
- [Testing-Based Formal Verification for Theorems and Its...][research_liu_2016]
- [Advanced ahead-of-time compilation for Javascript engine][research_park_2017]
- [Ahead-of-time compilation of JavaScript programs][research_zhuykov_2017]
- [DAME: Runtime-compilation for data movement][research_prabhu_2017]
- [Enhancing formal specification and verification of...][research_alrefai_2017]
- [Erratum to: Formal Description Techniques and Protocol...][research_budkowski_2017]
- [Formal Specification and Verification of Security...][research_zhioua_2017]
- [Formal verification of ABAP by Z specification][research_rodruksa_2017]
- [Hyperhierarchy of Semantics - A Formal Framework for...][research_mastroeni_2017]
- [KART – A Runtime Compilation Library for Improving HPC...][research_noack_2017]
- [Formal Specification and Verification of Self-Adaptive...][research_fakhir_2018]
- [HiPEAC compilation architecture][research_debosschere_2018]
- [Intrinsic Compilation Model to enhance Performance of...][research_aradhya_2018]
- [Reusing the Optimized Code for JavaScript Ahead-of-Time...][research_park_2018]
- [A Customized Real-Time Compilation for Motion Control in...][research_wu_2019]
- [Floating-point Semantics of Analyzed Programs][research_garoche_2019]
- [Formal Specification Technique in Smart Contract...][research_lee_2019]
- [Formal Specification and Verification of Smart Contracts][research_jiao_2019]
- [Formal specification and verification][research_merz_2019]
- [Improved Ahead-of-time Compilation of Stack-based JVM...][research_reijers_2019]
- [POSTER: Runtime Adaptations for Energy-Efficient VSLAM][research_khalufa_2019]
- [Towards a WebAssembly standalone runtime on GraalVM][research_salim_2019]
- [Analysis of WebAssembly as a Strategy to Improve...][research_oliveira_2020]
- [Conclusion: Debugging Blazor WebAssembly][research_himschoot_2020]
- [Introducing H, an Institution-Based Formal Specification...][research_diaconescu_2020]
- [Runtime prediction of high-performance computing jobs...][research_chen_2020]
- [Synchronized Shared Memory and Procedural Abstraction...][research_gretz_2020]
- [Targeting both Blazor Server and Blazor WebAssembly][research_himschoot_2020_b]
- [Valent-Blocks: Scalable High-Performance Compilation of...][research_scheidl_2020]
- [A Case Study in Formal Specification and Runtime...][research_luppen_2021]
- [A Self-certifying Compilation Framework for WebAssembly][research_namjoshi_2021]
- [Correction: A Case Study in Formal Specification and...][research_luppen_2021_b]
- [Formal Specification and Verification of MQTT Protocol in...][research_akhtar_2021]
- [HERTI: A Reinforcement Learning-Augmented System for...][research_han_2021]
- [On the Runtime and Energy Performance of WebAssembly: Is...][research_demacedo_2021]
- [Runtime Metric Analysis in NoSQL Database Performance...][research_andor_2021]
- [Twine: An Embedded Trusted Runtime for WebAssembly][research_menetrey_2021]
- [Vivienne: Relational Verification of Cryptographic...][research_tsoupidi_2021]
- [WAFL: Binary-Only WebAssembly Fuzzing with Fast Snapshots][research_haler_2021]
- [WebAssembly Module Internals: Sections and Memory Model][research_jain_2021]
- [Breaking the Vendor Lock][research_doerfert_2022]
- [Formal Verification of SUBLEQ Microcode implementing the...][research_klemmer_2022_b]
- [On JavaScript Ahead-of-Time Compilation Performance...][research_serrano_2022]
- [Potential of WebAssembly for Embedded Systems][research_wallentowitz_2022]
- [WaTZ: A Trusted WebAssembly Runtime Environment with...][research_menetrey_2022]
- [WebAssembly versus JavaScript: Energy and Runtime...][research_demacedo_2022]
- [A Comprehensive Study of Bugs in Embedded WebAssembly...][research_zheng_2023]
- [A Comprehensive Study of WebAssembly Runtime Bugs][research_wang_2023]
- [Automated WebAssembly Function Purpose Identification...][research_romano_2023]
- [CWASI: A WebAssembly Runtime Shim for Inter-function...][research_marcelino_2023]
- [Characterizing and Detecting WebAssembly Runtime Bugs][research_zhang_2023_b]
- [Formal Specification and Verification of JDK’s Identity...][research_deboer_2023]
- [Formal Verification Platform as a Service: WebAssembly...][research_deng_2023]
- [High-Performance Web Frontend Using WebAssembly][research_lyu_2023]
- [Hybrid Execution: Combining Ahead-of-Time and...][research_pichler_2023]
- [Of Ahead Time: Evaluating Disassembly of Android Apps...][research_bleier_2023]
- [Optimizing Tensor Computations: From Applications to...][research_boehm_2023]
- [Profile Guided Optimization Transfer-Learning for...][research_he_2023]
- [Studying WebAssembly and comparison of its performance...][research_rokotyanskaya_2023]
- [Support for Just-in-Time Compilation of WebAssembly for...][research_moron_2023]
- [WaVe: a verifiably secure WebAssembly sandboxing runtime][research_johnson_2023]
- [WasmSlim: Optimizing WebAssembly Binary Distribution via...][research_wen_2023]
- [When Function Inlining Meets WebAssembly...][research_romano_2023_b]
- [A Compilation of Experimental Binary Alloy Surface...][research_mazurowski_2024]
- [A Comprehensive Trusted Runtime for WebAssembly With...][research_menetrey_2024]
- [A Semantics of Structures, Unions, and Underspecified...][research_gauthier_2024]
- [Accelerating Embedded WebAssembly Based on FPGA][research_kim_2024]
- [Ahead-of-time Compilation for Diverse Samplers of...][research_madkour_2024]
- [Bringing Binary Exploitation at Port 80: Understanding C...][research_massidda_2024]
- [Challenges of Multilingual Program Specification and...][research_furia_2024]
- [Characterizing Dynamic Memory Behavior in WebAssembly...][research_qin_2024]
- [Formal Specification and Verification of MQTT Protocol...][research_talamali_2024]
- [SCALE-Ahead-Of-Time Compilation of CUDA for AMD GPUs][research_pavlidakis_2024]
- [TreeHouse: An MLIR-based Compilation Flow for Real-Time...][research_su_2024]
- [WARDuino: An embedded WebAssembly virtual machine][research_lauwaerts_2024]
- [Wapplique: Testing WebAssembly Runtime via Execution...][research_zhao_2024]
- [Wasm-Mutate: Fast and effective binary diversification...][research_cabreraarteaga_2024]
- [WebAssembly as a Fuzzing Compilation Target (Registered...][research_bauckholt_2024]
- [A QUANTITATIVE ANALYSIS OF WEBASSEMBLY INTEGRATION...][research_stepanov_2025]
- [A Two-step Approach to Find Short Compilation...][research_delatorre_2025]
- [Adaptivity in AdaptiveCpp: Optimizing Performance by...][research_alpay_2025]
- [Ahead of Time Generation for GPSA Protection in RISC-V...][research_savary_2025]
- [Application of WebAssembly for High-Performance...][research_anon_2025]
- [Archs: A WebAssembly Runtime for Cross-host Heterogeneous...][research_sun_2025]
- [Benchmarking WebAssembly for Embedded Systems][research_moron_2025]
- [Bringing Together Cross-ISA Checkpoint/Restoration and...][research_tamura_2025]
- [CWAMR: REIMAGINING A CAPABILITYBASED WEBASSEMBLY RUNTIME...][research_subramanyan_2025]
- [Calibro: Compilation-Assisted Linking-Time Binary Code...][research_liang_2025_b]
- [Detecting WebAssembly Runtime Bugs With Grammar-Guided...][research_lu_2025]
- [Distinguishability-Guided Test Program Generation for...][research_jiang_2025]
- [Ductape: Optimizing Dynamically Typed Programs Using...][research_harif_2025]
- [Ensuring Reliability in Self-Adaptive Systems: A...][research_basiturrahim_2025]
- [ForMAt: Formal Verification of Scalable Multiply and...][research_weingarten_2025]
- [Formal Specification and Verification of Smart...][research_yoon_2025]
- [FreeWavm: Enhanced WebAssembly Runtime Fuzzing Guided by...][research_qian_2025]
- [Furina: A Light-weight WebAssembly Runtime for ICS][research_lei_2025]
- [Hybrid WebAssembly-Container Orchestration in Embedded...][research_fan_2025]
- [HybridServe: Adaptive WebAssembly-Container Runtime...][research_kang_2025]
- [Investigating the Role of Formal Verification in Software...][research_masoudi_2025]
- [Lumos: Performance Characterization of WebAssembly as a...][research_marcelino_2025]
- [Performance and Usability Implications of Multiplatform...][research_kakati_2025]
- [Research of WebAssembly usage for high-performance code...][research_soluian_2025]
- [Runtime prediction model for high performance computing...][research_tian_2025]
- [Seamless Self-Healing in WebAssembly Container...][research_matsubara_2025]
- [Self-Hosted WebAssembly Runtime for Runtime-Neutral...][research_nakata_2025]
- [Specification and Formal Verification of...][research_trippel_2025]
- [Specification and Verification of a Formal Model for a...][research_anon_2025_b]
- [Typestates Specification and Verification in Frama-C][research_patte_2025]
- [WBSan: WebAssembly Bug Detection for Sanitization and...][research_wu_2025]
- [WebAssembly for Container Runtime: Are We There Yet?][research_liu_2025_b]
- [An Analysis of Modern Web Security Vulnerabilities Inside...][research_corrias_2026]
- [QJWasm: A lightweight runtime system for efficient...][research_hu_2026]
- [Stack-based static WebAssembly binary slicing and...][research_choi_2026]
- [SurtGIS: A high-performance raster geospatial analysis...][research_parra_2026]
- [Unleashing Triton on CPUs: Compilation and Runtime...][research_li_2026]
- [WARD: Efficient Memory Protection for WebAssembly on Tiny...][research_shin_2026]
- [Wasm-WCET: Worst-Case Execution-Time Analysis of...][research_seidler_2026]
- [WasmWeaver: A Framework for Runtime-Aware WebAssembly...][research_muller_2026]

**The interesting absence is that none of it reports a bring-up ORDER.** The specifications say what the
instruction set is, the papers say how fast the result runs, and the sequence in which the implementers
built it is not treated as a research object.

### The middle of the compiler became shared infrastructure

Lowering is now typically staged through a series of intermediate representations instead of performed in
one step, and the infrastructure for that is common property.

- [LAYANAN CLOUD COMPUTING BERBASIS INFRASTRUCTURE AS A...][research_wintolo_2015]
- [LLVM parallel intermediate representation][research_khaldi_2015]
- [LLVM-based communication optimizations for PGAS programs][research_hayashi_2015]
- [PENERAPAN PEMROSESAN PARALEL UNTUK MENGUJI WAKTU...][research_ngadiyono_2015]
- [Modular SDN Compiler Design with Intermediate...][research_li_2016]
- [The ARES High-Level Intermediate Representation][research_moss_2016]
- [Towards Automatic HBM Allocation Using LLVM: A Case Study...][research_khaldi_2016]
- [Multi-level physical hierarchy floorplanning using IC...][research_roze_2017]
- [A cost model for a graph-based...][research_leopoldseder_2018_b]
- [AIWC: OpenCL-Based Architecture-Independent Workload...][research_johnston_2018]
- [CLACC: Translating OpenACC to OpenMP in Clang][research_denny_2018]
- [Compiler and language design for quantum computing...][research_heim_2018]
- [Function/Kernel Vectorization via Loop Vectorizer][research_masten_2018]
- [LLVM and the Automatic Vectorization of Loops Invoking...][research_petrogalli_2018]
- [OP2-Clang: A Source-to-Source Translator Using Clang/LLVM...][research_balogh_2018]
- [OpenMP GPU Offload in Flang and LLVM][research_ozen_2018]
- [The CakeML Compiler Explorer][research_hjort_2018]
- [User-Directed Loop-Transformations in Clang][research_kruse_2018]
- [Comparing Mutation Testing at the Levels of Source Code...][research_hariri_2019]
- [Design of Cyanobyte: An Intermediate Representation to...][research_felker_2020]
- [Flexible Runtime Reconfigurable Computing Overlay...][research_shah_2020]
- [Introducing multi-level parallelism, at coarse, fine and...][research_gratien_2020]
- [LLHD: a multi-level intermediate representation for...][research_schuiki_2020]
- [Leveraging Compiler Intermediate Representation for...][research_garzella_2020]
- [Replication Package for Paper: LLHD: A Multi-level...][research_schuiki_2020_b]
- [Robust Practical Binary Optimization at Run-time using...][research_engelke_2020]
- [Static Neural Compiler Optimization via Deep...][research_mammadli_2020]
- [3CPS: The Design of an Environment-Focussed Intermediate...][research_quiring_2021]
- [A High Performance Sparse Tensor Algebra Compiler in MLIR][research_tian_2021]
- [Building SSA in a Compiler for PHP][research_biggar_2021]
- [Extending LLVM IR for DPC++ Matrix Support: A Case Study...][research_khaldi_2021]
- [Facilitating CoDesign with Automatic Code Similarity...][research_nguyen_2021]
- [Flacc: Towards OpenACC support for Fortran in the LLVM...][research_clement_2021]
- [Functional Representations of SSA][research_beringer_2021]
- [Improved Circuit Compilation for Hybrid MPC via Compiler...][research_demmler_2021]
- [Integrating a functional pattern-based IR into MLIR][research_lucke_2021]
- [Redundancy Elimination][research_chow_2021]
- [STERILIZER CHAMBER DESIGN WITH TELEGRAM-BASED INTERNET OF...][research_kusumaningrum_2021]
- [Toward an Automated Hardware Pipelining LLVM Pass...][research_leidel_2021]
- [An MLIR-based Compiler Flow for System-Level Design and...][research_agostini_2022]
- [Caffeine: CoArray Fortran Framework of Efficient...][research_rouson_2022]
- [Design of automatic aircraft parking system module...][research_kusumaningrum_2022]
- [Logic Synthesis with Design Compiler][research_chin_2022]
- [Reinforcement Learning Strategies for Compiler...][research_shahzad_2022]
- [SPNC: An Open-Source MLIR-Based Compiler for Fast...][research_sommer_2022]
- [ScaleHLS: A New Scalable High-Level Synthesis Framework...][research_ye_2022]
- [Towards Supporting Semiring in MLIR-Based COMET Compiler][research_guo_2022]
- [Unleashing the power of compiler intermediate...][research_li_2022]
- [Use of Compiler Intermediate Representation for Reverse...][research_mzid_2022]
- [ASPIRE: An Intermediate Representation for Abstract...][research_bhamidipati_2023]
- [INR-Arch: A Dataflow Architecture and Compiler for...][research_abikaram_2023]
- [Intermediate Representations][research_cooper_2023]
- [LAGrad: Statically Optimized Differentiable Programming...][research_peng_2023]
- [MLIRSmith: Random Program Generation for Fuzzing MLIR...][research_wang_2023_b]
- [Experiences Building an MLIR-Based SYCL Compiler][research_tiotto_2024]
- [Fully integrating the Flang Fortran compiler with...][research_brown_2024]
- [Fuzzing MLIR Compiler Infrastructure via Operation...][research_suo_2024]
- [MLIR-Based Homomorphic Encryption Compiler for GPU][research_nozaki_2024]
- [MLIR-to-CGRA: A Versatile MLIR-Based Compiler Framework...][research_yu_2024_b]
- [Open-Source MLIR-Based Intermediate Representation for...][research_kamkin_2024]
- [Paddle-Mlir: A Compiler Based on MLIR for Accelerating...][research_huang_2024]
- [VCNN: A compiler of CNNs based on MLIR for multi-core...][research_chen_2024]
- [An Innovation Study on Luggage Wheel Design for Seamless...][research_kurudirek_2025]
- [DESIL: Detecting Silent Bugs in MLIR Compiler...][research_suo_2025]
- [Enhancing Compiler Design for Machine Learning Workflows...][research_ankushjitendra_2025]
- [MLIR: A Panacea for ML Compiler Challenges?][research_agrawal_2025]
- [P4IRS: An intermediate representation and compiler for...][research_raveduttilucio_2025]
- [PolyMorphous: An MLIR-Based Polyhedral Compiler with Loop...][research_zhao_2025]
- [The MLIR Transform Dialect][research_lucke_2025]
- [Towards a Unified Multi-Target Mlir-Based Compiler: A...][research_letras_2025]
- [CombRewriter: Enabling Combinational Logic Simplification...][research_zheng_2026]
- [Compiling Linear Algebra Workloads from C to Quantum...][research_conte_2026]
- [GeoIR-Compiler: A Geospatial Intermediate Representation...][research_zhang_2026_b]
- [Quantum Circuit Synthesis from C via Multi-Level...][research_lancellotti_2026]
- [Quantum Oracle Synthesis from HDL Designs via Multi Level...][research_lancellotti_2026_b]
- [RV-IR: An MLIR-Based Architecture-Aware Intermediate...][research_jian_2026]

**Staging multiplies the number of lowering steps and does not touch the conjunction problem.** A program
still needs every step on its path.
**A partially implemented lowering pipeline has the same product form as a partially implemented instruction set**,
one level up, which suggests the measure generalises and does not suggest anyone has measured it.

### Selection and synthesis moved on from the classics

The instruction-selection tradition surveyed earlier did not stop in 1999. Selection is surveyed as a field,
superoptimisation became practical, peephole rules are generated and verified automatically, and program
synthesis acquired solver-based and syntax-guided formulations.

- [A Formal Approach based on Fuzzy Logic for the...][research_koutsoumpas_2015]
- [An innovative approach for automatic generation...][research_sortino_2015]
- [Counterexample-guided simulation framework for formal...][research_patil_2015]
- [Finding Good Compiler Optimization Sets - A Case-based...][research_queirozjunior_2015]
- [Keynote talk I: Syntax-guided synthesis][research_alur_2015]
- [PERANCANGAN PENGAMANAN SERVER SECARA OTOMATIS MENGGUNAKAN...][research_kusumaningrum_2015]
- [The Correctness-Security Gap in Compiler Optimization][research_dsilva_2015]
- [Alive-FP: Automated Verification of Floating Point Based...][research_menendez_2016]
- [Automatic Testbench Generation for Simulation-based...][research_weissnegger_2016]
- [Automatic data layout generation and kernel mapping for...][research_majeti_2016]
- [Counterexample-guided diagnosis][research_riener_2016]
- [A New Functional-Logic Compiler for Curry: Sprite][research_antoy_2017]
- [Accurate quasi-P traveltimes in 3D transversely isotropic...][research_padhi_2017]
- [Automatic Generation of the AADL ALISA Verification Plan...][research_wu_2017]
- [Automatic generation of simulation workflows for system...][research_hammadi_2017]
- [Counterexample-guided approach to finding numerical...][research_nguyen_2017]
- [HSS cluster-based direct solver for acoustic wave equation][research_kostin_2017]
- [Look for the Proof to Find the Program...][research_gascon_2017]
- [Automatic security verification of mobile app...][research_costa_2018]
- [Compiler optimization for scientific computation in C/C++][research_botor_2018]
- [Fast and flexible instruction selection with constraints][research_thier_2018]
- [Synthesizing an instruction selection rule library from...][research_buchwald_2018]
- [A Survey of Automatic Generation of Source Code Comments...][research_song_2019]
- [Accurate quasi-SV traveltimes in 3D transversely...][research_padhi_2019]
- [AliveInLean: A Verified LLVM Peephole Optimization...][research_lee_2019_b]
- [Alumni’s Perception on Program Specification of ELT...][research_refnaldi_2019]
- [Automatic Verification of FSA Strategies via...][research_luo_2019]
- [Design and Development of Bridge AI bid Program based on...][research_zhang_2019]
- [FrAngel: component-based synthesis with control structures][research_shi_2019]
- [Multi-target Compiler for the Deployment of Machine...][research_castrolopez_2019]
- [An Empirical Study of Counterexample-Guided Fuzzing for...][research_yi_2020]
- [An approach to generate text-based IDEs for syntax...][research_sasano_2020]
- [Artifact for article: Exact and Approximate Methods for...][research_hu_2020]
- [Automatic Generation of Multi-Objective Polyhedral...][research_chelini_2020]
- [Automatic compiler optimization on embedded software...][research_werner_2020]
- [Boosting component-based synthesis with control structure...][research_liu_2020]
- [Dataflow-based pruning for speeding up superoptimization][research_mukherjee_2020]
- [Exact and approximate methods for proving unrealizability...][research_hu_2020_b]
- [Grammar Filtering for Syntax-Guided Synthesis][research_morton_2020]
- [Performance Improvement of Kotlin Program in...][research_sonoyama_2020]
- [Specification and automatic verification of trust-based...][research_drawel_2020]
- [Automatic Verification of Data Summaries][research_rezgui_2021]
- [Can reactive synthesis and syntax-guided synthesis be...][research_choi_2021]
- [Compression Optimization For Automatic Verification of...][research_wang_2021]
- [Counterexample Guided Inductive Repair of Reactive...][research_hussein_2021]
- [EMPIRICAL INVESTIGATION OF CLOUD, GRID AND VIRTUALIZATION...][research_ilesanmi_2021]
- [Instruction Code Selection][research_ebner_2021]
- [Multi-modal program inference: a marriage of pre-trained...][research_rahmani_2021]
- [Open-Source Memory Compiler for Automatic RRAM Generation...][research_antoniadis_2021]
- [Solver-based gradual type migration][research_phippscostin_2021]
- [Special Issue on Syntax-Guided Synthesis Preface][research_fisman_2021]
- [The Impact of Undefined Behavior on Compiler Optimization][research_shen_2021]
- [Thread-Aware Area-Efficient High-Level Synthesis Compiler...][research_kim_2021]
- [Towards a Domain-Extensible Compiler: Optimizing an Image...][research_koehler_2021]
- [When Function Signature Recovery Meets Compiler...][research_lin_2021]
- [A Novel Counterexample-Guided Inductive Synthesis...][research_ding_2022]
- [Boosting Compiler Testing via Compiler Optimization...][research_chen_2022]
- [Can reactive synthesis and syntax-guided synthesis be...][research_choi_2022]
- [Cape: compiler-aided program transformation for HTM-based...][research_zhang_2022]
- [Code Generation Techniques in Compiler Design: Conceptual...][research_akanbi_2022]
- [SRTuner: Effective Compiler Optimization Customization by...][research_park_2022_b]
- [Specification-guided component-based synthesis from...][research_mishra_2022]
- [Testing a PL/I Compiler Using Precomputation-based...][research_postema_2022]
- [Threaded Code Generation with a Meta-Tracing JIT Compiler][research_izawa_2022]
- [Towards Automatic Property Generation for SoC Security...][research_wang_2022]
- [Accurate Compiler and Optimization Independent Function...][research_mckee_2023]
- [An Automatic Generation and Verification Method of...][research_wei_2023]
- [Automatic Benchmark Generation for Object Constraint...][research_jha_2023]
- [Component‐based specification, design and verification of...][research_graics_2023]
- [Counterexample Guided Knowledge Compilation for Boolean...][research_akshay_2023]
- [Fast Compiler Optimization Flag Selection][research_peker_2023]
- [From SMT to ASP: Solver-Based Approaches to Solving...][research_bembenek_2023]
- [Introduction to Optimization][research_cooper_2023_b]
- [Modular Component-Based Quantum Circuit Synthesis][research_kang_2023]
- [Neuroevolutionary Compiler Control for Code Optimization][research_heckel_2023]
- [Optimization of production planning using integer linear...][research_astuti_2023]
- [Optimization-Aware Compiler-Level Event Profiling][research_basso_2023]
- [Relational Solver for Java Generics Type System][research_lozov_2023]
- [An Experimental Analysis of RL based Compiler...][research_nikith_2024]
- [Association Rule Learning Based Approach to Automatic...][research_ferchichi_2024]
- [DEVELOPING SITUATIONAL CONDITIONS AND PROGRAM CODES FOR...][research_atanassov_2024]
- [Passenger Queue Simulation Analysis and Optimization at...][research_putra_2024]
- [Reinforcement Learning and Data-Generation for...][research_parsert_2024]
- [Revealing Compiler Heuristics Through Automated Discovery...][research_seeker_2024]
- [Rule modeling for automatic verification of RDC-50...][research_miyamoto_2024]
- [Automatic Generation of Assertions for Security...][research_heidariiman_2025]
- [Automatic Generation of Assertions for Functional...][research_heidariiman_2025_b]
- [Automatic Test Case Generation for Jasper App HDL...][research_crepalde_2025]
- [CTDip: a diversity-guided test program synthesis approach...][research_tang_2025]
- [CompilerDream: Learning a Compiler World Model for...][research_deng_2025]
- [Counterexample-Guided Inference of Modular Specifications][research_hallahan_2025]
- [LLM Compiler: Foundation Language Models for Compiler...][research_cummins_2025]
- [MarQSim: Reconciling Determinism and Randomness in...][research_cao_2025]
- [Optimasi Pemanfaatan Air Menggunakan Program Solver di...][research_supriyatna_2025]
- [Optimization-Directed Compiler Fuzzing for Continuous...][research_kwon_2025]
- [Programming Assessment in E-Learning through Rule-Based...][research_saputro_2025]
- [SAGE-HLS: Syntax-Aware AST-Guided LLM for High-Level...][research_khan_2025]
- [Accelerating Sparse Algebra with Program Synthesis][research_desouzamagalha_2026]
- [Accelerating Syntax-Guided Program Synthesis by...][research_ye_2026]
- [An Ultralow-latency Constrained Quadratic Program (QP)...][research_jimoh_2026]
- [CHEHAB: Automatic Compiler Code Optimization for Fully...][research_seddiki_2026]
- [CPerfSmith: A Randomized C Program Generator for...][research_boda_2026]
- [Compiler-Runtime Co-operative Chain of Verification for...][research_kwon_2026]
- [Distributionally robust optimization with...][research_jin_2026]
- [Hexcute: A Compiler Framework for Automating Layout...][research_zhang_2026_c]
- [LLM-VeriOpt: Verification-Guided Reinforcement Learning...][research_fang_2026]
- [SecSwift, a Compiler-Based Framework for Software...][research_deferriere_2026]
- [Synthesizing Instruction Selection Back-Ends from ISA...][research_drescher_2026]
- [Tensor Program Superoptimization through Cost-Guided...][research_brauckmann_2026]

**This is the most direct engagement with the cost side of the ordering problem and it leaves the value side untouched.**
Synthesis makes an individual lowering cheaper to produce. In the notation used here it reduces $\kappa$ and
leaves $\lvert B \rvert$ exactly where it was,
**so it moves the leverage ratio through the denominator and reorders nothing that the numerator determines.**

### Verification became a family rather than a single system

The conservative stance this article depends on, in which anything not provably handled is refused, is no
longer exotic. Verified compilation, translation validation, refinement checking for optimisations and
certified static analysis are an active field with several mature systems.

- [A verified type system for CakeML][research_tan_2015]
- [Abstract Interpretation with Infinitesimals][research_kido_2015]
- [An optimizing compiler for a purely functional...][research_chlipala_2015]
- [Certified Abstract Interpretation with Pretty-Big-Step...][research_bodin_2015]
- [Correctness of Isabelle's Cyclicity Checker][research_kuncar_2015]
- [Machine-Checked Verification of the Correctness and...][research_chargueraud_2015]
- [Many-core compiler fuzzing][research_lidbury_2015]
- [Modular translation validation of a full-sized...][research_ngo_2015]
- [Pilsner: a compositionally verified compiler for a...][research_neis_2015]
- [Session details: Session 4A: Compiler Correctness][research_chlipala_2015_b]
- [Towards a verified compiler prototype for the synchronous...][research_yang_2015]
- [Verification by abstract interpretation, soundness and...][research_cousot_2015]
- [A Mechanical Soundness Proof for Subtyping Over Recursive...][research_jones_2016]
- [A new verified compiler backend for CakeML][research_tan_2016]
- [Abstract Interpretation of Supermodular Games][research_ranzato_2016]
- [Automated compiler optimization of multiple vector...][research_aleen_2016]
- [Bounded Abstract Interpretation][research_christakis_2016]
- [From Array Domains to Abstract Interpretation Under...][research_suzanne_2016]
- [LifeJacket: verifying precise floating-point...][research_notzli_2016]
- [Mechanizing conventional SSA for a verified destruction...][research_demange_2016]
- [ModelPlex: verified runtime validation of verified...][research_mitsch_2016]
- [Static Analysis by Abstract Interpretation of the...][research_journault_2016]
- [Static analysis of Sequential Function Charts using...][research_simon_2016]
- [Termination-checking for LLVM peephole optimizations][research_menendez_2016_b]
- [Verified construction of static single assignment form][research_buchwald_2016]
- [Verified lifting of stencil computations][research_kamil_2016]
- [Verified peephole optimizations for CompCert][research_mullen_2016]
- [A Verified CompCert Front-End for a Memory Model...][research_besson_2017]
- [A Verified Generational Garbage Collector for CakeML][research_sandbergericss_2017]
- [A formally verified compiler for Lustre][research_bourke_2017]
- [A simple soundness proof for dependent object types][research_rapoport_2017]
- [Alive-Infer: data-driven precondition inference for...][research_menendez_2017]
- [Automated Compiler Optimization of Multiple Vector...][research_aleen_2017]
- [Automated Test Case Generation from OTS/CafeOBJ...][research_mori_2017]
- [Combining Forward and Backward Abstract Interpretation of...][research_bakhirkin_2017]
- [Handling Environments in a Nested Relational Algebra with...][research_auerbach_2017]
- [Lifting proof-relevant unification to higher dimensions][research_cockx_2017]
- [Modeling Undefined Behaviour Semantics for Checking...][research_dahiya_2017]
- [Prototype implementation of the OpenGL ES 2.0 shading...][research_baek_2017]
- [Reduction of Workflow Nets for Generalised Soundness...][research_bride_2017]
- [Skeletal program enumeration for rigorous compiler testing][research_zhang_2017]
- [Taming undefined behavior in LLVM][research_lee_2017]
- [Tutorial on Static Inference of Numeric Invariants by...][research_mine_2017]
- [Verified compilation of CakeML to multiple machine-code...][research_fox_2017]
- [A Proof Score Approach to Formal Verification of an...][research_daudier_2018]
- [A Verified Compiler from Isabelle/HOL to CakeML][research_hupel_2018]
- [A Verified Generational Garbage Collector for CakeML][research_sandbergericss_2018]
- [A fully verified container library][research_polikarpova_2018]
- [A machine-checked correctness proof for Pastry][research_azmy_2018]
- [CompCertS: A Memory-Aware Verified C Compiler Using a...][research_besson_2018]
- [Compiler-agnostic Translation Validation][research_banerjee_2018]
- [Compiler-aided Type Tracking for Correctness Checking of...][research_huck_2018]
- [Delta Debugging Type Errors with a Blackbox Compiler][research_sharrad_2018]
- [HHVM JIT: a profile-guided, region-based compiler for PHP...][research_ottoni_2018]
- [Mechanising a Type-Safe Model of Multithreaded Java with...][research_lochbihler_2018]
- [Reconciling high-level optimizations and low-level code...][research_lee_2018]
- [Securing a compiler transformation][research_deng_2018]
- [Static Value Analysis of Python Programs by Abstract...][research_fromherz_2018]
- [Towards a verified Lustre compiler with modular reset][research_bourke_2018]
- [VeriPhy: verified controller executables from verified...][research_bohrer_2018]
- [A verified protocol buffer compiler][research_ye_2019]
- [Testing and Verifying Parallel Programs Using Data...][research_martinjeremymr_2019]
- [The verified CakeML compiler backend][research_kiamtan_2019]
- [Verified compilation on a verified processor][research_loow_2019]
- [A Formal Proof of the Soundness of the Hybrid CPS Clock...][research_wang_2020]
- [Compiler and runtime support for continuation marks][research_flatt_2020]
- [CoreJIT: a Replication Package for Article...][research_barriere_2020]
- [Do you have space for dessert? a verified space cost...][research_gomezlondono_2020]
- [IMPLEMENTATION OF GENETIC ALGORITHM IN COLLEGE SCHEDULING...][research_saputra_2020]
- [Implementation and Performance Evaluation of Omni Compiler][research_nakao_2020]
- [Lost In Translation: Exposing Hidden Compiler...][research_georgiou_2020]
- [On a Machine-Checked Proof for Fraction Arithmetic over a...][research_meshveliani_2020]
- [Proof pearl: Braun trees][research_nipkow_2020]
- [Testing static analyses for precision and soundness][research_taneja_2020]
- [Towards compiler-aided correctness checking of adjoint...][research_huck_2020]
- [Translation from Visual to Layout-based Android Test...][research_coppola_2020]
- [A minimalistic verified bootstrapped compiler (proof...][research_myreen_2021]
- [Accessible Formal Methods for Verified Parser Development][research_li_2021]
- [CoStar: a verified ALL(*) parser][research_lasser_2021]
- [Compiler Module of Abstract Machine Code for Formal...][research_steingartner_2021]
- [Formally verified speculation and deoptimization in a JIT...][research_barriere_2021]
- [Hyperchaining Optimizations for an LLVM-Based Binary...][research_lai_2021]
- [Lutsig: a verified Verilog compiler for verified circuit...][research_loow_2021]
- [Machine-checked ZKP for NP relations: Formally Verified...][research_almeida_2021]
- [Parallelizing Compiler Translation Validation Using...][research_han_2021_b]
- [Static Analysis of Endian Portability by Abstract...][research_delmas_2021]
- [A machine-checked direct proof of the Steiner-lehmus...][research_kellison_2022]
- [AV-AFL: A Vulnerability Detection Fuzzing Approach by...][research_godboley_2022]
- [Certified abstract machines for skeletal semantics][research_ambal_2022]
- [CirC: Compiler infrastructure for proof systems, software...][research_ozdemir_2022]
- [DISTAL: the distributed tensor algebra compiler][research_yadav_2022]
- [Gradual Soundness: Lessons from Static Python][research_lu_2022]
- [LocSeq: Automated Localization for Compiler Optimization...][research_zhou_2022]
- [Machine-checked Verification of Cognitive Agents][research_jensen_2022]
- [SMT-Based Translation Validation for Machine Learning...][research_bang_2022]
- [Simulink Model Static Analysis Results based on Abstract...][research_yang_2022]
- [The Trusted Computing Base of the CompCert Verified...][research_monniaux_2022]
- [Towards Verified Rounding Error Analysis for Stationary...][research_kellison_2022_b]
- [Verifying optimizations of concurrent programs in the...][research_zha_2022]
- [A Control Flow based Static Analysis of GRAFCET using...][research_schnakenbeck_2023]
- [A Hotspot-Driven Semi-automated Competitive Analysis...][research_mu_2023]
- [CompCert: A Journey through the Landscape of Mechanized...][research_blazy_2023]
- [Completeness in Static Analysis by Abstract...][research_monniaux_2023]
- [Enhancing LLVM Optimizations for Linear Recurrence...][research_lai_2023]
- [Formalising Sharkovsky’s Theorem (Proof Pearl)][research_mehta_2023]
- [Formally Verified Native Code Generation in an Effectful...][research_barriere_2023]
- [Formally Verifying Optimizations with Block Simulations][research_gourdin_2023]
- [Improved Assistance for Interactive Proof (Keynote)][research_kaliszyk_2023]
- [Lazy Code Transformations in a Formally Verified Compiler][research_gourdin_2023_b]
- [PureCake: A Verified Compiler for a Lazy Functional...][research_kanabar_2023]
- [Syntax-Driven Translation][research_cooper_2023_c]
- [Terms for Efficient Proof Checking and Parsing][research_farber_2023]
- [Translation Validation of Information Leakage of Compiler...][research_panigrahi_2023]
- [Verified Propagation Redundancy and Compositional UNSAT...][research_tan_2023]
- [Verifying Term Graph Optimizations using Isabelle/HOL][research_webb_2023]
- [A Mechanised and Constructive Reverse Analysis of...][research_shillito_2024]
- [A Safe Low-Level Language for Computer Algebra and Its...][research_melquiond_2024]
- [A Verified Compiler for a Functional Tensor Language][research_liu_2024_b]
- [Assuring Correctness, Testing, and Verification of...][research_sanusi_2024]
- [Automated Testing to Evaluate Employee Attendance System...][research_hafizhah_2024]
- [Enhancing Translation Validation of Compiler...][research_wang_2024]
- [Extracting Invariants from Conditional Branches for...][research_baek_2024]
- [Leveraging LLVM OpenMP GPU Offload Optimizations for...][research_gayatri_2024]
- [Memory Simulations, Security and Optimization in a...][research_monniaux_2024]
- [PfComp: A Verified Compiler for Packet Filtering...][research_chavanon_2024]
- [Refinement of Parallel Algorithms Down to LLVM: Applied...][research_lammich_2024]
- [Source code obfuscation with genetic algorithms using...][research_delatorre_2024]
- [Tinyrossa: A Compiler Framework for Vertical, Verified...][research_vrany_2024]
- [Translation Validation for JIT Compiler in the V8...][research_kwon_2024]
- [A Formal Verification Library Design for Behavioral...][research_kim_2025]
- [A Formally Verified Microcoded RISC-V Platform][research_klemmer_2025]
- [A Fully Automated Agent for End-to-End Code Translation...][research_erer_2025]
- [A Proof-Producing Compiler for Blockchain Applications][research_avigad_2025]
- [A Universal Quantum Compiler GPT: Multi-Framework...][research_petchartee_2025]
- [CIRE: LLVM Analysis for Floating-Point Rounding Error...][research_tirpankar_2025]
- [FormalGym: Deep Reinforcement Learning Agent Based Formal...][research_majumder_2025]
- [Modeling and implementation of Common LISP functional...][research_chaplygin_2025]
- [ORMorpher: An Interactive Framework for ORM Translation...][research_abraham_2025]
- [Static analysis by abstract interpretation against data...][research_urban_2025]
- [Toward a Formally Verified Compiler for a Synchronous...][research_girault_2025]
- [A Calculus for Web Services Choreography: Formal...][research_yang_2026]
- [A Rose Tree Is Blooming (Proof Pearl)][research_korkut_2026]
- [Brack: A Verified Compiler for Scheme via CakeML][research_lasnier_2026]
- [CODO: An Automated Compiler for Comprehensive Dataflow...][research_zhang_2026_d]
- [CPP '26 Artifact - Brack: A Verified Compiler for Scheme...][research_lasnier_2026_b]
- [Chariot: Compiler-Aware Heterogeneous Graph...][research_huang_2026]
- [Inductor-TV: Formal Methods for the Pytorch Compiler][research_majumder_2026]
- [Making Time Observable: Compiler Correctness for...][research_lion_2026]
- [Test case sampling optimization for safety validation of...][research_qian_2026_b]
- [Testing, Credible Compilation, and Verification in the...][research_rinard_2026]
- [Towards Verified Security: Formal Methods for LLM-Based...][research_dauksevic_2026]
- [Verified VCG and Verified Compiler for Dafny][research_nezamabadi_2026]

**That matters to the argument in a specific way.** The product form arises because a verifying compiler
must refuse a program containing anything it cannot lower correctly.
**The more normal that stance becomes, the more compilers exhibit the behaviour this article measures**, and
the less the result depends on one project's unusual strictness.

### Testing the compiler became industrial, and it cannot answer this question

Compiler fuzzing is one of the genuine success stories of the last fifteen years. Random program generation,
equivalence modulo inputs, differential testing and empirical studies of compiler bugs have found very large
numbers of real defects.

- [An Empirical Study of Bug Fixing Rate][research_zou_2015]
- [An Empirical Study on Real Bug Fixes][research_zhong_2015]
- [Finding deep compiler bugs via guided stochastic program...][research_le_2015]
- [Test program generation for mixed-signal integrated...][research_mosin_2015]
- [An application of metamorphic testing for testing...][research_ding_2016]
- [An empirical study on how expert knowledge affects bug...][research_rodeghero_2016]
- [Efficient Program Tracing and Monitoring Through Power...][research_moreno_2016]
- [From Android Bug Reports to Android Bug Handling Process][research_yu_2016]
- [How Are Discussions Associated with Bug Reworking?][research_zhao_2016]
- [Metamorphic testing for (graphics) compilers][research_donaldson_2016]
- [Random testing of C compilers based on test program...][research_nakamura_2016]
- [A XOR data compiler: Combined with physical unclonable...][research_cambou_2017]
- [Are tweets useful in the bug fixing process? An empirical...][research_mezouar_2017]
- [Bug Propagation through Code Cloning: An Empirical Study][research_mondal_2017]
- [Common Bug-Fix Patterns: A Large-Scale Observational Study][research_campos_2017]
- [Empirical Study on Software Bug Prediction][research_rizwan_2017]
- [Experience Report: Security Vulnerability Profiles of...][research_gosevapopstoja_2017]
- [Faster mutation analysis via equivalence modulo states][research_wang_2017]
- [Metamorphic Testing for Adobe Data Analytics Software][research_jarman_2017]
- [PENERAPAN EIGENFACE UNTUK COMPUTER BASED TEST (CBT)...][research_sajati_2017]
- [Understanding Key Features of High-Impact Bug Reports][research_karim_2017]
- [An Empirical Study of Multi-entity Changes in Real Bug...][research_wang_2018]
- [Empirical study on developer factors affecting tossing...][research_wu_2018]
- [Equivalence Class Testing][research_jorgensen_2018]
- [Fault detection effectiveness of source test case...][research_saha_2018]
- [Finding missed compiler optimizations by differential...][research_barany_2018]
- [INSTRIM: Lightweight Instrumentation for Coverage-guided...][research_hsu_2018]
- [Not all bug reopens are negative: A case study on eclipse...][research_mi_2018]
- [Preventing duplicate bug reports by continuously querying...][research_hindle_2018]
- [Quality assurance of bioinformatics software][research_srinivasan_2018]
- [Compiler bug isolation via effective witness test program...][research_chen_2019]
- [Coverage-Guided Learning-Assisted Grammar-Based Fuzzing][research_jitsunari_2019]
- [Full-Speed Fuzzing: Reducing Fuzzing Overhead through...][research_nagy_2019]
- [Haskell Compiler Testing Automation Based on...][research_li_2019]
- [History-Guided Configuration Diversification for Compiler...][research_chen_2019_b]
- [Reinforcement-Learning-Based Test Program Generation for...][research_chen_2019_c]
- [Verifying Instruction Set Simulators using...][research_herdt_2019]
- [An Empirical Study of Bug Bounty Programs][research_walshe_2020]
- [Enhanced compiler bug isolation via memoized search][research_chen_2020_b]
- [On the relationship between bug reports and queries for...][research_mills_2020]
- [Demystifying the challenges and benefits of analyzing...][research_chen_2021]
- [EPF: An Evolutionary, Protocol-Aware, and Coverage-Guided...][research_helmke_2021]
- [How to Better Distinguish Security Bug Reports (Using...][research_shu_2021]
- [Metamorphic Testing on the Continuum of Verification and...][research_raunak_2021]
- [REST API Fuzzing by Coverage Level Guided Blackbox Testing][research_tsai_2021]
- [ReFuzz: A Remedy for Saturation in Coverage-Guided Fuzzing][research_lyu_2021]
- [Same Coverage, Less Bloat: Accelerating Binary-only...][research_nagy_2021]
- [Similarity-Aware Architecture/Compiler Co-Designed...][research_zhao_2021]
- [The forgotten role of search queries in IR-based bug...][research_rahman_2021]
- [Type-Centric Kotlin Compiler Fuzzing: Preserving Test...][research_stepanov_2021]
- [Why Some Bug-bounty Vulnerability Reports are Invalid?][research_shafigh_2021]
- [CAGFuzz: Coverage-Guided Adversarial Generative Fuzzing...][research_zhang_2022_b]
- [An Empirical Study of Aging Related Bug Prediction Using...][research_kaur_2022]
- [An Empirical Study of the Bug Link Rate][research_li_2022_b]
- [An empirical study of the effectiveness of IR-based bug...][research_li_2022_c]
- [Application of Property-based Testing Tools for...][research_alzahrani_2022]
- [Backend Bug Finder — a platform for effective compiler...][research_stepanov_2022]
- [CsmithEdge: more effective compiler testing by handling...][research_evenmendoza_2022]
- [Efficient Cross-Level Processor Verification using...][research_bruns_2022]
- [Enriching Compiler Testing with Real Program from Bug...][research_zhong_2022]
- [Fine-Grained Coverage-Based Fuzzing][research_nongpoh_2022]
- [FitM: Binary-Only Coverage-Guided Fuzzing for Stateful...][research_maier_2022]
- [High‐coverage metamorphic testing of concurrency support...][research_windsor_2022]
- [Investigating Coverage Guided Fuzzing with Mutation...][research_qian_2022]
- [Metamorphic testing in bioinformatics software][research_stacy_2022]
- [POWER: Program Option-Aware Fuzzer for High Bug Detection...][research_lee_2022]
- [Remgen: Remanufacturing a Random Program Generator for...][research_tu_2022]
- [SpinalFuzz: Coverage-Guided Fuzzing for SpinalHDL Designs][research_ruep_2022]
- [Testing ocean software with metamorphic testing][research_luu_2022]
- [Unified HW/SW Coverage: A Novel Metric to Boost...][research_bruns_2022_b]
- [Upstream bug management in Linux distributions][research_lin_2022]
- [Bug characterization in machine learning-based systems][research_morovati_2023]
- [Compiler Test-Program Generation via Memoized...][research_chen_2023]
- [Coverage-Guided Fuzzing for Plan-Based Robotics][research_meywerk_2023]
- [Finding Unstable Code via Compiler-Driven Differential...][research_li_2023_c]
- [Fuzzing Deep Learning Compilers with HirGen][research_ma_2023]
- [GrayC: Greybox Fuzzing of Compilers and Analysers for C][research_evenmendoza_2023]
- [Improve Model Testing by Integrating Bounded Model...][research_yang_2023]
- [Inferring test models from user bug reports using...][research_guizzo_2023]
- [JITfuzz: Coverage-guided Fuzzing for JVM Just-in-Time...][research_wu_2023]
- [Poster: BugOss: A Regression Bug Benchmark for Empirical...][research_kim_2023]
- [Program Reconditioning: Avoiding Undefined Behaviour When...][research_lecoeur_2023]
- [Rainfuzz: Reinforcement-Learning Driven Heat-Maps for...][research_binosi_2023]
- [RustSmith: Random Differential Compiler Testing for Rust][research_sharma_2023]
- [Silent Compiler Bug De-duplication via Three-Dimensional...][research_yang_2023_b]
- [A study of common bug fix patterns in Rust][research_robatishirzad_2024]
- [An empirical study on the potential of word embedding...][research_chen_2024_b]
- [Automated SC-MCC test case generation using...][research_golla_2024]
- [Automatic program bug fixing by focusing on finding the...][research_yousofvand_2024]
- [Boosting Compiler Testing by Injecting Real-World Code][research_li_2024_b]
- [Bug numbers matter: An empirical study of effort‐aware...][research_yang_2024]
- [CatchFuzz: Reliable active anti-fuzzing techniques...][research_kim_2024_b]
- [Compatible Branch Coverage Driven Symbolic Execution for...][research_yi_2024]
- [Compiler Bug Isolation via Enhanced Test Program Mutation][research_liu_2024_c]
- [Detecting Optimizing Compiler Bugs via History-Driven...][research_zeng_2024]
- [Diffy: Data-Driven Bug Finding for Configurations][research_kakarla_2024]
- [Discretized optimization algorithms for finding the...][research_arasteh_2024]
- [FOX: Coverage-guided Fuzzing as Online Stochastic Control][research_she_2024]
- [Fuzzing Command-line Interface by Edge Coverage Guided...][research_lu_2024]
- [Fuzzing JavaScript Interpreters with Coverage-Guided...][research_eom_2024]
- [Fuzzing guided by context-sensitive branch coverage][research_liu_2024_d]
- [History-driven Compiler Fuzzing via Assembling and...][research_fan_2024]
- [Industrial adoption of machine learning techniques for...][research_laiq_2024]
- [Inside Bug Report Templates: An Empirical Study on Bug...][research_zhang_2024]
- [Optimising Bcrypt Parameters: Finding the Optimal Number...][research_listiawan_2024]
- [RLGFuzz: Reinforcement Learning Guided Fuzzing with...][research_shen_2024]
- [Rust-twins: Automatic Rust Compiler Testing through...][research_yang_2024_b]
- [Rustlantis: Randomized Differential Testing of the Rust...][research_wang_2024_b]
- [Semantic-Type-Guided Bug Finding][research_qian_2024]
- [Testing Error Handling Code With Software Fault Injection...][research_bai_2024]
- [Testing the Unknown: A Framework for OpenMP Testing via...][research_laguna_2024]
- [When Compiler Optimizations Meet Symbolic Execution: An...][research_zhang_2024_b]
- [Automated Test Generation from Program Documentation...][research_denaro_2025]
- [BoostPolyGlot: A Structured IR Generation-Based Fuzz...][research_liu_2025_c]
- [CBGF: Callback Coverage Guided Fuzzing][research_hwang_2025]
- [Can We Enhance Bug Report Quality Using LLMs?: An...][research_acharya_2025]
- [Compiler Optimization Testing Based on...][research_wu_2025_b]
- [DeepUIFuzz: A Guided Fuzzing Strategy for Testing UI...][research_chowdhury_2025]
- [Differential Fuzzing Go Compilers using LLMs: A...][research_terres_2025]
- [Finding Compiler Bugs through Cross-Language Code...][research_feng_2025]
- [From Bug Reports to Workarounds: The Real-World Impact of...][research_he_2025]
- [Fuzzing JavaScript JIT compilers with a high-quality...][research_li_2025_b]
- [GrammLLM: Grammar-Guided LLM Test Generation for Compiler...][research_talaat_2025]
- [HFuzz: Havoc Mode Guided Fuzzing][research_xie_2025]
- [Hybrid Equivalence/Non-Equivalence Testing][research_sarker_2025]
- [Interleaving Large Language Models for Compiler Testing][research_ni_2025]
- [IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for...][research_cui_2025]
- [MALintent: Coverage Guided Intent Fuzzing Framework for...][research_askar_2025]
- [Metamorphic Relation Patterns for Metamorphic Testing...][research_ying_2025]
- [Research on coverage-guided fuzzing technique based on...][research_ma_2025]
- [SSFuzz: Synthesizing and scheduling bug-triggering code...][research_hu_2025]
- [Scalable SMT Sampling for Floating-Point Formulas via...][research_carrasco_2025]
- [Shepherd: High-Precision Coverage Inference for...][research_shimizu_2025]
- [Solsmith: Solidity Random Program Generator for Compiler...][research_li_2025_c]
- [Symbolic MRD: Dynamic Memory, Undefined Behaviour, and...][research_richards_2025]
- [Synchronized Behavior Checking: A Method for Finding...][research_zhang_2025]
- [Testing Autonomous Driving Systems Through Blind-Spot...][research_moussa_2025]
- [An Empirical Comparison of Human and LLM-Assisted Bug...][research_nasui_2026]
- [An exploratory study of bug-introducing changes...][research_schulte_2026]
- [Automated Inference of Expressive Metamorphic Relations...][research_nolasco_2026]
- [Batch Me If You Can: Coverage-Guided RPKI Fuzzing at Scale][research_schulmann_2026]
- [Coverage-Guided Multi-Agent Harness Generation for Java...][research_loose_2026]
- [Detecting Compiler-Introduced Security Bugs via IR...][research_oh_2026]
- [Grammar-Aware Coverage-Guided Fuzzing with Grammarinator...][research_hodovan_2026]
- [How Effective Is Coverage-Guided Fuzzing to Test Deep...][research_qin_2026]
- [QEMI: A Quantum Software Stacks Testing Framework via...][research_luo_2026]
- [TYPEFUZZ: Type Coverage Directed JavaScript Engine...][research_wienand_2026]
- [TenSure: Fuzzing Sparse Tensor Compilers (Registered...][research_mahathevan_2026]
- [Towards Path-Aware Coverage-Guided Fuzzing][research_priamo_2026]
- [Understanding Bug-Reproducing Tests: A First Empirical...][research_hora_2026]
- [Understanding and Finding JIT Compiler Performance Bugs][research_yi_2026]
- [WuppieFuzz: Coverage-Guided, Stateful REST API Fuzzing][research_rooijakkers_2026]

**And the entire apparatus is blind to the question asked here, for a precise reason.** A fuzzer generates
programs and checks whether the compiler handles them correctly. **It therefore tests what is implemented.**
An unimplemented instruction is not a bug the fuzzer can find, because the compiler correctly refuses it.
**The most sophisticated compiler-testing machinery ever built cannot tell an engineer what to implement next**,
and nothing in that literature claims otherwise.

### Timing analysis, which is the reason to go native at all

The motivation for native code generation in this project is worst-case resource behaviour, and that subject
remains active, with multicore timing, cache predictability and time-predictable architecture carrying the
effort.

- [Calculation of worst-case execution time for multicore...][research_mushtaq_2015]
- [Efficient Worst-Case Execution Time Analysis of Dynamic...][research_puffitsch_2016]
- [FIFO Cache Analysis for WCET Estimation][research_guan_2016]
- [MRU Cache Analysis for WCET Estimation][research_guan_2016_b]
- [Operator-data type pair based execution environments...][research_seo_2016]
- [Time-Accurate ASM as a Refinement Scheme for Worst-Case...][research_mguidich_2016]
- [Worst-Case Execution Time Analysis for Many-Core...][research_skalistis_2016]
- [Architecture of a tool for automated testing the...][research_fedasyuk_2017]
- [Class-based query-optimization for minimizing worst-case...][research_tabassam_2017]
- [Combining loop unrolling strategies and code predication...][research_carminati_2017]
- [Integration of Static Worst-Case Execution Time and Stack...][research_hausladen_2017]
- [On the Criticality of Probabilistic Worst-Case Execution...][research_santinelli_2017]
- [Predicting Worst-Case Execution Time Trends in Long-Lived...][research_dai_2017]
- [Replacing conjectures by positive knowledge: Inferring...][research_knoop_2017]
- [On the use of static branch prediction to reduce the...][research_carminati_2018]
- [PSO based optimization of worst-case execution time for...][research_venkanna_2018]
- [Static Worst-Case Execution Time Optimization using DPSO...][research_venkanna_2018_b]
- [Worst-Case Execution Time Testing via Evolutionary...][research_aquino_2018]
- [Correction to: A compiler framework for the reduction of...][research_falk_2019]
- [Software UART: A Use Case for VSCPU Worst-Case Execution...][research_yildiz_2019]
- [Symbolic Execution and Recent Applications to Worst-Case...][research_pasareanu_2019]
- [Reliability Test based on a Binomial Experiment for...][research_arcaro_2020]
- [Survey on Estimation and Optimization of Worst-case...][research_meng_2020]
- [Worst-case Execution Time Estimation of Legacy Vehicular...][research_ventovaara_2020]
- [Deep Neural Network Approach to Estimate Early Worst-Case...][research_kumar_2021]
- [Experiences from Adjusting Industrial Software for...][research_denzler_2021]
- [Practical Examples of Timing Problems][research_gliwa_2021]
- [Timing Analysis Techniques][research_gliwa_2021_b]
- [Use of Measurements in Worst-Case Execution Time...][research_costa_2021]
- [CUDA Acceleration of Worst-Case Execution Time Analysis...][research_wanxin_2022]
- [Worst-Case Execution Time Estimation for Numerical...][research_susca_2022]
- [Analysis of benchmark program results of worst case...][research_paraman_2023]
- [Design of DMS-RRIP replacement algorithm for L1-cache of...][research_ma_2023_b]
- [Worst Case Execution Time and Power Estimation of...][research_rodriguezferra_2023]
- [Analyzing Data Flow and Control Flow of Multicore...][research_thomas_2024]
- [Exact Worst-Case Execution-Time Analysis for Implicit...][research_arnstrom_2024]
- [Utilizing Machine Learning Techniques for Worst-Case...][research_kumar_2024]
- [Worst-Case Execution Time Analysis of Real-Time Robotic...][research_samiei_2024]
- [Determining Worst-Case Execution Time Bounds for...][research_kaestner_2025]
- [Hardware/Software Co-Analysis for Worst Case Execution...][research_lehmann_2025]
- [Static Timing and Power Analysis of a RISC-V Pipelined...][research_kadarkarai_2025]
- [Worst-Case Execution Time Analysis of a Real-Time System...][research_merazga_2025]
- [A Time-Predictable Multicore RISC-V Architecture for...][research_munezero_2026]

**The relevant point is that the analysis is only as complete as the lowering.** A bound that cannot be
computed for a program the compiler refuses is not a bound at all, so the coverage question sits upstream of
the timing question rather than beside it.

### Measuring a corpus became routine, which strengthens the recommendation

**This is the largest change and it cuts in the article's favour.** Mining software repositories is a mature
field with its own venue, and large-scale study of what code actually contains is ordinary work now.

- [A Large Scale Study of License Usage on GitHub][research_vendome_2015]
- [A large-scale study on the usage of Java’s concurrent...][research_pinto_2015]
- [Characteristics of Useful Code Reviews: An Empirical...][research_bosu_2015]
- [Co-evolution of Infrastructure and Source Code - An...][research_jiang_2015]
- [Code Ownership and Software Quality: A Replication Study][research_greiler_2015]
- [Code coverage and test suite effectiveness: Empirical...][research_kochhar_2015]
- [Fuse: A Reproducible, Extendable, Internet-Scale Corpus...][research_barik_2015]
- [Graph-Based Statistical Language Model for Code][research_nguyen_2015]
- [License Usage and Changes: A Large-Scale Study of Java...][research_vendome_2015_b]
- [Novice comprehension of Object-Oriented OO programs: An...][research_alardawi_2015]
- [Partitioning Composite Code Changes to Facilitate Code...][research_tao_2015]
- [Quality Questions Need Quality Code: Classifying Code...][research_duijn_2015]
- [Query by example in large-scale code repositories][research_balachandran_2015]
- [A Taxonomy of Spanish Nouns, a Statistical Algorithm to...][research_nazar_2016]
- [A large-scale empirical study on self-admitted technical...][research_bavota_2016]
- [A large-scale study on repetitiveness, containment, and...][research_nguyen_2016]
- [License usage and changes: a large-scale study on gitHub][research_vendome_2016]
- [Mining performance regression inducing code changes in...][research_luo_2016]
- [Mining the modern code review repositories][research_yang_2016]
- [A Large-Scale Study of the Impact of Feature Selection...][research_ghotra_2017]
- [A large-scale study of programming languages and code...][research_ray_2017]
- [An Empirical Study on Real Bugs for Machine Learning...][research_sun_2017]
- [Bug Characteristics in Blockchain Systems: A Large-Scale...][research_wan_2017]
- [Classifying Code Comments in Java Open-Source Software...][research_pascarella_2017]
- [Creating and Analyzing Source Code Repository Models - A...][research_scheidgen_2017]
- [PRPA REPERCUSSIONS and IMPLICATIONS FOR REAL WORLD STUDY...][research_anon_2017]
- [Statistical Unigram Analysis for Source Code Repository][research_xu_2017]
- [Who Will Leave the Company?: A Large-Scale Industry Study...][research_bao_2017]
- [A benchmark study on the effectiveness of search-based...][research_hosseini_2018]
- [Analyzing False Positive Source Code Vulnerabilities...][research_cheirdari_2018]
- [Large-scale analysis of the co-commit patterns of the...][research_cohen_2018]
- [SLAMPA: Recommending Code Snippets with Statistical...][research_zhou_2018]
- [Syntax, predicates, idioms — what really affects code...][research_ajami_2018]
- [The Expansion of Source Code Abbreviations Using a...][research_alatawi_2018]
- [Why are Android apps removed from Google Play?][research_wang_2018_b]
- [A Convolutional Neural Network for Language-Agnostic...][research_moore_2019]
- [A Large-Scale Study About Quality and Reproducibility of...][research_pimentel_2019]
- [Branch Use in Practice: A Large-Scale Empirical Study of...][research_zou_2019]
- [Combining Program Analysis and Statistical Language Model...][research_nguyen_2019]
- [GreenSource: A Large-Scale Collection of Android Code...][research_rua_2019]
- [Impact of Stack Overflow Code Snippets on Software...][research_ahmad_2019]
- [git2net - Mining Time-Stamped Co-Editing Networks from...][research_gote_2019]
- [A Large-Scale Comparative Evaluation of IR-Based Tools...][research_akbar_2020]
- [Big code != big vocabulary][research_karampatsis_2020]
- [Building Intelligent Integrated Development Environment...][research_althar_2020]
- [Dockerfile Changes in Practice: A Large-Scale Empirical...][research_wu_2020]
- [Empirical Study about Class Change Proneness Prediction...][research_martins_2020]
- [How does combinatorial testing perform in the real world...][research_hu_2020_c]
- [How to Evaluate the Productivity of Software Ecosystem: A...][research_liao_2020]
- [Large-Scale Manual Validation of Bugfixing Changes][research_herbold_2020]
- [Open Source Software (OSS) for Big Data][research_segall_2020]
- [Querying Big Source Code][research_garciaalvarado_2020]
- [RTFM: Towards Understanding Source Code using Natural...][research_galanis_2020]
- [The Software Heritage Graph Dataset][research_pietri_2020]
- [Using Large-Scale Anomaly Detection on Code to Improve...][research_bryksin_2020]
- [A Large Scale Study of Long-Time Contributor Prediction...][research_bao_2021]
- [A Large-Scale Empirical Study of COVID-19 Themed GitHub...][research_wang_2021_b]
- [A large-scale study on human-cloned changes for automated...][research_madeiral_2021]
- [An Empirical Study of Real-World WebAssembly Binaries][research_hilbig_2021]
- [An Empirical Study on the Impact of Aspect-oriented...][research_menolli_2021]
- [AndroidCompass: A Dataset of Android Compatibility Checks...][research_nielebock_2021]
- [CCEyes: An Effective Tool for Code Clone Detection on...][research_zhang_2021]
- [Does Code Review Promote Conformance? A Study of...][research_sriiesaranusor_2021]
- [Machine Learning Approaches for Authorship Attribution...][research_frankel_2021]
- [Predicting Design Impactful Changes in Modern Code...][research_uchoa_2021]
- [QScored: A Large Dataset of Code Smells and Quality...][research_sharma_2021]
- [A Mechanism for Automatically Extracting Reusable and...][research_papoudakis_2022]
- [A large-scale comparison of Python code in Jupyter...][research_grotov_2022]
- [A large-scale dataset of (open source) license text...][research_zacchiroli_2022]
- [Geographic diversity in public code contributions][research_rossi_2022]
- [How to improve deep learning for software analytics][research_yedida_2022]
- [Low Level Source Code Vulnerability Detection Using...][research_alqarni_2022]
- [Mining the usage of reactive programming APIs][research_zimmerle_2022]
- [A Large Scale Analysis of Semantic Versioning in NPM][research_pinckney_2023]
- [APR4Vul: an empirical study of automatic program repair...][research_bui_2023]
- [DeepSurveySim: Simulation Software and Benchmark...][research_voetberg_2023]
- [Enriching Source Code with Contextual Data for Code...][research_vandam_2023]
- [Improving Code Completion by Solving Data Inconsistencies...][research_yang_2023_c]
- [Language usage analysis for EMF metamodels on GitHub][research_babur_2023]
- [Large Language Models for Code Obfuscation Evaluation of...][research_kochberger_2023]
- [Naturalness in Source Code Summarization. How Significant...][research_ferretti_2023]
- [Source Code Features and their Dependencies: An...][research_toosi_2023]
- [Source Code Implied Language Structure Abstraction...][research_wang_2023_c]
- [Source Code Plagiarism Detection with Pre-Trained Model...][research_anon_2023]
- [A Large-Scale Empirical Study of Open Source License...][research_wu_2024]
- [A Methodology for Analysing Code Anomalies in Open-Source...][research_campbell_2024]
- [An Empirical Analysis of Issue Templates Usage in...][research_sulun_2024]
- [Can Large Language Model Detect Plagiarism in Source Code?][research_brach_2024]
- [EnStack: An Ensemble Stacking Framework of Large Language...][research_ridoy_2024]
- [How accessibility affects other quality attributes of...][research_zhao_2024_b]
- [Large-Scale Analysis of GitHub and CVEs to Determine...][research_dennis_2024]
- [Multi-faceted Code Smell Detection at Scale using...][research_sharma_2024]
- [Naturalness of Attention: Revisiting Attention in Code...][research_saad_2024]
- [Propagating Large Language Models Programming Feedback][research_koutcheme_2024]
- [CASTL: A Composable Source Code Query Language for...][research_johnson_2025]
- [Can LLMs Generate Higher Quality Code Than Humans? An...][research_jamil_2025]
- [CoUpJava: A Dataset of Code Upgrade Histories in...][research_jiang_2025_b]
- [Combining Large Language Models with Static Analyzers for...][research_jaoua_2025]
- [Come for syntax, stay for speed, write secure code: an...][research_zhang_2025_b]
- [Examining the impact of bias mitigation algorithms on the...][research_demartino_2025]
- [GHALogs: Large-Scale Dataset of GitHub Actions Runs][research_moriconi_2025]
- [Generating Software Architecture Description from Source...][research_hatahet_2025]
- [Harnessing Large Language Models for Curated Code Reviews][research_sghaier_2025]
- [HyperAST: Incrementally Mining Large Source Code...][research_ledilavrec_2025]
- [Java Source Code Vulnerability Detection Using Large...][research_anbiya_2025]
- [Large Language Models for Computer Programming Education...][research_zhu_2025_b]
- [OSS License Identification at Scale: A Comprehensive...][research_jahanshahi_2025]
- [Programming Large Language Models][research_calamo_2025]
- [RETRACTION: Study on Large‐Scale Promotion of...][research_programming_2025]
- [Towards understanding code review practices for...][research_bessghaier_2025]
- [Understanding Feature Request Practice on GitHub via a...][research_li_2025_d]
- [Wild SBOMs: a Large-scale Dataset of Software Bills of...][research_soeiro_2025]
- [rFocal: Run 'FOCAL' Language Source Code][research_witthoft_2025]
- [A Large-Scale Dataset of MCP Implementations on GitHub][research_toeppe_2026]
- [A Large-Scale Investigation Into the Loss of Pull Request...][research_tang_2026]
- [AI builds, We Analyze: An Empirical Study of AI-Generated...][research_ghammam_2026]
- [An Empirical Study of SBOM Usage Through GitHub Actions][research_kanemoto_2026]
- [Automating Software Documentation with n8n and Large...][research_toprak_2026]
- [Beyond Single Code Changes: An Empirical Study of...][research_chouchen_2026]
- [Empirical Study on Real-time System Modeling and Code...][research_hu_2026_b]
- [Floating-Point Usage on GitHub: A Large-Scale Study of...][research_gilot_2026]
- [GeoAutoModuler: a knowledge–enhanced large language model...][research_liang_2026]
- [GitEvo: Code Evolution Analysis for Git Repositories][research_hora_2026_b]
- [HackRep: A Large-Scale Dataset of GitHub Hackathon...][research_halmans_2026]
- [How AI Coding Agents Modify Code: A Large-Scale Study of...][research_ogenrwot_2026]
- [How challenging it is to identify real code authors: an...][research_gong_2026]
- [Integrating Large Language Models in Software Engineering...][research_khan_2026]
- [Modeling Sampling Workflows for Code Repositories][research_lefeuvre_2026]
- [OSSGameBench: A Large-Scale Dataset of Development...][research_marsad_2026]
- [Running Large Language Models at Scale for Mining...][research_su_2026]
- [Understanding Binary Code Similarity for Real-World...][research_guo_2026]

**The instrument this article describes took twenty minutes to build because that is now a twenty-minute job.**
When the instruction-selection classics were written it was not.
**The recommendation to measure before ordering was expensive advice in 1978 and is nearly free in 2026**,
which is the strongest argument for adopting it and is an argument the article did not previously make.

### The surrogate-measure warning has been rediscovered everywhere

The specific failure this article reports, where an easily computed measure stands in for the property
actually wanted, is not confined to compilers. Coverage as a proxy for suite quality, mutation scores, flaky
tests, benchmarking methodology and replication have all produced the same warning.

- [An Empirical Study on Effects of Code Visibility on Code...][research_ma_2015]
- [An Initiative to Improve Reproducibility and Empirical...][research_oliveiraneto_2015]
- [An empirical study of bugs in test code][research_vahabzadeh_2015]
- [Beyond code coverage and#x2014; An approach for test...][research_tengeri_2015]
- [Do Automatically Generated Unit Tests Find Real Faults?...][research_shamshiri_2015]
- [Exploring Test Suite Diversification and Code Coverage in...][research_mondal_2015]
- [Investigations about replication of empirical studies in...][research_demagalhaes_2015]
- [Mutation testing in practice using Ruby][research_li_2015]
- [On the Benefits and Barriers When Adopting Software...][research_vetro_2015]
- [Replication of Empirical Studies in Software Engineering...][research_bezerra_2015]
- [Using Artificial Bee Colony for Code Coverage Based Test...][research_konsaard_2015]
- [Using text clustering to predict defect resolution time...][research_assar_2015]
- [A detailed investigation of the effectiveness of whole...][research_rojas_2016]
- [A large-scale study of call graph-based impact prediction...][research_musco_2016]
- [Assessing the Test Suite of a Large System Based on Code...][research_vidacs_2016]
- [Characterizing logging practices in Java-based open...][research_chen_2016_b]
- [Empirical study of correlation between mutation score and...][research_felbinger_2016]
- [Global vs. local models for cross-project defect...][research_herbold_2016]
- [Relating Code Coverage, Mutation Score and Test Suite...][research_tengeri_2016]
- [System-Level Test Case Prioritization Using Machine...][research_lachmann_2016]
- [Techniques of Test Case Prioritization][research_puri_2016]
- [UML Associations - Reducing the Gap in Test Coverage...][research_eriksson_2016]
- [Using docker containers to improve reproducibility in...][research_cito_2016]
- [An Empirical Study of Activity, Popularity, Size...][research_gautam_2017]
- [An Empirical Study of the Personnel Overhead of...][research_manglaviti_2017]
- [An Empirical Study on the Cross-Project Predictability of...][research_xia_2017]
- [An empirical study of regression test suite reduction...][research_singhal_2017]
- [An empirical study on the application of mutation testing...][research_ramler_2017]
- [Analytics-Driven Load Testing: An Industrial Experience...][research_chen_2017]
- [Assessing and Improving the Mutation Testing Practice of...][research_laurent_2017]
- [Could We Predict the Result of a Continuous Integration...][research_xia_2017_b]
- [Creating and Running Tests with Xamarin Test Cloud][research_versluis_2017]
- [Extended firm mutation testing: A cost reduction...][research_singh_2017]
- [How effective are mutation testing tools? An empirical...][research_kintis_2017]
- [Impact of Static and Dynamic Coverage on Test-Case...][research_zhou_2017]
- [Integrating Tests into Your Builds][research_versluis_2017_b]
- [Reinforcement learning for automatic test case...][research_spieker_2017]
- [12.4 - Machine Learning-Driven Test Case Prioritization...][research_lachmann_2018]
- [An Empirical Study of Flaky Tests in Android Apps][research_thorve_2018]
- [An Industrial Application of Mutation Testing: Lessons...][research_petrovic_2018]
- [An empirical study of inadequate and adequate test suite...][research_coviello_2018]
- [Are mutation scores correlated with real fault detection?][research_papadakis_2018]
- [Continuous Integration and Visual GUI Testing: Benefits...][research_alegroth_2018]
- [Generating Effective Test Suite for Multiparameter...][research_patil_2018]
- [Prediction of relatedness in stack overflow: deep...][research_xu_2018]
- [Program comprehension of domain-specific and...][research_kosar_2018]
- [Redefining prioritization][research_liang_2018]
- [Reproducibility and credibility in empirical software...][research_rodriguezperez_2018]
- [State of mutation testing at google][research_petrovic_2018_b]
- [Test case prioritization and selection technique in...][research_xiao_2018]
- [Test prioritization in continuous integration environments][research_haghighatkhah_2018]
- [The role and value of replication in empirical software...][research_shepperd_2018]
- [A Time Window based Reinforcement Learning Reward for...][research_wu_2019_b]
- [An Empirical Study of the Relationship between Continuous...][research_sizilionery_2019]
- [An empirical study of the long duration of continuous...][research_ghaleb_2019]
- [Combining Code and Requirements Coverage with Execution...][research_marchetto_2019]
- [Comprehending Test Code: An Empirical Study][research_yu_2019]
- [Meta-analysis for families of experiments in software...][research_kitchenham_2019]
- [RETRACTED ARTICLE: The smell of fear: on the relation...][research_palomba_2019]
- [Temporal Discounting in Software Engineering: A...][research_fagerholm_2019]
- [Test Case Design and Test Case Prioritization using...][research_anon_2019_b]
- [TestCov: Robust Test-Suite Execution and Coverage...][research_beyer_2019]
- [A study on the lifecycle of flaky tests][research_lam_2020]
- [Code review effectiveness: an empirical study on selected...][research_jureczko_2020]
- [Data Science and Empirical Software Engineering][research_scott_2020]
- [De-Flake Your Tests : Automatically Locating Root Causes...][research_ziftci_2020]
- [Effective Test Suite Optimization for Improving the...][research_karuppusamy_2020]
- [Empirical Software Engineering Experimentation with Human...][research_sabou_2020]
- [Empirical Study of Restarted and Flaky Builds on Travis CI][research_durieux_2020]
- [Empirical Study of Software Test Suite Evolution][research_aljedaani_2020]
- [Learning-based prioritization of test cases in continuous...][research_lima_2020]
- [Multi-Armed Bandit Test Case Prioritization in Continuous...][research_lima_2020_b]
- [Resources for Reproducibility of Experiments in Empirical...][research_anchundia_2020]
- [Retraction Note: Retraction note to: The smell of fear...][research_palomba_2020]
- [TABU Search Prioritized Ant Colony Metaheuristic...][research_t_2020]
- [Test Case Prioritization in Continuous Integration...][research_pradolima_2020]
- [The Application Of Machine Learning In Test Case...][research_mece_2020]
- [The Evolution of Empirical Methods in Software Engineering][research_felderer_2020]
- [A Review on Continuous Integration and Continuous...][research_mahida_2021]
- [An Empirical Analysis of UI-Based Flaky Tests][research_romano_2021]
- [An Empirical Study of Flaky Tests in Python][research_gruber_2021]
- [Assessment of off-the-shelf SE-specific sentiment...][research_novielli_2021]
- [DeepCrime: mutation testing of deep learning systems...][research_humbatova_2021]
- [DeepOrder: Deep Learning for Test Case Prioritization in...][research_sharif_2021]
- [Empirical evaluation of tools for hairy requirements...][research_berry_2021]
- [Extreme mutation testing in practice: An industrial case...][research_betka_2021]
- [Genetic programming for feature model synthesis: a...][research_vescan_2021]
- [Industrial Scale Passive Testing with T-EARS][research_flemstrom_2021]
- [Lessons Learnt on Reproducibility in Machine Learning...][research_daoudi_2021]
- [Locating faults with program slicing: an empirical...][research_soremekun_2021]
- [Reflections on the Empirical Software Engineering journal][research_basili_2021]
- [Release synchronization in software ecosystems][research_foundjem_2021]
- [Statement frequency coverage: A code coverage criterion...][research_aghamohammadi_2021]
- [Test case selection and prioritization using machine...][research_pan_2021]
- [Understanding and improving the quality and...][research_pimentel_2021]
- [Weighted Reward for Reinforcement Learning based Test...][research_li_2021_b]
- [When is Continuous Integration Useful? Empirical Study on...][research_imai_2021]
- [A Comprehensive Study on Code Coverage Analysis for...][research_bandyopadhyay_2022]
- [A Multi-Armed Bandit Approach for Test Case...][research_lima_2022]
- [A Qualitative Study on the Sources, Impacts, and...][research_habchi_2022]
- [An Empirical Study of Flaky Tests in JavaScript][research_hashemi_2022]
- [An Improvement to Test Case Prioritization Techniques...][research_khan_2022]
- [Breaking bad? Semantic versioning and impact of breaking...][research_ochoa_2022]
- [Checked coverage for test suite reduction][research_koitzhristov_2022]
- [Cost-effective learning-based strategies for test case...][research_pradolima_2022]
- [Evaluating classifiers in SE research: the ECSER pipeline...][research_dellanna_2022]
- [Excluding code from test coverage: practices...][research_hora_2022]
- [Machine Learning Regression Techniques for Test Case...][research_daroza_2022]
- [Mutation analysis and its industrial applications][research_gopinath_2022]
- [Patterns of Code-to-Test Co-evolution for Automated Test...][research_shimmi_2022]
- [Preempting flaky tests via non-idempotent-outcome tests][research_wei_2022]
- [Real world projects, real faults: evaluating spectrum...][research_widyasari_2022]
- [Reinforcement Learning Reward Function for Test Case...][research_mirzaei_2022]
- [Revisiting the building of past snapshots — a replication...][research_maesbermejo_2022]
- [Static detection of equivalent mutants in real-time...][research_basile_2022]
- [The reproducibility of programming-related issues in...][research_mondal_2022]
- [What do developer-repaired Flaky tests tell us about the...][research_parry_2022]
- [An Empirical Study of Greedy Test Suite Minimization...][research_jehan_2023]
- [An Empirical Study of Regression Testing for Android Apps...][research_wang_2023_d]
- [An Empirical Study on the Correlation between Neuron...][research_li_2023_d]
- [An Evaluation of Ranking-to-Learn Approaches for Test...][research_lima_2023]
- [An Improved Method for Test Case Prioritization in...][research_han_2023]
- [Automated NFR testing in continuous integration...][research_yu_2023]
- [Comparative study of machine learning test case...][research_marijan_2023]
- [DeepCrime: from Real Faults to Mutation Testing Tool for...][research_humbatova_2023]
- [Evaluation of Coverage Metrics for Assessing Test Suite...][research_chippagi_2023]
- [Guest editorial: special issue on empirical software...][research_baldassarre_2023]
- [How Closely are Common Mutation Operators Coupled to Real...][research_gay_2023]
- [How Do Deep Learning Faults Affect AI-Enabled...][research_arrieta_2023]
- [Model vs system level testing of autonomous driving...][research_stocco_2023]
- [Mutation Testing in Continuous Integration: An...][research_orgard_2023]
- [Mutation Testing of Deep Reinforcement Learning Based on...][research_tambon_2023]
- [Neural Network-Based Test Case Prioritization in...][research_vescan_2023]
- [On factors that impact the relationship between code...][research_barani_2023]
- [Operationalizing validity of empirical software...][research_hartel_2023]
- [Optimizing test case prioritization using machine...][research_sharma_2023_b]
- [Parallel mutation testing for large scale systems][research_canizares_2023]
- [Revisiting Machine Learning based Test Case...][research_zhao_2023]
- [Revisiting the reproducibility of empirical software...][research_gonzalezbaraho_2023]
- [Scalable and Accurate Test Case Prioritization in...][research_yaraghi_2023]
- [Semantic Coverage: Measuring Test Suite Effectiveness][research_alblwi_2023]
- [Semantic‐aware two‐phase test case prioritization for...][research_li_2023_e]
- [Syntactic Versus Semantic Similarity of Artificial and...][research_ojdanic_2023]
- [Test Case Prioritization using Transfer Learning in...][research_mamata_2023]
- [The Vocabulary of Flaky Tests in the Context of SAP HANA][research_berndt_2023]
- [A Preliminary Framework for Optimising Test Case...][research_ndlovu_2024]
- [An Empirical Study on Code Coverage of Performance Testing][research_imran_2024]
- [An Exploratory Study on Soft Skills present in Software...][research_kapitsaki_2024]
- [An extensive replication study of the ABLoTS approach for...][research_niu_2024]
- [Cost of Flaky Tests in Continuous Integration: An...][research_leinen_2024]
- [Deployment and Integration of Machine Learning Methods...][research_wham_2024]
- [Examining ownership models in software teams][research_koana_2024]
- [Explainable Test Case Prioritization in Continuous...][research_garg_2024]
- [Exploring the Effectiveness of LLM based Test-driven...][research_fakhoury_2024]
- [FlakeSync: Automatically Repairing Async Flaky Tests][research_rahman_2024]
- [Leveraging Rough Sets for Enhanced Test Case...][research_gaceanu_2024]
- [Machine Learning for Test Case Prioritization in...][research_kumar_2024_b]
- [Machine Learning-based Test Case Prioritization using...][research_khan_2024]
- [Nonlinear Reinforcement Learning-Based Dynamic Test Case...][research_srinivasaraoko_2024]
- [On the use of contextual information for machine learning...][research_roza_2024]
- [Reinforcement learning for online testing of autonomous...][research_giamattei_2024]
- [Test Case Prioritization for Regression Testing Using...][research_sawant_2024]
- [Test code refactoring unveiled: where and how does it...][research_martins_2024]
- [Towards enhancing the reproducibility of deep learning...][research_shah_2024]
- [Using rapid reviews to support software engineering...][research_pizard_2024]
- [$\mu \text{PRL}$: A Mutation Testing Pipeline for Deep...][research_thomas_2025]
- [A Defect Taxonomy for Infrastructure as Code: A...][research_oliveira_2025]
- [A Preliminary Study of Fixed Flaky Tests in Rust Projects...][research_schroeder_2025]
- [AI-Driven Test Case Generation for Continuous Integration...][research_subrahmanyam_2025]
- [Achieving High-Integrity Software Quality and Security...][research_niharika_2025]
- [An Effective GRU-Based Deep Learning Method for Test Case...][research_behera_2025]
- [An Empirical Study of Web Flaky Tests: Understanding and...][research_pei_2025]
- [An Environment Adaptation Agent of Reinforcement Learning...][research_li_2025_e]
- [An Explainable Deep Learning Model in Improving Test Case...][research_ramakrishnan_2025]
- [Attention Transfer Reinforcement Learning for Test Case...][research_su_2025]
- [Dynamic Test Case Prioritization and Selection for...][research_waseem_2025]
- [Evaluating Machine Learning-Based Test Case...][research_son_2025]
- [How Does Test Code Differ from Production Code in Terms...][research_horikawa_2025]
- [Identifying and Mitigating Flaky Tests in JavaScript][research_hashemi_2025]
- [Intelligent Test Case Prioritization: A Review of Machine...][research_razi_2025]
- [Is code coverage of performance tests related to source...][research_imran_2025]
- [Mutation Operators for Mutation Testing of Angular Web...][research_augustin_2025]
- [Mutation Testing for Industrial Robotic Systems][research_goncalvesdossa_2025]
- [Mutation Testing of Programs for Industrial Robots][research_ashraf_2025]
- [Opportunities and security risks of technical leverage: A...][research_samaana_2025]
- [Optimizing Test Case Prioritization With Meta Deep...][research_alrakban_2025]
- [Ranking Relevant Tests for Order-Dependent Flaky Tests][research_rahman_2025]
- [Rechecking Recheck Requests in Continuous Integration: An...][research_brus_2025]
- [Reimagining Studies’ Replication: A Validity-Driven...][research_azevedo_2025]
- [Reproducibility Practices of Software Engineering...][research_cordeiro_2025]
- [Reviewing Reproducibility in Software Engineering Research][research_cordeiro_2025_b]
- [muttest: Mutation Testing][research_sobolewski_2025]
- [A large-scale empirical study of configurations, errors...][research_zhang_2026_e]
- [Adaptive and Explainable Test Case Prioritization in...][research_kongarana_2026]
- [Beyond Coverage: Automatic Test Suite Augmentation for...][research_lu_2026]
- [Can We Classify Flaky Tests Using Only Test Code? an...][research_berndt_2026]
- [Fuzzy-Graph Contrastive Test Case Prioritization...][research_kumar_2026]
- [Industrial Application of Deep Learning based Fault...][research_yang_2026_b]
- [Interruptibility of software developers and its...][research_poreba_2026]
- [Is this build failure related to my patch? An empirical...][research_huang_2026_b]
- [Mitigating omitted variable bias in empirical software...][research_furia_2026]
- [Neural-MCTS Test Prioritization for Smart Contract...][research_barboni_2026]

**Instruction-level coverage is a metric that became a target.** It is the measure a bring-up effort
naturally reports because it moves smoothly and always improves, and it is nearly uninformative about
whether anything works.

### Attribution and submodularity moved into machine learning

The Shapley machinery invoked for the attribution problem is no longer a game-theory curiosity. It is
production tooling for model explanation and data valuation, and submodular maximisation acquired streaming
and distributed algorithms.

- [Randomized Composable Core-sets for Distributed...][research_mirrokni_2015]
- [Risk Attribution Using the Shapley Value: Methodology and...][research_tarashev_2015]
- [Submodular maximization meets streaming: matchings...][research_chakrabarti_2015]
- [On distributed submodular maximization with limited...][research_gharesifard_2016]
- [The Shapley Value as a Sustainable Cooperative Solution...][research_gromova_2016]
- [A distributed algorithm for partitioned robust submodular...][research_bogunovic_2017]
- [Bicriteria Distributed Submodular Maximization in a Few...][research_epasto_2017]
- [Shapley Value of a Cooperative Game with Fuzzy Set of...][research_mashchenko_2017]
- [Distributed Submodular Maximization on Partition Matroids...][research_corah_2018]
- [Distributed matroid-constrained submodular maximization...][research_corah_2018_b]
- [Greedily Excluding Algorithm for Submodular Maximization][research_seo_2018]
- [Streaming Non-Monotone Submodular Maximization...][research_mirzasoleiman_2018]
- [An Approximation Algorithm for Distributed Resilient...][research_zhou_2019]
- [Collaboration Formation and Profit Sharing Between...][research_fahimullah_2019]
- [Distributed Submodular Maximization with Bounded...][research_castiglia_2019]
- [Hodge decomposition and the Shapley value of a...][research_stern_2019]
- [Shapley Value Approximation with Divisive Clustering][research_corder_2019]
- [Streaming Submodular Maximization Under Noises][research_yang_2019]
- [The Shapley Value, a Crown Jewel of Cooperative Game...][research_thomson_2019]
- [The Shapley and Position Values to Design Coalitional...][research_muros_2019]
- [A cooperative game theory application in chicks brood...][research_haque_2020]
- [An Improved Shapley Value Benefit Distribution Mechanism...][research_xie_2020]
- [Distributed Attack-Robust Submodular Maximization for...][research_zhou_2020]
- [Distributed Maximization of Submodular and Approximately...][research_ye_2020]
- [Distributed Submodular Maximization with Parallel...][research_sun_2020]
- [Sequence submodular maximization meets streaming][research_yang_2020]
- [A Multi-pass Streaming Algorithm for Regularized...][research_gong_2021]
- [A Streaming Model for Monotone Lattice Submodular...][research_zhang_2021_b]
- [Fast derivation of Shapley based feature importances...][research_liu_2021_b]
- [Fixed-size video summarization over streaming data via...][research_lu_2021]
- [Improved Prediction of Total Energy Consumption and...][research_pokharel_2021]
- [Multi-Pass Streaming Algorithms for Monotone Submodular...][research_huang_2021]
- [One‐pass streaming algorithm for monotone lattice...][research_zhang_2021_c]
- [Shapley-Value Data Valuation for Semi-supervised Learning][research_courtnage_2021]
- [Streaming algorithms for robust submodular maximization][research_yang_2021]
- [A Programming Approach for Worst-case Studies in...][research_downie_2022]
- [An Optimal Streaming Algorithm for Submodular...][research_alaluf_2022]
- [An optimal streaming algorithm for non-submodular...][research_liu_2022_b]
- [Application of an Improved Shapley Value Method in...][research_ma_2022]
- [CS-Shapley: Class-Wise Shapley Values for Data Valuation...][research_schoch_2022]
- [Data Shapley Valuation for Efficient Batch Active Learning][research_ghorbani_2022]
- [Distributed submodular maximization: trading performance...][research_rezazadeh_2022]
- [One-pass streaming algorithm for DR-submodular...][research_tan_2022]
- [Poster Abstract: Towards Shapley Value based Security...][research_marbukh_2022]
- [Regularized two-stage submodular maximization under...][research_yang_2022_b]
- [Resource-Aware Distributed Submodular Maximization: A...][research_xu_2022_b]
- [Shapley Value is an Equitable Metric for Data Valuation][research_shobeiri_2022]
- [Streaming submodular maximization under d-knapsack...][research_chen_2022_b]
- [A Model-Agnostic Feature Attribution Approach to...][research_fan_2023]
- [Algorithms to estimate Shapley value feature attributions][research_chen_2023_b]
- [Cooperative game amongst prefabricated building chain...][research_zhao_2023_b]
- [DASH: A Distributed and Parallelizable Algorithm for...][research_dey_2023]
- [Data valuation using Shapley value in machine learning][research_sharma_2023_c]
- [Distributed strategy selection: A submodular set function...][research_rezazadeh_2023]
- [Erratum: Weighted shapley value: a cooperative game...][research_anon_2023_b]
- [Fair and Efficient Alternatives to Shapley-based...][research_condevaux_2023]
- [Integrating Staleness and Shapley Value Consistency for...][research_jiang_2023]
- [Machine Learning for Data Center Optimizations: Feature...][research_gebreyesus_2023]
- [Streaming Algorithms for Constrained Submodular...][research_cui_2023_b]
- [Streaming Algorithms for Non-Submodular Maximization on...][research_tan_2023_b]
- [Streaming adaptive submodular maximization][research_tang_2023]
- [Weighted shapley value: A cooperative game theory for...][research_singh_2023]
- [Zoish: A Novel Feature Selection Approach Leveraging...][research_sadaei_2023]
- [A Semi-streaming Algorithm for Monotone Regularized...][research_nong_2024]
- [An Improved Space Semi-Streaming Algorithm for Submodular...][research_bao_2024]
- [An innovative machine learning workflow to research...][research_wang_2024_c]
- [Applications and Computation of the Shapley Value in...][research_luo_2024]
- [Approximation Algorithm for Connected Submodular Function...][research_xu_2024]
- [Blending Shapley values for feature ranking in machine...][research_guleria_2024]
- [Bridging efficacy and efficiency: Innovations in Shapley...][research_yang_2024_c]
- [Codes for machine learning and Shapley value analysis][research_he_2024]
- [DU-Shapley: A Shapley Value Proxy for Efficient Dataset...][research_garridolucero_2024]
- [Deterministic Algorithm and Faster Algorithm for...][research_buchbinder_2024]
- [Deterministic streaming algorithms for non-monotone...][research_sun_2024]
- [Efficient Shapley Value Driven Federated Learning System...][research_wu_2024_b]
- [Efficient Shapley performance attribution for...][research_bell_2024]
- [Explaining 3D Object Detection Through Shapley...][research_kuroki_2024]
- [Greedy algorithm for maximization of semi-monotone...][research_shi_2024]
- [Greedy+Singleton: An efficient approximation algorithm...][research_tang_2024]
- [Machine learning models with distinct Shapley value...][research_roth_2024]
- [Machine learning-based modelling, feature importance and...][research_karathanasopou_2024]
- [Multipass Streaming Algorithms for Regularized Submodular...][research_gong_2024]
- [Optimizing Shapley Value for Client Valuation in...][research_arbaoui_2024]
- [SHapley Additive exPlanations (SHAP) for Efficient...][research_santos_2024]
- [Semi-streaming Algorithms for Submodular Function...][research_huang_2024_b]
- [Shapley value in machine learning modeling: optimizing...][research_ciano_2024]
- [Shapley value: from cooperative game to explainable...][research_li_2024_c]
- [Shapley-Based Data Valuation Method for the Machine...][research_baghcheband_2024]
- [The Forward-Reverse Greedy Algorithm for Distributed...][research_tackett_2024]
- [Why Shapley Value and Its Variants Are Useful in Machine...][research_bokati_2024]
- [A Scalable and Efficient Intrusion Detection System Based...][research_rocca_2025]
- [DERIVATIVE-BASED SHAPLEY VALUE FOR GLOBAL SENSITIVITY...][research_duan_2025]
- [Data Valuation Method Based on Federated Learning and...][research_tan_2025_b]
- [Data Valuation with Shapley-based Methods for Medical...][research_akcelik_2025]
- [Data valuation with Leave-One-Out (LOO) test and Shapley...][research_martin_2025]
- [Deterministic Algorithm and Faster Algorithm for...][research_buchbinder_2025]
- [Fast Shapley Value Approximation Through Machine Learning...][research_guckel_2025]
- [Heterogeneous Graph Data Valuation: A Shapley Value-based...][research_tang_2025_b]
- [Integrating Shapley Value and Least Core Attribution for...][research_wang_2025_b]
- [Localized Data Shapley: Accelerating Valuation for...][research_zhang_2025_c]
- [Offline and Online Distributed Submodular Maximization...][research_ye_2025]
- [Online and Streaming Algorithms for Constrained...][research_spaeh_2025]
- [Optimizing Task Allocation in IT Project Management Using...][research_garmsirinejad_2025]
- [Privacy-Preserving Feature Valuation in Vertical...][research_laskurain_2025]
- [Reward-Aware Shapley Compensation: a Probabilistic and...][research_li_2025_f]
- [Shapley Patch Valuation Method for Histopathological...][research_karadeniz_2025]
- [Shapley value-based data valuation for machine learning...][research_baghcheband_2025]
- [Shapley-Based Data Valuation for Weighted $k$-Nearest...][research_zhang_2025_d]
- [Shapley-Based Data Valuation with Mutual Information: A...][research_vahedifar_2025]
- [Shapley-Value Based Feature Attribution for...][research_aldarmini_2025]
- [Streaming Stochastic Submodular Maximization with...][research_wang_2025_c]
- [Streaming algorithms for non-monotone DR-submodular...][research_zhang_2025_e]
- [Toward learnable and interpretable data Shapley valuation...][research_li_2025_g]
- [k-Submodular Maximization Under Individual Knapsack...][research_tran_2025]
- [A Priority-Ordered Swapping Algorithm for Submodular...][research_peng_2026]
- [A Shapley-value cooperative game-based risk decision...][research_wang_2026]
- [A primal-dual algorithm for monotone submodular...][research_chakrabarty_2026]
- [A streaming algorithm for non-monotone regularized...][research_zhang_2026_f]
- [Dynamic valuation of data assets via multi-agent...][research_xie_2026]
- [Energy-Based Model for Accurate Estimation of Shapley...][research_lu_2026_b]
- [Improving the accuracy and stability of privacy-aware...][research_tang_2026_b]
- [LTSV: Layered Type-Constrained Shapley Value for...][research_tang_2026_c]
- [Light Shapley: Improving the Scalability of Equitable...][research_li_2026_b]
- [P30 - Möbius-Shapley: Native Feature Attribution for...][research_dhahbi_2026]
- [Ripple Shapley: Data Influence Attribution in One...][research_zeng_2026]
- [Shapley Value-Based Feature Attribution for Data Masking][research_qu_2026]
- [Streaming Submodular Maximization Under Matroid...][research_feldman_2026]
- [Streaming submodular maximization with fairness...][research_guo_2026_b]
- [Submodular Maximization Subject to Uniform and Partition...][research_kia_2026]

**The transfer runs the wrong way for the present problem.** Those literatures overwhelmingly assume a
submodular or approximately submodular objective, because that is where the guarantees live.
**The coverage objective here is supermodular**, which is exactly the regime the contemporary work sets
aside, so the tooling is available and the guarantees are not.

### The compiler started learning, which changes the corpus

Machine learning entered the compiler itself, in phase ordering, learned cost models and heuristic
replacement, and large language models entered code production.

- [Checking correctness of code generator architecture...][research_hasabnis_2015]
- [Compiler-Directed Power Management for Superscalars][research_hajyihia_2015]
- [S-compiler: A code vulnerability detection method][research_monicacatherin_2015]
- [A Compiler Approach for Exploiting Partial SIMD...][research_zhou_2016]
- [A graph-based iterative compiler pass selection and phase...][research_nobre_2016]
- [Clustering-Based Selection for the Exploration of...][research_martins_2016]
- [JavaScript Parallelizing Compiler for Exploiting...][research_na_2016]
- [Compiler-Assisted Loop Hardening Against Fault Attacks][research_proy_2017]
- [On the Interactions Between Value Prediction and Compiler...][research_endo_2017]
- [Machine Learning in Compiler Optimization][research_wang_2018_c]
- [AutoPhase: Compiler Phase-Ordering for HLS with Deep...][research_huang_2019_b]
- [Nonio — modular automatic compiler phase selection and...][research_nobre_2019]
- [Identifying Compiler and Optimization Options from Binary...][research_pizzolotto_2020]
- [Reliable Compilation Optimization Phase-ordering...][research_wu_2020_b]
- [Automatic Joint Optimization of Algorithm-Level...][research_liu_2021_c]
- [Identifying Compiler and Optimization Level in Binary...][research_pizzolotto_2021]
- [Memory Utilization and Machine Learning Techniques for...][research_shreyasmadhav_2021]
- [Towards Compile-Time-Reducing Compiler Optimization...][research_jayatilaka_2021]
- [A Novel Prediction Model for Compiler Optimization with...][research_kadam_2022]
- [Automating reinforcement learning architecture design for...][research_wang_2022_b]
- [CARL: Compiler Assigned Reference Leasing][research_ding_2022_b]
- [Compiler Optimization Parameter Selection Method Based on...][research_liu_2022_c]
- [Compiler Support for Sparse Tensor Computations in MLIR][research_bik_2022]
- [Hybrid Approach based on Multi‐agent System and Fuzzy...][research_yahyaoui_2022]
- [Language models can prioritize patches for practical...][research_kang_2022]
- [Object Intersection Captures on Interactive Apps to Drive...][research_mpeis_2022]
- [An Evaluation Method for Large Language Models’ Code...][research_su_2023]
- [Automated Program Repair in the Era of Large Pre-trained...][research_xia_2023]
- [Compiler Optimization for Quantum Computing Using...][research_quetschlich_2023]
- [Is Your Code Generated by ChatGPT Really Correct?...][research_liu_2023_b]
- [Large Language Models for Automated Program Repair][research_ribeiro_2023]
- [Work-in-Progress: Searching Optimal Compiler Optimization...][research_chang_2023]
- [A Comparative Evaluation of Prompting Strategies for Code...][research_fanyizhao_2024]
- [A Digital Twin Modeling Code Generation Framework based...][research_dong_2024]
- [A Multi-Expert Large Language Model Architecture for...][research_nadimi_2024]
- [A Survey of Optimized Compiler Using Advanced Machine...][research_pandey_2024]
- [Advancements and Challenges of Large Language Model-Based...][research_wang_2024_d]
- [Assessing the Impact of Compiler Optimizations on GPUs...][research_santos_2024_b]
- [Automated C/C++ Program Repair for High-Level Synthesis...][research_xu_2024_b]
- [Chinese Generation and Security Index Evaluation Based on...][research_zhang_2024_c]
- [CodeJudge: Evaluating Code Generation with Large Language...][research_tong_2024]
- [Compiler-Based Memory Encryption for Machine Learning on...][research_maeng_2024]
- [Exponentially Expanding the Phase-Ordering Search Space...][research_han_2024_b]
- [FormalEval: A Method for Automatic Evaluation of Code...][research_yang_2024_d]
- [LLM-based Control Code Generation using Image Recognition][research_koziolek_2024]
- [Large Language Models Meet Automated Program Repair...][research_tang_2024_b]
- [Large Language Models in Automated Repair of Haskell Type...][research_santos_2024_c]
- [Machine Learning Based Compiler Optimization Technique][research_iqbal_2024]
- [Machine Learning-Driven GCC Loop Unrolling Optimization...][research_shi_2024_b]
- [Research on Program Automatic Repair Method Combining...][research_li_2024_d]
- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large...][research_yang_2024_e]
- [A Systematic Review about Large Language Models (LLMs)...][research_alecsandrobaci_2025]
- [AI for Code: Reinforcement-Learned Compiler Optimizations...][research_peta_2025]
- [APICoder: A Multi-Role Large Language Model Framework for...][research_yang_2025]
- [AUTOMATED GENERATION AND EVALUATION OF VOCABULARY TESTS...][research_nakanishi_2025]
- [Advancements in AI-Based Compiler Optimization Techniques...][research_shankar_2025]
- [Applying Knowledge-Guided Deep Reinforcement Learning...][research_li_2025_h]
- [Balancing Security and Correctness in Code Generation: An...][research_black_2025]
- [Beyond Functional Correctness: An Empirical Evaluation of...][research_nogueira_2025]
- [CWEval: Outcome-driven Evaluation on Functionality and...][research_peng_2025]
- [Can AI Fix Buggy Code? Exploring the Use of Large...][research_zhang_2025_f]
- [Causality-Aided Evaluation and Explanation of Large...][research_ji_2025]
- [Compiler-Assisted Optimization Using Neural Code...][research_matteordonelli_2025]
- [Compiler-R1: Towards Agentic Compiler Auto-tuning with...][research_pan_2025]
- [CompilerGPT: Leveraging Large Language Models for...][research_pirkelbauer_2025]
- [DeCOS: Data-Efficient Reinforcement Learning for Compiler...][research_cui_2025_b]
- [Efficient program optimization through knowledge-enhanced...][research_xu_2025]
- [EvoAPR: Enhancing Large Language Models for Automatic...][research_zhang_2025_g]
- [Exploiting Booster Pass Chain for Compiler Phase Ordering][research_chen_2025_b]
- [Finding Missed Code Size Optimizations in Compilers using...][research_italiano_2025]
- [Finetune-Then-Merge: Democratizing Large Language Model...][research_che_2025]
- [Holistic evaluation of LLM-Based Code Generation][research_holl_2025]
- [Hybrid Automated Program Repair by Combining Large...][research_li_2025_i]
- [Implement Machine Learning to Schedule Instructions to...][research_rajendran_2025]
- [InstructRepair: Instruct Large Language Models With Rich...][research_fu_2025]
- [Knowledge Graph Based Repository-Level Code Generation][research_athale_2025]
- [LMFuzz: Program repair fuzzing based on large language...][research_lin_2025]
- [Large Language Model Generation Safety: A Comprehensive...][research_zhang_2025_h]
- [LegoFuzz: Interleaving Large Language Models for Compiler...][research_ni_2025_b]
- [Leveraging Compilation Statistics for Compiler Phase...][research_zhao_2025_b]
- [Model-Driven Quantum Code Generation Using Large Language...][research_siavash_2025]
- [Navigating the SIMD Optimization Maze: A Reinforcement...][research_pan_2025_b]
- [Optimization, Machine Learning, and Fuzzy Logic][research_kingslystephen_2025]
- [Proving the Coding Interview: A Benchmark for Formally...][research_dougherty_2025]
- [ReAPR: Automatic program repair via retrieval-augmented...][research_liu_2025_d]
- [Reductive Analysis with Compiler-Guided Large Language...][research_wang_2025_d]
- [RepairBench: Leaderboard of Frontier Models for Program...][research_silva_2025]
- [Research on Compiler Optimization Technology Based on...][research_cui_2025_c]
- [Revisiting Unnaturalness for Automated Program Repair in...][research_yang_2025_b]
- [Role-Aware Intelligent Agent Framework for Enhanced Code...][research_roshan_2025]
- [SPRoC: Semantics-Preserving Mutations for Robustness...][research_shi_2025]
- [Supporting Dynamic Program Sizes in Deep Learning-Based...][research_hakimi_2025]
- [T 3 : Multi-level Tree-based Automatic Program Repair...][research_liu_2025_e]
- [TOWARDS AUTONOMOUS CODE OPTIMIZATION: A REINFORCEMENT...][research_svenkatesan_2025]
- [Template-Guided Program Repair in the Era of Large...][research_huang_2025]
- [The Impact of Fine-Tuning Large Language Models on...][research_machacek_2025]
- [The use of large language models for program repair][research_zubair_2025]
- [Toward Green Code: Prompting Small Language Models for...][research_ashraf_2025_b]
- [Usage of Large Language Model for Code Generation Tasks...][research_bistarelli_2025]
- [VEGA: Automatically Generating Compiler Backends using a...][research_zhong_2025]
- [A Systematic Literature Review on Automated Program...][research_hamdi_2026]
- [A comparative analysis of the role of Large Language...][research_patricio_2026]
- [Academic english writing generation-evaluation...][research_yingzhe_2026]
- [An overview of evaluation and enhancement methods for...][research_truong_2026]
- [ArkTS code generation: A comprehensive evaluation with...][research_erkus_2026]
- [Automatic Program Repair Using Large Language Models in...][research_ajiki_2026]
- [Automating code generation for a new ecosystem...][research_aytekin_2026]
- [Benchmarking Cross-Language Code Smell Detection with...][research_moldovan_2026]
- [Can test cases generated by large language models...][research_zhang_2026_g]
- [Combining Static Code Analysis and Large Language Models...][research_neumuller_2026]
- [Exploring Generalizable Automated Program Repair With...][research_campos_2026]
- [From Natural Language to Interpretable Code: Automated...][research_chen_2026]
- [Large Language Model-Based Interactive Code Generation...][research_hamasaki_2026]
- [Large Language Models for Code Translation: An In-Depth...][research_feischl_2026]
- [Model-Agnostic Empirical Evaluation of Test-Driven Prompt...][research_rizqullah_2026]
- [PredComp: Predicting Compiler Optimization Options with...][research_gao_2026]
- [PromptTone: A Dataset for Evaluating Large Language Model...][research_andruccioli_2026]
- [Protean Compiler: An Agile Framework to Drive Fine-grain...][research_ashouri_2026]
- [RE-APR: Reasoning-Enhanced Automated Program Repair via...][research_du_2026]
- [Rethinking Correctness and Efficiency in AI-Assisted Code...][research_altunel_2026]
- [SAGE: A Compiler-assisted Reinforcement Learning-based...][research_maity_2026]
- [Technical Perspective: Fusing Large Language Models with...][research_bavota_2026]
- [Towards defect-type-aware adaptive program repair: A...][research_zhang_2026_h]

**The second of those affects this article's method rather than its argument.** A corpus of real programs is
the instrument's foundation, and a growing fraction of real programs is now machine-generated.
**Whether generated code has the same instruction distribution as human code is an open empirical question**,
and if it does not, then the corpus caveat this article already states becomes sharper rather than milder.

### Ordering engineering work is a discipline, and it counts costs

There is a literature on deciding what to build next, covering technical debt prioritisation, requirements
prioritisation and effort estimation.

- [Accuracy Comparison of Analogy-Based Software Development...][research_idri_2015]
- [An Empirical Approach for Estimation of the Software...][research_jakhar_2015]
- [An Empirical Investigation on Effort Estimation in Agile...][research_britto_2015]
- [An empirical evaluation of ensemble adjustment methods...][research_azzeh_2015]
- [Analysis of task effort estimation accuracy based on use...][research_popovic_2015]
- [Automated selection of a software effort estimation model...][research_nayebi_2015]
- [Empirical Application of Simulated Annealing Using...][research_rizvi_2015]
- [How do open source software (OSS) developers practice and...][research_kuriakose_2015]
- [Prediction accuracy measurements as a fitness function...][research_urbanek_2015]
- [A large-scale empirical comparison of static and dynamic...][research_luo_2016_b]
- [A stability assessment of solution adaptation techniques...][research_phannachitta_2016]
- [Assessment and Comparison of Fuzzy Based Test Suite...][research_chaudhary_2016]
- [How do software development teams manage technical debt?...][research_ylihuumo_2016]
- [Negative results for software effort estimation][research_menzies_2016]
- [Realistic assessment of software effort estimation models][research_sigweni_2016]
- [Systematic Mapping Study of Ensemble Effort Estimation][research_idri_2016]
- [Technical debt prioritization using predictive analytics][research_codabux_2016]
- [AHP_GORE_PSR: Applying analytic hierarchy process in goal...][research_sadiq_2017]
- [An Empirical Comparison of Similarity Measures for...][research_huang_2017]
- [An Empirical Study of Technical Debt in Open-Source...][research_alfayez_2017]
- [An Evaluation of Selection Methods for Time-Aware Effort...][research_amasaki_2017]
- [DRank: A semi-automated requirements prioritization...][research_shao_2017]
- [Empirical Assessment of Machine Learning Models for...][research_satapathy_2017]
- [Empirical evaluation of fuzzy analogy for software...][research_abnane_2017]
- [Entropy-based Framework Dealing with Error in Software...][research_elkoutbi_2017]
- [Evaluating Pred(p) and standardized accuracy criteria in...][research_idri_2017]
- [Fuzzy_MoSCoW: A fuzzy based MoSCoW method for the...][research_ahmad_2017]
- [Identifying self-admitted technical debt in open source...][research_huang_2017_b]
- [Looking for Peace of Mind? Manage Your (Technical) Debt...][research_ghanbari_2017]
- [On the Evaluation of Effort Estimation Models][research_lavazza_2017]
- [Startups and Technical Debt: Managing Technical Debt with...][research_chicote_2017]
- [Cuckoo search based hybrid models for improving the...][research_kumari_2018]
- [Effective fault localization of automotive Simulink...][research_liu_2018]
- [Empirical evaluation of an entropy‐based approach to...][research_elkoutbi_2018]
- [Flaws of Quantification Method as applied to Software...][research_mshanmuganatha_2018]
- [Identification and prioritization of SLR search tool...][research_alzubidy_2018]
- [On the value of a prioritization scheme for resolving...][research_mensah_2018]
- [Prioritizing solution-oriented software requirements...][research_ibriwesh_2018]
- [Project productivity evaluation in early software effort...][research_azzeh_2018]
- [Software Development Effort Estimation Using Random...][research_anon_2018]
- [Towards a functional requirements prioritization with...][research_condorifernand_2018]
- [A novel online supervised hyperparameter tuning procedure...][research_minku_2019]
- [An Effort Estimation Support Tool for Agile Software...][research_dantas_2019]
- [An Empirical Study on Technical Debt in a Finnish SME][research_lenarduzzi_2019]
- [Analogy-Based Approaches to Improve Software Project...][research_resmi_2019]
- [Business-Driven Technical Debt Prioritization][research_reboucasdealme_2019]
- [Technical Debt Prioritization: A Search-Based Approach][research_alfayez_2019]
- [Tracy: A Business-Driven Technical Debt Prioritization...][research_reboucasdealme_2019_b]
- [Usability Technical Debt in Software Projects: A...][research_lage_2019]
- [A Taste of the Software Industry Perception of Technical...][research_apa_2020]
- [A systematic literature review of technical debt...][research_alfayez_2020]
- [Continuous Debt Valuation Approach (CoDVA) for Technical...][research_stochel_2020]
- [Empirical Evaluation of Mimic Software Project Data Sets...][research_gan_2020]
- [Evaluating the agreement among technical debt measurement...][research_amanatidis_2020]
- [Improving Estimation Accuracy Prediction of Software...][research_mahmood_2020]
- [Long-Term Evaluation of Technical Debt in Open-Source...][research_molnar_2020]
- [Profiling Developers Through the Lens of Technical Debt][research_codabux_2020]
- [Using Extremely Simplified Functional Size Measures for...][research_lavazza_2020]
- [Wait for it: identifying “On-Hold” self-admitted...][research_maipradit_2020]
- [A Collaborative Effort-Benefit-Value Analysis Model to...][research_gupta_2021]
- [A Stacking Ensemble-based Approach for Software Effort...][research_shukla_2021]
- [A systematic literature review on Technical Debt...][research_lenarduzzi_2021]
- [AI Techniques for Software Requirements Prioritization][research_felfernig_2021]
- [An Extreme Learning Machine based Approach for Software...][research_shukla_2021_b]
- [Applying test case prioritization to software...][research_laaber_2021]
- [Correction to: Wait for it: identifying “On-Hold”...][research_maipradit_2021]
- [Flower Pollination Algorithm for Software Effort...][research_puspaningrum_2021]
- [Measuring affective states from technical debt][research_olsson_2021]
- [Neural Networks based Software Development Effort...][research_boujida_2021]
- [Refactorings and Technical Debt in Docker Projects: An...][research_ksontini_2021]
- [Self-admitted technical debt practices: a comparison...][research_zampetti_2021]
- [Software effort estimation accuracy prediction of machine...][research_mahmood_2021]
- [Technical Debt Prioritization: Taxonomy, Methods Results...][research_pina_2021]
- [23 shades of self-admitted technical debt: an empirical...][research_obrien_2022]
- [Adopting DevOps Paradigm in Technical Debt Prioritization...][research_stochel_2022]
- [An Empirical Study on Software Test Effort Estimation for...][research_cibir_2022]
- [An empirical study on self-admitted technical debt in...][research_azuma_2022]
- [An extended study on applicability and performance of...][research_amasaki_2022]
- [Asking about Technical Debt: Characteristics and...][research_kozanidis_2022]
- [Blockchain-Based Software Effort Estimation: An Empirical...][research_ahmed_2022]
- [Characterizing Technical Debt in Evolving Open-source...][research_molnar_2022]
- [DebtFree: minimizing labeling cost in self-admitted...][research_tu_2022_b]
- [Development effort estimation in free/open source...][research_robles_2022]
- [Empirical Research for Self-Admitted Technical Debt...][research_yubin_2022]
- [Evaluation of Context-Aware Language Models and Experts...][research_alhamed_2022]
- [FIXME: synchronize with database! An empirical study of...][research_muse_2022]
- [Heterogeneous Graph Neural Networks for Software Effort...][research_phan_2022]
- [Identifying self-admitted technical debt in issue...][research_li_2022_d]
- [MCBRank Method to Improve Software Requirements...][research_ahmad_2022]
- [On the documentation of self-admitted technical debt in...][research_xavier_2022]
- [OurRank: A Software Requirements Prioritization Method...][research_rojas_2022]
- [PriorTD: A Method for Prioritization Technical Debt][research_detofeno_2022]
- [Security Requirements Prioritization Techniques: A Survey...][research_khanneh_2022]
- [Self-Admitted Technical Debt and comments’ polarity: an...][research_cassee_2022]
- [Solution to CAD Designer Effort Estimation based on...][research_nikiforova_2022]
- [Technical Debt, Software Evolution and Legacy][research_bass_2022]
- [Technical debt prioritization][research_pina_2022]
- [The Influence of Cost Drivers on Effort Estimation in...][research_iqbal_2022]
- [Toward prioritization of self-admitted technical debt: an...][research_delima_2022]
- [Use Case-Based Analytical Hierarchy Process Method for...][research_naufalmaulana_2022]
- [A practical approach for technical debt prioritization...][research_tsoukalas_2023]
- [Automatic identification of self-admitted technical debt...][research_li_2023_f]
- [Evaluating ensemble imputation in software effort...][research_abnane_2023]
- [Exploring Technical Debt in Security Questions on Stack...][research_edbert_2023]
- [Heterogeneous Ensemble Model to Optimize Software Effort...][research_ali_2023]
- [Improving Software Requirements Prioritization through...][research_winton_2023]
- [Much more than a prediction: Expert-based software effort...][research_matsubara_2023]
- [Software effort estimation using validated accuracy...][research_v_2023]
- [Technical Debt Contagiousness Metrics for Measurement and...][research_bi_2023]
- [An Empirical Study on Self-Admitted Technical Debt in...][research_ishimoto_2024]
- [Optimizing Software Effort Estimation Accuracy with a...][research_raghuraman_2024]
- [Quantifying and characterizing clones of self-admitted...][research_xiao_2024]
- [Technical Debt Tools: a Survey and an Empirical Evaluation][research_gomes_2024]
- [The broken windows theory applies to technical debt][research_leven_2024]
- [The method of requirements prioritization in software...][research_anon_2024]
- [Agile Effort Estimation Improved by Feature Selection and...][research_perezpiqueras_2025]
- [An Empirical Study on Software Developer-Related Factors...][research_sawasdee_2025]
- [How do Community Smells Influence Self-Admitted Technical...][research_cynthia_2025]
- [Identifying Key Requirements Prioritization Criteria for...][research_pattyn_2025]
- [Negativity in self-admitted technical debt: how sentiment...][research_cassee_2025]
- [Software effort estimation using validated accuracy...][research_jeyaram_2025]
- [Swarm Intelligence for Software Effort Estimation: An...][research_laboudi_2025]
- [Understanding practitioners’ reasoning and requirements...][research_biazotto_2025]
- [A Rigorous Empirical Benchmark of Machine Learning Models...][research_jaskirat_2026]
- [An Empirical Study of Self-Admitted Technical Debt in...][research_bhatia_2026]
- [An empirical evaluation of white-box and black-box test...][research_arrieta_2026]
- [Effort-optimized, accuracy-driven labelling and...][research_amini_2026]
- [Hybrid Model for Improving the Accuracy of Software...][research_silva_2026]
- [Input perturbation robustness for software effort...][research_phannachitta_2026]
- [Leveraging explainable AI for requirements prioritization...][research_alhumam_2026]
- [Reducing labeling effort in architecture technical debt...][research_sutoyo_2026]
- [TagDebt: a bot to support technical debt management][research_biazotto_2026]
- [Test input prioritization for image segmentation: an...][research_li_2026_c]
- [Towards Interpretable Ensemble Learning for Software...][research_doshi_2026]
- [Understanding Self-Admitted Technical Debt in Test Code...][research_nakamura_2026]
- [VECTR: A Lightweight Requirements Prioritization Method...][research_pattyn_2026]

**Read for the ordering question, it is almost entirely a cost-side literature.** Effort estimation predicts
$\kappa$. Technical debt prioritisation ranks by remediation cost and interest.
**Nothing found here defines a blocking-frequency notion**, meaning a measure of how much delivered
capability is gated on a single unbuilt item, which is the quantity this article argues should lead.

### The runtime side, and reading machine code back

Two smaller bodies of work bound the subject. The choice between interpretation, just-in-time compilation
and ahead-of-time compilation is the alternative to native lowering rather than a part of it.

- [14. Compilation of dictionaries of the Chinese language][research_hongbo_2015]
- [A Bytecode Interpreter for Secure Program Execution in...][research_seitzer_2015]
- [A Software-Managed Approach to Die-Stacked DRAM][research_oskin_2015]
- [Formal Certification of Non-interferent Android Bytecode...][research_gunadi_2015]
- [Load Balancing in Decoupled Look-ahead: A Do-It-Yourself...][research_parihar_2015]
- [The Simian concept: Parallel Discrete Event Simulation...][research_santhi_2015]
- [Buddhist studies on Seokbosangjeol and tasks ahead...][research_oh_2016]
- [Compilation for Operation Execution Time Variability][research_pop_2016]
- [Programming GPUs with C++14 and Just-In-Time Compilation][research_haidlmichael_2016]
- [A Study of Virtual Machine Placement Optimization in Data...][research_challita_2017]
- [Adaptive just-in-time and relevant vector machine based...][research_liu_2017]
- [DRUT: An Efficient Turbo Boost Solution via Load...][research_parihar_2017]
- [Fast Failure Erasure Encoding Using Just in Time...][research_rohr_2017]
- [Just-In-Time GPU Compilation for Interpreted Languages...][research_fumero_2017]
- [Corpus Compilation and Exploitation in Language...][research_mosel_2018]
- [ClangJIT: Enhancing C++ with Just-in-Time Compilation][research_finkel_2019]
- [Just-In-Time Compilation for Verilog][research_schkufza_2019]
- [POSTER: Tango: An Optimizing Compiler for Just-In-Time...][research_tine_2019]
- [JIT Leaks: Inducing Timing Side Channels through...][research_brennan_2020]
- [PHPIL: Fuzzing the PHP Interpreter with Custom Bytecode][research_rao_2020]
- [Automatically exploiting the memory hierarchy of GPUs...][research_papadimitriou_2021]
- [Fractional Artificial Bee Chicken Swarm Optimization...][research_pushpa_2022]
- [Just-In-Time Compilation on ARM—A Closer Look at...][research_hartley_2022]
- [Just-in-Time Compilation and Link-Time Optimization for...][research_tian_2022]
- [Just-in-time scheduling in identical parallel machine...][research_goli_2022]
- [Preprocessing and Compilation][research_uzayr_2022]
- [Quantum simulation with just-in-time compilation][research_efthymiou_2022]
- [A Low-Level Virtual Machine Just-In-Time Prototype for...][research_stirb_2023]
- [AHEAD-OF-TIME and JUST-IN-TIME technologies][research_anon_2023_c]
- [CHERI Performance Enhancement for a Bytecode Interpreter][research_lowther_2023]
- [Hybrid Metaheuristic Technique for Optimization of...][research_chayan_2023]
- [Reducing the Compilation Time of Quantum Circuits Using...][research_quetschlich_2023_b]
- [Remote Just-in-Time Compilation for Dynamic Languages][research_pecimuth_2023]
- [Resource Optimization based Virtual Machine Allocation...][research_dubey_2023]
- [Reverse Engineering of Obfuscated Lua Bytecode via...][research_luo_2023]
- [Compilation Optimization Methods in the Customization of...][research_wang_2024_e]
- [Efficient Virtual Machine Allocation Technique Based on...][research_rawat_2024]
- [Interactive Programming for Microcontrollers by...][research_mochizuki_2024]
- [Accelerating Startup Time of React Native Applications by...][research_li_2025_j]
- [An efficient load balance using virtual machine migration...][research_sivalingam_2025]
- [FPGA-Accelerated Neural Network Inference via a...][research_park_2025]
- [From Source to Bytecode: How.py Becomes.pyc][research_kao_2025]
- [Intelligent Power Grid Startup Scheme Based on Rule...][research_wu_2025_c]
- [Proteus: Portable Runtime Optimization of GPU Kernel...][research_georgakoudis_2025]
- [Trace-Based Bytecode Interpreter Visualization for...][research_herber_2025]
- [WebAssembly: How Low Can a Bytecode Go?][research_titzer_2025]
- [AST, Bytecode, and the Space In Between: An Exploration...][research_larose_2026]
- [Designing quantum chemistry algorithms with just-in-time...][research_wu_2026]
- [Practical Python FPGA Acceleration with Fast Just-In-Time...][research_dickerson_2026]
- [Why Just-In-Time Compilation Matters: Evaluating Runtime...][research_maia_2026]
And the inverse problem
of recovering structure from machine code has its own methods.

- [Lifting Assembly to Intermediate Representation][research_hasabnis_2016]
- [Zipr: Efficient Static Binary Rewriting for Security][research_hawkins_2017]
- [Evolving Exact Decompilation][research_schulte_2018]
- [Towards Incremental Static Race Detection in OpenMP...][research_swain_2018]
- [CLIK on PLCs! Attacking Control Logic with Decompilation...][research_kalle_2019]
- [Performance, Correctness, Exceptions: Pick Three][research_gussoni_2019]
- [How far we have come: testing decompilation correctness...][research_liu_2020_b]
- [PARCOACH Extension for Static MPI Nonblocking and...][research_nguyen_2020]
- [High-Precision Evaluation of Both Static and Dynamic...][research_lin_2021_b]
- [Beyond the C: Retargetable Decompilation using Neural...][research_hosseini_2022]
- [NemesisGuard: Mitigating interrupt latency side channel...][research_salehi_2022]
- [Performant Binary Fuzzing without Source Code using...][research_pauley_2022]
- [Static Local Concurrency Errors Detection in MPI-RMA...][research_saillard_2022]
- [BIRD: A Binary Intermediate Representation for Formally...][research_engel_2023]
- [BREWasm: A General Static Binary Rewriting Framework for...][research_cao_2023]
- [Cross-Language Binary-Source Code Matching Based on Rust...][research_mao_2023]
- [Static Analysis of JNI Programs via Binary Decompilation][research_park_2023]
- [dewolf: Improving Decompilation by leveraging User Surveys][research_enders_2023]
- [Automatically Mitigating Vulnerabilities in Binary...][research_reiter_2025]
- [Binary Similarity Detection Based on Intermediate...][research_li_2025_k]
- [Binary–Source Code Matching Based on Decompilation...][research_aljebreen_2025]
- [dAngr: Lifting Software Debugging to a Symbolic Level][research_deruck_2025]
- [Does Representation Matter? Evaluating IRs for LLM-based...][research_pelayobenedet_2026]
- [LAPSE: Automatic, Formal Fault-Tolerant Correctness...][research_averill_2026]
- [LLM-assisted end-to-end binary decompilation: a...][research_alruqaishi_2026]
- [Large Language Models for Binary Decompilation...][research_wang_2026_b]
- [NOProbe: A NOP-Based Dynamic Binary Instrumentation...][research_bushehri_2026]
- [Representation learning for coincidental correctness in...][research_hu_2026_c]

**The second matters here for a methodological reason.** The instrument measures the compiler's bytecode
output rather than source text, which is a lifting problem in miniature, and the difficulties that
literature documents are the reasons the measurement was kept deliberately shallow.

### What the survey shows

**The ordering question is asked far more often than it was, by far more people, and it still has no published principle.**
Custom instruction sets, a universal new target, staged lowering pipelines and accelerator back ends have
all multiplied the occasions for asking it. The classics that did not answer it have been extended,
automated and verified, and the extensions do not answer it either.

**The one thing that changed decisively is the cost of finding out.** Corpus measurement became ordinary, so
the advice to measure before ordering costs almost nothing to follow.

**And the blindness is structural rather than accidental.** Compiler testing asks whether what exists is
correct. Coverage tooling asks how much of what exists is exercised. Verification asks whether what exists
is sound. **None of them asks what does not exist yet and what that absence costs**, because all three
presuppose the artefact. The question this article asks falls in the gap between building a compiler and
testing one, and that gap has no literature.

## The Source Base

**This survey rests on 3,155 records harvested from Crossref across sixty-one queries, filtered to 1,678 by removing homonym contamination and reduced to 1,650 by removing duplicate titles.**
The queries were written to span the argument rather than the subject, so each cluster corresponds to a
claim above instead of to a keyword.

**The filtering was not incidental and the failures explain the counts**, because they are the reason the
counts are what they are. A query on binary translation returned a large body of work on the static
dielectric constants of binary liquid mixtures. A query on code corpora returned linguistic corpora. A query
on interpreters returned the training of human interpreters. A venue-level filter alone was insufficient,
since a study of industrial chiller faults reached the shortlist through the word empirical in a
software-engineering venue.
**Every contaminant listed here was found by reading a sample of each cluster and none by anticipating it**,
which is the same lesson the article's own citation-defect section reports in a different setting.

**The period distribution is deliberate and is reported as a count rather than only as a fraction.** The
foundational base carries the derivations and stands at 111 references with a median year of 1997, of which
62 predate 2000. The contemporary base carries this survey.
**Adding a contemporary survey lowers the primary fraction while leaving the primary count unchanged**, so
the fraction on its own would read as a regression when it is the directive working.

**One property of this survey's references matters here, because the article devotes a section to the opposite case.**
The citation defect reported earlier arose because identifiers were supplied from memory, so a digital
object identifier could be paired with a title it did not belong to.
**These were retrieved rather than recalled.** The identifier, title, author and year of each come from a
single record, so the substitution failure is not available here by construction.
**That is a structural guarantee and not a verified one**, and what verification can still add is
resolvability, checked on a random sample of 120 of the 1,650, all of which resolve.
**The foundational references were checked exhaustively instead**, at 86 of 86 digital object identifiers
resolving to the claimed author and year.

**What the source base cannot do is establish an absence.** The claim that no published ordering principle
exists is supported by not finding one across these queries, which is weaker than a proof and is stated that
way in the Epistemic State below.

## Epistemic State

**Measured, and reproducible from the instrument.** The corpus comprises 63 files of which 58 compiled,
yielding 496 compilation units and 73,434 instruction instances. The implemented subset was 39 of 66
instructions. Instruction-level coverage was 0.8731 and unit-level coverage 0.3387, for a gap of 0.5344. The
leading workstream blocked 267 units against 28 for the next, a ratio of 9.54. The instruction class the
falsified recommendation would have unblocked occurs zero times. Of 91 candidate digital object identifiers
supplied from memory, four resolved to different works and one did not resolve, an error rate of 5.5
percent.

**Later data, added as an addendum and not as a correction.** Three subsequent articles in this series
measured the same thing the same way, and the pattern across them says more than any single figure does.
**Nothing above is withdrawn.**

| Article | Identifiers checked | Needing correction | Rate |
|---|---|---|---|
| This article | 91 | 5 | 5.5 percent |
| The calling-convention article | 35 | 0 | 0 percent |
| The resource-bound article | 27 | 4 | 14.8 percent |
| The aggregate-cost article | 26 | 7 | 26.9 percent |

**The rate is not a measure of care**, since all four bibliographies were assembled and checked the same way.
What varies is the material. The zero-rate article draws on recent, widely cited works with distinctive
identifiers, while the highest-rate article draws on older conference papers, many from one proceedings
series.

**The failure mode that dominates is the one a working link cannot catch.** Four of the seven corrections in
the highest-rate article were neighbouring identifiers in the same proceedings volume, differing by one or
two digits in the suffix. Such an identifier resolves cleanly and returns a plausible paper in the right
field, and it is wrong. **It is caught only by comparing the resolved title against the cited title**, which
is why that comparison is load-bearing rather than fastidious.

Two further classes are instrument artefacts rather than citation defects, and separating them matters
because they inflate any reported rate. **A registry may store a title and its subtitle in different
fields**, so a citation giving both overlaps the stored title poorly while being correct. **And a work may be
registered with a different agency**, so querying one registry returns nothing for a perfectly valid
identifier. **A rate reported without separating these two classes from genuine mismatches is an upper
bound.** This article's own figure needed no such separation, because its identifiers carry neither pattern.

**Derived, and checkable from the definitions.** That unit-level coverage cannot exceed instruction-level
coverage follows from the product form. That the objective is supermodular and not submodular, so that the
classical greedy approximation guarantee does not apply, is established by counterexample. The clustering
coefficient of 5.51 and the confidence bounds on the zero counts follow from the stated method.

**Assumed, and marked as such.** The first-blocker attribution is order-dependent and the full blocking
lattice was not computed, so **the ordering of the second, third and fourth workstreams is not established**
and no claim about it should be read as such. The cost ratio between the measurement and the work it
redirected is an order of magnitude rather than a quantity, because its numerator is measured and its
denominator is an estimate of work never performed.

**Corrected during writing, and left visible.** An independence null was first evaluated at the mean
compilation-unit length rather than per unit, which would have inflated a clustering coefficient by seven
orders of magnitude. A modularity theorem was asserted that the objective does not admit. A citation defect
rate was first reported as near ten percent over the worse subsample rather than 5.5 percent over the full
one. **The conclusion that operand type recovery was worthless was itself too broad**, since the capability
was later required by a different workstream for an unrelated reason, at 18 compilation units. The zero was
correct and the inference from it was not.

**What the article does not establish.** Whether the corpus resembles the population the generator will
eventually serve, since it is drawn from one project's own examples and over-represents a text-processing
workload. Whether the classification of instructions into workstreams was drawn neutrally, since the party
that made the falsified recommendation also wrote the instrument that falsified it.
**The article offers the classification for inspection as mitigation and does not claim the concern is closed.**

**The strongest claim the evidence supports** is that on this corpus, at this implemented subset, a
frequency measurement redirected work away from an item that would have delivered exactly zero.
**The weakest link is corpus representativeness**, and a reader who doubts it should read the ordering as
established for the present consumer rather than for the eventual one.

## Out of Scope

The design of the code generator itself, and the lowering strategy for any particular instruction. The
worst-case execution time and memory analysis that motivates the project, which is a separate subject.
Register allocation, instruction scheduling and peephole optimisation, none of which the ordering question
touches. Dynamic profiling, since the measurement here is static by design and the two answer different
questions. The exact Shapley attribution over the blocking lattice, which is affordable at 64 corpus passes
and was not performed. Any claim about execution time, which would require a different and considerably more
careful methodology. The Keleusma language itself and its implementation history, which are covered in
[the getting-started article][related_post_keleusma_022] and
[the self-hosting strategy][related_post_keleusma_self_hosting].

## Conclusion

**Eighty-seven percent of the instructions and thirty-four percent of the programs are the same compiler on the same day.**
The first number is what a progress report contains and the second what a user experiences, and the distance
between them is created entirely by the fact that a program needs every instruction it uses.

**The practical rule is short.** When a consumer requires a conjunction of features, per-feature progress
overstates delivered capability, and the amount of the overstatement is not visible from inside the work.
**Dependency analysis tells you what is required before something can be built. It tells you nothing about whether anyone needs it**,
and those two questions are independent in a way that is easy to miss because the first is more satisfying
to answer.

**The measurement that settles it is usually trivial next to the work it redirects.** Twenty minutes of
instrument against a research spike, in this case, and the spike would have delivered nothing.

**The last part is the least comfortable and the most useful.** Four errors were made in producing this
article and every one of them pointed toward a more striking result. None was found by rereading. Each was
found by running something, whether a numerical evaluation whose answer was implausible, an enumeration over
small cases, a query against an authoritative record, or a recount over the full sample rather than the
remembered one. **The fourth was committed while writing the warning about the first three**, which is the
clearest evidence available that knowing about a bias does not protect anyone from it.

## References

### Reference

- [LLVM Language Reference][ref_llvm_langref]
- [Oracle Java Virtual Machine Specification][ref_jvm_spec]

[ref_jvm_spec]: https://docs.oracle.com/javase/specs/jvms/se21/html/index.html
[ref_llvm_langref]: https://llvm.org/docs/LangRef.html

### Related Post

- [Related Post, Getting Started with Keleusma 0.2.2][related_post_keleusma_022]
- [Related Post, The Self-Hosted Silicon Compiler][related_post_self_hosted_silicon]
- [Related Post, Keleusma's Self-Hosting Strategy][related_post_keleusma_self_hosting]
- [Related Post, The Stream Processor as Compiler and the Compiler as Stream Processor][related_post_compilers_streaming]

[related_post_compilers_streaming]: {% post_url 2026-04-17-stream_processor_as_compiler_and_compiler_as_stream_processor %}
[related_post_keleusma_022]: {% post_url 2026-07-11-keleusma_0_2_2_getting_started %}
[related_post_keleusma_self_hosting]: {% post_url 2026-07-12-keleusma_self_hosting_strategy %}
[related_post_self_hosted_silicon]: {% post_url 2026-07-10-self_hosted_silicon_compiler %}

### Research

- ["A Multi-Pass Compiler with Code Optimized Abstract...][research_odim_2023]
- [$\mu \text{PRL}$: A Mutation Testing Pipeline for Deep...][research_thomas_2025]
- [12.4 - Machine Learning-Driven Test Case Prioritization...][research_lachmann_2018]
- [14. Compilation of dictionaries of the Chinese language][research_hongbo_2015]
- [23 shades of self-admitted technical debt: an empirical...][research_obrien_2022]
- [3CPS: The Design of an Environment-Focussed Intermediate...][research_quiring_2021]
- [A basic linear algebra compiler for structured matrices][research_spampinato_2016]
- [A benchmark study on the effectiveness of search-based...][research_hosseini_2018]
- [A buffer overflow detection and defense method based on...][research_liu_2023]
- [A Bytecode Interpreter for Secure Program Execution in...][research_seitzer_2015]
- [A Calculus for Web Services Choreography: Formal...][research_yang_2026]
- [A Case Study in Formal Specification and Runtime...][research_luppen_2021]
- [A Collaborative Effort-Benefit-Value Analysis Model to...][research_gupta_2021]
- [A comparative analysis of the role of Large Language...][research_patricio_2026]
- [A Comparative Evaluation of Prompting Strategies for Code...][research_fanyizhao_2024]
- [A Compilation of Experimental Binary Alloy Surface...][research_mazurowski_2024]
- [A Compiler Approach for Exploiting Partial SIMD...][research_zhou_2016]
- [A compiler architecture for domain-specific type error...][research_serrano_2019]
- [A Compiler Comparison in the RISC-V Ecosystem][research_poorhosseini_2020]
- [A compiler for cyber-physical digital microfluidic...][research_curtis_2018]
- [A Compiler for Sound Floating-Point Computations using...][research_rivera_2022]
- [A Comprehensive Study of Bugs in Embedded WebAssembly...][research_zheng_2023]
- [A Comprehensive Study of WebAssembly Runtime Bugs][research_wang_2023]
- [A Comprehensive Study on Code Coverage Analysis for...][research_bandyopadhyay_2022]
- [A Comprehensive Trusted Runtime for WebAssembly With...][research_menetrey_2024]
- [A Control Flow based Static Analysis of GRAFCET using...][research_schnakenbeck_2023]
- [A Convolutional Neural Network for Language-Agnostic...][research_moore_2019]
- [A cooperative game theory application in chicks brood...][research_haque_2020]
- [A cost model for a graph-based...][research_leopoldseder_2018_b]
- [A Customized Real-Time Compilation for Motion Control in...][research_wu_2019]
- [A Defect Taxonomy for Infrastructure as Code: A...][research_oliveira_2025]
- [A detailed investigation of the effectiveness of whole...][research_rojas_2016]
- [A Digital Twin Modeling Code Generation Framework based...][research_dong_2024]
- [A distributed algorithm for partitioned robust submodular...][research_bogunovic_2017]
- [A Domain-Specific Compiler for a Parallel Multiresolution...][research_rajbhandari_2016]
- [A Domain-Specific Compiler for Embedded DSP Development...][research_zhu_2025]
- [A Domain-Specific Language and Compiler for...][research_yu_2017]
- [A Formal Approach based on Fuzzy Logic for the...][research_koutsoumpas_2015]
- [A Formal Proof of the Soundness of the Hybrid CPS Clock...][research_wang_2020]
- [A Formal Verification Library Design for Behavioral...][research_kim_2025]
- [A formally verified compiler for Lustre][research_bourke_2017]
- [A Formally Verified Microcoded RISC-V Platform][research_klemmer_2025]
- [A Fully Automated Agent for End-to-End Code Translation...][research_erer_2025]
- [A fully verified container library][research_polikarpova_2018]
- [A graph-based iterative compiler pass selection and phase...][research_nobre_2016]
- [A Graph-Based Learning Framework for Compiler Loop...][research_xiao_2025]
- [A High Performance Sparse Tensor Algebra Compiler in MLIR][research_tian_2021]
- [A Hotspot-Driven Semi-automated Competitive Analysis...][research_mu_2023]
- [A Large Scale Analysis of Semantic Versioning in NPM][research_pinckney_2023]
- [A Large Scale Study of License Usage on GitHub][research_vendome_2015]
- [A Large Scale Study of Long-Time Contributor Prediction...][research_bao_2021]
- [A Large-Scale Comparative Evaluation of IR-Based Tools...][research_akbar_2020]
- [A large-scale comparison of Python code in Jupyter...][research_grotov_2022]
- [A large-scale dataset of (open source) license text...][research_zacchiroli_2022]
- [A Large-Scale Dataset of MCP Implementations on GitHub][research_toeppe_2026]
- [A large-scale empirical comparison of static and dynamic...][research_luo_2016_b]
- [A large-scale empirical study of configurations, errors...][research_zhang_2026_e]
- [A Large-Scale Empirical Study of COVID-19 Themed GitHub...][research_wang_2021_b]
- [A Large-Scale Empirical Study of Open Source License...][research_wu_2024]
- [A large-scale empirical study on self-admitted technical...][research_bavota_2016]
- [A Large-Scale Investigation Into the Loss of Pull Request...][research_tang_2026]
- [A Large-Scale Study About Quality and Reproducibility of...][research_pimentel_2019]
- [A large-scale study of call graph-based impact prediction...][research_musco_2016]
- [A large-scale study of programming languages and code...][research_ray_2017]
- [A Large-Scale Study of the Impact of Feature Selection...][research_ghotra_2017]
- [A large-scale study on human-cloned changes for automated...][research_madeiral_2021]
- [A large-scale study on repetitiveness, containment, and...][research_nguyen_2016]
- [A large-scale study on the usage of Java’s concurrent...][research_pinto_2015]
- [A low-cost synthesizable RISC-V dual-issue processor core...][research_patsidis_2018]
- [A Low-Level Virtual Machine Just-In-Time Prototype for...][research_stirb_2023]
- [A machine-checked correctness proof for Pastry][research_azmy_2018]
- [A machine-checked direct proof of the Steiner-lehmus...][research_kellison_2022]
- [A MATLAB Vectorizing Compiler Targeting...][research_latifis_2017]
- [A Mechanical Soundness Proof for Subtyping Over Recursive...][research_jones_2016]
- [A Mechanised and Constructive Reverse Analysis of...][research_shillito_2024]
- [A Mechanism for Automatically Extracting Reusable and...][research_papoudakis_2022]
- [A Methodology for Analysing Code Anomalies in Open-Source...][research_campbell_2024]
- [A minimalistic verified bootstrapped compiler (proof...][research_myreen_2021]
- [A Model-Agnostic Feature Attribution Approach to...][research_fan_2023]
- [A Multi-Armed Bandit Approach for Test Case...][research_lima_2022]
- [A Multi-Expert Large Language Model Architecture for...][research_nadimi_2024]
- [A Multi-pass Streaming Algorithm for Regularized...][research_gong_2021]
- [A New Functional-Logic Compiler for Curry: Sprite][research_antoy_2017]
- [A new verified compiler backend for CakeML][research_tan_2016]
- [A Novel Counterexample-Guided Inductive Synthesis...][research_ding_2022]
- [A novel online supervised hyperparameter tuning procedure...][research_minku_2019]
- [A Novel Prediction Model for Compiler Optimization with...][research_kadam_2022]
- [A Pluggable Vector Unit for RISC-V Vector Extension][research_maisto_2022]
- [A practical approach for technical debt prioritization...][research_tsoukalas_2023]
- [A Preliminary Framework for Optimising Test Case...][research_ndlovu_2024]
- [A Preliminary Study of Fixed Flaky Tests in Rust Projects...][research_schroeder_2025]
- [A primal-dual algorithm for monotone submodular...][research_chakrabarty_2026]
- [A Priority-Ordered Swapping Algorithm for Submodular...][research_peng_2026]
- [A Programming Approach for Worst-case Studies in...][research_downie_2022]
- [A Proof Score Approach to Formal Verification of an...][research_daudier_2018]
- [A Proof-Producing Compiler for Blockchain Applications][research_avigad_2025]
- [A proposed synthesis method for Application-Specific...][research_horvath_2015]
- [A Qualitative Study on the Sources, Impacts, and...][research_habchi_2022]
- [A QUANTITATIVE ANALYSIS OF WEBASSEMBLY INTEGRATION...][research_stepanov_2025]
- [A Reinforcement Learning Environment for Automatic Code...][research_tirichine_2026]
- [A Review on Continuous Integration and Continuous...][research_mahida_2021]
- [A Rigorous Empirical Benchmark of Machine Learning Models...][research_jaskirat_2026]
- [A RISC-V Instruction Set Extension for Flexible...][research_lozachmeur_2023]
- [A RISC-V instruction set processor-micro-architecture...][research_raveendran_2016]
- [A RISC-V Post Quantum Cryptography Instruction Set...][research_nannipieri_2021]
- [A RISC-V Vector Extension for Multi-word Arithmetic][research_lan_2025]
- [A Rose Tree Is Blooming (Proof Pearl)][research_korkut_2026]
- [A Safe Low-Level Language for Computer Algebra and Its...][research_melquiond_2024]
- [A Scalable and Efficient Intrusion Detection System Based...][research_rocca_2025]
- [A Self-certifying Compilation Framework for WebAssembly][research_namjoshi_2021]
- [A Semantics of Structures, Unions, and Underspecified...][research_gauthier_2024]
- [A Semi-streaming Algorithm for Monotone Regularized...][research_nong_2024]
- [A Shapley-value cooperative game-based risk decision...][research_wang_2026]
- [A simple soundness proof for dependent object types][research_rapoport_2017]
- [A Software-Managed Approach to Die-Stacked DRAM][research_oskin_2015]
- [A stability assessment of solution adaptation techniques...][research_phannachitta_2016]
- [A Stacking Ensemble-based Approach for Software Effort...][research_shukla_2021]
- [A streaming algorithm for non-monotone regularized...][research_zhang_2026_f]
- [A Streaming Model for Monotone Lattice Submodular...][research_zhang_2021_b]
- [A study of common bug fix patterns in Rust][research_robatishirzad_2024]
- [A Study of Virtual Machine Placement Optimization in Data...][research_challita_2017]
- [A study on the lifecycle of flaky tests][research_lam_2020]
- [A Survey of Automatic Generation of Source Code Comments...][research_song_2019]
- [A Survey of Optimized Compiler Using Advanced Machine...][research_pandey_2024]
- [A systematic literature review of technical debt...][research_alfayez_2020]
- [A Systematic Literature Review on Automated Program...][research_hamdi_2026]
- [A systematic literature review on Technical Debt...][research_lenarduzzi_2021]
- [A Systematic Review about Large Language Models (LLMs)...][research_alecsandrobaci_2025]
- [A Taste of the Software Industry Perception of Technical...][research_apa_2020]
- [A Taxonomy of Spanish Nouns, a Statistical Algorithm to...][research_nazar_2016]
- [A Tensor Algebra Compiler for Sparse Differentiation][research_shaikhha_2024]
- [A Time Window based Reinforcement Learning Reward for...][research_wu_2019_b]
- [A Time-Predictable Multicore RISC-V Architecture for...][research_munezero_2026]
- [A Trigonometric Function Instruction Set Extension Method...][research_gao_2022]
- [A Two-step Approach to Find Short Compilation...][research_delatorre_2025]
- [A Universal Quantum Compiler GPT: Multi-Framework...][research_petchartee_2025]
- [A Verified CompCert Front-End for a Memory Model...][research_besson_2017]
- [A Verified Compiler for a Functional Tensor Language][research_liu_2024_b]
- [A Verified Compiler from Isabelle/HOL to CakeML][research_hupel_2018]
- [A Verified Generational Garbage Collector for CakeML][research_sandbergericss_2017]
- [A Verified Generational Garbage Collector for CakeML][research_sandbergericss_2018]
- [A verified protocol buffer compiler][research_ye_2019]
- [A verified type system for CakeML][research_tan_2015]
- [A Way to Identify Potential Functions for Vectorization...][research_stojkovic_2025]
- [A XOR data compiler: Combined with physical unclonable...][research_cambou_2017]
- [Abstract Interpretation of Supermodular Games][research_ranzato_2016]
- [Abstract Interpretation with Infinitesimals][research_kido_2015]
- [Academic english writing generation-evaluation...][research_yingzhe_2026]
- [Accelerating Embedded WebAssembly Based on FPGA][research_kim_2024]
- [Accelerating H.264/HEVC video slice processing using...][research_mandal_2015]
- [Accelerating Machine Learning using RISC-V Vector...][research_nunes_2025]
- [Accelerating Machine Learning with RISC-V Vector...][research_nunes_2025_b]
- [Accelerating NTT with RISC-V Vector Extension for Fully...][research_rodrigues_2025]
- [Accelerating Sparse Algebra with Program Synthesis][research_desouzamagalha_2026]
- [Accelerating Startup Time of React Native Applications by...][research_li_2025_j]
- [Accelerating Syntax-Guided Program Synthesis by...][research_ye_2026]
- [Acceleration of McEliece Cryptosystem with Instruction...][research_kennedy_2025]
- [Accessible Formal Methods for Verified Parser Development][research_li_2021]
- [Accuracy Comparison of Analogy-Based Software Development...][research_idri_2015]
- [Accurate Compiler and Optimization Independent Function...][research_mckee_2023]
- [Accurate quasi-P traveltimes in 3D transversely isotropic...][research_padhi_2017]
- [Accurate quasi-SV traveltimes in 3D transversely...][research_padhi_2019]
- [Achieving High-Integrity Software Quality and Security...][research_niharika_2025]
- [Adaptive and Explainable Test Case Prioritization in...][research_kongarana_2026]
- [Adaptive just-in-time and relevant vector machine based...][research_liu_2017]
- [Adaptivity in AdaptiveCpp: Optimizing Performance by...][research_alpay_2025]
- [Adjustable-Cost Overlays for Runtime Compilation][research_coole_2015]
- [Adopting DevOps Paradigm in Technical Debt Prioritization...][research_stochel_2022]
- [Advanced ahead-of-time compilation for Javascript engine][research_park_2017]
- [Advancements and Challenges of Large Language Model-Based...][research_wang_2024_d]
- [Advancements in AI-Based Compiler Optimization Techniques...][research_shankar_2025]
- [Agile Autotuning of a Transprecision Tensor Accelerator...][research_diamantopoulos_2020]
- [Agile Effort Estimation Improved by Feature Selection and...][research_perezpiqueras_2025]
- [Agresti and Coull 1998][research_agresti_coull_1998]
- [Ahead of Time Generation for GPSA Protection in RISC-V...][research_savary_2025]
- [AHEAD-OF-TIME and JUST-IN-TIME technologies][research_anon_2023_c]
- [Ahead-of-time Compilation for Diverse Samplers of...][research_madkour_2024]
- [Ahead-of-time compilation of JavaScript programs][research_zhuykov_2017]
- [Aho, Ganapathi and Tjiang 1989][research_aho_ganapathi_1989]
- [AHP_GORE_PSR: Applying analytic hierarchy process in goal...][research_sadiq_2017]
- [AI builds, We Analyze: An Empirical Study of AI-Generated...][research_ghammam_2026]
- [AI Edge Processor Using RISC - V Instruction Set...][research_borade_2025]
- [AI for Code: Reinforcement-Learned Compiler Optimizations...][research_peta_2025]
- [AI Techniques for Software Requirements Prioritization][research_felfernig_2021]
- [AI-Driven Test Case Generation for Continuous Integration...][research_subrahmanyam_2025]
- [AIWC: OpenCL-Based Architecture-Independent Workload...][research_johnston_2018]
- [Algorithms to estimate Shapley value feature attributions][research_chen_2023_b]
- [Alive-FP: Automated Verification of Floating Point Based...][research_menendez_2016]
- [Alive-Infer: data-driven precondition inference for...][research_menendez_2017]
- [AliveInLean: A Verified LLVM Peephole Optimization...][research_lee_2019_b]
- [Allamanis and Sutton 2013][research_allamanis_sutton_2013]
- [Allen 1970][research_allen_1970]
- [Alumni’s Perception on Program Specification of ELT...][research_refnaldi_2019]
- [Amdahl 1967][research_amdahl_1967]
- [An Agile Instruction Set Extension Method Based on the...][research_hu_2021]
- [An Analysis of Modern Web Security Vulnerabilities Inside...][research_corrias_2026]
- [An application of metamorphic testing for testing...][research_ding_2016]
- [An application specific instruction set processor (ASIP)...][research_hu_2018]
- [An Application-specific Instruction Set Processor for...][research_brenes_2019]
- [An Application-Specific Instruction Set Processor for...][research_vaas_2016]
- [An Application-Specific VLIW Processor with Vector...][research_bytyn_2019]
- [An approach to generate text-based IDEs for syntax...][research_sasano_2020]
- [An Approximation Algorithm for Distributed Resilient...][research_zhou_2019]
- [An Automatic Generation and Verification Method of...][research_wei_2023]
- [An Effective GRU-Based Deep Learning Method for Test Case...][research_behera_2025]
- [An Efficient Application Specific Instruction Set...][research_huang_2019]
- [An Efficient Application Specific Instruction Set...][research_liu_2022]
- [An efficient load balance using virtual machine migration...][research_sivalingam_2025]
- [An Effort Estimation Support Tool for Agile Software...][research_dantas_2019]
- [An Embedded RISC-V Vector Extension for Edge-Oriented...][research_corral_2026]
- [An Empirical Analysis of Issue Templates Usage in...][research_sulun_2024]
- [An Empirical Analysis of UI-Based Flaky Tests][research_romano_2021]
- [An Empirical Approach for Estimation of the Software...][research_jakhar_2015]
- [An Empirical Comparison of Human and LLM-Assisted Bug...][research_nasui_2026]
- [An Empirical Comparison of Similarity Measures for...][research_huang_2017]
- [An empirical evaluation of ensemble adjustment methods...][research_azzeh_2015]
- [An empirical evaluation of white-box and black-box test...][research_arrieta_2026]
- [An Empirical Investigation on Effort Estimation in Agile...][research_britto_2015]
- [An Empirical Study of Activity, Popularity, Size...][research_gautam_2017]
- [An Empirical Study of Aging Related Bug Prediction Using...][research_kaur_2022]
- [An Empirical Study of Bug Bounty Programs][research_walshe_2020]
- [An Empirical Study of Bug Fixing Rate][research_zou_2015]
- [An empirical study of bugs in test code][research_vahabzadeh_2015]
- [An Empirical Study of Counterexample-Guided Fuzzing for...][research_yi_2020]
- [An Empirical Study of Flaky Tests in Android Apps][research_thorve_2018]
- [An Empirical Study of Flaky Tests in JavaScript][research_hashemi_2022]
- [An Empirical Study of Flaky Tests in Python][research_gruber_2021]
- [An Empirical Study of Greedy Test Suite Minimization...][research_jehan_2023]
- [An empirical study of inadequate and adequate test suite...][research_coviello_2018]
- [An Empirical Study of Multi-entity Changes in Real Bug...][research_wang_2018]
- [An Empirical Study of Real-World WebAssembly Binaries][research_hilbig_2021]
- [An empirical study of regression test suite reduction...][research_singhal_2017]
- [An Empirical Study of Regression Testing for Android Apps...][research_wang_2023_d]
- [An Empirical Study of SBOM Usage Through GitHub Actions][research_kanemoto_2026]
- [An Empirical Study of Self-Admitted Technical Debt in...][research_bhatia_2026]
- [An Empirical Study of Technical Debt in Open-Source...][research_alfayez_2017]
- [An Empirical Study of the Bug Link Rate][research_li_2022_b]
- [An empirical study of the effectiveness of IR-based bug...][research_li_2022_c]
- [An empirical study of the long duration of continuous...][research_ghaleb_2019]
- [An Empirical Study of the Personnel Overhead of...][research_manglaviti_2017]
- [An Empirical Study of the Relationship between Continuous...][research_sizilionery_2019]
- [An Empirical Study of Web Flaky Tests: Understanding and...][research_pei_2025]
- [An Empirical Study on Code Coverage of Performance Testing][research_imran_2024]
- [An Empirical Study on Effects of Code Visibility on Code...][research_ma_2015]
- [An empirical study on how expert knowledge affects bug...][research_rodeghero_2016]
- [An Empirical Study on Real Bug Fixes][research_zhong_2015]
- [An Empirical Study on Real Bugs for Machine Learning...][research_sun_2017]
- [An empirical study on self-admitted technical debt in...][research_azuma_2022]
- [An Empirical Study on Self-Admitted Technical Debt in...][research_ishimoto_2024]
- [An Empirical Study on Software Developer-Related Factors...][research_sawasdee_2025]
- [An Empirical Study on Software Test Effort Estimation for...][research_cibir_2022]
- [An Empirical Study on Technical Debt in a Finnish SME][research_lenarduzzi_2019]
- [An empirical study on the application of mutation testing...][research_ramler_2017]
- [An Empirical Study on the Correlation between Neuron...][research_li_2023_d]
- [An Empirical Study on the Cross-Project Predictability of...][research_xia_2017]
- [An Empirical Study on the Impact of Aspect-oriented...][research_menolli_2021]
- [An empirical study on the potential of word embedding...][research_chen_2024_b]
- [An Environment Adaptation Agent of Reinforcement Learning...][research_li_2025_e]
- [An Evaluation Method for Large Language Models’ Code...][research_su_2023]
- [An Evaluation of Ranking-to-Learn Approaches for Test...][research_lima_2023]
- [An Evaluation of Selection Methods for Time-Aware Effort...][research_amasaki_2017]
- [An Experimental Analysis of RL based Compiler...][research_nikith_2024]
- [An Explainable Deep Learning Model in Improving Test Case...][research_ramakrishnan_2025]
- [An exploratory study of bug-introducing changes...][research_schulte_2026]
- [An Exploratory Study on Soft Skills present in Software...][research_kapitsaki_2024]
- [An extended study on applicability and performance of...][research_amasaki_2022]
- [An extension to the RISC-V instruction set architecture...][research_jones_2023]
- [An extensive replication study of the ABLoTS approach for...][research_niu_2024]
- [An Extreme Learning Machine based Approach for Software...][research_shukla_2021_b]
- [An FPGA-Based RISC-V Instruction Set Extension and Memory...][research_ibrahim_2024]
- [An Improved Method for Test Case Prioritization in...][research_han_2023]
- [An Improved Shapley Value Benefit Distribution Mechanism...][research_xie_2020]
- [An Improved Space Semi-Streaming Algorithm for Submodular...][research_bao_2024]
- [An Improvement to Test Case Prioritization Techniques...][research_khan_2022]
- [An Industrial Application of Mutation Testing: Lessons...][research_petrovic_2018]
- [An Initiative to Improve Reproducibility and Empirical...][research_oliveiraneto_2015]
- [An Innovation Study on Luggage Wheel Design for Seamless...][research_kurudirek_2025]
- [An innovative approach for automatic generation...][research_sortino_2015]
- [An innovative machine learning workflow to research...][research_wang_2024_c]
- [An Interval Compiler for Sound Floating-Point Computations][research_rivera_2021]
- [An MLIR-based Compiler Flow for System-Level Design and...][research_agostini_2022]
- [An MLIR-Based Compiler for Hardware Acceleration with...][research_li_2024]
- [An optimal streaming algorithm for non-submodular...][research_liu_2022_b]
- [An Optimal Streaming Algorithm for Submodular...][research_alaluf_2022]
- [An optimizing compiler for a purely functional...][research_chlipala_2015]
- [An overview of evaluation and enhancement methods for...][research_truong_2026]
- [An Ultralow-latency Constrained Quadratic Program (QP)...][research_jimoh_2026]
- [Analogy-Based Approaches to Improve Software Project...][research_resmi_2019]
- [Analysis of benchmark program results of worst case...][research_paraman_2023]
- [Analysis of task effort estimation accuracy based on use...][research_popovic_2015]
- [Analysis of the RISC-V Vector Extension for Vulkan...][research_troiber_2025]
- [Analysis of WebAssembly as a Strategy to Improve...][research_oliveira_2020]
- [Analytics-Driven Load Testing: An Industrial Experience...][research_chen_2017]
- [Analyzing Data Flow and Control Flow of Multicore...][research_thomas_2024]
- [Analyzing False Positive Source Code Vulnerabilities...][research_cheirdari_2018]
- [Andrews and colleagues 2005][research_andrews_2005]
- [AndroidCompass: A Dataset of Android Compatibility Checks...][research_nielebock_2021]
- [APICoder: A Multi-Role Large Language Model Framework for...][research_yang_2025]
- [Appel 1998][research_appel_1998]
- [Application of an Improved Shapley Value Method in...][research_ma_2022]
- [Application of Property-based Testing Tools for...][research_alzahrani_2022]
- [Application of WebAssembly for High-Performance...][research_anon_2025]
- [Application Specific Instruction Set Processor Design for...][research_samal_2019]
- [Application specific instruction set processor for sensor...][research_sisto_2016]
- [Application-Specific Instruction Set Processor][research_chakravarthi_2025]
- [Application-Specific Instruction Set Processors for Video...][research_kim_2017]
- [Applications and Computation of the Shapley Value in...][research_luo_2024]
- [Applying Knowledge-Guided Deep Reinforcement Learning...][research_li_2025_h]
- [Applying test case prioritization to software...][research_laaber_2021]
- [Approximation Algorithm for Connected Submodular Function...][research_xu_2024]
- [APR4Vul: an empirical study of automatic program repair...][research_bui_2023]
- [Architecture of a tool for automated testing the...][research_fedasyuk_2017]
- [Archs: A WebAssembly Runtime for Cross-host Heterogeneous...][research_sun_2025]
- [Are mutation scores correlated with real fault detection?][research_papadakis_2018]
- [Are tweets useful in the bug fixing process? An empirical...][research_mezouar_2017]
- [ArkTS code generation: A comprehensive evaluation with...][research_erkus_2026]
- [Artifact for article: Exact and Approximate Methods for...][research_hu_2020]
- [Artifact for Lifting Code Generation of Cardiac...][research_thangamani_2023]
- [Asking about Technical Debt: Characteristics and...][research_kozanidis_2022]
- [ASPIRE: An Intermediate Representation for Abstract...][research_bhamidipati_2023]
- [Assessing and Improving the Mutation Testing Practice of...][research_laurent_2017]
- [Assessing the Impact of Compiler Optimizations on GPUs...][research_santos_2024_b]
- [Assessing the Test Suite of a Large System Based on Code...][research_vidacs_2016]
- [Assessment and Comparison of Fuzzy Based Test Suite...][research_chaudhary_2016]
- [Assessment of off-the-shelf SE-specific sentiment...][research_novielli_2021]
- [Association Rule Learning Based Approach to Automatic...][research_ferchichi_2024]
- [Assuring Correctness, Testing, and Verification of...][research_sanusi_2024]
- [AST, Bytecode, and the Space In Between: An Exploration...][research_larose_2026]
- [Attention Transfer Reinforcement Learning for Test Case...][research_su_2025]
- [Audio Denoising Coprocessor Based on RISC-V Custom...][research_yuan_2022]
- [Augmenting JavaScript JIT with ahead-of-time compilation][research_zhuykov_2015]
- [Automated C/C++ Program Repair for High-Level Synthesis...][research_xu_2024_b]
- [Automated compiler optimization of multiple vector...][research_aleen_2016]
- [Automated Compiler Optimization of Multiple Vector...][research_aleen_2017]
- [Automated formal verification of the refined...][research_maron_2016]
- [AUTOMATED GENERATION AND EVALUATION OF VOCABULARY TESTS...][research_nakanishi_2025]
- [Automated Inference of Expressive Metamorphic Relations...][research_nolasco_2026]
- [Automated NFR testing in continuous integration...][research_yu_2023]
- [Automated Program Repair in the Era of Large Pre-trained...][research_xia_2023]
- [Automated SC-MCC test case generation using...][research_golla_2024]
- [Automated selection of a software effort estimation model...][research_nayebi_2015]
- [Automated Test Case Generation from OTS/CafeOBJ...][research_mori_2017]
- [Automated Test Generation from Program Documentation...][research_denaro_2025]
- [Automated Testing to Evaluate Employee Attendance System...][research_hafizhah_2024]
- [Automated WebAssembly Function Purpose Identification...][research_romano_2023]
- [Automatic Benchmark Generation for Object Constraint...][research_jha_2023]
- [Automatic compiler optimization on embedded software...][research_werner_2020]
- [Automatic compiler/interpreter generation from programs...][research_kovacevic_2022]
- [Automatic complex instruction identification for...][research_nery_2015]
- [Automatic Configurable Hardware Code Generation for...][research_tsoeunyane_2018]
- [Automatic data layout generation and kernel mapping for...][research_majeti_2016]
- [Automatic Generation of Assertions for Functional...][research_heidariiman_2025_b]
- [Automatic Generation of Assertions for Security...][research_heidariiman_2025]
- [Automatic generation of fast BLAS3-GEMM: A portable...][research_su_2017]
- [Automatic Generation of Multi-Objective Polyhedral...][research_chelini_2020]
- [Automatic generation of simulation workflows for system...][research_hammadi_2017]
- [Automatic Generation of the AADL ALISA Verification Plan...][research_wu_2017]
- [Automatic identification of self-admitted technical debt...][research_li_2023_f]
- [Automatic Joint Optimization of Algorithm-Level...][research_liu_2021_c]
- [Automatic program bug fixing by focusing on finding the...][research_yousofvand_2024]
- [Automatic Program Repair Using Large Language Models in...][research_ajiki_2026]
- [Automatic security verification of mobile app...][research_costa_2018]
- [Automatic Test Case Generation for Jasper App HDL...][research_crepalde_2025]
- [Automatic Testbench Generation for Simulation-based...][research_weissnegger_2016]
- [Automatic Verification of Data Summaries][research_rezgui_2021]
- [Automatic Verification of FSA Strategies via...][research_luo_2019]
- [Automatically exploiting the memory hierarchy of GPUs...][research_papadimitriou_2021]
- [Automatically Localizing Dynamic Code Generation Bugs in...][research_lim_2023]
- [Automatically Mitigating Vulnerabilities in Binary...][research_reiter_2025]
- [Automating code generation for a new ecosystem...][research_aytekin_2026]
- [Automating Cryptographic Code Generation][research_yarom_2022]
- [Automating reinforcement learning architecture design for...][research_wang_2022_b]
- [Automating Software Documentation with n8n and Large...][research_toprak_2026]
- [AutoPhase: Compiler Phase-Ordering for HLS with Deep...][research_huang_2019_b]
- [AV-AFL: A Vulnerability Detection Fuzzing Approach by...][research_godboley_2022]
- [Backend Bug Finder — a platform for effective compiler...][research_stepanov_2022]
- [Backward Graph Construction and Lowering in DL Compiler...][research_kwon_2022]
- [Balancing Security and Correctness in Code Generation: An...][research_black_2025]
- [Bansal and Aiken 2006][research_bansal_aiken_2006]
- [Basili and Weiss 1984][research_basili_weiss_1984]
- [Batch Me If You Can: Coverage-Guided RPKI Fuzzing at Scale][research_schulmann_2026]
- [Benchmarking Cross-Language Code Smell Detection with...][research_moldovan_2026]
- [Benchmarking WebAssembly for Embedded Systems][research_moron_2025]
- [Berger and colleagues 2002][research_berger_2002]
- [Beyond code coverage and#x2014; An approach for test...][research_tengeri_2015]
- [Beyond Coverage: Automatic Test Suite Augmentation for...][research_lu_2026]
- [Beyond Functional Correctness: An Empirical Evaluation of...][research_nogueira_2025]
- [Beyond Single Code Changes: An Empirical Study of...][research_chouchen_2026]
- [Beyond the C: Retargetable Decompilation using Neural...][research_hosseini_2022]
- [Bicriteria Distributed Submodular Maximization in a Few...][research_epasto_2017]
- [Big code != big vocabulary][research_karampatsis_2020]
- [Binary Similarity Detection Based on Intermediate...][research_li_2025_k]
- [Binary–Source Code Matching Based on Decompilation...][research_aljebreen_2025]
- [BIRD: A Binary Intermediate Representation for Formally...][research_engel_2023]
- [Birnbaum 1968][research_birnbaum_1968]
- [Blackburn and colleagues 2006][research_blackburn_2006]
- [Blackburn and colleagues 2016][research_blackburn_2016]
- [Blanchet and colleagues 2003][research_blanchet_2003]
- [Blending Shapley values for feature ranking in machine...][research_guleria_2024]
- [Blockchain-Based Software Effort Estimation: An Empirical...][research_ahmed_2022]
- [Boehm 1988][research_boehm_1988]
- [Bohm and Jacopini 1966][research_bohm_jacopini_1966]
- [Boosting Compiler Testing by Injecting Real-World Code][research_li_2024_b]
- [Boosting Compiler Testing via Compiler Optimization...][research_chen_2022]
- [Boosting component-based synthesis with control structure...][research_liu_2020]
- [BoostPolyGlot: A Structured IR Generation-Based Fuzz...][research_liu_2025_c]
- [BOSON - Application-Specific Instruction Set Processor...][research_mazurek_2020]
- [Bounded Abstract Interpretation][research_christakis_2016]
- [Brack: A Verified Compiler for Scheme via CakeML][research_lasnier_2026]
- [Branch Use in Practice: A Large-Scale Empirical Study of...][research_zou_2019]
- [Bratter: An Instruction Set Extension for Forward...][research_park_2022]
- [Braun and colleagues 2013][research_braun_2013]
- [Breaking bad? Semantic versioning and impact of breaking...][research_ochoa_2022]
- [Breaking the Vendor Lock][research_doerfert_2022]
- [BREWasm: A General Static Binary Rewriting Framework for...][research_cao_2023]
- [Bridging efficacy and efficiency: Innovations in Shapley...][research_yang_2024_c]
- [Bringing Binary Exploitation at Port 80: Understanding C...][research_massidda_2024]
- [Bringing Together Cross-ISA Checkpoint/Restoration and...][research_tamura_2025]
- [Buchbinder and colleagues 2015][research_buchbinder_2015]
- [Buddhist studies on Seokbosangjeol and tasks ahead...][research_oh_2016]
- [Bug Characteristics in Blockchain Systems: A Large-Scale...][research_wan_2017]
- [Bug characterization in machine learning-based systems][research_morovati_2023]
- [Bug numbers matter: An empirical study of effort‐aware...][research_yang_2024]
- [Bug Propagation through Code Cloning: An Empirical Study][research_mondal_2017]
- [Building a domain-specific compiler for emerging...][research_li_2023]
- [Building Intelligent Integrated Development Environment...][research_althar_2020]
- [Building SSA in a Compiler for PHP][research_biggar_2021]
- [Business-Driven Technical Debt Prioritization][research_reboucasdealme_2019]
- [Bytecode-to-C Ahead-of-Time Compilation for Android...][research_oh_2015]
- [Caffeine: CoArray Fortran Framework of Efficient...][research_rouson_2022]
- [CAGFuzz: Coverage-Guided Adversarial Generative Fuzzing...][research_zhang_2022_b]
- [Calculation of worst-case execution time for multicore...][research_mushtaq_2015]
- [Calibro: Compilation-Assisted Linking-Time Binary Code...][research_liang_2025_b]
- [Can AI Fix Buggy Code? Exploring the Use of Large...][research_zhang_2025_f]
- [Can Large Language Model Detect Plagiarism in Source Code?][research_brach_2024]
- [Can LLMs Generate Higher Quality Code Than Humans? An...][research_jamil_2025]
- [Can reactive synthesis and syntax-guided synthesis be...][research_choi_2021]
- [Can reactive synthesis and syntax-guided synthesis be...][research_choi_2022]
- [Can test cases generated by large language models...][research_zhang_2026_g]
- [Can We Classify Flaky Tests Using Only Test Code? an...][research_berndt_2026]
- [Can We Enhance Bug Report Quality Using LLMs?: An...][research_acharya_2025]
- [CAnDL: a domain specific language for compiler analysis][research_ginsbach_2018]
- [Cape: compiler-aided program transformation for HTM-based...][research_zhang_2022]
- [CARL: Compiler Assigned Reference Leasing][research_ding_2022_b]
- [CASTL: A Composable Source Code Query Language for...][research_johnson_2025]
- [Castro, Gomez and Tejada 2009][research_castro_2009]
- [CatchFuzz: Reliable active anti-fuzzing techniques...][research_kim_2024_b]
- [Causality-Aided Evaluation and Explanation of Large...][research_ji_2025]
- [CBGF: Callback Coverage Guided Fuzzing][research_hwang_2025]
- [CCEyes: An Effective Tool for Code Clone Detection on...][research_zhang_2021]
- [Certified Abstract Interpretation with Pretty-Big-Step...][research_bodin_2015]
- [Certified abstract machines for skeletal semantics][research_ambal_2022]
- [Chaitin 1982][research_chaitin_1982]
- [Challenges of Multilingual Program Specification and...][research_furia_2024]
- [Characteristics of Useful Code Reviews: An Empirical...][research_bosu_2015]
- [Characterizing and Detecting WebAssembly Runtime Bugs][research_zhang_2023_b]
- [Characterizing Dynamic Memory Behavior in WebAssembly...][research_qin_2024]
- [Characterizing logging practices in Java-based open...][research_chen_2016_b]
- [Characterizing Technical Debt in Evolving Open-source...][research_molnar_2022]
- [Chariot: Compiler-Aware Heterogeneous Graph...][research_huang_2026]
- [Checked coverage for test suite reduction][research_koitzhristov_2022]
- [Checking correctness of code generator architecture...][research_hasabnis_2015]
- [CHEHAB: Automatic Compiler Code Optimization for Fully...][research_seddiki_2026]
- [Chen and colleagues 2016][research_chen_2016]
- [CHERI Performance Enhancement for a Bytecode Interpreter][research_lowther_2023]
- [Chinese Generation and Security Index Evaluation Based on...][research_zhang_2024_c]
- [Chvatal 1979][research_chvatal_1979]
- [CirC: Compiler infrastructure for proof systems, software...][research_ozdemir_2022]
- [CIRE: LLVM Analysis for Floating-Point Rounding Error...][research_tirpankar_2025]
- [CKTI: A Domain-Specific Compiler for Lowering CUDA...][research_shi_2026]
- [CLACC: Translating OpenACC to OpenMP in Clang][research_denny_2018]
- [ClangJIT: Enhancing C++ with Just-in-Time Compilation][research_finkel_2019]
- [Class-based query-optimization for minimizing worst-case...][research_tabassam_2017]
- [Classifying Code Comments in Java Open-Source Software...][research_pascarella_2017]
- [CLIK on PLCs! Attacking Control Logic with Decompilation...][research_kalle_2019]
- [Clopper and Pearson 1934][research_clopper_pearson_1934]
- [Clustering-Based Selection for the Exploration of...][research_martins_2016]
- [Co-evolution of Infrastructure and Source Code - An...][research_jiang_2015]
- [Code coverage and test suite effectiveness: Empirical...][research_kochhar_2015]
- [Code Generation Techniques in Compiler Design: Conceptual...][research_akanbi_2022]
- [Code Ownership and Software Quality: A Replication Study][research_greiler_2015]
- [Code review effectiveness: an empirical study on selected...][research_jureczko_2020]
- [CodeJudge: Evaluating Code Generation with Large Language...][research_tong_2024]
- [Codes for machine learning and Shapley value analysis][research_he_2024]
- [CODO: An Automated Compiler for Comprehensive Dataflow...][research_zhang_2026_d]
- [Collaboration Formation and Profit Sharing Between...][research_fahimullah_2019]
- [Combining Code and Requirements Coverage with Execution...][research_marchetto_2019]
- [Combining Forward and Backward Abstract Interpretation of...][research_bakhirkin_2017]
- [Combining Large Language Models with Static Analyzers for...][research_jaoua_2025]
- [Combining loop unrolling strategies and code predication...][research_carminati_2017]
- [Combining Program Analysis and Statistical Language Model...][research_nguyen_2019]
- [Combining Static Code Analysis and Large Language Models...][research_neumuller_2026]
- [CombRewriter: Enabling Combinational Logic Simplification...][research_zheng_2026]
- [Come for syntax, stay for speed, write secure code: an...][research_zhang_2025_b]
- [Common Bug-Fix Patterns: A Large-Scale Observational Study][research_campos_2017]
- [Communications Signal Processing Using RISC-V Vector...][research_razilov_2022]
- [Compact native code generation for dynamic languages on...][research_jamieson_2021]
- [Comparative study of machine learning test case...][research_marijan_2023]
- [Comparing Mutation Testing at the Levels of Source Code...][research_hariri_2019]
- [Compatible Branch Coverage Driven Symbolic Execution for...][research_yi_2024]
- [CompCert: A Journey through the Landscape of Mechanized...][research_blazy_2023]
- [CompCertS: A Memory-Aware Verified C Compiler Using a...][research_besson_2018]
- [Compilation for Operation Execution Time Variability][research_pop_2016]
- [Compilation Optimization Methods in the Customization of...][research_wang_2024_e]
- [Compile-Time Analysis of Compiler Frameworks for Query...][research_engelke_2024]
- [Compiler and language design for quantum computing...][research_heim_2018]
- [Compiler and runtime support for continuation marks][research_flatt_2020]
- [Compiler auto-vectorization of matrix multiplication...][research_lambert_2017]
- [Compiler bug isolation via effective witness test program...][research_chen_2019]
- [Compiler Bug Isolation via Enhanced Test Program Mutation][research_liu_2024_c]
- [Compiler Module of Abstract Machine Code for Formal...][research_steingartner_2021]
- [Compiler Optimization for Quantum Computing Using...][research_quetschlich_2023]
- [Compiler optimization for scientific computation in C/C++][research_botor_2018]
- [Compiler Optimization Parameter Selection Method Based on...][research_liu_2022_c]
- [Compiler Optimization Testing Based on...][research_wu_2025_b]
- [Compiler Support for Sparse Tensor Computations in MLIR][research_bik_2022]
- [Compiler Techniques for Efficient MATLAB to OpenCL Code...][research_reis_2017]
- [Compiler Test-Program Generation via Memoized...][research_chen_2023]
- [Compiler Testing with Relaxed Memory Models][research_geeson_2024]
- [Compiler-agnostic Translation Validation][research_banerjee_2018]
- [Compiler-aided Type Tracking for Correctness Checking of...][research_huck_2018]
- [Compiler-ASR: Bridging the IR-to-Assembly Gap for...][research_zhang_2026]
- [Compiler-Assisted Instruction Fusion][research_reddy_2026]
- [Compiler-Assisted Loop Hardening Against Fault Attacks][research_proy_2017]
- [Compiler-Assisted Optimization Using Neural Code...][research_matteordonelli_2025]
- [Compiler-Assisted Selection of Hardware Acceleration...][research_zacharopoulos_2019]
- [Compiler-Based Memory Encryption for Machine Learning on...][research_maeng_2024]
- [Compiler-Directed Power Management for Superscalars][research_hajyihia_2015]
- [Compiler-Like Code Generation for fUML: Reducing Overhead...][research_hammer_2025]
- [Compiler-R1: Towards Agentic Compiler Auto-tuning with...][research_pan_2025]
- [Compiler-Runtime Co-operative Chain of Verification for...][research_kwon_2026]
- [Compiler-support for Critical Data Persistence in NVM][research_elkhouly_2019]
- [CompilerDream: Learning a Compiler World Model for...][research_deng_2025]
- [CompilerGPT: Leveraging Large Language Models for...][research_pirkelbauer_2025]
- [Compiling Linear Algebra Workloads from C to Quantum...][research_conte_2026]
- [Completeness in Static Analysis by Abstract...][research_monniaux_2023]
- [Component‐based specification, design and verification of...][research_graics_2023]
- [Comprehending Test Code: An Empirical Study][research_yu_2019]
- [Compression Optimization For Automatic Verification of...][research_wang_2021]
- [Conclusion: Debugging Blazor WebAssembly][research_himschoot_2020]
- [Configurable Loop Shuffling via Instruction Set Extensions][research_cui_2024]
- [Conforti and Cornuejols 1984][research_conforti_cornuejols_1984]
- [Continuous Debt Valuation Approach (CoDVA) for Technical...][research_stochel_2020]
- [Continuous Integration and Visual GUI Testing: Benefits...][research_alegroth_2018]
- [Convex: A RISC-V Instruction Set Extension Scheme for...][research_liu_2024]
- [Conway 1963][research_conway_1963]
- [Cooperative game amongst prefabricated building chain...][research_zhao_2023_b]
- [COpt: A High Level Domain-Specific Language to Generate...][research_venkat_2018]
- [CoreJIT: a Replication Package for Article...][research_barriere_2020]
- [Corpus Compilation and Exploitation in Language...][research_mosel_2018]
- [Correction to: A compiler framework for the reduction of...][research_falk_2019]
- [Correction to: Wait for it: identifying “On-Hold”...][research_maipradit_2021]
- [Correction: A Case Study in Formal Specification and...][research_luppen_2021_b]
- [Correctness of Isabelle's Cyclicity Checker][research_kuncar_2015]
- [Cost of Flaky Tests in Continuous Integration: An...][research_leinen_2024]
- [Cost-effective learning-based strategies for test case...][research_pradolima_2022]
- [CoStar: a verified ALL(*) parser][research_lasser_2021]
- [Could We Predict the Result of a Continuous Integration...][research_xia_2017_b]
- [Counterexample Guided Inductive Repair of Reactive...][research_hussein_2021]
- [Counterexample Guided Knowledge Compilation for Boolean...][research_akshay_2023]
- [Counterexample-guided approach to finding numerical...][research_nguyen_2017]
- [Counterexample-guided diagnosis][research_riener_2016]
- [Counterexample-Guided Inference of Modular Specifications][research_hallahan_2025]
- [Counterexample-guided simulation framework for formal...][research_patil_2015]
- [CoUpJava: A Dataset of Code Upgrade Histories in...][research_jiang_2025_b]
- [Cousot and Cousot 1977][research_cousot_1977]
- [Coverage-Guided Fuzzing for Plan-Based Robotics][research_meywerk_2023]
- [Coverage-Guided Learning-Assisted Grammar-Based Fuzzing][research_jitsunari_2019]
- [Coverage-Guided Multi-Agent Harness Generation for Java...][research_loose_2026]
- [CPerfSmith: A Randomized C Program Generator for...][research_boda_2026]
- [CPP '26 Artifact - Brack: A Verified Compiler for Scheme...][research_lasnier_2026_b]
- [Creating and Analyzing Source Code Repository Models - A...][research_scheidgen_2017]
- [Creating and Running Tests with Xamarin Test Cloud][research_versluis_2017]
- [CREF-Lang: A domain-specific language and compiler for...][research_undheim_2026]
- [Cross-Language Binary-Source Code Matching Based on Rust...][research_mao_2023]
- [CS-Shapley: Class-Wise Shapley Values for Data Valuation...][research_schoch_2022]
- [CsmithEdge: more effective compiler testing by handling...][research_evenmendoza_2022]
- [CTDip: a diversity-guided test program synthesis approach...][research_tang_2025]
- [Cuckoo search based hybrid models for improving the...][research_kumari_2018]
- [CUDA Acceleration of Worst-Case Execution Time Analysis...][research_wanxin_2022]
- [CWAMR: REIMAGINING A CAPABILITYBASED WEBASSEMBLY RUNTIME...][research_subramanyan_2025]
- [CWASI: A WebAssembly Runtime Shim for Inter-function...][research_marcelino_2023]
- [CWEval: Outcome-driven Evaluation on Functionality and...][research_peng_2025]
- [Cytron and colleagues 1991][research_cytron_1991]
- [DAME: Runtime-compilation for data movement][research_prabhu_2017]
- [dAngr: Lifting Software Debugging to a Symbolic Level][research_deruck_2025]
- [DASH: A Distributed and Parallelizable Algorithm for...][research_dey_2023]
- [Data Science and Empirical Software Engineering][research_scott_2020]
- [Data Shapley Valuation for Efficient Batch Active Learning][research_ghorbani_2022]
- [Data Valuation Method Based on Federated Learning and...][research_tan_2025_b]
- [Data valuation using Shapley value in machine learning][research_sharma_2023_c]
- [Data valuation with Leave-One-Out (LOO) test and Shapley...][research_martin_2025]
- [Data Valuation with Shapley-based Methods for Medical...][research_akcelik_2025]
- [Dataflow-based pruning for speeding up superoptimization][research_mukherjee_2020]
- [Davidson and Fraser 1984][research_davidson_fraser_1984]
- [De-Flake Your Tests : Automatically Locating Root Causes...][research_ziftci_2020]
- [Dean 1992][research_dean_1992]
- [DebtFree: minimizing labeling cost in self-admitted...][research_tu_2022_b]
- [DeCOS: Data-Efficient Reinforcement Learning for Compiler...][research_cui_2025_b]
- [Deep Neural Network Approach to Estimate Early Worst-Case...][research_kumar_2021]
- [DeepCrime: from Real Faults to Mutation Testing Tool for...][research_humbatova_2023]
- [DeepCrime: mutation testing of deep learning systems...][research_humbatova_2021]
- [DeepOrder: Deep Learning for Test Case Prioritization in...][research_sharif_2021]
- [DeepSurveySim: Simulation Software and Benchmark...][research_voetberg_2023]
- [DeepUIFuzz: A Guided Fuzzing Strategy for Testing UI...][research_chowdhury_2025]
- [Delta Debugging Type Errors with a Blackbox Compiler][research_sharrad_2018]
- [DeMillo and colleagues 1978][research_demillo_1978]
- [Demystifying the challenges and benefits of analyzing...][research_chen_2021]
- [Deployment and Integration of Machine Learning Methods...][research_wham_2024]
- [DERIVATIVE-BASED SHAPLEY VALUE FOR GLOBAL SENSITIVITY...][research_duan_2025]
- [Design and Development of Bridge AI bid Program based on...][research_zhang_2019]
- [Design and Implementation of a Compiler Supporting RISC-V...][research_zou_2023]
- [Design and Simulation Of 64-Bit Hybrid Processor...][research_ms_2018]
- [Design of an Application Specific Instruction Set...][research_xiao_2017]
- [Design of automatic aircraft parking system module...][research_kusumaningrum_2022]
- [Design of Cyanobyte: An Intermediate Representation to...][research_felker_2020]
- [Design of DMS-RRIP replacement algorithm for L1-cache of...][research_ma_2023_b]
- [Design of RISC Processor with IEEE754 Standard...][research_ozkilbac_2022]
- [Design of RLWE Cryptoprocessor Based on...][research_zhang_2018]
- [Design Space Exploration of RISC-V Vector Extension...][research_nunes_2026]
- [Design, development and testing of a 16-bit reduced...][research_jain_2023]
- [Designing quantum chemistry algorithms with just-in-time...][research_wu_2026]
- [Designing RISC-V Instruction Set Extensions for...][research_balasubramania_2024]
- [DESIL: Detecting Silent Bugs in MLIR Compiler...][research_suo_2025]
- [Detecting Compiler-Introduced Security Bugs via IR...][research_oh_2026]
- [Detecting Optimizing Compiler Bugs via History-Driven...][research_zeng_2024]
- [Detecting WebAssembly Runtime Bugs With Grammar-Guided...][research_lu_2025]
- [Determining Worst-Case Execution Time Bounds for...][research_kaestner_2025]
- [Deterministic Algorithm and Faster Algorithm for...][research_buchbinder_2024]
- [Deterministic Algorithm and Faster Algorithm for...][research_buchbinder_2025]
- [Deterministic streaming algorithms for non-monotone...][research_sun_2024]
- [DEVELOPING SITUATIONAL CONDITIONS AND PROGRAM CODES FOR...][research_atanassov_2024]
- [Development effort estimation in free/open source...][research_robles_2022]
- [Development of a Code Generation Support System in...][research_kwon_2016]
- [Development of RISC-V Based Soft-core Processor with...][research_kimura_2021]
- [dewolf: Improving Decompilation by leveraging User Surveys][research_enders_2023]
- [Differential Fuzzing Go Compilers using LLMs: A...][research_terres_2025]
- [Diffy: Data-Driven Bug Finding for Configurations][research_kakarla_2024]
- [Discretized optimization algorithms for finding the...][research_arasteh_2024]
- [DISTAL: the distributed tensor algebra compiler][research_yadav_2022]
- [Distinguishability-Guided Test Program Generation for...][research_jiang_2025]
- [Distributed Attack-Robust Submodular Maximization for...][research_zhou_2020]
- [Distributed matroid-constrained submodular maximization...][research_corah_2018_b]
- [Distributed Maximization of Submodular and Approximately...][research_ye_2020]
- [Distributed strategy selection: A submodular set function...][research_rezazadeh_2023]
- [Distributed Submodular Maximization on Partition Matroids...][research_corah_2018]
- [Distributed Submodular Maximization with Bounded...][research_castiglia_2019]
- [Distributed Submodular Maximization with Parallel...][research_sun_2020]
- [Distributed submodular maximization: trading performance...][research_rezazadeh_2022]
- [Distributionally robust optimization with...][research_jin_2026]
- [Do Automatically Generated Unit Tests Find Real Faults?...][research_shamshiri_2015]
- [Do you have space for dessert? a verified space cost...][research_gomezlondono_2020]
- [Dockerfile Changes in Practice: A Large-Scale Empirical...][research_wu_2020]
- [Does Code Review Promote Conformance? A Study of...][research_sriiesaranusor_2021]
- [Does Representation Matter? Evaluating IRs for LLM-based...][research_pelayobenedet_2026]
- [Domain specific compiler for coordinated signal...][research_li_2017]
- [Dominance-based duplication simulation (DBDS): code...][research_leopoldseder_2018]
- [DRank: A semi-automated requirements prioritization...][research_shao_2017]
- [DRUT: An Efficient Turbo Boost Solution via Load...][research_parihar_2017]
- [DU-Shapley: A Shapley Value Proxy for Efficient Dataset...][research_garridolucero_2024]
- [Ductape: Optimizing Dynamically Typed Programs Using...][research_harif_2025]
- [Dyer and colleagues 2013][research_dyer_2013]
- [Dynamic Test Case Prioritization and Selection for...][research_waseem_2025]
- [Dynamic valuation of data assets via multi-agent...][research_xie_2026]
- [eCC++ : A Compiler Construction Framework for Embedded...][research_tallada_2024]
- [Effective fault localization of automotive Simulink...][research_liu_2018]
- [Effective Performance Modeling and Domain-Specific...][research_xu_2022]
- [Effective Test Suite Optimization for Improving the...][research_karuppusamy_2020]
- [Efficient Compilation for Application Specific...][research_sohl_2015]
- [Efficient Compiler Design for a Geometric Shape...][research_gupta_2023]
- [Efficient Cross-Level Processor Verification using...][research_bruns_2022]
- [Efficient program optimization through knowledge-enhanced...][research_xu_2025]
- [Efficient Program Tracing and Monitoring Through Power...][research_moreno_2016]
- [Efficient Shapley performance attribution for...][research_bell_2024]
- [Efficient Shapley Value Driven Federated Learning System...][research_wu_2024_b]
- [Efficient Support of the Scan Vector Model for RISC-V...][research_lai_2022]
- [Efficient TinyML Inference on a Fault-Tolerant RISC-V SoC...][research_imianosky_2025]
- [Efficient Virtual Machine Allocation Technique Based on...][research_rawat_2024]
- [Efficient Worst-Case Execution Time Analysis of Dynamic...][research_puffitsch_2016]
- [Effort-optimized, accuracy-driven labelling and...][research_amini_2026]
- [Eight-Bit Vector SoftFloat Extension for the RISC-V Spike...][research_marcelli_2025]
- [Elbaum and colleagues 2002][research_elbaum_2002]
- [Empirical Application of Simulated Annealing Using...][research_rizvi_2015]
- [Empirical Assessment of Machine Learning Models for...][research_satapathy_2017]
- [Empirical evaluation of an entropy‐based approach to...][research_elkoutbi_2018]
- [Empirical evaluation of fuzzy analogy for software...][research_abnane_2017]
- [Empirical Evaluation of Mimic Software Project Data Sets...][research_gan_2020]
- [Empirical evaluation of tools for hairy requirements...][research_berry_2021]
- [EMPIRICAL INVESTIGATION OF CLOUD, GRID AND VIRTUALIZATION...][research_ilesanmi_2021]
- [Empirical Research for Self-Admitted Technical Debt...][research_yubin_2022]
- [Empirical Software Engineering Experimentation with Human...][research_sabou_2020]
- [Empirical Study about Class Change Proneness Prediction...][research_martins_2020]
- [Empirical study of correlation between mutation score and...][research_felbinger_2016]
- [Empirical Study of Restarted and Flaky Builds on Travis CI][research_durieux_2020]
- [Empirical Study of Software Test Suite Evolution][research_aljedaani_2020]
- [Empirical study on developer factors affecting tossing...][research_wu_2018]
- [Empirical Study on Real-time System Modeling and Code...][research_hu_2026_b]
- [Empirical Study on Software Bug Prediction][research_rizwan_2017]
- [Enabling Automatic Compiler-Driven Vectorization of...][research_alladi_2026]
- [Enabling Fine-Grained Incremental Builds by Making...][research_han_2024]
- [Energy-Based Model for Accurate Estimation of Shapley...][research_lu_2026_b]
- [Enhanced compiler bug isolation via memoized search][research_chen_2020_b]
- [Enhancing Compiler Design for Machine Learning Workflows...][research_ankushjitendra_2025]
- [Enhancing formal specification and verification of...][research_alrefai_2017]
- [Enhancing LLVM Optimizations for Linear Recurrence...][research_lai_2023]
- [Enhancing Python Compiler Error Messages via Stack][research_thiselton_2019]
- [Enhancing Translation Validation of Compiler...][research_wang_2024]
- [Enriching Compiler Testing with Real Program from Bug...][research_zhong_2022]
- [Enriching Source Code with Contextual Data for Code...][research_vandam_2023]
- [EnStack: An Ensemble Stacking Framework of Large Language...][research_ridoy_2024]
- [Ensuring Reliability in Self-Adaptive Systems: A...][research_basiturrahim_2025]
- [Entropy-based Framework Dealing with Error in Software...][research_elkoutbi_2017]
- [EPF: An Evolutionary, Protocol-Aware, and Coverage-Guided...][research_helmke_2021]
- [Equivalence Class Testing][research_jorgensen_2018]
- [Erratum to: Formal Description Techniques and Protocol...][research_budkowski_2017]
- [Erratum: Weighted shapley value: a cooperative game...][research_anon_2023_b]
- [Error-tolerant processors: Formal specification and...][research_golnari_2015]
- [Ertl 1999][research_ertl_1999]
- [Esary and Proschan 1963][research_esary_proschan_1963]
- [Evaluating and optimising compiler code generation for...][research_jesus_2024]
- [Evaluating classifiers in SE research: the ECSER pipeline...][research_dellanna_2022]
- [Evaluating ensemble imputation in software effort...][research_abnane_2023]
- [Evaluating Machine Learning-Based Test Case...][research_son_2025]
- [Evaluating Pred(p) and standardized accuracy criteria in...][research_idri_2017]
- [Evaluating RISC-V Vector Instruction Set Architecture...][research_li_2023_b]
- [Evaluating the agreement among technical debt measurement...][research_amanatidis_2020]
- [Evaluation and Benefit Modeling of Auto-Vectorization...][research_yao_2026]
- [Evaluation of Context-Aware Language Models and Experts...][research_alhamed_2022]
- [Evaluation of Coverage Metrics for Assessing Test Suite...][research_chippagi_2023]
- [EvoAPR: Enhancing Large Language Models for Automatic...][research_zhang_2025_g]
- [Evolving Exact Decompilation][research_schulte_2018]
- [Exact and approximate methods for proving unrealizability...][research_hu_2020_b]
- [Exact Worst-Case Execution-Time Analysis for Implicit...][research_arnstrom_2024]
- [Examining ownership models in software teams][research_koana_2024]
- [Examining the impact of bias mitigation algorithms on the...][research_demartino_2025]
- [Excluding code from test coverage: practices...][research_hora_2022]
- [Executable Semantics for the Formal Specification and...][research_qasim_2015]
- [Experience Report: Security Vulnerability Profiles of...][research_gosevapopstoja_2017]
- [Experiences Building an MLIR-Based SYCL Compiler][research_tiotto_2024]
- [Experiences from Adjusting Industrial Software for...][research_denzler_2021]
- [Explainable Test Case Prioritization in Continuous...][research_garg_2024]
- [Explaining 3D Object Detection Through Shapley...][research_kuroki_2024]
- [Exploiting Booster Pass Chain for Compiler Phase Ordering][research_chen_2025_b]
- [Exploring Compiler Optimization Opportunities for the...][research_hayashi_2016]
- [Exploring Generalizable Automated Program Repair With...][research_campos_2026]
- [Exploring Instruction Set Extension Emulation for...][research_gorius_2026]
- [Exploring Technical Debt in Security Questions on Stack...][research_edbert_2023]
- [Exploring Test Suite Diversification and Code Coverage in...][research_mondal_2015]
- [Exploring the Effectiveness of LLM based Test-driven...][research_fakhoury_2024]
- [Exploring the RISC-V Vector Extension for the Classic...][research_pircher_2021]
- [Exponentially Expanding the Phase-Ordering Search Space...][research_han_2024_b]
- [Extended firm mutation testing: A cost reduction...][research_singh_2017]
- [Extending LLVM IR for DPC++ Matrix Support: A Case Study...][research_khaldi_2021]
- [Extracting Invariants from Conditional Branches for...][research_baek_2024]
- [Extreme mutation testing in practice: An industrial case...][research_betka_2021]
- [Facilitating CoDesign with Automatic Code Similarity...][research_nguyen_2021]
- [Fair and Efficient Alternatives to Shapley-based...][research_condevaux_2023]
- [Fast and accurate power estimation for...][research_hesselbarth_2015]
- [Fast and flexible instruction selection with constraints][research_thier_2018]
- [Fast Compiler Optimization Flag Selection][research_peker_2023]
- [Fast derivation of Shapley based feature importances...][research_liu_2021_b]
- [Fast Failure Erasure Encoding Using Just in Time...][research_rohr_2017]
- [Fast Interpreter-Based Instruction Set Simulation for...][research_schlagl_2025]
- [Fast Shapley Value Approximation Through Machine Learning...][research_guckel_2025]
- [Fast Template-Based Code Generation for MLIR][research_drescher_2024]
- [Faster mutation analysis via equivalence modulo states][research_wang_2017]
- [Fault detection effectiveness of source test case...][research_saha_2018]
- [Feige 1998][research_feige_1998]
- [Fenton and Ohlsson 2000][research_fenton_ohlsson_2000]
- [Ferdinand and Wilhelm 1999][research_ferdinand_wilhelm_1999]
- [Ferrante and colleagues 1987][research_ferrante_1987]
- [FIFO Cache Analysis for WCET Estimation][research_guan_2016]
- [Finding Bugs in MLIR Compiler Infrastructure via Lowering...][research_liang_2025]
- [Finding Compiler Bugs through Cross-Language Code...][research_feng_2025]
- [Finding deep compiler bugs via guided stochastic program...][research_le_2015]
- [Finding Good Compiler Optimization Sets - A Case-based...][research_queirozjunior_2015]
- [Finding Missed Code Size Optimizations in Compilers using...][research_italiano_2025]
- [Finding missed compiler optimizations by differential...][research_barany_2018]
- [Finding Unstable Code via Compiler-Driven Differential...][research_li_2023_c]
- [Fine-Grained Coverage-Based Fuzzing][research_nongpoh_2022]
- [Finetune-Then-Merge: Democratizing Large Language Model...][research_che_2025]
- [FitM: Binary-Only Coverage-Guided Fuzzing for Stateful...][research_maier_2022]
- [Fixed-size video summarization over streaming data via...][research_lu_2021]
- [FIXME: synchronize with database! An empirical study of...][research_muse_2022]
- [Flacc: Towards OpenACC support for Fortran in the LLVM...][research_clement_2021]
- [FlakeSync: Automatically Repairing Async Flaky Tests][research_rahman_2024]
- [Flaws of Quantification Method as applied to Software...][research_mshanmuganatha_2018]
- [Flexible and Efficient Implementation of CRYSTALS-KYBER...][research_zhang_2023]
- [Flexible Runtime Reconfigurable Computing Overlay...][research_shah_2020]
- [Floating-point Semantics of Analyzed Programs][research_garoche_2019]
- [Floating-Point Usage on GitHub: A Large-Scale Study of...][research_gilot_2026]
- [Flower Pollination Algorithm for Software Effort...][research_puspaningrum_2021]
- [FlowPix: Accelerating Image Processing Pipelines on an...][research_choudhury_2023]
- [Formal Certification of Non-interferent Android Bytecode...][research_gunadi_2015]
- [Formal Semantics of Runtime Monitoring, Verification...][research_chen_2015]
- [Formal specification and verification][research_merz_2019]
- [Formal Specification and Verification of JDK’s Identity...][research_deboer_2023]
- [Formal Specification and Verification of MQTT Protocol in...][research_akhtar_2021]
- [Formal Specification and Verification of MQTT Protocol...][research_talamali_2024]
- [Formal Specification and Verification of Security...][research_zhioua_2017]
- [Formal Specification and Verification of Self-Adaptive...][research_fakhir_2018]
- [Formal Specification and Verification of Smart Contracts][research_jiao_2019]
- [Formal Specification and Verification of Smart...][research_yoon_2025]
- [Formal Specification Technique in Smart Contract...][research_lee_2019]
- [Formal verification of ABAP by Z specification][research_rodruksa_2017]
- [Formal Verification of SUBLEQ Microcode implementing the...][research_klemmer_2022_b]
- [Formal Verification Platform as a Service: WebAssembly...][research_deng_2023]
- [FormalEval: A Method for Automatic Evaluation of Code...][research_yang_2024_d]
- [FormalGym: Deep Reinforcement Learning Agent Based Formal...][research_majumder_2025]
- [Formalising Sharkovsky’s Theorem (Proof Pearl)][research_mehta_2023]
- [Formally Verified Native Code Generation in an Effectful...][research_barriere_2023]
- [Formally verified speculation and deoptimization in a JIT...][research_barriere_2021]
- [Formally Verifying Optimizations with Block Simulations][research_gourdin_2023]
- [ForMAt: Formal Verification of Scalable Multiply and...][research_weingarten_2025]
- [FOX: Coverage-guided Fuzzing as Online Stochastic Control][research_she_2024]
- [FPGA-Accelerated Neural Network Inference via a...][research_park_2025]
- [FPGA-Based ORB Accelerator: Effects of Compiler...][research_rostum_2026]
- [FPGA-based SHA-3 acceleration on a 32-bit processor via...][research_wang_2015]
- [Fractional Artificial Bee Chicken Swarm Optimization...][research_pushpa_2022]
- [FrAngel: component-based synthesis with control structures][research_shi_2019]
- [Fraser, Hanson and Proebsting 1992][research_fraser_1992]
- [FreeWavm: Enhanced WebAssembly Runtime Fuzzing Guided by...][research_qian_2025]
- [From Android Bug Reports to Android Bug Handling Process][research_yu_2016]
- [From Array Domains to Abstract Interpretation Under...][research_suzanne_2016]
- [From Bug Reports to Workarounds: The Real-World Impact of...][research_he_2025]
- [From Natural Language to Interpretable Code: Automated...][research_chen_2026]
- [From SMT to ASP: Solver-Based Approaches to Solving...][research_bembenek_2023]
- [From Source to Bytecode: How.py Becomes.pyc][research_kao_2025]
- [Full-Speed Fuzzing: Reducing Fuzzing Overhead through...][research_nagy_2019]
- [Fully Automatic Compiler Retargeting and CV-X-IF Hardware...][research_hepola_2024]
- [Fully integrating the Flang Fortran compiler with...][research_brown_2024]
- [Function/Kernel Vectorization via Loop Vectorizer][research_masten_2018]
- [Functional Representations of SSA][research_beringer_2021]
- [Functional Validation of the RISC-V Unlimited Vector...][research_fernandes_2025]
- [Furina: A Light-weight WebAssembly Runtime for ICS][research_lei_2025]
- [Fuse: A Reproducible, Extendable, Internet-Scale Corpus...][research_barik_2015]
- [Fuzzing Command-line Interface by Edge Coverage Guided...][research_lu_2024]
- [Fuzzing Deep Learning Compilers with HirGen][research_ma_2023]
- [Fuzzing guided by context-sensitive branch coverage][research_liu_2024_d]
- [Fuzzing JavaScript Interpreters with Coverage-Guided...][research_eom_2024]
- [Fuzzing JavaScript JIT compilers with a high-quality...][research_li_2025_b]
- [Fuzzing MLIR Compiler Infrastructure via Operation...][research_suo_2024]
- [Fuzzy-Graph Contrastive Test Case Prioritization...][research_kumar_2026]
- [Fuzzy_MoSCoW: A fuzzy based MoSCoW method for the...][research_ahmad_2017]
- [FWHT-RVV: A RISC-V vector processor with FWHT instruction...][research_lv_2026]
- [Generating Effective Test Suite for Multiparameter...][research_patil_2018]
- [Generating Software Architecture Description from Source...][research_hatahet_2025]
- [Genetic programming for feature model synthesis: a...][research_vescan_2021]
- [GeoAutoModuler: a knowledge–enhanced large language model...][research_liang_2026]
- [Geographic diversity in public code contributions][research_rossi_2022]
- [GeoIR-Compiler: A Geospatial Intermediate Representation...][research_zhang_2026_b]
- [Georges and colleagues 2007][research_georges_2007]
- [GHALogs: Large-Scale Dataset of GitHub Actions Runs][research_moriconi_2025]
- [git2net - Mining Time-Stamped Co-Editing Networks from...][research_gote_2019]
- [GitEvo: Code Evolution Analysis for Git Repositories][research_hora_2026_b]
- [Glanville and Graham 1978][research_glanville_graham_1978]
- [Global vs. local models for cross-project defect...][research_herbold_2016]
- [Gradual Soundness: Lessons from Static Python][research_lu_2022]
- [Grammar Filtering for Syntax-Guided Synthesis][research_morton_2020]
- [Grammar-Aware Coverage-Guided Fuzzing with Grammarinator...][research_hodovan_2026]
- [GrammLLM: Grammar-Guided LLM Test Generation for Compiler...][research_talaat_2025]
- [Graph-Based Statistical Language Model for Code][research_nguyen_2015]
- [GrayC: Greybox Fuzzing of Compilers and Analysers for C][research_evenmendoza_2023]
- [Greedily Excluding Algorithm for Submodular Maximization][research_seo_2018]
- [Greedy algorithm for maximization of semi-monotone...][research_shi_2024]
- [Greedy+Singleton: An efficient approximation algorithm...][research_tang_2024]
- [GreenSource: A Large-Scale Collection of Android Code...][research_rua_2019]
- [Grossman and colleagues 2002][research_grossman_2002]
- [Guest editorial: special issue on empirical software...][research_baldassarre_2023]
- [Gustafson 1988][research_gustafson_1988]
- [HackRep: A Large-Scale Dataset of GitHub Hackathon...][research_halmans_2026]
- [Handling Environments in a Nested Relational Algebra with...][research_auerbach_2017]
- [Hanley and Lippman-Hand 1983][research_hanley_1983]
- [Hanson 1990][research_hanson_1990]
- [Hardware implementation of a SHA-3 application-specific...][research_elmohr_2016]
- [Hardware/Software Co-Analysis for Worst Case Execution...][research_lehmann_2025]
- [Harnessing Large Language Models for Curated Code Reviews][research_sghaier_2025]
- [Harrold, Gupta and Soffa 1993][research_harrold_1993]
- [Haskell Compiler Testing Automation Based on...][research_li_2019]
- [HERTI: A Reinforcement Learning-Augmented System for...][research_han_2021]
- [Heterogeneous Ensemble Model to Optimize Software Effort...][research_ali_2023]
- [Heterogeneous Graph Data Valuation: A Shapley Value-based...][research_tang_2025_b]
- [Heterogeneous Graph Neural Networks for Software Effort...][research_phan_2022]
- [Hexcute: A Compiler Framework for Automating Layout...][research_zhang_2026_c]
- [HFuzz: Havoc Mode Guided Fuzzing][research_xie_2025]
- [HHVM JIT: a profile-guided, region-based compiler for PHP...][research_ottoni_2018]
- [High Performance Instruction-Data Level Parallelism Based...][research_israel_2024]
- [High-Performance Web Frontend Using WebAssembly][research_lyu_2023]
- [High-Precision Evaluation of Both Static and Dynamic...][research_lin_2021_b]
- [High‐coverage metamorphic testing of concurrency support...][research_windsor_2022]
- [Hikami: A Lightweight Hypervisor for Emulating RISC-V...][research_takana_2026]
- [HiPEAC compilation architecture][research_debosschere_2018]
- [History-driven Compiler Fuzzing via Assembling and...][research_fan_2024]
- [History-Guided Configuration Diversification for Compiler...][research_chen_2019_b]
- [Hodge decomposition and the Shapley value of a...][research_stern_2019]
- [Holistic evaluation of LLM-Based Code Generation][research_holl_2025]
- [How accessibility affects other quality attributes of...][research_zhao_2024_b]
- [How AI Coding Agents Modify Code: A Large-Scale Study of...][research_ogenrwot_2026]
- [How Are Discussions Associated with Bug Reworking?][research_zhao_2016]
- [How challenging it is to identify real code authors: an...][research_gong_2026]
- [How Closely are Common Mutation Operators Coupled to Real...][research_gay_2023]
- [How do Community Smells Influence Self-Admitted Technical...][research_cynthia_2025]
- [How Do Deep Learning Faults Affect AI-Enabled...][research_arrieta_2023]
- [How do open source software (OSS) developers practice and...][research_kuriakose_2015]
- [How do software development teams manage technical debt?...][research_ylihuumo_2016]
- [How does combinatorial testing perform in the real world...][research_hu_2020_c]
- [How Does Test Code Differ from Production Code in Terms...][research_horikawa_2025]
- [How effective are mutation testing tools? An empirical...][research_kintis_2017]
- [How Effective Is Coverage-Guided Fuzzing to Test Deep...][research_qin_2026]
- [How far we have come: testing decompilation correctness...][research_liu_2020_b]
- [How to Better Distinguish Security Bug Reports (Using...][research_shu_2021]
- [How to Evaluate the Productivity of Software Ecosystem: A...][research_liao_2020]
- [How to improve deep learning for software analytics][research_yedida_2022]
- [HSS cluster-based direct solver for acoustic wave equation][research_kostin_2017]
- [Hybrid Approach based on Multi‐agent System and Fuzzy...][research_yahyaoui_2022]
- [Hybrid Automated Program Repair by Combining Large...][research_li_2025_i]
- [Hybrid Equivalence/Non-Equivalence Testing][research_sarker_2025]
- [Hybrid Execution: Combining Ahead-of-Time and...][research_pichler_2023]
- [Hybrid Metaheuristic Technique for Optimization of...][research_chayan_2023]
- [Hybrid Model for Improving the Accuracy of Software...][research_silva_2026]
- [Hybrid WebAssembly-Container Orchestration in Embedded...][research_fan_2025]
- [HybridServe: Adaptive WebAssembly-Container Runtime...][research_kang_2025]
- [HyperAST: Incrementally Mining Large Source Code...][research_ledilavrec_2025]
- [Hyperchaining Optimizations for an LLVM-Based Binary...][research_lai_2021]
- [Hyperhierarchy of Semantics - A Formal Framework for...][research_mastroeni_2017]
- [Identification and prioritization of SLR search tool...][research_alzubidy_2018]
- [Identifying and Mitigating Flaky Tests in JavaScript][research_hashemi_2025]
- [Identifying Compiler and Optimization Level in Binary...][research_pizzolotto_2021]
- [Identifying Compiler and Optimization Options from Binary...][research_pizzolotto_2020]
- [Identifying Key Requirements Prioritization Criteria for...][research_pattyn_2025]
- [Identifying self-admitted technical debt in issue...][research_li_2022_d]
- [Identifying self-admitted technical debt in open source...][research_huang_2017_b]
- [Impact of Stack Overflow Code Snippets on Software...][research_ahmad_2019]
- [Impact of Static and Dynamic Coverage on Test-Case...][research_zhou_2017]
- [Implement Machine Learning to Schedule Instructions to...][research_rajendran_2025]
- [Implementation and Performance Evaluation of Omni Compiler][research_nakao_2020]
- [Implementation and Reliability Evaluation of a RISC-V...][research_imianosky_2023]
- [Implementation of Application Specific Instruction set...][research_deole_2024]
- [IMPLEMENTATION OF GENETIC ALGORITHM IN COLLEGE SCHEDULING...][research_saputra_2020]
- [Implementing an Application-Specific Instruction-Set...][research_heo_2015]
- [Improve Model Testing by Integrating Bounded Model...][research_yang_2023]
- [Improved Ahead-of-time Compilation of Stack-based JVM...][research_reijers_2019]
- [Improved Assistance for Interactive Proof (Keynote)][research_kaliszyk_2023]
- [Improved Circuit Compilation for Hybrid MPC via Compiler...][research_demmler_2021]
- [Improved Prediction of Total Energy Consumption and...][research_pokharel_2021]
- [Improving Code Completion by Solving Data Inconsistencies...][research_yang_2023_c]
- [Improving Estimation Accuracy Prediction of Software...][research_mahmood_2020]
- [Improving Software Requirements Prioritization through...][research_winton_2023]
- [Improving the accuracy and stability of privacy-aware...][research_tang_2026_b]
- [Improving the Accuracy of Batik Classification using Deep...][research_dzulqarnain_2024]
- [Inductor-TV: Formal Methods for the Pytorch Compiler][research_majumder_2026]
- [Industrial adoption of machine learning techniques for...][research_laiq_2024]
- [Industrial Application of Deep Learning based Fault...][research_yang_2026_b]
- [Industrial Scale Passive Testing with T-EARS][research_flemstrom_2021]
- [Inferring test models from user bug reports using...][research_guizzo_2023]
- [Inozemtseva and Holmes 2014][research_inozemtseva_holmes_2014]
- [Input perturbation robustness for software effort...][research_phannachitta_2026]
- [INR-Arch: A Dataflow Architecture and Compiler for...][research_abikaram_2023]
- [Inside Bug Report Templates: An Empirical Study on Bug...][research_zhang_2024]
- [INSTRIM: Lightweight Instrumentation for Coverage-guided...][research_hsu_2018]
- [Instruction Code Selection][research_ebner_2021]
- [Instruction set extension and hardware acceleration for...][research_pang_2017]
- [Instruction Set Optimization for FM-Type Digital Signal...][research_ayeoribe_2026]
- [InstructRepair: Instruct Large Language Models With Rich...][research_fu_2025]
- [Integrating a functional pattern-based IR into MLIR][research_lucke_2021]
- [Integrating Large Language Models in Software Engineering...][research_khan_2026]
- [Integrating Shapley Value and Least Core Attribution for...][research_wang_2025_b]
- [Integrating Staleness and Shapley Value Consistency for...][research_jiang_2023]
- [Integrating Tests into Your Builds][research_versluis_2017_b]
- [Integration of a Real-Time CCSDS 410.0-B-32...][research_kuo_2023]
- [Integration of Static Worst-Case Execution Time and Stack...][research_hausladen_2017]
- [Intelligent Power Grid Startup Scheme Based on Rule...][research_wu_2025_c]
- [Intelligent Test Case Prioritization: A Review of Machine...][research_razi_2025]
- [Interactive Programming for Microcontrollers by...][research_mochizuki_2024]
- [Interleaving Large Language Models for Compiler Testing][research_ni_2025]
- [Intermediate Representations][research_cooper_2023]
- [Intermediate-Code Generation][research_mogensen_2017]
- [Intermediate-Code Generation][research_mogensen_2024]
- [Interruptibility of software developers and its...][research_poreba_2026]
- [IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for...][research_cui_2025]
- [Intrinsic Compilation Model to enhance Performance of...][research_aradhya_2018]
- [Introducing H, an Institution-Based Formal Specification...][research_diaconescu_2020]
- [Introducing multi-level parallelism, at coarse, fine and...][research_gratien_2020]
- [Introduction to Optimization][research_cooper_2023_b]
- [Investigating Coverage Guided Fuzzing with Mutation...][research_qian_2022]
- [Investigating the Role of Formal Verification in Software...][research_masoudi_2025]
- [Investigations about replication of empirical studies in...][research_demagalhaes_2015]
- [Ioannidis 2005][research_ioannidis_2005]
- [Is code coverage of performance tests related to source...][research_imran_2025]
- [Is dynamic compilation possible for embedded systems?][research_charles_2015]
- [Is this build failure related to my patch? An empirical...][research_huang_2026_b]
- [Is Your Code Generated by ChatGPT Really Correct?...][research_liu_2023_b]
- [ISA customization for application specific instruction...][research_singh_2015]
- [Java Source Code Vulnerability Detection Using Large...][research_anbiya_2025]
- [Javascript ahead-of-time compilation for embedded web...][research_park_2015]
- [JavaScript Parallelizing Compiler for Exploiting...][research_na_2016]
- [Jensen 1906][research_jensen_1906]
- [Jia and Harman 2011][research_jia_harman_2011]
- [JIT Compiler Security through Low-Cost RISC-V Extension][research_ducasse_2023]
- [JIT Leaks: Inducing Timing Side Channels through...][research_brennan_2020]
- [JITfuzz: Coverage-guided Fuzzing for JVM Just-in-Time...][research_wu_2023]
- [Johnson 1974][research_johnson_1974]
- [Jovanovic and Levy 1997][research_jovanovic_levy_1997]
- [Just and colleagues 2014][research_just_2014]
- [Just-in-Time Compilation and Link-Time Optimization for...][research_tian_2022]
- [Just-In-Time Compilation for Verilog][research_schkufza_2019]
- [Just-In-Time Compilation on ARM—A Closer Look at...][research_hartley_2022]
- [Just-In-Time Compiler System in Aspect-Oriented...][research_ishimura_2022]
- [Just-In-Time GPU Compilation for Interpreted Languages...][research_fumero_2017]
- [Just-in-time scheduling in identical parallel machine...][research_goli_2022]
- [k-Submodular Maximization Under Individual Knapsack...][research_tran_2025]
- [Kang and colleagues 2018][research_kang_2018]
- [Karlsson and Ryan 1997][research_karlsson_ryan_1997]
- [Karp 1972][research_karp_1972]
- [KART – A Runtime Compilation Library for Improving HPC...][research_noack_2017]
- [Key Operator Vectorization for LeNet and ResNet Based on...][research_chen_2025]
- [Keynote talk I: Syntax-guided synthesis][research_alur_2015]
- [Khuller and colleagues 1999][research_khuller_1999]
- [Kildall 1973][research_kildall_1973]
- [Knowledge Graph Based Repository-Level Code Generation][research_athale_2025]
- [Knuth 1971][research_knuth_1971]
- [Kumar and colleagues 2014][research_kumar_2014]
- [LAGrad: Statically Optimized Differentiable Programming...][research_peng_2023]
- [Landi 1992][research_landi_1992]
- [Language models can prioritize patches for practical...][research_kang_2022]
- [Language usage analysis for EMF metamodels on GitHub][research_babur_2023]
- [LAPSE: Automatic, Formal Fault-Tolerant Correctness...][research_averill_2026]
- [Large Language Model Generation Safety: A Comprehensive...][research_zhang_2025_h]
- [Large Language Model-Based Interactive Code Generation...][research_hamasaki_2026]
- [Large Language Models for Automated Program Repair][research_ribeiro_2023]
- [Large Language Models for Binary Decompilation...][research_wang_2026_b]
- [Large Language Models for Code Obfuscation Evaluation of...][research_kochberger_2023]
- [Large Language Models for Code Translation: An In-Depth...][research_feischl_2026]
- [Large Language Models for Computer Programming Education...][research_zhu_2025_b]
- [Large Language Models in Automated Repair of Haskell Type...][research_santos_2024_c]
- [Large Language Models Meet Automated Program Repair...][research_tang_2024_b]
- [Large-Scale Analysis of GitHub and CVEs to Determine...][research_dennis_2024]
- [Large-scale analysis of the co-commit patterns of the...][research_cohen_2018]
- [Large-Scale Manual Validation of Bugfixing Changes][research_herbold_2020]
- [Lattner and Adve 2004][research_lattner_adve_2004]
- [LAYANAN CLOUD COMPUTING BERBASIS INFRASTRUCTURE AS A...][research_wintolo_2015]
- [Lazy Code Transformations in a Formally Verified Compiler][research_gourdin_2023_b]
- [Le and colleagues 2014][research_le_2014]
- [Learning-based prioritization of test cases in continuous...][research_lima_2020]
- [LegoFuzz: Interleaving Large Language Models for Compiler...][research_ni_2025_b]
- [Leroy 2003][research_leroy_2003]
- [Leroy 2009][research_leroy_2009]
- [Lessons Learnt on Reproducibility in Machine Learning...][research_daoudi_2021]
- [Leveraging Compilation Statistics for Compiler Phase...][research_zhao_2025_b]
- [Leveraging Compiler Intermediate Representation for...][research_garzella_2020]
- [Leveraging explainable AI for requirements prioritization...][research_alhumam_2026]
- [Leveraging LLVM OpenMP GPU Offload Optimizations for...][research_gayatri_2024]
- [Leveraging Rough Sets for Enhanced Test Case...][research_gaceanu_2024]
- [Li and Malik 1995][research_li_malik_1995]
- [License Usage and Changes: A Large-Scale Study of Java...][research_vendome_2015_b]
- [License usage and changes: a large-scale study on gitHub][research_vendome_2016]
- [LifeJacket: verifying precise floating-point...][research_notzli_2016]
- [Lifting Assembly to Intermediate Representation][research_hasabnis_2016]
- [Lifting Code Generation of Cardiac Physiology Simulation...][research_thangamani_2023_b]
- [Lifting proof-relevant unification to higher dimensions][research_cockx_2017]
- [Light Shapley: Improving the Scalability of Equitable...][research_li_2026_b]
- [Lightweight Cryptographic Instruction Set Extension on...][research_eisenkraemer_2020]
- [Liu and Layland 1973][research_liu_layland_1973]
- [LLHD: a multi-level intermediate representation for...][research_schuiki_2020]
- [LLM Compiler: Foundation Language Models for Compiler...][research_cummins_2025]
- [LLM-assisted end-to-end binary decompilation: a...][research_alruqaishi_2026]
- [LLM-based Control Code Generation using Image Recognition][research_koziolek_2024]
- [LLM-VeriOpt: Verification-Guided Reinforcement Learning...][research_fang_2026]
- [LLVM and the Automatic Vectorization of Loops Invoking...][research_petrogalli_2018]
- [LLVM Library for a Dedicated Processor Instruction Set –...][research_zubert_2024]
- [LLVM parallel intermediate representation][research_khaldi_2015]
- [LLVM-based communication optimizations for PGAS programs][research_hayashi_2015]
- [LMFuzz: Program repair fuzzing based on large language...][research_lin_2025]
- [Load Balancing in Decoupled Look-ahead: A Do-It-Yourself...][research_parihar_2015]
- [Localized Data Shapley: Accelerating Valuation for...][research_zhang_2025_c]
- [Locating faults with program slicing: an empirical...][research_soremekun_2021]
- [LocSeq: Automated Localization for Compiler Optimization...][research_zhou_2022]
- [Logic Gate Network Inference Acceleration with RISC-V...][research_wang_2025]
- [Logic Synthesis with Design Compiler][research_chin_2022]
- [Long-Term Evaluation of Technical Debt in Open-Source...][research_molnar_2020]
- [Look for the Proof to Find the Program...][research_gascon_2017]
- [Looking for Peace of Mind? Manage Your (Technical) Debt...][research_ghanbari_2017]
- [Lopes and colleagues 2021][research_lopes_2021]
- [Lost In Translation: Exposing Hidden Compiler...][research_georgiou_2020]
- [Lovasz 1983][research_lovasz_1983]
- [Low Level Source Code Vulnerability Detection Using...][research_alqarni_2022]
- [Low-Power Implementation of DSP Instruction Set Extension...][research_li_2025]
- [Lowering Barriers to Application Development With...][research_perezalvarez_2022]
- [LTSV: Layered Type-Constrained Shapley Value for...][research_tang_2026_c]
- [Lumos: Performance Characterization of WebAssembly as a...][research_marcelino_2025]
- [Lund and Yannakakis 1994][research_lund_yannakakis_1994]
- [Lutsig: a verified Verilog compiler for verified circuit...][research_loow_2021]
- [Machine Learning Approaches for Authorship Attribution...][research_frankel_2021]
- [Machine Learning Based Compiler Optimization Technique][research_iqbal_2024]
- [Machine Learning for Data Center Optimizations: Feature...][research_gebreyesus_2023]
- [Machine Learning for Test Case Prioritization in...][research_kumar_2024_b]
- [Machine Learning in Compiler Optimization][research_wang_2018_c]
- [Machine learning models with distinct Shapley value...][research_roth_2024]
- [Machine Learning Regression Techniques for Test Case...][research_daroza_2022]
- [Machine learning-based modelling, feature importance and...][research_karathanasopou_2024]
- [Machine Learning-based Test Case Prioritization using...][research_khan_2024]
- [Machine Learning-Driven GCC Loop Unrolling Optimization...][research_shi_2024_b]
- [Machine-checked Verification of Cognitive Agents][research_jensen_2022]
- [Machine-Checked Verification of the Correctness and...][research_chargueraud_2015]
- [Machine-checked ZKP for NP relations: Formally Verified...][research_almeida_2021]
- [Machine-Code Generation][research_mogensen_2017_b]
- [Machine-Code Generation][research_mogensen_2024_b]
- [Making Time Observable: Compiler Correctness for...][research_lion_2026]
- [MALintent: Coverage Guided Intent Fuzzing Framework for...][research_askar_2025]
- [Many-core compiler fuzzing][research_lidbury_2015]
- [MarQSim: Reconciling Determinism and Randomness in...][research_cao_2025]
- [Massalin 1987][research_massalin_1987]
- [Matlab to C Compilation Targeting Application Specific...][research_latifis_2016]
- [MCBRank Method to Improve Software Requirements...][research_ahmad_2022]
- [Measuring affective states from technical debt][research_olsson_2021]
- [Mechanising a Type-Safe Model of Multithreaded Java with...][research_lochbihler_2018]
- [Mechanizing conventional SSA for a verified destruction...][research_demange_2016]
- [Meehl 1967][research_meehl_1967]
- [Memory Simulations, Security and Optimization in a...][research_monniaux_2024]
- [Memory Utilization and Machine Learning Techniques for...][research_shreyasmadhav_2021]
- [Meta-analysis for families of experiments in software...][research_kitchenham_2019]
- [Metacasanova: an optimized meta-compiler for...][research_digiacomo_2017]
- [Metamodeling and Code Generation in the Hardware/Software...][research_ecker_2017]
- [Metamorphic Relation Patterns for Metamorphic Testing...][research_ying_2025]
- [Metamorphic testing for (graphics) compilers][research_donaldson_2016]
- [Metamorphic Testing for Adobe Data Analytics Software][research_jarman_2017]
- [Metamorphic testing in bioinformatics software][research_stacy_2022]
- [Metamorphic Testing on the Continuum of Verification and...][research_raunak_2021]
- [Microarchitecture Design and Benchmarking of Custom SHA-3...][research_bolat_2025]
- [Mining performance regression inducing code changes in...][research_luo_2016]
- [Mining the modern code review repositories][research_yang_2016]
- [Mining the usage of reactive programming APIs][research_zimmerle_2022]
- [Mitigating omitted variable bias in empirical software...][research_furia_2026]
- [MLIR-based code generation for GPU tensor cores][research_katel_2022]
- [MLIR-Based Homomorphic Encryption Compiler for GPU][research_nozaki_2024]
- [MLIR-to-CGRA: A Versatile MLIR-Based Compiler Framework...][research_yu_2024_b]
- [MLIR: A Panacea for ML Compiler Challenges?][research_agrawal_2025]
- [MLIR: Scaling Compiler Infrastructure for Domain Specific...][research_lattner_2021]
- [MLIRSmith: Random Program Generation for Fuzzing MLIR...][research_wang_2023_b]
- [Model vs system level testing of autonomous driving...][research_stocco_2023]
- [Model-Agnostic Empirical Evaluation of Test-Driven Prompt...][research_rizqullah_2026]
- [Model-Driven Quantum Code Generation Using Large Language...][research_siavash_2025]
- [Modeling and implementation of Common LISP functional...][research_chaplygin_2025]
- [Modeling Sampling Workflows for Code Repositories][research_lefeuvre_2026]
- [Modeling Undefined Behaviour Semantics for Checking...][research_dahiya_2017]
- [ModelPlex: verified runtime validation of verified...][research_mitsch_2016]
- [Modular Component-Based Quantum Circuit Synthesis][research_kang_2023]
- [Modular SDN Compiler Design with Intermediate...][research_li_2016]
- [Modular specification and verification of a...][research_mcmillan_2016]
- [Modular translation validation of a full-sized...][research_ngo_2015]
- [Moura and Ierusalimschy 2009][research_moura_ierusalimschy_2009]
- [MRU Cache Analysis for WCET Estimation][research_guan_2016_b]
- [Much more than a prediction: Expert-based software effort...][research_matsubara_2023]
- [Multi-Armed Bandit Test Case Prioritization in Continuous...][research_lima_2020_b]
- [Multi-faceted Code Smell Detection at Scale using...][research_sharma_2024]
- [Multi-level physical hierarchy floorplanning using IC...][research_roze_2017]
- [Multi-modal program inference: a marriage of pre-trained...][research_rahmani_2021]
- [Multi-Pass Streaming Algorithms for Monotone Submodular...][research_huang_2021]
- [Multi-target Compiler for the Deployment of Machine...][research_castrolopez_2019]
- [Multipass Streaming Algorithms for Regularized Submodular...][research_gong_2024]
- [Munafo and colleagues 2017][research_munafo_2017]
- [Mutation analysis and its industrial applications][research_gopinath_2022]
- [Mutation Operators for Mutation Testing of Angular Web...][research_augustin_2025]
- [Mutation Testing for Industrial Robotic Systems][research_goncalvesdossa_2025]
- [Mutation Testing in Continuous Integration: An...][research_orgard_2023]
- [Mutation testing in practice using Ruby][research_li_2015]
- [Mutation Testing of Deep Reinforcement Learning Based on...][research_tambon_2023]
- [Mutation Testing of Programs for Industrial Robots][research_ashraf_2025]
- [muttest: Mutation Testing][research_sobolewski_2025]
- [Mytkowicz and colleagues 2009][research_mytkowicz_2009]
- [Naturalness in Source Code Summarization. How Significant...][research_ferretti_2023]
- [Naturalness of Attention: Revisiting Attention in Code...][research_saad_2024]
- [Navigating the SIMD Optimization Maze: A Reinforcement...][research_pan_2025_b]
- [Necula 1997][research_necula_1997]
- [Necula and Lee 1998][research_necula_lee_1998]
- [Negative results for software effort estimation][research_menzies_2016]
- [Negativity in self-admitted technical debt: how sentiment...][research_cassee_2025]
- [NemesisGuard: Mitigating interrupt latency side channel...][research_salehi_2022]
- [Nemhauser and Wolsey 1978][research_nemhauser_wolsey_1978b]
- [Nemhauser, Wolsey and Fisher 1978][research_nemhauser_1978]
- [Neural Network-Based Test Case Prioritization in...][research_vescan_2023]
- [Neural Networks based Software Development Effort...][research_boujida_2021]
- [Neural-MCTS Test Prioritization for Smart Contract...][research_barboni_2026]
- [Neuroevolutionary Compiler Control for Code Optimization][research_heckel_2023]
- [Nonio — modular automatic compiler phase selection and...][research_nobre_2019]
- [Nonlinear Reinforcement Learning-Based Dynamic Test Case...][research_srinivasaraoko_2024]
- [NOProbe: A NOP-Based Dynamic Binary Instrumentation...][research_bushehri_2026]
- [Not all bug reopens are negative: A case study on eclipse...][research_mi_2018]
- [Novice comprehension of Object-Oriented OO programs: An...][research_alardawi_2015]
- [Object Intersection Captures on Interactive Apps to Drive...][research_mpeis_2022]
- [Of Ahead Time: Evaluating Disassembly of Android Apps...][research_bleier_2023]
- [Offline and Online Distributed Submodular Maximization...][research_ye_2025]
- [On a Machine-Checked Proof for Fraction Arithmetic over a...][research_meshveliani_2020]
- [On distributed submodular maximization with limited...][research_gharesifard_2016]
- [On factors that impact the relationship between code...][research_barani_2023]
- [On JavaScript Ahead-of-Time Compilation Performance...][research_serrano_2022]
- [On the Benefits and Barriers When Adopting Software...][research_vetro_2015]
- [On the Criticality of Probabilistic Worst-Case Execution...][research_santinelli_2017]
- [On the documentation of self-admitted technical debt in...][research_xavier_2022]
- [On the Evaluation of Effort Estimation Models][research_lavazza_2017]
- [On the Interactions Between Value Prediction and Compiler...][research_endo_2017]
- [On the relationship between bug reports and queries for...][research_mills_2020]
- [On the Runtime and Energy Performance of WebAssembly: Is...][research_demacedo_2021]
- [On the use of contextual information for machine learning...][research_roza_2024]
- [On the use of static branch prediction to reduce the...][research_carminati_2018]
- [On the value of a prioritization scheme for resolving...][research_mensah_2018]
- [One-pass streaming algorithm for DR-submodular...][research_tan_2022]
- [One‐pass streaming algorithm for monotone lattice...][research_zhang_2021_c]
- [Online and Streaming Algorithms for Constrained...][research_spaeh_2025]
- [Oolong: A Baseband processor extension to the RISC-V ISA][research_melo_2016]
- [OP2-Clang: A Source-to-Source Translator Using Clang/LLVM...][research_balogh_2018]
- [Open Source Software (OSS) for Big Data][research_segall_2020]
- [Open-Source Memory Compiler for Automatic RRAM Generation...][research_antoniadis_2021]
- [Open-Source MLIR-Based Intermediate Representation for...][research_kamkin_2024]
- [OpenASIP 2.0: Co-Design Toolset for RISC-V...][research_hepola_2022]
- [OpenMP GPU Offload in Flang and LLVM][research_ozen_2018]
- [Operationalizing validity of empirical software...][research_hartel_2023]
- [Operator-data type pair based execution environments...][research_seo_2016]
- [Opportunities and security risks of technical leverage: A...][research_samaana_2025]
- [Optimasi Pemanfaatan Air Menggunakan Program Solver di...][research_supriyatna_2025]
- [Optimising Bcrypt Parameters: Finding the Optimal Number...][research_listiawan_2024]
- [Optimization of production planning using integer linear...][research_astuti_2023]
- [Optimization of Specific Instruction Set Processor for...][research_lei_2018]
- [Optimization, Machine Learning, and Fuzzy Logic][research_kingslystephen_2025]
- [Optimization-Aware Compiler-Level Event Profiling][research_basso_2023]
- [Optimization-Directed Compiler Fuzzing for Continuous...][research_kwon_2025]
- [Optimizing Shapley Value for Client Valuation in...][research_arbaoui_2024]
- [Optimizing Software Effort Estimation Accuracy with a...][research_raghuraman_2024]
- [Optimizing Task Allocation in IT Project Management Using...][research_garmsirinejad_2025]
- [Optimizing Tensor Computations: From Applications to...][research_boehm_2023]
- [Optimizing test case prioritization using machine...][research_sharma_2023_b]
- [Optimizing Test Case Prioritization With Meta Deep...][research_alrakban_2025]
- [Optimizing TinyEngine for the RISC-V Vector Extension][research_tan_2025]
- [ORMorpher: An Interactive Framework for ORM Translation...][research_abraham_2025]
- [OSS License Identification at Scale: A Comprehensive...][research_jahanshahi_2025]
- [OSSGameBench: A Large-Scale Dataset of Development...][research_marsad_2026]
- [Ostrand and Weyuker 2002][research_ostrand_weyuker_2002]
- [Ostrand, Weyuker and Bell 2005][research_ostrand_weyuker_2005]
- [OurRank: A Software Requirements Prioritization Method...][research_rojas_2022]
- [Outer-Loop Auto-Vectorization for SIMD Architectures...][research_dong_2016]
- [Owen 1972][research_owen_1972]
- [P30 - Möbius-Shapley: Native Feature Attribution for...][research_dhahbi_2026]
- [P4IRS: An intermediate representation and compiler for...][research_raveduttilucio_2025]
- [Paddle-Mlir: A Compiler Based on MLIR for Accelerating...][research_huang_2024]
- [Parallel mutation testing for large scale systems][research_canizares_2023]
- [Parallelizing Compiler Translation Validation Using...][research_han_2021_b]
- [PARCOACH Extension for Static MPI Nonblocking and...][research_nguyen_2020]
- [Partitioning Composite Code Changes to Facilitate Code...][research_tao_2015]
- [Passenger Queue Simulation Analysis and Optimization at...][research_putra_2024]
- [Patterns of Code-to-Test Co-evolution for Automated Test...][research_shimmi_2022]
- [PEMBANGUNAN COMPILER DOMAIN SPECIFIC LANGUAGE SEBAGAI...][research_adiyoso_2023]
- [PENERAPAN EIGENFACE UNTUK COMPUTER BASED TEST (CBT)...][research_sajati_2017]
- [PENERAPAN PEMROSESAN PARALEL UNTUK MENGUJI WAKTU...][research_ngadiyono_2015]
- [PERANCANGAN PENGAMANAN SERVER SECARA OTOMATIS MENGGUNAKAN...][research_kusumaningrum_2015]
- [Performance and Usability Implications of Multiplatform...][research_kakati_2025]
- [Performance Evaluation of CNN using RISC-V Vector...][research_okawara_2025]
- [PERFORMANCE EVALUATION OF THE UETRV-PCORE USING RISC-V...][research_zia_2026]
- [Performance Improvement of Kotlin Program in...][research_sonoyama_2020]
- [Performance, Correctness, Exceptions: Pick Three][research_gussoni_2019]
- [Performant Binary Fuzzing without Source Code using...][research_pauley_2022]
- [PfComp: A Verified Compiler for Packet Filtering...][research_chavanon_2024]
- [PHPIL: Fuzzing the PHP Interpreter with Custom Bytecode][research_rao_2020]
- [Pilsner: a compositionally verified compiler for a...][research_neis_2015]
- [PIMFlow: Compiler and Runtime Support for CNN Models on...][research_shin_2023]
- [Pnueli and colleagues 1998][research_pnueli_1998]
- [Polyhedral Compiler Technology in Collaboration with...][research_hall_2017]
- [PolyMorphous: An MLIR-Based Polyhedral Compiler with Loop...][research_zhao_2025]
- [Poster Abstract: Towards Shapley Value based Security...][research_marbukh_2022]
- [Poster: BugOss: A Regression Bug Benchmark for Empirical...][research_kim_2023]
- [POSTER: Runtime Adaptations for Energy-Efficient VSLAM][research_khalufa_2019]
- [POSTER: Tango: An Optimizing Compiler for Just-In-Time...][research_tine_2019]
- [Potential of WebAssembly for Embedded Systems][research_wallentowitz_2022]
- [POWER: Program Option-Aware Fuzzer for High Bug Detection...][research_lee_2022]
- [Practical Examples of Timing Problems][research_gliwa_2021]
- [Practical Python FPGA Acceleration with Fast Just-In-Time...][research_dickerson_2026]
- [PredComp: Predicting Compiler Optimization Options with...][research_gao_2026]
- [Predicting Design Impactful Changes in Modern Code...][research_uchoa_2021]
- [Predicting Worst-Case Execution Time Trends in Long-Lived...][research_dai_2017]
- [Prediction accuracy measurements as a fitness function...][research_urbanek_2015]
- [Prediction of relatedness in stack overflow: deep...][research_xu_2018]
- [Preempting flaky tests via non-idempotent-outcome tests][research_wei_2022]
- [Preprocessing and Compilation][research_uzayr_2022]
- [Preventing duplicate bug reports by continuously querying...][research_hindle_2018]
- [Prioritizing solution-oriented software requirements...][research_ibriwesh_2018]
- [PriorTD: A Method for Prioritization Technical Debt][research_detofeno_2022]
- [Privacy-Preserving Feature Valuation in Vertical...][research_laskurain_2025]
- [Profile Guided Optimization Transfer-Learning for...][research_he_2023]
- [Profiling Developers Through the Lens of Technical Debt][research_codabux_2020]
- [Program comprehension of domain-specific and...][research_kosar_2018]
- [Program Reconditioning: Avoiding Undefined Behaviour When...][research_lecoeur_2023]
- [Programming Assessment in E-Learning through Rule-Based...][research_saputro_2025]
- [Programming GPUs with C++14 and Just-In-Time Compilation][research_haidlmichael_2016]
- [Programming Large Language Models][research_calamo_2025]
- [Project productivity evaluation in early software effort...][research_azzeh_2018]
- [PromptTone: A Dataset for Evaluating Large Language Model...][research_andruccioli_2026]
- [Proof pearl: Braun trees][research_nipkow_2020]
- [Propagating Large Language Models Programming Feedback][research_koutcheme_2024]
- [Proposal of Scalable Vector Extension for Embedded RISC-V...][research_kimura_2019]
- [Protean Compiler: An Agile Framework to Drive Fine-grain...][research_ashouri_2026]
- [Proteus: Portable Runtime Optimization of GPU Kernel...][research_georgakoudis_2025]
- [Prototype implementation of the OpenGL ES 2.0 shading...][research_baek_2017]
- [Proving the Coding Interview: A Benchmark for Formally...][research_dougherty_2025]
- [PRPA REPERCUSSIONS and IMPLICATIONS FOR REAL WORLD STUDY...][research_anon_2017]
- [PSO based optimization of worst-case execution time for...][research_venkanna_2018]
- [PureCake: A Verified Compiler for a Lazy Functional...][research_kanabar_2023]
- [Puschner and Burns 2000][research_puschner_burns_2000]
- [QEMI: A Quantum Software Stacks Testing Framework via...][research_luo_2026]
- [QJWasm: A lightweight runtime system for efficient...][research_hu_2026]
- [QScored: A Large Dataset of Code Smells and Quality...][research_sharma_2021]
- [Quality assurance of bioinformatics software][research_srinivasan_2018]
- [Quality Questions Need Quality Code: Classifying Code...][research_duijn_2015]
- [Quantifying and characterizing clones of self-admitted...][research_xiao_2024]
- [Quantum Circuit Synthesis from C via Multi-Level...][research_lancellotti_2026]
- [Quantum Oracle Synthesis from HDL Designs via Multi Level...][research_lancellotti_2026_b]
- [Quantum simulation with just-in-time compilation][research_efthymiou_2022]
- [Query by example in large-scale code repositories][research_balachandran_2015]
- [Querying Big Source Code][research_garciaalvarado_2020]
- [Rainfuzz: Reinforcement-Learning Driven Heat-Maps for...][research_binosi_2023]
- [Random testing of C compilers based on test program...][research_nakamura_2016]
- [Randomized Composable Core-sets for Distributed...][research_mirrokni_2015]
- [Ranking Relevant Tests for Order-Dependent Flaky Tests][research_rahman_2025]
- [Ray and colleagues 2014][research_ray_2014]
- [RE-APR: Reasoning-Enhanced Automated Program Repair via...][research_du_2026]
- [Real world projects, real faults: evaluating spectrum...][research_widyasari_2022]
- [Realistic assessment of software effort estimation models][research_sigweni_2016]
- [Really Embedding Domain-Specific Languages into C++][research_finkel_2020]
- [ReAPR: Automatic program repair via retrieval-augmented...][research_liu_2025_d]
- [Rechecking Recheck Requests in Continuous Integration: An...][research_brus_2025]
- [Reconciling high-level optimizations and low-level code...][research_lee_2018]
- [Redefining prioritization][research_liang_2018]
- [Reducing labeling effort in architecture technical debt...][research_sutoyo_2026]
- [Reducing the Compilation Time of Quantum Circuits Using...][research_quetschlich_2023_b]
- [Reduction of Workflow Nets for Generalised Soundness...][research_bride_2017]
- [Reductive Analysis with Compiler-Guided Large Language...][research_wang_2025_d]
- [Redundancy Elimination][research_chow_2021]
- [Refactorings and Technical Debt in Docker Projects: An...][research_ksontini_2021]
- [Refinement of Parallel Algorithms Down to LLVM: Applied...][research_lammich_2024]
- [Reflections on the Empirical Software Engineering journal][research_basili_2021]
- [ReFuzz: A Remedy for Saturation in Coverage-Guided Fuzzing][research_lyu_2021]
- [Regehr and colleagues 2005][research_regehr_2005]
- [Regression Test Suites Optimization for...][research_zachariaova_2016]
- [Regularized two-stage submodular maximization under...][research_yang_2022_b]
- [Reimagining Studies’ Replication: A Validity-Driven...][research_azevedo_2025]
- [Reineke and colleagues 2007][research_reineke_2007]
- [Reinforcement Learning and Data-Generation for...][research_parsert_2024]
- [Reinforcement learning for automatic test case...][research_spieker_2017]
- [Reinforcement learning for online testing of autonomous...][research_giamattei_2024]
- [Reinforcement Learning Reward Function for Test Case...][research_mirzaei_2022]
- [Reinforcement Learning Strategies for Compiler...][research_shahzad_2022]
- [Reinforcement-Learning-Based Test Program Generation for...][research_chen_2019_c]
- [Relating Code Coverage, Mutation Score and Test Suite...][research_tengeri_2016]
- [Relational Solver for Java Generics Type System][research_lozov_2023]
- [Relaxed Peephole Optimization: A Novel Compiler...][research_liu_2021]
- [Release synchronization in software ecosystems][research_foundjem_2021]
- [Reliability Test based on a Binomial Experiment for...][research_arcaro_2020]
- [Reliable Compilation Optimization Phase-ordering...][research_wu_2020_b]
- [Remgen: Remanufacturing a Random Program Generator for...][research_tu_2022]
- [Remote Just-in-Time Compilation for Dynamic Languages][research_pecimuth_2023]
- [RepairBench: Leaderboard of Frontier Models for Program...][research_silva_2025]
- [Replacing conjectures by positive knowledge: Inferring...][research_knoop_2017]
- [Replication of Empirical Studies in Software Engineering...][research_bezerra_2015]
- [Replication Package for Paper: LLHD: A Multi-level...][research_schuiki_2020_b]
- [Representation learning for coincidental correctness in...][research_hu_2026_c]
- [Reproducibility and credibility in empirical software...][research_rodriguezperez_2018]
- [Reproducibility Practices of Software Engineering...][research_cordeiro_2025]
- [Research of WebAssembly usage for high-performance code...][research_soluian_2025]
- [Research on Compiler Optimization Technology Based on...][research_cui_2025_c]
- [Research on coverage-guided fuzzing technique based on...][research_ma_2025]
- [Research on Instruction Set Architecture of 40-Bit...][research_anon_2019]
- [Research on Program Automatic Repair Method Combining...][research_li_2024_d]
- [Research on RISC-V-based Edge Convolution Acceleration...][research_luan_2025]
- [Resource Optimization based Virtual Machine Allocation...][research_dubey_2023]
- [Resource-Aware Distributed Submodular Maximization: A...][research_xu_2022_b]
- [Resource-efficient RISC-V Vector Extension Architecture...][research_islam_2023]
- [Resources for Reproducibility of Experiments in Empirical...][research_anchundia_2020]
- [REST API Fuzzing by Coverage Level Guided Blackbox Testing][research_tsai_2021]
- [Rethinking Correctness and Efficiency in AI-Assisted Code...][research_altunel_2026]
- [RETRACTED ARTICLE: The smell of fear: on the relation...][research_palomba_2019]
- [Retraction Note: Retraction note to: The smell of fear...][research_palomba_2020]
- [RETRACTION: Study on Large‐Scale Promotion of...][research_programming_2025]
- [Reusing the Optimized Code for JavaScript Ahead-of-Time...][research_park_2018]
- [Revealing Compiler Heuristics Through Automated Discovery...][research_seeker_2024]
- [Reverse Engineering of Obfuscated Lua Bytecode via...][research_luo_2023]
- [Reviewing Reproducibility in Software Engineering Research][research_cordeiro_2025_b]
- [Revisiting Machine Learning based Test Case...][research_zhao_2023]
- [Revisiting the building of past snapshots — a replication...][research_maesbermejo_2022]
- [Revisiting the reproducibility of empirical software...][research_gonzalezbaraho_2023]
- [Revisiting Unnaturalness for Automated Program Repair in...][research_yang_2025_b]
- [Reward-Aware Shapley Compensation: a Probabilistic and...][research_li_2025_f]
- [rFocal: Run 'FOCAL' Language Source Code][research_witthoft_2025]
- [RI-MAC: Optimising MAC Operation Using Custom RISC-V...][research_longchar_2025]
- [Rice 1953][research_rice_1953]
- [Richards and colleagues 2010][research_richards_2010]
- [Ripple Shapley: Data Influence Attribution in One...][research_zeng_2026]
- [RISC-TAE: Instruction Set Extension for Transformer Model...][research_liu_2025]
- [RISC-V Instruction Set Architecture Extensions: A Survey][research_cui_2023]
- [RISC-V SIMD Instructions - Vector Extension (Load/Store)][research_b_2025]
- [RISC-VTF: RISC-V Based Extended Instruction Set for...][research_jiao_2021]
- [RISC‐V Processor Hardware Modelling with Custom...][research_antony_2025]
- [Risk Attribution Using the Shapley Value: Methodology and...][research_tarashev_2015]
- [RLGFuzz: Reinforcement Learning Guided Fuzzing with...][research_shen_2024]
- [Robust Practical Binary Optimization at Run-time using...][research_engelke_2020]
- [Role-Aware Intelligent Agent Framework for Enhanced Code...][research_roshan_2025]
- [Rosenthal 1979][research_rosenthal_1979]
- [Rothermel and colleagues 2001][research_rothermel_2001]
- [Rothermel and Harrold 1997][research_rothermel_harrold_1997]
- [RTFM: Towards Understanding Source Code using Natural...][research_galanis_2020]
- [Rule modeling for automatic verification of RDC-50...][research_miyamoto_2024]
- [Running Large Language Models at Scale for Mining...][research_su_2026]
- [Runtime Metric Analysis in NoSQL Database Performance...][research_andor_2021]
- [Runtime prediction model for high performance computing...][research_tian_2025]
- [Runtime prediction of high-performance computing jobs...][research_chen_2020]
- [Runtime Value Numbering: A Profiling Technique to...][research_wen_2015]
- [Rust-twins: Automatic Rust Compiler Testing through...][research_yang_2024_b]
- [Rustlantis: Randomized Differential Testing of the Rust...][research_wang_2024_b]
- [RustSmith: Random Differential Compiler Testing for Rust][research_sharma_2023]
- [RV-IR: An MLIR-Based Architecture-Aware Intermediate...][research_jian_2026]
- [RVCE-FAL: A RISC-V Scalar-Vector Custom Extension for...][research_yu_2024]
- [RVVRadar: A Framework for Supporting the Programmer in...][research_klemmer_2022]
- [S-compiler: A code vulnerability detection method][research_monicacatherin_2015]
- [SAGE-HLS: Syntax-Aware AST-Guided LLM for High-Level...][research_khan_2025]
- [SAGE: A Compiler-assisted Reinforcement Learning-based...][research_maity_2026]
- [Same Coverage, Less Bloat: Accelerating Binary-only...][research_nagy_2021]
- [Scalable and Accurate Test Case Prioritization in...][research_yaraghi_2023]
- [Scalable SMT Sampling for Floating-Point Formulas via...][research_carrasco_2025]
- [SCALE-Ahead-Of-Time Compilation of CUDA for AMD GPUs][research_pavlidakis_2024]
- [ScaleHLS: A New Scalable High-Level Synthesis Framework...][research_ye_2022]
- [Schkufza, Sharma and Aiken 2013][research_schkufza_2013]
- [Seamless Self-Healing in WebAssembly Container...][research_matsubara_2025]
- [SecSwift, a Compiler-Based Framework for Software...][research_deferriere_2026]
- [Securing a compiler transformation][research_deng_2018]
- [Security Requirements Prioritization Techniques: A Survey...][research_khanneh_2022]
- [Self-Admitted Technical Debt and comments’ polarity: an...][research_cassee_2022]
- [Self-admitted technical debt practices: a comparison...][research_zampetti_2021]
- [Self-Hosted WebAssembly Runtime for Runtime-Neutral...][research_nakata_2025]
- [Semantic Coverage: Measuring Test Suite Effectiveness][research_alblwi_2023]
- [Semantic-Type-Guided Bug Finding][research_qian_2024]
- [Semantic‐aware two‐phase test case prioritization for...][research_li_2023_e]
- [Semi-streaming Algorithms for Submodular Function...][research_huang_2024_b]
- [Sequence submodular maximization meets streaming][research_yang_2020]
- [Session details: Session 4A: Compiler Correctness][research_chlipala_2015_b]
- [Sethi and Ullman 1970][research_sethi_ullman_1970]
- [Sewell and colleagues 2013][research_sewell_2013]
- [SHA-3 Instruction Set Extension for A 32-bit RISC...][research_eissa_2016]
- [Shapley 1953][research_shapley_1953]
- [SHapley Additive exPlanations (SHAP) for Efficient...][research_santos_2024]
- [Shapley Patch Valuation Method for Histopathological...][research_karadeniz_2025]
- [Shapley Value Approximation with Divisive Clustering][research_corder_2019]
- [Shapley value in machine learning modeling: optimizing...][research_ciano_2024]
- [Shapley Value is an Equitable Metric for Data Valuation][research_shobeiri_2022]
- [Shapley Value of a Cooperative Game with Fuzzy Set of...][research_mashchenko_2017]
- [Shapley value-based data valuation for machine learning...][research_baghcheband_2025]
- [Shapley Value-Based Feature Attribution for Data Masking][research_qu_2026]
- [Shapley value: from cooperative game to explainable...][research_li_2024_c]
- [Shapley-Based Data Valuation for Weighted $k$-Nearest...][research_zhang_2025_d]
- [Shapley-Based Data Valuation Method for the Machine...][research_baghcheband_2024]
- [Shapley-Based Data Valuation with Mutual Information: A...][research_vahedifar_2025]
- [Shapley-Value Based Feature Attribution for...][research_aldarmini_2025]
- [Shapley-Value Data Valuation for Semi-supervised Learning][research_courtnage_2021]
- [Shepherd: High-Precision Coverage Inference for...][research_shimizu_2025]
- [Silent Compiler Bug De-duplication via Three-Dimensional...][research_yang_2023_b]
- [Similarity-Aware Architecture/Compiler Co-Designed...][research_zhao_2021]
- [Simmons, Nelson and Simonsohn 2011][research_simmons_2011]
- [Simulink Model Static Analysis Results based on Abstract...][research_yang_2022]
- [Skeletal program enumeration for rigorous compiler testing][research_zhang_2017]
- [SLAMPA: Recommending Code Snippets with Statistical...][research_zhou_2018]
- [Slavı́k 1997][research_slavik_1997]
- [SMT-Based Translation Validation for Machine Learning...][research_bang_2022]
- [Software Development Effort Estimation Using Random...][research_anon_2018]
- [Software effort estimation accuracy prediction of machine...][research_mahmood_2021]
- [Software effort estimation using validated accuracy...][research_jeyaram_2025]
- [Software effort estimation using validated accuracy...][research_v_2023]
- [Software UART: A Use Case for VSCPU Worst-Case Execution...][research_yildiz_2019]
- [Solsmith: Solidity Random Program Generator for Compiler...][research_li_2025_c]
- [Solution to CAD Designer Effort Estimation based on...][research_nikiforova_2022]
- [Solver-based gradual type migration][research_phippscostin_2021]
- [Source Code Features and their Dependencies: An...][research_toosi_2023]
- [Source Code Implied Language Structure Abstraction...][research_wang_2023_c]
- [Source code obfuscation with genetic algorithms using...][research_delatorre_2024]
- [Source Code Plagiarism Detection with Pre-Trained Model...][research_anon_2023]
- [Special Issue on Syntax-Guided Synthesis Preface][research_fisman_2021]
- [Special Session: Reliability and Performance Evaluation...][research_imianosky_2024]
- [Specification and automatic verification of trust-based...][research_drawel_2020]
- [Specification and Formal Verification of...][research_trippel_2025]
- [Specification and Verification of a Formal Model for a...][research_anon_2025_b]
- [Specification-guided component-based synthesis from...][research_mishra_2022]
- [SpinalFuzz: Coverage-Guided Fuzzing for SpinalHDL Designs][research_ruep_2022]
- [SPNC: An Open-Source MLIR-Based Compiler for Fast...][research_sommer_2022]
- [SPRoC: Semantics-Preserving Mutations for Robustness...][research_shi_2025]
- [SRTuner: Effective Compiler Optimization Customization by...][research_park_2022_b]
- [SSA Form and Code Generation][research_dupontdedinech_2021]
- [SSFuzz: Synthesizing and scheduling bug-triggering code...][research_hu_2025]
- [Stack-based static WebAssembly binary slicing and...][research_choi_2026]
- [Startups and Technical Debt: Managing Technical Debt with...][research_chicote_2017]
- [State of mutation testing at google][research_petrovic_2018_b]
- [Statement frequency coverage: A code coverage criterion...][research_aghamohammadi_2021]
- [Static analysis by abstract interpretation against data...][research_urban_2025]
- [Static Analysis by Abstract Interpretation of the...][research_journault_2016]
- [Static Analysis of Endian Portability by Abstract...][research_delmas_2021]
- [Static Analysis of JNI Programs via Binary Decompilation][research_park_2023]
- [Static analysis of Sequential Function Charts using...][research_simon_2016]
- [Static detection of equivalent mutants in real-time...][research_basile_2022]
- [Static Local Concurrency Errors Detection in MPI-RMA...][research_saillard_2022]
- [Static Neural Compiler Optimization via Deep...][research_mammadli_2020]
- [Static Timing and Power Analysis of a RISC-V Pipelined...][research_kadarkarai_2025]
- [Static Value Analysis of Python Programs by Abstract...][research_fromherz_2018]
- [Static Worst-Case Execution Time Optimization using DPSO...][research_venkanna_2018_b]
- [Statistical Unigram Analysis for Source Code Repository][research_xu_2017]
- [STERILIZER CHAMBER DESIGN WITH TELEGRAM-BASED INTERNET OF...][research_kusumaningrum_2021]
- [Streaming adaptive submodular maximization][research_tang_2023]
- [Streaming Algorithms for Constrained Submodular...][research_cui_2023_b]
- [Streaming algorithms for non-monotone DR-submodular...][research_zhang_2025_e]
- [Streaming Algorithms for Non-Submodular Maximization on...][research_tan_2023_b]
- [Streaming algorithms for robust submodular maximization][research_yang_2021]
- [Streaming Non-Monotone Submodular Maximization...][research_mirzasoleiman_2018]
- [Streaming Stochastic Submodular Maximization with...][research_wang_2025_c]
- [Streaming submodular maximization under d-knapsack...][research_chen_2022_b]
- [Streaming Submodular Maximization Under Matroid...][research_feldman_2026]
- [Streaming Submodular Maximization Under Noises][research_yang_2019]
- [Streaming submodular maximization with fairness...][research_guo_2026_b]
- [Strumbelj and Kononenko 2013][research_strumbelj_kononenko_2013]
- [Studying WebAssembly and comparison of its performance...][research_rokotyanskaya_2023]
- [Submodular maximization meets streaming: matchings...][research_chakrabarti_2015]
- [Submodular Maximization Subject to Uniform and Partition...][research_kia_2026]
- [SuperGraph-SLP Auto-Vectorization][research_porpodas_2017]
- [Support for Just-in-Time Compilation of WebAssembly for...][research_moron_2023]
- [Supporting Dynamic Program Sizes in Deep Learning-Based...][research_hakimi_2025]
- [SurtGIS: A high-performance raster geospatial analysis...][research_parra_2026]
- [Survey on Estimation and Optimization of Worst-case...][research_meng_2020]
- [Swarm Intelligence for Software Effort Estimation: An...][research_laboudi_2025]
- [Symbolic Execution and Recent Applications to Worst-Case...][research_pasareanu_2019]
- [Symbolic MRD: Dynamic Memory, Undefined Behaviour, and...][research_richards_2025]
- [Synchronized Behavior Checking: A Method for Finding...][research_zhang_2025]
- [Synchronized Shared Memory and Procedural Abstraction...][research_gretz_2020]
- [Syntactic Versus Semantic Similarity of Artificial and...][research_ojdanic_2023]
- [Syntax, predicates, idioms — what really affects code...][research_ajami_2018]
- [Syntax-Driven Translation][research_cooper_2023_c]
- [Synthesizing an instruction selection rule library from...][research_buchwald_2018]
- [Synthesizing Instruction Selection Back-Ends from ISA...][research_drescher_2026]
- [SySTeC: A Symmetric Sparse Tensor Compiler][research_patel_2025]
- [System on Chip Implementation of Compiler Stack with a...][research_ismael_2018]
- [System-Level Test Case Prioritization Using Machine...][research_lachmann_2016]
- [Systematic Mapping Study of Ensemble Effort Estimation][research_idri_2016]
- [T 3 : Multi-level Tree-based Automatic Program Repair...][research_liu_2025_e]
- [TABU Search Prioritized Ant Colony Metaheuristic...][research_t_2020]
- [TagDebt: a bot to support technical debt management][research_biazotto_2026]
- [Taming undefined behavior in LLVM][research_lee_2017]
- [Targeting both Blazor Server and Blazor WebAssembly][research_himschoot_2020_b]
- [Technical Debt Contagiousness Metrics for Measurement and...][research_bi_2023]
- [Technical debt prioritization][research_pina_2022]
- [Technical debt prioritization using predictive analytics][research_codabux_2016]
- [Technical Debt Prioritization: A Search-Based Approach][research_alfayez_2019]
- [Technical Debt Prioritization: Taxonomy, Methods Results...][research_pina_2021]
- [Technical Debt Tools: a Survey and an Empirical Evaluation][research_gomes_2024]
- [Technical Debt, Software Evolution and Legacy][research_bass_2022]
- [Technical Perspective: Fusing Large Language Models with...][research_bavota_2026]
- [Techniques of Test Case Prioritization][research_puri_2016]
- [Template-Guided Program Repair in the Era of Large...][research_huang_2025]
- [Temporal Discounting in Software Engineering: A...][research_fagerholm_2019]
- [Tensor Program Optimization for the RISC-V Vector...][research_peccia_2025]
- [Tensor Program Superoptimization through Cost-Guided...][research_brauckmann_2026]
- [TenSure: Fuzzing Sparse Tensor Compilers (Registered...][research_mahathevan_2026]
- [Termination-checking for LLVM peephole optimizations][research_menendez_2016_b]
- [Terms for Efficient Proof Checking and Parsing][research_farber_2023]
- [Test Case Design and Test Case Prioritization using...][research_anon_2019_b]
- [Test case prioritization and selection technique in...][research_xiao_2018]
- [Test Case Prioritization for Regression Testing Using...][research_sawant_2024]
- [Test Case Prioritization in Continuous Integration...][research_pradolima_2020]
- [Test Case Prioritization using Transfer Learning in...][research_mamata_2023]
- [Test case sampling optimization for safety validation of...][research_qian_2026_b]
- [Test case selection and prioritization using machine...][research_pan_2021]
- [Test code refactoring unveiled: where and how does it...][research_martins_2024]
- [Test input prioritization for image segmentation: an...][research_li_2026_c]
- [Test prioritization in continuous integration environments][research_haghighatkhah_2018]
- [Test program generation for mixed-signal integrated...][research_mosin_2015]
- [TestCov: Robust Test-Suite Execution and Coverage...][research_beyer_2019]
- [Testing a PL/I Compiler Using Precomputation-based...][research_postema_2022]
- [Testing and Verifying Parallel Programs Using Data...][research_martinjeremymr_2019]
- [Testing Autonomous Driving Systems Through Blind-Spot...][research_moussa_2025]
- [Testing Error Handling Code With Software Fault Injection...][research_bai_2024]
- [Testing ocean software with metamorphic testing][research_luu_2022]
- [Testing static analyses for precision and soundness][research_taneja_2020]
- [Testing the Unknown: A Framework for OpenMP Testing via...][research_laguna_2024]
- [Testing, Credible Compilation, and Verification in the...][research_rinard_2026]
- [Testing-Based Formal Verification for Theorems and Its...][research_liu_2016]
- [The Application Of Machine Learning In Test Case...][research_mece_2020]
- [The ARES High-Level Intermediate Representation][research_moss_2016]
- [The broken windows theory applies to technical debt][research_leven_2024]
- [The CakeML Compiler Explorer][research_hjort_2018]
- [The Correctness-Security Gap in Compiler Optimization][research_dsilva_2015]
- [The Design of Optimized RISC Processor for Edge...][research_oh_2023]
- [The Evolution of Empirical Methods in Software Engineering][research_felderer_2020]
- [The Expansion of Source Code Abbreviations Using a...][research_alatawi_2018]
- [The forgotten role of search queries in IR-based bug...][research_rahman_2021]
- [The Forward-Reverse Greedy Algorithm for Distributed...][research_tackett_2024]
- [The Impact of Fine-Tuning Large Language Models on...][research_machacek_2025]
- [The Impact of Undefined Behavior on Compiler Optimization][research_shen_2021]
- [The Influence of Cost Drivers on Effort Estimation in...][research_iqbal_2022]
- [The method of requirements prioritization in software...][research_anon_2024]
- [The MLIR Transform Dialect][research_lucke_2025]
- [The reproducibility of programming-related issues in...][research_mondal_2022]
- [The role and value of replication in empirical software...][research_shepperd_2018]
- [The Shapley and Position Values to Design Coalitional...][research_muros_2019]
- [The Shapley Value as a Sustainable Cooperative Solution...][research_gromova_2016]
- [The Shapley Value, a Crown Jewel of Cooperative Game...][research_thomson_2019]
- [The Simian concept: Parallel Discrete Event Simulation...][research_santhi_2015]
- [The Software Heritage Graph Dataset][research_pietri_2020]
- [The Trusted Computing Base of the CompCert Verified...][research_monniaux_2022]
- [The use of large language models for program repair][research_zubair_2025]
- [The verified CakeML compiler backend][research_kiamtan_2019]
- [The Vocabulary of Flaky Tests in the Context of SAP HANA][research_berndt_2023]
- [Thinking Fast and Correct: Automated Rewriting of...][research_qian_2026]
- [Thread-Aware Area-Efficient High-Level Synthesis Compiler...][research_kim_2021]
- [Threaded Code Generation with a Meta-Tracing JIT Compiler][research_izawa_2022]
- [Time-Accurate ASM as a Refinement Scheme for Worst-Case...][research_mguidich_2016]
- [Timing Analysis Techniques][research_gliwa_2021_b]
- [Timing speculation-aware instruction set extension for...][research_ahmed_2015]
- [TinyGen: Portable and Compact Code Generation for Tiny...][research_ko_2026]
- [TinyML Unleashed: Accelerating TensorFlow Lite Micro...][research_mahmoudi_2025]
- [Tinyrossa: A Compiler Framework for Vertical, Verified...][research_vrany_2024]
- [Tofte and Talpin 1997][research_tofte_talpin_1997]
- [Toward a Formally Verified Compiler for a Synchronous...][research_girault_2025]
- [Toward an Automated Hardware Pipelining LLVM Pass...][research_leidel_2021]
- [Toward Green Code: Prompting Small Language Models for...][research_ashraf_2025_b]
- [Toward learnable and interpretable data Shapley valuation...][research_li_2025_g]
- [Toward prioritization of self-admitted technical debt: an...][research_delima_2022]
- [Towards a Domain-Extensible Compiler: Optimizing an Image...][research_koehler_2021]
- [Towards a functional requirements prioritization with...][research_condorifernand_2018]
- [Towards a Unified Multi-Target Mlir-Based Compiler: A...][research_letras_2025]
- [Towards a verified compiler prototype for the synchronous...][research_yang_2015]
- [Towards a verified Lustre compiler with modular reset][research_bourke_2018]
- [Towards a WebAssembly standalone runtime on GraalVM][research_salim_2019]
- [Towards Automatic HBM Allocation Using LLVM: A Case Study...][research_khaldi_2016]
- [Towards Automatic Property Generation for SoC Security...][research_wang_2022]
- [TOWARDS AUTONOMOUS CODE OPTIMIZATION: A REINFORCEMENT...][research_svenkatesan_2025]
- [Towards Compile-Time-Reducing Compiler Optimization...][research_jayatilaka_2021]
- [Towards compiler-aided correctness checking of adjoint...][research_huck_2020]
- [Towards defect-type-aware adaptive program repair: A...][research_zhang_2026_h]
- [Towards enhancing the reproducibility of deep learning...][research_shah_2024]
- [Towards Incremental Static Race Detection in OpenMP...][research_swain_2018]
- [Towards Interpretable Ensemble Learning for Software...][research_doshi_2026]
- [Towards Path-Aware Coverage-Guided Fuzzing][research_priamo_2026]
- [Towards Supporting Semiring in MLIR-Based COMET Compiler][research_guo_2022]
- [Towards understanding code review practices for...][research_bessghaier_2025]
- [Towards Verified Rounding Error Analysis for Stationary...][research_kellison_2022_b]
- [Towards Verified Security: Formal Methods for LLM-Based...][research_dauksevic_2026]
- [TPDE: A Fast Adaptable Compiler Back-End Framework][research_schwarz_2026]
- [Trace-Based Bytecode Interpreter Visualization for...][research_herber_2025]
- [Tracy: A Business-Driven Technical Debt Prioritization...][research_reboucasdealme_2019_b]
- [Translating CUDA to OpenCL for Hardware Generation using...][research_kim_2019]
- [Translation from Visual to Layout-based Android Test...][research_coppola_2020]
- [Translation Validation for JIT Compiler in the V8...][research_kwon_2024]
- [Translation Validation of Information Leakage of Compiler...][research_panigrahi_2023]
- [TreeHouse: An MLIR-based Compilation Flow for Real-Time...][research_su_2024]
- [Tutorial on Static Inference of Numeric Invariants by...][research_mine_2017]
- [Twine: An Embedded Trusted Runtime for WebAssembly][research_menetrey_2021]
- [Type-Centric Kotlin Compiler Fuzzing: Preserving Test...][research_stepanov_2021]
- [TYPEFUZZ: Type Coverage Directed JavaScript Engine...][research_wienand_2026]
- [Typestates Specification and Verification in Frama-C][research_patte_2025]
- [UML Associations - Reducing the Gap in Test Coverage...][research_eriksson_2016]
- [Understanding and Finding JIT Compiler Performance Bugs][research_yi_2026]
- [Understanding and improving the quality and...][research_pimentel_2021]
- [Understanding Binary Code Similarity for Real-World...][research_guo_2026]
- [Understanding Bug-Reproducing Tests: A First Empirical...][research_hora_2026]
- [Understanding Feature Request Practice on GitHub via a...][research_li_2025_d]
- [Understanding Key Features of High-Impact Bug Reports][research_karim_2017]
- [Understanding practitioners’ reasoning and requirements...][research_biazotto_2025]
- [Understanding Self-Admitted Technical Debt in Test Code...][research_nakamura_2026]
- [Unified HW/SW Coverage: A Novel Metric to Boost...][research_bruns_2022_b]
- [Unleashing the power of compiler intermediate...][research_li_2022]
- [Unleashing Triton on CPUs: Compilation and Runtime...][research_li_2026]
- [Upstream bug management in Linux distributions][research_lin_2022]
- [Usability Technical Debt in Software Projects: A...][research_lage_2019]
- [Usage of Large Language Model for Code Generation Tasks...][research_bistarelli_2025]
- [Use Case-Based Analytical Hierarchy Process Method for...][research_naufalmaulana_2022]
- [Use of Compiler Intermediate Representation for Reverse...][research_mzid_2022]
- [Use of Measurements in Worst-Case Execution Time...][research_costa_2021]
- [User-Directed Loop-Transformations in Clang][research_kruse_2018]
- [Using Artificial Bee Colony for Code Coverage Based Test...][research_konsaard_2015]
- [Using docker containers to improve reproducibility in...][research_cito_2016]
- [Using Extremely Simplified Functional Size Measures for...][research_lavazza_2020]
- [Using Large-Scale Anomaly Detection on Code to Improve...][research_bryksin_2020]
- [Using rapid reviews to support software engineering...][research_pizard_2024]
- [Using text clustering to predict defect resolution time...][research_assar_2015]
- [Utilizing Machine Learning Techniques for Worst-Case...][research_kumar_2024]
- [Valent-Blocks: Scalable High-Performance Compilation of...][research_scheidl_2020]
- [Variable Bit-Precision Vector Extension for RISC-V Based...][research_rk_2021]
- [VCNN: A compiler of CNNs based on MLIR for multi-core...][research_chen_2024]
- [Vectorization in PyPy's Tracing Just-In-Time Compiler][research_plangger_2016]
- [Vectorized Nonlinear Functions with the RISC-V Vector...][research_bavier_2023]
- [VECTR: A Lightweight Requirements Prioritization Method...][research_pattyn_2026]
- [VEGA: Automatically Generating Compiler Backends using a...][research_zhong_2025]
- [Verification by abstract interpretation, soundness and...][research_cousot_2015]
- [Verified compilation of CakeML to multiple machine-code...][research_fox_2017]
- [Verified compilation on a verified processor][research_loow_2019]
- [Verified construction of static single assignment form][research_buchwald_2016]
- [Verified lifting of stencil computations][research_kamil_2016]
- [Verified peephole optimizations for CompCert][research_mullen_2016]
- [Verified Propagation Redundancy and Compositional UNSAT...][research_tan_2023]
- [Verified VCG and Verified Compiler for Dafny][research_nezamabadi_2026]
- [Verifying Instruction Set Simulators using...][research_herdt_2019]
- [Verifying optimizations of concurrent programs in the...][research_zha_2022]
- [Verifying Term Graph Optimizations using Isabelle/HOL][research_webb_2023]
- [VeriPhy: verified controller executables from verified...][research_bohrer_2018]
- [Video SIMDBench: Benchmarking the Compiler Vectorization...][research_alvanos_2016]
- [Vivienne: Relational Verification of Cryptographic...][research_tsoupidi_2021]
- [Vmxdotp: A RISC-V Vector ISA Extension for Efficient...][research_wipfli_2026]
- [WAFL: Binary-Only WebAssembly Fuzzing with Fast Snapshots][research_haler_2021]
- [Wait for it: identifying “On-Hold” self-admitted...][research_maipradit_2020]
- [Wapplique: Testing WebAssembly Runtime via Execution...][research_zhao_2024]
- [WARD: Efficient Memory Protection for WebAssembly on Tiny...][research_shin_2026]
- [WARDuino: An embedded WebAssembly virtual machine][research_lauwaerts_2024]
- [Wasm-Mutate: Fast and effective binary diversification...][research_cabreraarteaga_2024]
- [Wasm-WCET: Worst-Case Execution-Time Analysis of...][research_seidler_2026]
- [WasmSlim: Optimizing WebAssembly Binary Distribution via...][research_wen_2023]
- [WasmWeaver: A Framework for Runtime-Aware WebAssembly...][research_muller_2026]
- [WaTZ: A Trusted WebAssembly Runtime Environment with...][research_menetrey_2022]
- [WaVe: a verifiably secure WebAssembly sandboxing runtime][research_johnson_2023]
- [WBSan: WebAssembly Bug Detection for Sanitization and...][research_wu_2025]
- [WebAssembly as a Fuzzing Compilation Target (Registered...][research_bauckholt_2024]
- [WebAssembly for Container Runtime: Are We There Yet?][research_liu_2025_b]
- [WebAssembly Module Internals: Sections and Memory Model][research_jain_2021]
- [WebAssembly versus JavaScript: Energy and Runtime...][research_demacedo_2022]
- [WebAssembly: How Low Can a Bytecode Go?][research_titzer_2025]
- [Wegman and Zadeck 1991][research_wegman_zadeck_1991]
- [Weighted Reward for Reinforcement Learning based Test...][research_li_2021_b]
- [Weighted shapley value: A cooperative game theory for...][research_singh_2023]
- [What do developer-repaired Flaky tests tell us about the...][research_parry_2022]
- [When Compiler Optimizations Meet Symbolic Execution: An...][research_zhang_2024_b]
- [When Function Inlining Meets WebAssembly...][research_romano_2023_b]
- [When Function Signature Recovery Meets Compiler...][research_lin_2021]
- [When is Continuous Integration Useful? Empirical Study on...][research_imai_2021]
- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large...][research_yang_2024_e]
- [Who Will Leave the Company?: A Large-Scale Industry Study...][research_bao_2017]
- [Whose Baseline Compiler is it Anyway?][research_titzer_2024]
- [Why are Android apps removed from Google Play?][research_wang_2018_b]
- [Why Just-In-Time Compilation Matters: Evaluating Runtime...][research_maia_2026]
- [Why Shapley Value and Its Variants Are Useful in Machine...][research_bokati_2024]
- [Why Some Bug-bounty Vulnerability Reports are Invalid?][research_shafigh_2021]
- [Wild SBOMs: a Large-scale Dataset of Software Bills of...][research_soeiro_2025]
- [Wilhelm and colleagues 2008][research_wilhelm_2008]
- [Wilson 1927][research_wilson_1927]
- [Wong and colleagues 1995][research_wong_1995]
- [Work-in-Progress: Searching Optimal Compiler Optimization...][research_chang_2023]
- [Worst Case Execution Time and Power Estimation of...][research_rodriguezferra_2023]
- [Worst-Case Execution Time Analysis for Many-Core...][research_skalistis_2016]
- [Worst-Case Execution Time Analysis of a Real-Time System...][research_merazga_2025]
- [Worst-Case Execution Time Analysis of Real-Time Robotic...][research_samiei_2024]
- [Worst-Case Execution Time Estimation for Numerical...][research_susca_2022]
- [Worst-case Execution Time Estimation of Legacy Vehicular...][research_ventovaara_2020]
- [Worst-Case Execution Time Testing via Evolutionary...][research_aquino_2018]
- [WuppieFuzz: Coverage-Guided, Stateful REST API Fuzzing][research_rooijakkers_2026]
- [Yang and colleagues 2011][research_yang_2011]
- [Yoo and Harman 2012][research_yoo_harman_2012]
- [Young 1985][research_young_1985]
- [Zhao and colleagues 2012][research_zhao_2012]
- [Zhu, Hall and May 1997][research_zhu_1997]
- [Zipr: Efficient Static Binary Rewriting for Security][research_hawkins_2017]
- [Zoish: A Novel Feature Selection Approach Leveraging...][research_sadaei_2023]

[research_abikaram_2023]: https://doi.org/10.1109/iccad57390.2023.10323650
[research_abnane_2017]: https://doi.org/10.1145/3019612.3019905
[research_abnane_2023]: https://doi.org/10.1007/s10664-022-10260-0
[research_abraham_2025]: https://doi.org/10.1109/ase63991.2025.00369
[research_acharya_2025]: https://doi.org/10.1145/3756681.3756995
[research_adiyoso_2023]: https://doi.org/10.35870/jimik.v4i2.231
[research_aghamohammadi_2021]: https://doi.org/10.1016/j.infsof.2020.106426
[research_agostini_2022]: https://doi.org/10.1145/3508352.3549424
[research_agrawal_2025]: https://doi.org/10.55041/ijsrem10701
[research_agresti_coull_1998]: https://doi.org/10.1080/00031305.1998.10480550
[research_ahmad_2017]: https://doi.org/10.1109/icicict1.2017.8342602
[research_ahmad_2019]: https://doi.org/10.1109/msr.2019.00050
[research_ahmad_2022]: https://doi.org/10.14569/ijacsa.2022.0130728
[research_ahmed_2015]: https://doi.org/10.1109/asap.2015.7245701
[research_ahmed_2022]: https://doi.org/10.1109/access.2022.3216840
[research_aho_ganapathi_1989]: https://doi.org/10.1145/69558.75700
[research_ajami_2018]: https://doi.org/10.1007/s10664-018-9628-3
[research_ajiki_2026]: https://doi.org/10.5220/0014491100004058
[research_akanbi_2022]: https://doi.org/10.14445/23497157/ijres-v9i3p101
[research_akbar_2020]: https://doi.org/10.1145/3379597.3387474
[research_akcelik_2025]: https://doi.org/10.1109/icmlt65785.2025.11193393
[research_akhtar_2021]: https://doi.org/10.1007/s11277-021-08296-4
[research_akshay_2023]: https://doi.org/10.1007/978-3-031-37706-8_19
[research_alaluf_2022]: https://doi.org/10.1287/moor.2021.1224
[research_alardawi_2015]: https://doi.org/10.1109/wcitca.2015.7367057
[research_alatawi_2018]: https://doi.org/10.1109/compsac.2018.10260
[research_alblwi_2023]: https://doi.org/10.5220/0012063900003538
[research_aldarmini_2025]: https://doi.org/10.1109/icdmw69685.2025.00046
[research_alecsandrobaci_2025]: https://doi.org/10.5335/rbca.v17i3.16310
[research_aleen_2016]: https://doi.org/10.1145/2903150.2903169
[research_aleen_2017]: https://doi.org/10.1007/s10766-016-0485-7
[research_alegroth_2018]: https://doi.org/10.1109/icst.2018.00026
[research_alfayez_2017]: https://doi.org/10.1007/978-3-319-62217-0_9
[research_alfayez_2019]: https://doi.org/10.1109/qrs.2019.00060
[research_alfayez_2020]: https://doi.org/10.1145/3387906.3388630
[research_alhamed_2022]: https://doi.org/10.1109/icsme55016.2022.00020
[research_alhumam_2026]: https://doi.org/10.1016/j.array.2026.101027
[research_ali_2023]: https://doi.org/10.1109/access.2023.3256533
[research_aljebreen_2025]: https://doi.org/10.14569/ijacsa.2025.0160525
[research_aljedaani_2020]: https://doi.org/10.1109/cdma47397.2020.00021
[research_alladi_2026]: https://doi.org/10.1109/cgo68049.2026.11395226
[research_allamanis_sutton_2013]: https://doi.org/10.1109/MSR.2013.6624029
[research_allen_1970]: https://doi.org/10.1145/800028.808479
[research_almeida_2021]: https://doi.org/10.1145/3460120.3484771
[research_alpay_2025]: https://doi.org/10.1145/3731125.3731127
[research_alqarni_2022]: https://doi.org/10.21428/594757db.b85e6625
[research_alrakban_2025]: https://doi.org/10.1109/access.2025.3617387
[research_alrefai_2017]: https://doi.org/10.14419/jacst.v6i1.6713
[research_alruqaishi_2026]: https://doi.org/10.1007/s11227-026-08506-5
[research_althar_2020]: https://doi.org/10.1007/978-981-15-7965-3_7
[research_altunel_2026]: https://doi.org/10.5220/0014971000004015
[research_alur_2015]: https://doi.org/10.1109/memcod.2015.7340460
[research_alvanos_2016]: https://doi.org/10.1109/dsd.2016.90
[research_alzahrani_2022]: https://doi.org/10.5220/0011101700003176
[research_alzubidy_2018]: https://doi.org/10.1007/s10664-018-9626-5
[research_amanatidis_2020]: https://doi.org/10.1007/s10664-020-09869-w
[research_amasaki_2017]: https://doi.org/10.1109/apsec.2017.105
[research_amasaki_2022]: https://doi.org/10.1007/s10664-021-10103-4
[research_ambal_2022]: https://doi.org/10.1145/3497775.3503676
[research_amdahl_1967]: https://doi.org/10.1145/1465482.1465560
[research_amini_2026]: https://doi.org/10.1007/s10664-026-10850-2
[research_anbiya_2025]: https://doi.org/10.1016/j.procs.2025.09.405
[research_anchundia_2020]: https://doi.org/10.1109/access.2020.2964587
[research_andor_2021]: https://doi.org/10.23919/softcom52868.2021.9559083
[research_andrews_2005]: https://doi.org/10.1109/ICSE.2005.1553583
[research_andruccioli_2026]: https://doi.org/10.3390/data11040088
[research_ankushjitendra_2025]: https://doi.org/10.30574/ijsra.2025.16.2.2463
[research_anon_2017]: https://doi.org/10.1130/abs/2017ne-290436
[research_anon_2018]: https://doi.org/10.22266/ijies2018.1231.30
[research_anon_2019]: https://doi.org/10.12677/csa.2019.99186
[research_anon_2019_b]: https://doi.org/10.35940/ijeat.a9762.109119
[research_anon_2023]: https://doi.org/10.26615/978-954-452-092-2_034
[research_anon_2023_b]: https://doi.org/10.3389/fenrg.2023.1212388
[research_anon_2023_c]: https://doi.org/10.18137/rnu.v9187.23.04.p.171
[research_anon_2024]: https://doi.org/10.15407/pp2024.02-03.132
[research_anon_2025]: https://doi.org/10.37547/tajet/volume07issue10-17
[research_anon_2025_b]: https://doi.org/10.32515/2664-262x.2025.11(42).2.38-44
[research_antoniadis_2021]: https://doi.org/10.1109/mwscas47672.2021.9531908
[research_antony_2025]: https://doi.org/10.1002/9781394272549.ch7
[research_antoy_2017]: https://doi.org/10.1007/978-3-319-63139-4_6
[research_apa_2020]: https://doi.org/10.1145/3382494.3421463
[research_appel_1998]: https://doi.org/10.1145/278283.278285
[research_aquino_2018]: https://doi.org/10.1109/issre.2018.00019
[research_aradhya_2018]: https://doi.org/10.21817/ijet/2018/v10i3/181003098
[research_arasteh_2024]: https://doi.org/10.1016/b978-0-443-16147-6.00019-0
[research_arbaoui_2024]: https://doi.org/10.1109/iwcmc61514.2024.10592437
[research_arcaro_2020]: https://doi.org/10.1109/rtss49844.2020.00016
[research_arnstrom_2024]: https://doi.org/10.1109/tac.2024.3395521
[research_arrieta_2023]: https://doi.org/10.1109/esem56168.2023.10304794
[research_arrieta_2026]: https://doi.org/10.1007/s10664-026-10875-7
[research_ashouri_2026]: https://doi.org/10.1145/3831596
[research_ashraf_2025]: https://doi.org/10.1109/case58245.2025.11163762
[research_ashraf_2025_b]: https://doi.org/10.1109/fllm67465.2025.11391183
[research_askar_2025]: https://doi.org/10.14722/ndss.2025.230125
[research_assar_2015]: https://doi.org/10.1007/s10664-015-9391-7
[research_astuti_2023]: https://doi.org/10.28989/compiler.v12i2.1919
[research_atanassov_2024]: https://doi.org/10.3897/arb.v36.e02
[research_athale_2025]: https://doi.org/10.1109/llm4code66737.2025.00026
[research_auerbach_2017]: https://doi.org/10.1145/3035918.3035961
[research_augustin_2025]: https://doi.org/10.5220/0013203900003928
[research_averill_2026]: https://doi.org/10.14722/bar.2026.23046
[research_avigad_2025]: https://doi.org/10.1007/s10817-025-09723-y
[research_ayeoribe_2026]: https://doi.org/10.58466/35jafg24
[research_aytekin_2026]: https://doi.org/10.1007/s10515-026-00599-9
[research_azevedo_2025]: https://doi.org/10.5753/sbes.2025.11270
[research_azmy_2018]: https://doi.org/10.1016/j.scico.2017.08.003
[research_azuma_2022]: https://doi.org/10.1007/s10664-021-10081-7
[research_azzeh_2015]: https://doi.org/10.1016/j.jss.2015.01.028
[research_azzeh_2018]: https://doi.org/10.1002/smr.2110
[research_b_2025]: https://doi.org/10.1109/icici65870.2025.11069565
[research_babur_2023]: https://doi.org/10.1007/s10664-023-10368-x
[research_baek_2017]: https://doi.org/10.1007/s10586-017-1113-z
[research_baek_2024]: https://doi.org/10.5626/ktcp.2024.30.10.519
[research_baghcheband_2024]: https://doi.org/10.1007/978-3-031-62700-2_16
[research_baghcheband_2025]: https://doi.org/10.1007/s42452-025-07328-z
[research_bai_2024]: https://doi.org/10.1109/tdsc.2023.3288876
[research_bakhirkin_2017]: https://doi.org/10.1007/978-3-319-66706-5_2
[research_balachandran_2015]: https://doi.org/10.1109/icsm.2015.7332498
[research_balasubramania_2024]: https://doi.org/10.1109/access.2024.3389673
[research_baldassarre_2023]: https://doi.org/10.1007/s10664-023-10357-0
[research_balogh_2018]: https://doi.org/10.1109/llvm-hpc.2018.8639205
[research_bandyopadhyay_2022]: https://doi.org/10.15864/ajse.3205
[research_banerjee_2018]: https://doi.org/10.1145/3172871.3180078
[research_bang_2022]: https://doi.org/10.1007/978-3-031-13188-2_19
[research_bansal_aiken_2006]: https://doi.org/10.1145/1168857.1168906
[research_bao_2017]: https://doi.org/10.1109/msr.2017.58
[research_bao_2021]: https://doi.org/10.1109/tse.2019.2918536
[research_bao_2024]: https://doi.org/10.1007/s40305-024-00543-2
[research_barani_2023]: https://doi.org/10.1109/icstw58534.2023.00071
[research_barany_2018]: https://doi.org/10.1145/3178372.3179521
[research_barboni_2026]: https://doi.org/10.1145/3828728
[research_barik_2015]: https://doi.org/10.1109/msr.2015.70
[research_barriere_2020]: https://doi.org/10.1145/3410263
[research_barriere_2021]: https://doi.org/10.1145/3434327
[research_barriere_2023]: https://doi.org/10.1145/3571202
[research_basile_2022]: https://doi.org/10.1007/s10664-022-10149-y
[research_basili_2021]: https://doi.org/10.1007/s10664-021-10055-9
[research_basili_weiss_1984]: https://doi.org/10.1109/TSE.1984.5010301
[research_basiturrahim_2025]: https://doi.org/10.37256/cm.6520256223
[research_bass_2022]: https://doi.org/10.1007/978-3-031-05469-3_20
[research_basso_2023]: https://doi.org/10.1145/3591473
[research_bauckholt_2024]: https://doi.org/10.1145/3678722.3685531
[research_bavier_2023]: https://doi.org/10.1109/arith58626.2023.00032
[research_bavota_2016]: https://doi.org/10.1145/2901739.2901742
[research_bavota_2026]: https://doi.org/10.1145/3789228
[research_behera_2025]: https://doi.org/10.1016/j.procs.2025.04.658
[research_bell_2024]: https://doi.org/10.1007/s11222-024-10459-9
[research_bembenek_2023]: https://doi.org/10.1145/3571200
[research_berger_2002]: https://doi.org/10.1145/582419.582421
[research_beringer_2021]: https://doi.org/10.1007/978-3-030-80515-9_6
[research_berndt_2023]: https://doi.org/10.1109/esem56168.2023.10304860
[research_berndt_2026]: https://doi.org/10.1109/saner67736.2026.00016
[research_berry_2021]: https://doi.org/10.1007/s10664-021-09986-0
[research_bessghaier_2025]: https://doi.org/10.1007/s10664-025-10654-w
[research_besson_2017]: https://doi.org/10.1007/s10817-017-9439-z
[research_besson_2018]: https://doi.org/10.1007/s10817-018-9496-y
[research_betka_2021]: https://doi.org/10.1109/ast52587.2021.00021
[research_beyer_2019]: https://doi.org/10.1109/ase.2019.00105
[research_bezerra_2015]: https://doi.org/10.1109/esem.2015.7321213
[research_bhamidipati_2023]: https://doi.org/10.1109/vlsid57277.2023.00046
[research_bhatia_2026]: https://doi.org/10.1145/3785001
[research_bi_2023]: https://doi.org/10.1109/techdebt59074.2023.00012
[research_biazotto_2025]: https://doi.org/10.1007/s10664-025-10691-5
[research_biazotto_2026]: https://doi.org/10.1007/s10664-026-10900-9
[research_biggar_2021]: https://doi.org/10.1007/978-3-030-80515-9_24
[research_bik_2022]: https://doi.org/10.1145/3544559
[research_binosi_2023]: https://doi.org/10.5220/0011625300003411
[research_birnbaum_1968]: https://doi.org/10.21236/ad0670563
[research_bistarelli_2025]: https://doi.org/10.1007/s42979-025-04241-5
[research_black_2025]: https://doi.org/10.1109/tetci.2024.3446695
[research_blackburn_2006]: https://doi.org/10.1145/1167473.1167488
[research_blackburn_2016]: https://doi.org/10.1145/2983574
[research_blanchet_2003]: https://doi.org/10.1145/781131.781153
[research_blazy_2023]: https://doi.org/10.1145/3573105.3579107
[research_bleier_2023]: https://doi.org/10.1145/3578357.3591219
[research_boda_2026]: https://doi.org/10.1145/3771775.3786271
[research_bodin_2015]: https://doi.org/10.1145/2676724.2693174
[research_boehm_1988]: https://doi.org/10.1109/2.59
[research_boehm_2023]: https://doi.org/10.1145/3555041.3589407
[research_bogunovic_2017]: https://doi.org/10.1109/camsap.2017.8313155
[research_bohm_jacopini_1966]: https://doi.org/10.1145/355592.365646
[research_bohrer_2018]: https://doi.org/10.1145/3192366.3192406
[research_bokati_2024]: https://doi.org/10.1007/978-3-031-43601-7_10
[research_bolat_2025]: https://doi.org/10.1109/isvlsi65124.2025.11130308
[research_borade_2025]: https://doi.org/10.1109/ginotech63460.2025.11076631
[research_bosu_2015]: https://doi.org/10.1109/msr.2015.21
[research_botor_2018]: https://doi.org/10.1063/1.5079067
[research_boujida_2021]: https://doi.org/10.5220/0010603700002992
[research_bourke_2017]: https://doi.org/10.1145/3140587.3062358
[research_bourke_2018]: https://doi.org/10.1145/3207719.3207732
[research_brach_2024]: https://doi.org/10.1109/fllm63129.2024.10852497
[research_brauckmann_2026]: https://doi.org/10.1109/cgo68049.2026.11395198
[research_braun_2013]: https://doi.org/10.1007/978-3-642-37051-9_6
[research_brenes_2019]: https://doi.org/10.1109/concapanxxxix47272.2019.8976981
[research_brennan_2020]: https://doi.org/10.1109/sp40000.2020.00007
[research_bride_2017]: https://doi.org/10.1007/978-3-319-52234-0_6
[research_britto_2015]: https://doi.org/10.1109/icgse.2015.10
[research_brown_2024]: https://doi.org/10.1109/scw63240.2024.00133
[research_bruns_2022]: https://doi.org/10.1145/3526241.3530340
[research_bruns_2022_b]: https://doi.org/10.1109/fdl56239.2022.9925661
[research_brus_2025]: https://doi.org/10.1109/ase63991.2025.00121
[research_bryksin_2020]: https://doi.org/10.1145/3379597.3387447
[research_buchbinder_2015]: https://doi.org/10.1137/130929205
[research_buchbinder_2024]: https://doi.org/10.1109/focs61266.2024.00050
[research_buchbinder_2025]: https://doi.org/10.1137/24m1698122
[research_buchwald_2016]: https://doi.org/10.1145/2892208.2892211
[research_buchwald_2018]: https://doi.org/10.1145/3168821
[research_budkowski_2017]: https://doi.org/10.1007/978-0-387-35394-4_29
[research_bui_2023]: https://doi.org/10.1007/s10664-023-10415-7
[research_bushehri_2026]: https://doi.org/10.1109/tdsc.2025.3641055
[research_bytyn_2019]: https://doi.org/10.1109/iscas.2019.8702357
[research_cabreraarteaga_2024]: https://doi.org/10.1016/j.cose.2024.103731
[research_calamo_2025]: https://doi.org/10.1007/978-3-031-92285-5_6
[research_cambou_2017]: https://doi.org/10.1109/sai.2017.8252190
[research_campbell_2024]: https://doi.org/10.1109/bigdata62323.2024.10825952
[research_campos_2017]: https://doi.org/10.1109/esem.2017.55
[research_campos_2026]: https://doi.org/10.1109/access.2026.3714292
[research_canizares_2023]: https://doi.org/10.1007/s10586-023-04074-y
[research_cao_2023]: https://doi.org/10.1007/978-3-031-44245-2_8
[research_cao_2025]: https://doi.org/10.1145/3729269
[research_carminati_2017]: https://doi.org/10.1016/j.aci.2017.03.002
[research_carminati_2018]: https://doi.org/10.1007/s11241-018-9306-y
[research_carrasco_2025]: https://doi.org/10.1109/icst62969.2025.10989031
[research_cassee_2022]: https://doi.org/10.1007/s10664-022-10183-w
[research_cassee_2025]: https://doi.org/10.1007/s10664-024-10611-z
[research_castiglia_2019]: https://doi.org/10.1109/cdc40024.2019.9029710
[research_castro_2009]: https://doi.org/10.1016/j.cor.2008.04.004
[research_castrolopez_2019]: https://doi.org/10.1109/cgo.2019.8661199
[research_chaitin_1982]: https://doi.org/10.1145/872726.806984
[research_chakrabarti_2015]: https://doi.org/10.1007/s10107-015-0900-7
[research_chakrabarty_2026]: https://doi.org/10.1016/j.orl.2025.107387
[research_chakravarthi_2025]: https://doi.org/10.1007/978-3-031-85044-8_7
[research_challita_2017]: https://doi.org/10.5220/0006236500001535
[research_chang_2023]: https://doi.org/10.1145/3607890.3608460
[research_chaplygin_2025]: https://doi.org/10.21869/2223-1560-2025-29-3-99-112
[research_chargueraud_2015]: https://doi.org/10.1007/978-3-319-22102-1_9
[research_charles_2015]: https://doi.org/10.1145/2764967.2782785
[research_chaudhary_2016]: https://doi.org/10.14569/ijacsa.2016.070131
[research_chavanon_2024]: https://doi.org/10.1145/3636501.3636954
[research_chayan_2023]: https://doi.org/10.5391/ijfis.2023.23.3.353
[research_che_2025]: https://doi.org/10.1109/fllm67465.2025.11391195
[research_cheirdari_2018]: https://doi.org/10.1109/bigdata.2018.8622456
[research_chelini_2020]: https://doi.org/10.1145/3410463.3414635
[research_chen_2015]: https://doi.org/10.1109/tase.2015.11
[research_chen_2016]: https://doi.org/10.1145/2908080.2908095
[research_chen_2016_b]: https://doi.org/10.1007/s10664-016-9429-5
[research_chen_2017]: https://doi.org/10.1109/icse-seip.2017.26
[research_chen_2019]: https://doi.org/10.1145/3338906.3338957
[research_chen_2019_b]: https://doi.org/10.1109/ase.2019.00037
[research_chen_2019_c]: https://doi.org/10.1109/ats47505.2019.00013
[research_chen_2020]: https://doi.org/10.1145/3407947.3407968
[research_chen_2020_b]: https://doi.org/10.1145/3324884.3416570
[research_chen_2021]: https://doi.org/10.1007/s10664-020-09893-w
[research_chen_2022]: https://doi.org/10.1145/3508362
[research_chen_2022_b]: https://doi.org/10.1007/s10878-022-00951-1
[research_chen_2023]: https://doi.org/10.1109/icse48619.2023.00172
[research_chen_2023_b]: https://doi.org/10.1038/s42256-023-00657-x
[research_chen_2024]: https://doi.org/10.1109/hpcc64274.2024.00024
[research_chen_2024_b]: https://doi.org/10.1007/s10664-024-10510-3
[research_chen_2025]: https://doi.org/10.3390/app15179523
[research_chen_2025_b]: https://doi.org/10.1145/3755881.3755899
[research_chen_2026]: https://doi.org/10.5220/0014717000004052
[research_chicote_2017]: https://doi.org/10.1109/softstart.2017.6
[research_chin_2022]: https://doi.org/10.1201/9781003187196-10
[research_chippagi_2023]: https://doi.org/10.17762/ijritcc.v11i9.11427
[research_chlipala_2015]: https://doi.org/10.1145/2784731.2784741
[research_chlipala_2015_b]: https://doi.org/10.1145/3264293
[research_choi_2021]: https://doi.org/10.1145/3484271.3484972
[research_choi_2022]: https://doi.org/10.1145/3519939.3523429
[research_choi_2026]: https://doi.org/10.1038/s41598-026-45837-y
[research_chouchen_2026]: https://doi.org/10.1145/3793302.3793381
[research_choudhury_2023]: https://doi.org/10.1145/3629523
[research_chow_2021]: https://doi.org/10.1007/978-3-030-80515-9_11
[research_chowdhury_2025]: https://doi.org/10.1109/sbft66712.2025.00016
[research_christakis_2016]: https://doi.org/10.1007/978-3-662-53413-7_6
[research_chvatal_1979]: https://doi.org/10.1287/moor.4.3.233
[research_ciano_2024]: https://doi.org/10.12988/ams.2024.919155
[research_cibir_2022]: https://doi.org/10.1109/access.2022.3172326
[research_cito_2016]: https://doi.org/10.1145/2889160.2891057
[research_clement_2021]: https://doi.org/10.1109/llvmhpc54804.2021.00007
[research_clopper_pearson_1934]: https://doi.org/10.1093/biomet/26.4.404
[research_cockx_2017]: https://doi.org/10.1145/3018610.3018612
[research_codabux_2016]: https://doi.org/10.1145/2889160.2892643
[research_codabux_2020]: https://doi.org/10.1145/3382494.3422172
[research_cohen_2018]: https://doi.org/10.1145/3196398.3196436
[research_condevaux_2023]: https://doi.org/10.1007/978-3-031-26387-3_19
[research_condorifernand_2018]: https://doi.org/10.1145/3195538.3195539
[research_conforti_cornuejols_1984]: https://doi.org/10.1016/0166-218X(84)90003-9
[research_conte_2026]: https://doi.org/10.1145/3801488.3806071
[research_conway_1963]: https://doi.org/10.1145/366663.366704
[research_coole_2015]: https://doi.org/10.1109/fccm.2015.49
[research_cooper_2023]: https://doi.org/10.1016/b978-0-12-815412-0.00010-3
[research_cooper_2023_b]: https://doi.org/10.1016/b978-0-12-815412-0.00014-0
[research_cooper_2023_c]: https://doi.org/10.1016/b978-0-12-815412-0.00011-5
[research_coppola_2020]: https://doi.org/10.1109/icstw50294.2020.00027
[research_corah_2018]: https://doi.org/10.1109/cdc.2018.8619396
[research_corah_2018_b]: https://doi.org/10.1007/s10514-018-9778-6
[research_cordeiro_2025]: https://doi.org/10.5220/0013475600003929
[research_cordeiro_2025_b]: https://doi.org/10.5220/0013456000003929
[research_corder_2019]: https://doi.org/10.1109/icmla.2019.00044
[research_corral_2026]: https://doi.org/10.1145/3801488.3806237
[research_corrias_2026]: https://doi.org/10.5220/0014597200004061
[research_costa_2018]: https://doi.org/10.1016/j.future.2016.06.014
[research_costa_2021]: https://doi.org/10.1109/sbesc53686.2021.9628230
[research_courtnage_2021]: https://doi.org/10.1007/978-3-030-88942-5_8
[research_cousot_1977]: https://doi.org/10.1145/512950.512973
[research_cousot_2015]: https://doi.org/10.1145/2790449.2790451
[research_coviello_2018]: https://doi.org/10.1145/3239235.3240497
[research_crepalde_2025]: https://doi.org/10.1145/3708493.3712681
[research_cui_2023]: https://doi.org/10.1109/access.2023.3246491
[research_cui_2023_b]: https://doi.org/10.1145/3606376.3593573
[research_cui_2024]: https://doi.org/10.1109/asap61560.2024.00021
[research_cui_2025]: https://doi.org/10.1109/dac63849.2025.11132848
[research_cui_2025_b]: https://doi.org/10.1145/3721145.3725765
[research_cui_2025_c]: https://doi.org/10.1109/eiecs67708.2025.11283571
[research_cummins_2025]: https://doi.org/10.1145/3708493.3712691
[research_curtis_2018]: https://doi.org/10.1145/3168826
[research_cynthia_2025]: https://doi.org/10.1109/esem64174.2025.00072
[research_cytron_1991]: https://doi.org/10.1145/115372.115320
[research_dahiya_2017]: https://doi.org/10.1007/978-3-319-70389-3_2
[research_dai_2017]: https://doi.org/10.1007/978-3-319-60588-3_6
[research_dantas_2019]: https://doi.org/10.18293/seke2019-141
[research_daoudi_2021]: https://doi.org/10.1007/s10664-021-09955-7
[research_daroza_2022]: https://doi.org/10.1109/saner53432.2022.00034
[research_daudier_2018]: https://doi.org/10.1007/978-3-319-90104-6_13
[research_dauksevic_2026]: https://doi.org/10.1109/icc59461.2026.11587351
[research_davidson_fraser_1984]: https://doi.org/10.1145/502874.502885
[research_dean_1992]: https://doi.org/10.1080/01621459.1992.10475225
[research_deboer_2023]: https://doi.org/10.1145/3594729
[research_debosschere_2018]: https://doi.org/10.1109/meco.2018.8405949
[research_deferriere_2026]: https://doi.org/10.1109/cgo68049.2026.11395204
[research_delatorre_2024]: https://doi.org/10.1093/jigpal/jzae069
[research_delatorre_2025]: https://doi.org/10.1145/3712255.3726624
[research_delima_2022]: https://doi.org/10.1007/s11219-021-09578-7
[research_dellanna_2022]: https://doi.org/10.1007/s10664-022-10243-1
[research_delmas_2021]: https://doi.org/10.1007/978-3-030-88806-0_5
[research_demacedo_2021]: https://doi.org/10.1109/asew52652.2021.00056
[research_demacedo_2022]: https://doi.org/10.1109/ict4s55073.2022.00014
[research_demagalhaes_2015]: https://doi.org/10.1016/j.infsof.2015.02.001
[research_demange_2016]: https://doi.org/10.1145/2892208.2892222
[research_demartino_2025]: https://doi.org/10.1016/j.jss.2025.112458
[research_demillo_1978]: https://doi.org/10.1109/C-M.1978.218136
[research_demmler_2021]: https://doi.org/10.5220/0010540500002998
[research_denaro_2025]: https://doi.org/10.1109/ast66626.2025.00012
[research_deng_2018]: https://doi.org/10.1007/s10703-017-0313-8
[research_deng_2023]: https://doi.org/10.32604/csse.2023.027680
[research_deng_2025]: https://doi.org/10.1145/3711896.3736887
[research_dennis_2024]: https://doi.org/10.5220/0012835200003767
[research_denny_2018]: https://doi.org/10.1109/llvm-hpc.2018.8639349
[research_denzler_2021]: https://doi.org/10.1109/isorc52013.2021.00019
[research_deole_2024]: https://doi.org/10.37394/23205.2024.23.19
[research_deruck_2025]: https://doi.org/10.14722/bar.2025.23014
[research_desouzamagalha_2026]: https://doi.org/10.1145/3771775.3786281
[research_detofeno_2022]: https://doi.org/10.1145/3555228.3555238
[research_dey_2023]: https://doi.org/10.1609/aaai.v37i4.25508
[research_dhahbi_2026]: https://doi.org/10.5162/iccc2026/p30
[research_diaconescu_2020]: https://doi.org/10.1007/s11787-020-00249-y
[research_diamantopoulos_2020]: https://doi.org/10.1109/fpl50879.2020.00058
[research_dickerson_2026]: https://doi.org/10.1145/3797265
[research_digiacomo_2017]: https://doi.org/10.1145/3136014.3136015
[research_ding_2016]: https://doi.org/10.1145/2896971.2896981
[research_ding_2022]: https://doi.org/10.1109/issre55969.2022.00034
[research_ding_2022_b]: https://doi.org/10.1145/3498730
[research_doerfert_2022]: https://doi.org/10.1145/3559009.3569687
[research_donaldson_2016]: https://doi.org/10.1145/2896971.2896978
[research_dong_2016]: https://doi.org/10.1109/pdcat.2016.020
[research_dong_2024]: https://doi.org/10.1109/iecon55916.2024.10905976
[research_doshi_2026]: https://doi.org/10.5220/0015043100004015
[research_dougherty_2025]: https://doi.org/10.1109/llm4code66737.2025.00014
[research_downie_2022]: https://doi.org/10.1109/cdc51059.2022.9992771
[research_drawel_2020]: https://doi.org/10.1016/j.future.2018.01.040
[research_drescher_2024]: https://doi.org/10.1145/3640537.3641567
[research_drescher_2026]: https://doi.org/10.1109/cgo68049.2026.11395203
[research_dsilva_2015]: https://doi.org/10.1109/spw.2015.33
[research_du_2026]: https://doi.org/10.1145/3796315.3796332
[research_duan_2025]: https://doi.org/10.1615/int.j.uncertaintyquantification.2024051548
[research_dubey_2023]: https://doi.org/10.1109/icccnt56998.2023.10307781
[research_ducasse_2023]: https://doi.org/10.1109/ipdpsw59300.2023.00032
[research_duijn_2015]: https://doi.org/10.1109/msr.2015.51
[research_dupontdedinech_2021]: https://doi.org/10.1007/978-3-030-80515-9_18
[research_durieux_2020]: https://doi.org/10.1145/3379597.3387460
[research_dyer_2013]: https://doi.org/10.1109/ICSE.2013.6606588
[research_dzulqarnain_2024]: https://doi.org/10.28989/compiler.v13i2.2649
[research_ebner_2021]: https://doi.org/10.1007/978-3-030-80515-9_19
[research_ecker_2017]: https://doi.org/10.1007/978-94-017-7267-9_32
[research_edbert_2023]: https://doi.org/10.1109/esem56168.2023.10304868
[research_efthymiou_2022]: https://doi.org/10.22331/q-2022-09-22-814
[research_eisenkraemer_2020]: https://doi.org/10.1109/iscas45731.2020.9180579
[research_eissa_2016]: https://doi.org/10.1109/asap.2016.7760804
[research_elbaum_2002]: https://doi.org/10.1109/32.988497
[research_elkhouly_2019]: https://doi.org/10.1145/3371236
[research_elkoutbi_2017]: https://doi.org/10.5220/0006312901950202
[research_elkoutbi_2018]: https://doi.org/10.1002/smr.2149
[research_elmohr_2016]: https://doi.org/10.1109/icm.2016.7847921
[research_enders_2023]: https://doi.org/10.14722/bar.2023.23001
[research_endo_2017]: https://doi.org/10.1145/3090634
[research_engel_2023]: https://doi.org/10.1007/978-3-031-38828-6_1
[research_engelke_2020]: https://doi.org/10.1109/llvmhpchipar51896.2020.00011
[research_engelke_2024]: https://doi.org/10.1109/cgo57630.2024.10444856
[research_eom_2024]: https://doi.org/10.1145/3650212.3680389
[research_epasto_2017]: https://doi.org/10.1145/3087556.3087574
[research_erer_2025]: https://doi.org/10.1109/esem64174.2025.00058
[research_eriksson_2016]: https://doi.org/10.5220/0005745205890599
[research_erkus_2026]: https://doi.org/10.1007/s10664-026-10844-0
[research_ertl_1999]: https://doi.org/10.1145/292540.292562
[research_esary_proschan_1963]: https://doi.org/10.1080/00401706.1963.10490075
[research_evenmendoza_2022]: https://doi.org/10.1007/s10664-022-10146-1
[research_evenmendoza_2023]: https://doi.org/10.1145/3597926.3598130
[research_fagerholm_2019]: https://doi.org/10.1109/esem.2019.8870161
[research_fahimullah_2019]: https://doi.org/10.1109/access.2019.2908459
[research_fakhir_2018]: https://doi.org/10.1109/access.2018.2849821
[research_fakhoury_2024]: https://doi.org/10.1145/3639478.3643525
[research_falk_2019]: https://doi.org/10.1007/s11241-019-09337-9
[research_fan_2023]: https://doi.org/10.1109/jbhi.2023.3248139
[research_fan_2024]: https://doi.org/10.1109/issre62328.2024.00040
[research_fan_2025]: https://doi.org/10.1109/aiita65135.2025.11047894
[research_fang_2026]: https://doi.org/10.1109/cgo68049.2026.11395239
[research_fanyizhao_2024]: https://doi.org/10.66372/jger.v2i1.1
[research_farber_2023]: https://doi.org/10.1145/3573105.3575686
[research_fedasyuk_2017]: https://doi.org/10.1109/cadsm.2017.7916134
[research_feige_1998]: https://doi.org/10.1145/285055.285059
[research_feischl_2026]: https://doi.org/10.1145/3777383
[research_felbinger_2016]: https://doi.org/10.1145/2896921.2896923
[research_felderer_2020]: https://doi.org/10.1007/978-3-030-32489-6_1
[research_feldman_2026]: https://doi.org/10.1287/moor.2023.0276
[research_felfernig_2021]: https://doi.org/10.1142/9789811239922_0002
[research_felker_2020]: https://doi.org/10.1109/sas48726.2020.9220074
[research_feng_2025]: https://doi.org/10.1145/3763152
[research_fenton_ohlsson_2000]: https://doi.org/10.1109/32.879815
[research_ferchichi_2024]: https://doi.org/10.5220/0012742000003687
[research_ferdinand_wilhelm_1999]: https://doi.org/10.1023/A:1008186323068
[research_fernandes_2025]: https://doi.org/10.1109/les.2024.3416820
[research_ferrante_1987]: https://doi.org/10.1145/24039.24041
[research_ferretti_2023]: https://doi.org/10.1109/icpc58990.2023.00027
[research_finkel_2019]: https://doi.org/10.1109/p3hpc49587.2019.00013
[research_finkel_2020]: https://doi.org/10.1109/llvmhpchipar51896.2020.00012
[research_fisman_2021]: https://doi.org/10.1007/s10703-021-00386-0
[research_flatt_2020]: https://doi.org/10.1145/3385412.3385981
[research_flemstrom_2021]: https://doi.org/10.1109/icst49551.2021.00047
[research_foundjem_2021]: https://doi.org/10.1007/s10664-020-09929-1
[research_fox_2017]: https://doi.org/10.1145/3018610.3018621
[research_frankel_2021]: https://doi.org/10.1109/bigdata52589.2021.9671332
[research_fraser_1992]: https://doi.org/10.1145/151640.151642
[research_fromherz_2018]: https://doi.org/10.1007/978-3-319-77935-5_14
[research_fu_2025]: https://doi.org/10.1109/tifs.2025.3618407
[research_fumero_2017]: https://doi.org/10.1145/3050748.3050761
[research_furia_2024]: https://doi.org/10.1007/978-3-031-75380-0_8
[research_furia_2026]: https://doi.org/10.1007/s10664-026-10851-1
[research_gaceanu_2024]: https://doi.org/10.1109/saner-c62648.2024.00030
[research_galanis_2020]: https://doi.org/10.5220/0009826604300437
[research_gan_2020]: https://doi.org/10.1587/transinf.2019edp7150
[research_gao_2022]: https://doi.org/10.1109/icis54925.2022.9882453
[research_gao_2026]: https://doi.org/10.1145/3820771
[research_garciaalvarado_2020]: https://doi.org/10.1109/bigdata50022.2020.9378481
[research_garg_2024]: https://doi.org/10.1109/ccis63231.2024.10932075
[research_garmsirinejad_2025]: https://doi.org/10.1109/dese68208.2025.11367830
[research_garoche_2019]: https://doi.org/10.23943/princeton/9780691181301.003.0009
[research_garridolucero_2024]: https://doi.org/10.52202/079017-0063
[research_garzella_2020]: https://doi.org/10.1007/978-3-030-39322-9_5
[research_gascon_2017]: https://doi.org/10.1007/978-3-319-63390-9_5
[research_gautam_2017]: https://doi.org/10.1109/msr.2017.38
[research_gauthier_2024]: https://doi.org/10.1145/3644033.3644380
[research_gay_2023]: https://doi.org/10.1109/icst57152.2023.00021
[research_gayatri_2024]: https://doi.org/10.1109/hipc62374.2024.00035
[research_gebreyesus_2023]: https://doi.org/10.3390/fi15030088
[research_geeson_2024]: https://doi.org/10.1109/cgo57630.2024.10444836
[research_georgakoudis_2025]: https://doi.org/10.1145/3696443.3708939
[research_georges_2007]: https://doi.org/10.1145/1297027.1297033
[research_georgiou_2020]: https://doi.org/10.1093/comjnl/bxaa103
[research_ghaleb_2019]: https://doi.org/10.1007/s10664-019-09695-9
[research_ghammam_2026]: https://doi.org/10.1145/3793302.3793563
[research_ghanbari_2017]: https://doi.org/10.1109/esem.2017.53
[research_gharesifard_2016]: https://doi.org/10.1109/acc.2016.7525053
[research_ghorbani_2022]: https://doi.org/10.1109/ieeeconf56349.2022.10064696
[research_ghotra_2017]: https://doi.org/10.1109/msr.2017.18
[research_giamattei_2024]: https://doi.org/10.1007/s10664-024-10562-5
[research_gilot_2026]: https://doi.org/10.1145/3798203
[research_ginsbach_2018]: https://doi.org/10.1145/3178372.3179515
[research_girault_2025]: https://doi.org/10.1145/3768311
[research_glanville_graham_1978]: https://doi.org/10.1145/512760.512785
[research_gliwa_2021]: https://doi.org/10.1007/978-3-030-64144-3_6
[research_gliwa_2021_b]: https://doi.org/10.1007/978-3-030-64144-3_5
[research_godboley_2022]: https://doi.org/10.5220/0011032900003176
[research_goli_2022]: https://doi.org/10.3934/jimo.2021124
[research_golla_2024]: https://doi.org/10.1007/s11219-024-09667-3
[research_golnari_2015]: https://doi.org/10.1109/iccad.2015.7372582
[research_gomes_2024]: https://doi.org/10.5753/jserd.2024.3591
[research_gomezlondono_2020]: https://doi.org/10.1145/3428272
[research_goncalvesdossa_2025]: https://doi.org/10.4204/eptcs.436.5
[research_gong_2021]: https://doi.org/10.1007/978-3-030-92681-6_55
[research_gong_2024]: https://doi.org/10.26599/tst.2023.9010026
[research_gong_2026]: https://doi.org/10.1007/s10664-026-10819-1
[research_gonzalezbaraho_2023]: https://doi.org/10.1016/j.infsof.2023.107318
[research_gopinath_2022]: https://doi.org/10.1002/stvr.1830
[research_gorius_2026]: https://doi.org/10.1145/3801488.3807478
[research_gosevapopstoja_2017]: https://doi.org/10.1109/issre.2017.42
[research_gote_2019]: https://doi.org/10.1109/msr.2019.00070
[research_gourdin_2023]: https://doi.org/10.1145/3622799
[research_gourdin_2023_b]: https://doi.org/10.1145/3605158.3605848
[research_graics_2023]: https://doi.org/10.1002/sys.21675
[research_gratien_2020]: https://doi.org/10.1109/llvmhpchipar51896.2020.00014
[research_greiler_2015]: https://doi.org/10.1109/msr.2015.8
[research_gretz_2020]: https://doi.org/10.1109/fdl50818.2020.9232942
[research_gromova_2016]: https://doi.org/10.1007/978-3-319-43838-2_4
[research_grossman_2002]: https://doi.org/10.1145/512529.512563
[research_grotov_2022]: https://doi.org/10.1145/3524842.3528447
[research_gruber_2021]: https://doi.org/10.1109/icst49551.2021.00026
[research_guan_2016]: https://doi.org/10.1007/978-3-319-27198-9_3
[research_guan_2016_b]: https://doi.org/10.1007/978-3-319-27198-9_2
[research_guckel_2025]: https://doi.org/10.1002/net.70003
[research_guizzo_2023]: https://doi.org/10.1007/s10664-023-10333-8
[research_guleria_2024]: https://doi.org/10.1007/s00521-024-09861-1
[research_gunadi_2015]: https://doi.org/10.1109/iceccs.2015.36
[research_guo_2022]: https://doi.org/10.1145/3559009.3569683
[research_guo_2026]: https://doi.org/10.1145/3797125
[research_guo_2026_b]: https://doi.org/10.1016/j.tcs.2026.116037
[research_gupta_2021]: https://doi.org/10.4018/ijsi.2021010104
[research_gupta_2023]: https://doi.org/10.4108/eetsis.4346
[research_gussoni_2019]: https://doi.org/10.14722/bar.2019.23093
[research_gustafson_1988]: https://doi.org/10.1145/42411.42415
[research_habchi_2022]: https://doi.org/10.1109/icst53961.2022.00034
[research_hafizhah_2024]: https://doi.org/10.28989/compiler.v13i2.2685
[research_haghighatkhah_2018]: https://doi.org/10.1016/j.jss.2018.08.061
[research_haidlmichael_2016]: https://doi.org/10.3233/978-1-61499-621-7-247
[research_hajyihia_2015]: https://doi.org/10.1145/2685393
[research_hakimi_2025]: https://doi.org/10.1145/3727638
[research_haler_2021]: https://doi.org/10.1145/3503921.3503924
[research_hall_2017]: https://doi.org/10.1007/978-3-319-52709-3_9
[research_hallahan_2025]: https://doi.org/10.1145/3720505
[research_halmans_2026]: https://doi.org/10.1145/3793302.3793305
[research_hamasaki_2026]: https://doi.org/10.7759/cureus.107791
[research_hamdi_2026]: https://doi.org/10.3897/jucs.171035
[research_hammadi_2017]: https://doi.org/10.1109/syseng.2017.8088306
[research_hammer_2025]: https://doi.org/10.1109/access.2025.3615249
[research_han_2021]: https://doi.org/10.1109/pact52795.2021.00014
[research_han_2021_b]: https://doi.org/10.1109/candarw53999.2021.00022
[research_han_2023]: https://doi.org/10.2991/978-94-6463-262-0_99
[research_han_2024]: https://doi.org/10.1109/cgo57630.2024.10444865
[research_han_2024_b]: https://doi.org/10.1145/3640537.3641582
[research_hanley_1983]: https://doi.org/10.1001/jama.1983.03330370053031
[research_hanson_1990]: https://doi.org/10.1002/spe.4380200104
[research_haque_2020]: https://doi.org/10.5935/jetia.v6i25.692
[research_harif_2025]: https://doi.org/10.1007/978-3-032-07106-4_12
[research_hariri_2019]: https://doi.org/10.1109/icst.2019.00021
[research_harrold_1993]: https://doi.org/10.1145/152388.152391
[research_hartel_2023]: https://doi.org/10.1007/s10664-023-10370-3
[research_hartley_2022]: https://doi.org/10.1145/3546568
[research_hasabnis_2015]: https://doi.org/10.1109/cgo.2015.7054197
[research_hasabnis_2016]: https://doi.org/10.1145/2954679.2872380
[research_hashemi_2022]: https://doi.org/10.1109/icsme55016.2022.00011
[research_hashemi_2025]: https://doi.org/10.1109/icst62969.2025.10989021
[research_hatahet_2025]: https://doi.org/10.1109/models-c68889.2025.00080
[research_hausladen_2017]: https://doi.org/10.1115/detc2017-67402
[research_hawkins_2017]: https://doi.org/10.1109/dsn.2017.27
[research_hayashi_2015]: https://doi.org/10.1145/2833157.2833164
[research_hayashi_2016]: https://doi.org/10.1109/waccpd.2016.011
[research_he_2023]: https://doi.org/10.1145/3585341.3585359
[research_he_2024]: https://doi.org/10.14711/dataset/9zoato
[research_he_2025]: https://doi.org/10.1109/saner64311.2025.00032
[research_heckel_2023]: https://doi.org/10.1145/3583133.3596380
[research_heidariiman_2025]: https://doi.org/10.1007/978-3-031-90410-3_6
[research_heidariiman_2025_b]: https://doi.org/10.1007/978-3-031-90410-3_4
[research_heim_2018]: https://doi.org/10.1145/3178372.3183636
[research_helmke_2021]: https://doi.org/10.1109/pst52912.2021.9647801
[research_heo_2015]: https://doi.org/10.1145/2746238
[research_hepola_2022]: https://doi.org/10.1109/asap54787.2022.00034
[research_hepola_2024]: https://doi.org/10.1109/norcas64408.2024.10752475
[research_herber_2025]: https://doi.org/10.1109/vissoft67405.2025.00010
[research_herbold_2016]: https://doi.org/10.1007/s10664-016-9468-y
[research_herbold_2020]: https://doi.org/10.1145/3379597.3387504
[research_herdt_2019]: https://doi.org/10.23919/date.2019.8714912
[research_hesselbarth_2015]: https://doi.org/10.1109/dasip.2015.7367249
[research_hilbig_2021]: https://doi.org/10.1145/3442381.3450138
[research_himschoot_2020]: https://doi.org/10.1007/978-1-4842-6592-5_8
[research_himschoot_2020_b]: https://doi.org/10.1007/978-1-4842-6592-5_3
[research_hindle_2018]: https://doi.org/10.1007/s10664-018-9643-4
[research_hjort_2018]: https://doi.org/10.1007/978-3-319-89719-6_8
[research_hodovan_2026]: https://doi.org/10.1109/saner-c67878.2026.00055
[research_holl_2025]: https://doi.org/10.1109/fllm67465.2025.11390916
[research_hongbo_2015]: https://doi.org/10.1515/9781501503146-015
[research_hora_2022]: https://doi.org/10.1007/s10664-022-10259-7
[research_hora_2026]: https://doi.org/10.1145/3793654.3793752
[research_hora_2026_b]: https://doi.org/10.1145/3793302.3793327
[research_horikawa_2025]: https://doi.org/10.1109/icsme64153.2025.00079
[research_horvath_2015]: https://doi.org/10.1016/j.mejo.2015.01.001
[research_hosseini_2018]: https://doi.org/10.1016/j.infsof.2017.06.004
[research_hosseini_2022]: https://doi.org/10.14722/bar.2022.23009
[research_hsu_2018]: https://doi.org/10.14722/bar.2018.23014
[research_hu_2018]: https://doi.org/10.1109/isdfs.2018.8355364
[research_hu_2020]: https://doi.org/10.1145/3395631
[research_hu_2020_b]: https://doi.org/10.1145/3385412.3385979
[research_hu_2020_c]: https://doi.org/10.1007/s10664-019-09799-2
[research_hu_2021]: https://doi.org/10.1109/icet51757.2021.9450911
[research_hu_2025]: https://doi.org/10.1007/s10664-025-10777-0
[research_hu_2026]: https://doi.org/10.1016/j.sysarc.2026.103926
[research_hu_2026_b]: https://doi.org/10.3724/zrht.1674-5825.2025039
[research_hu_2026_c]: https://doi.org/10.1016/j.infsof.2025.107978
[research_huang_2017]: https://doi.org/10.1109/compsac.2017.271
[research_huang_2017_b]: https://doi.org/10.1007/s10664-017-9522-4
[research_huang_2019]: https://doi.org/10.1109/asap.2019.00-36
[research_huang_2019_b]: https://doi.org/10.1109/fccm.2019.00049
[research_huang_2021]: https://doi.org/10.1007/s00224-021-10065-6
[research_huang_2024]: https://doi.org/10.1109/ccai61966.2024.10602841
[research_huang_2024_b]: https://doi.org/10.1007/s00453-024-01272-x
[research_huang_2025]: https://doi.org/10.1109/icse55347.2025.00030
[research_huang_2026]: https://doi.org/10.1109/fccm68464.2026.00052
[research_huang_2026_b]: https://doi.org/10.1007/s10664-026-10874-8
[research_huck_2018]: https://doi.org/10.1109/correctness.2018.00011
[research_huck_2020]: https://doi.org/10.1109/correctness51934.2020.00010
[research_humbatova_2021]: https://doi.org/10.1145/3460319.3464825
[research_humbatova_2023]: https://doi.org/10.1109/icse-companion58688.2023.00027
[research_hupel_2018]: https://doi.org/10.1007/978-3-319-89884-1_35
[research_hussein_2021]: https://doi.org/10.1109/ase51524.2021.9678548
[research_hwang_2025]: https://doi.org/10.1109/access.2025.3561135
[research_ibrahim_2024]: https://doi.org/10.1109/icm63406.2024.10815826
[research_ibriwesh_2018]: https://doi.org/10.1177/1063293x18808559
[research_idri_2015]: https://doi.org/10.1002/int.21748
[research_idri_2016]: https://doi.org/10.5220/0005822701320139
[research_idri_2017]: https://doi.org/10.1002/smr.1925
[research_ilesanmi_2021]: https://doi.org/10.21276/ijircst.2021.9.5.5
[research_imai_2021]: https://doi.org/10.1109/issrew53611.2021.00081
[research_imianosky_2023]: https://doi.org/10.1109/dft59622.2023.10313569
[research_imianosky_2024]: https://doi.org/10.1109/dft63277.2024.10753524
[research_imianosky_2025]: https://doi.org/10.1109/iwasi66786.2025.11121981
[research_imran_2024]: https://doi.org/10.1145/3661167.3661196
[research_imran_2025]: https://doi.org/10.1007/s10664-025-10712-3
[research_inozemtseva_holmes_2014]: https://doi.org/10.1145/2568225.2568271
[research_ioannidis_2005]: https://doi.org/10.1371/journal.pmed.0020124
[research_iqbal_2022]: https://doi.org/10.1145/3530019.3531331
[research_iqbal_2024]: https://doi.org/10.30537/sjet.v7i1.1428
[research_ishimoto_2024]: https://doi.org/10.1109/apsec65559.2024.00015
[research_ishimura_2022]: https://doi.org/10.1109/candarw57323.2022.00082
[research_islam_2023]: https://doi.org/10.1145/3597031.3597047
[research_ismael_2018]: https://doi.org/10.1109/scee.2018.8684137
[research_israel_2024]: https://doi.org/10.1109/cict64037.2024.10899652
[research_italiano_2025]: https://doi.org/10.1145/3708493.3712686
[research_izawa_2022]: https://doi.org/10.5381/jot.2022.21.2.a1
[research_jahanshahi_2025]: https://doi.org/10.1109/msr66628.2025.00032
[research_jain_2021]: https://doi.org/10.1007/978-1-4842-7496-5_2
[research_jain_2023]: https://doi.org/10.1007/s12046-023-02304-y
[research_jakhar_2015]: https://doi.org/10.14257/ijmue.2015.10.2.09
[research_jamieson_2021]: https://doi.org/10.1145/3446804.3446853
[research_jamil_2025]: https://doi.org/10.1109/msr66628.2025.00081
[research_jaoua_2025]: https://doi.org/10.1109/msr66628.2025.00038
[research_jarman_2017]: https://doi.org/10.1109/met.2017.1
[research_jaskirat_2026]: https://doi.org/10.23940/ijpe.26.04.p2.188199
[research_jayatilaka_2021]: https://doi.org/10.1145/3458744.3473355
[research_jehan_2023]: https://doi.org/10.1109/access.2023.3289073
[research_jensen_1906]: https://doi.org/10.1007/BF02418571
[research_jensen_2022]: https://doi.org/10.5220/0010838700003116
[research_jesus_2024]: https://doi.org/10.1145/3673038.3673104
[research_jeyaram_2025]: https://doi.org/10.1504/ijpqm.2025.150888
[research_jha_2023]: https://doi.org/10.1109/icst57152.2023.00057
[research_ji_2025]: https://doi.org/10.1145/3728938
[research_jia_harman_2011]: https://doi.org/10.1109/TSE.2010.62
[research_jian_2026]: https://doi.org/10.1145/3774895.3812195
[research_jiang_2015]: https://doi.org/10.1109/msr.2015.12
[research_jiang_2023]: https://doi.org/10.1109/bigdata59044.2023.10386972
[research_jiang_2025]: https://doi.org/10.1109/saner64311.2025.00078
[research_jiang_2025_b]: https://doi.org/10.1109/msr66628.2025.00075
[research_jiao_2019]: https://doi.org/10.1007/978-3-030-32409-4_35
[research_jiao_2021]: https://doi.org/10.1109/smc52423.2021.9658643
[research_jimoh_2026]: https://doi.org/10.1364/cleo_si.2026.sw2d.7
[research_jin_2026]: https://doi.org/10.1007/s10107-026-02346-0
[research_jitsunari_2019]: https://doi.org/10.1109/icstw.2019.00065
[research_johnson_1974]: https://doi.org/10.1016/s0022-0000(74)80044-9
[research_johnson_2023]: https://doi.org/10.1109/sp46215.2023.10179357
[research_johnson_2025]: https://doi.org/10.5220/0013176200003899
[research_johnston_2018]: https://doi.org/10.1109/llvm-hpc.2018.8639381
[research_jones_2016]: https://doi.org/10.1145/2955811.2955812
[research_jones_2023]: https://doi.org/10.1049/icp.2023.3273
[research_jorgensen_2018]: https://doi.org/10.1201/b15980-7
[research_journault_2016]: https://doi.org/10.1007/978-3-662-53413-7_13
[research_jovanovic_levy_1997]: https://doi.org/10.1080/00031305.1997.10473947
[research_jureczko_2020]: https://doi.org/10.1049/iet-sen.2020.0134
[research_just_2014]: https://doi.org/10.1145/2635868.2635929
[research_kadam_2022]: https://doi.org/10.14569/ijacsa.2022.0131068
[research_kadarkarai_2025]: https://doi.org/10.1109/icacrs67045.2025.11324142
[research_kaestner_2025]: https://doi.org/10.4271/2025-01-0155
[research_kakarla_2024]: https://doi.org/10.1145/3656385
[research_kakati_2025]: https://doi.org/10.5220/0013203200003950
[research_kaliszyk_2023]: https://doi.org/10.1145/3573105.3579108
[research_kalle_2019]: https://doi.org/10.14722/bar.2019.23074
[research_kamil_2016]: https://doi.org/10.1145/2908080.2908117
[research_kamkin_2024]: https://doi.org/10.15514/ispras-2024-36(5)-3
[research_kanabar_2023]: https://doi.org/10.1145/3591259
[research_kanemoto_2026]: https://doi.org/10.1109/access.2026.3698914
[research_kang_2018]: https://doi.org/10.1145/3192366.3192377
[research_kang_2022]: https://doi.org/10.1145/3524459.3527343
[research_kang_2023]: https://doi.org/10.1145/3586039
[research_kang_2025]: https://doi.org/10.1145/3774899.3775011
[research_kao_2025]: https://doi.org/10.1007/979-8-8688-1769-4_13
[research_kapitsaki_2024]: https://doi.org/10.1145/3674805.3686681
[research_karadeniz_2025]: https://doi.org/10.1109/icmlt65785.2025.11193186
[research_karampatsis_2020]: https://doi.org/10.1145/3377811.3380342
[research_karathanasopou_2024]: https://doi.org/10.1016/j.istruc.2024.106206
[research_karim_2017]: https://doi.org/10.1109/iwesep.2017.17
[research_karlsson_ryan_1997]: https://doi.org/10.1109/52.605933
[research_karp_1972]: https://doi.org/10.1007/978-1-4684-2001-2_9
[research_karuppusamy_2020]: https://doi.org/10.36548/jscp.2020.2.001
[research_katel_2022]: https://doi.org/10.1145/3497776.3517770
[research_kaur_2022]: https://doi.org/10.31449/inf.v46i8.4197
[research_kellison_2022]: https://doi.org/10.1145/3497775.3503682
[research_kellison_2022_b]: https://doi.org/10.1109/correctness56720.2022.00007
[research_kennedy_2025]: https://doi.org/10.1109/csr64739.2025.11130090
[research_khaldi_2015]: https://doi.org/10.1145/2833157.2833158
[research_khaldi_2016]: https://doi.org/10.1109/llvm-hpc.2016.007
[research_khaldi_2021]: https://doi.org/10.1109/llvmhpc54804.2021.00008
[research_khalufa_2019]: https://doi.org/10.1109/pact.2019.00052
[research_khan_2022]: https://doi.org/10.1007/978-981-19-3148-2_34
[research_khan_2024]: https://doi.org/10.1145/3644032.3644467
[research_khan_2025]: https://doi.org/10.1109/iccd65941.2025.00088
[research_khan_2026]: https://doi.org/10.1145/3748522.3780033
[research_khanneh_2022]: https://doi.org/10.3390/software1040019
[research_khuller_1999]: https://doi.org/10.1016/S0020-0190(99)00031-9
[research_kia_2026]: https://doi.org/10.1016/b978-0-443-14081-5.00090-8
[research_kiamtan_2019]: https://doi.org/10.1017/s0956796818000229
[research_kido_2015]: https://doi.org/10.1007/978-3-662-49122-5_11
[research_kildall_1973]: https://doi.org/10.1145/512927.512945
[research_kim_2017]: https://doi.org/10.1201/b11716-31
[research_kim_2019]: https://doi.org/10.1109/cgo.2019.8661172
[research_kim_2021]: https://doi.org/10.1109/cgo51591.2021.9370341
[research_kim_2023]: https://doi.org/10.1109/icst57152.2023.00053
[research_kim_2024]: https://doi.org/10.1109/isocc62682.2024.10762325
[research_kim_2024_b]: https://doi.org/10.1016/j.cose.2024.103904
[research_kim_2025]: https://doi.org/10.1109/access.2025.3539584
[research_kimura_2019]: https://doi.org/10.1109/candarw.2019.00082
[research_kimura_2021]: https://doi.org/10.1145/3468081.3471061
[research_kingslystephen_2025]: https://doi.org/10.4018/979-8-3693-7352-1.ch001
[research_kintis_2017]: https://doi.org/10.1007/s10664-017-9582-5
[research_kitchenham_2019]: https://doi.org/10.1007/s10664-019-09747-0
[research_klemmer_2022]: https://doi.org/10.1145/3526241.3530388
[research_klemmer_2022_b]: https://doi.org/10.1109/fdl56239.2022.9925662
[research_klemmer_2025]: https://doi.org/10.1007/978-3-031-83093-8_4
[research_knoop_2017]: https://doi.org/10.1016/j.jsc.2016.07.023
[research_knuth_1971]: https://doi.org/10.1002/spe.4380010203
[research_ko_2026]: https://doi.org/10.1145/3771775.3786278
[research_koana_2024]: https://doi.org/10.1007/s10664-024-10538-5
[research_kochberger_2023]: https://doi.org/10.5220/0012167000003555
[research_kochhar_2015]: https://doi.org/10.1109/saner.2015.7081877
[research_koehler_2021]: https://doi.org/10.1109/cgo51591.2021.9370337
[research_koitzhristov_2022]: https://doi.org/10.1145/3524481.3527216
[research_kongarana_2026]: https://doi.org/10.1109/access.2026.3683914
[research_konsaard_2015]: https://doi.org/10.1109/icissec.2015.7371038
[research_korkut_2026]: https://doi.org/10.1145/3779031.3779091
[research_kosar_2018]: https://doi.org/10.1007/s10664-017-9593-2
[research_kostin_2017]: https://doi.org/10.1190/segam2017-17443086.1
[research_koutcheme_2024]: https://doi.org/10.1145/3657604.3664665
[research_koutsoumpas_2015]: https://doi.org/10.4204/eptcs.178.6
[research_kovacevic_2022]: https://doi.org/10.1016/j.cola.2022.101105
[research_kozanidis_2022]: https://doi.org/10.1145/3544902.3546245
[research_koziolek_2024]: https://doi.org/10.1145/3643795.3648385
[research_kruse_2018]: https://doi.org/10.1109/llvm-hpc.2018.8639402
[research_ksontini_2021]: https://doi.org/10.1109/ase51524.2021.9678585
[research_kumar_2014]: https://doi.org/10.1145/2535838.2535841
[research_kumar_2021]: https://doi.org/10.1109/dasc52595.2021.9594326
[research_kumar_2024]: https://doi.org/10.1109/access.2024.3379018
[research_kumar_2024_b]: https://doi.org/10.35444/ijana.2024.15609
[research_kumar_2026]: https://doi.org/10.1109/icvadv67766.2026.11470391
[research_kumari_2018]: https://doi.org/10.1007/s00542-018-3871-9
[research_kuncar_2015]: https://doi.org/10.1145/2676724.2693175
[research_kuo_2023]: https://doi.org/10.1109/taes.2023.3266314
[research_kuriakose_2015]: https://doi.org/10.1109/empire.2015.7431307
[research_kuroki_2024]: https://doi.org/10.1109/icip51287.2024.10647574
[research_kurudirek_2025]: https://doi.org/10.28989/compiler.v14i1.2819
[research_kusumaningrum_2015]: https://doi.org/10.28989/compiler.v4i2.92
[research_kusumaningrum_2021]: https://doi.org/10.28989/compiler.v10i2.1111
[research_kusumaningrum_2022]: https://doi.org/10.28989/compiler.v11i1.1231
[research_kwon_2016]: https://doi.org/10.9708/jksci.2016.21.11.159
[research_kwon_2022]: https://doi.org/10.1109/isocc56007.2022.10031488
[research_kwon_2024]: https://doi.org/10.1145/3597503.3639189
[research_kwon_2025]: https://doi.org/10.1145/3729275
[research_kwon_2026]: https://doi.org/10.1109/cgo68049.2026.11395240
[research_laaber_2021]: https://doi.org/10.1007/s10664-021-10037-x
[research_laboudi_2025]: https://doi.org/10.1142/s0218194025500482
[research_lachmann_2016]: https://doi.org/10.1109/icmla.2016.0065
[research_lachmann_2018]: https://doi.org/10.5162/ettc2018/12.4
[research_lage_2019]: https://doi.org/10.1109/esem.2019.8870180
[research_laguna_2024]: https://doi.org/10.1109/scw63240.2024.00080
[research_lai_2021]: https://doi.org/10.1145/3458744.3473348
[research_lai_2022]: https://doi.org/10.1145/3547276.3548518
[research_lai_2023]: https://doi.org/10.1145/3605731.3605904
[research_laiq_2024]: https://doi.org/10.1007/s10664-024-10502-3
[research_lam_2020]: https://doi.org/10.1145/3377811.3381749
[research_lambert_2017]: https://doi.org/10.1145/3115936.3115943
[research_lammich_2024]: https://doi.org/10.1007/s10817-024-09701-w
[research_lan_2025]: https://doi.org/10.1145/3731599.3767530
[research_lancellotti_2026]: https://doi.org/10.1145/3748522.3779947
[research_lancellotti_2026_b]: https://doi.org/10.1109/asp-dac66049.2026.11420750
[research_landi_1992]: https://doi.org/10.1145/161494.161501
[research_larose_2026]: https://doi.org/10.5381/jot.2026.25.1.a15
[research_laskurain_2025]: https://doi.org/10.1109/flta67013.2025.11336639
[research_lasnier_2026]: https://doi.org/10.1145/3779031.3779098
[research_lasnier_2026_b]: https://doi.org/10.1145/3747413
[research_lasser_2021]: https://doi.org/10.1145/3453483.3454053
[research_latifis_2016]: https://doi.org/10.3850/9783981537079_0426
[research_latifis_2017]: https://doi.org/10.1145/2996182
[research_lattner_2021]: https://doi.org/10.1109/cgo51591.2021.9370308
[research_lattner_adve_2004]: https://doi.org/10.1109/CGO.2004.1281665
[research_laurent_2017]: https://doi.org/10.1109/icst.2017.47
[research_lauwaerts_2024]: https://doi.org/10.1016/j.cola.2024.101268
[research_lavazza_2017]: https://doi.org/10.1145/3084226.3084260
[research_lavazza_2020]: https://doi.org/10.1145/3382494.3410691
[research_le_2014]: https://doi.org/10.1145/2594291.2594334
[research_le_2015]: https://doi.org/10.1145/2858965.2814319
[research_lecoeur_2023]: https://doi.org/10.1145/3591294
[research_ledilavrec_2025]: https://doi.org/10.1109/msr66628.2025.00079
[research_lee_2017]: https://doi.org/10.1145/3140587.3062343
[research_lee_2018]: https://doi.org/10.1145/3276495
[research_lee_2019]: https://doi.org/10.1109/platcon.2019.8669419
[research_lee_2019_b]: https://doi.org/10.1007/978-3-030-25543-5_25
[research_lee_2022]: https://doi.org/10.1109/icst53961.2022.00032
[research_lefeuvre_2026]: https://doi.org/10.1145/3793302.3793369
[research_lehmann_2025]: https://doi.org/10.23919/date64628.2025.10992765
[research_lei_2018]: https://doi.org/10.1016/j.procs.2018.04.202
[research_lei_2025]: https://doi.org/10.1145/3733823.3764514
[research_leidel_2021]: https://doi.org/10.1109/llvmhpc54804.2021.00010
[research_leinen_2024]: https://doi.org/10.1109/icst60714.2024.00037
[research_lenarduzzi_2019]: https://doi.org/10.1109/esem.2019.8870169
[research_lenarduzzi_2021]: https://doi.org/10.1016/j.jss.2020.110827
[research_leopoldseder_2018]: https://doi.org/10.1145/3168811
[research_leopoldseder_2018_b]: https://doi.org/10.1145/3281287.3281290
[research_leroy_2003]: https://doi.org/10.1023/A:1025055424017
[research_leroy_2009]: https://doi.org/10.1145/1538788.1538814
[research_letras_2025]: https://doi.org/10.1109/qce65121.2025.10288
[research_leven_2024]: https://doi.org/10.1007/s10664-024-10456-6
[research_li_2015]: https://doi.org/10.1109/icstw.2015.7107453
[research_li_2016]: https://doi.org/10.1145/2934872.2959061
[research_li_2017]: https://doi.org/10.1145/3132479.3132487
[research_li_2019]: https://doi.org/10.2991/msbda-19.2019.25
[research_li_2021]: https://doi.org/10.1109/spw53761.2021.00028
[research_li_2021_b]: https://doi.org/10.1109/compsac51774.2021.00132
[research_li_2022]: https://doi.org/10.1145/3510003.3510217
[research_li_2022_b]: https://doi.org/10.1109/qrs57517.2022.00028
[research_li_2022_c]: https://doi.org/10.1007/s10664-021-10082-6
[research_li_2022_d]: https://doi.org/10.1007/s10664-022-10128-3
[research_li_2023]: https://doi.org/10.1007/s11432-022-3727-6
[research_li_2023_b]: https://doi.org/10.1007/s11390-023-1266-6
[research_li_2023_c]: https://doi.org/10.1145/3582016.3582053
[research_li_2023_d]: https://doi.org/10.1109/isctis58954.2023.10213091
[research_li_2023_e]: https://doi.org/10.1002/stvr.1864
[research_li_2023_f]: https://doi.org/10.1007/s10664-023-10297-9
[research_li_2024]: https://doi.org/10.1109/icfpt64416.2024.11113451
[research_li_2024_b]: https://doi.org/10.1145/3656386
[research_li_2024_c]: https://doi.org/10.1007/s43684-023-00060-8
[research_li_2024_d]: https://doi.org/10.1109/isctis63324.2024.10698980
[research_li_2025]: https://doi.org/10.1109/icbats66542.2025.11258097
[research_li_2025_b]: https://doi.org/10.1016/j.cose.2025.104660
[research_li_2025_c]: https://doi.org/10.1109/qrs-c65679.2025.00031
[research_li_2025_d]: https://doi.org/10.1109/ase63991.2025.00228
[research_li_2025_e]: https://doi.org/10.1142/s0218194025500792
[research_li_2025_f]: https://doi.org/10.1109/bigdata66926.2025.11401593
[research_li_2025_g]: https://doi.org/10.1016/j.knosys.2025.114002
[research_li_2025_h]: https://doi.org/10.1145/3727648.3727682
[research_li_2025_i]: https://doi.org/10.1145/3715004
[research_li_2025_j]: https://doi.org/10.1002/ett.70232
[research_li_2025_k]: https://doi.org/10.1145/3723890.3723908
[research_li_2026]: https://doi.org/10.3390/computers15070406
[research_li_2026_b]: https://doi.org/10.1109/tkde.2026.3651564
[research_li_2026_c]: https://doi.org/10.1007/s10664-026-10932-1
[research_li_malik_1995]: https://doi.org/10.1145/217474.217570
[research_liang_2018]: https://doi.org/10.1145/3180155.3180213
[research_liang_2025]: https://doi.org/10.1109/ase63991.2025.00059
[research_liang_2025_b]: https://doi.org/10.1145/3696443.3708955
[research_liang_2026]: https://doi.org/10.1080/20964471.2026.2689760
[research_liao_2020]: https://doi.org/10.1155/2020/8814247
[research_lidbury_2015]: https://doi.org/10.1145/2737924.2737986
[research_lim_2023]: https://doi.org/10.1145/3578360.3580260
[research_lima_2020]: https://doi.org/10.1145/3382025.3414967
[research_lima_2020_b]: https://doi.org/10.1145/3425174.3425210
[research_lima_2022]: https://doi.org/10.1109/tse.2020.2992428
[research_lima_2023]: https://doi.org/10.5753/jserd.2023.2142
[research_lin_2021]: https://doi.org/10.1109/sp40001.2021.00006
[research_lin_2021_b]: https://doi.org/10.1109/correctness54621.2021.00011
[research_lin_2022]: https://doi.org/10.1007/s10664-022-10173-y
[research_lin_2025]: https://doi.org/10.1007/s10515-025-00568-8
[research_lion_2026]: https://doi.org/10.1109/facct71761.2026.00011
[research_listiawan_2024]: https://doi.org/10.28989/compiler.v13i1.2111
[research_liu_2016]: https://doi.org/10.1007/978-3-319-41135-4_7
[research_liu_2017]: https://doi.org/10.1016/j.ces.2017.07.006
[research_liu_2018]: https://doi.org/10.1007/s10664-018-9611-z
[research_liu_2020]: https://doi.org/10.1145/3416506.3423579
[research_liu_2020_b]: https://doi.org/10.1145/3395363.3397370
[research_liu_2021]: https://doi.org/10.1109/cgo51591.2021.9370310
[research_liu_2021_b]: https://doi.org/10.1088/2632-2153/ac0167
[research_liu_2021_c]: https://doi.org/10.1109/ijcnn52387.2021.9533729
[research_liu_2022]: https://doi.org/10.1109/iccece54139.2022.9712838
[research_liu_2022_b]: https://doi.org/10.1007/s10878-022-00975-7
[research_liu_2022_c]: https://doi.org/10.3390/electronics11152452
[research_liu_2023]: https://doi.org/10.1186/s42400-023-00164-x
[research_liu_2023_b]: https://doi.org/10.52202/075280-0943
[research_liu_2024]: https://doi.org/10.1145/3675018.3675029
[research_liu_2024_b]: https://doi.org/10.1145/3656390
[research_liu_2024_c]: https://doi.org/10.1145/3691620.3695074
[research_liu_2024_d]: https://doi.org/10.1117/12.3038243
[research_liu_2025]: https://doi.org/10.1145/3742872.3757073
[research_liu_2025_b]: https://doi.org/10.1145/3712197
[research_liu_2025_c]: https://doi.org/10.3390/app15115935
[research_liu_2025_d]: https://doi.org/10.1007/s11219-025-09728-1
[research_liu_2025_e]: https://doi.org/10.1109/ijcnn64981.2025.11228000
[research_liu_layland_1973]: https://doi.org/10.1145/321738.321743
[research_lochbihler_2018]: https://doi.org/10.1007/s10817-018-9452-x
[research_longchar_2025]: https://doi.org/10.1109/aimlsystems67835.2025.11330892
[research_loose_2026]: https://doi.org/10.1145/3786155.3788582
[research_loow_2019]: https://doi.org/10.1145/3314221.3314622
[research_loow_2021]: https://doi.org/10.1145/3437992.3439916
[research_lopes_2021]: https://doi.org/10.1145/3453483.3454030
[research_lovasz_1983]: https://doi.org/10.1007/978-3-642-68874-4_10
[research_lowther_2023]: https://doi.org/10.1145/3623507.3623552
[research_lozachmeur_2023]: https://doi.org/10.1109/mwscas57524.2023.10405991
[research_lozov_2023]: https://doi.org/10.1007/978-3-031-45784-5_8
[research_lu_2021]: https://doi.org/10.1145/3444685.3446285
[research_lu_2022]: https://doi.org/10.22152/programming-journal.org/2023/7/2
[research_lu_2024]: https://doi.org/10.1109/qrs62785.2024.00058
[research_lu_2025]: https://doi.org/10.1109/tr.2025.3614352
[research_lu_2026]: https://doi.org/10.1145/3798251
[research_lu_2026_b]: https://doi.org/10.1109/tpami.2025.3626404
[research_luan_2025]: https://doi.org/10.1109/isset66828.2025.11184959
[research_lucke_2021]: https://doi.org/10.1145/3446804.3446844
[research_lucke_2025]: https://doi.org/10.1145/3696443.3708922
[research_lund_yannakakis_1994]: https://doi.org/10.1145/185675.306789
[research_luo_2016]: https://doi.org/10.1145/2901739.2901765
[research_luo_2016_b]: https://doi.org/10.1145/2950290.2950344
[research_luo_2019]: https://doi.org/10.24963/ijcai.2019/251
[research_luo_2023]: https://doi.org/10.1109/tifs.2023.3289254
[research_luo_2024]: https://doi.org/10.1145/3626246.3654680
[research_luo_2026]: https://doi.org/10.1007/978-3-032-22774-4_8
[research_luppen_2021]: https://doi.org/10.2514/6.2021-0997
[research_luppen_2021_b]: https://doi.org/10.2514/6.2021-0997.c1
[research_luu_2022]: https://doi.org/10.1145/3524846.3527341
[research_lv_2026]: https://doi.org/10.1587/elex.23.20260182
[research_lyu_2021]: https://doi.org/10.3390/electronics10161921
[research_lyu_2023]: https://doi.org/10.1007/978-1-4842-9331-7_4
[research_ma_2015]: https://doi.org/10.1109/ast.2015.23
[research_ma_2022]: https://doi.org/10.1007/978-3-031-05484-6_109
[research_ma_2023]: https://doi.org/10.1145/3597926.3598053
[research_ma_2023_b]: https://doi.org/10.1117/12.2685759
[research_ma_2025]: https://doi.org/10.1145/3747912.3747940
[research_machacek_2025]: https://doi.org/10.1109/icsme64153.2025.00042
[research_madeiral_2021]: https://doi.org/10.1109/msr52588.2021.00064
[research_madkour_2024]: https://doi.org/10.1145/3649921.3656986
[research_maeng_2024]: https://doi.org/10.1145/3640537.3641564
[research_maesbermejo_2022]: https://doi.org/10.1007/s10664-022-10117-6
[research_mahathevan_2026]: https://doi.org/10.14722/fuzzing.2026.23006
[research_mahida_2021]: https://doi.org/10.21275/sr24314131827
[research_mahmood_2020]: https://doi.org/10.1109/icecce49384.2020.9179279
[research_mahmood_2021]: https://doi.org/10.1002/spe.3009
[research_mahmoudi_2025]: https://doi.org/10.1109/telfor67910.2025.11314213
[research_maia_2026]: https://doi.org/10.1145/3806383.3815520
[research_maier_2022]: https://doi.org/10.14722/bar.2022.23008
[research_maipradit_2020]: https://doi.org/10.1007/s10664-020-09854-3
[research_maipradit_2021]: https://doi.org/10.1007/s10664-021-09939-7
[research_maisto_2022]: https://doi.org/10.23919/date54114.2022.9774501
[research_maity_2026]: https://doi.org/10.1145/3778361
[research_majeti_2016]: https://doi.org/10.1145/2892208.2892210
[research_majumder_2025]: https://doi.org/10.1145/3769002.3769975
[research_majumder_2026]: https://doi.org/10.1109/airc69745.2026.11631461
[research_mamata_2023]: https://doi.org/10.1109/ast58925.2023.00023
[research_mammadli_2020]: https://doi.org/10.1109/llvmhpchipar51896.2020.00006
[research_mandal_2015]: https://doi.org/10.1109/icce.2015.7066465
[research_manglaviti_2017]: https://doi.org/10.1109/msr.2017.31
[research_mao_2023]: https://doi.org/10.1109/ccai57533.2023.10201266
[research_marbukh_2022]: https://doi.org/10.1109/ipsn54338.2022.00060
[research_marcelino_2023]: https://doi.org/10.1145/3583740.3626611
[research_marcelino_2025]: https://doi.org/10.1145/3770501.3770515
[research_marcelli_2025]: https://doi.org/10.3390/electronics14193924
[research_marchetto_2019]: https://doi.org/10.1109/tse.2017.2777831
[research_marijan_2023]: https://doi.org/10.1007/s11219-023-09646-0
[research_maron_2016]: https://doi.org/10.1109/iceta.2016.7802074
[research_marsad_2026]: https://doi.org/10.1145/3793302.3793313
[research_martin_2025]: https://doi.org/10.64804/t6yn4h63
[research_martinjeremymr_2019]: https://doi.org/10.3233/978-1-61499-949-2-491
[research_martins_2016]: https://doi.org/10.1145/2883614
[research_martins_2020]: https://doi.org/10.5220/0009410601400147
[research_martins_2024]: https://doi.org/10.1007/s10664-024-10577-y
[research_mashchenko_2017]: https://doi.org/10.1007/s10559-017-9944-4
[research_masoudi_2025]: https://doi.org/10.1145/3696630.3731465
[research_massalin_1987]: https://doi.org/10.1145/36206.36194
[research_massidda_2024]: https://doi.org/10.5220/0012852400003767
[research_masten_2018]: https://doi.org/10.1109/llvm-hpc.2018.8639483
[research_mastroeni_2017]: https://doi.org/10.1007/978-3-319-66706-5_12
[research_matsubara_2023]: https://doi.org/10.1007/s10664-023-10332-9
[research_matsubara_2025]: https://doi.org/10.1109/candarw68385.2025.00013
[research_matteordonelli_2025]: https://doi.org/10.36676/jmk.v5.i2.93
[research_mazurek_2020]: https://doi.org/10.1109/icarcv50220.2020.9305396
[research_mazurowski_2024]: https://doi.org/10.1201/9781003574958-13
[research_mckee_2023]: https://doi.org/10.14722/bar.2023.23003
[research_mcmillan_2016]: https://doi.org/10.1109/fmcad.2016.7886668
[research_mece_2020]: https://doi.org/10.24018/ejece.2020.4.1.128
[research_meehl_1967]: https://doi.org/10.1086/288135
[research_mehta_2023]: https://doi.org/10.1145/3573105.3575689
[research_melo_2016]: https://doi.org/10.1109/asap.2016.7760808
[research_melquiond_2024]: https://doi.org/10.1145/3674629
[research_menendez_2016]: https://doi.org/10.1007/978-3-662-53413-7_16
[research_menendez_2016_b]: https://doi.org/10.1145/2884781.2884809
[research_menendez_2017]: https://doi.org/10.1145/3140587.3062372
[research_menetrey_2021]: https://doi.org/10.1109/icde51399.2021.00025
[research_menetrey_2022]: https://doi.org/10.1109/icdcs54860.2022.00116
[research_menetrey_2024]: https://doi.org/10.1109/tdsc.2023.3334516
[research_meng_2020]: https://doi.org/10.1109/cicn49253.2020.9242624
[research_menolli_2021]: https://doi.org/10.5220/0010442802750282
[research_mensah_2018]: https://doi.org/10.1016/j.jss.2017.09.026
[research_menzies_2016]: https://doi.org/10.1007/s10664-016-9472-2
[research_merazga_2025]: https://doi.org/10.48084/etasr.10990
[research_merz_2019]: https://doi.org/10.1145/3335772.3335780
[research_meshveliani_2020]: https://doi.org/10.1134/s0361768820020073
[research_meywerk_2023]: https://doi.org/10.5220/0011630600003393
[research_mezouar_2017]: https://doi.org/10.1007/s10664-017-9559-4
[research_mguidich_2016]: https://doi.org/10.1109/rtss.2016.051
[research_mi_2018]: https://doi.org/10.1016/j.infsof.2018.03.006
[research_mills_2020]: https://doi.org/10.1007/s10664-020-09823-w
[research_mine_2017]: https://doi.org/10.1561/2500000034
[research_minku_2019]: https://doi.org/10.1007/s10664-019-09686-w
[research_mirrokni_2015]: https://doi.org/10.1145/2746539.2746624
[research_mirzaei_2022]: https://doi.org/10.1109/cfis54774.2022.9756464
[research_mirzasoleiman_2018]: https://doi.org/10.1609/aaai.v32i1.11529
[research_mishra_2022]: https://doi.org/10.1145/3563310
[research_mitsch_2016]: https://doi.org/10.1007/s10703-016-0241-z
[research_miyamoto_2024]: https://doi.org/10.56238/sevened2024.025-014
[research_mochizuki_2024]: https://doi.org/10.1145/3679007.3685062
[research_mogensen_2017]: https://doi.org/10.1007/978-3-319-66966-3_6
[research_mogensen_2017_b]: https://doi.org/10.1007/978-3-319-66966-3_7
[research_mogensen_2024]: https://doi.org/10.1007/978-3-031-46460-7_6
[research_mogensen_2024_b]: https://doi.org/10.1007/978-3-031-46460-7_7
[research_moldovan_2026]: https://doi.org/10.5220/0014803700004015
[research_molnar_2020]: https://doi.org/10.1145/3382494.3410673
[research_molnar_2022]: https://doi.org/10.5220/0011073600003176
[research_mondal_2015]: https://doi.org/10.1109/icst.2015.7102588
[research_mondal_2017]: https://doi.org/10.1109/icsme.2017.33
[research_mondal_2022]: https://doi.org/10.1007/s10664-021-10113-2
[research_monicacatherin_2015]: https://doi.org/10.1109/eesco.2015.7254018
[research_monniaux_2022]: https://doi.org/10.1007/978-3-030-99336-8_8
[research_monniaux_2023]: https://doi.org/10.1007/978-981-19-9601-6_6
[research_monniaux_2024]: https://doi.org/10.1145/3636501.3636952
[research_moore_2019]: https://doi.org/10.5220/0007678100150026
[research_moreno_2016]: https://doi.org/10.3850/9783981537079_0829
[research_mori_2017]: https://doi.org/10.1109/icstw.2017.78
[research_moriconi_2025]: https://doi.org/10.1109/msr66628.2025.00104
[research_moron_2023]: https://doi.org/10.1109/meco58584.2023.10155088
[research_moron_2025]: https://doi.org/10.1145/3736169
[research_morovati_2023]: https://doi.org/10.1007/s10664-023-10400-0
[research_morton_2020]: https://doi.org/10.1609/aaai.v34i02.5522
[research_mosel_2018]: https://doi.org/10.1093/oxfordhb/9780190610029.013.14
[research_mosin_2015]: https://doi.org/10.1109/ewdts.2015.7493152
[research_moss_2016]: https://doi.org/10.1109/llvm-hpc.2016.009
[research_moura_ierusalimschy_2009]: https://doi.org/10.1145/1462166.1462167
[research_moussa_2025]: https://doi.org/10.1109/ase63991.2025.00396
[research_mpeis_2022]: https://doi.org/10.1145/3517338
[research_ms_2018]: https://doi.org/10.14419/ijet.v7i4.36.23809
[research_mshanmuganatha_2018]: https://doi.org/10.17577/ijertcon091
[research_mu_2023]: https://doi.org/10.1145/3578360.3580255
[research_mukherjee_2020]: https://doi.org/10.1145/3428245
[research_mullen_2016]: https://doi.org/10.1145/2980983.2908109
[research_muller_2026]: https://doi.org/10.1109/saner67736.2026.00045
[research_munafo_2017]: https://doi.org/10.1038/s41562-016-0021
[research_munezero_2026]: https://doi.org/10.1109/iccss69952.2026.11593309
[research_muros_2019]: https://doi.org/10.1007/978-3-030-10489-4_4
[research_musco_2016]: https://doi.org/10.1007/s11219-016-9332-8
[research_muse_2022]: https://doi.org/10.1007/s10664-022-10119-4
[research_mushtaq_2015]: https://doi.org/10.1109/patmos.2015.7347584
[research_myreen_2021]: https://doi.org/10.1145/3437992.3439915
[research_mytkowicz_2009]: https://doi.org/10.1145/1508284.1508275
[research_mzid_2022]: https://doi.org/10.5220/0010821700003119
[research_na_2016]: https://doi.org/10.1145/2846098
[research_nadimi_2024]: https://doi.org/10.1109/lad62341.2024.10691683
[research_nagy_2019]: https://doi.org/10.1109/sp.2019.00069
[research_nagy_2021]: https://doi.org/10.1145/3460120.3484787
[research_nakamura_2016]: https://doi.org/10.1109/apccas.2016.7804063
[research_nakamura_2026]: https://doi.org/10.1145/3786791
[research_nakanishi_2025]: https://doi.org/10.21125/inted.2025.0016
[research_nakao_2020]: https://doi.org/10.1007/978-981-15-7683-6_2
[research_nakata_2025]: https://doi.org/10.1145/3774898.3778040
[research_namjoshi_2021]: https://doi.org/10.1007/978-3-030-67067-2_7
[research_nannipieri_2021]: https://doi.org/10.1109/access.2021.3126208
[research_nasui_2026]: https://doi.org/10.5220/0014936200004015
[research_naufalmaulana_2022]: https://doi.org/10.1109/icitisee57756.2022.10057944
[research_nayebi_2015]: https://doi.org/10.5430/air.v4n2p45
[research_nazar_2016]: https://doi.org/10.63317/55dbkcxk94vf
[research_ndlovu_2024]: https://doi.org/10.1109/zcict63770.2024.10958234
[research_necula_1997]: https://doi.org/10.1145/263699.263712
[research_necula_lee_1998]: https://doi.org/10.1145/277650.277752
[research_neis_2015]: https://doi.org/10.1145/2858949.2784764
[research_nemhauser_1978]: https://doi.org/10.1007/BF01588971
[research_nemhauser_wolsey_1978b]: https://doi.org/10.1287/moor.3.3.177
[research_nery_2015]: https://doi.org/10.1007/s10470-015-0585-0
[research_neumuller_2026]: https://doi.org/10.1109/saner67736.2026.00068
[research_nezamabadi_2026]: https://doi.org/10.1145/3779031.3779092
[research_ngadiyono_2015]: https://doi.org/10.28989/compiler.v4i1.88
[research_ngo_2015]: https://doi.org/10.1145/2764967.2775291
[research_nguyen_2015]: https://doi.org/10.1109/icse.2015.336
[research_nguyen_2016]: https://doi.org/10.1145/2901739.2901759
[research_nguyen_2017]: https://doi.org/10.1145/3106237.3106281
[research_nguyen_2019]: https://doi.org/10.1109/ase.2019.00072
[research_nguyen_2020]: https://doi.org/10.1109/correctness51934.2020.00009
[research_nguyen_2021]: https://doi.org/10.1109/llvmhpc54804.2021.00011
[research_ni_2025]: https://doi.org/10.1145/3763079
[research_ni_2025_b]: https://doi.org/10.1145/3758316.3763251
[research_nielebock_2021]: https://doi.org/10.1109/msr52588.2021.00069
[research_niharika_2025]: https://doi.org/10.38124/ijisrt/25jul468
[research_nikiforova_2022]: https://doi.org/10.5220/0011032700003176
[research_nikith_2024]: https://doi.org/10.1109/i2ct61223.2024.10543642
[research_nipkow_2020]: https://doi.org/10.1145/3372885.3373834
[research_niu_2024]: https://doi.org/10.1007/s10664-024-10537-6
[research_noack_2017]: https://doi.org/10.1007/978-3-319-67630-2_29
[research_nobre_2016]: https://doi.org/10.1145/2980930.2907959
[research_nobre_2019]: https://doi.org/10.1016/j.softx.2019.100238
[research_nogueira_2025]: https://doi.org/10.1109/issre66568.2025.00036
[research_nolasco_2026]: https://doi.org/10.1109/icst69053.2026.00016
[research_nong_2024]: https://doi.org/10.1007/s40305-023-00525-w
[research_nongpoh_2022]: https://doi.org/10.14722/fuzzing.2022.23007
[research_notzli_2016]: https://doi.org/10.1145/2931021.2931024
[research_novielli_2021]: https://doi.org/10.1007/s10664-021-09960-w
[research_nozaki_2024]: https://doi.org/10.1145/3665283.3665343
[research_nunes_2025]: https://doi.org/10.1109/vlsi-soc64688.2025.11421728
[research_nunes_2025_b]: https://doi.org/10.1109/iscas56072.2025.11043225
[research_nunes_2026]: https://doi.org/10.1109/tc.2026.3700461
[research_obrien_2022]: https://doi.org/10.1145/3540250.3549088
[research_ochoa_2022]: https://doi.org/10.1007/s10664-021-10052-y
[research_odim_2023]: https://doi.org/10.26821/ijshre.11.5.2023.110409
[research_ogenrwot_2026]: https://doi.org/10.1145/3793302.3793603
[research_oh_2015]: https://doi.org/10.7873/date.2015.0927
[research_oh_2016]: https://doi.org/10.18587/bh.2016.12.77.331
[research_oh_2023]: https://doi.org/10.1109/access.2023.3276411
[research_oh_2026]: https://doi.org/10.1145/3803525.3804981
[research_ojdanic_2023]: https://doi.org/10.1109/tse.2023.3277564
[research_okawara_2025]: https://doi.org/10.1109/candarw68385.2025.00065
[research_oliveira_2020]: https://doi.org/10.5753/sbesc_estendido.2020.13102
[research_oliveira_2025]: https://doi.org/10.1109/esem64174.2025.00073
[research_oliveiraneto_2015]: https://doi.org/10.1109/icse.2015.197
[research_olsson_2021]: https://doi.org/10.1007/s10664-021-09998-w
[research_orgard_2023]: https://doi.org/10.1109/icstw58534.2023.00063
[research_oskin_2015]: https://doi.org/10.1109/pact.2015.30
[research_ostrand_weyuker_2002]: https://doi.org/10.1145/566172.566181
[research_ostrand_weyuker_2005]: https://doi.org/10.1109/tse.2005.49
[research_ottoni_2018]: https://doi.org/10.1145/3192366.3192374
[research_owen_1972]: https://doi.org/10.1287/mnsc.18.5.64
[research_ozdemir_2022]: https://doi.org/10.1109/sp46214.2022.9833782
[research_ozen_2018]: https://doi.org/10.1109/llvm-hpc.2018.8639434
[research_ozkilbac_2022]: https://doi.org/10.18185/erzifbed.1077921
[research_padhi_2017]: https://doi.org/10.1190/segam2017-17587724.1
[research_padhi_2019]: https://doi.org/10.1190/segam2019-3216245.1
[research_palomba_2019]: https://doi.org/10.1007/s10664-019-09683-z
[research_palomba_2020]: https://doi.org/10.1007/s10664-020-09821-y
[research_pan_2021]: https://doi.org/10.1007/s10664-021-10066-6
[research_pan_2025]: https://doi.org/10.52202/085713-2951
[research_pan_2025_b]: https://doi.org/10.18293/seke2025-076
[research_pandey_2024]: https://doi.org/10.1109/icccmla63077.2024.10871813
[research_pang_2017]: https://doi.org/10.1109/isocc.2017.8368818
[research_panigrahi_2023]: https://doi.org/10.1109/tcad.2023.3269954
[research_papadakis_2018]: https://doi.org/10.1145/3180155.3180183
[research_papadimitriou_2021]: https://doi.org/10.1145/3453933.3454014
[research_papoudakis_2022]: https://doi.org/10.5220/0011279300003266
[research_paraman_2023]: https://doi.org/10.11591/ijeecs.v29.i2.pp990-1005
[research_parihar_2015]: https://doi.org/10.1109/pact.2015.55
[research_parihar_2017]: https://doi.org/10.1109/pact.2017.35
[research_park_2015]: https://doi.org/10.1109/estimedia.2015.7351768
[research_park_2017]: https://doi.org/10.1145/3125501.3125512
[research_park_2018]: https://doi.org/10.1145/3291056
[research_park_2022]: https://doi.org/10.3390/s22041392
[research_park_2022_b]: https://doi.org/10.1109/cgo53902.2022.9741263
[research_park_2023]: https://doi.org/10.1109/tse.2023.3241639
[research_park_2025]: https://doi.org/10.1109/isocc66390.2025.11329603
[research_parra_2026]: https://doi.org/10.1016/j.envsoft.2026.107102
[research_parry_2022]: https://doi.org/10.1145/3524481.3527227
[research_parsert_2024]: https://doi.org/10.1609/aaai.v38i9.28938
[research_pasareanu_2019]: https://doi.org/10.1016/bs.adcom.2018.10.004
[research_pascarella_2017]: https://doi.org/10.1109/msr.2017.63
[research_patel_2025]: https://doi.org/10.1145/3696443.3708919
[research_patil_2015]: https://doi.org/10.1109/indin.2015.7281905
[research_patil_2018]: https://doi.org/10.14299/ijser.2018.08.04
[research_patricio_2026]: https://doi.org/10.1016/j.infsof.2026.108238
[research_patsidis_2018]: https://doi.org/10.1016/j.micpro.2018.05.007
[research_patte_2025]: https://doi.org/10.1109/formalise66629.2025.00021
[research_pattyn_2025]: https://doi.org/10.1109/iwsib66663.2025.00006
[research_pattyn_2026]: https://doi.org/10.3390/computers15020117
[research_pauley_2022]: https://doi.org/10.1109/cns56114.2022.9947273
[research_pavlidakis_2024]: https://doi.org/10.1145/3704440.3704782
[research_peccia_2025]: https://doi.org/10.1109/iccad66269.2025.11241007
[research_pecimuth_2023]: https://doi.org/10.1145/3618305.3623593
[research_pei_2025]: https://doi.org/10.1109/icst62969.2025.10989030
[research_peker_2023]: https://doi.org/10.1145/3625223.3649273
[research_pelayobenedet_2026]: https://doi.org/10.14722/bar.2026.23077
[research_peng_2023]: https://doi.org/10.1145/3578360.3580259
[research_peng_2025]: https://doi.org/10.1109/llm4code66737.2025.00009
[research_peng_2026]: https://doi.org/10.1109/lcsys.2026.3670932
[research_perezalvarez_2022]: https://doi.org/10.1109/icse-seis55304.2022.9793869
[research_perezpiqueras_2025]: https://doi.org/10.5220/0013229800003928
[research_peta_2025]: https://doi.org/10.1109/wconf64849.2025.11233456
[research_petchartee_2025]: https://doi.org/10.1109/icsec67360.2025.11298108
[research_petrogalli_2018]: https://doi.org/10.1109/llvm-hpc.2018.8639354
[research_petrovic_2018]: https://doi.org/10.1109/icstw.2018.00027
[research_petrovic_2018_b]: https://doi.org/10.1145/3183519.3183521
[research_phan_2022]: https://doi.org/10.1145/3544902.3546248
[research_phannachitta_2016]: https://doi.org/10.1007/s10664-016-9434-8
[research_phannachitta_2026]: https://doi.org/10.1007/s11219-026-09758-3
[research_phippscostin_2021]: https://doi.org/10.1145/3485488
[research_pichler_2023]: https://doi.org/10.1145/3623507.3623554
[research_pietri_2020]: https://doi.org/10.1145/3379597.3387510
[research_pimentel_2019]: https://doi.org/10.1109/msr.2019.00077
[research_pimentel_2021]: https://doi.org/10.1007/s10664-021-09961-9
[research_pina_2021]: https://doi.org/10.1109/seaa53835.2021.00034
[research_pina_2022]: https://doi.org/10.1145/3524843.3528096
[research_pinckney_2023]: https://doi.org/10.1109/msr59073.2023.00073
[research_pinto_2015]: https://doi.org/10.1016/j.jss.2015.04.064
[research_pircher_2021]: https://doi.org/10.1109/isqed51717.2021.9424273
[research_pirkelbauer_2025]: https://doi.org/10.1007/978-3-032-07612-0_25
[research_pizard_2024]: https://doi.org/10.1007/s10664-024-10545-6
[research_pizzolotto_2020]: https://doi.org/10.1109/icsme46990.2020.00031
[research_pizzolotto_2021]: https://doi.org/10.1109/access.2021.3132950
[research_plangger_2016]: https://doi.org/10.1145/2906363.2906384
[research_pnueli_1998]: https://doi.org/10.1007/BFb0054170
[research_pokharel_2021]: https://doi.org/10.3390/wevj12030094
[research_polikarpova_2018]: https://doi.org/10.1007/s00165-017-0435-1
[research_poorhosseini_2020]: https://doi.org/10.1109/coins49042.2020.9191411
[research_pop_2016]: https://doi.org/10.1007/978-3-319-23072-6_12
[research_popovic_2015]: https://doi.org/10.1049/iet-sen.2014.0254
[research_poreba_2026]: https://doi.org/10.1007/s10664-025-10739-6
[research_porpodas_2017]: https://doi.org/10.1109/pact.2017.21
[research_postema_2022]: https://doi.org/10.1109/icst53961.2022.00042
[research_prabhu_2017]: https://doi.org/10.1177/1094342017695444
[research_pradolima_2020]: https://doi.org/10.1016/j.infsof.2020.106268
[research_pradolima_2022]: https://doi.org/10.1007/s10664-021-10093-3
[research_priamo_2026]: https://doi.org/10.1109/cgo68049.2026.11395191
[research_programming_2025]: https://doi.org/10.1155/scpr/9801273
[research_proy_2017]: https://doi.org/10.1145/3141234
[research_puffitsch_2016]: https://doi.org/10.1109/ecrts.2016.23
[research_puri_2016]: https://doi.org/10.70729/ijser15755
[research_puschner_burns_2000]: https://doi.org/10.1023/A:1008119029962
[research_pushpa_2022]: https://doi.org/10.1002/cpe.7532
[research_puspaningrum_2021]: https://doi.org/10.30595/juita.v9i2.10511
[research_putra_2024]: https://doi.org/10.28989/compiler.v13i2.2653
[research_qasim_2015]: https://doi.org/10.17485/ijst/2015/v8i16/55160
[research_qian_2022]: https://doi.org/10.1145/3545258.3545285
[research_qian_2024]: https://doi.org/10.1145/3689788
[research_qian_2025]: https://doi.org/10.1145/3728877
[research_qian_2026]: https://doi.org/10.1109/cgo68049.2026.11395228
[research_qian_2026_b]: https://doi.org/10.1038/s41467-026-69675-8
[research_qin_2024]: https://doi.org/10.1109/ispass61541.2024.00047
[research_qin_2026]: https://doi.org/10.1109/icst69053.2026.00023
[research_qu_2026]: https://doi.org/10.25300/misq/2025/18502
[research_queirozjunior_2015]: https://doi.org/10.5220/0005380605040515
[research_quetschlich_2023]: https://doi.org/10.1109/dac56929.2023.10248002
[research_quetschlich_2023_b]: https://doi.org/10.1109/qce57702.2023.00091
[research_quiring_2021]: https://doi.org/10.1145/3544885.3544889
[research_raghuraman_2024]: https://doi.org/10.1109/incet61516.2024.10593223
[research_rahman_2021]: https://doi.org/10.1007/s10664-021-10022-4
[research_rahman_2024]: https://doi.org/10.1145/3597503.3639115
[research_rahman_2025]: https://doi.org/10.1109/icse55347.2025.00178
[research_rahmani_2021]: https://doi.org/10.1145/3485535
[research_rajbhandari_2016]: https://doi.org/10.1109/sc.2016.39
[research_rajendran_2025]: https://doi.org/10.1109/punecon67554.2025.11379283
[research_ramakrishnan_2025]: https://doi.org/10.21275/sr25813194634
[research_ramler_2017]: https://doi.org/10.1145/3019612.3019830
[research_ranzato_2016]: https://doi.org/10.1007/978-3-662-53413-7_20
[research_rao_2020]: https://doi.org/10.1109/icccnt49239.2020.9225578
[research_rapoport_2017]: https://doi.org/10.1145/3133870
[research_raunak_2021]: https://doi.org/10.1109/met52542.2021.00015
[research_raveduttilucio_2025]: https://doi.org/10.1177/10943420251405928
[research_raveendran_2016]: https://doi.org/10.1109/vlsi-sata.2016.7593047
[research_rawat_2024]: https://doi.org/10.1201/9781003457152-5
[research_ray_2014]: https://doi.org/10.1145/2635868.2635922
[research_ray_2017]: https://doi.org/10.1145/3126905
[research_razi_2025]: https://doi.org/10.1109/icscds65426.2025.11167624
[research_razilov_2022]: https://doi.org/10.1109/iwcmc55113.2022.9824961
[research_reboucasdealme_2019]: https://doi.org/10.1109/icsme.2019.00096
[research_reboucasdealme_2019_b]: https://doi.org/10.1109/icsme.2019.00028
[research_reddy_2026]: https://doi.org/10.1109/cgo68049.2026.11394845
[research_refnaldi_2019]: https://doi.org/10.2991/icoelt-18.2019.27
[research_regehr_2005]: https://doi.org/10.1145/1113830.1113833
[research_reijers_2019]: https://doi.org/10.1145/3341170
[research_reineke_2007]: https://doi.org/10.1007/s11241-007-9032-3
[research_reis_2017]: https://doi.org/10.1145/3078155.3078186
[research_reiter_2025]: https://doi.org/10.1109/tdsc.2024.3482413
[research_resmi_2019]: https://doi.org/10.1515/jisys-2019-0023
[research_rezazadeh_2022]: https://doi.org/10.1109/cdc51059.2022.9992452
[research_rezazadeh_2023]: https://doi.org/10.1016/j.automatica.2023.111000
[research_rezgui_2021]: https://doi.org/10.18653/v1/2021.inlg-1.27
[research_ribeiro_2023]: https://doi.org/10.1145/3618305.3623587
[research_rice_1953]: https://doi.org/10.1090/S0002-9947-1953-0053041-6
[research_richards_2010]: https://doi.org/10.1145/1806596.1806598
[research_richards_2025]: https://doi.org/10.1145/3721089
[research_ridoy_2024]: https://doi.org/10.1109/bigdata62323.2024.10825609
[research_riener_2016]: https://doi.org/10.1109/ivsw.2016.7566605
[research_rinard_2026]: https://doi.org/10.1145/3819802.3820579
[research_rivera_2021]: https://doi.org/10.1109/cgo51591.2021.9370307
[research_rivera_2022]: https://doi.org/10.1109/cgo53902.2022.9741286
[research_rizqullah_2026]: https://doi.org/10.1109/access.2026.3662817
[research_rizvi_2015]: https://doi.org/10.5121/ijcsa.2015.5603
[research_rizwan_2017]: https://doi.org/10.1145/3178212.3178221
[research_rk_2021]: https://doi.org/10.1109/mcsoc51149.2021.00024
[research_robatishirzad_2024]: https://doi.org/10.1007/s10664-023-10437-1
[research_robles_2022]: https://doi.org/10.1007/s10664-022-10166-x
[research_rocca_2025]: https://doi.org/10.1109/wimob66857.2025.11257512
[research_rodeghero_2016]: https://doi.org/10.1002/smr.1773
[research_rodrigues_2025]: https://doi.org/10.46586/tches.v2025.i4.711-736
[research_rodriguezferra_2023]: https://doi.org/10.1145/3631483.3631502
[research_rodriguezperez_2018]: https://doi.org/10.1016/j.infsof.2018.03.009
[research_rodruksa_2017]: https://doi.org/10.1109/jcsse.2017.8025943
[research_rohr_2017]: https://doi.org/10.1109/cluster.2017.101
[research_rojas_2016]: https://doi.org/10.1007/s10664-015-9424-2
[research_rojas_2022]: https://doi.org/10.1109/access.2022.3230152
[research_rokotyanskaya_2023]: https://doi.org/10.24143/2072-9502-2023-2-93-100
[research_romano_2021]: https://doi.org/10.1109/icse43902.2021.00141
[research_romano_2023]: https://doi.org/10.1145/3543507.3583235
[research_romano_2023_b]: https://doi.org/10.1145/3611643.3616311
[research_rooijakkers_2026]: https://doi.org/10.5220/0014327000004061
[research_rosenthal_1979]: https://doi.org/10.1037/0033-2909.86.3.638
[research_roshan_2025]: https://doi.org/10.1109/ic3it66137.2025.11341145
[research_rossi_2022]: https://doi.org/10.1145/3524842.3528471
[research_rostum_2026]: https://doi.org/10.1109/iccc71363.2026.11593248
[research_roth_2024]: https://doi.org/10.1016/j.xcrp.2024.102110
[research_rothermel_2001]: https://doi.org/10.1109/32.962562
[research_rothermel_harrold_1997]: https://doi.org/10.1145/248233.248262
[research_rouson_2022]: https://doi.org/10.1109/llvm-hpc56686.2022.00009
[research_roza_2024]: https://doi.org/10.1016/j.infsof.2024.107444
[research_roze_2017]: https://doi.org/10.22184/1992-4178.2017.164.4.72.79
[research_rua_2019]: https://doi.org/10.1109/msr.2019.00035
[research_ruep_2022]: https://doi.org/10.1109/ets54262.2022.9810421
[research_saad_2024]: https://doi.org/10.1145/3639476.3639774
[research_sabou_2020]: https://doi.org/10.1007/978-3-030-32489-6_7
[research_sadaei_2023]: https://doi.org/10.1142/9789811286421_0007
[research_sadiq_2017]: https://doi.org/10.1109/ciact.2017.7977366
[research_saha_2018]: https://doi.org/10.1145/3193977.3193982
[research_saillard_2022]: https://doi.org/10.1109/correctness56720.2022.00008
[research_sajati_2017]: https://doi.org/10.28989/compiler.v6i2.228
[research_salehi_2022]: https://doi.org/10.1016/j.comnet.2021.108744
[research_salim_2019]: https://doi.org/10.1145/3359061.3362780
[research_samaana_2025]: https://doi.org/10.1007/s10664-025-10648-8
[research_samal_2019]: https://doi.org/10.1109/icitaet47105.2019.9170210
[research_samiei_2024]: https://doi.org/10.1109/cascon62161.2024.10838116
[research_sandbergericss_2017]: https://doi.org/10.1007/978-3-319-66107-0_28
[research_sandbergericss_2018]: https://doi.org/10.1007/s10817-018-9487-z
[research_santhi_2015]: https://doi.org/10.1109/wsc.2015.7408405
[research_santinelli_2017]: https://doi.org/10.1007/978-3-319-69483-2_4
[research_santos_2024]: https://doi.org/10.3390/make6010016
[research_santos_2024_b]: https://doi.org/10.1145/3638249
[research_santos_2024_c]: https://doi.org/10.1145/3643788.3648012
[research_sanusi_2024]: https://doi.org/10.1145/3686614.3686622
[research_saputra_2020]: https://doi.org/10.28989/compiler.v9i1.656
[research_saputro_2025]: https://doi.org/10.30871/jaic.v9i6.10901
[research_sarker_2025]: https://doi.org/10.1109/icst62969.2025.10988990
[research_sasano_2020]: https://doi.org/10.1145/3372884.3373158
[research_satapathy_2017]: https://doi.org/10.1145/3021460.3021468
[research_savary_2025]: https://doi.org/10.1109/asap65064.2025.00019
[research_sawant_2024]: https://doi.org/10.1109/aitest62860.2024.00027
[research_sawasdee_2025]: https://doi.org/10.1145/3789037.3789048
[research_scheidgen_2017]: https://doi.org/10.5220/0006127303290336
[research_scheidl_2020]: https://doi.org/10.1109/iccece49321.2020.9231154
[research_schkufza_2013]: https://doi.org/10.1145/2451116.2451150
[research_schkufza_2019]: https://doi.org/10.1145/3297858.3304010
[research_schlagl_2025]: https://doi.org/10.23919/date64628.2025.10992929
[research_schnakenbeck_2023]: https://doi.org/10.1109/indin51400.2023.10218176
[research_schoch_2022]: https://doi.org/10.52202/068431-2505
[research_schroeder_2025]: https://doi.org/10.1109/ftw66604.2025.00010
[research_schuiki_2020]: https://doi.org/10.1145/3385412.3386024
[research_schuiki_2020_b]: https://doi.org/10.1145/3395654
[research_schulmann_2026]: https://doi.org/10.1109/sp63933.2026.00188
[research_schulte_2018]: https://doi.org/10.14722/bar.2018.23008
[research_schulte_2026]: https://doi.org/10.1007/s10664-026-10822-6
[research_schwarz_2026]: https://doi.org/10.1109/cgo68049.2026.11395208
[research_scott_2020]: https://doi.org/10.1007/978-3-030-32489-6_8
[research_seddiki_2026]: https://doi.org/10.1145/3771775.3786269
[research_seeker_2024]: https://doi.org/10.1109/cgo57630.2024.10444847
[research_segall_2020]: https://doi.org/10.4018/978-1-7998-2768-9.ch002
[research_seidler_2026]: https://doi.org/10.1109/rtas68450.2026.00024
[research_seitzer_2015]: https://doi.org/10.1007/978-3-319-24177-7_19
[research_seo_2016]: https://doi.org/10.1109/icis.2016.7550831
[research_seo_2018]: https://doi.org/10.1109/ccta.2018.8511628
[research_serrano_2019]: https://doi.org/10.1515/comp-2019-0002
[research_serrano_2022]: https://doi.org/10.1145/3546918.3560825
[research_sethi_ullman_1970]: https://doi.org/10.1145/321607.321620
[research_sewell_2013]: https://doi.org/10.1145/2491956.2462183
[research_sghaier_2025]: https://doi.org/10.1109/msr66628.2025.00039
[research_shafigh_2021]: https://doi.org/10.1145/3475716.3484193
[research_shah_2020]: https://doi.org/10.1109/llvmhpchipar51896.2020.00015
[research_shah_2024]: https://doi.org/10.1007/s10664-024-10579-w
[research_shahzad_2022]: https://doi.org/10.1109/llvm-hpc56686.2022.00007
[research_shaikhha_2024]: https://doi.org/10.1109/cgo57630.2024.10444787
[research_shamshiri_2015]: https://doi.org/10.1109/ase.2015.86
[research_shankar_2025]: https://doi.org/10.26438/ijcse/v13i3.7077
[research_shao_2017]: https://doi.org/10.1016/j.jss.2016.09.043
[research_shapley_1953]: https://doi.org/10.1515/9781400881970-018
[research_sharif_2021]: https://doi.org/10.1109/icsme52107.2021.00053
[research_sharma_2021]: https://doi.org/10.1109/msr52588.2021.00080
[research_sharma_2023]: https://doi.org/10.1145/3597926.3604919
[research_sharma_2023_b]: https://doi.org/10.32629/jai.v6i2.661
[research_sharma_2023_c]: https://doi.org/10.1063/5.0178097
[research_sharma_2024]: https://doi.org/10.1145/3643991.3644881
[research_sharrad_2018]: https://doi.org/10.1145/3310232.3310243
[research_she_2024]: https://doi.org/10.1145/3643659.3648562
[research_shen_2021]: https://doi.org/10.1145/3501774.3501781
[research_shen_2024]: https://doi.org/10.1109/icnp61940.2024.10858502
[research_shepperd_2018]: https://doi.org/10.1016/j.infsof.2018.01.006
[research_shi_2019]: https://doi.org/10.1145/3290386
[research_shi_2024]: https://doi.org/10.1016/j.tcs.2024.114755
[research_shi_2024_b]: https://doi.org/10.1142/s0218126625500355
[research_shi_2025]: https://doi.org/10.1109/smc58881.2025.11343558
[research_shi_2026]: https://doi.org/10.1145/3797905.3800551
[research_shillito_2024]: https://doi.org/10.1145/3636501.3636957
[research_shimizu_2025]: https://doi.org/10.1145/3713081.3731719
[research_shimmi_2022]: https://doi.org/10.1109/icst53961.2022.00023
[research_shin_2023]: https://doi.org/10.1145/3579990.3580009
[research_shin_2026]: https://doi.org/10.1109/access.2025.3650447
[research_shobeiri_2022]: https://doi.org/10.37917/ijeee.18.2.2
[research_shreyasmadhav_2021]: https://doi.org/10.1051/itmconf/20213701021
[research_shu_2021]: https://doi.org/10.1007/s10664-020-09906-8
[research_shukla_2021]: https://doi.org/10.5220/0010405002050212
[research_shukla_2021_b]: https://doi.org/10.5220/0010397700470057
[research_siavash_2025]: https://doi.org/10.1109/models67397.2025.00031
[research_sigweni_2016]: https://doi.org/10.1145/2915970.2916005
[research_silva_2025]: https://doi.org/10.1109/llm4code66737.2025.00006
[research_silva_2026]: https://doi.org/10.5753/cibse.2026.42458
[research_simmons_2011]: https://doi.org/10.1177/0956797611417632
[research_simon_2016]: https://doi.org/10.1109/etfa.2016.7733648
[research_singh_2015]: https://doi.org/10.1109/pervasive.2015.7087117
[research_singh_2017]: https://doi.org/10.1109/iciip.2017.8313788
[research_singh_2023]: https://doi.org/10.3389/fenrg.2023.1129846
[research_singhal_2017]: https://doi.org/10.1109/iccni.2017.8123805
[research_sisto_2016]: https://doi.org/10.1016/j.micpro.2016.10.001
[research_sivalingam_2025]: https://doi.org/10.11591/ijeecs.v38.i2.pp1265-1272
[research_sizilionery_2019]: https://doi.org/10.1109/icsme.2019.00075
[research_skalistis_2016]: https://doi.org/10.1007/978-3-319-44878-7_13
[research_slavik_1997]: https://doi.org/10.1006/jagm.1997.0887
[research_sobolewski_2025]: https://doi.org/10.32614/cran.package.muttest
[research_soeiro_2025]: https://doi.org/10.1109/msr66628.2025.00036
[research_sohl_2015]: https://doi.org/10.3384/diss.diva-113702
[research_soluian_2025]: https://doi.org/10.34185/1562-9945-3-158-2025-19
[research_sommer_2022]: https://doi.org/10.1109/cgo53902.2022.9741277
[research_son_2025]: https://doi.org/10.1109/icst62969.2025.10989019
[research_song_2019]: https://doi.org/10.1109/access.2019.2931579
[research_sonoyama_2020]: https://doi.org/10.1109/icce-taiwan49838.2020.9258219
[research_soremekun_2021]: https://doi.org/10.1007/s10664-020-09931-7
[research_sortino_2015]: https://doi.org/10.1016/j.jmsy.2014.03.002
[research_spaeh_2025]: https://doi.org/10.1609/aaai.v39i19.34266
[research_spampinato_2016]: https://doi.org/10.1145/2854038.2854060
[research_spieker_2017]: https://doi.org/10.1145/3092703.3092709
[research_sriiesaranusor_2021]: https://doi.org/10.1109/msr52588.2021.00056
[research_srinivasan_2018]: https://doi.org/10.1145/3193977.3193981
[research_srinivasaraoko_2024]: https://doi.org/10.52783/cana.v32.2114
[research_stacy_2022]: https://doi.org/10.1145/3524846.3527340
[research_steingartner_2021]: https://doi.org/10.1109/sami50585.2021.9378696
[research_stepanov_2021]: https://doi.org/10.1109/icst49551.2021.00044
[research_stepanov_2022]: https://doi.org/10.31799/1684-8853-2022-6-31-40
[research_stepanov_2025]: https://doi.org/10.30970/eli.32.10
[research_stern_2019]: https://doi.org/10.1016/j.geb.2018.09.006
[research_stirb_2023]: https://doi.org/10.3390/en16196781
[research_stocco_2023]: https://doi.org/10.1007/s10664-023-10306-x
[research_stochel_2020]: https://doi.org/10.1109/seaa51224.2020.00066
[research_stochel_2022]: https://doi.org/10.1109/seaa56994.2022.00055
[research_stojkovic_2025]: https://doi.org/10.1109/icetran66854.2025.11114225
[research_strumbelj_kononenko_2013]: https://doi.org/10.1007/s10115-013-0679-x
[research_su_2017]: https://doi.org/10.1109/cgo.2017.7863734
[research_su_2023]: https://doi.org/10.1109/dsa59317.2023.00118
[research_su_2024]: https://doi.org/10.1145/3704727
[research_su_2025]: https://doi.org/10.3390/app15042243
[research_su_2026]: https://doi.org/10.1145/3793302.3793383
[research_subrahmanyam_2025]: https://doi.org/10.21275/sr25916082410
[research_subramanyan_2025]: https://doi.org/10.5121/csit.2025.151407
[research_sulun_2024]: https://doi.org/10.1145/3643673
[research_sun_2017]: https://doi.org/10.1109/apsec.2017.41
[research_sun_2020]: https://doi.org/10.23919/acc45564.2020.9147476
[research_sun_2024]: https://doi.org/10.1007/s11704-024-40266-4
[research_sun_2025]: https://doi.org/10.1145/3774949.3774968
[research_suo_2024]: https://doi.org/10.1145/3650212.3680360
[research_suo_2025]: https://doi.org/10.1145/3763161
[research_supriyatna_2025]: https://doi.org/10.25139/jprs.v8i2.10926
[research_susca_2022]: https://doi.org/10.1109/aqtr55203.2022.9802027
[research_sutoyo_2026]: https://doi.org/10.1007/s10664-026-10916-1
[research_suzanne_2016]: https://doi.org/10.1007/978-3-662-53413-7_23
[research_svenkatesan_2025]: https://doi.org/10.12732/ijam.v38i11s.1286
[research_swain_2018]: https://doi.org/10.1109/correctness.2018.00009
[research_t_2020]: https://doi.org/10.5373/jardcs/v12sp1/20201079
[research_tabassam_2017]: https://doi.org/10.1109/indin.2017.8104849
[research_tackett_2024]: https://doi.org/10.1109/cdc56724.2024.10886209
[research_takana_2026]: https://doi.org/10.1145/3814943.3816171
[research_talaat_2025]: https://doi.org/10.1109/icm66518.2025.11322450
[research_talamali_2024]: https://doi.org/10.1109/icaase64542.2024.10850926
[research_tallada_2024]: https://doi.org/10.1109/ipdpsw63119.2024.00129
[research_tambon_2023]: https://doi.org/10.1109/icst57152.2023.00026
[research_tamura_2025]: https://doi.org/10.1145/3759426.3760985
[research_tan_2015]: https://doi.org/10.1145/2897336.2897344
[research_tan_2016]: https://doi.org/10.1145/3022670.2951924
[research_tan_2022]: https://doi.org/10.1016/j.compeleceng.2022.107766
[research_tan_2023]: https://doi.org/10.1007/s10009-022-00690-y
[research_tan_2023_b]: https://doi.org/10.26599/tst.2022.9010031
[research_tan_2025]: https://doi.org/10.1109/ismac65024.2025.11175984
[research_tan_2025_b]: https://doi.org/10.1109/ijcnn64981.2025.11229084
[research_taneja_2020]: https://doi.org/10.1145/3368826.3377927
[research_tang_2023]: https://doi.org/10.1016/j.tcs.2022.11.030
[research_tang_2024]: https://doi.org/10.1016/j.tcs.2023.114320
[research_tang_2024_b]: https://doi.org/10.54254/2755-2721/2024.18303
[research_tang_2025]: https://doi.org/10.1007/s10664-025-10642-0
[research_tang_2025_b]: https://doi.org/10.1109/yac66630.2025.11150137
[research_tang_2026]: https://doi.org/10.1109/access.2026.3652670
[research_tang_2026_b]: https://doi.org/10.1007/s42452-026-08711-0
[research_tang_2026_c]: https://doi.org/10.1145/3770855.3817695
[research_tao_2015]: https://doi.org/10.1109/msr.2015.24
[research_tarashev_2015]: https://doi.org/10.1093/rof/rfv028
[research_tengeri_2015]: https://doi.org/10.1109/icstw.2015.7107476
[research_tengeri_2016]: https://doi.org/10.1109/icstw.2016.25
[research_terres_2025]: https://doi.org/10.5753/eres.2025.16857
[research_thangamani_2023]: https://doi.org/10.1145/3554349
[research_thangamani_2023_b]: https://doi.org/10.1145/3579990.3580008
[research_thier_2018]: https://doi.org/10.1145/3178372.3179501
[research_thiselton_2019]: https://doi.org/10.1109/esem.2019.8870155
[research_thomas_2024]: https://doi.org/10.1109/dasc62030.2024.10749649
[research_thomas_2025]: https://doi.org/10.1109/icse55347.2025.00036
[research_thomson_2019]: https://doi.org/10.1201/9781351241410-1
[research_thorve_2018]: https://doi.org/10.1109/icsme.2018.00062
[research_tian_2021]: https://doi.org/10.1109/llvmhpc54804.2021.00009
[research_tian_2022]: https://doi.org/10.1007/978-3-031-15922-0_10
[research_tian_2025]: https://doi.org/10.1145/3774949.3774960
[research_tine_2019]: https://doi.org/10.1109/pact.2019.00055
[research_tiotto_2024]: https://doi.org/10.1109/cgo57630.2024.10444866
[research_tirichine_2026]: https://doi.org/10.1109/cgo68049.2026.11394838
[research_tirpankar_2025]: https://doi.org/10.1145/3731599.3767479
[research_titzer_2024]: https://doi.org/10.1109/cgo57630.2024.10444855
[research_titzer_2025]: https://doi.org/10.1145/3746172
[research_toeppe_2026]: https://doi.org/10.1145/3793302.3793311
[research_tofte_talpin_1997]: https://doi.org/10.1006/inco.1996.2613
[research_tong_2024]: https://doi.org/10.18653/v1/2024.emnlp-main.1118
[research_toosi_2023]: https://doi.org/10.2478/acss-2023-0022
[research_toprak_2026]: https://doi.org/10.1109/iisec69317.2026.11418473
[research_tran_2025]: https://doi.org/10.1142/s0217595925500356
[research_trippel_2025]: https://doi.org/10.1109/mc.2025.3573841
[research_troiber_2025]: https://doi.org/10.1109/ispass64960.2025.00053
[research_truong_2026]: https://doi.org/10.1016/j.infsof.2026.108185
[research_tsai_2021]: https://doi.org/10.1109/qrs54544.2021.00040
[research_tsoeunyane_2018]: https://doi.org/10.3390/computers7040053
[research_tsoukalas_2023]: https://doi.org/10.1002/smr.2564
[research_tsoupidi_2021]: https://doi.org/10.1109/secdev51306.2021.00029
[research_tu_2022]: https://doi.org/10.1109/issre55969.2022.00057
[research_tu_2022_b]: https://doi.org/10.1007/s10664-022-10121-w
[research_uchoa_2021]: https://doi.org/10.1109/msr52588.2021.00059
[research_undheim_2026]: https://doi.org/10.1016/j.softx.2026.102861
[research_urban_2025]: https://doi.org/10.1016/j.scico.2025.103338
[research_urbanek_2015]: https://doi.org/10.1186/s40064-015-1555-9
[research_uzayr_2022]: https://doi.org/10.1201/9781003214762-6
[research_v_2023]: https://doi.org/10.1504/ijpqm.2023.10060668
[research_vaas_2016]: https://doi.org/10.1109/ipdpsw.2016.143
[research_vahabzadeh_2015]: https://doi.org/10.1109/icsm.2015.7332456
[research_vahedifar_2025]: https://doi.org/10.1109/mlsp62443.2025.11204262
[research_vandam_2023]: https://doi.org/10.1109/msr59073.2023.00035
[research_vendome_2015]: https://doi.org/10.1109/icse.2015.245
[research_vendome_2015_b]: https://doi.org/10.1109/icpc.2015.32
[research_vendome_2016]: https://doi.org/10.1007/s10664-016-9438-4
[research_venkanna_2018]: https://doi.org/10.14419/ijet.v7i2.33.14162
[research_venkanna_2018_b]: https://doi.org/10.16925/.v14i0.2230
[research_venkat_2018]: https://doi.org/10.1109/icacat.2018.8933593
[research_ventovaara_2020]: https://doi.org/10.1109/icit45562.2020.9067160
[research_versluis_2017]: https://doi.org/10.1007/978-1-4842-2716-9_5
[research_versluis_2017_b]: https://doi.org/10.1007/978-1-4842-2716-9_6
[research_vescan_2021]: https://doi.org/10.1007/s10664-021-09947-7
[research_vescan_2023]: https://doi.org/10.1109/asew60602.2023.00014
[research_vetro_2015]: https://doi.org/10.1109/esem.2015.7321210
[research_vidacs_2016]: https://doi.org/10.1109/saner.2016.69
[research_voetberg_2023]: https://doi.org/10.2172/2246791
[research_vrany_2024]: https://doi.org/10.1145/3660829.3660838
[research_wallentowitz_2022]: https://doi.org/10.1109/meco55406.2022.9797106
[research_walshe_2020]: https://doi.org/10.1109/ibf50092.2020.9034828
[research_wan_2017]: https://doi.org/10.1109/msr.2017.59
[research_wang_2015]: https://doi.org/10.1109/edssc.2015.7285111
[research_wang_2017]: https://doi.org/10.1145/3092703.3092714
[research_wang_2018]: https://doi.org/10.1109/icsme.2018.00038
[research_wang_2018_b]: https://doi.org/10.1145/3196398.3196412
[research_wang_2018_c]: https://doi.org/10.1109/jproc.2018.2817118
[research_wang_2020]: https://doi.org/10.1109/tase49443.2020.00022
[research_wang_2021]: https://doi.org/10.1109/icsp51882.2021.9408924
[research_wang_2021_b]: https://doi.org/10.1109/compsac51774.2021.00124
[research_wang_2022]: https://doi.org/10.1109/isocc56007.2022.10031448
[research_wang_2022_b]: https://doi.org/10.1145/3497776.3517769
[research_wang_2023]: https://doi.org/10.1109/saner56733.2023.00041
[research_wang_2023_b]: https://doi.org/10.1109/ase56229.2023.00120
[research_wang_2023_c]: https://doi.org/10.5220/0012129000003538
[research_wang_2023_d]: https://doi.org/10.1109/esem56168.2023.10304799
[research_wang_2024]: https://doi.org/10.1142/s0218194024500475
[research_wang_2024_b]: https://doi.org/10.1145/3689780
[research_wang_2024_c]: https://doi.org/10.1186/s40854-023-00574-3
[research_wang_2024_d]: https://doi.org/10.5220/0013271800004558
[research_wang_2024_e]: https://doi.org/10.1201/9780429355080-13
[research_wang_2025]: https://doi.org/10.1145/3719276.3725178
[research_wang_2025_b]: https://doi.org/10.3390/buildings15173133
[research_wang_2025_c]: https://doi.org/10.52202/085713-4155
[research_wang_2025_d]: https://doi.org/10.1145/3729282
[research_wang_2026]: https://doi.org/10.1016/j.ress.2026.112886
[research_wang_2026_b]: https://doi.org/10.1145/3803633.3803666
[research_wanxin_2022]: https://doi.org/10.1109/cbd58033.2022.00044
[research_waseem_2025]: https://doi.org/10.1007/978-3-031-91481-2_10
[research_webb_2023]: https://doi.org/10.1145/3573105.3575673
[research_wegman_zadeck_1991]: https://doi.org/10.1145/103135.103136
[research_wei_2022]: https://doi.org/10.1145/3510003.3510170
[research_wei_2023]: https://doi.org/10.3390/electronics12122734
[research_weingarten_2025]: https://doi.org/10.1109/fdl68117.2025.11165398
[research_weissnegger_2016]: https://doi.org/10.5220/0005997700700075
[research_wen_2015]: https://doi.org/10.1109/pact.2015.29
[research_wen_2023]: https://doi.org/10.1109/saner56733.2023.00069
[research_werner_2020]: https://doi.org/10.1145/3380446.3430631
[research_wham_2024]: https://doi.org/10.1353/jaa.00007
[research_widyasari_2022]: https://doi.org/10.1007/s10664-022-10189-4
[research_wienand_2026]: https://doi.org/10.14722/fuzzing.2026.23005
[research_wilhelm_2008]: https://doi.org/10.1145/1347375.1347389
[research_wilson_1927]: https://doi.org/10.1080/01621459.1927.10502953
[research_windsor_2022]: https://doi.org/10.1002/stvr.1812
[research_wintolo_2015]: https://doi.org/10.28989/compiler.v4i2.91
[research_winton_2023]: https://doi.org/10.21428/594757db.09e3d60c
[research_wipfli_2026]: https://doi.org/10.23919/date69613.2026.11539385
[research_witthoft_2025]: https://doi.org/10.32614/cran.package.rfocal
[research_wong_1995]: https://doi.org/10.1145/225014.225018
[research_wu_2017]: https://doi.org/10.23940/ijpe.17.07.p14.11111122
[research_wu_2018]: https://doi.org/10.1049/iet-sen.2017.0159
[research_wu_2019]: https://doi.org/10.1109/tii.2018.2826140
[research_wu_2019_b]: https://doi.org/10.1145/3361242.3361258
[research_wu_2020]: https://doi.org/10.1109/apsec51365.2020.00033
[research_wu_2020_b]: https://doi.org/10.1109/smc42975.2020.9283132
[research_wu_2023]: https://doi.org/10.1109/icse48619.2023.00017
[research_wu_2024]: https://doi.org/10.1145/3643991.3644900
[research_wu_2024_b]: https://doi.org/10.1109/icpics62053.2024.10796417
[research_wu_2025]: https://doi.org/10.1145/3696410.3714622
[research_wu_2025_b]: https://doi.org/10.1145/3696630.3728528
[research_wu_2025_c]: https://doi.org/10.1109/mpcon66082.2025.11256702
[research_wu_2026]: https://doi.org/10.1063/5.0314659
[research_xavier_2022]: https://doi.org/10.1007/s10664-022-10203-9
[research_xia_2017]: https://doi.org/10.1109/wisa.2017.53
[research_xia_2017_b]: https://doi.org/10.1109/qrs-c.2017.59
[research_xia_2023]: https://doi.org/10.1109/icse48619.2023.00129
[research_xiao_2017]: https://doi.org/10.1587/transfun.e100.a.1384
[research_xiao_2018]: https://doi.org/10.14419/ijet.v7i2.28.13207
[research_xiao_2024]: https://doi.org/10.1007/s10664-024-10449-5
[research_xiao_2025]: https://doi.org/10.34133/icomputing.0113
[research_xie_2020]: https://doi.org/10.1109/infocomwkshps50562.2020.9162739
[research_xie_2025]: https://doi.org/10.1109/sbft66712.2025.00018
[research_xie_2026]: https://doi.org/10.1016/j.ipm.2026.104943
[research_xu_2017]: https://doi.org/10.1109/bigmm.2017.13
[research_xu_2018]: https://doi.org/10.1145/3239235.3240503
[research_xu_2022]: https://doi.org/10.1145/3559009.3569674
[research_xu_2022_b]: https://doi.org/10.1109/cdc51059.2022.9993308
[research_xu_2024]: https://doi.org/10.1109/icdcs60910.2024.00106
[research_xu_2024_b]: https://doi.org/10.1109/mlcad62225.2024.10740262
[research_xu_2025]: https://doi.org/10.1007/s11227-025-07378-5
[research_yadav_2022]: https://doi.org/10.1145/3519939.3523437
[research_yahyaoui_2022]: https://doi.org/10.1002/9781119902881.ch7
[research_yang_2011]: https://doi.org/10.1145/1993498.1993532
[research_yang_2015]: https://doi.org/10.1007/s11704-015-4364-y
[research_yang_2016]: https://doi.org/10.1145/2901739.2903504
[research_yang_2019]: https://doi.org/10.1109/icdcs.2019.00042
[research_yang_2020]: https://doi.org/10.1007/s10878-020-00662-5
[research_yang_2021]: https://doi.org/10.1016/j.dam.2020.05.001
[research_yang_2022]: https://doi.org/10.1109/dsa56465.2022.00087
[research_yang_2022_b]: https://doi.org/10.1007/s11432-020-3420-9
[research_yang_2023]: https://doi.org/10.3390/electronics12071573
[research_yang_2023_b]: https://doi.org/10.1145/3597926.3598087
[research_yang_2023_c]: https://doi.org/10.3390/electronics12071576
[research_yang_2024]: https://doi.org/10.1002/spe.3363
[research_yang_2024_b]: https://doi.org/10.1145/3691620.3695059
[research_yang_2024_c]: https://doi.org/10.1117/12.3027116
[research_yang_2024_d]: https://doi.org/10.1109/iseda62518.2024.10617643
[research_yang_2024_e]: https://doi.org/10.1145/3689736
[research_yang_2025]: https://doi.org/10.1109/icws67624.2025.00109
[research_yang_2025_b]: https://doi.org/10.1109/icse55347.2025.00089
[research_yang_2026]: https://doi.org/10.1109/cacml68972.2026.11507087
[research_yang_2026_b]: https://doi.org/10.1109/icst69053.2026.00032
[research_yao_2026]: https://doi.org/10.1109/eicct69950.2026.11564611
[research_yaraghi_2023]: https://doi.org/10.1109/tse.2022.3184842
[research_yarom_2022]: https://doi.org/10.1145/3560834.3564147
[research_ye_2019]: https://doi.org/10.1145/3293880.3294105
[research_ye_2020]: https://doi.org/10.1109/cdc42340.2020.9304492
[research_ye_2022]: https://doi.org/10.1109/hpca53966.2022.00060
[research_ye_2025]: https://doi.org/10.1109/cdc57313.2025.11312887
[research_ye_2026]: https://doi.org/10.1145/3776679
[research_yedida_2022]: https://doi.org/10.1145/3524842.3528458
[research_yi_2020]: https://doi.org/10.1109/dsa51864.2020.00022
[research_yi_2024]: https://doi.org/10.1145/3656443
[research_yi_2026]: https://doi.org/10.1145/3798245
[research_yildiz_2019]: https://doi.org/10.1109/ubmk.2019.8907220
[research_ying_2025]: https://doi.org/10.1002/stvr.70003
[research_yingzhe_2026]: https://doi.org/10.1016/j.nlp.2026.100215
[research_ylihuumo_2016]: https://doi.org/10.1016/j.jss.2016.05.018
[research_yoo_harman_2012]: https://doi.org/10.1002/stvr.430
[research_yoon_2025]: https://doi.org/10.1109/access.2025.3558081
[research_young_1985]: https://doi.org/10.1007/bf01769885
[research_yousofvand_2024]: https://doi.org/10.1007/s10462-023-10686-y
[research_yu_2016]: https://doi.org/10.4018/ijossp.2016100101
[research_yu_2017]: https://doi.org/10.1145/3060403.3060474
[research_yu_2019]: https://doi.org/10.1109/icsme.2019.00084
[research_yu_2023]: https://doi.org/10.1007/s10664-023-10356-1
[research_yu_2024]: https://doi.org/10.23919/date58400.2024.10546713
[research_yu_2024_b]: https://doi.org/10.1109/asap61560.2024.00045
[research_yuan_2022]: https://doi.org/10.3390/acoustics4030033
[research_yubin_2022]: https://doi.org/10.23940/ijpe.22.03.p1.149157
[research_zacchiroli_2022]: https://doi.org/10.1145/3524842.3528491
[research_zachariaova_2016]: https://doi.org/10.1109/dsd.2016.50
[research_zacharopoulos_2019]: https://doi.org/10.1109/iccd46524.2019.00024
[research_zampetti_2021]: https://doi.org/10.1007/s10664-021-10031-3
[research_zeng_2024]: https://doi.org/10.1145/3671016.3671387
[research_zeng_2026]: https://doi.org/10.1609/aaai.v40i33.40034
[research_zha_2022]: https://doi.org/10.1145/3519939.3523734
[research_zhang_2017]: https://doi.org/10.1145/3062341.3062379
[research_zhang_2018]: https://doi.org/10.1109/icsict.2018.8564985
[research_zhang_2019]: https://doi.org/10.1109/ccdc.2019.8833178
[research_zhang_2021]: https://doi.org/10.1109/icicse52190.2021.9404141
[research_zhang_2021_b]: https://doi.org/10.1007/978-3-030-69244-5_32
[research_zhang_2021_c]: https://doi.org/10.1002/cpe.6645
[research_zhang_2022]: https://doi.org/10.1145/3497776.3517778
[research_zhang_2022_b]: https://doi.org/10.1109/tse.2021.3124006
[research_zhang_2023]: https://doi.org/10.1109/a-sscc58667.2023.10347942
[research_zhang_2023_b]: https://doi.org/10.1145/3624743
[research_zhang_2024]: https://doi.org/10.1145/3671016.3671401
[research_zhang_2024_b]: https://doi.org/10.1145/3658644.3670372
[research_zhang_2024_c]: https://doi.org/10.1109/ialp63756.2024.10661189
[research_zhang_2025]: https://doi.org/10.1145/3763105
[research_zhang_2025_b]: https://doi.org/10.1007/s10664-024-10606-w
[research_zhang_2025_c]: https://doi.org/10.52202/085713-1276
[research_zhang_2025_d]: https://doi.org/10.52202/085713-1615
[research_zhang_2025_e]: https://doi.org/10.1007/s10288-025-00593-z
[research_zhang_2025_f]: https://doi.org/10.1109/mc.2025.3527407
[research_zhang_2025_g]: https://doi.org/10.1109/icws67624.2025.00123
[research_zhang_2025_h]: https://doi.org/10.5220/0014756900004940
[research_zhang_2026]: https://doi.org/10.1145/3774895.3812196
[research_zhang_2026_b]: https://doi.org/10.3390/ijgi15070310
[research_zhang_2026_c]: https://doi.org/10.1109/cgo68049.2026.11395194
[research_zhang_2026_d]: https://doi.org/10.1109/isca66397.2026.00018
[research_zhang_2026_e]: https://doi.org/10.1007/s10664-025-10798-9
[research_zhang_2026_f]: https://doi.org/10.1016/j.orl.2026.107456
[research_zhang_2026_g]: https://doi.org/10.1007/s10664-026-10802-w
[research_zhang_2026_h]: https://doi.org/10.1007/s11219-026-09751-w
[research_zhao_2012]: https://doi.org/10.1145/2103656.2103709
[research_zhao_2016]: https://doi.org/10.1145/2961111.2962591
[research_zhao_2021]: https://doi.org/10.3390/electronics10182210
[research_zhao_2023]: https://doi.org/10.1109/icsme58846.2023.00032
[research_zhao_2023_b]: https://doi.org/10.1504/ijcat.2023.131064
[research_zhao_2024]: https://doi.org/10.1145/3650212.3680340
[research_zhao_2024_b]: https://doi.org/10.1016/j.scico.2023.103027
[research_zhao_2025]: https://doi.org/10.1109/ipdps64566.2025.00041
[research_zhao_2025_b]: https://doi.org/10.1109/ipdps64566.2025.00054
[research_zheng_2023]: https://doi.org/10.1109/cei60616.2023.10528174
[research_zheng_2026]: https://doi.org/10.1109/asp-dac66049.2026.11420469
[research_zhioua_2017]: https://doi.org/10.1109/prdc.2017.51
[research_zhong_2015]: https://doi.org/10.1109/icse.2015.101
[research_zhong_2022]: https://doi.org/10.1145/3551349.3556894
[research_zhong_2025]: https://doi.org/10.1145/3696443.3708931
[research_zhou_2016]: https://doi.org/10.1145/2886101
[research_zhou_2017]: https://doi.org/10.1109/icstw.2017.74
[research_zhou_2018]: https://doi.org/10.1109/apsec.2018.00022
[research_zhou_2019]: https://doi.org/10.1109/mrs.2019.8901088
[research_zhou_2020]: https://doi.org/10.1109/icra40945.2020.9197243
[research_zhou_2022]: https://doi.org/10.1109/tr.2022.3165378
[research_zhu_1997]: https://doi.org/10.1145/267580.267590
[research_zhu_2025]: https://doi.org/10.1109/icmlca66850.2025.11336697
[research_zhu_2025_b]: https://doi.org/10.3102/ip.25.2182044
[research_zhuykov_2015]: https://doi.org/10.1109/csitechnol.2015.7358262
[research_zhuykov_2017]: https://doi.org/10.1134/s036176881701008x
[research_zia_2026]: https://doi.org/10.33564/ijeast.2026.v10i10.001
[research_ziftci_2020]: https://doi.org/10.1109/icsme46990.2020.00083
[research_zimmerle_2022]: https://doi.org/10.1145/3524842.3527966
[research_zou_2015]: https://doi.org/10.1109/compsac.2015.57
[research_zou_2019]: https://doi.org/10.1109/qrs.2019.00047
[research_zou_2023]: https://doi.org/10.1145/3627915.3628090
[research_zubair_2025]: https://doi.org/10.1016/j.csi.2024.103951
[research_zubert_2024]: https://doi.org/10.23919/mixdes62605.2024.10613932
