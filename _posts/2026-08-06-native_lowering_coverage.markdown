---
layout: post
mathjax: true
comments: true
title: "Keleusma Research Spike: Blocking Frequency as the Ordering Principle for Instruction-Set Coverage"
date: 2026-08-06 09:00:00 +0000
categories: engineering compilers verification
series: keleusma_research_spikes
series_title: Keleusma Research Spikes
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
| Verified and validated compilation | [Necula 1997][research_necula_1997] to [Lopes et al. 2021][research_lopes_2021] |
| Abstract interpretation | [Cousot and Cousot 1977][research_cousot_1977] to [Blanchet et al. 2003][research_blanchet_2003] |
| Worst-case resource analysis | [Liu and Layland 1973][research_liu_layland_1973] to [Wilhelm et al. 2008][research_wilhelm_2008] |
| Corpus-based empirical study | [Knuth 1971][research_knuth_1971] to [Ray et al. 2014][research_ray_2014] |
| Test adequacy and mutation | [DeMillo et al. 1978][research_demillo_1978] to [Inozemtseva and Holmes 2014][research_inozemtseva_holmes_2014] |
| Submodular optimisation and prioritisation | [Nemhauser et al. 1978][research_nemhauser_1978] to [Buchbinder et al. 2015][research_buchbinder_2015] |

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
[Wilhelm et al. 2008][research_wilhelm_2008] and by
[Puschner and Burns 2000][research_puschner_burns_2000], treats the coverage property as a
soundness-preservation question, in the sense [Leroy 2009][research_leroy_2009] establishes for a realistic
compiler and [Pnueli et al. 1998][research_pnueli_1998] formulate as translation validation, in
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
in the sense of the structured program theorem of [Böhm and Jacopini 1966][research_bohm_jacopini_1966], so
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
[Lovász 1983][research_lovasz_1983]. Submodularity, the property that was asserted, is diminishing returns,

$$S \subseteq S' \implies g(\iota, S) \ \ge\ g(\iota, S') \qquad \text{(submodular, and FALSE here)}$$

$$S \subseteq S' \implies g(\iota, S) \ \le\ g(\iota, S') \qquad \text{(supermodular, and true here)}$$

**And the guarantee that submodularity would have bought belongs here too**, since invoking it by name
without stating it is what let the error pass. For a monotone submodular objective under a cardinality
constraint the greedy algorithm satisfies

$$f(S_{\text{greedy}}) \ \ge\ \Bigl( 1 - \tfrac{1}{e} \Bigr) f(S_{\text{OPT}}) \approx 0.632 \, f(S_{\text{OPT}})$$

**No such bound is available here.** Under supermodularity the greedy choice can be arbitrarily bad, because
an instruction with zero marginal gain today may have large gain once its companions are present, which is
exactly the situation equation for $\lvert B(\iota, S) \rvert = 0$ above describes. An initial draft of this article
asserted the opposite and invoked the [Nemhauser et al. 1978][research_nemhauser_1978] result to
claim that greedy selection attains $\bigl(1 - \tfrac{1}{e}\bigr) \approx 0.632$ of the optimum under a
cardinality constraint. That claim is false. The classical guarantee requires diminishing returns, whose
tightness [Nemhauser and Wolsey 1978][research_nemhauser_wolsey_1978b] establish, whose dependence on
curvature [Conforti and Cornuéjols 1984][research_conforti_cornuejols_1984] characterise, whose geometric
character [Lovász 1983][research_lovasz_1983] develops, whose budgeted variant
[Khuller et al. 1999][research_khuller_1999] treat, and whose unconstrained non-monotone case
[Buchbinder et al. 2015][research_buchbinder_2015] settle at one half. Maximisation of a monotone
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
[Fraser et al. 1992][research_fraser_1992] reduced the approach to a practical generator
generator. [Ertl 1999][research_ertl_1999] extended optimality from trees to directed acyclic graphs. At the
extreme, [Massalin 1987][research_massalin_1987] searched the instruction space exhaustively for the
shortest program computing a function.
**The tradition also learned to synthesise the rules rather than write them, which matters because it changes what a lowering costs without changing what this article measures.**
[Davidson and Fraser 1984][research_davidson_fraser_1984] generated peephole optimisations automatically
from a machine description, [Aho et al. 1989][research_aho_ganapathi_1989] reduced
instruction selection to tree matching with dynamic programming,
[Bansal and Aiken 2006][research_bansal_aiken_2006] harvested a peephole superoptimiser by enumeration over
the target, and [Schkufza et al. 2013][research_schkufza_2013] replaced enumeration with
stochastic search over loop-free binaries. **Synthesis lowers $\kappa$ and leaves $\lvert B \rvert$ untouched**, so it
changes the leverage ratio through its denominator only and reorders nothing that the numerator determines.

Every one of these results presupposes that the target instruction set is available in its entirety. None
addresses the partial-implementation regime, because none has a reason to.

The supporting analyses are likewise complete-set analyses. [Allen 1970][research_allen_1970] established
control-flow analysis, [Kildall 1973][research_kildall_1973] the unified dataflow framework,
[Ferrante et al. 1987][research_ferrante_1987] the program dependence graph,
[Wegman and Zadeck 1991][research_wegman_zadeck_1991] conditional constant propagation, and
[Chaitin 1982][research_chaitin_1982] register allocation by graph colouring. Static single assignment form,
introduced by [Cytron et al. 1991][research_cytron_1991], given a functional reading by
[Appel 1998][research_appel_1998], and reduced to a simple construction by
[Braun et al. 2013][research_braun_2013], is the representation the present generator relies on,
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
[Kumar et al. 2014][research_kumar_2014] the analogous result for a functional language with a
verified implementation down to machine code. The second validates each compilation run instead of the
compiler, an approach [Pnueli et al. 1998][research_pnueli_1998] introduced as translation
validation, [Sewell et al. 2013][research_sewell_2013] applied to a verified operating-system
kernel, and [Kang et al. 2018][research_kang_2018] carried into the LLVM setting as credible
compilation. [Zhao et al. 2012][research_zhao_2012] formalised the LLVM intermediate representation
itself so that transformations over it may be verified, and [Lopes et al. 2021][research_lopes_2021]
built bounded translation validation for LLVM into a practical tool.

Where full verification is unavailable, differential and randomised testing carries the load.
[Yang et al. 2011][research_yang_2011] found hundreds of defects in production C compilers by random
program generation, [Le et al. 2014][research_le_2014] introduced equivalence modulo inputs as a
general oracle for compiler testing, and [Chen et al. 2016][research_chen_2016] applied
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
[Blanchet et al. 2003][research_blanchet_2003] built a static analyser for large safety-critical
avionics software and within which [Regehr et al. 2005][research_regehr_2005] eliminated stack
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
literature surveyed by [Wilhelm et al. 2008][research_wilhelm_2008] and earlier by
[Puschner and Burns 2000][research_puschner_burns_2000]. The dominant bounding technique is implicit path
enumeration, introduced by [Li and Malik 1995][research_li_malik_1995], which expresses the worst-case path
as an integer linear program over basic-block execution counts. The precision of any such bound on real
hardware depends on microarchitectural modelling, for which
[Ferdinand and Wilhelm 1999][research_ferdinand_wilhelm_1999] gave cache behaviour prediction and
[Reineke et al. 2007][research_reineke_2007] characterised the predictability of cache replacement
policies themselves.

The memory-bound side draws on the region and arena literature.
[Tofte and Talpin 1997][research_tofte_talpin_1997] introduced region-based memory management with static
inference of region lifetimes, [Grossman et al. 2002][research_grossman_2002] carried regions into a
safe systems language, [Hanson 1990][research_hanson_1990] gave the practical arena discipline of allocation
by object lifetime, and [Berger et al. 2002][research_berger_2002] examined empirically when custom
allocation actually pays. Keleusma's arena model is of this family, and **a bound proven over the arena
transfers to native code without further argument**, because the machine code allocates from the same
fixed-size arena in the same bytes. The open native question is a different quantity, being the machine
stack frame, which no bytecode-level bound describes and which is chosen instead by a register allocator in
the tradition of [Chaitin 1982][research_chaitin_1982].

A companion measurement, recorded in the project's decision register rather than in a separate article,
establishes that the per-function frame size is recoverable from the emitted object file, that it folds to a
compile-time constant, and that it varies by a factor of roughly thirty depending on whether the middle-end
promotion pass of [Cytron et al. 1991][research_cytron_1991] has run. That measurement is what makes
the [Regehr et al. 2005][research_regehr_2005] approach applicable here, since it supplies the
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
[Richards et al. 2010][research_richards_2010] measured the dynamic behaviour of deployed JavaScript
programs and found systematic divergence between what the language permits, what the literature assumed
programs did, and what programs actually did. [Allamanis and Sutton 2013][research_allamanis_sutton_2013]
and [Dyer et al. 2013][research_dyer_2013] built infrastructure for corpus mining at repository
scale, and [Ray et al. 2014][research_ray_2014] applied such infrastructure to language-level
questions about code quality.

Two lessons from this tradition bear directly on the present measurement. The first is that the gap between
permitted and actual is routinely large, which is exactly the gap the zero result below occupies, since the
four instructions in question are fully supported by the language and used by no program in the corpus. The
second concerns corpus composition, which dominates conclusions, a point
[Ray et al. 2014][research_ray_2014] and its subsequent reanalyses illustrate at length, and which
the threats-to-validity section below treats as the principal limitation of this work, never as a formality.

## Coverage Adequacy, Mutation, and What a Passing Suite Permits

The instrument reports a coverage figure, and the software-testing literature has spent decades establishing
what coverage figures do and do not mean. The parallel is close enough to draw explicitly.

[Zhu et al. 1997][research_zhu_1997] surveyed test coverage and adequacy criteria and the
relationships among them. The decisive empirical result is
[Inozemtseva and Holmes 2014][research_inozemtseva_holmes_2014], which found that coverage is not strongly
correlated with test-suite effectiveness once suite size is controlled, and therefore that a coverage
percentage is a poor proxy for the property anyone actually wants. The structural analogy to the present
case is exact. Instruction-level coverage $\rho^{\text{inst}}$ is the attractive, easily computed, and
largely uninformative measure. Unit-level coverage $\rho^{\text{unit}}$ is the one that tracks delivered
capability, and the two differ here by $\Gamma = 0.534$.

**The testing literature also solved the selection problem this article poses, in its own setting and with the same formal object.**
Reducing a test suite to a subset preserving coverage is set cover, stated as such by
[Harrold et al. 1993][research_harrold_1993], and the ordering variant is test-case
prioritisation, formalised by [Rothermel et al. 2001][research_rothermel_2001] and surveyed with
selection and minimisation by [Yoo and Harman 2012][research_yoo_harman_2012]. Safe selection, meaning
selection that cannot discard a test capable of exposing a difference, is due to
[Rothermel and Harrold 1997][research_rothermel_harrold_1997].
**The cautionary result belongs beside them.** [Wong et al. 1995][research_wong_1995] found that
minimising a suite while holding coverage constant can reduce fault-detection effectiveness, which is the
same warning the present article issues in the opposite direction.
**A coverage-preserving reduction and a coverage-maximising ordering are the same optimisation read forwards and backwards, and both are vulnerable to the measure standing in for the goal.**

The correctness discipline used throughout the development this article reports is mutation testing,
introduced by [DeMillo et al. 1978][research_demillo_1978] and surveyed by
[Jia and Harman 2011][research_jia_harman_2011]. Every structural assertion in the generator's test suite
carries a must-fire case, meaning a deliberate defect injected into the lowering that the assertion is
required to detect, and a must-not-fire case, meaning a known-clean input on which it is required to stay
silent. The empirical justification for treating mutants as a proxy for real defects is given by
[Andrews et al. 2005][research_andrews_2005] and strengthened by
[Just et al. 2014][research_just_2014], which found mutant detection to be correlated with
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
[Elbaum et al. 2002][research_elbaum_2002] studied test-case prioritisation across a family of
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
an obvious error, a point [Mytkowicz et al. 2009][research_mytkowicz_2009] make forcefully for
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
modern treatment of [de Moura and Ierusalimschy 2009][research_moura_ierusalimschy_2009], are the load-bearing
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
[Ostrand et al. 2005][research_ostrand_weyuker_2005], who found small fractions of modules
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
Repeating the calculation at $\lvert S' \rvert = 46$ gives $\rho^{\text{unit}}\_{0} = 3.275 \times 10^{-1}$ and $\Phi =
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
[Simmons et al. 2011][research_simmons_2011] demonstrated that undisclosed flexibility in
data collection and analysis suffices to produce statistically significant evidence for false propositions
without any conscious dishonesty. [Ioannidis 2005][research_ioannidis_2005] derived the consequences for
base rates of published findings, and [Munafò et al. 2017][research_munafo_2017] set out the
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
$\mathcal{D}\_{\text{corpus}}$ for the empirical distribution over units and $\mathcal{D}\_{\text{target}}$
for the eventual target population, every quantity reported above estimates

$$\mathbb{E}_{c \sim \mathcal{D}_{\text{corpus}}}\bigl[ \cdot \bigr] \qquad \text{rather than} \qquad \mathbb{E}_{c \sim \mathcal{D}_{\text{target}}}\bigl[ \cdot \bigr]$$

and no importance weighting is applied because the target distribution is not yet observable. The corpus
over-represents the self-hosted compiler, a text-processing workload with heavy data-segment use, and
under-represents the signal-processing and embedded-control workloads the roadmap names as target
applications. A defensible reading is that the data segment leads for the near-term consumer and that the
ranking should be re-measured when the target population changes. The sensitivity of conclusions to corpus
composition is the standard caution of this literature, and
[Blackburn et al. 2006][research_blackburn_2006] made the point concrete in constructing a benchmark
suite specifically because prior suites had shaped conclusions unrepresentatively, while
[Blackburn et al. 2016][research_blackburn_2016] set out the corresponding evaluation discipline.

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
of [Castro et al. 2009][research_castro_2009], which averages marginal gains over randomly drawn
permutations and converges at the usual rate in the number of samples, and in the closely related
attribution scheme of [Štrumbelj and Kononenko 2013][research_strumbelj_kononenko_2013].
**Neither was needed here and both would be needed for any instruction-level restatement of the same question.**

The zero results are subject to the corpus caveat and are bounded above rather than asserted absent, as
quantified in the confidence-bound section. The correct inference is not that the typed arithmetic class
will never matter but that it does not matter now, which is the question an ordering principle asks.

The measurement is static. It counts instruction instances in compiled units, never executions, so it
estimates the difficulty of lowering a program and says nothing about the time a program spends in any
instruction. For the ordering question this is the correct unit, since a refusal is a static property, but
the resulting figures must not be read as execution profiles.
[Georges et al. 2007][research_georges_2007] set out why execution-time claims require a different
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
| [The resource-bound article][related_post_a371] | 27 | 4 | 14.8 percent |
| [The aggregate-cost article][related_post_a372] | 26 | 7 | 26.9 percent |

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

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Abi-Karam, Stefan, Rishov Sarkar, Dejia Xu, Zhiwen Fan, Zhangyang Wang, and Cong Hao. 2023. "INR-Arch: A Dataflow Architecture and Compiler for Arbitrary-Order Gradient Computations in Implicit Neural Representation Processing." In *2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD)*. IEEE. [https://doi.org/10.1109/iccad57390.2023.10323650][research_abikaram_2023]
- Abnane, Ibtissam, Ali Idri, Imane Chlioui, and Alain Abran. 2023. "Evaluating Ensemble Imputation in Software Effort Estimation." *Empirical Software Engineering* 28 (2): 56. [https://doi.org/10.1007/s10664-022-10260-0][research_abnane_2023]
- Abrahám, Milan, and Pavel Koupil. 2025. "ORMorpher: An Interactive Framework for ORM Translation and Optimization." In *2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase63991.2025.00369][research_abraham_2025]
- Aghamohammadi, Alireza, Seyed-Hassan Mirian-Hosseinabadi, and Sajad Jalali. 2021. "Statement Frequency Coverage: A Code Coverage Criterion for Assessing Test Suite Effectiveness." *Information and Software Technology* 129: 106426. [https://doi.org/10.1016/j.infsof.2020.106426][research_aghamohammadi_2021]
- Agresti, Alan, and Brent A. Coull. 1998. "Approximate Is Better than “Exact” for Interval Estimation of Binomial Proportions." *American Statistician* 52 (2): 119–26. [https://doi.org/10.1080/00031305.1998.10480550][research_agresti_coull_1998]
- Ahmad, Khadija Sania, Nazia Ahmad, Hina Tahir, and Shaista Khan. 2017. "Fuzzy\_MoSCoW: A Fuzzy Based MoSCoW Method for the Prioritization of Software Requirements." In *2017 International Conference on Intelligent Computing, Instrumentation and Control Technologies (ICICICT)*. IEEE. [https://doi.org/10.1109/icicict1.2017.8342602][research_ahmad_2017]
- Ahmad, Mashal, and Mel O. Cinneide. 2019. "Impact of Stack Overflow Code Snippets on Software Cohesion: A Preliminary Study." In *2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2019.00050][research_ahmad_2019]
- Ahmed, Tanvir, and Yuko Hara-Azumi. 2015. "Timing Speculation-Aware Instruction Set Extension for Resource-Constrained Embedded Systems." In *2015 IEEE 26th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap.2015.7245701][research_ahmed_2015]
- Ahmed, Mansoor, Naeem Iqbal, Faraz Hussain, et al. 2022. "Blockchain-Based Software Effort Estimation: An Empirical Study." *IEEE Access* 10: 120412–25. [https://doi.org/10.1109/access.2022.3216840][research_ahmed_2022]
- Ajami, Shulamyt, Yonatan Woodbridge, and Dror G. Feitelson. 2018. "Syntax, Predicates, Idioms — What Really Affects Code Complexity?" *Empirical Software Engineering* 24 (1): 287–328. [https://doi.org/10.1007/s10664-018-9628-3][research_ajami_2018]
- Ajiki, Ren, and Kenji Hisazumi. 2026. "Automatic Program Repair Using Large Language Models in Model-Based Development." In *Proceedings of the 14th International Conference on Model-Based Software and Systems Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014491100004058][research_ajiki_2026]
- Akçelik, Zeliha Kaya, Reyhan Hoşavcı, Sümeyye Zülal Dik, Musa Aydin, and Zeki Kuş. 2025. "Data Valuation with Shapley-Based Methods for Medical Image Classification." In *2025 10th International Conference on Machine Learning Technologies (ICMLT)*. IEEE. [https://doi.org/10.1109/icmlt65785.2025.11193393][research_akcelik_2025]
- Akhtar, Sabina, and Ehtesham Zahoor. 2021. "Formal Specification and Verification of MQTT Protocol in PlusCal-2." *Wireless Personal Communications* 119 (2): 1589–1606. [https://doi.org/10.1007/s11277-021-08296-4][research_akhtar_2021]
- Akshay, S., Supratik Chakraborty, and Sahil Jain. 2023. "Counterexample Guided Knowledge Compilation for Boolean Functional Synthesis." In *Computer Aided Verification*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-37706-8\_19][research_akshay_2023]
- Al Blwi, Samia, Amani Ayad, Besma Khaireddine, Imen Marsit, and Ali Mili. 2023. "Semantic Coverage: Measuring Test Suite Effectiveness." In *Proceedings of the 18th International Conference on Software Technologies*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0012063900003538][research_alblwi_2023]
- Al-Ruqaishi, Yousuf, Abdelaziz Amara Korba, and Sharifa Al Khanjari. 2026. "LLM-Assisted End-to-End Binary Decompilation: A Hierarchical Generation and Semantic Reconstruction Approach." *Journal of Supercomputing* 82 (6): 356. [https://doi.org/10.1007/s11227-026-08506-5][research_alruqaishi_2026]
- Al-Zubidy, Ahmed, and Jeffrey C. Carver. 2018. "Identification and Prioritization of SLR Search Tool Requirements: An SLR and a Survey." *Empirical Software Engineering* 24 (1): 139–69. [https://doi.org/10.1007/s10664-018-9626-5][research_alzubidy_2018]
- Alardawi, Ahmed S., and Agil M. Agil. 2015. "Novice Comprehension of Object-Oriented OO Programs: An Empirical Study." In *2015 World Congress on Information Technology and Computer Applications (WCITCA)*. IEEE. [https://doi.org/10.1109/wcitca.2015.7367057][research_alardawi_2015]
- Alatawi, Abdulrahman, Weifeng Xu, and Jie Yan. 2018. "The Expansion of Source Code Abbreviations Using a Language Model." In *2018 IEEE 42nd Annual Computer Software and Applications Conference (COMPSAC)*. IEEE. [https://doi.org/10.1109/compsac.2018.10260][research_alatawi_2018]
- Aldarmini, Sokrat, and Mohamed Nafea. 2025. "Shapley-Value Based Feature Attribution for Explainability and Algorithmic Fairness: A Model-Agnostic Benchmark." In *2025 IEEE International Conference on Data Mining Workshops (ICDMW)*. IEEE. [https://doi.org/10.1109/icdmw69685.2025.00046][research_aldarmini_2025]
- Aleen, Farhana, Vyacheslav P. Zakharin, Rakesh Krishnaiyer, Garima Gupta, David Kreitzer, and Chang-Sun Lin. 2017. "Automated Compiler Optimization of Multiple Vector Loads/Stores." *International Journal of Parallel Programming* 46 (2): 471–503. [https://doi.org/10.1007/s10766-016-0485-7][research_aleen_2017]
- Alegroth, Emil, Arvid Karlsson, and Alexander Radway. 2018. "Continuous Integration and Visual GUI Testing: Benefits and Drawbacks in Industrial Practice." In *2018 IEEE 11th International Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst.2018.00026][research_alegroth_2018]
- Alfayez, Reem, and Barry Boehm. 2019. "Technical Debt Prioritization: A Search-Based Approach." In *2019 IEEE 19th International Conference on Software Quality, Reliability and Security (QRS)*. IEEE. [https://doi.org/10.1109/qrs.2019.00060][research_alfayez_2019]
- Alhamed, Mohammed, and Tim Storer. 2022. "Evaluation of Context-Aware Language Models and Experts for Effort Estimation of Software Maintenance Issues." In *2022 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme55016.2022.00020][research_alhamed_2022]
- Alhumam, Abdulaziz. 2026. "Leveraging Explainable AI for Requirements Prioritization in Agile Software Development." *Array* 31: 101027. [https://doi.org/10.1016/j.array.2026.101027][research_alhumam_2026]
- Ali, Syed Sarmad, Jian Ren, Kui Zhang, Ji Wu, and Chao Liu. 2023. "Heterogeneous Ensemble Model to Optimize Software Effort Estimation Accuracy." *IEEE Access* 11: 27759–92. [https://doi.org/10.1109/access.2023.3256533][research_ali_2023]
- Aljedaani, Wajdi, and Yasir Javed. 2020. "Empirical Study of Software Test Suite Evolution." In *2020 6th Conference on Data Science and Machine Learning Applications (CDMA)*. IEEE. [https://doi.org/10.1109/cdma47397.2020.00021][research_aljedaani_2020]
- Alladi, Shreya, Alberto Ros, and Alexandra Jimborean. 2026. "Enabling Automatic Compiler-Driven Vectorization of Transformers." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395226][research_alladi_2026]
- Allamanis, Miltiadis, and Charles Sutton. 2013. "Mining Source Code Repositories at Massive Scale Using Language Modeling." In *2013 10th Working Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2013.6624029][research_allamanis_sutton_2013]
- Alrakban, Nahlah A., Mubarak Alrashoud, and M. Abdullah-Al-Wadud. 2025. "Optimizing Test Case Prioritization with Meta Deep Reinforcement Learning in Continuous Integration." *IEEE Access* 13: 172435–55. [https://doi.org/10.1109/access.2025.3617387][research_alrakban_2025]
- Altunel, Haluk, Tugba Erdogan, and Ayca Kolukısa. 2026. "Rethinking Correctness and Efficiency in AI-Assisted Code Generation." In *Proceedings of the 21st International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014971000004015][research_altunel_2026]
- Alur, Rajeev. 2015. "Keynote Talk I: Syntax-Guided Synthesis." In *2015 ACM/IEEE International Conference on Formal Methods and Models for Codesign (MEMOCODE)*. IEEE. [https://doi.org/10.1109/memcod.2015.7340460][research_alur_2015]
- Alvanos, Michail, and Pedro Trancoso. 2016. "Video SIMDBench: Benchmarking the Compiler Vectorization for Multimedia Applications." In *2016 Euromicro Conference on Digital System Design (DSD)*. IEEE. [https://doi.org/10.1109/dsd.2016.90][research_alvanos_2016]
- Alzahrani, Nasser, Maria Spichkova, and James Harland. 2022. "Application of Property-Based Testing Tools for Metamorphic Testing." In *Proceedings of the 17th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0011101700003176][research_alzahrani_2022]
- Amanatidis, Theodoros, Nikolaos Mittas, Athanasia Moschou, Alexander Chatzigeorgiou, Apostolos Ampatzoglou, and Lefteris Angelis. 2020. "Evaluating the Agreement among Technical Debt Measurement Tools: Building an Empirical Benchmark of Technical Debt Liabilities." *Empirical Software Engineering* 25 (5): 4161–4204. [https://doi.org/10.1007/s10664-020-09869-w][research_amanatidis_2020]
- Amasaki, Sousuke, Hirohisa Aman, and Tomoyuki Yokogawa. 2022. "An Extended Study on Applicability and Performance of Homogeneous Cross-Project Defect Prediction Approaches under Homogeneous Cross-Company Effort Estimation Situation." *Empirical Software Engineering* 27 (2): 46. [https://doi.org/10.1007/s10664-021-10103-4][research_amasaki_2022]
- Amasaki, Sousuke, and Chris Lokan. 2017. "An Evaluation of Selection Methods for Time-Aware Effort Estimation." In *2017 24th Asia-Pacific Software Engineering Conference (APSEC)*. IEEE. [https://doi.org/10.1109/apsec.2017.105][research_amasaki_2017]
- Ambal, Guillaume, Sergueï Lenglet, and Alan Schmitt. 2022. "Certified Abstract Machines for Skeletal Semantics." In *Proceedings of the 11th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3497775.3503676][research_ambal_2022]
- Amini, Mohammad Hossein, Mehrdad Sabetzadeh, and Shiva Nejati. 2026. "Effort-Optimized, Accuracy-Driven Labelling and Validation of Test Inputs for DL Systems: A Mixed-Integer Linear Programming Approach." *Empirical Software Engineering* 31 (5): 135. [https://doi.org/10.1007/s10664-026-10850-2][research_amini_2026]
- Anbiya, Dhika Rizki, Teddy Ferdinan, and Grzegorz Kołaczek. 2025. "Java Source Code Vulnerability Detection Using Large Language Model." *Procedia Computer Science* 270: 2828–37. [https://doi.org/10.1016/j.procs.2025.09.405][research_anbiya_2025]
- Anchundia, Carlos E., and Efrain R. Fonseca C. 2020. "Resources for Reproducibility of Experiments in Empirical Software Engineering: Topics Derived from a Secondary Study." *IEEE Access* 8: 8992–9004. [https://doi.org/10.1109/access.2020.2964587][research_anchundia_2020]
- Andor, Camelia-Florina. 2021. "Runtime Metric Analysis in NoSQL Database Performance Benchmarking." In *2021 International Conference on Software, Telecommunications and Computer Networks (SoftCOM)*. IEEE. [https://doi.org/10.23919/softcom52868.2021.9559083][research_andor_2021]
- Andrews, J. H., L. C. Brand, and Y. Labiche. 2005. "Is Mutation an Appropriate Tool for Testing Experiments?" In *Proceedings. 27th International Conference on Software Engineering, 2005. ICSE 2005.*. IEEe. [https://doi.org/10.1109/icse.2005.1553583][research_andrews_2005]
- Andruccioli, Manuel, Giovanni Delnevo, Silvia Mirri, and Paola Salomoni. 2026. "PromptTone: A Dataset for Evaluating Large Language Model Code Generation under Varying Prompt Politeness Levels." *Data* 11 (4): 88. [https://doi.org/10.3390/data11040088][research_andruccioli_2026]
- Antoniadis, Dimitrios Dimitris, Peilong Feng, Andrea Mifsud, and Timothy G. Constandinou. 2021. "Open-Source Memory Compiler for Automatic RRAM Generation and Verification." In *2021 IEEE International Midwest Symposium on Circuits and Systems (MWSCAS)*. IEEE. [https://doi.org/10.1109/mwscas47672.2021.9531908][research_antoniadis_2021]
- Antoy, Sergio, and Andy Jost. 2017. "A New Functional-Logic Compiler for Curry: Sprite." In *Logic-Based Program Synthesis and Transformation*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-63139-4\_6][research_antoy_2017]
- Appel, Andrew W. 1998. "SSA Is Functional Programming." *ACM SIGPLAN Notices* 33 (4): 17–20. [https://doi.org/10.1145/278283.278285][research_appel_1998]
- Aquino, Andrea, Giovanni Denaro, and Pasquale Salza. 2018. "Worst-Case Execution Time Testing via Evolutionary Symbolic Execution." In *2018 IEEE 29th International Symposium on Software Reliability Engineering (ISSRE)*. IEEE. [https://doi.org/10.1109/issre.2018.00019][research_aquino_2018]
- Arbaoui, Meriem, Mohamed-El-Amine Brahmia, Abdellatif Rahmoun, and Mourad Zghal. 2024. "Optimizing Shapley Value for Client Valuation in Federated Learning through Enhanced GTG-Shapley." In *2024 International Wireless Communications and Mobile Computing (IWCMC)*. IEEE. [https://doi.org/10.1109/iwcmc61514.2024.10592437][research_arbaoui_2024]
- Arcaro, Luis Fernando, Karila Palma Silva, Romulo Silva de Oliveira, and Luis Almeida. 2020. "Reliability Test Based on a Binomial Experiment for Probabilistic Worst-Case Execution Times." In *2020 IEEE Real-Time Systems Symposium (RTSS)*. IEEE. [https://doi.org/10.1109/rtss49844.2020.00016][research_arcaro_2020]
- Arnström, Daniel, David Broman, and Daniel Axehill. 2024. "Exact Worst-Case Execution-Time Analysis for Implicit Model Predictive Control." *IEEE Transactions on Automatic Control* 69 (10): 7190–96. [https://doi.org/10.1109/tac.2024.3395521][research_arnstrom_2024]
- Arrieta, Aitor. 2026. "An Empirical Evaluation of White-Box and Black-Box Test Case Prioritization Techniques in CPSs Modeled in Simulink." *Empirical Software Engineering* 31 (5): 141. [https://doi.org/10.1007/s10664-026-10875-7][research_arrieta_2026]
- Arrieta, Aitor, Pablo Valle, Asier Iriarte, and Miren Illarramendi. 2023. "How Do Deep Learning Faults Affect AI-Enabled Cyber-Physical Systems in Operation? A Preliminary Study Based on DeepCrime Mutation Operators." In *2023 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem56168.2023.10304794][research_arrieta_2023]
- Ashraf, Ameena K., and Meenakshi D'Souza. 2025. "Mutation Testing of Programs for Industrial Robots." In *2025 IEEE 21st International Conference on Automation Science and Engineering (CASE)*. IEEE. [https://doi.org/10.1109/case58245.2025.11163762][research_ashraf_2025]
- Ashraf, Humza, Syed Muhammad Danish, Shadikur Rahman, and Zeeshan Sattar. 2025. "Toward Green Code: Prompting Small Language Models for Energy-Efficient Code Generation." In *2025 3rd International Conference on Foundation and Large Language Models (FLLM)*. IEEE. [https://doi.org/10.1109/fllm67465.2025.11391183][research_ashraf_2025_b]
- Assar, Saïd, Markus Borg, and Dietmar Pfahl. 2015. "Using Text Clustering to Predict Defect Resolution Time: A Conceptual Replication and an Evaluation of Prediction Accuracy." *Empirical Software Engineering* 21 (4): 1437–75. [https://doi.org/10.1007/s10664-015-9391-7][research_assar_2015]
- Athale, Mihir, and Vishal Vaddina. 2025. "Knowledge Graph Based Repository-Level Code Generation." In *2025 IEEE/ACM International Workshop on Large Language Models for Code (LLM4Code)*. IEEE. [https://doi.org/10.1109/llm4code66737.2025.00026][research_athale_2025]
- Augustin, Sarah, Hendrik Winkelmann, and Herbert Kuchen. 2025. "Mutation Operators for Mutation Testing of Angular Web Applications." In *Proceedings of the 20th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0013203900003928][research_augustin_2025]
- Avigad, Jeremy, Lior Goldberg, David Levit, Yoav Seginer, and Alon Titelman. 2025. "A Proof-Producing Compiler for Blockchain Applications." *Journal of Automated Reasoning* 69 (2): 9. [https://doi.org/10.1007/s10817-025-09723-y][research_avigad_2025]
- Aytekin, Mehmet Cem, Fatma Gizem Yılmaz, and Mustafa Umut Demirezen. 2026. "Automating Code Generation for a New Ecosystem: Establishing Baselines with Large Language Model Based Code Generation for ArkTS and HarmonyOS." *Automated Software Engineering* 33 (2): 59. [https://doi.org/10.1007/s10515-026-00599-9][research_aytekin_2026]
- Azmy, Noran, Stephan Merz, and Christoph Weidenbach. 2018. "A Machine-Checked Correctness Proof for Pastry." *Science of Computer Programming* 158: 64–80. [https://doi.org/10.1016/j.scico.2017.08.003][research_azmy_2018]
- Azuma, Hideaki, Shinsuke Matsumoto, Yasutaka Kamei, and Shinji Kusumoto. 2022. "An Empirical Study on Self-Admitted Technical Debt in Dockerfiles." *Empirical Software Engineering* 27 (2): 49. [https://doi.org/10.1007/s10664-021-10081-7][research_azuma_2022]
- Azzeh, Mohammad, and Ali Bou Nassif. 2018. "Project Productivity Evaluation in Early Software Effort Estimation." *Journal of Software: Evolution and Process* 30 (12): e2110. [https://doi.org/10.1002/smr.2110][research_azzeh_2018]
- Azzeh, Mohammad, Ali Bou Nassif, and Leandro L. Minku. 2015. "An Empirical Evaluation of Ensemble Adjustment Methods for Analogy-Based Effort Estimation." *Journal of Systems and Software* 103: 36–52. [https://doi.org/10.1016/j.jss.2015.01.028][research_azzeh_2015]
- Babur, Önder, Eleni Constantinou, and Alexander Serebrenik. 2023. "Language Usage Analysis for EMF Metamodels on GitHub." *Empirical Software Engineering* 29 (1): 23. [https://doi.org/10.1007/s10664-023-10368-x][research_babur_2023]
- Baek, Nakhoon, and Kuinam J. Kim. 2017. "Prototype Implementation of the OpenGL ES 2.0 Shading Language Offline Compiler." *Cluster Computing* 22 (S1): 943–48. [https://doi.org/10.1007/s10586-017-1113-z][research_baek_2017]
- Baghcheband, Hajar, Carlos Soares, and Luis Paulo Reis. 2024. "Shapley-Based Data Valuation Method for the Machine Learning Data Markets (MLDM)." In *Foundations of Intelligent Systems*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-62700-2\_16][research_baghcheband_2024]
- Baghcheband, Hajar, Carlos Soares, and Luis Paulo Reis. 2025. "Shapley Value-Based Data Valuation for Machine Learning Data Markets." *Discover Applied Sciences* 7 (12): 1431. [https://doi.org/10.1007/s42452-025-07328-z][research_baghcheband_2025]
- Bai, Jia-Ju, Zi-Xuan Fu, Kai-Tao Xie, and Zu-Ming Jiang. 2024. "Testing Error Handling Code with Software Fault Injection and Error-Coverage-Guided Fuzzing." *IEEE Transactions on Dependable and Secure Computing* 21 (4): 1724–39. [https://doi.org/10.1109/tdsc.2023.3288876][research_bai_2024]
- Bakhirkin, Alexey, and David Monniaux. 2017. "Combining Forward and Backward Abstract Interpretation of Horn Clauses." In *Static Analysis*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-66706-5\_2][research_bakhirkin_2017]
- Balachandran, Vipin. 2015. "Query by Example in Large-Scale Code Repositories." In *2015 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsm.2015.7332498][research_balachandran_2015]
- Balasubramanian, Karthikeyan Kalyanasundaram, Mirco Di Salvo, Walter Rocchia, Sergio Decherchi, and Marco Crepaldi. 2024. "Designing RISC-V Instruction Set Extensions for Artificial Neural Networks: An LLVM Compiler-Driven Perspective." *IEEE Access* 12: 55925–44. [https://doi.org/10.1109/access.2024.3389673][research_balasubramania_2024]
- Baldassarre, Maria Teresa, and Marcos Kalinowski. 2023. "Guest Editorial: Special Issue on Empirical Software Engineering and Measurement." *Empirical Software Engineering* 29 (1): 3. [https://doi.org/10.1007/s10664-023-10357-0][research_baldassarre_2023]
- Balogh, G. D., G. R. Mudalige, I. Z. Reguly, S. F. Antao, and C. Bertolli. 2018. "OP2-Clang: A Source-to-Source Translator Using Clang/LLVM LibTooling." In *2018 IEEE/ACM 5th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2018.8639205][research_balogh_2018]
- Bang, Seongwon, Seunghyeon Nam, Inwhan Chun, Ho Young Jhoo, and Juneyoung Lee. 2022. "SMT-Based Translation Validation for Machine Learning Compiler." In *Computer Aided Verification*. Springer International Publishing. [https://doi.org/10.1007/978-3-031-13188-2\_19][research_bang_2022]
- Bao, Shu-Yu, Qing-Qin Nong, and Su-Ning Gong. 2024. "An Improved Space Semi-Streaming Algorithm for Submodular Maximization under b-Matching Constraint." *Journal of the Operations Research Society of China* 14 (2): 671–86. [https://doi.org/10.1007/s40305-024-00543-2][research_bao_2024]
- Bao, Lingfeng, Xin Xia, David Lo, and Gail C. Murphy. 2021. "A Large Scale Study of Long-Time Contributor Prediction for GitHub Projects." *IEEE Transactions on Software Engineering* 47 (6): 1277–98. [https://doi.org/10.1109/tse.2019.2918536][research_bao_2021]
- Bao, Lingfeng, Zhenchang Xing, Xin Xia, David Lo, and Shanping Li. 2017. "Who Will Leave the Company?: A Large-Scale Industry Study of Developer Turnover by Mining Monthly Work Report." In *2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2017.58][research_bao_2017]
- Barani, Maryam, Yvan Labiche, and Antoine Rollet. 2023. "On Factors That Impact the Relationship between Code Coverage and Test Suite Effectiveness: A Survey." In *2023 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw58534.2023.00071][research_barani_2023]
- Barik, Titus, Kevin Lubick, Justin Smith, John Slankas, and Emerson Murphy-Hill. 2015. "Fuse: A Reproducible, Extendable, Internet-Scale Corpus of Spreadsheets." In *2015 IEEE/ACM 12th Working Conference on Mining Software Repositories*. IEEE. [https://doi.org/10.1109/msr.2015.70][research_barik_2015]
- Barrière, Aurèle, Sandrine Blazy, Olivier Flückiger, David Pichardie, and Jan Vitek. 2021. "Formally Verified Speculation and Deoptimization in a JIT Compiler." *Proceedings of the ACM on Programming Languages* 5 (POPL): 1–26. [https://doi.org/10.1145/3434327][research_barriere_2021]
- Barrière, Aurèle, Sandrine Blazy, and David Pichardie. 2023. "Formally Verified Native Code Generation in an Effectful JIT: Turning the CompCert Backend into a Formally Verified JIT Compiler." *Proceedings of the ACM on Programming Languages* 7 (POPL): 249–77. [https://doi.org/10.1145/3571202][research_barriere_2023]
- Basile, Davide, Maurice H. ter Beek, Sami Lazreg, Maxime Cordy, and Axel Legay. 2022. "Static Detection of Equivalent Mutants in Real-Time Model-Based Mutation Testing: An Empirical Evaluation." *Empirical Software Engineering* 27 (7): 160. [https://doi.org/10.1007/s10664-022-10149-y][research_basile_2022]
- Basili, Victor, and Lionel Briand. 2021. "Reflections on the Empirical Software Engineering Journal." *Empirical Software Engineering* 27 (1): 6. [https://doi.org/10.1007/s10664-021-10055-9][research_basili_2021]
- Basili, Victor R., and David M. Weiss. 1984. "A Methodology for Collecting Valid Software Engineering Data." *IEEE Transactions on Software Engineering* SE-10 (6): 728–38. [https://doi.org/10.1109/tse.1984.5010301][research_basili_weiss_1984]
- Bavier, Eric, Nicholas Knight, Hugues de Lassus Saint-Geniès, and Eric Love. 2023. "Vectorized Nonlinear Functions with the RISC-V Vector Extension." In *2023 IEEE 30th Symposium on Computer Arithmetic (ARITH)*. IEEE. [https://doi.org/10.1109/arith58626.2023.00032][research_bavier_2023]
- Behera, Aishwaryarani, and Arup Abhinna Acharya. 2025. "An Effective GRU-Based Deep Learning Method for Test Case Prioritization in Continuous Integration Testing." *Procedia Computer Science* 258: 4070–83. [https://doi.org/10.1016/j.procs.2025.04.658][research_behera_2025]
- Bell, Logan, Nikhil Devanathan, and Stephen Boyd. 2024. "Efficient Shapley Performance Attribution for Least-Squares Regression." *Statistics and Computing* 34 (5): 149. [https://doi.org/10.1007/s11222-024-10459-9][research_bell_2024]
- Bembenek, Aaron, Michael Greenberg, and Stephen Chong. 2023. "From SMT to ASP: Solver-Based Approaches to Solving Datalog Synthesis-as-Rule-Selection Problems." *Proceedings of the ACM on Programming Languages* 7 (POPL): 185–217. [https://doi.org/10.1145/3571200][research_bembenek_2023]
- Berger, Emery D., Benjamin G. Zorn, and Kathryn S. McKinley. 2002. "Reconsidering Custom Memory Allocation." In *Proceedings of the 17th ACM SIGPLAN conference on Object-oriented programming, systems, languages, and applications - OOPSLA '02*. ACM Press. [https://doi.org/10.1145/582419.582421][research_berger_2002]
- Berndt, Alexander, Vekil Bekmyradov, Rainer Gemulla, Marcus Kessel, Thomas Bach, and Sebastian Baltes. 2026. "Can We Classify Flaky Tests Using Only Test Code? An LLM-Based Empirical Study." In *2026 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner67736.2026.00016][research_berndt_2026]
- Berndt, Alexander, Zoltán Nochta, and Thomas Bach. 2023. "The Vocabulary of Flaky Tests in the Context of SAP HANA." In *2023 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem56168.2023.10304860][research_berndt_2023]
- Berry, Daniel M. 2021. "Empirical Evaluation of Tools for Hairy Requirements Engineering Tasks." *Empirical Software Engineering* 26 (6): 111. [https://doi.org/10.1007/s10664-021-09986-0][research_berry_2021]
- Bessghaier, Narjes, Ali Ouni, Mohammed Sayagh, Moataz Chouchen, and Mohamed Wiem Mkaouer. 2025. "Towards Understanding Code Review Practices for Infrastructure-as-Code: An Empirical Study on OpenStack Projects." *Empirical Software Engineering* 30 (4): 106. [https://doi.org/10.1007/s10664-025-10654-w][research_bessghaier_2025]
- Besson, Frédéric, Sandrine Blazy, and Pierre Wilke. 2017. "A Verified CompCert Front-End for a Memory Model Supporting Pointer Arithmetic and Uninitialised Data." *Journal of Automated Reasoning* 62 (4): 433–80. [https://doi.org/10.1007/s10817-017-9439-z][research_besson_2017]
- Besson, Frédéric, Sandrine Blazy, and Pierre Wilke. 2018. "CompCertS: A Memory-Aware Verified C Compiler Using a Pointer as Integer Semantics." *Journal of Automated Reasoning* 63 (2): 369–92. [https://doi.org/10.1007/s10817-018-9496-y][research_besson_2018]
- Betka, Maik, and Stefan Wagner. 2021. "Extreme Mutation Testing in Practice: An Industrial Case Study." In *2021 IEEE/ACM International Conference on Automation of Software Test (AST)*. IEEE. [https://doi.org/10.1109/ast52587.2021.00021][research_betka_2021]
- Beyer, Dirk, and Thomas Lemberger. 2019. "TestCov: Robust Test-Suite Execution and Coverage Measurement." In *2019 34th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase.2019.00105][research_beyer_2019]
- Bezerra, Roberta M. M., Fabio Q. B. da Silva, Anderson M. Santana, Cleyton V. C. Magalhaes, and Ronnie E. S. Santos. 2015. "Replication of Empirical Studies in Software Engineering: An Update of a Systematic Mapping Study." In *2015 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2015.7321213][research_bezerra_2015]
- Bhamidipati, Padmaja, and Ranga Vemuri. 2023. "ASPIRE: An Intermediate Representation for Abstract Security Policies." In *2023 36th International Conference on VLSI Design and 2023 22nd International Conference on Embedded Systems (VLSID)*. IEEE. [https://doi.org/10.1109/vlsid57277.2023.00046][research_bhamidipati_2023]
- Bi, Fandi, Birgit Vogel-Heuser, Fengmin Du, Nils Hanich, and Ennuri Cho. 2023. "Technical Debt Contagiousness Metrics for Measurement and Prioritization in Mechatronics." In *2023 ACM/IEEE International Conference on Technical Debt (TechDebt)*. IEEE. [https://doi.org/10.1109/techdebt59074.2023.00012][research_bi_2023]
- Biazotto, João Paulo, Daniel Feitosa, Paris Avgeriou, and Elisa Yumi Nakagawa. 2025. "Understanding Practitioners’ Reasoning and Requirements for Efficient Tool Support in Technical Debt Management." *Empirical Software Engineering* 30 (5): 134. [https://doi.org/10.1007/s10664-025-10691-5][research_biazotto_2025]
- Biazotto, João Paulo, Daniel Feitosa, Paris Avgeriou, and Elisa Yumi Nakagawa. 2026. "TagDebt: A Bot to Support Technical Debt Management." *Empirical Software Engineering* 31 (6): 170. [https://doi.org/10.1007/s10664-026-10900-9][research_biazotto_2026]
- Binosi, Lorenzo, Luca Rullo, Mario Polino, Michele Carminati, and Stefano Zanero. 2023. "Rainfuzz: Reinforcement-Learning Driven Heat-Maps for Boosting Coverage-Guided Fuzzing." In *Proceedings of the 12th International Conference on Pattern Recognition Applications and Methods*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0011625300003411][research_binosi_2023]
- Bistarelli, Stefano, Marco Fiore, Ivan Mercanti, and Marina Mongiello. 2025. "Usage of Large Language Model for Code Generation Tasks: A Review." *SN Computer Science* 6 (6): 673. [https://doi.org/10.1007/s42979-025-04241-5][research_bistarelli_2025]
- Black, Gavin S., Bhaskar P. Rimal, and Varghese Mathew Vaidyan. 2025. "Balancing Security and Correctness in Code Generation: An Empirical Study on Commercial Large Language Models." *IEEE Transactions on Emerging Topics in Computational Intelligence* 9 (1): 419–30. [https://doi.org/10.1109/tetci.2024.3446695][research_black_2025]
- Blackburn, Stephen M., Robin Garner, Chris Hoffmann, et al. 2006. "The DaCapo Benchmarks: Java Benchmarking Development and Analysis." In *Proceedings of the 21st annual ACM SIGPLAN conference on Object-oriented programming systems, languages, and applications*. ACM. [https://doi.org/10.1145/1167473.1167488][research_blackburn_2006]
- Blanchet, Bruno, Patrick Cousot, Radhia Cousot, et al. 2003. "A Static Analyzer for Large Safety-Critical Software." In *Proceedings of the ACM SIGPLAN 2003 conference on Programming language design and implementation*. ACM. [https://doi.org/10.1145/781131.781153][research_blanchet_2003]
- Blazy, Sandrine. 2023. "CompCert: A Journey through the Landscape of Mechanized Semantics for Verified Compilation (Keynote)." In *Proceedings of the 12th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3573105.3579107][research_blazy_2023]
- Boda, Yashwanth, Abhijit Chunduri, Ruchi Kumari, and Awanish Pandey. 2026. "CPerfSmith: A Randomized C Program Generator for Performance-Oriented Compiler Testing." In *Proceedings of the 35th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3771775.3786271][research_boda_2026]
- Boehm, B. W. 1988. "A Spiral Model of Software Development and Enhancement." *Computer* 21 (5): 61–72. [https://doi.org/10.1109/2.59][research_boehm_1988]
- Bogunovic, Ilija, Slobodan Mitrovic, Jonathan Scarlett, and Volkan Cevher. 2017. "A Distributed Algorithm for Partitioned Robust Submodular Maximization." In *2017 IEEE 7th International Workshop on Computational Advances in Multi-Sensor Adaptive Processing (CAMSAP)*. IEEE. [https://doi.org/10.1109/camsap.2017.8313155][research_bogunovic_2017]
- Bohrer, Rose, Yong Kiam Tan, Stefan Mitsch, Magnus O. Myreen, and André Platzer. 2018. "VeriPhy: Verified Controller Executables from Verified Cyber-Physical System Models." In *Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3192366.3192406][research_bohrer_2018]
- Bolat, Alperen, Sakir Sezer, Kieran McLaughlin, and Henry Hui. 2025. "Microarchitecture Design and Benchmarking of Custom SHA-3 Instruction for RISC-V." In *2025 IEEE Computer Society Annual Symposium on VLSI (ISVLSI)*. IEEE. [https://doi.org/10.1109/isvlsi65124.2025.11130308][research_bolat_2025]
- Borade, Shilpa Anil, Saurabh Bansod, Anirban Jyoti Hati, and Shashank Kumar Singh. 2025. "AI Edge Processor Using RISC: V Instruction Set Architecture Design." In *2025 Global Conference in Emerging Technology (GINOTECH)*. IEEE. [https://doi.org/10.1109/ginotech63460.2025.11076631][research_borade_2025]
- Bosu, Amiangshu, Michaela Greiler, and Christian Bird. 2015. "Characteristics of Useful Code Reviews: An Empirical Study at Microsoft." In *2015 IEEE/ACM 12th Working Conference on Mining Software Repositories*. IEEE. [https://doi.org/10.1109/msr.2015.21][research_bosu_2015]
- Boujida, Fatima, Fatima Amazal, and Ali Idri. 2021. "Neural Networks Based Software Development Effort Estimation: A Systematic Mapping Study." In *Proceedings of the 16th International Conference on Software Technologies*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0010603700002992][research_boujida_2021]
- Bourke, Timothy, Lélio Brun, Pierre-Évariste Dagand, Xavier Leroy, Marc Pouzet, and Lionel Rieg. 2017. "A Formally Verified Compiler for Lustre." *ACM SIGPLAN Notices* 52 (6): 586–601. [https://doi.org/10.1145/3140587.3062358][research_bourke_2017]
- Brach, William, Kristián Košt'ál, and Michal Ries. 2024. "Can Large Language Model Detect Plagiarism in Source Code?" In *2024 2nd International Conference on Foundation and Large Language Models (FLLM)*. IEEE. [https://doi.org/10.1109/fllm63129.2024.10852497][research_brach_2024]
- Brauckmann, Alexander, Aarsh Chaube, José W. De Souza Magalhães, Elizabeth Polgreen, and Michael F. P. O'Boyle. 2026. "Tensor Program Superoptimization through Cost-Guided Symbolic Program Synthesis." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395198][research_brauckmann_2026]
- Braun, Matthias, Sebastian Buchwald, Sebastian Hack, Roland Leißa, Christoph Mallon, and Andreas Zwinkau. 2013. "Simple and Efficient Construction of Static Single Assignment Form." In *Compiler Construction*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-642-37051-9\_6][research_braun_2013]
- Brenes, Edgar Mauricio, and Carlos Meza. 2019. "An Application-Specific Instruction Set Processor for Microgrid Simulation." In *2019 IEEE 39th Central America and Panama Convention (CONCAPAN XXXIX)*. IEEE. [https://doi.org/10.1109/concapanxxxix47272.2019.8976981][research_brenes_2019]
- Brennan, Tegan, Nicolas Rosner, and Tevfik Bultan. 2020. "JIT Leaks: Inducing Timing Side Channels through Just-In-Time Compilation." In *2020 IEEE Symposium on Security and Privacy (SP)*. IEEE. [https://doi.org/10.1109/sp40000.2020.00007][research_brennan_2020]
- Bride, Hadrien, Olga Kouchnarenko, and Fabien Peureux. 2017. "Reduction of Workflow Nets for Generalised Soundness Verification." In *Verification, Model Checking, and Abstract Interpretation*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-52234-0\_6][research_bride_2017]
- Britto, Ricardo, Emilia Mendes, and Jurgen Borstler. 2015. "An Empirical Investigation on Effort Estimation in Agile Global Software Development." In *2015 IEEE 10th International Conference on Global Software Engineering*. IEEE. [https://doi.org/10.1109/icgse.2015.10][research_britto_2015]
- Brown, Nick. 2024. "Fully Integrating the Flang Fortran Compiler with Standard MLIR." In *SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis*. IEEE. [https://doi.org/10.1109/scw63240.2024.00133][research_brown_2024]
- Bruns, Niklas, Vladimir Herdt, and Rolf Drechsler. 2022b. "Unified HW/SW Coverage: A Novel Metric to Boost Coverage-Guided Fuzzing for Virtual Prototype Based HW/SW Co-Verification." In *2022 Forum on Specification & Design Languages (FDL)*. IEEE. [https://doi.org/10.1109/fdl56239.2022.9925661][research_bruns_2022_b]
- Brus, Yelizaveta, Rungroj Maipradit, Earl T. Barr, and Shane McIntosh. 2025. "Rechecking Recheck Requests in Continuous Integration: An Empirical Study of OpenStack." In *2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase63991.2025.00121][research_brus_2025]
- Buchbinder, Niv, and Moran Feldman. 2024. "Deterministic Algorithm and Faster Algorithm for Submodular Maximization Subject to a Matroid Constraint." In *2024 IEEE 65th Annual Symposium on Foundations of Computer Science (FOCS)*. IEEE. [https://doi.org/10.1109/focs61266.2024.00050][research_buchbinder_2024]
- Budkowski, Stan, Ana Cavalli, and Elie Najm. 2017. "Erratum To: Formal Description Techniques and Protocol Specification, Testing and Verification." In *Formal Description Techniques and Protocol Specification, Testing and Verification*. Springer US. [https://doi.org/10.1007/978-0-387-35394-4\_29][research_budkowski_2017]
- Bui, Quang-Cuong, Ranindya Paramitha, Duc-Ly Vu, Fabio Massacci, and Riccardo Scandariato. 2023. "APR4Vul: An Empirical Study of Automatic Program Repair Techniques on Real-World Java Vulnerabilities." *Empirical Software Engineering* 29 (1): 18. [https://doi.org/10.1007/s10664-023-10415-7][research_bui_2023]
- Bushehri, Ahmad Shahnejat, Anas Balboul, Adel Belkhiri, Samira Keivanpour, Gabriela Nicolescu, and Michel Dagenais. 2026. "NOProbe: A NOP-Based Dynamic Binary Instrumentation Framework Using Binary Rewriting on x86." *IEEE Transactions on Dependable and Secure Computing* 23 (2): 3828–44. [https://doi.org/10.1109/tdsc.2025.3641055][research_bushehri_2026]
- Bytyn, Andreas, Rainer Leupers, and Gerd Ascheid. 2019. "An Application-Specific VLIW Processor with Vector Instruction Set for CNN Acceleration." In *2019 IEEE International Symposium on Circuits and Systems (ISCAS)*. IEEE. [https://doi.org/10.1109/iscas.2019.8702357][research_bytyn_2019]
- Cabrera-Arteaga, Javier, Nicholas Fitzgerald, Martin Monperrus, and Benoit Baudry. 2024. "Wasm-Mutate: Fast and Effective Binary Diversification for WebAssembly." *Computers & Security* 139: 103731. [https://doi.org/10.1016/j.cose.2024.103731][research_cabreraarteaga_2024]
- Cambou, Bertrand. 2017. "A XOR Data Compiler: Combined with Physical Unclonable Function for True Random Number Generation." In *2017 Computing Conference*. IEEE. [https://doi.org/10.1109/sai.2017.8252190][research_cambou_2017]
- Campbell, Jimmy. 2024. "A Methodology for Analysing Code Anomalies in Open-Source Software Using Big Data Analytics." In *2024 IEEE International Conference on Big Data (BigData)*. IEEE. [https://doi.org/10.1109/bigdata62323.2024.10825952][research_campbell_2024]
- Campos, Eduardo Cunha, and Marcelo de Almeida Maia. 2017. "Common Bug-Fix Patterns: A Large-Scale Observational Study." In *2017 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2017.55][research_campos_2017]
- Campos, Viola, Ridwan Shariffdeen, Adrian Ulges, and Yannic Noller. 2026. "Exploring Generalizable Automated Program Repair with Large Language Models." *IEEE Access* 14: 110543–58. [https://doi.org/10.1109/access.2026.3714292][research_campos_2026]
- Cañizares, Pablo C., Alberto Núñez, Rosa Filgueira, and Juan de Lara. 2023. "Parallel Mutation Testing for Large Scale Systems." *Cluster Computing* 27 (2): 2071–97. [https://doi.org/10.1007/s10586-023-04074-y][research_canizares_2023]
- Cao, Shangtong, Ningyu He, Yao Guo, and Haoyu Wang. 2023. "BREWasm: A General Static Binary Rewriting Framework for WebAssembly." In *Static Analysis*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-44245-2\_8][research_cao_2023]
- Cao, Xiuqi, Junyu Zhou, Yuhao Liu, Yunong Shi, and Gushu Li. 2025. "MarQSim: Reconciling Determinism and Randomness in Compiler Optimization for Quantum Simulation." *Proceedings of the ACM on Programming Languages* 9 (PLDI): 576–600. [https://doi.org/10.1145/3729269][research_cao_2025]
- Carminati, Andreu, Renan Augusto Starke, and Rômulo Silva de Oliveira. 2018. "On the Use of Static Branch Prediction to Reduce the Worst-Case Execution Time of Real-Time Applications." *Real-Time Systems* 54 (3): 537–61. [https://doi.org/10.1007/s11241-018-9306-y][research_carminati_2018]
- Carrasco, Manuel, Cristian Cadar, and Alastair F. Donaldson. 2025. "Scalable SMT Sampling for Floating-Point Formulas via Coverage-Guided Fuzzing." In *2025 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst62969.2025.10989031][research_carrasco_2025]
- Cassee, Nathan, Neil Ernst, Nicole Novielli, and Alexander Serebrenik. 2025. "Negativity in Self-Admitted Technical Debt: How Sentiment Influences Prioritization." *Empirical Software Engineering* 30 (2): 54. [https://doi.org/10.1007/s10664-024-10611-z][research_cassee_2025]
- Cassee, Nathan, Fiorella Zampetti, Nicole Novielli, Alexander Serebrenik, and Massimiliano Di Penta. 2022. "Self-Admitted Technical Debt and Comments’ Polarity: An Empirical Study." *Empirical Software Engineering* 27 (6): 139. [https://doi.org/10.1007/s10664-022-10183-w][research_cassee_2022]
- Castiglia, Timothy, and Stacy Patterson. 2019. "Distributed Submodular Maximization with Bounded Communication Cost." In *2019 IEEE 58th Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc40024.2019.9029710][research_castiglia_2019]
- Castro, Javier, Daniel Gómez, and Juan Tejada. 2009. "Polynomial Calculation of the Shapley Value Based on Sampling." *Computers & Operations Research* 36 (5): 1726–30. [https://doi.org/10.1016/j.cor.2008.04.004][research_castro_2009]
- Castro-Lopez, Oscar, and Ines F. Vega-Lopez. 2019. "Multi-Target Compiler for the Deployment of Machine Learning Models." In *2019 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo.2019.8661199][research_castrolopez_2019]
- Chaitin, G. J. 1982. "Register Allocation & Spilling via Graph Coloring." *ACM SIGPLAN Notices* 17 (6): 98–101. [https://doi.org/10.1145/872726.806984][research_chaitin_1982]
- Chakrabarti, Amit, and Sagar Kale. 2015. "Submodular Maximization Meets Streaming: Matchings, Matroids, and More." *Mathematical Programming* 154 (1–2): 225–47. [https://doi.org/10.1007/s10107-015-0900-7][research_chakrabarti_2015]
- Chakrabarty, Deeparnab, and Luc Coté. 2026. "A Primal-Dual Algorithm for Monotone Submodular Maximization." *Operations Research Letters* 65: 107387. [https://doi.org/10.1016/j.orl.2025.107387][research_chakrabarty_2026]
- Challita, Stephanie, Fawaz Paraiso, and Philippe Merle. 2017. "A Study of Virtual Machine Placement Optimization in Data Centers." In *Proceedings of the 7th International Conference on Cloud Computing and Services Science*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0006236500001535][research_challita_2017]
- Charguéraud, Arthur, and François Pottier. 2015. "Machine-Checked Verification of the Correctness and Amortized Complexity of an Efficient Union-Find Implementation." In *Interactive Theorem Proving*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-22102-1\_9][research_chargueraud_2015]
- Chavanon, Clément, Frédéric Besson, and Tristan Ninet. 2024. "PfComp: A Verified Compiler for Packet Filtering Leveraging Binary Decision Diagrams." In *Proceedings of the 13th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3636501.3636954][research_chavanon_2024]
- Che, James. 2025. "Finetune-Then-Merge: Democratizing Large Language Model Accessibility through Efficiency Optimization." In *2025 3rd International Conference on Foundation and Large Language Models (FLLM)*. IEEE. [https://doi.org/10.1109/fllm67465.2025.11391195][research_che_2025]
- Cheirdari, Foteini, and George Karabatis. 2018. "Analyzing False Positive Source Code Vulnerabilities Using Static Analysis Tools." In *2018 IEEE International Conference on Big Data (Big Data)*. IEEE. [https://doi.org/10.1109/bigdata.2018.8622456][research_cheirdari_2018]
- Chen, Boyuan, and Zhen Ming (Jack) Jiang. 2016. "Characterizing Logging Practices in Java-Based Open Source Software Projects – a Replication Study in Apache Software Foundation." *Empirical Software Engineering* 22 (1): 330–74. [https://doi.org/10.1007/s10664-016-9429-5][research_chen_2016_b]
- Chen, Juncheng, Weiwei Chen, and Zhi Cai. 2025b. "Key Operator Vectorization for LeNet and ResNet Based on Buddy Compiler." *Applied Sciences* 15 (17): 9523. [https://doi.org/10.3390/app15179523][research_chen_2025]
- Chen, An Ran, Tse-Hsun (Peter) Chen, and Shaowei Wang. 2021. "Demystifying the Challenges and Benefits of Analyzing User-Reported Logs in Bug Reports." *Empirical Software Engineering* 26 (1): 8. [https://doi.org/10.1007/s10664-020-09893-w][research_chen_2021]
- Chen, Hugh, Ian C. Covert, Scott M. Lundberg, and Su-In Lee. 2023a. "Algorithms to Estimate Shapley Value Feature Attributions." *Nature Machine Intelligence* 5 (6): 590–601. [https://doi.org/10.1038/s42256-023-00657-x][research_chen_2023_b]
- Chen, Ching-Yuan, and Jiun-Lang Huang. 2019. "Reinforcement-Learning-Based Test Program Generation for Software-Based Self-Test." In *2019 IEEE 28th Asian Test Symposium (ATS)*. IEEE. [https://doi.org/10.1109/ats47505.2019.00013][research_chen_2019_c]
- Chen, Xiaorong, Cheng Li, and Zhong B. Liu. 2024b. "VCNN: A Compiler of CNNs Based on MLIR for Multi-Core Vector Accelerators." In *2024 IEEE International Conference on High Performance Computing and Communications (HPCC)*. IEEE. [https://doi.org/10.1109/hpcc64274.2024.00024][research_chen_2024]
- Chen, Zihan, Bin Liu, and Hongmin W. Du. 2022. "Streaming Submodular Maximization under d-Knapsack Constraints." *Journal of Combinatorial Optimization* 45 (1): 15. [https://doi.org/10.1007/s10878-022-00951-1][research_chen_2022_b]
- Chen, Yuting, Ting Su, Chengnian Sun, Zhendong Su, and Jianjun Zhao. 2016. "Coverage-Directed Differential Testing of JVM Implementations." In *Proceedings of the 37th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/2908080.2908095][research_chen_2016]
- Chen, Junjie, Chenyao Suo, Jiajun Jiang, Peiqi Chen, and Xingjian Li. 2023b. "Compiler Test-Program Generation via Memoized Configuration Search." In *2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse48619.2023.00172][research_chen_2023]
- Chen, Tse-Hsun, Mark D. Syer, Weiyi Shang, et al. 2017. "Analytics-Driven Load Testing: An Industrial Experience Report on Load Testing of Large-Scale Systems." In *2017 IEEE/ACM 39th International Conference on Software Engineering: Software Engineering in Practice Track (ICSE-SEIP)*. IEEE. [https://doi.org/10.1109/icse-seip.2017.26][research_chen_2017]
- Chen, Yuexi, Gauri Vaidya, Alison O'Connor, and Meghana Kshirsagar. 2026. "From Natural Language to Interpretable Code: Automated Code Generation for Healthcare with Large Language Models: A Comparative Analysis." In *Proceedings of the 18th International Conference on Agents and Artificial Intelligence*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014717000004052][research_chen_2026]
- Chen, Junjie, Guancheng Wang, Dan Hao, Yingfei Xiong, Hongyu Zhang, and Lu Zhang. 2019b. "History-Guided Configuration Diversification for Compiler Test-Program Generation." In *2019 34th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase.2019.00037][research_chen_2019_b]
- Chen, Zhe, Ou Wei, Zhiqiu Huang, and Hongwei Xi. 2015. "Formal Semantics of Runtime Monitoring, Verification, Enforcement and Control." In *2015 International Symposium on Theoretical Aspects of Software Engineering*. IEEE. [https://doi.org/10.1109/tase.2015.11][research_chen_2015]
- Chen, Bingting, Weiqin Zou, Biyu Cai, et al. 2024a. "An Empirical Study on the Potential of Word Embedding Techniques in Bug Report Management Tasks." *Empirical Software Engineering* 29 (5): 122. [https://doi.org/10.1007/s10664-024-10510-3][research_chen_2024_b]
- Chicote, Marcos. 2017. "Startups and Technical Debt: Managing Technical Debt with Visual Thinking." In *2017 IEEE/ACM 1st International Workshop on Software Engineering for Startups (SoftStart)*. IEEE. [https://doi.org/10.1109/softstart.2017.6][research_chicote_2017]
- Chlipala, Adam. 2015a. "An Optimizing Compiler for a Purely Functional Web-Application Language." In *Proceedings of the 20th ACM SIGPLAN International Conference on Functional Programming*. ACM. [https://doi.org/10.1145/2784731.2784741][research_chlipala_2015]
- Chlipala, Adam. 2015b. "Session Details: Session 4A: Compiler Correctness." *ACM SIGPLAN Notices* 50 (1): 3264293. [https://doi.org/10.1145/3264293][research_chlipala_2015_b]
- Choi, Wonhyuk. 2021. "Can Reactive Synthesis and Syntax-Guided Synthesis Be Friends?" In *Companion Proceedings of the 2021 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity*. ACM. [https://doi.org/10.1145/3484271.3484972][research_choi_2021]
- Choi, Wonhyuk, Bernd Finkbeiner, Ruzica Piskac, and Mark Santolucito. 2022. "Can Reactive Synthesis and Syntax-Guided Synthesis Be Friends?" In *Proceedings of the 43rd ACM SIGPLAN International Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3519939.3523429][research_choi_2022]
- Choi, GyeongTaek, and Seungho Jeon. 2026. "Stack-Based Static WebAssembly Binary Slicing and Mutation for Generating Valid Sub-Binaries." *Scientific Reports* 16 (1): 10910. [https://doi.org/10.1038/s41598-026-45837-y][research_choi_2026]
- Chowdhury, Proma, and Kazi Sakib. 2025. "DeepUIFuzz: A Guided Fuzzing Strategy for Testing UI Component Detection Models." In *2025 IEEE/ACM International Workshop on Search-Based and Fuzz Testing (SBFT)*. IEEE. [https://doi.org/10.1109/sbft66712.2025.00016][research_chowdhury_2025]
- Christakis, Maria, and Valentin Wüstholz. 2016. "Bounded Abstract Interpretation." In *Static Analysis*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-662-53413-7\_6][research_christakis_2016]
- Cibir, Esra, and Tulin Ercelebi Ayyildiz. 2022. "An Empirical Study on Software Test Effort Estimation for Defense Projects." *IEEE Access* 10: 48082–87. [https://doi.org/10.1109/access.2022.3172326][research_cibir_2022]
- Clement, Valentin, and Jeffrey S. Vetter. 2021. "Flacc: Towards OpenACC Support for Fortran in the LLVM Ecosystem." In *2021 IEEE/ACM 7th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvmhpc54804.2021.00007][research_clement_2021]
- Cockx, Jesper, and Dominique Devriese. 2017. "Lifting Proof-Relevant Unification to Higher Dimensions." In *Proceedings of the 6th ACM SIGPLAN Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3018610.3018612][research_cockx_2017]
- Condevaux, Charles, Sébastien Harispe, and Stéphane Mussard. 2023. "Fair and Efficient Alternatives to Shapley-Based Attribution Methods." In *Machine Learning and Knowledge Discovery in Databases*. Springer International Publishing. [https://doi.org/10.1007/978-3-031-26387-3\_19][research_condevaux_2023]
- Conforti, Michele, and Gérard Cornuéjols. 1984. "Submodular Set Functions, Matroids and the Greedy Algorithm: Tight Worst-Case Bounds and Some Generalizations of the Rado-Edmonds Theorem." *Discrete Applied Mathematics* 7 (3): 251–74. [https://doi.org/10.1016/0166-218x(84)90003-9][research_conforti_cornuejols_1984]
- Coole, James, and Greg Stitt. 2015. "Adjustable-Cost Overlays for Runtime Compilation." In *2015 IEEE 23rd Annual International Symposium on Field-Programmable Custom Computing Machines*. IEEE. [https://doi.org/10.1109/fccm.2015.49][research_coole_2015]
- Coppola, Riccardo, Luca Ardito, Marco Torchiano, and Emil Alegroth. 2020. "Translation from Visual to Layout-Based Android Test Cases: A Proof of Concept." In *2020 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw50294.2020.00027][research_coppola_2020]
- Corah, Micah, and Nathan Michael. 2018a. "Distributed Matroid-Constrained Submodular Maximization for Multi-Robot Exploration: Theory and Practice." *Autonomous Robots* 43 (2): 485–501. [https://doi.org/10.1007/s10514-018-9778-6][research_corah_2018_b]
- Corah, Micah, and Nathan Michael. 2018b. "Distributed Submodular Maximization on Partition Matroids for Planning on Large Sensor Networks." In *2018 IEEE Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc.2018.8619396][research_corah_2018]
- Cordeiro, André, and Edson Oliveira Jr. 2025a. "Reproducibility Practices of Software Engineering Controlled Experiments: Survey and Prospective Actions." In *Proceedings of the 27th International Conference on Enterprise Information Systems*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0013475600003929][research_cordeiro_2025]
- Cordeiro, André, and Edson Oliveira Jr. 2025b. "Reviewing Reproducibility in Software Engineering Research." In *Proceedings of the 27th International Conference on Enterprise Information Systems*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0013456000003929][research_cordeiro_2025_b]
- Corder, Kevin, and Keith Decker. 2019. "Shapley Value Approximation with Divisive Clustering." In *2019 18th IEEE International Conference On Machine Learning And Applications (ICMLA)*. IEEE. [https://doi.org/10.1109/icmla.2019.00044][research_corder_2019]
- Corrias, Lorenzo, Lorenzo Pisu, Davide Maiorca, and Giorgio Giacinto. 2026. "An Analysis of Modern Web Security Vulnerabilities inside WebAssembly Applications." In *Proceedings of the 12th International Conference on Information Systems Security and Privacy*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014597200004061][research_corrias_2026]
- Costa, Jessica Junia Santillo, Romulo Silva de Oliveira, and Luis Fernando Arcaro. 2021. "Use of Measurements in Worst-Case Execution Time Estimation for Real-Time Systems." In *2021 XI Brazilian Symposium on Computing Systems Engineering (SBESC)*. IEEE. [https://doi.org/10.1109/sbesc53686.2021.9628230][research_costa_2021]
- Costa, Gabriele, Alessio Merlo, Luca Verderame, and Alessandro Armando. 2018. "Automatic Security Verification of Mobile App Configurations." *Future Generation Computer Systems* 80: 519–36. [https://doi.org/10.1016/j.future.2016.06.014][research_costa_2018]
- Courtnage, Christie, and Evgueni Smirnov. 2021. "Shapley-Value Data Valuation for Semi-Supervised Learning." In *Discovery Science*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-88942-5\_8][research_courtnage_2021]
- Cousot, Patrick, and Radhia Cousot. 1977. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." In *Proceedings of the 4th ACM SIGACT-SIGPLAN symposium on Principles of programming languages - POPL '77*. ACM Press. [https://doi.org/10.1145/512950.512973][research_cousot_1977]
- Crepalde, Mirlaine, Augusto Mafra, Lucas Cavalini, et al. 2025. "Automatic Test Case Generation for Jasper App HDL Compiler: An Industry Experience." In *Proceedings of the 34th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3708493.3712681][research_crepalde_2025]
- Cui, Songqiao, and Josep Balasch. 2024. "Configurable Loop Shuffling via Instruction Set Extensions." In *2024 IEEE 35th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap61560.2024.00021][research_cui_2024]
- Cui, Pingfei, Shanhong He, Mengyao Chen, and Haoran Li. 2025c. "Research on Compiler Optimization Technology Based on Reinforcement Learning." In *2025 5th International Conference on Electronic Information Engineering and Computer Science (EIECS)*. IEEE. [https://doi.org/10.1109/eiecs67708.2025.11283571][research_cui_2025_c]
- Cui, Enfang, Tianzheng Li, and Qian Wei. 2023a. "RISC-V Instruction Set Architecture Extensions: A Survey." *IEEE Access* 11: 24696–24711. [https://doi.org/10.1109/access.2023.3246491][research_cui_2023]
- Cui, Jinhua, Qiao Peng, Yiwen Yao, Ke Ye, and Jiliang Zhang. 2025b. "IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications." In *2025 62nd ACM/IEEE Design Automation Conference (DAC)*. IEEE. [https://doi.org/10.1109/dac63849.2025.11132848][research_cui_2025]
- Cummins, Chris, Volker Seeker, Dejan Grubisic, et al. 2025. "LLM Compiler: Foundation Language Models for Compiler Optimization." In *Proceedings of the 34th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3708493.3712691][research_cummins_2025]
- Cynthia, Shamse Tasnim, Nuri Almarimi, and Banani Roy. 2025. "How Do Community Smells Influence Self-Admitted Technical Debt in Machine Learning Projects?" In *2025 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem64174.2025.00072][research_cynthia_2025]
- D'Silva, Vijay, Mathias Payer, and Dawn Song. 2015. "The Correctness-Security Gap in Compiler Optimization." In *2015 IEEE Security and Privacy Workshops*. IEEE. [https://doi.org/10.1109/spw.2015.33][research_dsilva_2015]
- Da Roza, Enrique A., Jackson A. Prado Lima, Rogerio C. Silva, and Silvia Regina Vergilio. 2022. "Machine Learning Regression Techniques for Test Case Prioritization in Continuous Integration Environment." In *2022 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner53432.2022.00034][research_daroza_2022]
- Dahiya, Manjeet, and Sorav Bansal. 2017. "Modeling Undefined Behaviour Semantics for Checking Equivalence across Compiler Optimizations." In *Hardware and Software: Verification and Testing*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-70389-3\_2][research_dahiya_2017]
- Dai, Xiaotian, and Alan Burns. 2017. "Predicting Worst-Case Execution Time Trends in Long-Lived Real-Time Systems." In *Reliable Software Technologies – Ada-Europe 2017*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-60588-3\_6][research_dai_2017]
- Daoudi, Nadia, Kevin Allix, Tegawendé F. Bissyandé, and Jacques Klein. 2021. "Lessons Learnt on Reproducibility in Machine Learning Based Android Malware Detection." *Empirical Software Engineering* 26 (4): 74. [https://doi.org/10.1007/s10664-021-09955-7][research_daoudi_2021]
- Daudier, Dorian, Trinh Ngoc Quoc Bao, and Kazuhiro Ogata. 2018. "A Proof Score Approach to Formal Verification of an Imperative Programming Language Compiler." In *Structured Object-Oriented Formal Language and Method*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-90104-6\_13][research_daudier_2018]
- Daukševič, Daniel, Roberto Magán-Carrión, and Linas Laibinis. 2026. "Towards Verified Security: Formal Methods for LLM-Based Defenses." In *ICC 2026 - IEEE International Conference on Communications*. IEEE. [https://doi.org/10.1109/icc59461.2026.11587351][research_dauksevic_2026]
- Davidson, Jack W., and Christopher W. Fraser. 1984. "Automatic Generation of Peephole Optimizations." In *Proceedings of the 1984 SIGPLAN symposium on Compiler construction - SIGPLAN '84*. ACM Press. [https://doi.org/10.1145/502874.502885][research_davidson_fraser_1984]
- De Bosschere, Koen, and Rainer Leupers. 2018. "HiPEAC Compilation Architecture." In *2018 7th Mediterranean Conference on Embedded Computing (MECO)*. IEEE. [https://doi.org/10.1109/meco.2018.8405949][research_debosschere_2018]
- de Ferrière, François, Yves Janin, and Sirine Mechmech. 2026. "SecSwift, a Compiler-Based Framework for Software Countermeasures in Cybersecurity." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395204][research_deferriere_2026]
- de Lima, Bruno Santos, Rogerio Eduardo Garcia, and Danilo Medeiros Eler. 2022. "Toward Prioritization of Self-Admitted Technical Debt: An Approach to Support Decision to Payment." *Software Quality Journal* 30 (3): 729–55. [https://doi.org/10.1007/s11219-021-09578-7][research_delima_2022]
- De Macedo, Joao, Rui Abreu, Rui Pereira, and Joao Saraiva. 2021. "On the Runtime and Energy Performance of WebAssembly: Is WebAssembly Superior to JavaScript Yet?" In *2021 36th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW)*. IEEE. [https://doi.org/10.1109/asew52652.2021.00056][research_demacedo_2021]
- De Macedo, Joao, Rui Abreu, Rui Pereira, and Joao Saraiva. 2022. "WebAssembly versus JavaScript: Energy and Runtime Performance." In *2022 International Conference on ICT for Sustainability (ICT4S)*. IEEE. [https://doi.org/10.1109/ict4s55073.2022.00014][research_demacedo_2022]
- de Magalhães, Cleyton V. C., Fabio Q. B. da Silva, Ronnie E. S. Santos, and Marcos Suassuna. 2015. "Investigations about Replication of Empirical Studies in Software Engineering: A Systematic Mapping Study." *Information and Software Technology* 64: 76–101. [https://doi.org/10.1016/j.infsof.2015.02.001][research_demagalhaes_2015]
- De Martino, Vincenzo, Gianmario Voria, Ciro Troiano, Gemma Catolino, and Fabio Palomba. 2025. "Examining the Impact of Bias Mitigation Algorithms on the Sustainability of ML-Enabled Systems: A Benchmark Study." *Journal of Systems and Software* 230: 112458. [https://doi.org/10.1016/j.jss.2025.112458][research_demartino_2025]
- de Souza Magalhães, José Wesley, Shideh Hashemian, Alexander Brauckmann, Jackson Woodruff, Elizabeth Polgreen, and Michael F. P. O'Boyle. 2026. "Accelerating Sparse Algebra with Program Synthesis." In *Proceedings of the 35th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3771775.3786281][research_desouzamagalha_2026]
- Dean, C. B. 1992. "Testing for Overdispersion in Poisson and Binomial Regression Models." *Journal of the American Statistical Association* 87 (418): 451–57. [https://doi.org/10.1080/01621459.1992.10475225][research_dean_1992]
- Dell'Anna, Davide, Fatma Başak Aydemir, and Fabiano Dalpiaz. 2022. "Evaluating Classifiers in SE Research: The ECSER Pipeline and Two Replication Studies." *Empirical Software Engineering* 28 (1): 3. [https://doi.org/10.1007/s10664-022-10243-1][research_dellanna_2022]
- Delmas, David, Abdelraouf Ouadjaout, and Antoine Miné. 2021. "Static Analysis of Endian Portability by Abstract Interpretation." In *Static Analysis*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-88806-0\_5][research_delmas_2021]
- DeMillo, R. A., R. J. Lipton, and F. G. Sayward. 1978. "Hints on Test Data Selection: Help for the Practicing Programmer." *Computer* 11 (4): 34–41. [https://doi.org/10.1109/c-m.1978.218136][research_demillo_1978]
- Demmler, Daniel, Stefan Katzenbeisser, Thomas Schneider, Tom Schuster, and Christian Weinert. 2021. "Improved Circuit Compilation for Hybrid MPC via Compiler Intermediate Representation." In *Proceedings of the 18th International Conference on Security and Cryptography*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0010540500002998][research_demmler_2021]
- Denaro, Giovanni, and Luca Gugliemo. 2025. "Automated Test Generation from Program Documentation Encoded in Code Comments." In *2025 IEEE/ACM International Conference on Automation of Software Test (AST)*. IEEE. [https://doi.org/10.1109/ast66626.2025.00012][research_denaro_2025]
- Deng, Chaoqiang, and Kedar S. Namjoshi. 2018. "Securing a Compiler Transformation." *Formal Methods in System Design* 53 (2): 166–88. [https://doi.org/10.1007/s10703-017-0313-8][research_deng_2018]
- Dennis, Kevin, Bianca Dehaan, Parisa Momeni, Gabriel Laverghetta, and Jay Ligatti. 2024. "Large-Scale Analysis of GitHub and CVEs to Determine Prevalence of SQL Concatenations." In *Proceedings of the 21st International Conference on Security and Cryptography*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0012835200003767][research_dennis_2024]
- Denny, Joel E., Seyong Lee, and Jeffrey S. Vetter. 2018. "CLACC: Translating OpenACC to OpenMP in Clang." In *2018 IEEE/ACM 5th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2018.8639349][research_denny_2018]
- Denzler, Patrick, Thomas Fruhwirth, Andreas Kirchberger, Martin Schoeberl, and Wolfgang Kastner. 2021. "Experiences from Adjusting Industrial Software for Worst-Case Execution Time Analysis." In *2021 IEEE 24th International Symposium on Real-Time Distributed Computing (ISORC)*. IEEE. [https://doi.org/10.1109/isorc52013.2021.00019][research_denzler_2021]
- Di Giacomo, Francesco, Mohamed Abbadi, Agostino Cortesi, Pieter Spronck, and Giuseppe Maggiore. 2017. "Metacasanova: An Optimized Meta-Compiler for Domain-Specific Languages." In *Proceedings of the 10th ACM SIGPLAN International Conference on Software Language Engineering*. ACM. [https://doi.org/10.1145/3136014.3136015][research_digiacomo_2017]
- Diaconescu, Răzvan. 2020. "Introducing H, an Institution-Based Formal Specification and Verification Language." *Logica Universalis* 14 (2): 259–77. [https://doi.org/10.1007/s11787-020-00249-y][research_diaconescu_2020]
- Diamantopoulos, Dionysios, Burkhard Ringlein, Mitra Purandare, Gagandeep Singh, and Christoph Hagleitner. 2020. "Agile Autotuning of a Transprecision Tensor Accelerator Overlay for TVM Compiler Stack." In *2020 30th International Conference on Field-Programmable Logic and Applications (FPL)*. IEEE. [https://doi.org/10.1109/fpl50879.2020.00058][research_diamantopoulos_2020]
- Ding, Mi, Kaipeng Lin, Wang Lin, and Zuohua Ding. 2022b. "A Novel Counterexample-Guided Inductive Synthesis Framework for Barrier Certificate Generation." In *2022 IEEE 33rd International Symposium on Software Reliability Engineering (ISSRE)*. IEEE. [https://doi.org/10.1109/issre55969.2022.00034][research_ding_2022]
- Dong, Jiabao, and Lei Ren. 2024. "A Digital Twin Modeling Code Generation Framework Based on Large Language Model." In *IECON 2024 - 50th Annual Conference of the IEEE Industrial Electronics Society*. IEEE. [https://doi.org/10.1109/iecon55916.2024.10905976][research_dong_2024]
- Dong, Wang, Zhao Rongcai, Wang Qi, and Li Yingying. 2016. "Outer-Loop Auto-Vectorization for SIMD Architectures Based on Open64 Compiler." In *2016 17th International Conference on Parallel and Distributed Computing, Applications and Technologies (PDCAT)*. IEEE. [https://doi.org/10.1109/pdcat.2016.020][research_dong_2016]
- Doshi, Karishma, Suyash Shukla, and Sandeep Kumar. 2026. "Towards Interpretable Ensemble Learning for Software Effort Estimation." In *Proceedings of the 21st International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0015043100004015][research_doshi_2026]
- Dougherty, Quinn, and Ronak Mehta. 2025. "Proving the Coding Interview: A Benchmark for Formally Verified Code Generation." In *2025 IEEE/ACM International Workshop on Large Language Models for Code (LLM4Code)*. IEEE. [https://doi.org/10.1109/llm4code66737.2025.00014][research_dougherty_2025]
- Downie, Andrew, Bahman Gharesifard, and Stephen L. Smith. 2022. "A Programming Approach for Worst-Case Studies in Distributed Submodular Maximization." In *2022 IEEE 61st Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc51059.2022.9992771][research_downie_2022]
- Drawel, Nagat, Hongyang Qu, Jamal Bentahar, and Elhadi Shakshuki. 2020. "Specification and Automatic Verification of Trust-Based Multi-Agent Systems." *Future Generation Computer Systems* 107: 1047–60. [https://doi.org/10.1016/j.future.2018.01.040][research_drawel_2020]
- Drescher, Florian, and Alexis Engelke. 2024. "Fast Template-Based Code Generation for MLIR." In *Proceedings of the 33rd ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3640537.3641567][research_drescher_2024]
- Drescher, Florian, and Alexis Engelke. 2026. "Synthesizing Instruction Selection Back-Ends from ISA Specifications Made Practical." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395203][research_drescher_2026]
- Dubey, Kalka, S. C. Sharma, and Mohit Kumar. 2023. "Resource Optimization Based Virtual Machine Allocation Technique in Cloud Computing Domain." In *2023 14th International Conference on Computing Communication and Networking Technologies (ICCCNT)*. IEEE. [https://doi.org/10.1109/icccnt56998.2023.10307781][research_dubey_2023]
- Ducasse, Quentin, Pascal Cotret, and Loïc Lagadec. 2023. "JIT Compiler Security through Low-Cost RISC-V Extension." In *2023 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)*. IEEE. [https://doi.org/10.1109/ipdpsw59300.2023.00032][research_ducasse_2023]
- Duijn, Maarten, Adam Kucera, and Alberto Bacchelli. 2015. "Quality Questions Need Quality Code: Classifying Code Fragments on Stack Overflow." In *2015 IEEE/ACM 12th Working Conference on Mining Software Repositories*. IEEE. [https://doi.org/10.1109/msr.2015.51][research_duijn_2015]
- Dyer, Robert, Hoan Anh Nguyen, Hridesh Rajan, and Tien N. Nguyen. 2013. "Boa: A Language and Infrastructure for Analyzing Ultra-Large-Scale Software Repositories." In *2013 35th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse.2013.6606588][research_dyer_2013]
- Edbert, Joshua Aldrich, Sahrima Jannat Oishwee, Shubhashis Karmakar, Zadia Codabux, and Roberto Verdecchia. 2023. "Exploring Technical Debt in Security Questions on Stack Overflow." In *2023 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem56168.2023.10304868][research_edbert_2023]
- Eisenkraemer, Gabriel H., Fernando G. Moraes, Leonardo L. de Oliveira, and Everton Carara. 2020. "Lightweight Cryptographic Instruction Set Extension on Xtensa Processor." In *2020 IEEE International Symposium on Circuits and Systems (ISCAS)*. IEEE. [https://doi.org/10.1109/iscas45731.2020.9180579][research_eisenkraemer_2020]
- Eissa, Ahmed S., Mahmoud A. Elmohr, Mostafa A. Saleh, Khaled E. Ahmed, and Mohammed M. Farag. 2016. "SHA-3 Instruction Set Extension for a 32-Bit RISC Processor Architecture." In *2016 IEEE 27th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap.2016.7760804][research_eissa_2016]
- El Koutbi, Salma, and Ali Idri. 2017. "Entropy-Based Framework Dealing with Error in Software Development Effort Estimation." In *Proceedings of the 12th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0006312901950202][research_elkoutbi_2017]
- El Koutbi, Salma, Ali Idri, and Alain Abran. 2018. "Empirical Evaluation of an Entropy-Based Approach to Estimation Variation of Software Development Effort." *Journal of Software: Evolution and Process* 31 (3): e2149. [https://doi.org/10.1002/smr.2149][research_elkoutbi_2018]
- Elbaum, S., A. G. Malishevsky, and G. Rothermel. 2002. "Test Case Prioritization: A Family of Empirical Studies." *IEEE Transactions on Software Engineering* 28 (2): 159–82. [https://doi.org/10.1109/32.988497][research_elbaum_2002]
- Elmohr, Mahmoud A., Mostafa A. Saleh, Ahmed S. Eissa, Khaled E. Ahmed, and Mohammed M. Farag. 2016. "Hardware Implementation of a SHA-3 Application-Specific Instruction Set Processor." In *2016 28th International Conference on Microelectronics (ICM)*. IEEE. [https://doi.org/10.1109/icm.2016.7847921][research_elmohr_2016]
- Engel, Daniel, Freek Verbeek, and Binoy Ravindran. 2023. "BIRD: A Binary Intermediate Representation for Formally Verified Decompilation of X86-64 Binaries." In *Tests and Proofs*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-38828-6\_1][research_engel_2023]
- Engelke, Alexis, and Martin Schulz. 2020. "Robust Practical Binary Optimization at Run-Time Using LLVM." In *2020 IEEE/ACM 6th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC) and Workshop on Hierarchical Parallelism for Exascale Computing (HiPar)*. IEEE. [https://doi.org/10.1109/llvmhpchipar51896.2020.00011][research_engelke_2020]
- Engelke, Alexis, and Tobias Schwarz. 2024. "Compile-Time Analysis of Compiler Frameworks for Query Compilation." In *2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo57630.2024.10444856][research_engelke_2024]
- Erer, Eray, Aysun Bozanta, Turgay Aytac, and Ayse Basar. 2025. "A Fully Automated Agent for End-to-End Code Translation and Validation." In *2025 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem64174.2025.00058][research_erer_2025]
- Eriksson, Anders, and Birgitta Lindström. 2016. "UML Associations: Reducing the Gap in Test Coverage between Model and Code." In *Proceedings of the 4th International Conference on Model-Driven Engineering and Software Development*. SCITEPRESS - Science and and Technology Publications. [https://doi.org/10.5220/0005745205890599][research_eriksson_2016]
- Erkuş, Ekin Can, Cansen Çağlayan Yılmaz, and Mustafa Umut Demirezen. 2026. "ArkTS Code Generation: A Comprehensive Evaluation with Large Language Models." *Empirical Software Engineering* 31 (4): 109. [https://doi.org/10.1007/s10664-026-10844-0][research_erkus_2026]
- Ertl, M. Anton. 1999. "Optimal Code Selection in DAGs." In *Proceedings of the 26th ACM SIGPLAN-SIGACT symposium on Principles of programming languages*. ACM. [https://doi.org/10.1145/292540.292562][research_ertl_1999]
- Esary, J. D., and F. Proschan. 1963. "Coherent Structures of Non-Identical Components." *Technometrics* 5 (2): 191–209. [https://doi.org/10.1080/00401706.1963.10490075][research_esary_proschan_1963]
- Even-Mendoza, Karine, Cristian Cadar, and Alastair F. Donaldson. 2022. "CsmithEdge: More Effective Compiler Testing by Handling Undefined Behaviour Less Conservatively." *Empirical Software Engineering* 27 (6): 129. [https://doi.org/10.1007/s10664-022-10146-1][research_evenmendoza_2022]
- Fagerholm, Fabian, Christoph Becker, Alexander Chatzigeorgiou, et al. 2019. "Temporal Discounting in Software Engineering: A Replication Study." In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2019.8870161][research_fagerholm_2019]
- Fahimullah, Muhammad, Yasir Faheem, and Naveed Ahmad. 2019. "Collaboration Formation and Profit Sharing between Software Development Firms: A Shapley Value Based Cooperative Game." *IEEE Access* 7: 42859–73. [https://doi.org/10.1109/access.2019.2908459][research_fahimullah_2019]
- Fakhir, Muhammad Ilyas, and Syed Asad Raza Kazmi. 2018. "Formal Specification and Verification of Self-Adaptive Concurrent Systems." *IEEE Access* 6: 34790–34803. [https://doi.org/10.1109/access.2018.2849821][research_fakhir_2018]
- Falk, Heiko, and Paul Lokuciejewski. 2019. "Correction To: A Compiler Framework for the Reduction of Worst-Case Execution Times." *Real-Time Systems* 55 (4): 925–925. [https://doi.org/10.1007/s11241-019-09337-9][research_falk_2019]
- Fan, Xumeng, Jian Li, and Chang Deng. 2025. "Hybrid WebAssembly-Container Orchestration in Embedded Heterogeneous Scenarios." In *2025 5th International Conference on Artificial Intelligence and Industrial Technology Applications (AIITA)*. IEEE. [https://doi.org/10.1109/aiita65135.2025.11047894][research_fan_2025]
- Fan, Yongdong, Haokun Mao, and Qiong Li. 2023. "A Model-Agnostic Feature Attribution Approach to Magnetoencephalography Predictions Based on Shapley Value." *IEEE Journal of Biomedical and Health Informatics* 27 (5): 2524–35. [https://doi.org/10.1109/jbhi.2023.3248139][research_fan_2023]
- Fan, Zhenye, Guixin Ye, Tianmin Hu, and Zhanyong Tang. 2024. "History-Driven Compiler Fuzzing via Assembling and Scheduling Bug-Triggering Code Segments." In *2024 IEEE 35th International Symposium on Software Reliability Engineering (ISSRE)*. IEEE. [https://doi.org/10.1109/issre62328.2024.00040][research_fan_2024]
- Fang, Xiangxin, Jiaqin Kang, Rodrigo Rocha, Sam Ainsworth, and Lev Mukhanov. 2026. "LLM-VeriOpt: Verification-Guided Reinforcement Learning for LLM-Based Compiler Optimization." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395239][research_fang_2026]
- Färber, Michael. 2023. "Terms for Efficient Proof Checking and Parsing." In *Proceedings of the 12th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3573105.3575686][research_farber_2023]
- Fedasyuk, Dmytro, Ratybor Chopey, and Bohdan Knysh. 2017. "Architecture of a Tool for Automated Testing the Worst-Case Execution Time of Real-Time Embedded Systems' Firmware." In *2017 14th International Conference The Experience of Designing and Application of CAD Systems in Microelectronics (CADSM)*. IEEE. [https://doi.org/10.1109/cadsm.2017.7916134][research_fedasyuk_2017]
- Felker, Nicholas. 2020. "Design of Cyanobyte: An Intermediate Representation to Standardize Digital Peripheral Datasheets for Automatic Code Generation." In *2020 IEEE Sensors Applications Symposium (SAS)*. IEEE. [https://doi.org/10.1109/sas48726.2020.9220074][research_felker_2020]
- Feng, Qiong, Xiaotian Ma, Ziyuan Feng, Marat Akhin, Wei Song, and Peng Liang. 2025. "Finding Compiler Bugs through Cross-Language Code Generator and Differential Testing." *Proceedings of the ACM on Programming Languages* 9 (OOPSLA2): 2843–69. [https://doi.org/10.1145/3763152][research_feng_2025]
- Fenton, N. E., and N. Ohlsson. 2000. "Quantitative Analysis of Faults and Failures in a Complex Software System." *IEEE Transactions on Software Engineering* 26 (8): 797–814. [https://doi.org/10.1109/32.879815][research_fenton_ohlsson_2000]
- Ferchichi, Olfa, Raoudha Beltaifa, and Lamia Labed. 2024. "Association Rule Learning Based Approach to Automatic Generation of Feature Model Configurations." In *Proceedings of the 19th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0012742000003687][research_ferchichi_2024]
- Ferdinand, Christian, and Reinhard Wilhelm. 1999. "Efficient and Precise Cache Behavior Prediction for Real-Time Systems." *Real-Time Systems* 17 (2–3): 131–81. [https://doi.org/10.1023/a:1008186323068][research_ferdinand_wilhelm_1999]
- Fernandes, Ana, Luís Crespo, Nuno Neves, Pedro Tomás, Nuno Roma, and Gabriel Falcao. 2025. "Functional Validation of the RISC-V Unlimited Vector Extension." *IEEE Embedded Systems Letters* 17 (1): 2–5. [https://doi.org/10.1109/les.2024.3416820][research_fernandes_2025]
- Ferretti, Claudio, and Martina Saletta. 2023. "Naturalness in Source Code Summarization. How Significant Is It?" In *2023 IEEE/ACM 31st International Conference on Program Comprehension (ICPC)*. IEEE. [https://doi.org/10.1109/icpc58990.2023.00027][research_ferretti_2023]
- Finkel, Hal, Alex McCaskey, Tobi Popoola, Dmitry Lyakh, and Johannes Doerfert. 2020. "Really Embedding Domain-Specific Languages into C++." In *2020 IEEE/ACM 6th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC) and Workshop on Hierarchical Parallelism for Exascale Computing (HiPar)*. IEEE. [https://doi.org/10.1109/llvmhpchipar51896.2020.00012][research_finkel_2020]
- Finkel, Hal, David Poliakoff, Jean-Sylvain Camier, and David F. Richards. 2019. "ClangJIT: Enhancing C++ with Just-in-Time Compilation." In *2019 IEEE/ACM International Workshop on Performance, Portability and Productivity in HPC (P3HPC)*. IEEE. [https://doi.org/10.1109/p3hpc49587.2019.00013][research_finkel_2019]
- Fisman, Dana, Rishabh Singh, and Armando Solar-Lezama. 2021. "Special Issue on Syntax-Guided Synthesis Preface." *Formal Methods in System Design* 58 (3): 469–70. [https://doi.org/10.1007/s10703-021-00386-0][research_fisman_2021]
- Flatt, Matthew, and R. Kent Dybvig. 2020. "Compiler and Runtime Support for Continuation Marks." In *Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3385412.3385981][research_flatt_2020]
- Flemstrom, Daniel, Henrik Jonsson, Eduard Paul Enoiu, and Wasif Afzal. 2021. "Industrial Scale Passive Testing with T-EARS." In *2021 14th IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst49551.2021.00047][research_flemstrom_2021]
- Foundjem, Armstrong, and Bram Adams. 2021. "Release Synchronization in Software Ecosystems: Empirical Study on OpenStack." *Empirical Software Engineering* 26 (3): 34. [https://doi.org/10.1007/s10664-020-09929-1][research_foundjem_2021]
- Fox, Anthony, Magnus O. Myreen, Yong Kiam Tan, and Ramana Kumar. 2017. "Verified Compilation of CakeML to Multiple Machine-Code Targets." In *Proceedings of the 6th ACM SIGPLAN Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3018610.3018621][research_fox_2017]
- Frankel, Sophia F., and Krishnendu Ghosh. 2021. "Machine Learning Approaches for Authorship Attribution Using Source Code Stylometry." In *2021 IEEE International Conference on Big Data (Big Data)*. IEEE. [https://doi.org/10.1109/bigdata52589.2021.9671332][research_frankel_2021]
- Fromherz, Aymeric, Abdelraouf Ouadjaout, and Antoine Miné. 2018. "Static Value Analysis of Python Programs by Abstract Interpretation." In *NASA Formal Methods*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-77935-5\_14][research_fromherz_2018]
- Frontiers Production Office. 2023. "Erratum: Weighted Shapley Value: A Cooperative Game Theory for Loss Allocation in Distribution Systems." *Frontiers in Energy Research* 11: 1212388. [https://doi.org/10.3389/fenrg.2023.1212388][research_anon_2023_b]
- Fu, Anmin, Pengyu Xu, Jichunyang Li, Boyu Kuang, and Yansong Gao. 2025. "InstructRepair: Instruct Large Language Models with Rich Bug Information for Automated Program Repair." *IEEE Transactions on Information Forensics and Security* 20: 10864–78. [https://doi.org/10.1109/tifs.2025.3618407][research_fu_2025]
- Fumero, Juan, Michel Steuwer, Lukas Stadler, and Christophe Dubach. 2017. "Just-In-Time GPU Compilation for Interpreted Languages with Partial Evaluation." In *Proceedings of the 13th ACM SIGPLAN/SIGOPS International Conference on Virtual Execution Environments*. ACM. [https://doi.org/10.1145/3050748.3050761][research_fumero_2017]
- Furia, Carlo A., and Abhishek Tiwari. 2024. "Challenges of Multilingual Program Specification and Analysis." In *Leveraging Applications of Formal Methods, Verification and Validation. Specification and Verification*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-75380-0\_8][research_furia_2024]
- Furia, Carlo A., and Richard Torkar. 2026. "Mitigating Omitted Variable Bias in Empirical Software Engineering." *Empirical Software Engineering* 31 (5): 123. [https://doi.org/10.1007/s10664-026-10851-1][research_furia_2026]
- Găceanu, Radu, Arnold Szederjesi-Dragomir, and Andreea Vescan. 2024. "Leveraging Rough Sets for Enhanced Test Case Prioritization in a Continuous Integration Context." In *2024 IEEE International Conference on Software Analysis, Evolution and Reengineering - Companion (SANER-C)*. IEEE. [https://doi.org/10.1109/saner-c62648.2024.00030][research_gaceanu_2024]
- Galanis, Maximilian, Vincent Dietrich, Bernd Kast, and Michael Fiegert. 2020. "RTFM: Towards Understanding Source Code Using Natural Language Processing." In *Proceedings of the 17th International Conference on Informatics in Control, Automation and Robotics*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0009826604300437][research_galanis_2020]
- Gao, Zhanyuan, Laiping Zhao, and Haonan Chen. 2022. "A Trigonometric Function Instruction Set Extension Method Based on RISC-V." In *2022 IEEE/ACIS 22nd International Conference on Computer and Information Science (ICIS)*. IEEE. [https://doi.org/10.1109/icis54925.2022.9882453][research_gao_2022]
- Garcia-Alvarado, Carlos, and Carlos Ordonez. 2020. "Querying Big Source Code." In *2020 IEEE International Conference on Big Data (Big Data)*. IEEE. [https://doi.org/10.1109/bigdata50022.2020.9378481][research_garciaalvarado_2020]
- Garg, Kamal, Rohit Agarwal, and Shashi Shekhar. 2024. "Explainable Test Case Prioritization in Continuous Integration through Incremental Learning Approach." In *2024 International Conference on Communication, Control, and Intelligent Systems (CCIS)*. IEEE. [https://doi.org/10.1109/ccis63231.2024.10932075][research_garg_2024]
- Garmsirinejad, Omid, Shatha Ghareeb, and Jamila Mustafina. 2025. "Optimizing Task Allocation in IT Project Management Using Cooperative Game Theory: A Shapley Value Approach." In *2025 18th International Conference on Development in eSystem Engineering (DeSE)*. IEEE. [https://doi.org/10.1109/dese68208.2025.11367830][research_garmsirinejad_2025]
- Garzella, Jack J., Marek Baranowski, Shaobo He, and Zvonimir Rakamarić. 2020. "Leveraging Compiler Intermediate Representation for Multi- and Cross-Language Verification." In *Verification, Model Checking, and Abstract Interpretation*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-39322-9\_5][research_garzella_2020]
- Gascón, Adrià, Ashish Tiwari, Brent Carmer, and Umang Mathur. 2017. "Look for the Proof to Find the Program: Decorated-Component-Based Program Synthesis." In *Computer Aided Verification*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-63390-9\_5][research_gascon_2017]
- Gautam, Aakash, Saket Vishwasrao, and Francisco Servant. 2017. "An Empirical Study of Activity, Popularity, Size, Testing, and Stability in Continuous Integration." In *2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2017.38][research_gautam_2017]
- Gay, Gregory, and Alireza Salahirad. 2023. "How Closely Are Common Mutation Operators Coupled to Real Faults?" In *2023 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst57152.2023.00021][research_gay_2023]
- Gayatri, Rahulkumar, Shilei Tian, Stephen L. Olivier, Eric Wright, and Johannes Doerfert. 2024. "Leveraging LLVM OpenMP GPU Offload Optimizations for Kokkos Applications." In *2024 IEEE 31st International Conference on High Performance Computing, Data, and Analytics (HiPC)*. IEEE. [https://doi.org/10.1109/hipc62374.2024.00035][research_gayatri_2024]
- Gebreyesus, Yibrah, Damian Dalton, Sebastian Nixon, Davide De Chiara, and Marta Chinnici. 2023. "Machine Learning for Data Center Optimizations: Feature Selection Using Shapley Additive exPlanation (SHAP)." *Future Internet* 15 (3): 88. [https://doi.org/10.3390/fi15030088][research_gebreyesus_2023]
- Geeson, Luke, and Lee Smith. 2024. "Compiler Testing with Relaxed Memory Models." In *2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo57630.2024.10444836][research_geeson_2024]
- Georges, Andy, Dries Buytaert, and Lieven Eeckhout. 2007. "Statistically Rigorous Java Performance Evaluation." In *Proceedings of the 22nd annual ACM SIGPLAN conference on Object-oriented programming systems, languages and applications*. ACM. [https://doi.org/10.1145/1297027.1297033][research_georges_2007]
- Ghaleb, Taher Ahmed, Daniel Alencar da Costa, and Ying Zou. 2019. "An Empirical Study of the Long Duration of Continuous Integration Builds." *Empirical Software Engineering* 24 (4): 2102–39. [https://doi.org/10.1007/s10664-019-09695-9][research_ghaleb_2019]
- Ghanbari, Hadi, Terese Besker, Antonio Martini, and Jan Bosch. 2017. "Looking for Peace of Mind? Manage Your (Technical) Debt: An Exploratory Field Study." In *2017 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2017.53][research_ghanbari_2017]
- Gharesifard, Bahman, and Stephen L. Smith. 2016. "On Distributed Submodular Maximization with Limited Information." In *2016 American Control Conference (ACC)*. IEEE. [https://doi.org/10.1109/acc.2016.7525053][research_gharesifard_2016]
- Ghorbani, Amirata, James Zou, and Andre Esteva. 2022. "Data Shapley Valuation for Efficient Batch Active Learning." In *2022 56th Asilomar Conference on Signals, Systems, and Computers*. IEEE. [https://doi.org/10.1109/ieeeconf56349.2022.10064696][research_ghorbani_2022]
- Ghotra, Baljinder, Shane McIntosh, and Ahmed E. Hassan. 2017. "A Large-Scale Study of the Impact of Feature Selection Techniques on Defect Classification Models." In *2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2017.18][research_ghotra_2017]
- Giamattei, Luca, Matteo Biagiola, Roberto Pietrantuono, Stefano Russo, and Paolo Tonella. 2024. "Reinforcement Learning for Online Testing of Autonomous Driving Systems: A Replication and Extension Study." *Empirical Software Engineering* 30 (1): 19. [https://doi.org/10.1007/s10664-024-10562-5][research_giamattei_2024]
- Gilot, Andrea, Tobias Wrigstad, and Eva Darulova. 2026. "Floating-Point Usage on GitHub: A Large-Scale Study of Statically Typed Languages." *Proceedings of the ACM on Programming Languages* 10 (OOPSLA1): 86–113. [https://doi.org/10.1145/3798203][research_gilot_2026]
- Glanville, R. Steven, and Susan L. Graham. 1978. "A New Method for Compiler Code Generation." In *Proceedings of the 5th ACM SIGACT-SIGPLAN symposium on Principles of programming languages - POPL '78*. ACM Press. [https://doi.org/10.1145/512760.512785][research_glanville_graham_1978]
- Godboley, Sangharatna, Kanika Gupta, and . G. Monika. 2022. "AV-AFL: A Vulnerability Detection Fuzzing Approach by Proving Non-Reachable Vulnerabilities Using Sound Static Analyser." In *Proceedings of the 17th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0011032900003176][research_godboley_2022]
- Golla, Monika Rani, and Sangharatna Godboley. 2024. "Automated SC-MCC Test Case Generation Using Coverage-Guided Fuzzing." *Software Quality Journal* 32 (3): 849–80. [https://doi.org/10.1007/s11219-024-09667-3][research_golla_2024]
- Golnari, Ameneh, Yakir Vizel, and Sharad Malik. 2015. "Error-Tolerant Processors: Formal Specification and Verification." In *2015 IEEE/ACM International Conference on Computer-Aided Design (ICCAD)*. IEEE. [https://doi.org/10.1109/iccad.2015.7372582][research_golnari_2015]
- Gómez-Londoño, Alejandro, Johannes Åman Pohjola, Hira Taqdees Syeda, Magnus O. Myreen, and Yong Kiam Tan. 2020. "Do You Have Space for Dessert? A Verified Space Cost Semantics for CakeML Programs." *Proceedings of the ACM on Programming Languages* 4 (OOPSLA): 1–29. [https://doi.org/10.1145/3428272][research_gomezlondono_2020]
- Gong, Qinqin, Suixiang Gao, Fengmin Wang, and Ruiqi Yang. 2021. "A Multi-Pass Streaming Algorithm for Regularized Submodular Maximization." In *Combinatorial Optimization and Applications*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-92681-6\_55][research_gong_2021]
- Gong, Siyi, and Hao Zhong. 2026. "How Challenging It Is to Identify Real Code Authors: An Empirical Study." *Empirical Software Engineering* 31 (4): 107. [https://doi.org/10.1007/s10664-026-10819-1][research_gong_2026]
- Gonzalez-Barahona, Jesus M., and Gregorio Robles. 2023. "Revisiting the Reproducibility of Empirical Software Engineering Studies Based on Data Retrieved from Development Repositories." *Information and Software Technology* 164: 107318. [https://doi.org/10.1016/j.infsof.2023.107318][research_gonzalezbaraho_2023]
- Gopinath, Rahul, Jie M. Zhang, Marinos Kintis, and Mike Papadakis. 2022. "Mutation Analysis and Its Industrial Applications." *Software Testing, Verification and Reliability* 32 (7): e1830. [https://doi.org/10.1002/stvr.1830][research_gopinath_2022]
- Goseva-Popstojanova, Katerina, and Jacob Tyo. 2017. "Experience Report: Security Vulnerability Profiles of Mission Critical Software: Empirical Analysis of Security Related Bug Reports." In *2017 IEEE 28th International Symposium on Software Reliability Engineering (ISSRE)*. IEEE. [https://doi.org/10.1109/issre.2017.42][research_gosevapopstoja_2017]
- Gote, Christoph, Ingo Scholtes, and Frank Schweitzer. 2019. "git2net: Mining Time-Stamped Co-Editing Networks from Large Git Repositories." In *2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2019.00070][research_gote_2019]
- Gourdin, Léo, Benjamin Bonneau, Sylvain Boulmé, David Monniaux, and Alexandre Bérard. 2023. "Formally Verifying Optimizations with Block Simulations." *Proceedings of the ACM on Programming Languages* 7 (OOPSLA2): 59–88. [https://doi.org/10.1145/3622799][research_gourdin_2023]
- Graics, Bence, Vince Molnár, and István Majzik. 2023. "Component-Based Specification, Design and Verification of Adaptive Systems." *Systems Engineering* 26 (5): 567–89. [https://doi.org/10.1002/sys.21675][research_graics_2023]
- Gratien, Jean-Marc. 2020. "Introducing Multi-Level Parallelism, at Coarse, Fine and Instruction Level to Enhance the Performance of Iterative Solvers for Large Sparse Linear Systems on Multi- and Many-Core Architecture." In *2020 IEEE/ACM 6th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC) and Workshop on Hierarchical Parallelism for Exascale Computing (HiPar)*. IEEE. [https://doi.org/10.1109/llvmhpchipar51896.2020.00014][research_gratien_2020]
- Greiler, Michaela, Kim Herzig, and Jacek Czerwonka. 2015. "Code Ownership and Software Quality: A Replication Study." In *2015 IEEE/ACM 12th Working Conference on Mining Software Repositories*. IEEE. [https://doi.org/10.1109/msr.2015.8][research_greiler_2015]
- Gretz, F., F-J. Grosch, M. Mendler, and S. Scheele. 2020. "Synchronized Shared Memory and Procedural Abstraction: Towards a Formal Semantics of Blech." In *2020 Forum for Specification and Design Languages (FDL)*. IEEE. [https://doi.org/10.1109/fdl50818.2020.9232942][research_gretz_2020]
- Grossman, Dan, Greg Morrisett, Trevor Jim, Michael Hicks, Yanling Wang, and James Cheney. 2002. "Region-Based Memory Management in Cyclone." In *Proceedings of the ACM SIGPLAN 2002 conference on Programming language design and implementation*. ACM. [https://doi.org/10.1145/512529.512563][research_grossman_2002]
- Gruber, Martin, Stephan Lukasczyk, Florian Krois, and Gordon Fraser. 2021. "An Empirical Study of Flaky Tests in Python." In *2021 14th IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst49551.2021.00026][research_gruber_2021]
- Gückel, Johannes, and Pirmin Fontaine. 2025. "Fast Shapley Value Approximation through Machine Learning with Application in Routing Problems." *Networks* 86 (4): 402–27. [https://doi.org/10.1002/net.70003][research_guckel_2025]
- Guizzo, Giovani, Francesco Califano, Federica Sarro, Filomena Ferrucci, and Mark Harman. 2023. "Inferring Test Models from User Bug Reports Using Multi-Objective Search." *Empirical Software Engineering* 28 (4): 95. [https://doi.org/10.1007/s10664-023-10333-8][research_guizzo_2023]
- Guleria, Pratiyush. 2024. "Blending Shapley Values for Feature Ranking in Machine Learning: An Analysis on Educational Data." *Neural Computing and Applications* 36 (23): 14093–14117. [https://doi.org/10.1007/s00521-024-09861-1][research_guleria_2024]
- Gunadi, Hendra. 2015. "Formal Certification of Non-Interferent Android Bytecode (DEX Bytecode)." In *2015 20th International Conference on Engineering of Complex Computer Systems (ICECCS)*. IEEE. [https://doi.org/10.1109/iceccs.2015.36][research_gunadi_2015]
- Guo, Longkun, Jiawei Lin, and Shuqian Zhu. 2026a. "Streaming Submodular Maximization with Fairness Constraints for Massive Data Summarization." *Theoretical Computer Science* 1081: 116037. [https://doi.org/10.1016/j.tcs.2026.116037][research_guo_2026_b]
- Habchi, Sarra, Guillaume Haben, Mike Papadakis, Maxime Cordy, and Yves Le Traon. 2022. "A Qualitative Study on the Sources, Impacts, and Mitigation Strategies of Flaky Tests." In *2022 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst53961.2022.00034][research_habchi_2022]
- Haghighatkhah, Alireza, Mika Mäntylä, Markku Oivo, and Pasi Kuvaja. 2018. "Test Prioritization in Continuous Integration Environments." *Journal of Systems and Software* 146: 80–98. [https://doi.org/10.1016/j.jss.2018.08.061][research_haghighatkhah_2018]
- Hall, Mary, and Protonu Basu. 2017. "Polyhedral Compiler Technology in Collaboration with Autotuning Important to Domain-Specific Frameworks for HPC." In *Languages and Compilers for Parallel Computing*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-52709-3\_9][research_hall_2017]
- Hallahan, William T., Ranjit Jhala, and Ruzica Piskac. 2025. "Counterexample-Guided Inference of Modular Specifications." *Proceedings of the ACM on Programming Languages* 9 (OOPSLA1): 1689–1716. [https://doi.org/10.1145/3720505][research_hallahan_2025]
- Hamasaki, Ichiro, Keiko Kunimi, Kiyo Shibata, and Goseki Toshiaki. 2026. "Large Language Model-Based Interactive Code Generation for Developing a 3D Eye Movement Schematic." *Cureus*. [https://doi.org/10.7759/cureus.107791][research_hamasaki_2026]
- Hammadi, Moncef, and Stanislao Patalano. 2017. "Automatic Generation of Simulation Workflows for System Verification Using XDSM Representation." In *2017 IEEE International Systems Engineering Symposium (ISSE)*. IEEE. [https://doi.org/10.1109/syseng.2017.8088306][research_hammadi_2017]
- Hammer, Maximilian, Ralph Maschotta, and Armin Zimmermann. 2025. "Compiler-Like Code Generation for fUML: Reducing Overhead in Executable UML." *IEEE Access* 13: 173267–97. [https://doi.org/10.1109/access.2025.3615249][research_hammer_2025]
- Han, Myeonggyun, and Woongki Baek. 2021. "HERTI: A Reinforcement Learning-Augmented System for Efficient Real-Time Inference on Heterogeneous Embedded Systems." In *2021 30th International Conference on Parallel Architectures and Compilation Techniques (PACT)*. IEEE. [https://doi.org/10.1109/pact52795.2021.00014][research_han_2021]
- Han, Ruobing, and Hyesoon Kim. 2024. "Exponentially Expanding the Phase-Ordering Search Space via Dormant Information." In *Proceedings of the 33rd ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3640537.3641582][research_han_2024_b]
- Han, Jixin, Tomofumi Yuki, Michelle Mills Strout, Dan Umeda, Hironori Kasahara, and Keiji Kimura. 2021. "Parallelizing Compiler Translation Validation Using Happens-Before and Task-Set." In *2021 Ninth International Symposium on Computing and Networking Workshops (CANDARW)*. IEEE. [https://doi.org/10.1109/candarw53999.2021.00022][research_han_2021_b]
- Han, Ruobing, Jisheng Zhao, and Hyesoon Kim. 2024. "Enabling Fine-Grained Incremental Builds by Making Compiler Stateful." In *2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo57630.2024.10444865][research_han_2024]
- Hanson, David R. 1990. "Fast Allocation and Deallocation of Memory Based on Object Lifetimes." *Software: Practice and Experience* 20 (1): 5–12. [https://doi.org/10.1002/spe.4380200104][research_hanson_1990]
- Harif, Adi, and Shachar Itzhaky. 2025. "Ductape: Optimizing Dynamically Typed Programs Using Ahead-of-Time Compilation and Data-Flow Analysis." In *Static Analysis*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-032-07106-4\_12][research_harif_2025]
- Hariri, Farah, August Shi, Vimuth Fernando, Suleman Mahmood, and Darko Marinov. 2019. "Comparing Mutation Testing at the Levels of Source Code and Compiler Intermediate Representation." In *2019 12th IEEE Conference on Software Testing, Validation and Verification (ICST)*. IEEE. [https://doi.org/10.1109/icst.2019.00021][research_hariri_2019]
- Härtel, Johannes, and Ralf Lämmel. 2023. "Operationalizing Validity of Empirical Software Engineering Studies." *Empirical Software Engineering* 28 (6): 153. [https://doi.org/10.1007/s10664-023-10370-3][research_hartel_2023]
- Hasabnis, Niranjan, Rui Qiao, and R. Sekar. 2015. "Checking Correctness of Code Generator Architecture Specifications." In *2015 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo.2015.7054197][research_hasabnis_2015]
- Hasabnis, Niranjan, and R. Sekar. 2016. "Lifting Assembly to Intermediate Representation: A Novel Approach Leveraging Compilers." *ACM SIGPLAN Notices* 51 (4): 311–24. [https://doi.org/10.1145/2954679.2872380][research_hasabnis_2016]
- Hashemi, Negar. 2025. "Identifying and Mitigating Flaky Tests in JavaScript." In *2025 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst62969.2025.10989021][research_hashemi_2025]
- Hashemi, Negar, Amjed Tahir, and Shawn Rasheed. 2022. "An Empirical Study of Flaky Tests in JavaScript." In *2022 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme55016.2022.00011][research_hashemi_2022]
- Hatahet, Ahmad, Christoph Knieke, and Andreas Rausch. 2025. "Generating Software Architecture Description from Source Code Using Reverse Engineering and Large Language Model." In *2025 ACM/IEEE 28th International Conference on Model Driven Engineering Languages and Systems Companion (MODELS-C)*. IEEE. [https://doi.org/10.1109/models-c68889.2025.00080][research_hatahet_2025]
- Hawkins, William H., Jason D. Hiser, Michele Co, Anh Nguyen-Tuong, and Jack W. Davidson. 2017. "Zipr: Efficient Static Binary Rewriting for Security." In *2017 47th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)*. IEEE. [https://doi.org/10.1109/dsn.2017.27][research_hawkins_2017]
- Hayashi, Akihiro, Jun Shirako, Ettore Tiotto, Robert Ho, and Vivek Sarkar. 2016. "Exploring Compiler Optimization Opportunities for the OpenMP 4.× Accelerator Model on a POWER8+GPU Platform." In *2016 Third Workshop on Accelerator Programming Using Directives (WACCPD)*. IEEE. [https://doi.org/10.1109/waccpd.2016.011][research_hayashi_2016]
- He, Zhixing, and Hao Zhong. 2025. "From Bug Reports to Workarounds: The Real-World Impact of Compiler Bugs." In *2025 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner64311.2025.00032][research_he_2025]
- Helmke, Rene, Eugen Winter, and Michael Rademacher. 2021. "EPF: An Evolutionary, Protocol-Aware, and Coverage-Guided Network Fuzzing Framework." In *2021 18th International Conference on Privacy, Security and Trust (PST)*. IEEE. [https://doi.org/10.1109/pst52912.2021.9647801][research_helmke_2021]
- Hepola, Kari, Tharaka Ranasinghe Arachchige, Joonas Multanen, and Pekka Jääskeläinen. 2024. "Fully Automatic Compiler Retargeting and CV-X-IF Hardware Interface Generation for RISC-V Custom Instructions." In *2024 IEEE Nordic Circuits and Systems Conference (NorCAS)*. IEEE. [https://doi.org/10.1109/norcas64408.2024.10752475][research_hepola_2024]
- Hepola, Kari, Joonas Multanen, and Pekka Jaaskelainen. 2022. "OpenASIP 2.0: Co-Design Toolset for RISC-V Application-Specific Instruction-Set Processors." In *2022 IEEE 33rd International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap54787.2022.00034][research_hepola_2022]
- Herber, Tobias, and Markus Weninger. 2025. "Trace-Based Bytecode Interpreter Visualization for Compiler Construction Education." In *2025 IEEE Working Conference on Software Visualization (VISSOFT)*. IEEE. [https://doi.org/10.1109/vissoft67405.2025.00010][research_herber_2025]
- Herbold, Steffen, Alexander Trautsch, and Jens Grabowski. 2016. "Global vs. Local Models for Cross-Project Defect Prediction: A Replication Study." *Empirical Software Engineering* 22 (4): 1866–1902. [https://doi.org/10.1007/s10664-016-9468-y][research_herbold_2016]
- Herdt, Vladimir, Daniel Grose, Hoang M. Le, and Rolf Drechsler. 2019. "Verifying Instruction Set Simulators Using Coverage-Guided Fuzzing." In *2019 Design, Automation & Test in Europe Conference & Exhibition (DATE)*. IEEE. [https://doi.org/10.23919/date.2019.8714912][research_herdt_2019]
- Hesselbarth, Sebastian, Gregor Schewior, and Holger Blume. 2015. "Fast and Accurate Power Estimation for Application-Specific Instruction Set Processors Using FPGA Emulation." In *2015 Conference on Design and Architectures for Signal and Image Processing (DASIP)*. IEEE. [https://doi.org/10.1109/dasip.2015.7367249][research_hesselbarth_2015]
- Hindle, Abram, and Curtis Onuczko. 2018. "Preventing Duplicate Bug Reports by Continuously Querying Bug Reports." *Empirical Software Engineering* 24 (2): 902–36. [https://doi.org/10.1007/s10664-018-9643-4][research_hindle_2018]
- Hjort, Rikard, Jakob Holmgren, and Christian Persson. 2018. "The CakeML Compiler Explorer: Tracking Intermediate Representations in a Verified Compiler." In *Trends in Functional Programming*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-89719-6\_8][research_hjort_2018]
- Hodován, Renáta, and Ákos Kiss. 2026. "Grammar-Aware Coverage-Guided Fuzzing with Grammarinator and AFL++." In *2026 IEEE International Conference on Software Analysis, Evolution and Reengineering - Companion (SANER-C)*. IEEE. [https://doi.org/10.1109/saner-c67878.2026.00055][research_hodovan_2026]
- Höll, Jos, and Jonas Kufer. 2025. "Holistic Evaluation of LLM-Based Code Generation." In *2025 3rd International Conference on Foundation and Large Language Models (FLLM)*. IEEE. [https://doi.org/10.1109/fllm67465.2025.11390916][research_holl_2025]
- Hora, Andre. 2022. "Excluding Code from Test Coverage: Practices, Motivations, and Impact." *Empirical Software Engineering* 28 (1): 16. [https://doi.org/10.1007/s10664-022-10259-7][research_hora_2022]
- Horikawa, Kosei, Yutaro Kashiwa, Bin Lin, Kenji Fujiwara, and Hajimu Iida. 2025. "How Does Test Code Differ from Production Code in Terms of Refactoring? An Empirical Study." In *2025 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme64153.2025.00079][research_horikawa_2025]
- Horváth, Péter, Gábor Hosszú, and Ferenc Kovács. 2015. "A Proposed Synthesis Method for Application-Specific Instruction Set Processors." *Microelectronics Journal* 46 (3): 237–47. [https://doi.org/10.1016/j.mejo.2015.01.001][research_horvath_2015]
- Hosseini, Seyedrebvar, Burak Turhan, and Mika Mäntylä. 2018. "A Benchmark Study on the Effectiveness of Search-Based Data Selection and Feature Selection for Cross Project Defect Prediction." *Information and Software Technology* 95: 296–312. [https://doi.org/10.1016/j.infsof.2017.06.004][research_hosseini_2018]
- Hu, Jian. 2026. "Representation Learning for Coincidental Correctness in Fault Localization." *Information and Software Technology* 191: 107978. [https://doi.org/10.1016/j.infsof.2025.107978][research_hu_2026_c]
- Hu, Bowen, Yun Chen, and Xiaoyang Zeng. 2021. "An Agile Instruction Set Extension Method Based on the RISC-V Processor." In *2021 IEEE 4th International Conference on Electronics Technology (ICET)*. IEEE. [https://doi.org/10.1109/icet51757.2021.9450911][research_hu_2021]
- Hu, Qinheping, John Cyphert, Loris D'Antoni, and Thomas Reps. 2020b. "Exact and Approximate Methods for Proving Unrealizability of Syntax-Guided Synthesis Problems." In *Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3385412.3385979][research_hu_2020_b]
- Hu, Jingwei, Wangchen Dai, Liu Yao, and Ray C. C. Cheung. 2018. "An Application Specific Instruction Set Processor (ASIP) for the Niederreiter Cryptosystem." In *2018 6th International Symposium on Digital Forensic and Security (ISDFS)*. IEEE. [https://doi.org/10.1109/isdfs.2018.8355364][research_hu_2018]
- Hu, Tianmin, Zhenye Fan, Zhanbo Ye, Guixin Ye, and Lu He. 2025. "SSFuzz: Synthesizing and Scheduling Bug-Triggering Code Segments for History-Driven Compiler Testing." *Empirical Software Engineering* 31 (2): 27. [https://doi.org/10.1007/s10664-025-10777-0][research_hu_2025]
- Hu, Yunfei, Fei Gu, Puyu Han, Zhihao Wei, and Zhijun Li. 2026b. "QJWasm: A Lightweight Runtime System for Efficient WebAssembly Execution in Resource-Constrained Environments." *Journal of Systems Architecture* 179: 103926. [https://doi.org/10.1016/j.sysarc.2026.103926][research_hu_2026]
- Hu, Linghuan, W. Eric Wong, D. Richard Kuhn, and Raghu N. Kacker. 2020c. "How Does Combinatorial Testing Perform in the Real World: An Empirical Study." *Empirical Software Engineering* 25 (4): 2661–93. [https://doi.org/10.1007/s10664-019-09799-2][research_hu_2020_c]
- Huang, Wei-pei, Ray C. C. Cheung, and Hong Yan. 2019b. "An Efficient Application Specific Instruction Set Processor (ASIP) for Tensor Computation." In *2019 IEEE 30th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap.2019.00-36][research_huang_2019]
- Huang, Yonghui Andie, Daniel Alencar da Costa, Grant Dick, Mariam El Mezouar, and Liwen Xiao. 2026b. "Is This Build Failure Related to My Patch? An Empirical Study of Unrelated Build Failures in Continuous Integration." *Empirical Software Engineering* 31 (6): 148. [https://doi.org/10.1007/s10664-026-10874-8][research_huang_2026_b]
- Huang, Qijing, Ameer Haj-Ali, William Moses, et al. 2019a. "AutoPhase: Compiler Phase-Ordering for HLS with Deep Reinforcement Learning." In *2019 IEEE 27th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM)*. IEEE. [https://doi.org/10.1109/fccm.2019.00049][research_huang_2019_b]
- Huang, Chien-Chung, and Naonori Kakimura. 2021. "Multi-Pass Streaming Algorithms for Monotone Submodular Function Maximization." *Theory of Computing Systems* 66 (1): 354–94. [https://doi.org/10.1007/s00224-021-10065-6][research_huang_2021]
- Huang, Yanlong, Jierui Liu, Yuhan She, et al. 2026a. "Chariot: Compiler-Aware Heterogeneous Graph Representation Learning for Automated HLS Optimization." In *2026 IEEE 34th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM)*. IEEE. [https://doi.org/10.1109/fccm68464.2026.00052][research_huang_2026]
- Huang, Chien-Chung, and François Sellier. 2024. "Semi-Streaming Algorithms for Submodular Function Maximization under b-Matching, Matroid, and Matchoid Constraints." *Algorithmica* 86 (11): 3598–3628. [https://doi.org/10.1007/s00453-024-01272-x][research_huang_2024_b]
- Huang, Qiao, Emad Shihab, Xin Xia, David Lo, and Shanping Li. 2017b. "Identifying Self-Admitted Technical Debt in Open Source Projects Using Text Mining." *Empirical Software Engineering* 23 (1): 418–51. [https://doi.org/10.1007/s10664-017-9522-4][research_huang_2017_b]
- Huang, Kai, Jian Zhang, Xiangxin Meng, and Yang Liu. 2025. "Template-Guided Program Repair in the Era of Large Language Models." In *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse55347.2025.00030][research_huang_2025]
- Huang, Longtao, Shida Zhong, Huihong Liang, and Tao Yuan. 2024. "Paddle-Mlir: A Compiler Based on MLIR for Accelerating PaddlePaddle on Edge Intelligence Devices." In *2024 4th International Conference on Computer Communication and Artificial Intelligence (CCAI)*. IEEE. [https://doi.org/10.1109/ccai61966.2024.10602841][research_huang_2024]
- Huang, Rubing, Yunan Zhou, Weiwen Zong, Dave Towey, and Jinfu Chen. 2017a. "An Empirical Comparison of Similarity Measures for Abstract Test Case Prioritization." In *2017 IEEE 41st Annual Computer Software and Applications Conference (COMPSAC)*. IEEE. [https://doi.org/10.1109/compsac.2017.271][research_huang_2017]
- Huck, Alexander, Jan-Patrick Lehr, Sebastian Kreutzer, et al. 2018. "Compiler-Aided Type Tracking for Correctness Checking of MPI Applications." In *2018 IEEE/ACM 2nd International Workshop on Software Correctness for HPC Applications (Correctness)*. IEEE. [https://doi.org/10.1109/correctness.2018.00011][research_huck_2018]
- Huck, Alexander, Joachim Protze, Jan-Patrick Lehr, Christian Terboven, Christian Bischof, and Matthias S. Muller. 2020. "Towards Compiler-Aided Correctness Checking of Adjoint MPI Applications." In *2020 IEEE/ACM 4th International Workshop on Software Correctness for HPC Applications (Correctness)*. IEEE. [https://doi.org/10.1109/correctness51934.2020.00010][research_huck_2020]
- Humbatova, Nargiz, Gunel Jahangirova, and Paolo Tonella. 2023. "DeepCrime: From Real Faults to Mutation Testing Tool for Deep Learning." In *2023 IEEE/ACM 45th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion)*. IEEE. [https://doi.org/10.1109/icse-companion58688.2023.00027][research_humbatova_2023]
- Hupel, Lars, and Tobias Nipkow. 2018. "A Verified Compiler from Isabelle/HOL to CakeML." In *Programming Languages and Systems*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-89884-1\_35][research_hupel_2018]
- Hussein, Soha, Vaibhav Sharma, Stephen McCamant, Sanjai Rayadurgam, and Mats Heimdahl. 2021. "Counterexample Guided Inductive Repair of Reactive Contracts." In *2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase51524.2021.9678548][research_hussein_2021]
- Hwang, Ho, and Daesung Moon. 2025. "CBGF: Callback Coverage Guided Fuzzing." *IEEE Access* 13: 68831–40. [https://doi.org/10.1109/access.2025.3561135][research_hwang_2025]
- Ibrahim, Mina, Martel Shokry, Lokesh Siddhu, Lars Bauer, Hassan Nassar, and Jörg Henkel. 2024. "An FPGA-Based RISC-V Instruction Set Extension and Memory Controller for Multi-Level Cell NVM." In *2024 International Conference on Microelectronics (ICM)*. IEEE. [https://doi.org/10.1109/icm63406.2024.10815826][research_ibrahim_2024]
- Idri, Ali, Ibtissam Abnane, and Alain Abran. 2017. "Evaluating Pred(p) and Standardized Accuracy Criteria in Software Development Effort Estimation." *Journal of Software: Evolution and Process* 30 (4): e1925. [https://doi.org/10.1002/smr.1925][research_idri_2017]
- Idri, Ali, Fatima azzahra Amazal, and Alain Abran. 2015. "Accuracy Comparison of Analogy-Based Software Development Effort Estimation Techniques." *International Journal of Intelligent Systems* 31 (2): 128–52. [https://doi.org/10.1002/int.21748][research_idri_2015]
- Idri, Ali, Mohamed Hosni, and Alain Abran. 2016. "Systematic Mapping Study of Ensemble Effort Estimation." In *Proceedings of the 11th International Conference on Evaluation of Novel Software Approaches to Software Engineering*. SCITEPRESS - Science and and Technology Publications. [https://doi.org/10.5220/0005822701320139][research_idri_2016]
- Imai, Naoko, Hironori Washizaki, Naohiko Tsuda, and Yoshiaki Fukazawa. 2021. "When Is Continuous Integration Useful? Empirical Study on Team Size and Reporters in Development." In *2021 IEEE International Symposium on Software Reliability Engineering Workshops (ISSREW)*. IEEE. [https://doi.org/10.1109/issrew53611.2021.00081][research_imai_2021]
- Imianosky, Carolina, Douglas A. Santos, and Luigi Dilillo. 2025. "Efficient TinyML Inference on a Fault-Tolerant RISC-V SoC with Vector Extension." In *2025 10th International Workshop on Advances in Sensors and Interfaces (IWASI)*. IEEE. [https://doi.org/10.1109/iwasi66786.2025.11121981][research_imianosky_2025]
- Imianosky, Carolina, Douglas A. Santos, Douglas R. Melo, Felipe VieE, and Luigi Dilillo. 2023. "Implementation and Reliability Evaluation of a RISC-V Vector Extension Unit." In *2023 IEEE International Symposium on Defect and Fault Tolerance in VLSI and Nanotechnology Systems (DFT)*. IEEE. [https://doi.org/10.1109/dft59622.2023.10313569][research_imianosky_2023]
- Imianosky, Carolina, Douglas A. Santos, Douglas R. Melo, Felipe Viel, and Luigi Dilillo. 2024. "Special Session: Reliability and Performance Evaluation of a RISC-V Vector Extension Unit for Vector Multiplication." In *2024 IEEE International Symposium on Defect and Fault Tolerance in VLSI and Nanotechnology Systems (DFT)*. IEEE. [https://doi.org/10.1109/dft63277.2024.10753524][research_imianosky_2024]
- Imran, Muhammad, Vittorio Cortellessa, Davide Di Ruscio, Riccardo Rubei, and Luca Traini. 2025. "Is Code Coverage of Performance Tests Related to Source Code Features? An Empirical Study on Open-Source Java Systems." *Empirical Software Engineering* 30 (6): 157. [https://doi.org/10.1007/s10664-025-10712-3][research_imran_2025]
- Ishimoto, Yuta, Yuto Nakamura, Ryota Katsube, et al. 2024. "An Empirical Study on Self-Admitted Technical Debt in Quantum Software." In *2024 31st Asia-Pacific Software Engineering Conference (APSEC)*. IEEE. [https://doi.org/10.1109/apsec65559.2024.00015][research_ishimoto_2024]
- Ishimura, Osamu, and Yoshihide Yoshimoto. 2022. "Just-In-Time Compiler System in Aspect-Oriented Programming Based Building Block Platform for Constructing Domain-Specific Language for HPC Application." In *2022 Tenth International Symposium on Computing and Networking Workshops (CANDARW)*. IEEE. [https://doi.org/10.1109/candarw57323.2022.00082][research_ishimura_2022]
- Ismael, Sarmad F., Omar T. Zyad, and Yahya T. Qassim. 2018. "System on Chip Implementation of Compiler Stack with a Delimiter Matching Application." In *2018 Third Scientific Conference of Electrical Engineering (SCEE)*. IEEE. [https://doi.org/10.1109/scee.2018.8684137][research_ismael_2018]
- Israel, Gudipudi Joel, and Mohamed Asan Basiri M. 2024. "High Performance Instruction-Data Level Parallelism Based Instruction Set Architecture in RISC-V." In *2024 IEEE 8th International Conference on Information and Communication Technology (CICT)*. IEEE. [https://doi.org/10.1109/cict64037.2024.10899652][research_israel_2024]
- Italiano, Davide, and Chris Cummins. 2025. "Finding Missed Code Size Optimizations in Compilers Using Large Language Models." In *Proceedings of the 34th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3708493.3712686][research_italiano_2025]
- Jahanshahi, Mahmoud, David Reid, Adam McDaniel, and Audris Mockus. 2025. "OSS License Identification at Scale: A Comprehensive Dataset Using World of Code." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00032][research_jahanshahi_2025]
- Jain, Manan, Het Kanzariya, Neel Joshi, Yesha Masharu, Sachin Gajjar, and Dhaval Shah. 2023. "Design, Development and Testing of a 16-Bit Reduced Instruction Set Computer Architecture Based Processor." *Sādhanā* 48 (4): 244. [https://doi.org/10.1007/s12046-023-02304-y][research_jain_2023]
- Jamieson, Maurice, and Nick Brown. 2021. "Compact Native Code Generation for Dynamic Languages on Micro-Core Architectures." In *Proceedings of the 30th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3446804.3446853][research_jamieson_2021]
- Jamil, Mohammad Talal, Shamsa Abid, and Shafay Shamail. 2025. "Can LLMs Generate Higher Quality Code than Humans? An Empirical Study." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00081][research_jamil_2025]
- Jaoua, Imen, Oussama Ben Sghaier, and Houari Sahraoui. 2025. "Combining Large Language Models with Static Analyzers for Code Review Generation." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00038][research_jaoua_2025]
- Jarman, Darryl C., Zhi Quan Zhou, and Tsong Yueh Chen. 2017. "Metamorphic Testing for Adobe Data Analytics Software." In *2017 IEEE/ACM 2nd International Workshop on Metamorphic Testing (MET)*. IEEE. [https://doi.org/10.1109/met.2017.1][research_jarman_2017]
- Jehan, Seema, and Franz Wotawa. 2023. "An Empirical Study of Greedy Test Suite Minimization Techniques Using Mutation Coverage." *IEEE Access* 11: 65427–42. [https://doi.org/10.1109/access.2023.3289073][research_jehan_2023]
- Jensen, Alexander. 2022. "Machine-Checked Verification of Cognitive Agents." In *Proceedings of the 14th International Conference on Agents and Artificial Intelligence*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0010838700003116][research_jensen_2022]
- Jha, Ankit. 2023. "Automatic Benchmark Generation for Object Constraint Language." In *2023 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst57152.2023.00057][research_jha_2023]
- Jia, Yue, and Mark Harman. 2011. "An Analysis and Survey of the Development of Mutation Testing." *IEEE Transactions on Software Engineering* 37 (5): 649–78. [https://doi.org/10.1109/tse.2010.62][research_jia_harman_2011]
- Jiang, Yujuan, and Bram Adams. 2015. "Co-Evolution of Infrastructure and Source Code: An Empirical Study." In *2015 IEEE/ACM 12th Working Conference on Mining Software Repositories*. IEEE. [https://doi.org/10.1109/msr.2015.12][research_jiang_2015]
- Jiang, Kaihang, Bihui Jin, and Pengyu Nie. 2025a. "CoUpJava: A Dataset of Code Upgrade Histories in Open-Source Java Repositories." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00075][research_jiang_2025_b]
- Jiang, Yuhui, Xingjian Lu, Wei Mao, and Ying Lin. 2023. "Integrating Staleness and Shapley Value Consistency for Efficient K-Asynchronous Federated Learning." In *2023 IEEE International Conference on Big Data (BigData)*. IEEE. [https://doi.org/10.1109/bigdata59044.2023.10386972][research_jiang_2023]
- Jiang, Shuyao, Ruiying Zeng, Yangfan Zhou, and Michael R. Lyu. 2025b. "Distinguishability-Guided Test Program Generation for WebAssembly Runtime Performance Testing." In *2025 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner64311.2025.00078][research_jiang_2025]
- Jiao, Jiao. 2019. "Formal Specification and Verification of Smart Contracts." In *Formal Methods and Software Engineering*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-32409-4\_35][research_jiao_2019]
- Jiao, Qiang, Wei Hu, Fang Liu, and Yong Dong. 2021. "RISC-VTF: RISC-V Based Extended Instruction Set for Transformer." In *2021 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*. IEEE. [https://doi.org/10.1109/smc52423.2021.9658643][research_jiao_2021]
- Jin, Qing, Angelos Georghiou, Phebe Vayanos, and Grani A. Hanasusanto. 2026. "Distributionally Robust Optimization with Decision-Dependent Information Discovery." *Mathematical Programming*. [https://doi.org/10.1007/s10107-026-02346-0][research_jin_2026]
- Jitsunari, Yuma, and Yoshitaka Arahori. 2019. "Coverage-Guided Learning-Assisted Grammar-Based Fuzzing." In *2019 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw.2019.00065][research_jitsunari_2019]
- Johnson, David S. 1974. "Approximation Algorithms for Combinatorial Problems." *Journal of Computer and System Sciences* 9 (3): 256–78. [https://doi.org/10.1016/s0022-0000(74)80044-9][research_johnson_1974]
- Johnson, Evan, Evan Laufer, Zijie Zhao, et al. 2023. "WaVe: A Verifiably Secure WebAssembly Sandboxing Runtime." In *2023 IEEE Symposium on Security and Privacy (SP)*. IEEE. [https://doi.org/10.1109/sp46215.2023.10179357][research_johnson_2023]
- Johnson, Blake, and Rahul Simha. 2025. "CASTL: A Composable Source Code Query Language for Security and Vulnerability Analysis." In *Proceedings of the 11th International Conference on Information Systems Security and Privacy*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0013176200003899][research_johnson_2025]
- Johnston, Beau, and Josh Milthorpe. 2018. "AIWC: OpenCL-Based Architecture-Independent Workload Characterization." In *2018 IEEE/ACM 5th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2018.8639381][research_johnston_2018]
- Journault, Matthieu, and Antoine Miné. 2016. "Static Analysis by Abstract Interpretation of the Functional Correctness of Matrix Manipulating Programs." In *Static Analysis*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-662-53413-7\_13][research_journault_2016]
- Jovanovic, B. D., and P. S. Levy. 1997. "A Look at the Rule of Three." *American Statistician* 51 (2): 137–39. [https://doi.org/10.1080/00031305.1997.10473947][research_jovanovic_levy_1997]
- Kadarkarai, Pandiaraj, Muthumari Saravanakumar, Varshini Palanikumar, and Molabanti Satish Kumar. 2025. "Static Timing and Power Analysis of a RISC-V Pipelined Processor." In *2025 4th International Conference on Automation, Computing and Renewable Systems (ICACRS)*. IEEE. [https://doi.org/10.1109/icacrs67045.2025.11324142][research_kadarkarai_2025]
- Kakarla, Siva Kesava Reddy, Francis Y. Yan, and Ryan Beckett. 2024. "Diffy: Data-Driven Bug Finding for Configurations." *Proceedings of the ACM on Programming Languages* 8 (PLDI): 199–222. [https://doi.org/10.1145/3656385][research_kakarla_2024]
- Kakati, Sangeeta, and Mats Brorsson. 2025. "Performance and Usability Implications of Multiplatform and WebAssembly Containers." In *Proceedings of the 15th International Conference on Cloud Computing and Services Science*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0013203200003950][research_kakati_2025]
- Kaliszyk, Cezary. 2023. "Improved Assistance for Interactive Proof (Keynote)." In *Proceedings of the 12th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3573105.3579108][research_kaliszyk_2023]
- Kamil, Shoaib, Alvin Cheung, Shachar Itzhaky, and Armando Solar-Lezama. 2016. "Verified Lifting of Stencil Computations." In *Proceedings of the 37th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/2908080.2908117][research_kamil_2016]
- Kanabar, Hrutvik, Samuel Vivien, Oskar Abrahamsson, et al. 2023. "PureCake: A Verified Compiler for a Lazy Functional Language." *Proceedings of the ACM on Programming Languages* 7 (PLDI): 952–76. [https://doi.org/10.1145/3591259][research_kanabar_2023]
- Kanemoto, Yo, Reika Nishimura Arakawa, and Mitsuaki Akiyama. 2026. "An Empirical Study of SBOM Usage through GitHub Actions." *IEEE Access* 14: 100780–92. [https://doi.org/10.1109/access.2026.3698914][research_kanemoto_2026]
- Kang, Jeehoon, Yoonseung Kim, Youngju Song, et al. 2018. "Crellvm: Verified Credible Compilation for LLVM." In *Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3192366.3192377][research_kang_2018]
- Kang, Chan Gu, and Hakjoo Oh. 2023. "Modular Component-Based Quantum Circuit Synthesis." *Proceedings of the ACM on Programming Languages* 7 (OOPSLA1): 348–75. [https://doi.org/10.1145/3586039][research_kang_2023]
- Karadeniz, Büșra Sinem, Sümeyye Zülal Dik, Zeki Kuș, and Musa Aydin. 2025. "Shapley Patch Valuation Method for Histopathological Image Classification." In *2025 10th International Conference on Machine Learning Technologies (ICMLT)*. IEEE. [https://doi.org/10.1109/icmlt65785.2025.11193186][research_karadeniz_2025]
- Karathanasopoulos, Nikolaos, Agyapal Singh, and Panagiotis Hadjidoukas. 2024. "Machine Learning-Based Modelling, Feature Importance and Shapley Additive Explanations Analysis of Variable-Stiffness Composite Beam Structures." *Structures* 62: 106206. [https://doi.org/10.1016/j.istruc.2024.106206][research_karathanasopou_2024]
- Karim, Md. Rejaul, Akinori Ihara, Xin Yang, Hajimu Iida, and Kenichi Matsumoto. 2017. "Understanding Key Features of High-Impact Bug Reports." In *2017 8th International Workshop on Empirical Software Engineering in Practice (IWESEP)*. IEEE. [https://doi.org/10.1109/iwesep.2017.17][research_karim_2017]
- Karlsson, J., and K. Ryan. 1997. "A Cost-Value Approach for Prioritizing Requirements." *IEEE Software* 14 (5): 67–74. [https://doi.org/10.1109/52.605933][research_karlsson_ryan_1997]
- Katel, Navdeep, Vivek Khandelwal, and Uday Bondhugula. 2022. "MLIR-Based Code Generation for GPU Tensor Cores." In *Proceedings of the 31st ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3497776.3517770][research_katel_2022]
- Kavyashree, B., A. Geethashree, Monisha Suresh, Niranjan R. Khatavkar, D. D. Suhas, and N. M. Nikhil. 2025. "RISC-V SIMD Instructions: Vector Extension (Load/Store)." In *2025 3rd International Conference on Inventive Computing and Informatics (ICICI)*. IEEE. [https://doi.org/10.1109/icici65870.2025.11069565][research_b_2025]
- Kellison, Ariel. 2022. "A Machine-Checked Direct Proof of the Steiner-Lehmus Theorem." In *Proceedings of the 11th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3497775.3503682][research_kellison_2022]
- Kellison, Ariel, Mohit Tekriwal, Jean-Baptiste Jeannin, and Geoffrey Hulette. 2022. "Towards Verified Rounding Error Analysis for Stationary Iterative Methods." In *2022 IEEE/ACM Sixth International Workshop on Software Correctness for HPC Applications (Correctness)*. IEEE. [https://doi.org/10.1109/correctness56720.2022.00007][research_kellison_2022_b]
- Kennedy, Samuel, and Basel Halak. 2025. "Acceleration of McEliece Cryptosystem with Instruction Set Extension for RISC-V." In *2025 IEEE International Conference on Cyber Security and Resilience (CSR)*. IEEE. [https://doi.org/10.1109/csr64739.2025.11130090][research_kennedy_2025]
- Khaldi, Dounia, and Barbara Chapman. 2016. "Towards Automatic HBM Allocation Using LLVM: A Case Study with Knights Landing." In *2016 Third Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2016.007][research_khaldi_2016]
- Khaldi, Dounia, Yuanke Luo, Bing Yu, Alexey Sotkin, Bruno Morais, and Milind Girkar. 2021. "Extending LLVM IR for DPC++ Matrix Support: A Case Study with Intel® Advanced Matrix Extensions (Intel® AMX)." In *2021 IEEE/ACM 7th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvmhpc54804.2021.00008][research_khaldi_2021]
- Khalufa, Abdullah, Graham Riley, and Mikel Lujan. 2019. "POSTER: Runtime Adaptations for Energy-Efficient VSLAM." In *2019 28th International Conference on Parallel Architectures and Compilation Techniques (PACT)*. IEEE. [https://doi.org/10.1109/pact.2019.00052][research_khalufa_2019]
- Khan, M. Zafir Sadik, Nowfel Mashnoor, Mohammad Akyash, Kimia Azar, and Hadi Kamali. 2025. "SAGE-HLS: Syntax-Aware AST-Guided LLM for High-Level Synthesis Code Generation." In *2025 IEEE 43rd International Conference on Computer Design (ICCD)*. IEEE. [https://doi.org/10.1109/iccd65941.2025.00088][research_khan_2025]
- Khanneh, Shada, and Vaibhav Anu. 2022. "Security Requirements Prioritization Techniques: A Survey and Classification Framework." *Software* 1 (4): 450–72. [https://doi.org/10.3390/software1040019][research_khanneh_2022]
- Khuller, Samir, Anna Moss, and Joseph (Seffi) Naor. 1999. "The Budgeted Maximum Coverage Problem." *Information Processing Letters* 70 (1): 39–45. [https://doi.org/10.1016/s0020-0190(99)00031-9][research_khuller_1999]
- Kido, Kengo, Swarat Chaudhuri, and Ichiro Hasuo. 2015. "Abstract Interpretation with Infinitesimals: Towards Scalability in Nonstandard Static Analysis." In *Verification, Model Checking, and Abstract Interpretation*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-662-49122-5\_11][research_kido_2015]
- Kildall, Gary A. 1973. "A Unified Approach to Global Program Optimization." In *Proceedings of the 1st annual ACM SIGACT-SIGPLAN symposium on Principles of programming languages - POPL '73*. ACM Press. [https://doi.org/10.1145/512927.512945][research_kildall_1973]
- Kim, Yoonseung. 2025. "A Formal Verification Library Design for Behavioral Refinement of CompCert Clight." *IEEE Access* 13: 26927–44. [https://doi.org/10.1109/access.2025.3539584][research_kim_2025]
- Kim, Jeewoong, and Shin Hong. 2023. "Poster: BugOss: A Regression Bug Benchmark for Empirical Study of Regression Fuzzing Techniques." In *2023 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst57152.2023.00053][research_kim_2023]
- Kim, Changsu, Shinnung Jeong, Sungjun Cho, et al. 2021. "Thread-Aware Area-Efficient High-Level Synthesis Compiler for Embedded Devices." In *2021 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo51591.2021.9370341][research_kim_2021]
- Kim, Yonghae, and Hyesoon Kim. 2019. "Translating CUDA to OpenCL for Hardware Generation Using Neural Machine Translation." In *2019 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo.2019.8661172][research_kim_2019]
- Kim, Jinyeol, Raehyeong Kim, Jongwon Oh, and Seung Eun Lee. 2024. "Accelerating Embedded WebAssembly Based on FPGA." In *2024 21st International SoC Design Conference (ISOCC)*. IEEE. [https://doi.org/10.1109/isocc62682.2024.10762325][research_kim_2024]
- Kim, Hee Yeon, and Dong Hoon Lee. 2024. "CatchFuzz: Reliable Active Anti-Fuzzing Techniques against Coverage-Guided Fuzzer." *Computers & Security* 143: 103904. [https://doi.org/10.1016/j.cose.2024.103904][research_kim_2024_b]
- Kimura, Yoshiki, Tomoya Kikuchi, Kanemitsu Ootsu, and Takashi Yokota. 2019. "Proposal of Scalable Vector Extension for Embedded RISC-V Soft-Core Processor." In *2019 Seventh International Symposium on Computing and Networking Workshops (CANDARW)*. IEEE. [https://doi.org/10.1109/candarw.2019.00082][research_kimura_2019]
- Kintis, Marinos, Mike Papadakis, Andreas Papadopoulos, Evangelos Valvis, Nicos Malevris, and Yves Le Traon. 2017. "How Effective Are Mutation Testing Tools? An Empirical Analysis of Java Mutation Testing Tools with Manual Analysis and Real Faults." *Empirical Software Engineering* 23 (4): 2426–63. [https://doi.org/10.1007/s10664-017-9582-5][research_kintis_2017]
- Kitchenham, Barbara, Lech Madeyski, and Pearl Brereton. 2019. "Meta-Analysis for Families of Experiments in Software Engineering: A Systematic Review and Reproducibility and Validity Assessment." *Empirical Software Engineering* 25 (1): 353–401. [https://doi.org/10.1007/s10664-019-09747-0][research_kitchenham_2019]
- Klemmer, Lucas, Sonja Gurtner, and Daniel Grose. 2022a. "Formal Verification of SUBLEQ Microcode Implementing the RV32I ISA." In *2022 Forum on Specification & Design Languages (FDL)*. IEEE. [https://doi.org/10.1109/fdl56239.2022.9925662][research_klemmer_2022_b]
- Knoop, Jens, Laura Kovács, and Jakob Zwirchmayr. 2017. "Replacing Conjectures by Positive Knowledge: Inferring Proven Precise Worst-Case Execution Time Bounds Using Symbolic Execution." *Journal of Symbolic Computation* 80: 101–24. [https://doi.org/10.1016/j.jsc.2016.07.023][research_knoop_2017]
- Knuth, Donald E. 1971. "An Empirical Study of FORTRAN Programs." *Software: Practice and Experience* 1 (2): 105–33. [https://doi.org/10.1002/spe.4380010203][research_knuth_1971]
- Ko, Gaeun, and Seonyeong Heo. 2026. "TinyGen: Portable and Compact Code Generation for Tiny Machine Learning." In *Proceedings of the 35th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3771775.3786278][research_ko_2026]
- Koana, Umme Ayman, Quang Hy Le, Shadikur Rahman, Chris Carlson, Francis Chew, and Maleknaz Nayebi. 2024. "Examining Ownership Models in Software Teams: A Systematic Literature Review and a Replication Study." *Empirical Software Engineering* 29 (6): 155. [https://doi.org/10.1007/s10664-024-10538-5][research_koana_2024]
- Kochberger, Patrick, Maximilian Gramberger, Sebastian Schrittwieser, Caroline Lawitschka, and Edgar Weippl. 2023. "Large Language Models for Code Obfuscation Evaluation of the Obfuscation Capabilities of OpenAI’s GPT-3.5 on C Source Code." In *Proceedings of the 20th International Conference on Security and Cryptography*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0012167000003555][research_kochberger_2023]
- Kochhar, Pavneet Singh, Ferdian Thung, and David Lo. 2015. "Code Coverage and Test Suite Effectiveness: Empirical Study with Real Bugs in Large Systems." In *2015 IEEE 22nd International Conference on Software Analysis, Evolution, and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner.2015.7081877][research_kochhar_2015]
- Koehler, Thomas, and Michel Steuwer. 2021. "Towards a Domain-Extensible Compiler: Optimizing an Image Processing Pipeline on Mobile CPUs." In *2021 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo51591.2021.9370337][research_koehler_2021]
- Kongarana, Srinivasa Rao, Ananda Rao Akepogu, and Palagiri Radhika Raju. 2026. "Adaptive and Explainable Test Case Prioritization in Continuous Integration: A Systematic Review of Reinforcement Learning, Learning-to-Rank, and Search-/Combinatorial-Based Methods." *IEEE Access* 14: 59241–64. [https://doi.org/10.1109/access.2026.3683914][research_kongarana_2026]
- Konsaard, Patipat, and Lachana Ramingwong. 2015. "Using Artificial Bee Colony for Code Coverage Based Test Suite Prioritization." In *2015 2nd International Conference on Information Science and Security (ICISS)*. IEEE. [https://doi.org/10.1109/icissec.2015.7371038][research_konsaard_2015]
- Korkut, Joomy. 2026. "A Rose Tree Is Blooming (Proof Pearl)." In *Proceedings of the 15th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3779031.3779091][research_korkut_2026]
- Kosar, Tomaž, Sašo Gaberc, Jeffrey C. Carver, and Marjan Mernik. 2018. "Program Comprehension of Domain-Specific and General-Purpose Languages: Replication of a Family of Experiments Using Integrated Development Environments." *Empirical Software Engineering* 23 (5): 2734–63. [https://doi.org/10.1007/s10664-017-9593-2][research_kosar_2018]
- Kovačević, Željko, Miha Ravber, Shih-Hsi Liu, and Matej Črepinšek. 2022. "Automatic Compiler/interpreter Generation from Programs for Domain-Specific Languages: Code Bloat Problem and Performance Improvement." *Journal of Computer Languages* 70: 101105. [https://doi.org/10.1016/j.cola.2022.101105][research_kovacevic_2022]
- Kruse, Michael, and Hal Finkel. 2018. "User-Directed Loop-Transformations in Clang." In *2018 IEEE/ACM 5th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2018.8639402][research_kruse_2018]
- Ksontini, Emna, Marouane Kessentini, Thiago do N. Ferreira, and Foyzul Hassan. 2021. "Refactorings and Technical Debt in Docker Projects: An Empirical Study." In *2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase51524.2021.9678585][research_ksontini_2021]
- Kumar, Vikash. 2021. "Deep Neural Network Approach to Estimate Early Worst-Case Execution Time." In *2021 IEEE/AIAA 40th Digital Avionics Systems Conference (DASC)*. IEEE. [https://doi.org/10.1109/dasc52595.2021.9594326][research_kumar_2021]
- Kumar, A. R. Ramesh, and U. Karthikeyan. 2026. "Fuzzy-Graph Contrastive Test Case Prioritization Framework for Continuous Integration Pipelines." In *2026 International Conference on Visual Analytics and Data Visualization (ICVADV)*. IEEE. [https://doi.org/10.1109/icvadv67766.2026.11470391][research_kumar_2026]
- Kumar, Ramana, Magnus O. Myreen, Michael Norrish, and Scott Owens. 2014. "CakeML: A Verified Implementation of ML." In *Proceedings of the 41st ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*. ACM. [https://doi.org/10.1145/2535838.2535841][research_kumar_2014]
- Kumar, Vikash, Behnaz Ranjbar, and Akash Kumar. 2024. "Utilizing Machine Learning Techniques for Worst-Case Execution Time Estimation on GPU Architectures." *IEEE Access* 12: 41464–78. [https://doi.org/10.1109/access.2024.3379018][research_kumar_2024]
- Kumari, Sweta, and Shashank Pushkar. 2018. "Cuckoo Search Based Hybrid Models for Improving the Accuracy of Software Effort Estimation." *Microsystem Technologies* 24 (12): 4767–74. [https://doi.org/10.1007/s00542-018-3871-9][research_kumari_2018]
- Kuo, Yao-Ming, Mark F. Flanagan, Francisco Garcia-Herrero, Õscar Ruano, and Juan Antonio Maestro. 2023. "Integration of a Real-Time CCSDS 410.0-B-32 Error-Correction Decoder on FPGA-Based RISC-V SoCs Using RISC-V Vector Extension." *IEEE Transactions on Aerospace and Electronic Systems*: 1–12. [https://doi.org/10.1109/taes.2023.3266314][research_kuo_2023]
- Kuriakose, Jaison, and Jeffrey Parsons. 2015. "How Do Open Source Software (OSS) Developers Practice and Perceive Requirements Engineering? An Empirical Study." In *2015 IEEE Fifth International Workshop on Empirical Requirements Engineering (EmpiRE)*. IEEE. [https://doi.org/10.1109/empire.2015.7431307][research_kuriakose_2015]
- Kuroki, Michihiro, and Toshihiko Yamasaki. 2024. "Explaining 3D Object Detection through Shapley Value-Based Attribution Map." In *2024 IEEE International Conference on Image Processing (ICIP)*. IEEE. [https://doi.org/10.1109/icip51287.2024.10647574][research_kuroki_2024]
- Kwon, Jaeseong, Bongjun Jang, Juneyoung Lee, and Kihong Heo. 2025. "Optimization-Directed Compiler Fuzzing for Continuous Translation Validation." *Proceedings of the ACM on Programming Languages* 9 (PLDI): 627–50. [https://doi.org/10.1145/3729275][research_kwon_2025]
- Kwon, Hyunjeong, Youngsu Kwon, and Jinho Han. 2022. "Backward Graph Construction and Lowering in DL Compiler for Model Training on AI Accelerators." In *2022 19th International SoC Design Conference (ISOCC)*. IEEE. [https://doi.org/10.1109/isocc56007.2022.10031488][research_kwon_2022]
- Kwon, Hyunho, Sanggyu Shin, Ju Min Lee, et al. 2026. "Compiler-Runtime Co-Operative Chain of Verification for LLM-Based Code Optimization." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395240][research_kwon_2026]
- Laaber, Christoph, Harald C. Gall, and Philipp Leitner. 2021. "Applying Test Case Prioritization to Software Microbenchmarks." *Empirical Software Engineering* 26 (6): 133. [https://doi.org/10.1007/s10664-021-10037-x][research_laaber_2021]
- Lachmann, Remo, Sandro Schulze, Manuel Nieke, Christoph Seidl, and Ina Schaefer. 2016. "System-Level Test Case Prioritization Using Machine Learning." In *2016 15th IEEE International Conference on Machine Learning and Applications (ICMLA)*. IEEE. [https://doi.org/10.1109/icmla.2016.0065][research_lachmann_2016]
- Lage, Luiz Carlos da Fonseca, Marcos Kalinowski, Daniela Trevisan, and Rodrigo Spinola. 2019. "Usability Technical Debt in Software Projects: A Multi-Case Study." In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2019.8870180][research_lage_2019]
- Laguna, Ignacio, Patrick Chapman, Konstantinos Parasyris, Giorgis Georgakoudis, and Cindy Rubio-González. 2024. "Testing the Unknown: A Framework for OpenMP Testing via Random Program Generation." In *SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis*. IEEE. [https://doi.org/10.1109/scw63240.2024.00080][research_laguna_2024]
- Laiq, Muhammad, Nauman bin Ali, Jürgen Börstler, and Emelie Engström. 2024. "Industrial Adoption of Machine Learning Techniques for Early Identification of Invalid Bug Reports." *Empirical Software Engineering* 29 (5): 130. [https://doi.org/10.1007/s10664-024-10502-3][research_laiq_2024]
- Lammich, Peter. 2024. "Refinement of Parallel Algorithms down to LLVM: Applied to Practically Efficient Parallel Sorting." *Journal of Automated Reasoning* 68 (3): 14. [https://doi.org/10.1007/s10817-024-09701-w][research_lammich_2024]
- Lancellotti, Giacomo, Filippo Buda, Giacomo Carugati, et al. 2026b. "Quantum Oracle Synthesis from HDL Designs via Multi Level Intermediate Representation." In *2026 31st Asia and South Pacific Design Automation Conference (ASP-DAC)*. IEEE. [https://doi.org/10.1109/asp-dac66049.2026.11420750][research_lancellotti_2026_b]
- Laskurain, Unai, Aitor Aguirre-Ortuzar, and Urko Zurutuza. 2025. "Privacy-Preserving Feature Valuation in Vertical Federated Learning Using Shapley-CMI and PSI Permutation." In *2025 3rd International Conference on Federated Learning Technologies and Applications (FLTA)*. IEEE. [https://doi.org/10.1109/flta67013.2025.11336639][research_laskurain_2025]
- Lasnier, Pascal Y., Jeremy Yallop, and Magnus O. Myreen. 2026a. "Brack: A Verified Compiler for Scheme via CakeML." In *Proceedings of the 15th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3779031.3779098][research_lasnier_2026]
- Lasser, Sam, Chris Casinghino, Kathleen Fisher, and Cody Roux. 2021. "CoStar: A Verified ALL(\*) Parser." In *Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3453483.3454053][research_lasser_2021]
- Lattner, C., and V. Adve. 2004. "LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation." In *International Symposium on Code Generation and Optimization, 2004. CGO 2004.*. IEEE. [https://doi.org/10.1109/cgo.2004.1281665][research_lattner_adve_2004]
- Lattner, Chris, Mehdi Amini, Uday Bondhugula, et al. 2021. "MLIR: Scaling Compiler Infrastructure for Domain Specific Computation." In *2021 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo51591.2021.9370308][research_lattner_2021]
- Laurent, Thomas, Mike Papadakis, Marinos Kintis, Christopher Henard, Yves Le Traon, and Anthony Ventresque. 2017. "Assessing and Improving the Mutation Testing Practice of PIT." In *2017 IEEE International Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst.2017.47][research_laurent_2017]
- Lauwaerts, Tom, Robbert Gurdeep Singh, and Christophe Scholliers. 2024. "WARDuino: An Embedded WebAssembly Virtual Machine." *Journal of Computer Languages* 79: 101268. [https://doi.org/10.1016/j.cola.2024.101268][research_lauwaerts_2024]
- Le, Vu, Mehrdad Afshari, and Zhendong Su. 2014. "Compiler Validation via Equivalence Modulo Inputs." In *Proceedings of the 35th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/2594291.2594334][research_le_2014]
- Le, Vu, Chengnian Sun, and Zhendong Su. 2015. "Finding Deep Compiler Bugs via Guided Stochastic Program Mutation." *ACM SIGPLAN Notices* 50 (10): 386–99. [https://doi.org/10.1145/2858965.2814319][research_le_2015]
- Le Dilavrec, Quentin, and Andy Zaidman. 2025. "HyperAST: Incrementally Mining Large Source Code Repositories." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00079][research_ledilavrec_2025]
- Lecoeur, Bastien, Hasan Mohsin, and Alastair F. Donaldson. 2023. "Program Reconditioning: Avoiding Undefined Behaviour When Finding and Reducing Compiler Bugs." *Proceedings of the ACM on Programming Languages* 7 (PLDI): 1801–25. [https://doi.org/10.1145/3591294][research_lecoeur_2023]
- Lee, Ahcheong, Irfan Ariq, Yunho Kim, and Moonzoo Kim. 2022. "POWER: Program Option-Aware Fuzzer for High Bug Detection Ability." In *2022 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst53961.2022.00032][research_lee_2022]
- Lee, Juneyoung, Chung-Kil Hur, Ralf Jung, Zhengyang Liu, John Regehr, and Nuno P. Lopes. 2018. "Reconciling High-Level Optimizations and Low-Level Code in LLVM." *Proceedings of the ACM on Programming Languages* 2 (OOPSLA): 1–28. [https://doi.org/10.1145/3276495][research_lee_2018]
- Lee, Juneyoung, Chung-Kil Hur, and Nuno P. Lopes. 2019a. "AliveInLean: A Verified LLVM Peephole Optimization Verifier." In *Computer Aided Verification*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-25543-5\_25][research_lee_2019_b]
- Lee, Juneyoung, Yoonseung Kim, Youngju Song, et al. 2017. "Taming Undefined Behavior in LLVM." *ACM SIGPLAN Notices* 52 (6): 633–47. [https://doi.org/10.1145/3140587.3062343][research_lee_2017]
- Lee, Seung-Min, Soojin Park, and Young B. Park. 2019b. "Formal Specification Technique in Smart Contract Verification." In *2019 International Conference on Platform Technology and Service (PlatCon)*. IEEE. [https://doi.org/10.1109/platcon.2019.8669419][research_lee_2019]
- Lehmann, Can Joshua, Lars Bauer, Hassan Nassar, Heba Khdr, and Jörg Henkel. 2025. "Hardware/Software Co-Analysis for Worst Case Execution Time Bounds." In *2025 Design, Automation & Test in Europe Conference (DATE)*. IEEE. [https://doi.org/10.23919/date64628.2025.10992765][research_lehmann_2025]
- Lei, Yi, and Yabo Chen. 2018. "Optimization of Specific Instruction Set Processor for Image Algorithms." *Procedia Computer Science* 131: 182–91. [https://doi.org/10.1016/j.procs.2018.04.202][research_lei_2018]
- Leidel, John, Ryan Kabrick, and David Donofrio. 2021. "Toward an Automated Hardware Pipelining LLVM Pass Infrastructure." In *2021 IEEE/ACM 7th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvmhpc54804.2021.00010][research_leidel_2021]
- Leinen, Fabian, Daniel Elsner, Alexander Pretschner, Andreas Stahlbauer, Michael Sailer, and Elmar Jürgens. 2024. "Cost of Flaky Tests in Continuous Integration: An Industrial Case Study." In *2024 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst60714.2024.00037][research_leinen_2024]
- Lenarduzzi, Valentina, Terese Besker, Davide Taibi, Antonio Martini, and Francesca Arcelli Fontana. 2021. "A Systematic Literature Review on Technical Debt Prioritization: Strategies, Processes, Factors, and Tools." *Journal of Systems and Software* 171: 110827. [https://doi.org/10.1016/j.jss.2020.110827][research_lenarduzzi_2021]
- Lenarduzzi, Valentina, Teemu Orava, Nyyti Saarimaki, Kari Systa, and Davide Taibi. 2019. "An Empirical Study on Technical Debt in a Finnish SME." In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2019.8870169][research_lenarduzzi_2019]
- Leopoldseder, David, Lukas Stadler, Manuel Rigger, Thomas Würthinger, and Hanspeter Mössenböck. 2018a. "A Cost Model for a Graph-Based Intermediate-Representation in a Dynamic Compiler." In *Proceedings of the 10th ACM SIGPLAN International Workshop on Virtual Machines and Intermediate Languages*. ACM. [https://doi.org/10.1145/3281287.3281290][research_leopoldseder_2018_b]
- Leroy, Xavier. 2003. "Java Bytecode Verification: Algorithms and Formalizations." *Journal of Automated Reasoning* 30 (3–4): 235–69. [https://doi.org/10.1023/a:1025055424017][research_leroy_2003]
- Letras, Martín, Jorge Echavarria, Muhammad Nufail Farooqi, et al. 2025. "Towards a Unified Multi-Target Mlir-Based Compiler: A Heterogeneous Compilation Framework for High-Performance and Quantum Computing Integration." In *2025 IEEE International Conference on Quantum Computing and Engineering (QCE)*. IEEE. [https://doi.org/10.1109/qce65121.2025.10288][research_letras_2025]
- Levén, William, Hampus Broman, Terese Besker, and Richard Torkar. 2024. "The Broken Windows Theory Applies to Technical Debt." *Empirical Software Engineering* 29 (4): 73. [https://doi.org/10.1007/s10664-024-10456-6][research_leven_2024]
- Li, Zihang. 2025. "Low-Power Implementation of DSP Instruction Set Extension and Audio Signal Denoising Algorithm in Embedded RISC-V System." In *2025 3rd International Conference on Business Analytics for Technology and Security (ICBATS)*. IEEE. [https://doi.org/10.1109/icbats66542.2025.11258097][research_li_2025]
- Li, Jianan, Xiaonan Chai, and Wei Gao. 2026b. "Unleashing Triton on CPUs: Compilation and Runtime Co-Optimization for Scalable Vector Architectures." *Computers* 15 (7): 406. [https://doi.org/10.3390/computers15070406][research_li_2026]
- Li, Yinghua, Xueqi Dang, Wendkûuni C. Ouédraogo, Jacques Klein, and Tegawendé F. Bissyandé. 2026a. "Test Input Prioritization for Image Segmentation: An Empirical Study." *Empirical Software Engineering* 32 (1): 8. [https://doi.org/10.1007/s10664-026-10932-1][research_li_2026_c]
- Li, Letitia W., Greg Eakman, Elias J. M. Garcia, and Sam Atman. 2021a. "Accessible Formal Methods for Verified Parser Development." In *2021 IEEE Security and Privacy Workshops (SPW)*. IEEE. [https://doi.org/10.1109/spw53761.2021.00028][research_li_2021]
- Li, Yalong, and Junxia Guo. 2024. "Research on Program Automatic Repair Method Combining Context Optimization Strategy and Large Language Models." In *2024 4th International Symposium on Computer Technology and Information Science (ISCTIS)*. IEEE. [https://doi.org/10.1109/isctis63324.2024.10698980][research_li_2024_d]
- Li, Yahui, and Guangjie Li. 2023. "An Empirical Study on the Correlation between Neuron Coverage and Code Coverage." In *2023 3rd International Symposium on Computer Technology and Information Science (ISCTIS)*. IEEE. [https://doi.org/10.1109/isctis58954.2023.10213091][research_li_2023_d]
- Li, Angela, and David Li. 2025. "Reward-Aware Shapley Compensation: A Probabilistic and Game-Theoretic Approach in Cooperative Sharing Economies." In *2025 IEEE International Conference on Big Data (BigData)*. IEEE. [https://doi.org/10.1109/bigdata66926.2025.11401593][research_li_2025_f]
- Li, Wei, Qingan Li, Yunlong Ming, Weijiao Dai, Shi Ying, and Mengting Yuan. 2022b. "An Empirical Study of the Effectiveness of IR-Based Bug Localization for Large-Scale Industrial Projects." *Empirical Software Engineering* 27 (2): 47. [https://doi.org/10.1007/s10664-021-10082-6][research_li_2022_c]
- Li, Mingzhen, Yi Liu, Bangduo Chen, Hailong Yang, Zhongzhi Luan, and Depei Qian. 2023b. "Building a Domain-Specific Compiler for Emerging Processors with a Reusable Approach." *Science China Information Sciences* 67 (1): 112101. [https://doi.org/10.1007/s11432-022-3727-6][research_li_2023]
- Li, Lantian, Zhihao Liu, and Zhongxing Yu. 2025g. "Solsmith: Solidity Random Program Generator for Compiler Testing." In *2025 25th International Conference on Software Quality, Reliability, and Security Companion (QRS-C)*. IEEE. [https://doi.org/10.1109/qrs-c65679.2025.00031][research_li_2025_c]
- Li, Ruo-Shi, Ping Peng, Zhi-Yuan Shao, Hai Jin, and Ran Zheng. 2023c. "Evaluating RISC-V Vector Instruction Set Architecture Extension with Computer Vision Workloads." *Journal of Computer Science and Technology* 38 (4): 807–20. [https://doi.org/10.1007/s11390-023-1266-6][research_li_2023_b]
- Li, Yikun, Mohamed Soliman, and Paris Avgeriou. 2022c. "Identifying Self-Admitted Technical Debt in Issue Tracking Systems Using Machine Learning." *Empirical Software Engineering* 27 (6): 131. [https://doi.org/10.1007/s10664-022-10128-3][research_li_2022_d]
- Li, Yikun, Mohamed Soliman, and Paris Avgeriou. 2023a. "Automatic Identification of Self-Admitted Technical Debt from Four Different Sources." *Empirical Software Engineering* 28 (3): 65. [https://doi.org/10.1007/s10664-023-10297-9][research_li_2023_f]
- Li, Meng, Hengyang Sun, Yanjun Huang, and Hong Chen. 2024c. "Shapley Value: From Cooperative Game to Explainable Artificial Intelligence." *Autonomous Intelligent Systems* 4 (1): 2. [https://doi.org/10.1007/s43684-023-00060-8][research_li_2024_c]
- Li, Shaohua, Theodoros Theodoridis, and Zhendong Su. 2024a. "Boosting Compiler Testing by Injecting Real-World Code." *Proceedings of the ACM on Programming Languages* 8 (PLDI): 223–45. [https://doi.org/10.1145/3656386][research_li_2024_b]
- Li, Zhiwei, and Cheng Wang. 2026. "Light Shapley: Improving the Scalability of Equitable Data Utility Valuation." *IEEE Transactions on Knowledge and Data Engineering* 38 (3): 1826–42. [https://doi.org/10.1109/tkde.2026.3651564][research_li_2026_b]
- Li, Yingling, Ziao Wang, Junjie Wang, Jie Chen, Rui Mou, and Guibing Li. 2023d. "Semantic-Aware Two-Phase Test Case Prioritization for Continuous Integration." *Software Testing, Verification and Reliability* 34 (1): e1864. [https://doi.org/10.1002/stvr.1864][research_li_2023_e]
- Li, Nan, Michael West, Anthony Escalona, and Vinicius H. S. Durelli. 2015. "Mutation Testing in Practice Using Ruby." In *2015 IEEE Eighth International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw.2015.7107453][research_li_2015]
- Li, Jizhe, Haoran Xu, Yongjun Wang, et al. 2025e. "Fuzzing JavaScript JIT Compilers with a High-Quality Differential Test Oracle." *Computers & Security* 159: 104660. [https://doi.org/10.1016/j.cose.2025.104660][research_li_2025_b]
- Li, Jiajun, Wenhua Yang, Minxue Pan, and Yu Zhou. 2025i. "Understanding Feature Request Practice on GitHub via a Large-Scale Empirical Study." In *2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase63991.2025.00228][research_li_2025_d]
- Li, Guowei, Yang Yang, Zhaolin Wu, Tiange Cao, Yong Liu, and Zheng Li. 2021b. "Weighted Reward for Reinforcement Learning Based Test Case Prioritization in Continuous Integration Testing." In *2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC)*. IEEE. [https://doi.org/10.1109/compsac51774.2021.00132][research_li_2021_b]
- Li, Jiangnan, Zhengyi Zhang, Xuegong Zhou, and Lingli Wang. 2024b. "An MLIR-Based Compiler for Hardware Acceleration with Recursion Support: (PhD Forum Paper)." In *2024 International Conference on Field Programmable Technology (ICFPT)*. IEEE. [https://doi.org/10.1109/icfpt64416.2024.11113451][research_li_2024]
- Li, Chenglin, Yangyang Zhao, and Yibiao Yang. 2022a. "An Empirical Study of the Bug Link Rate." In *2022 IEEE 22nd International Conference on Software Quality, Reliability and Security (QRS)*. IEEE. [https://doi.org/10.1109/qrs57517.2022.00028][research_li_2022_b]
- Li, Ziye, Ruiqi Zhao, Hanke Zhang, and Xiaohua Shi. 2025a. "Accelerating Startup Time of React Native Applications by Compiling JavaScript Ahead-Of-Time under Network Communication Security." *Transactions on Emerging Telecommunications Technologies* 36 (9): e70232. [https://doi.org/10.1002/ett.70232][research_li_2025_j]
- Li, Mengyang, Weiyao Zhu, and Ou Wu. 2025h. "Toward Learnable and Interpretable Data Shapley Valuation for Deep Learning." *Knowledge-Based Systems* 325: 114002. [https://doi.org/10.1016/j.knosys.2025.114002][research_li_2025_g]
- Liang, Jianyuan, Shuyang Hou, Wenjie Chen, et al. 2026. "GeoAutoModuler: A Knowledge–enhanced Large Language Model for Heterogeneous Geospatial Code Understanding and Knowledge Extraction." *Big Earth Data* 10 (3): 1785–1826. [https://doi.org/10.1080/20964471.2026.2689760][research_liang_2026]
- Liang, Jingjing, Shan Huang, and Ting Su. 2025b. "Finding Bugs in MLIR Compiler Infrastructure via Lowering Space Exploration." In *2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase63991.2025.00059][research_liang_2025]
- Liao, Zhifang, Xiaofei Qi, Yan Zhang, Xiaoping Fan, and Yun Zhou. 2020. "How to Evaluate the Productivity of Software Ecosystem: A Case Study in GitHub." *Scientific Programming* 2020: 1–13. [https://doi.org/10.1155/2020/8814247][research_liao_2020]
- Lidbury, Christopher, Andrei Lascu, Nathan Chong, and Alastair F. Donaldson. 2015. "Many-Core Compiler Fuzzing." In *Proceedings of the 36th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/2737924.2737986][research_lidbury_2015]
- Lim, HeuiChan, and Saumya Debray. 2023. "Automatically Localizing Dynamic Code Generation Bugs in JIT Compiler Back-End." In *Proceedings of the 32nd ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3578360.3580260][research_lim_2023]
- Lima, Jackson A. Prado, and Silvia Regina Vergilio. 2022. "A Multi-Armed Bandit Approach for Test Case Prioritization in Continuous Integration Environments." *IEEE Transactions on Software Engineering* 48 (2): 453–65. [https://doi.org/10.1109/tse.2020.2992428][research_lima_2022]
- Lin, Yan, and Debin Gao. 2021. "When Function Signature Recovery Meets Compiler Optimization." In *2021 IEEE Symposium on Security and Privacy (SP)*. IEEE. [https://doi.org/10.1109/sp40001.2021.00006][research_lin_2021]
- Lin, Pei-Hung, and Chunhua Liao. 2021. "High-Precision Evaluation of Both Static and Dynamic Tools Using DataRaceBench." In *2021 IEEE/ACM 5th International Workshop on Software Correctness for HPC Applications (Correctness)*. IEEE. [https://doi.org/10.1109/correctness54621.2021.00011][research_lin_2021_b]
- Lin, Renze, Ran Wang, Guanghuan Hu, and Xianghua Xu. 2025. "LMFuzz: Program Repair Fuzzing Based on Large Language Models." *Automated Software Engineering* 33 (1): 25. [https://doi.org/10.1007/s10515-025-00568-8][research_lin_2025]
- Lin, Jiahuei, Haoxiang Zhang, Bram Adams, and Ahmed E. Hassan. 2022. "Upstream Bug Management in Linux Distributions: An Empirical Study of Debian and Fedora Practices." *Empirical Software Engineering* 27 (6): 134. [https://doi.org/10.1007/s10664-022-10173-y][research_lin_2022]
- Lion, Benjamin, and David Broman. 2026. "Making Time Observable: Compiler Correctness for Real-Time C Programs." In *2026 IEEE Workshop on Formal Arguments for CPS Certification (FACCT)*. IEEE. [https://doi.org/10.1109/facct71761.2026.00011][research_lion_2026]
- Liu, Shaoying. 2016. "Testing-Based Formal Verification for Theorems and Its Application in Software Specification Verification." In *Tests and Proofs*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-41135-4\_7][research_liu_2016]
- Liu, Yiqi. 2017. "Adaptive Just-in-Time and Relevant Vector Machine Based Soft-Sensors with Adaptive Differential Evolution Algorithms for Parameter Optimization." *Chemical Engineering Science* 172: 571–84. [https://doi.org/10.1016/j.ces.2017.07.006][research_liu_2017]
- Liu, Ji, Luciano Bello, and Huiyang Zhou. 2021b. "Relaxed Peephole Optimization: A Novel Compiler Optimization for Quantum Circuits." In *2021 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo51591.2021.9370310][research_liu_2021]
- Liu, Amanda, Gilbert Bernstein, Adam Chlipala, and Jonathan Ragan-Kelley. 2024c. "A Verified Compiler for a Functional Tensor Language." *Proceedings of the ACM on Programming Languages* 8 (PLDI): 320–42. [https://doi.org/10.1145/3656390][research_liu_2024_b]
- Liu, Quanming, Xupeng Bu, Zhichao Yan, and Ru Li. 2025d. "T 3: Multi-Level Tree-Based Automatic Program Repair with Large Language Models." In *2025 International Joint Conference on Neural Networks (IJCNN)*. IEEE. [https://doi.org/10.1109/ijcnn64981.2025.11228000][research_liu_2025_e]
- Liu, Bin, Zihan Chen, Huijuan Wang, and Weili Wu. 2022c. "An Optimal Streaming Algorithm for Non-Submodular Functions Maximization on the Integer Lattice." *Journal of Combinatorial Optimization* 45 (1): 42. [https://doi.org/10.1007/s10878-022-00975-7][research_liu_2022_b]
- Liu, Zixin, Xiaozhi Du, and Hairui Liu. 2025b. "ReAPR: Automatic Program Repair via Retrieval-Augmented Large Language Models." *Software Quality Journal* 33 (3): 30. [https://doi.org/10.1007/s11219-025-09728-1][research_liu_2025_d]
- Liu, Hui, Hanbin Guo, Peng Liu, and Tongding Hou. 2025a. "BoostPolyGlot: A Structured IR Generation-Based Fuzz Testing Framework for GCC Compiler Frontend." *Applied Sciences* 15 (11): 5935. [https://doi.org/10.3390/app15115935][research_liu_2025_c]
- Liu, Zhili, Hao Jiang, Dandan Zheng, Kai Huang, Dongliang Xiong, and Xiaowen Jiang. 2022b. "An Efficient Application Specific Instruction Set Processor for Multi-Tone Digital Halftoning." In *2022 2nd International Conference on Consumer Electronics and Computer Engineering (ICCECE)*. IEEE. [https://doi.org/10.1109/iccece54139.2022.9712838][research_liu_2022]
- Liu, Bing, Shiva Nejati, Lucia, and Lionel C. Briand. 2018. "Effective Fault Localization of Automotive Simulink Models: Achieving the Trade-off between Test Oracle Effort and Fault Localization Accuracy." *Empirical Software Engineering* 24 (1): 444–90. [https://doi.org/10.1007/s10664-018-9611-z][research_liu_2018]
- Liu, Jie, Jianzong Wang, Xiaoyang Qu, Bo Chen, Zihang Wei, and Jing Xiao. 2021a. "Automatic Joint Optimization of Algorithm-Level Compression and Compiler-Based Acceleration with Reinforcement Learning for DNN in Edge Devices." In *2021 International Joint Conference on Neural Networks (IJCNN)*. IEEE. [https://doi.org/10.1109/ijcnn52387.2021.9533729][research_liu_2021_c]
- Liu, Chang, Yan-Jun Wu, Jing-Zheng Wu, and Chen Zhao. 2023a. "A Buffer Overflow Detection and Defense Method Based on RISC-V Instruction Set Extension." *Cybersecurity* 6 (1): 45. [https://doi.org/10.1186/s42400-023-00164-x][research_liu_2023]
- Liu, Hui, Jinlong Xu, Sen Chen, and Te Guo. 2022a. "Compiler Optimization Parameter Selection Method Based on Ensemble Learning." *Electronics* 11 (15): 2452. [https://doi.org/10.3390/electronics11152452][research_liu_2022_c]
- Lochbihler, Andreas. 2018. "Mechanising a Type-Safe Model of Multithreaded Java with a Verified Compiler." *Journal of Automated Reasoning* 61 (1–4): 243–332. [https://doi.org/10.1007/s10817-018-9452-x][research_lochbihler_2018]
- Longchar, Imlijungla, Kaustubh Khutal, Ashwath C. Reddy, Amey Varhade, and Hemangee K. Kapoor. 2025. "RI-MAC: Optimising MAC Operation Using Custom RISC-V Instruction Set for Neural Network Inference." In *2025 5th International Conference on AI-ML-Systems (AIMLSystems)*. IEEE. [https://doi.org/10.1109/aimlsystems67835.2025.11330892][research_longchar_2025]
- Lööw, Andreas. 2021. "Lutsig: A Verified Verilog Compiler for Verified Circuit Development." In *Proceedings of the 10th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3437992.3439916][research_loow_2021]
- Lööw, Andreas, Ramana Kumar, Yong Kiam Tan, et al. 2019. "Verified Compilation on a Verified Processor." In *Proceedings of the 40th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3314221.3314622][research_loow_2019]
- Lopes, Nuno P., Juneyoung Lee, Chung-Kil Hur, Zhengyang Liu, and John Regehr. 2021. "Alive2: Bounded Translation Validation for LLVM." In *Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3453483.3454030][research_lopes_2021]
- Lowther, Duncan, Dejice Jacob, and Jeremy Singer. 2023. "CHERI Performance Enhancement for a Bytecode Interpreter." In *Proceedings of the 15th ACM SIGPLAN International Workshop on Virtual Machines and Intermediate Languages*. ACM. [https://doi.org/10.1145/3623507.3623552][research_lowther_2023]
- Lozachmeur, Fabrice, and Arnaud Tisserand. 2023. "A RISC-V Instruction Set Extension for Flexible Hardware/Software Protection of Cryptosystems Masked at High Orders." In *2023 IEEE 66th International Midwest Symposium on Circuits and Systems (MWSCAS)*. IEEE. [https://doi.org/10.1109/mwscas57524.2023.10405991][research_lozachmeur_2023]
- Lozov, Peter, Dmitry Kosarev, Dmitry Ivanov, and Dmitry Boulytchev. 2023. "Relational Solver for Java Generics Type System." In *Logic-Based Program Synthesis and Transformation*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-45784-5\_8][research_lozov_2023]
- Lu, Han-Lin, Zong-Yuan Wu, Chien-Hsing Wu, Guan-Zhong Wang, and Shih-Kun Huang. 2024. "Fuzzing Command-Line Interface by Edge Coverage Guided Combinatorial Testing and Input Clustering." In *2024 IEEE 24th International Conference on Software Quality, Reliability and Security (QRS)*. IEEE. [https://doi.org/10.1109/qrs62785.2024.00058][research_lu_2024]
- Lu, Cheng, Jiusun Zeng, Yu Xia, Jinhui Cai, and Shihua Luo. 2026b. "Energy-Based Model for Accurate Estimation of Shapley Values in Feature Attribution." *IEEE Transactions on Pattern Analysis and Machine Intelligence* 48 (3): 2496–2513. [https://doi.org/10.1109/tpami.2025.3626404][research_lu_2026_b]
- Lu, Zeyu, Peng Zhang, Yuge Nie, et al. 2026a. "Beyond Coverage: Automatic Test Suite Augmentation for Enhanced Effectiveness Using Large Language Models." *Proceedings of the ACM on Programming Languages* 10 (OOPSLA1): 1403–31. [https://doi.org/10.1145/3798251][research_lu_2026]
- Lu, Xinyi, Zhide Zhou, Xiaochen Li, et al. 2025. "Detecting WebAssembly Runtime Bugs with Grammar-Guided Program Mutation." *IEEE Transactions on Reliability* 74 (4): 5056–69. [https://doi.org/10.1109/tr.2025.3614352][research_lu_2025]
- Luan, Jiajun, Rui Shan, Gang Cai, and Zhihong Huang. 2025. "Research on RISC-V-Based Edge Convolution Acceleration Extension Instruction Set." In *2025 4th International Symposium on Semiconductor and Electronic Technology (ISSET)*. IEEE. [https://doi.org/10.1109/isset66828.2025.11184959][research_luan_2025]
- Lücke, Martin, Michel Steuwer, and Aaron Smith. 2021. "Integrating a Functional Pattern-Based IR into MLIR." In *Proceedings of the 30th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3446804.3446844][research_lucke_2021]
- Luo, Chenke, Jiang Ming, Jianming Fu, Guojun Peng, and Zhetao Li. 2023. "Reverse Engineering of Obfuscated Lua Bytecode via Interpreter Semantics Testing." *IEEE Transactions on Information Forensics and Security* 18: 3891–3905. [https://doi.org/10.1109/tifs.2023.3289254][research_luo_2023]
- Luo, Junjie, Shangzhou Xia, Fuyuan Zhang, and Jianjun Zhao. 2026. "QEMI: A Quantum Software Stacks Testing Framework via Equivalence Modulo Inputs." In *Fundamental Approaches to Software Engineering*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-032-22774-4\_8][research_luo_2026]
- Lyu, Qian, Dalin Zhang, Rihan Da, and Hailong Zhang. 2021. "ReFuzz: A Remedy for Saturation in Coverage-Guided Fuzzing." *Electronics* 10 (16): 1921. [https://doi.org/10.3390/electronics10161921][research_lyu_2021]
- Ma, Lei, Cheng Zhang, Bing Yu, and Hiroyuki Sato. 2015. "An Empirical Study on Effects of Code Visibility on Code Coverage of Software Testing." In *2015 IEEE/ACM 10th International Workshop on Automation of Software Test*. IEEE. [https://doi.org/10.1109/ast.2015.23][research_ma_2015]
- Macháček, Roman, Anastasiia Grishina, Max Hort, and Leon Moonen. 2025. "The Impact of Fine-Tuning Large Language Models on Automated Program Repair." In *2025 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme64153.2025.00042][research_machacek_2025]
- Madeiral, Fernanda, and Thomas Durieux. 2021. "A Large-Scale Study on Human-Cloned Changes for Automated Program Repair." In *2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr52588.2021.00064][research_madeiral_2021]
- Maeng, Kiwan, and Brandon Lucia. 2024. "Compiler-Based Memory Encryption for Machine Learning on Commodity Low-Power Devices." In *Proceedings of the 33rd ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3640537.3641564][research_maeng_2024]
- Maes-Bermejo, Michel, Micael Gallego, Francisco Gortázar, Gregorio Robles, and Jesus M. Gonzalez-Barahona. 2022. "Revisiting the Building of past Snapshots — A Replication and Reproduction Study." *Empirical Software Engineering* 27 (3): 65. [https://doi.org/10.1007/s10664-022-10117-6][research_maesbermejo_2022]
- Mahmood, Yasir, Nazri Kama, Azri Azmi, and Mazlan Ali. 2020. "Improving Estimation Accuracy Prediction of Software Development Effort: A Proposed Ensemble Model." In *2020 International Conference on Electrical, Communication, and Computer Engineering (ICECCE)*. IEEE. [https://doi.org/10.1109/icecce49384.2020.9179279][research_mahmood_2020]
- Mahmood, Yasir, Nazri Kama, Azri Azmi, Ahmad Salman Khan, and Mazlan Ali. 2021. "Software Effort Estimation Accuracy Prediction of Machine Learning Techniques: A Systematic Performance Evaluation." *Software: Practice and Experience* 52 (1): 39–65. [https://doi.org/10.1002/spe.3009][research_mahmood_2021]
- Mahmoudi, Ahmed, Christopher Horn, Saleh Mulhem, Rainer Buchty, Mladen Berekovic, and Rolf Meyer. 2025. "TinyML Unleashed: Accelerating TensorFlow Lite Micro Kernels with RISC-V Vector Extension." In *2025 33rd Telecommunications Forum (TELFOR)*. IEEE. [https://doi.org/10.1109/telfor67910.2025.11314213][research_mahmoudi_2025]
- Maia, Luís, Simão Cunha, and João Saraiva. 2026. "Why Just-In-Time Compilation Matters: Evaluating Runtime and Energy Efficiency." In *Proceedings of the 19th ACM SIGPLAN International Conference on Software Language Engineering*. ACM. [https://doi.org/10.1145/3806383.3815520][research_maia_2026]
- Maipradit, Rungroj, Christoph Treude, Hideaki Hata, and Kenichi Matsumoto. 2020. "Wait for It: Identifying “on-Hold” Self-Admitted Technical Debt." *Empirical Software Engineering* 25 (5): 3770–98. [https://doi.org/10.1007/s10664-020-09854-3][research_maipradit_2020]
- Maipradit, Rungroj, Christoph Treude, Hideaki Hata, and Kenichi Matsumoto. 2021. "Correction To: Wait for It: Identifying “on-Hold” Self-Admitted Technical Debt." *Empirical Software Engineering* 26 (3): 33. [https://doi.org/10.1007/s10664-021-09939-7][research_maipradit_2021]
- Maisto, Vincenzo, and Alessandro Cilardo. 2022. "A Pluggable Vector Unit for RISC-V Vector Extension." In *2022 Design, Automation & Test in Europe Conference & Exhibition (DATE)*. IEEE. [https://doi.org/10.23919/date54114.2022.9774501][research_maisto_2022]
- Majumder, Abhilash. 2026. "Inductor-TV: Formal Methods for the Pytorch Compiler." In *2026 7th International Conference on Artificial Intelligence, Robotics, and Control (AIRC)*. IEEE. [https://doi.org/10.1109/airc69745.2026.11631461][research_majumder_2026]
- Mamata, Rezwana, Akramul Azim, Ramiro Liscano, et al. 2023. "Test Case Prioritization Using Transfer Learning in Continuous Integration Environments." In *2023 IEEE/ACM International Conference on Automation of Software Test (AST)*. IEEE. [https://doi.org/10.1109/ast58925.2023.00023][research_mamata_2023]
- Mammadli, Rahim, Ali Jannesari, and Felix Wolf. 2020. "Static Neural Compiler Optimization via Deep Reinforcement Learning." In *2020 IEEE/ACM 6th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC) and Workshop on Hierarchical Parallelism for Exascale Computing (HiPar)*. IEEE. [https://doi.org/10.1109/llvmhpchipar51896.2020.00006][research_mammadli_2020]
- Mandal, Dipan Kumar, Mihir Mody, Mahesh Mehendale, et al. 2015. "Accelerating H.264/HEVC Video Slice Processing Using Application Specific Instruction Set Processor." In *2015 IEEE International Conference on Consumer Electronics (ICCE)*. IEEE. [https://doi.org/10.1109/icce.2015.7066465][research_mandal_2015]
- Manglaviti, Marco, Eduardo Coronado-Montoya, Keheliya Gallaba, and Shane McIntosh. 2017. "An Empirical Study of the Personnel Overhead of Continuous Integration." In *2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2017.31][research_manglaviti_2017]
- Mao, Jiacheng, Zukai Tang, and Wenbi Rao. 2023. "Cross-Language Binary-Source Code Matching Based on Rust and Intermediate Representation." In *2023 IEEE 3rd International Conference on Computer Communication and Artificial Intelligence (CCAI)*. IEEE. [https://doi.org/10.1109/ccai57533.2023.10201266][research_mao_2023]
- Marbukh, Vladimir. 2022. "Poster Abstract: Towards Shapley Value Based Security Risk Attribution in Sensor Networks." In *2022 21st ACM/IEEE International Conference on Information Processing in Sensor Networks (IPSN)*. IEEE. [https://doi.org/10.1109/ipsn54338.2022.00060][research_marbukh_2022]
- Marcelli, Andrea, Abdallah Cheikh, Marcello Barbirotta, Antonio Mastrandrea, Francesco Menichelli, and Mauro Olivieri. 2025. "Eight-Bit Vector SoftFloat Extension for the RISC-V Spike Simulator." *Electronics* 14 (19): 3924. [https://doi.org/10.3390/electronics14193924][research_marcelli_2025]
- Marchetto, Alessandro, Giuseppe Scanniello, and Angelo Susi. 2019. "Combining Code and Requirements Coverage with Execution Cost for Test Suite Reduction." *IEEE Transactions on Software Engineering* 45 (4): 363–90. [https://doi.org/10.1109/tse.2017.2777831][research_marchetto_2019]
- Marijan, Dusica. 2023. "Comparative Study of Machine Learning Test Case Prioritization for Continuous Integration Testing." *Software Quality Journal* 31 (4): 1415–38. [https://doi.org/10.1007/s11219-023-09646-0][research_marijan_2023]
- Maron, L., and D. Macko. 2016. "Automated Formal Verification of the Refined Specification of Digital Systems in HSSL." In *2016 International Conference on Emerging eLearning Technologies and Applications (ICETA)*. IEEE. [https://doi.org/10.1109/iceta.2016.7802074][research_maron_2016]
- Martins, Antonio, Cristiano Melo, José Monteiro, and Javam Machado. 2020. "Empirical Study about Class Change Proneness Prediction Using Software Metrics and Code Smells." In *Proceedings of the 22nd International Conference on Enterprise Information Systems*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0009410601400147][research_martins_2020]
- Martins, Luana, Valeria Pontillo, Heitor Costa, Filomena Ferrucci, Fabio Palomba, and Ivan Machado. 2024. "Test Code Refactoring Unveiled: Where and How Does It Affect Test Code Quality and Effectiveness?" *Empirical Software Engineering* 30 (1): 27. [https://doi.org/10.1007/s10664-024-10577-y][research_martins_2024]
- Mashchenko, S. O., and V. I. Morenets. 2017. "Shapley Value of a Cooperative Game with Fuzzy Set of Feasible Coalitions." *Cybernetics and Systems Analysis* 53 (3): 432–40. [https://doi.org/10.1007/s10559-017-9944-4][research_mashchenko_2017]
- Massidda, Emmanuele, Lorenzo Pisu, Davide Maiorca, and Giorgio Giacinto. 2024. "Bringing Binary Exploitation at Port 80: Understanding C Vulnerabilities in WebAssembly." In *Proceedings of the 21st International Conference on Security and Cryptography*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0012852400003767][research_massidda_2024]
- Masten, Matt, Evgeniy Tyurin, Konstantina Mitropoulou, Eric Garcia, and Hideki Saito. 2018. "Function/Kernel Vectorization via Loop Vectorizer." In *2018 IEEE/ACM 5th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2018.8639483][research_masten_2018]
- Mastroeni, Isabella, and Michele Pasqua. 2017. "Hyperhierarchy of Semantics: A Formal Framework for Hyperproperties Verification." In *Static Analysis*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-66706-5\_12][research_mastroeni_2017]
- Matsubara, Katsuya, Yuzuki Saito, Daigo Fujii, and Yuki Nakata. 2025. "Seamless Self-Healing in WebAssembly Container Orchestration with Runtime-Neutral Checkpointing." In *2025 Thirteenth International Symposium on Computing and Networking Workshops (CANDARW)*. IEEE. [https://doi.org/10.1109/candarw68385.2025.00013][research_matsubara_2025]
- Matsubara, Patrícia G. F., Igor Steinmacher, Bruno Gadelha, and Tayana Conte. 2023. "Much More than a Prediction: Expert-Based Software Effort Estimation as a Behavioral Act." *Empirical Software Engineering* 28 (4): 98. [https://doi.org/10.1007/s10664-023-10332-9][research_matsubara_2023]
- Mazurek, Przemyslaw. 2020. "BOSON: Application-Specific Instruction Set Processor (ASIP) for Educational Purposes." In *2020 16th International Conference on Control, Automation, Robotics and Vision (ICARCV)*. IEEE. [https://doi.org/10.1109/icarcv50220.2020.9305396][research_mazurek_2020]
- McMillan, Kenneth. 2016. "Modular Specification and Verification of a Cache-Coherent Interface." In *2016 Formal Methods in Computer-Aided Design (FMCAD)*. IEEE. [https://doi.org/10.1109/fmcad.2016.7886668][research_mcmillan_2016]
- Mehta, Bhavik. 2023. "Formalising Sharkovsky’s Theorem (Proof Pearl)." In *Proceedings of the 12th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3573105.3575689][research_mehta_2023]
- Melo, Cecil Accetti R. A., and Edna Barros. 2016. "Oolong: A Baseband Processor Extension to the RISC-V ISA." In *2016 IEEE 27th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap.2016.7760808][research_melo_2016]
- Melquiond, Guillaume, and Josué Moreau. 2024. "A Safe Low-Level Language for Computer Algebra and Its Formally Verified Compiler." *Proceedings of the ACM on Programming Languages* 8 (ICFP): 121–46. [https://doi.org/10.1145/3674629][research_melquiond_2024]
- Menendez, David, and Santosh Nagarakatte. 2017. "Alive-Infer: Data-Driven Precondition Inference for Peephole Optimizations in LLVM." *ACM SIGPLAN Notices* 52 (6): 49–63. [https://doi.org/10.1145/3140587.3062372][research_menendez_2017]
- Menendez, David, Santosh Nagarakatte, and Aarti Gupta. 2016. "Alive-FP: Automated Verification of Floating Point Based Peephole Optimizations in LLVM." In *Static Analysis*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-662-53413-7\_16][research_menendez_2016]
- Menetrey, James, Marcelo Pasin, Pascal Felber, and Valerio Schiavoni. 2021. "Twine: An Embedded Trusted Runtime for WebAssembly." In *2021 IEEE 37th International Conference on Data Engineering (ICDE)*. IEEE. [https://doi.org/10.1109/icde51399.2021.00025][research_menetrey_2021]
- Menetrey, James, Marcelo Pasin, Pascal Felber, and Valerio Schiavoni. 2022. "WaTZ: A Trusted WebAssembly Runtime Environment with Remote Attestation for TrustZone." In *2022 IEEE 42nd International Conference on Distributed Computing Systems (ICDCS)*. IEEE. [https://doi.org/10.1109/icdcs54860.2022.00116][research_menetrey_2022]
- Ménétrey, Jämes, Marcelo Pasin, Pascal Felber, et al. 2024. "A Comprehensive Trusted Runtime for WebAssembly with Intel SGX." *IEEE Transactions on Dependable and Secure Computing* 21 (4): 3562–79. [https://doi.org/10.1109/tdsc.2023.3334516][research_menetrey_2024]
- Meng, Fanqi, Haochen Sun, and Jingdong Wang. 2020. "Survey on Estimation and Optimization of Worst-Case Execution Time with Energy Consumption Constraint." In *2020 12th International Conference on Computational Intelligence and Communication Networks (CICN)*. IEEE. [https://doi.org/10.1109/cicn49253.2020.9242624][research_meng_2020]
- Menolli, André, Luan Melo, Maurício Arimoto, and Andreia Malucelli. 2021. "An Empirical Study on the Impact of Aspect-Oriented Model-Driven Code Generation." In *Proceedings of the 23rd International Conference on Enterprise Information Systems*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0010442802750282][research_menolli_2021]
- Mensah, Solomon, Jacky Keung, Jeffery Svajlenko, Kwabena Ebo Bennin, and Qing Mi. 2018. "On the Value of a Prioritization Scheme for Resolving Self-Admitted Technical Debt." *Journal of Systems and Software* 135: 37–54. [https://doi.org/10.1016/j.jss.2017.09.026][research_mensah_2018]
- Menzies, Tim, Ye Yang, George Mathew, Barry Boehm, and Jairus Hihn. 2016. "Negative Results for Software Effort Estimation." *Empirical Software Engineering* 22 (5): 2658–83. [https://doi.org/10.1007/s10664-016-9472-2][research_menzies_2016]
- Meywerk, Tim, Vladimir Herdt, and Rolf Drechsler. 2023. "Coverage-Guided Fuzzing for Plan-Based Robotics." In *Proceedings of the 15th International Conference on Agents and Artificial Intelligence*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0011630600003393][research_meywerk_2023]
- Mezouar, Mariam El, Feng Zhang, and Ying Zou. 2017. "Are Tweets Useful in the Bug Fixing Process? An Empirical Study on Firefox and Chrome." *Empirical Software Engineering* 23 (3): 1704–42. [https://doi.org/10.1007/s10664-017-9559-4][research_mezouar_2017]
- Mguidich, Achraf, Vladimir-Alexandru Paun, Bruno Monsuez, and Philippe Baufreton. 2016. "Time-Accurate ASM as a Refinement Scheme for Worst-Case Execution Time Estimation in Hard Real-Time Systems." In *2016 IEEE Real-Time Systems Symposium (RTSS)*. IEEE. [https://doi.org/10.1109/rtss.2016.051][research_mguidich_2016]
- Mi, Qing, Jacky Keung, Yuqi Huo, and Solomon Mensah. 2018. "Not All Bug Reopens Are Negative: A Case Study on Eclipse Bug Reports." *Information and Software Technology* 99: 93–97. [https://doi.org/10.1016/j.infsof.2018.03.006][research_mi_2018]
- Mills, Chris, Esteban Parra, Jevgenija Pantiuchina, Gabriele Bavota, and Sonia Haiduc. 2020. "On the Relationship between Bug Reports and Queries for Text Retrieval-Based Bug Localization." *Empirical Software Engineering* 25 (5): 3086–3127. [https://doi.org/10.1007/s10664-020-09823-w][research_mills_2020]
- Minku, Leandro L. 2019. "A Novel Online Supervised Hyperparameter Tuning Procedure Applied to Cross-Company Software Effort Estimation." *Empirical Software Engineering* 24 (5): 3153–3204. [https://doi.org/10.1007/s10664-019-09686-w][research_minku_2019]
- Mirzaei, Hajar, and Mohammad Reza Keyvanpour. 2022. "Reinforcement Learning Reward Function for Test Case Prioritization in Continuous Integration." In *2022 9th Iranian Joint Congress on Fuzzy and Intelligent Systems (CFIS)*. IEEE. [https://doi.org/10.1109/cfis54774.2022.9756464][research_mirzaei_2022]
- Mishra, Ashish, and Suresh Jagannathan. 2022. "Specification-Guided Component-Based Synthesis from Effectful Libraries." *Proceedings of the ACM on Programming Languages* 6 (OOPSLA2): 616–45. [https://doi.org/10.1145/3563310][research_mishra_2022]
- Mitsch, Stefan, and André Platzer. 2016. "ModelPlex: Verified Runtime Validation of Verified Cyber-Physical System Models." *Formal Methods in System Design* 49 (1–2): 33–74. [https://doi.org/10.1007/s10703-016-0241-z][research_mitsch_2016]
- Mochizuki, Fumika, Tetsuro Yamazaki, and Shigeru Chiba. 2024. "Interactive Programming for Microcontrollers by Offloading Dynamic Incremental Compilation." In *Proceedings of the 21st ACM SIGPLAN International Conference on Managed Programming Languages and Runtimes*. ACM. [https://doi.org/10.1145/3679007.3685062][research_mochizuki_2024]
- Moldovan, Vasilica. 2026. "Benchmarking Cross-Language Code Smell Detection with Pretrained and Large Language Models." In *Proceedings of the 21st International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014803700004015][research_moldovan_2026]
- Molnar, Arthur-Jozsef, and Simona Motogna. 2022. "Characterizing Technical Debt in Evolving Open-Source Software." In *Proceedings of the 17th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0011073600003176][research_molnar_2022]
- Mondal, Debajyoti, Hadi Hemmati, and Stephane Durocher. 2015. "Exploring Test Suite Diversification and Code Coverage in Multi-Objective Test Case Selection." In *2015 IEEE 8th International Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst.2015.7102588][research_mondal_2015]
- Mondal, Saikat, Mohammad Masudur Rahman, Chanchal K. Roy, and Kevin Schneider. 2022. "The Reproducibility of Programming-Related Issues in Stack Overflow Questions." *Empirical Software Engineering* 27 (3): 62. [https://doi.org/10.1007/s10664-021-10113-2][research_mondal_2022]
- Mondal, Manishankar, Chanchal K. Roy, and Kevin A. Schneider. 2017. "Bug Propagation through Code Cloning: An Empirical Study." In *2017 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme.2017.33][research_mondal_2017]
- Monica Catherine S, and Geogen George. 2015. "S-Compiler: A Code Vulnerability Detection Method." In *2015 International Conference on Electrical, Electronics, Signals, Communication and Optimization (EESCO)*. IEEE. [https://doi.org/10.1109/eesco.2015.7254018][research_monicacatherin_2015]
- Monniaux, David. 2024. "Memory Simulations, Security and Optimization in a Verified Compiler." In *Proceedings of the 13th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3636501.3636952][research_monniaux_2024]
- Monniaux, David, and Sylvain Boulmé. 2022. "The Trusted Computing Base of the CompCert Verified Compiler." In *Programming Languages and Systems*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-99336-8\_8][research_monniaux_2022]
- Moore, Jessica, Ben Gelman, and David Slater. 2019. "A Convolutional Neural Network for Language-Agnostic Source Code Summarization." In *Proceedings of the 14th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0007678100150026][research_moore_2019]
- Mori, Ryusei, and Masaki Nakamura. 2017. "Automated Test Case Generation from OTS/CafeOBJ Specifications by Specification Translation." In *2017 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw.2017.78][research_mori_2017]
- Moriconi, Florent, Thomas Durieux, Jean-Rémy Falleri, Raphaël Troncy, and Aurélien Francillon. 2025. "GHALogs: Large-Scale Dataset of GitHub Actions Runs." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00104][research_moriconi_2025]
- Moron, Konrad, and Stefan Wallentowitz. 2023. "Support for Just-in-Time Compilation of WebAssembly for Embedded Systems." In *2023 12th Mediterranean Conference on Embedded Computing (MECO)*. IEEE. [https://doi.org/10.1109/meco58584.2023.10155088][research_moron_2023]
- Morovati, Mohammad Mehdi, Amin Nikanjam, Florian Tambon, Foutse Khomh, and Zhen Ming Jiang. 2023. "Bug Characterization in Machine Learning-Based Systems." *Empirical Software Engineering* 29 (1): 14. [https://doi.org/10.1007/s10664-023-10400-0][research_morovati_2023]
- Mosin, Sergey. 2015. "Test Program Generation for Mixed-Signal Integrated Circuits Based on Automata Network." In *2015 IEEE East-West Design & Test Symposium (EWDTS)*. IEEE. [https://doi.org/10.1109/ewdts.2015.7493152][research_mosin_2015]
- Moss, Nick, Kei Davis, and Patrick McCormick. 2016. "The ARES High-Level Intermediate Representation." In *2016 Third Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2016.009][research_moss_2016]
- Moussa, Sali. 2025. "Testing Autonomous Driving Systems through Blind-Spot Guided Fuzzing." In *2025 40th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase63991.2025.00396][research_moussa_2025]
- Mu, Wenlong, Yilei Zhang, Bo Huang, Jianmei Guo, and Shiqiang Cui. 2023. "A Hotspot-Driven Semi-Automated Competitive Analysis Framework for Identifying Compiler Key Optimizations." In *Proceedings of the 32nd ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3578360.3580255][research_mu_2023]
- Mukherjee, Manasij, Pranav Kant, Zhengyang Liu, and John Regehr. 2020. "Dataflow-Based Pruning for Speeding up Superoptimization." *Proceedings of the ACM on Programming Languages* 4 (OOPSLA): 1–24. [https://doi.org/10.1145/3428245][research_mukherjee_2020]
- Mullen, Eric, Daryl Zuniga, Zachary Tatlock, and Dan Grossman. 2016. "Verified Peephole Optimizations for CompCert." *ACM SIGPLAN Notices* 51 (6): 448–61. [https://doi.org/10.1145/2980983.2908109][research_mullen_2016]
- Müller, Kilian, Siddharth Mane, Peter Wägemann, and Norman Franchi. 2026. "WasmWeaver: A Framework for Runtime-Aware WebAssembly Program Generation with Reinforcement Learning." In *2026 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner67736.2026.00045][research_muller_2026]
- Munafò, Marcus R., Brian A. Nosek, Dorothy V. M. Bishop, et al. 2017. "A Manifesto for Reproducible Science." *Nature Human Behaviour* 1 (1): 0021. [https://doi.org/10.1038/s41562-016-0021][research_munafo_2017]
- Munezero, Sonia, Nicasio Maguu Muchuka, and Peter Kamita Kihato. 2026. "A Time-Predictable Multicore RISC-V Architecture for Real-Time AI Workloads." In *2026 9th International Conference on Circuits, Systems and Simulation (ICCSS)*. IEEE. [https://doi.org/10.1109/iccss69952.2026.11593309][research_munezero_2026]
- Musco, Vincenzo, Martin Monperrus, and Philippe Preux. 2016. "A Large-Scale Study of Call Graph-Based Impact Prediction Using Mutation Testing." *Software Quality Journal* 25 (3): 921–50. [https://doi.org/10.1007/s11219-016-9332-8][research_musco_2016]
- Muse, Biruk Asmare, Csaba Nagy, Anthony Cleve, Foutse Khomh, and Giuliano Antoniol. 2022. "FIXME: Synchronize with Database! An Empirical Study of Data Access Self-Admitted Technical Debt." *Empirical Software Engineering* 27 (6): 130. [https://doi.org/10.1007/s10664-022-10119-4][research_muse_2022]
- Mushtaq, Hamid, Zaid Al-Ars, and Koen Bertels. 2015. "Calculation of Worst-Case Execution Time for Multicore Processors Using Deterministic Execution." In *2015 25th International Workshop on Power and Timing Modeling, Optimization and Simulation (PATMOS)*. IEEE. [https://doi.org/10.1109/patmos.2015.7347584][research_mushtaq_2015]
- Myreen, Magnus O. 2021. "A Minimalistic Verified Bootstrapped Compiler (Proof Pearl)." In *Proceedings of the 10th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3437992.3439915][research_myreen_2021]
- Mytkowicz, Todd, Amer Diwan, Matthias Hauswirth, and Peter F. Sweeney. 2009. "Producing Wrong Data without Doing Anything Obviously Wrong!" *ACM SIGPLAN Notices* 44 (3): 265–76. [https://doi.org/10.1145/1508284.1508275][research_mytkowicz_2009]
- Mzid, Rania, Asma Charfi, and Najmeddine Etteyeb. 2022. "Use of Compiler Intermediate Representation for Reverse Engineering: A Case Study for GCC Compiler and UML Activity Diagram." In *Proceedings of the 10th International Conference on Model-Driven Engineering and Software Development*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0010821700003119][research_mzid_2022]
- Nadimi, Bardia, and Hao Zheng. 2024. "A Multi-Expert Large Language Model Architecture for Verilog Code Generation." In *2024 IEEE LLM Aided Design Workshop (LAD)*. IEEE. [https://doi.org/10.1109/lad62341.2024.10691683][research_nadimi_2024]
- Nagy, Stefan, and Matthew Hicks. 2019. "Full-Speed Fuzzing: Reducing Fuzzing Overhead through Coverage-Guided Tracing." In *2019 IEEE Symposium on Security and Privacy (SP)*. IEEE. [https://doi.org/10.1109/sp.2019.00069][research_nagy_2019]
- Nakamura, Kazuhiro, and Nagisa Ishiura. 2016. "Random Testing of C Compilers Based on Test Program Generation by Equivalence Transformation." In *2016 IEEE Asia Pacific Conference on Circuits and Systems (APCCAS)*. IEEE. [https://doi.org/10.1109/apccas.2016.7804063][research_nakamura_2016]
- Namjoshi, Kedar S., and Anton Xue. 2021. "A Self-Certifying Compilation Framework for WebAssembly." In *Verification, Model Checking, and Abstract Interpretation*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-67067-2\_7][research_namjoshi_2021]
- Nannipieri, Pietro, Stefano Di Matteo, Luca Zulberti, Francesco Albicocchi, Sergio Saponara, and Luca Fanucci. 2021. "A RISC-V Post Quantum Cryptography Instruction Set Extension for Number Theoretic Transform to Speed-Up CRYSTALS Algorithms." *IEEE Access* 9: 150798–150808. [https://doi.org/10.1109/access.2021.3126208][research_nannipieri_2021]
- Nasui, Andreea, Andreea Vescan, and Cristina Marinescu. 2026. "An Empirical Comparison of Human and LLM-Assisted Bug Priority Assignment." In *Proceedings of the 21st International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014936200004015][research_nasui_2026]
- Naufal Maulana, Moh. Zulfiqar, and Daniel Siahaan. 2022. "Use Case-Based Analytical Hierarchy Process Method for Software Requirements Prioritization." In *2022 6th International Conference on Information Technology, Information Systems and Electrical Engineering (ICITISEE)*. IEEE. [https://doi.org/10.1109/icitisee57756.2022.10057944][research_naufalmaulana_2022]
- Ndlovu, Siqabukile, and Ernest Mnkandla. 2024. "A Preliminary Framework for Optimising Test Case Selection Using Natural Language Processing and Test Case Prioritisation Using Deep Learning in Continuous Integration." In *2024 3rd Zimbabwe Conference of Information and Communication Technologies (ZCICT)*. IEEE. [https://doi.org/10.1109/zcict63770.2024.10958234][research_ndlovu_2024]
- Necula, George C. 1997. "Proof-Carrying Code." In *Proceedings of the 24th ACM SIGPLAN-SIGACT symposium on Principles of programming languages - POPL '97*. ACM Press. [https://doi.org/10.1145/263699.263712][research_necula_1997]
- Necula, George C., and Peter Lee. 1998. "The Design and Implementation of a Certifying Compiler." In *Proceedings of the ACM SIGPLAN 1998 conference on Programming language design and implementation*. ACM. [https://doi.org/10.1145/277650.277752][research_necula_lee_1998]
- Neis, Georg, Chung-Kil Hur, Jan-Oliver Kaiser, Craig McLaughlin, Derek Dreyer, and Viktor Vafeiadis. 2015. "Pilsner: A Compositionally Verified Compiler for a Higher-Order Imperative Language." *ACM SIGPLAN Notices* 50 (9): 166–78. [https://doi.org/10.1145/2858949.2784764][research_neis_2015]
- Nemhauser, G. L., L. A. Wolsey, and M. L. Fisher. 1978. "An Analysis of Approximations for Maximizing Submodular Set Functions—I." *Mathematical Programming* 14 (1): 265–94. [https://doi.org/10.1007/bf01588971][research_nemhauser_1978]
- Nery, Alexandre S., Nadia Nedjah, Felipe M. G. França, Lech Jóźwiak, and Henk Corporaal. 2015. "Automatic Complex Instruction Identification for Efficient Application Mapping onto Application-Specific Instruction Set Processors." *Analog Integrated Circuits and Signal Processing* 85 (1): 139–58. [https://doi.org/10.1007/s10470-015-0585-0][research_nery_2015]
- Neumüller, Denis, Sebastian Boll, David Schüler, and Matthias Tichy. 2026. "Combining Static Code Analysis and Large Language Models Improves Correctness and Performance of Algorithm Recognition." In *2026 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner67736.2026.00068][research_neumuller_2026]
- Nezamabadi, Daniel, Magnus O. Myreen, and Yong Kiam Tan. 2026. "Verified VCG and Verified Compiler for Dafny." In *Proceedings of the 15th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3779031.3779092][research_nezamabadi_2026]
- Nguyen, Anh Tuan, and Tien N. Nguyen. 2015. "Graph-Based Statistical Language Model for Code." In *2015 IEEE/ACM 37th IEEE International Conference on Software Engineering*. IEEE. [https://doi.org/10.1109/icse.2015.336][research_nguyen_2015]
- Nguyen, Son, Tien Nguyen, Yi Li, and Shaohua Wang. 2019. "Combining Program Analysis and Statistical Language Model for Code Statement Completion." In *2019 34th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase.2019.00072][research_nguyen_2019]
- Nguyen, Van Man, Emmanuelle Saillard, Julien Jaeger, Denis Barthou, and Patrick Carribault. 2020. "PARCOACH Extension for Static MPI Nonblocking and Persistent Communication Validation." In *2020 IEEE/ACM 4th International Workshop on Software Correctness for HPC Applications (Correctness)*. IEEE. [https://doi.org/10.1109/correctness51934.2020.00009][research_nguyen_2020]
- Nguyen, Tan, Erich Strohmaier, and John Shalf. 2021. "Facilitating CoDesign with Automatic Code Similarity Learning." In *2021 IEEE/ACM 7th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvmhpc54804.2021.00011][research_nguyen_2021]
- Ni, Yunbo. 2025. "LegoFuzz: Interleaving Large Language Models for Compiler Testing." In *Companion Proceedings of the 2025 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity*. ACM. [https://doi.org/10.1145/3758316.3763251][research_ni_2025_b]
- Ni, Yunbo, and Shaohua Li. 2025. "Interleaving Large Language Models for Compiler Testing." *Proceedings of the ACM on Programming Languages* 9 (OOPSLA2): 815–41. [https://doi.org/10.1145/3763079][research_ni_2025]
- Nielebock, Sebastian, Paul Blockhaus, Jacob Krüger, and Frank Ortmeier. 2021. "AndroidCompass: A Dataset of Android Compatibility Checks in Code Repositories." In *2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr52588.2021.00069][research_nielebock_2021]
- Ņikiforova, Oksana, Vitaly Zabiniako, Jurijs Kornienko, Pāvels Garkalns, Ruslan Rizhko, and Madara Gasparoviča-Asīte. 2022. "Solution to CAD Designer Effort Estimation Based on Analogy with Software Development Metrics." In *Proceedings of the 17th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0011032700003176][research_nikiforova_2022]
- Nikith, Boda Venkata, Shaik Reeha, G. Mani Prakash Reddy, and Meena Belwal. 2024. "An Experimental Analysis of RL Based Compiler Optimization Techniques Using Compiler GYM." In *2024 IEEE 9th International Conference for Convergence in Technology (I2CT)*. IEEE. [https://doi.org/10.1109/i2ct61223.2024.10543642][research_nikith_2024]
- Nipkow, Tobias, and Thomas Sewell. 2020. "Proof Pearl: Braun Trees." In *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3372885.3373834][research_nipkow_2020]
- Niu, Feifei, Enshuo Zhang, Christoph Mayr-Dorn, et al. 2024. "An Extensive Replication Study of the ABLoTS Approach for Bug Localization." *Empirical Software Engineering* 29 (6): 143. [https://doi.org/10.1007/s10664-024-10537-6][research_niu_2024]
- Noack, Matthias, Florian Wende, Georg Zitzlsberger, Michael Klemm, and Thomas Steinke. 2017. "KART – a Runtime Compilation Library for Improving HPC Application Performance." In *High Performance Computing*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-67630-2\_29][research_noack_2017]
- Nobre, Ricardo, João Bispo, Tiago Carvalho, and João M. P. Cardoso. 2019. "Nonio — Modular Automatic Compiler Phase Selection and Ordering Specialization Framework for Modern Compilers." *SoftwareX* 10: 100238. [https://doi.org/10.1016/j.softx.2019.100238][research_nobre_2019]
- Nobre, Ricardo, Luiz G. A. Martins, and João M. P. Cardoso. 2016. "A Graph-Based Iterative Compiler Pass Selection and Phase Ordering Approach." *ACM SIGPLAN Notices* 51 (5): 21–30. [https://doi.org/10.1145/2980930.2907959][research_nobre_2016]
- Nogueira, Rodrigo Pato, Marco Vieira, and João R. Campos. 2025. "Beyond Functional Correctness: An Empirical Evaluation of Large Language Models for Text-to-Code Generation." In *2025 IEEE 36th International Symposium on Software Reliability Engineering (ISSRE)*. IEEE. [https://doi.org/10.1109/issre66568.2025.00036][research_nogueira_2025]
- Nolasco, Agustín. 2026. "Automated Inference of Expressive Metamorphic Relations for Effective Metamorphic Testing." In *2026 IEEE International Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst69053.2026.00016][research_nolasco_2026]
- Nong, Qing-Qin, Yue Wang, and Su-Ning Gong. 2024. "A Semi-Streaming Algorithm for Monotone Regularized Submodular Maximization with a Matroid Constraint." *Journal of the Operations Research Society of China* 14 (1): 162–78. [https://doi.org/10.1007/s40305-023-00525-w][research_nong_2024]
- Nötzli, Andres, and Fraser Brown. 2016. "LifeJacket: Verifying Precise Floating-Point Optimizations in LLVM." In *Proceedings of the 5th ACM SIGPLAN International Workshop on State Of the Art in Program Analysis*. ACM. [https://doi.org/10.1145/2931021.2931024][research_notzli_2016]
- Novielli, Nicole, Fabio Calefato, Filippo Lanubile, and Alexander Serebrenik. 2021. "Assessment of off-the-Shelf SE-Specific Sentiment Analysis Tools: An Extended Replication Study." *Empirical Software Engineering* 26 (4): 77. [https://doi.org/10.1007/s10664-021-09960-w][research_novielli_2021]
- Nunes, Willian Analdo, Antônio Vinicius Corrêa dos Santos, Lucas Damo, and Fernando Gehm Moraes. 2026. "Design Space Exploration of RISC-V Vector Extension Targeting Embedded Processors." *IEEE Transactions on Computers* 75 (8): 2986–3000. [https://doi.org/10.1109/tc.2026.3700461][research_nunes_2026]
- Nunes, Willian Analdo, Antônio Vinicius Corrêa Dos Santos, César Marcon, and Fernando Gehm Moraes. 2025a. "Accelerating Machine Learning Using RISC-V Vector Extension in a Manycore Platform." In *2025 IFIP/IEEE 33rd International Conference on Very Large Scale Integration (VLSI-SoC)*. IEEE. [https://doi.org/10.1109/vlsi-soc64688.2025.11421728][research_nunes_2025]
- Nunes, Willian Analdo, Antônio Vinicius Corrêa Dos Santos, and Fernando Gehm Moraes. 2025b. "Accelerating Machine Learning with RISC-V Vector Extension and Auto-Vectorization Techniques." In *2025 IEEE International Symposium on Circuits and Systems (ISCAS)*. IEEE. [https://doi.org/10.1109/iscas56072.2025.11043225][research_nunes_2025_b]
- Ochoa, Lina, Thomas Degueule, Jean-Rémy Falleri, and Jurgen Vinju. 2022. "Breaking Bad? Semantic Versioning and Impact of Breaking Changes in Maven Central: An External and Differentiated Replication Study." *Empirical Software Engineering* 27 (3): 61. [https://doi.org/10.1007/s10664-021-10052-y][research_ochoa_2022]
- Oh, Hyun Woo, and Seung Eun Lee. 2023. "The Design of Optimized RISC Processor for Edge Artificial Intelligence Based on Custom Instruction Set Extension." *IEEE Access* 11: 49409–21. [https://doi.org/10.1109/access.2023.3276411][research_oh_2023]
- Ojdanic, Milos, Aayush Garg, Ahmed Khanfir, Renzo Degiovanni, Mike Papadakis, and Yves Le Traon. 2023. "Syntactic versus Semantic Similarity of Artificial and Real Faults in Mutation Testing Studies." *IEEE Transactions on Software Engineering* 49 (7): 3922–38. [https://doi.org/10.1109/tse.2023.3277564][research_ojdanic_2023]
- Okawara, Manato, Kanemitsu Ootsu, Takuma Kitamoto, and Takashi Yokota. 2025. "Performance Evaluation of CNN Using RISC-V Vector Extension for Embedded System." In *2025 Thirteenth International Symposium on Computing and Networking Workshops (CANDARW)*. IEEE. [https://doi.org/10.1109/candarw68385.2025.00065][research_okawara_2025]
- Oliveira, Wendell, Filipe Paiva, Thiago Emmanuel Pereira, and João Brunet. 2025. "A Defect Taxonomy for Infrastructure as Code: A Replication Study." In *2025 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem64174.2025.00073][research_oliveira_2025]
- Oliveira Neto, Francisco G. de, Richard Torkar, and Patricia D. L. Machado. 2015. "An Initiative to Improve Reproducibility and Empirical Evaluation of Software Testing Techniques." In *2015 IEEE/ACM 37th IEEE International Conference on Software Engineering*. IEEE. [https://doi.org/10.1109/icse.2015.197][research_oliveiraneto_2015]
- Olsson, Jesper, Erik Risfelt, Terese Besker, Antonio Martini, and Richard Torkar. 2021. "Measuring Affective States from Technical Debt: A Psychoempirical Software Engineering Experiment." *Empirical Software Engineering* 26 (5): 105. [https://doi.org/10.1007/s10664-021-09998-w][research_olsson_2021]
- Örgård, Jonathan, Gregory Gay, Francisco Gomes de Oliveira Neto, and Kim Viggedal. 2023. "Mutation Testing in Continuous Integration: An Exploratory Industrial Case Study." In *2023 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw58534.2023.00063][research_orgard_2023]
- Oskin, Mark, and Gabriel H. Loh. 2015. "A Software-Managed Approach to Die-Stacked DRAM." In *2015 International Conference on Parallel Architecture and Compilation (PACT)*. IEEE. [https://doi.org/10.1109/pact.2015.30][research_oskin_2015]
- Ostrand, T. J., E. J. Weyuker, and R. M. Bell. 2005. "Predicting the Location and Number of Faults in Large Software Systems." *IEEE Transactions on Software Engineering* 31 (4): 340–55. [https://doi.org/10.1109/tse.2005.49][research_ostrand_weyuker_2005]
- Ottoni, Guilherme. 2018. "HHVM JIT: A Profile-Guided, Region-Based Compiler for PHP and Hack." In *Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3192366.3192374][research_ottoni_2018]
- Ozdemir, Alex, Fraser Brown, and Riad S. Wahby. 2022. "CirC: Compiler Infrastructure for Proof Systems, Software Verification, and More." In *2022 IEEE Symposium on Security and Privacy (SP)*. IEEE. [https://doi.org/10.1109/sp46214.2022.9833782][research_ozdemir_2022]
- Ozen, Guray, Simone Atzeni, Michael Wolfe, Annemarie Southwell, and Gary Klimowicz. 2018. "OpenMP GPU Offload in Flang and LLVM." In *2018 IEEE/ACM 5th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2018.8639434][research_ozen_2018]
- Palomba, Fabio, and Andy Zaidman. 2019. "RETRACTED ARTICLE: The Smell of Fear: On the Relation between Test Smells and Flaky Tests." *Empirical Software Engineering* 24 (5): 2907–46. [https://doi.org/10.1007/s10664-019-09683-z][research_palomba_2019]
- Palomba, Fabio, and Andy Zaidman. 2020. "Retraction Note: Retraction Note To: The Smell of Fear: On the Relation between Test Smells and Flaky Tests." *Empirical Software Engineering* 25 (4): 3041–3041. [https://doi.org/10.1007/s10664-020-09821-y][research_palomba_2020]
- Pan, Rongqi, Mojtaba Bagherzadeh, Taher A. Ghaleb, and Lionel Briand. 2021. "Test Case Selection and Prioritization Using Machine Learning: A Systematic Literature Review." *Empirical Software Engineering* 27 (2): 29. [https://doi.org/10.1007/s10664-021-10066-6][research_pan_2021]
- Pandey, Lal Bahadur, Manisha Sharma, Rajesh Tiwari, Radhe Shyam Panda, and Partha Roy. 2024. "A Survey of Optimized Compiler Using Advanced Machine Learning and Deep Learning Techniques." In *2024 IEEE 6th International Conference on Cybernetics, Cognition and Machine Learning Applications (ICCCMLA)*. IEEE. [https://doi.org/10.1109/icccmla63077.2024.10871813][research_pandey_2024]
- Pang, Yalong, Jun Han, Jianmin Zeng, Yujie Huang, and Xiaoyang Zeng. 2017. "Instruction Set Extension and Hardware Acceleration for SVM Application toward a Vector Processor." In *2017 International SoC Design Conference (ISOCC)*. IEEE. [https://doi.org/10.1109/isocc.2017.8368818][research_pang_2017]
- Panigrahi, Priyanka, and Chandan Karfa. 2023. "Translation Validation of Information Leakage of Compiler Optimizations." *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems* 42 (11): 3585–98. [https://doi.org/10.1109/tcad.2023.3269954][research_panigrahi_2023]
- Papadimitriou, Michail, Juan Fumero, Athanasios Stratikopoulos, and Christos Kotselidis. 2021. "Automatically Exploiting the Memory Hierarchy of GPUs through Just-in-Time Compilation." In *Proceedings of the 17th ACM SIGPLAN/SIGOPS International Conference on Virtual Execution Environments*. ACM. [https://doi.org/10.1145/3453933.3454014][research_papadimitriou_2021]
- Papoudakis, Argyrios, Thomas Karanikiotis, and Andreas Symeonidis. 2022. "A Mechanism for Automatically Extracting Reusable and Maintainable Code Idioms from Software Repositories." In *Proceedings of the 17th International Conference on Software Technologies*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0011279300003266][research_papoudakis_2022]
- Parihar, Raj, and Michael C. Huang. 2015. "Load Balancing in Decoupled Look-Ahead: A Do-It-Yourself (DIY) Approach." In *2015 International Conference on Parallel Architecture and Compilation (PACT)*. IEEE. [https://doi.org/10.1109/pact.2015.55][research_parihar_2015]
- Parihar, Raj, and Michael C. Huang. 2017. "DRUT: An Efficient Turbo Boost Solution via Load Balancing in Decoupled Look-Ahead Architecture." In *2017 26th International Conference on Parallel Architectures and Compilation Techniques (PACT)*. IEEE. [https://doi.org/10.1109/pact.2017.35][research_parihar_2017]
- Park, Hyukwoo, Wonki Jung, and Soo-Mook Moon. 2015. "Javascript Ahead-of-Time Compilation for Embedded Web Platform." In *2015 13th IEEE Symposium on Embedded Systems For Real-time Multimedia (ESTIMedia)*. IEEE. [https://doi.org/10.1109/estimedia.2015.7351768][research_park_2015]
- Park, Seonghwan, Dongwook Kang, Jeonghwan Kang, and Donghyun Kwon. 2022a. "Bratter: An Instruction Set Extension for Forward Control-Flow Integrity in RISC-V." *Sensors* 22 (4): 1392. [https://doi.org/10.3390/s22041392][research_park_2022]
- Park, Sunghyun, Salar Latifi, Yongjun Park, Armand Behroozi, Byungsoo Jeon, and Scott Mahlke. 2022b. "SRTuner: Effective Compiler Optimization Customization by Exposing Synergistic Relations." In *2022 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo53902.2022.9741263][research_park_2022_b]
- Park, Jihee, Sungho Lee, Jaemin Hong, and Sukyoung Ryu. 2023. "Static Analysis of JNI Programs via Binary Decompilation." *IEEE Transactions on Software Engineering* 49 (5): 3089–3105. [https://doi.org/10.1109/tse.2023.3241639][research_park_2023]
- Park, Sangcheol, Suhwan Park, Jin-Ku Kang, and Yongwoo Kim. 2025. "FPGA-Accelerated Neural Network Inference via a μkernel-Enabled Bytecode Interpreter." In *2025 22nd International SoC Design Conference (ISOCC)*. IEEE. [https://doi.org/10.1109/isocc66390.2025.11329603][research_park_2025]
- Parra, Francisco. 2026. "SurtGIS: A High-Performance Raster Geospatial Analysis Library in Rust with WebAssembly and Python Support." *Environmental Modelling & Software* 204: 107102. [https://doi.org/10.1016/j.envsoft.2026.107102][research_parra_2026]
- Pascarella, Luca, and Alberto Bacchelli. 2017. "Classifying Code Comments in Java Open-Source Software Systems." In *2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2017.63][research_pascarella_2017]
- Patil, Sandeep, Valeriy Vyatkin, and Cheng Pang. 2015. "Counterexample-Guided Simulation Framework for Formal Verification of Flexible Automation Systems." In *2015 IEEE 13th International Conference on Industrial Informatics (INDIN)*. IEEE. [https://doi.org/10.1109/indin.2015.7281905][research_patil_2015]
- Patricio, Celia, Pablo Zubasti, Antonio Berlanga, and Miguel A. Patricio. 2026. "A Comparative Analysis of the Role of Large Language Models and Low-Rank Adaptation in Automated Program Repair." *Information and Software Technology* 198: 108238. [https://doi.org/10.1016/j.infsof.2026.108238][research_patricio_2026]
- Patsidis, Karyofyllis, Dimitris Konstantinou, Chrysostomos Nicopoulos, and Giorgos Dimitrakopoulos. 2018. "A Low-Cost Synthesizable RISC-V Dual-Issue Processor Core Leveraging the Compressed Instruction Set Extension." *Microprocessors and Microsystems* 61: 1–10. [https://doi.org/10.1016/j.micpro.2018.05.007][research_patsidis_2018]
- Patte, Sébastien, and Virgile Prevosto. 2025. "Typestates Specification and Verification in Frama-C." In *2025 IEEE/ACM 13th International Conference on Formal Methods in Software Engineering (FormaliSE)*. IEEE. [https://doi.org/10.1109/formalise66629.2025.00021][research_patte_2025]
- Pattyn, Frédéric. 2025. "Identifying Key Requirements Prioritization Criteria for Software Startup Survival: From Literature Review to Startup Focused Prioritization Method." In *2025 IEEE/ACM International Workshop on Software-Intensive Business (IWSiB)*. IEEE. [https://doi.org/10.1109/iwsib66663.2025.00006][research_pattyn_2025]
- Pattyn, Frédéric, Xiaofeng Wang, Geert Poels, Yannick Dillen, and Peter Goetz. 2026. "VECTR: A Lightweight Requirements Prioritization Method for Software Startups Grounded in ROI, Time-to-Value, and Confidence." *Computers* 15 (2): 117. [https://doi.org/10.3390/computers15020117][research_pattyn_2026]
- Pauley, Eric, Gang Tan, Danfeng Zhang, and Patrick McDaniel. 2022. "Performant Binary Fuzzing without Source Code Using Static Instrumentation." In *2022 IEEE Conference on Communications and Network Security (CNS)*. IEEE. [https://doi.org/10.1109/cns56114.2022.9947273][research_pauley_2022]
- Peccia, Federico Nicolás, Frederik Haxel, and Oliver Bringmann. 2025. "Tensor Program Optimization for the RISC-V Vector Extension Using Probabilistic Programs." In *2025 IEEE/ACM International Conference On Computer Aided Design (ICCAD)*. IEEE. [https://doi.org/10.1109/iccad66269.2025.11241007][research_peccia_2025]
- Pečimúth, Andrej. 2023. "Remote Just-in-Time Compilation for Dynamic Languages." In *Companion Proceedings of the 2023 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity*. ACM. [https://doi.org/10.1145/3618305.3623593][research_pecimuth_2023]
- Pei, Yu, Jeongju Sohn, and Mike Papadakis. 2025. "An Empirical Study of Web Flaky Tests: Understanding and Unveiling DOM Event Interaction Challenges." In *2025 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst62969.2025.10989030][research_pei_2025]
- Peng, Jinjun, Leyi Cui, Kele Huang, Junfeng Yang, and Baishakhi Ray. 2025. "CWEval: Outcome-Driven Evaluation on Functionality and Security of LLM Code Generation." In *2025 IEEE/ACM International Workshop on Large Language Models for Code (LLM4Code)*. IEEE. [https://doi.org/10.1109/llm4code66737.2025.00009][research_peng_2025]
- Peng, Mai Jacob, and Christophe Dubach. 2023. "LAGrad: Statically Optimized Differentiable Programming in MLIR." In *Proceedings of the 32nd ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3578360.3580259][research_peng_2023]
- Peng, Xianlun, Xiangyu Meng, and Fangfei Li. 2026. "A Priority-Ordered Swapping Algorithm for Submodular Maximization Problems." *IEEE Control Systems Letters* 10: 133–38. [https://doi.org/10.1109/lcsys.2026.3670932][research_peng_2026]
- Perez-Alvarez, Jose Miguel, Adrian Mos, Benjamin V. Hanrahan, and Iyadunni J. Adenuga. 2022. "Lowering Barriers to Application Development with Cloud-Native Domain-Specific Functions." In *2022 IEEE/ACM 44th International Conference on Software Engineering: Software Engineering in Society (ICSE-SEIS)*. IEEE. [https://doi.org/10.1109/icse-seis55304.2022.9793869][research_perezalvarez_2022]
- Pérez-Piqueras, Víctor, Pablo Bermejo López, and José Gámez. 2025. "Agile Effort Estimation Improved by Feature Selection and Model Explainability." In *Proceedings of the 20th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0013229800003928][research_perezpiqueras_2025]
- Peta, Sumeer Basha, Ranganath Nagesh Taware, Balkrishna Patil, Ramesh Krishna Mahimalur, and Srinivas Maddela. 2025. "AI for Code: Reinforcement-Learned Compiler Optimizations for HPC Workflows." In *2025 3rd World Conference on Communication & Computing (WCONF)*. IEEE. [https://doi.org/10.1109/wconf64849.2025.11233456][research_peta_2025]
- Petchartee, Somrak. 2025. "A Universal Quantum Compiler GPT: Multi-Framework Optimization and Translation Using Large Language Models." In *2025 29th International Computer Science and Engineering Conference (ICSEC)*. IEEE. [https://doi.org/10.1109/icsec67360.2025.11298108][research_petchartee_2025]
- Petrogalli, Francesco, and Paul Walker. 2018. "LLVM and the Automatic Vectorization of Loops Invoking Math Routines: -FSIMDMATH." In *2018 IEEE/ACM 5th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc.2018.8639354][research_petrogalli_2018]
- Petrovic, Goran, Marko Ivankovic, Bob Kurtz, Paul Ammann, and Rene Just. 2018. "An Industrial Application of Mutation Testing: Lessons, Challenges, and Research Directions." In *2018 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw.2018.00027][research_petrovic_2018]
- Phannachitta, Passakorn. 2026. "Input Perturbation Robustness for Software Effort Estimation: An Empirical Evaluation of LP4EE Enhancement Strategies." *Software Quality Journal* 34 (2): 30. [https://doi.org/10.1007/s11219-026-09758-3][research_phannachitta_2026]
- Phannachitta, Passakorn, Jacky Keung, Akito Monden, and Kenichi Matsumoto. 2016. "A Stability Assessment of Solution Adaptation Techniques for Analogy-Based Software Effort Estimation." *Empirical Software Engineering* 22 (1): 474–504. [https://doi.org/10.1007/s10664-016-9434-8][research_phannachitta_2016]
- Phipps-Costin, Luna, Carolyn Jane Anderson, Michael Greenberg, and Arjun Guha. 2021. "Solver-Based Gradual Type Migration." *Proceedings of the ACM on Programming Languages* 5 (OOPSLA): 1–27. [https://doi.org/10.1145/3485488][research_phippscostin_2021]
- Pichler, Christoph, Paley Li, Roland Schatz, and Hanspeter Mössenböck. 2023. "Hybrid Execution: Combining Ahead-of-Time and Just-in-Time Compilation." In *Proceedings of the 15th ACM SIGPLAN International Workshop on Virtual Machines and Intermediate Languages*. ACM. [https://doi.org/10.1145/3623507.3623554][research_pichler_2023]
- Pimentel, Joao Felipe, Leonardo Murta, Vanessa Braganholo, and Juliana Freire. 2019. "A Large-Scale Study about Quality and Reproducibility of Jupyter Notebooks." In *2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2019.00077][research_pimentel_2019]
- Pimentel, João Felipe, Leonardo Murta, Vanessa Braganholo, and Juliana Freire. 2021. "Understanding and Improving the Quality and Reproducibility of Jupyter Notebooks." *Empirical Software Engineering* 26 (4): 65. [https://doi.org/10.1007/s10664-021-09961-9][research_pimentel_2021]
- Pina, Diogo, Alfredo Goldman, and Graziela Tonin. 2021. "Technical Debt Prioritization: Taxonomy, Methods Results, and Practical Characteristics." In *2021 47th Euromicro Conference on Software Engineering and Advanced Applications (SEAA)*. IEEE. [https://doi.org/10.1109/seaa53835.2021.00034][research_pina_2021]
- Pinckney, Donald, Federico Cassano, Arjun Guha, and Jonathan Bell. 2023. "A Large Scale Analysis of Semantic Versioning in NPM." In *2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr59073.2023.00073][research_pinckney_2023]
- Pinto, Gustavo, Weslley Torres, Benito Fernandes, Fernando Castor, and Roberto S. M. Barros. 2015. "A Large-Scale Study on the Usage of Java’s Concurrent Programming Constructs." *Journal of Systems and Software* 106: 59–81. [https://doi.org/10.1016/j.jss.2015.04.064][research_pinto_2015]
- Pircher, S., J. Geier, A. Zeh, and D. Mueller-Gritschneder. 2021. "Exploring the RISC-V Vector Extension for the Classic McEliece Post-Quantum Cryptosystem." In *2021 22nd International Symposium on Quality Electronic Design (ISQED)*. IEEE. [https://doi.org/10.1109/isqed51717.2021.9424273][research_pircher_2021]
- Pirkelbauer, Peter, and Chunhua Liao. 2025. "CompilerGPT: Leveraging Large Language Models for Analyzing and Acting on Compiler Optimization Reports." In *High Performance Computing*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-032-07612-0\_25][research_pirkelbauer_2025]
- Pizard, Sebastián, Joaquín Lezama, Rodrigo García, Diego Vallespir, and Barbara Kitchenham. 2024. "Using Rapid Reviews to Support Software Engineering Practice: A Systematic Review and a Replication Study." *Empirical Software Engineering* 30 (1): 10. [https://doi.org/10.1007/s10664-024-10545-6][research_pizard_2024]
- Pizzolotto, Davide, and Katsuro Inoue. 2020. "Identifying Compiler and Optimization Options from Binary Code Using Deep Learning Approaches." In *2020 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme46990.2020.00031][research_pizzolotto_2020]
- Pizzolotto, Davide, and Katsuro Inoue. 2021. "Identifying Compiler and Optimization Level in Binary Code from Multiple Architectures." *IEEE Access* 9: 163461–75. [https://doi.org/10.1109/access.2021.3132950][research_pizzolotto_2021]
- Pnueli, A., M. Siegel, and E. Singerman. 1998. "Translation Validation." In *Tools and Algorithms for the Construction and Analysis of Systems*. Springer Berlin Heidelberg. [https://doi.org/10.1007/bfb0054170][research_pnueli_1998]
- Pokharel, Sugam, Pradip Sah, and Deepak Ganta. 2021. "Improved Prediction of Total Energy Consumption and Feature Analysis in Electric Vehicles Using Machine Learning and Shapley Additive Explanations Method." *World Electric Vehicle Journal* 12 (3): 94. [https://doi.org/10.3390/wevj12030094][research_pokharel_2021]
- Poorhosseini, Mehrdad, Wolfgang Nebel, and Kim Gruttner. 2020. "A Compiler Comparison in the RISC-V Ecosystem." In *2020 International Conference on Omni-layer Intelligent Systems (COINS)*. IEEE. [https://doi.org/10.1109/coins49042.2020.9191411][research_poorhosseini_2020]
- Poreba, Florian, and Stefan Sobernig. 2026. "Interruptibility of Software Developers and Its Prediction Using Psycho-Physiological Sensors: A Replication." *Empirical Software Engineering* 31 (3): 57. [https://doi.org/10.1007/s10664-025-10739-6][research_poreba_2026]
- Porpodas, Vasileios. 2017. "SuperGraph-SLP Auto-Vectorization." In *2017 26th International Conference on Parallel Architectures and Compilation Techniques (PACT)*. IEEE. [https://doi.org/10.1109/pact.2017.21][research_porpodas_2017]
- Postema, Jesse, Johan Fabry, Yannick Barthol, and Ana Oprescu. 2022. "Testing a PL/I Compiler Using Precomputation-Based Program Generation." In *2022 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst53961.2022.00042][research_postema_2022]
- Prado Lima, Jackson A., Willian D. F. Mendonça, Silvia R. Vergilio, and Wesley K. G. Assunção. 2022. "Cost-Effective Learning-Based Strategies for Test Case Prioritization in Continuous Integration of Highly-Configurable Software." *Empirical Software Engineering* 27 (6): 133. [https://doi.org/10.1007/s10664-021-10093-3][research_pradolima_2022]
- Prado Lima, Jackson A., and Silvia R. Vergilio. 2020. "Test Case Prioritization in Continuous Integration Environments: A Systematic Mapping Study." *Information and Software Technology* 121: 106268. [https://doi.org/10.1016/j.infsof.2020.106268][research_pradolima_2020]
- Priamo, Giacomo, Daniele Cono D'Elia, Mathias Payer, and Leonardo Querzoni. 2026. "Towards Path-Aware Coverage-Guided Fuzzing." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395191][research_priamo_2026]
- Programming, Scientific. 2025. "RETRACTION: Study on Large-Scale Promotion of Prefabricated Buildings in Anhui Province Based on SEM and IoT." *Scientific Programming* 2025 (1): 9801273. [https://doi.org/10.1155/scpr/9801273][research_programming_2025]
- Puffitsch, Wolfgang. 2016. "Efficient Worst-Case Execution Time Analysis of Dynamic Branch Prediction." In *2016 28th Euromicro Conference on Real-Time Systems (ECRTS)*. IEEE. [https://doi.org/10.1109/ecrts.2016.23][research_puffitsch_2016]
- Puschner, Peter, and Alan Burns. 2000. "Guest Editorial: A Review of Worst-Case Execution-Time Analysis." *Real-Time Systems* 18 (2–3): 115–28. [https://doi.org/10.1023/a:1008119029962][research_puschner_burns_2000]
- Pushpa, Ramaiah, and Maadappa Siddappa. 2022. "Fractional Artificial Bee Chicken Swarm Optimization Technique for QoS Aware Virtual Machine Placement in Cloud." *Concurrency and Computation: Practice and Experience* 35 (4): e7532. [https://doi.org/10.1002/cpe.7532][research_pushpa_2022]
- Qian, Siyuan Brant, Vimarsh Sathia, Ivan R. Ivanov, Jan Hückelheim, Paul Hovland, and William S. Moses. 2026b. "Thinking Fast and Correct: Automated Rewriting of Numerical Code through Compiler Augmentation." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395228][research_qian_2026]
- Qian, Kelvin, Scott Smith, Brandon Stride, Shiwei Weng, and Ke Wu. 2024. "Semantic-Type-Guided Bug Finding." *Proceedings of the ACM on Programming Languages* 8 (OOPSLA2): 2183–2210. [https://doi.org/10.1145/3689788][research_qian_2024]
- Qian, Chen, Jingbin Xu, Xin Xing, and Feng Guo. 2026a. "Test Case Sampling Optimization for Safety Validation of Automated Driving Systems." *Nature Communications* 17 (1): 3114. [https://doi.org/10.1038/s41467-026-69675-8][research_qian_2026_b]
- Qin, Yuxin, Dejice Jacob, and Jeremy Singer. 2024. "Characterizing Dynamic Memory Behavior in WebAssembly Workloads." In *2024 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)*. IEEE. [https://doi.org/10.1109/ispass61541.2024.00047][research_qin_2024]
- Qin, Feiran Alex, M. M. Abid Naziri, Hengyu Ai, Saikat Dutta, and Marcelo d'Amorim. 2026. "How Effective Is Coverage-Guided Fuzzing to Test Deep Learning Library APIs?" In *2026 IEEE International Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst69053.2026.00023][research_qin_2026]
- Queiroz Junior, Nilton Luiz, and Anderson Faustino da Silva. 2015. "Finding Good Compiler Optimization Sets: A Case-Based Reasoning Approach." In *Proceedings of the 17th International Conference on Enterprise Information Systems*. SCITEPRESS - Science and and Technology Publications. [https://doi.org/10.5220/0005380605040515][research_queirozjunior_2015]
- Quetschlich, Nils, Lukas Burgholzer, and Robert Wille. 2023a. "Compiler Optimization for Quantum Computing Using Reinforcement Learning." In *2023 60th ACM/IEEE Design Automation Conference (DAC)*. IEEE. [https://doi.org/10.1109/dac56929.2023.10248002][research_quetschlich_2023]
- Quetschlich, Nils, Lukas Burgholzer, and Robert Wille. 2023b. "Reducing the Compilation Time of Quantum Circuits Using Pre-Compilation on the Gate Level." In *2023 IEEE International Conference on Quantum Computing and Engineering (QCE)*. IEEE. [https://doi.org/10.1109/qce57702.2023.00091][research_quetschlich_2023_b]
- Raghu Raman, D., D. Santhagarooban, and N. Sathyanarayanan. 2024. "Optimizing Software Effort Estimation Accuracy with a Machine Learning Model." In *2024 5th International Conference for Emerging Technology (INCET)*. IEEE. [https://doi.org/10.1109/incet61516.2024.10593223][research_raghuraman_2024]
- Rahman, Shanto, Bala Naren Chanumolu, Suzzana Rafi, August Shi, and Wing Lam. 2025. "Ranking Relevant Tests for Order-Dependent Flaky Tests." In *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse55347.2025.00178][research_rahman_2025]
- Rahman, Mohammad Masudur, Foutse Khomh, Shamima Yeasmin, and Chanchal K. Roy. 2021. "The Forgotten Role of Search Queries in IR-Based Bug Localization: An Empirical Study." *Empirical Software Engineering* 26 (6): 116. [https://doi.org/10.1007/s10664-021-10022-4][research_rahman_2021]
- Rahmani, Kia, Mohammad Raza, Sumit Gulwani, et al. 2021. "Multi-Modal Program Inference: A Marriage of Pre-Trained Language Models and Component-Based Synthesis." *Proceedings of the ACM on Programming Languages* 5 (OOPSLA): 1–29. [https://doi.org/10.1145/3485535][research_rahmani_2021]
- Rajbhandari, Samyam, Jinsung Kim, Sriram Krishnamoorthy, et al. 2016. "A Domain-Specific Compiler for a Parallel Multiresolution Adaptive Numerical Simulation Environment." In *SC16: International Conference for High Performance Computing, Networking, Storage and Analysis*. IEEE. [https://doi.org/10.1109/sc.2016.39][research_rajbhandari_2016]
- Rajendran, Ganesamoorthy, Ghassan Samara, Johnsi J. Rani, Navyatha Ravi, G. Karthikeyan, and R. Ruth Shobitha. 2025. "Implement Machine Learning to Schedule Instructions to Speed up Execution: AI-Powered Microprocessor and Microcontroller Compiler Optimization." In *2025 IEEE Pune Section International Conference (PuneCon)*. IEEE. [https://doi.org/10.1109/punecon67554.2025.11379283][research_rajendran_2025]
- Ranzato, Francesco. 2016. "Abstract Interpretation of Supermodular Games." In *Static Analysis*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-662-53413-7\_20][research_ranzato_2016]
- Rao, Vignesh S., Tarunkant Gupta, Saastha Vasan, and L. R. Deepthi. 2020. "PHPIL: Fuzzing the PHP Interpreter with Custom Bytecode." In *2020 11th International Conference on Computing, Communication and Networking Technologies (ICCCNT)*. IEEE. [https://doi.org/10.1109/icccnt49239.2020.9225578][research_rao_2020]
- Rapoport, Marianna, Ifaz Kabir, Paul He, and Ondřej Lhoták. 2017. "A Simple Soundness Proof for Dependent Object Types." *Proceedings of the ACM on Programming Languages* 1 (OOPSLA): 1–27. [https://doi.org/10.1145/3133870][research_rapoport_2017]
- Raunak, M. S., and Megan M. Olsen. 2021. "Metamorphic Testing on the Continuum of Verification and Validation of Simulation Models." In *2021 IEEE/ACM 6th International Workshop on Metamorphic Testing (MET)*. IEEE. [https://doi.org/10.1109/met52542.2021.00015][research_raunak_2021]
- Raveendran, Aneesh, Vinayak Baramu Patil, David Selvakumar, and Vivian Desalphine. 2016. "A RISC-V Instruction Set Processor-Micro-Architecture Design and Analysis." In *2016 International Conference on VLSI Systems, Architectures, Technology and Applications (VLSI-SATA)*. IEEE. [https://doi.org/10.1109/vlsi-sata.2016.7593047][research_raveendran_2016]
- Razi, Mohammad, Nidhi Gupta, and Rajendra Kumar. 2025. "Intelligent Test Case Prioritization: A Review of Machine Learning-Based Approaches." In *2025 3rd International Conference on Sustainable Computing and Data Communication Systems (ICSCDS)*. IEEE. [https://doi.org/10.1109/icscds65426.2025.11167624][research_razi_2025]
- Razilov, Viktor, Emil Matus, and Gerhard Fettweis. 2022. "Communications Signal Processing Using RISC-V Vector Extension." In *2022 International Wireless Communications and Mobile Computing (IWCMC)*. IEEE. [https://doi.org/10.1109/iwcmc55113.2022.9824961][research_razilov_2022]
- Reboucas de Almeida, Rodrigo. 2019. "Business-Driven Technical Debt Prioritization." In *2019 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme.2019.00096][research_reboucasdealme_2019]
- Reboucas de Almeida, Rodrigo, Christoph Treude, and Uira Kulesza. 2019. "Tracy: A Business-Driven Technical Debt Prioritization Framework." In *2019 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme.2019.00028][research_reboucasdealme_2019_b]
- Reddy, Ravikiran Ravindranath, Sawan Singh, Arthur Perais, Alberto Ros, and Alexandra Jimborean. 2026. "Compiler-Assisted Instruction Fusion." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11394845][research_reddy_2026]
- Reineke, Jan, Daniel Grund, Christoph Berg, and Reinhard Wilhelm. 2007. "Timing Predictability of Cache Replacement Policies." *Real-Time Systems* 37 (2): 99–122. [https://doi.org/10.1007/s11241-007-9032-3][research_reineke_2007]
- Reiter, Pemma, Hui Jun Tay, Westley Weimer, Adam Doupé, Ruoyu Wang, and Stephanie Forrest. 2025. "Automatically Mitigating Vulnerabilities in Binary Programs via Partially Recompilable Decompilation." *IEEE Transactions on Dependable and Secure Computing* 22 (3): 2270–82. [https://doi.org/10.1109/tdsc.2024.3482413][research_reiter_2025]
- Rezazadeh, Navid, and Solmaz S. Kia. 2022. "Distributed Submodular Maximization: Trading Performance for Privacy." In *2022 IEEE 61st Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc51059.2022.9992452][research_rezazadeh_2022]
- Rezazadeh, Navid, and Solmaz S. Kia. 2023. "Distributed Strategy Selection: A Submodular Set Function Maximization Approach." *Automatica* 153: 111000. [https://doi.org/10.1016/j.automatica.2023.111000][research_rezazadeh_2023]
- Ribeiro, Francisco. 2023. "Large Language Models for Automated Program Repair." In *Companion Proceedings of the 2023 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity*. ACM. [https://doi.org/10.1145/3618305.3623587][research_ribeiro_2023]
- Richards, Gregor, Sylvain Lebresne, Brian Burg, and Jan Vitek. 2010. "An Analysis of the Dynamic Behavior of JavaScript Programs." In *Proceedings of the 31st ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/1806596.1806598][research_richards_2010]
- Richards, Jay, Daniel Wright, Simon Cooksey, and Mark Batty. 2025. "Symbolic MRD: Dynamic Memory, Undefined Behaviour, and Extrinsic Choice." *Proceedings of the ACM on Programming Languages* 9 (OOPSLA1): 1858–82. [https://doi.org/10.1145/3721089][research_richards_2025]
- Ridoy, Shahriyar Zaman, Md. Shazzad Hossain Shaon, Alfredo Cuzzocrea, and Mst Shapna Akter. 2024. "EnStack: An Ensemble Stacking Framework of Large Language Models for Enhanced Vulnerability Detection in Source Code." In *2024 IEEE International Conference on Big Data (BigData)*. IEEE. [https://doi.org/10.1109/bigdata62323.2024.10825609][research_ridoy_2024]
- Riener, Heinz, and Goerschwin Fey. 2016. "Counterexample-Guided Diagnosis." In *2016 1st IEEE International Verification and Security Workshop (IVSW)*. IEEE. [https://doi.org/10.1109/ivsw.2016.7566605][research_riener_2016]
- Rinard, Martin C. 2026. "Testing, Credible Compilation, and Verification in the Axon Verified Compiler in Lean and Claude Code." In *Proceedings of the 2026 ACM SIGPLAN International Workshop on Principles of Agentic Engineering*. ACM. [https://doi.org/10.1145/3819802.3820579][research_rinard_2026]
- Rivera, Joao, Franz Franchetti, and Markus Puschel. 2021. "An Interval Compiler for Sound Floating-Point Computations." In *2021 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo51591.2021.9370307][research_rivera_2021]
- Rivera, Joao, Franz Franchetti, and Markus Puschel. 2022. "A Compiler for Sound Floating-Point Computations Using Affine Arithmetic." In *2022 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo53902.2022.9741286][research_rivera_2022]
- Rizqullah, Muhammad, and Emad Albassam. 2026. "Model-Agnostic Empirical Evaluation of Test-Driven Prompt Engineering on Improving Accuracy and Efficiency in Large Language Models Python Code Generation." *IEEE Access* 14: 22801–21. [https://doi.org/10.1109/access.2026.3662817][research_rizqullah_2026]
- Rk, Risikesh, Sharad Sinha, and Nanditha Rao. 2021. "Variable Bit-Precision Vector Extension for RISC-V Based Processors." In *2021 IEEE 14th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)*. IEEE. [https://doi.org/10.1109/mcsoc51149.2021.00024][research_rk_2021]
- Robati Shirzad, Mohammad, and Patrick Lam. 2024. "A Study of Common Bug Fix Patterns in Rust." *Empirical Software Engineering* 29 (2): 44. [https://doi.org/10.1007/s10664-023-10437-1][research_robatishirzad_2024]
- Robles, Gregorio, Andrea Capiluppi, Jesus M. Gonzalez-Barahona, Björn Lundell, and Jonas Gamalielsson. 2022. "Development Effort Estimation in Free/open Source Software from Activity in Version Control Systems." *Empirical Software Engineering* 27 (6): 135. [https://doi.org/10.1007/s10664-022-10166-x][research_robles_2022]
- Rocca, Giovanni, Mattia G. Spina, and Floriano De Rango. 2025. "A Scalable and Efficient Intrusion Detection System Based on a Shapley Value Driven Feature Selection." In *2025 21th International Conference on Wireless and Mobile Computing, Networking and Communications (WiMob)*. IEEE. [https://doi.org/10.1109/wimob66857.2025.11257512][research_rocca_2025]
- Rodeghero, Paige, Da Huo, Tao Ding, Collin McMillan, and Malcom Gethers. 2016. "An Empirical Study on How Expert Knowledge Affects Bug Reports." *Journal of Software: Evolution and Process* 28 (7): 542–64. [https://doi.org/10.1002/smr.1773][research_rodeghero_2016]
- Rodríguez-Pérez, Gema, Gregorio Robles, and Jesús M. González-Barahona. 2018. "Reproducibility and Credibility in Empirical Software Engineering: A Case Study Based on a Systematic Literature Review of the Use of the SZZ Algorithm." *Information and Software Technology* 99: 164–76. [https://doi.org/10.1016/j.infsof.2018.03.009][research_rodriguezperez_2018]
- Rodruksa, Soravit, and Denduang Pradubsuwun. 2017. "Formal Verification of ABAP by Z Specification." In *2017 14th International Joint Conference on Computer Science and Software Engineering (JCSSE)*. IEEE. [https://doi.org/10.1109/jcsse.2017.8025943][research_rodruksa_2017]
- Rohr, David, and Volker Lindenstruth. 2017. "Fast Failure Erasure Encoding Using Just in Time Compilation for CPUs, GPUs, and FPGAs." In *2017 IEEE International Conference on Cluster Computing (CLUSTER)*. IEEE. [https://doi.org/10.1109/cluster.2017.101][research_rohr_2017]
- Rojas, Luis, Cristian Olivares-Rodriguez, Claudio Alvarez, and Pedro G. Campos. 2022. "OurRank: A Software Requirements Prioritization Method Based on Qualitative Assessment and Cost-Benefit Prediction." *IEEE Access* 10: 131772–87. [https://doi.org/10.1109/access.2022.3230152][research_rojas_2022]
- Rojas, José Miguel, Mattia Vivanti, Andrea Arcuri, and Gordon Fraser. 2016. "A Detailed Investigation of the Effectiveness of Whole Test Suite Generation." *Empirical Software Engineering* 22 (2): 852–93. [https://doi.org/10.1007/s10664-015-9424-2][research_rojas_2016]
- Romano, Alan, Zihe Song, Sampath Grandhi, Wei Yang, and Weihang Wang. 2021. "An Empirical Analysis of UI-Based Flaky Tests." In *2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse43902.2021.00141][research_romano_2021]
- Rooijakkers, Thomas, Anne Nijsten, Cristian Daniele, Erieke Weitenberg, Ringo Groenewegen, and Arthur Melissen. 2026. "WuppieFuzz: Coverage-Guided, Stateful REST API Fuzzing." In *Proceedings of the 12th International Conference on Information Systems Security and Privacy*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014327000004061][research_rooijakkers_2026]
- Roshan, A. Krithik, and M. Sughasiny. 2025. "Role-Aware Intelligent Agent Framework for Enhanced Code Generation Using Large Language Model." In *2025 International Conference on Communication, Computer, and Information Technology (IC3IT)*. IEEE. [https://doi.org/10.1109/ic3it66137.2025.11341145][research_roshan_2025]
- Rostum, Hussam, and Jόzsef Vásárhelyi. 2026. "FPGA-Based ORB Accelerator: Effects of Compiler Optimization Levels." In *2026 27th International Carpathian Control Conference (ICCC)*. IEEE. [https://doi.org/10.1109/iccc71363.2026.11593248][research_rostum_2026]
- Roth, Jannik P., and Jürgen Bajorath. 2024. "Machine Learning Models with Distinct Shapley Value Explanations Decouple Feature Attribution and Interpretation for Chemical Compound Predictions." *Cell Reports Physical Science* 5 (8): 102110. [https://doi.org/10.1016/j.xcrp.2024.102110][research_roth_2024]
- Rothermel, G., R. H. Untch, Chengyun Chu, and M. J. Harrold. 2001. "Prioritizing Test Cases for Regression Testing." *IEEE Transactions on Software Engineering* 27 (10): 929–48. [https://doi.org/10.1109/32.962562][research_rothermel_2001]
- Rouson, Damian, and Dan Bonachea. 2022. "Caffeine: CoArray Fortran Framework of Efficient Interfaces to Network Environments." In *2022 IEEE/ACM Eighth Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc56686.2022.00009][research_rouson_2022]
- Roza, Enrique A. da, Jackson A. do Prado Lima, and Silvia R. Vergilio. 2024. "On the Use of Contextual Information for Machine Learning Based Test Case Prioritization in Continuous Integration Development." *Information and Software Technology* 171: 107444. [https://doi.org/10.1016/j.infsof.2024.107444][research_roza_2024]
- Rua, Rui, Marco Couto, and Joao Saraiva. 2019. "GreenSource: A Large-Scale Collection of Android Code, Tests and Energy Metrics." In *2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2019.00035][research_rua_2019]
- Ruep, Katharina, and Daniel Grose. 2022. "SpinalFuzz: Coverage-Guided Fuzzing for SpinalHDL Designs." In *2022 IEEE European Test Symposium (ETS)*. IEEE. [https://doi.org/10.1109/ets54262.2022.9810421][research_ruep_2022]
- Sadiq, Mohd., Tanveer Hassan, and Sanjida Nazneen. 2017. "AHP\_GORE\_PSR: Applying Analytic Hierarchy Process in Goal Oriented Requirements Elicitation Method for the Prioritization of Software Requirements." In *2017 3rd International Conference on Computational Intelligence & Communication Technology (CICT)*. IEEE. [https://doi.org/10.1109/ciact.2017.7977366][research_sadiq_2017]
- Saillard, Emmanuelle, Marc Sergent, Celia Tassadit Ait Kaci, and Denis Barthou. 2022. "Static Local Concurrency Errors Detection in MPI-RMA Programs." In *2022 IEEE/ACM Sixth International Workshop on Software Correctness for HPC Applications (Correctness)*. IEEE. [https://doi.org/10.1109/correctness56720.2022.00008][research_saillard_2022]
- Salehi, Majid, Gilles De Borger, Danny Hughes, and Bruno Crispo. 2022. "NemesisGuard: Mitigating Interrupt Latency Side Channel Attacks with Static Binary Rewriting." *Computer Networks* 205: 108744. [https://doi.org/10.1016/j.comnet.2021.108744][research_salehi_2022]
- Salim, Salim S., Andy Nisbet, and Mikel Luján. 2019. "Towards a WebAssembly Standalone Runtime on GraalVM." In *Proceedings Companion of the 2019 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity*. ACM. [https://doi.org/10.1145/3359061.3362780][research_salim_2019]
- Samaana, Haya, Diego Elias Costa, Ahmad Abdellatif, and Emad Shihab. 2025. "Opportunities and Security Risks of Technical Leverage: A Replication Study on the NPM Ecosystem." *Empirical Software Engineering* 30 (4): 96. [https://doi.org/10.1007/s10664-025-10648-8][research_samaana_2025]
- Samal, Lopamudra, and Chiranjibi Samal. 2019. "Application Specific Instruction Set Processor Design for Embedded Application Using the CoWare Tool." In *2019 International Conference on Innovative Trends and Advances in Engineering and Technology (ICITAET)*. IEEE. [https://doi.org/10.1109/icitaet47105.2019.9170210][research_samal_2019]
- Samiei, Arvin, Nafiseh Kahani, Mohammadreza Dehghanitafti, and Mojtaba Ahmadi. 2024. "Worst-Case Execution Time Analysis of Real-Time Robotic Algorithms Using Reinforcement Learning." In *2024 34th International Conference on Collaborative Advances in Software and COmputiNg (CASCON)*. IEEE. [https://doi.org/10.1109/cascon62161.2024.10838116][research_samiei_2024]
- Sandberg Ericsson, Adam, Magnus O. Myreen, and Johannes Åman Pohjola. 2017. "A Verified Generational Garbage Collector for CakeML." In *Interactive Theorem Proving*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-66107-0\_28][research_sandbergericss_2017]
- Sandberg Ericsson, Adam, Magnus O. Myreen, and Johannes Åman Pohjola. 2018. "A Verified Generational Garbage Collector for CakeML." *Journal of Automated Reasoning* 63 (2): 463–88. [https://doi.org/10.1007/s10817-018-9487-z][research_sandbergericss_2018]
- Santhi, Nandakishore, Stephan Eidenbenz, and Jason Liu. 2015. "The Simian Concept: Parallel Discrete Event Simulation with Interpreted Languages and Just-in-Time Compilation." In *2015 Winter Simulation Conference (WSC)*. IEEE. [https://doi.org/10.1109/wsc.2015.7408405][research_santhi_2015]
- Santinelli, Luca, and Zhishan Guo. 2017. "On the Criticality of Probabilistic Worst-Case Execution Time Models." In *Dependable Software Engineering. Theories, Tools, and Applications*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-69483-2\_4][research_santinelli_2017]
- Santos, Mailson Ribeiro, Affonso Guedes, and Ignacio Sanchez-Gendriz. 2024c. "SHapley Additive exPlanations (SHAP) for Efficient Feature Selection in Rolling Bearing Fault Diagnosis." *Machine Learning and Knowledge Extraction* 6 (1): 316–41. [https://doi.org/10.3390/make6010016][research_santos_2024]
- Sarker, Laboni, and Tevfik Bultan. 2025. "Hybrid Equivalence/Non-Equivalence Testing." In *2025 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst62969.2025.10988990][research_sarker_2025]
- Sasano, Isao. 2020. "An Approach to Generate Text-Based IDEs for Syntax Completion Based on Syntax Specification." In *Proceedings of the 2020 ACM SIGPLAN Workshop on Partial Evaluation and Program Manipulation*. ACM. [https://doi.org/10.1145/3372884.3373158][research_sasano_2020]
- Savary, Louis, Simon Rokicki, and Steven Derrien. 2025. "Ahead of Time Generation for GPSA Protection in RISC-V Embedded Cores." In *2025 IEEE 36th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap65064.2025.00019][research_savary_2025]
- Sawant, Priyanka Dattatray. 2024. "Test Case Prioritization for Regression Testing Using Machine Learning." In *2024 IEEE International Conference on Artificial Intelligence Testing (AITest)*. IEEE. [https://doi.org/10.1109/aitest62860.2024.00027][research_sawant_2024]
- Scheidgen, Markus, Martin Smidt, and Joachim Fischer. 2017. "Creating and Analyzing Source Code Repository Models: A Model-Based Approach to Mining Software Repositories." In *Proceedings of the 5th International Conference on Model-Driven Engineering and Software Development*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0006127303290336][research_scheidgen_2017]
- Scheidl, Fabian. 2020. "Valent-Blocks: Scalable High-Performance Compilation of WebAssembly Bytecode for Embedded Systems." In *2020 International Conference on Computing, Electronics & Communications Engineering (iCCECE)*. IEEE. [https://doi.org/10.1109/iccece49321.2020.9231154][research_scheidl_2020]
- Schlägl, Manfred, and Daniel Groβe. 2025. "Fast Interpreter-Based Instruction Set Simulation for Virtual Prototypes." In *2025 Design, Automation & Test in Europe Conference (DATE)*. IEEE. [https://doi.org/10.23919/date64628.2025.10992929][research_schlagl_2025]
- Schnakenbeck, Aron, Robin Mroß, Marcus Völker, Stefan Kowalewski, and Alexander Fay. 2023. "A Control Flow Based Static Analysis of GRAFCET Using Abstract Interpretation." In *2023 IEEE 21st International Conference on Industrial Informatics (INDIN)*. IEEE. [https://doi.org/10.1109/indin51400.2023.10218176][research_schnakenbeck_2023]
- Schroeder, Tom, Minh Phan, and Yang Chen. 2025. "A Preliminary Study of Fixed Flaky Tests in Rust Projects on GitHub." In *2025 IEEE/ACM International Flaky Tests Workshop (FTW)*. IEEE. [https://doi.org/10.1109/ftw66604.2025.00010][research_schroeder_2025]
- Schuiki, Fabian, Andreas Kurth, Tobias Grosser, and Luca Benini. 2020a. "LLHD: A Multi-Level Intermediate Representation for Hardware Description Languages." In *Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3385412.3386024][research_schuiki_2020]
- Schulmann, Haya, and Niklas Vogel. 2026. "Batch Me If You Can: Coverage-Guided RPKI Fuzzing at Scale." In *2026 IEEE Symposium on Security and Privacy (SP)*. IEEE. [https://doi.org/10.1109/sp63933.2026.00188][research_schulmann_2026]
- Schulte, Lukas, Anamaria Mojica-Hanke, Mario Linares-Vásquez, and Steffen Herbold. 2026. "An Exploratory Study of Bug-Introducing Changes: Exploring Relationships in Bug-Introducing Changes towards Causal Understanding." *Empirical Software Engineering* 31 (5): 114. [https://doi.org/10.1007/s10664-026-10822-6][research_schulte_2026]
- Schwarz, Tobias, Tobias Kamm, and Alexis Engelke. 2026. "TPDE: A Fast Adaptable Compiler Back-End Framework." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395208][research_schwarz_2026]
- Seddiki, Abdessamed, Arab Mohammed, Zakaria Hebbal, et al. 2026. "CHEHAB: Automatic Compiler Code Optimization for Fully Homomorphic Encryption." In *Proceedings of the 35th ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3771775.3786269][research_seddiki_2026]
- Seeker, Volker, Chris Cummins, Murray Cole, Björn Franke, Kim Hazelwood, and Hugh Leather. 2024. "Revealing Compiler Heuristics through Automated Discovery and Optimization." In *2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo57630.2024.10444847][research_seeker_2024]
- Seidler, Maximilian, Martin Michelis, Peter Wägemann, and Rüdiger Kapitza. 2026. "Wasm-WCET: Worst-Case Execution-Time Analysis of WebAssembly Modules on Updatable Resource-Constrained Embedded Devices." In *2026 IEEE 32nd Real-Time and Embedded Technology and Applications Symposium (RTAS)*. IEEE. [https://doi.org/10.1109/rtas68450.2026.00024][research_seidler_2026]
- Seitzer, Maximilian, Michael Gruhn, and Tilo Müller. 2015. "A Bytecode Interpreter for Secure Program Execution in Untrusted Main Memory." In *Computer Security -- ESORICS 2015*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-24177-7\_19][research_seitzer_2015]
- Seo, Yongjin, and Hyeon Soo Kim. 2016. "Operator-Data Type Pair Based Execution Environments Independent Worst-Case Execution Time Measuring Method." In *2016 IEEE/ACIS 15th International Conference on Computer and Information Science (ICIS)*. IEEE. [https://doi.org/10.1109/icis.2016.7550831][research_seo_2016]
- Seo, Min-Guk, and Hyo-Sang Shin. 2018. "Greedily Excluding Algorithm for Submodular Maximization." In *2018 IEEE Conference on Control Technology and Applications (CCTA)*. IEEE. [https://doi.org/10.1109/ccta.2018.8511628][research_seo_2018]
- Sewell, Thomas Arthur Leck, Magnus O. Myreen, and Gerwin Klein. 2013. "Translation Validation for a Verified OS Kernel." In *Proceedings of the 34th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/2491956.2462183][research_sewell_2013]
- Sghaier, Oussama Ben, Martin Weyssow, and Houari Sahraoui. 2025. "Harnessing Large Language Models for Curated Code Reviews." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00039][research_sghaier_2025]
- Shah, Mehil B., Mohammad Masudur Rahman, and Foutse Khomh. 2024. "Towards Enhancing the Reproducibility of Deep Learning Bugs: An Empirical Study." *Empirical Software Engineering* 30 (1): 23. [https://doi.org/10.1007/s10664-024-10579-w][research_shah_2024]
- Shah, Mihir, and Benjamin Carrion Schafer. 2020. "Flexible Runtime Reconfigurable Computing Overlay Architecture and Optimization for Dataflow Applications." In *2020 IEEE/ACM 6th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC) and Workshop on Hierarchical Parallelism for Exascale Computing (HiPar)*. IEEE. [https://doi.org/10.1109/llvmhpchipar51896.2020.00015][research_shah_2020]
- Shahzad, Hafsah, Ahmed Sanaullah, Sanjay Arora, et al. 2022. "Reinforcement Learning Strategies for Compiler Optimization in High Level Synthesis." In *2022 IEEE/ACM Eighth Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvm-hpc56686.2022.00007][research_shahzad_2022]
- Shaikhha, Amir, Mathieu Huot, and Shideh Hashemian. 2024. "A Tensor Algebra Compiler for Sparse Differentiation." In *2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo57630.2024.10444787][research_shaikhha_2024]
- Shamshiri, Sina, Rene Just, Jose Miguel Rojas, Gordon Fraser, Phil McMinn, and Andrea Arcuri. 2015. "Do Automatically Generated Unit Tests Find Real Faults? An Empirical Study of Effectiveness and Challenges (T)." In *2015 30th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase.2015.86][research_shamshiri_2015]
- Shao, Fei, Rong Peng, Han Lai, and Bangchao Wang. 2017. "DRank: A Semi-Automated Requirements Prioritization Method Based on Preferences and Dependencies." *Journal of Systems and Software* 126: 141–56. [https://doi.org/10.1016/j.jss.2016.09.043][research_shao_2017]
- Sharif, Aizaz, Dusica Marijan, and Marius Liaaen. 2021. "DeepOrder: Deep Learning for Test Case Prioritization in Continuous Integration Testing." In *2021 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme52107.2021.00053][research_sharif_2021]
- Sharma, Tushar, and Marouane Kessentini. 2021. "QScored: A Large Dataset of Code Smells and Quality Metrics." In *2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr52588.2021.00080][research_sharma_2021]
- Shen, Yanlong, Yu Liu, and Ying Zhou. 2024. "RLGFuzz: Reinforcement Learning Guided Fuzzing with State-Coverage Mapping Environment." In *2024 IEEE 32nd International Conference on Network Protocols (ICNP)*. IEEE. [https://doi.org/10.1109/icnp61940.2024.10858502][research_shen_2024]
- Shepperd, Martin, Nemitari Ajienka, and Steve Counsell. 2018. "The Role and Value of Replication in Empirical Software Engineering Results." *Information and Software Technology* 99: 120–32. [https://doi.org/10.1016/j.infsof.2018.01.006][research_shepperd_2018]
- Shi, Qiancheng, Qihong Han, Zhanqi Cui, and Zheng Zeng. 2025. "SPRoC: Semantics-Preserving Mutations for Robustness Evaluation of Code Generation Large Language Models." In *2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*. IEEE. [https://doi.org/10.1109/smc58881.2025.11343558][research_shi_2025]
- Shi, Kensen, Jacob Steinhardt, and Percy Liang. 2019. "FrAngel: Component-Based Synthesis with Control Structures." *Proceedings of the ACM on Programming Languages* 3 (POPL): 1–29. [https://doi.org/10.1145/3290386][research_shi_2019]
- Shi, Yishuo, and Hui Zhao. 2024. "Greedy Algorithm for Maximization of Semi-Monotone Non-Submodular Functions with Applications." *Theoretical Computer Science* 1013: 114755. [https://doi.org/10.1016/j.tcs.2024.114755][research_shi_2024]
- Shillito, Ian, and Dominik Kirst. 2024. "A Mechanised and Constructive Reverse Analysis of Soundness and Completeness of Bi-Intuitionistic Logic." In *Proceedings of the 13th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3636501.3636957][research_shillito_2024]
- Shimmi, Samiha, and Mona Rahimi. 2022. "Patterns of Code-to-Test Co-Evolution for Automated Test Suite Maintenance." In *2022 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst53961.2022.00023][research_shimmi_2022]
- Shin, Chaewon, Gowon Han, Suhyeon Song, Jinsun Park, Yoon-Ho Choi, and Donghyun Kwon. 2026. "WARD: Efficient Memory Protection for WebAssembly on Tiny Embedded Systems." *IEEE Access* 14: 5925–39. [https://doi.org/10.1109/access.2025.3650447][research_shin_2026]
- Shu, Rui, Tianpei Xia, Jianfeng Chen, Laurie Williams, and Tim Menzies. 2021. "How to Better Distinguish Security Bug Reports (Using Dual Hyperparameter Optimization)." *Empirical Software Engineering* 26 (3): 53. [https://doi.org/10.1007/s10664-020-09906-8][research_shu_2021]
- Shukla, Suyash, and Sandeep Kumar. 2021a. "An Extreme Learning Machine Based Approach for Software Effort Estimation." In *Proceedings of the 16th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0010397700470057][research_shukla_2021_b]
- Shukla, Suyash, and Sandeep Kumar. 2021b. "A Stacking Ensemble-Based Approach for Software Effort Estimation." In *Proceedings of the 16th International Conference on Evaluation of Novel Approaches to Software Engineering*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0010405002050212][research_shukla_2021]
- Siavash, Nazanin, and Armin Moin. 2025. "Model-Driven Quantum Code Generation Using Large Language Models and Retrieval-Augmented Generation." In *2025 ACM/IEEE 28th International Conference on Model Driven Engineering Languages and Systems (MODELS)*. IEEE. [https://doi.org/10.1109/models67397.2025.00031][research_siavash_2025]
- Silva, André, and Martin Monperrus. 2025. "RepairBench: Leaderboard of Frontier Models for Program Repair." In *2025 IEEE/ACM International Workshop on Large Language Models for Code (LLM4Code)*. IEEE. [https://doi.org/10.1109/llm4code66737.2025.00006][research_silva_2025]
- Simon, Hendrik, and Stefan Kowalewski. 2016. "Static Analysis of Sequential Function Charts Using Abstract Interpretation." In *2016 IEEE 21st International Conference on Emerging Technologies and Factory Automation (ETFA)*. IEEE. [https://doi.org/10.1109/etfa.2016.7733648][research_simon_2016]
- Singh, Vijay Pal, Aijaz Ahmad, and Kushal Manoharrao Jagtap. 2023. "Weighted Shapley Value: A Cooperative Game Theory for Loss Allocation in Distribution Systems." *Frontiers in Energy Research* 11: 1129846. [https://doi.org/10.3389/fenrg.2023.1129846][research_singh_2023]
- Singh, Mahendra Pratap, and Manoj Kumar Jain. 2015. "ISA Customization for Application Specific Instruction Set Processors." In *2015 International Conference on Pervasive Computing (ICPC)*. IEEE. [https://doi.org/10.1109/pervasive.2015.7087117][research_singh_2015]
- Singh, Mayank, and Viranjay M. Srivastava. 2017. "Extended Firm Mutation Testing: A Cost Reduction Technique for Mutation Testing." In *2017 Fourth International Conference on Image Information Processing (ICIIP)*. IEEE. [https://doi.org/10.1109/iciip.2017.8313788][research_singh_2017]
- Singhal, Shweta, Bharti Suri, and Sanjay Misra. 2017. "An Empirical Study of Regression Test Suite Reduction Using MHBG\_TCS Tool." In *2017 International Conference on Computing Networking and Informatics (ICCNI)*. IEEE. [https://doi.org/10.1109/iccni.2017.8123805][research_singhal_2017]
- Sisto, A., L. Pilato, R. Serventi, S. Saponara, and L. Fanucci. 2016. "Application Specific Instruction Set Processor for Sensor Conditioning in Automotive Applications." *Microprocessors and Microsystems* 47: 375–84. [https://doi.org/10.1016/j.micpro.2016.10.001][research_sisto_2016]
- Sizilio Nery, Gustavo, Daniel Alencar da Costa, and Uira Kulesza. 2019. "An Empirical Study of the Relationship between Continuous Integration and Test Code Evolution." In *2019 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme.2019.00075][research_sizilionery_2019]
- Skalistis, Stefanos, and Alena Simalatsar. 2016. "Worst-Case Execution Time Analysis for Many-Core Architectures with NoC." In *Formal Modeling and Analysis of Timed Systems*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-44878-7\_13][research_skalistis_2016]
- Slavı́k, Petr. 1997. "A Tight Analysis of the Greedy Algorithm for Set Cover." *Journal of Algorithms* 25 (2): 237–54. [https://doi.org/10.1006/jagm.1997.0887][research_slavik_1997]
- Soeiro, Luís, Thomas Robert, and Stefano Zacchiroli. 2025. "Wild SBOMs: A Large-Scale Dataset of Software Bills of Materials from Public Code." In *2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr66628.2025.00036][research_soeiro_2025]
- Sommer, Lukas, Cristian Axenie, and Andreas Koch. 2022. "SPNC: An Open-Source MLIR-Based Compiler for Fast Sum-Product Network Inference on CPUs and GPUs." In *2022 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo53902.2022.9741277][research_sommer_2022]
- Son, Jeongki, Gabin An, Jingun Hong, and Shin Yoo. 2025. "Evaluating Machine Learning-Based Test Case Prioritization in the Real World: An Experiment with SAP HANA." In *2025 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst62969.2025.10989019][research_son_2025]
- Song, Xiaotao, Hailong Sun, Xu Wang, and Jiafei Yan. 2019. "A Survey of Automatic Generation of Source Code Comments: Algorithms and Techniques." *IEEE Access* 7: 111411–28. [https://doi.org/10.1109/access.2019.2931579][research_song_2019]
- Sonoyama, Atsuya, Masato Oguchi, Takeshi Kamiyama, Akira Fukuda, and Saneyasu Yamaguchi. 2020. "Performance Improvement of Kotlin Program in Consideration of JIT Compiler Optimization." In *2020 IEEE International Conference on Consumer Electronics - Taiwan (ICCE-Taiwan)*. IEEE. [https://doi.org/10.1109/icce-taiwan49838.2020.9258219][research_sonoyama_2020]
- Soremekun, Ezekiel, Lukas Kirschner, Marcel Böhme, and Andreas Zeller. 2021. "Locating Faults with Program Slicing: An Empirical Analysis." *Empirical Software Engineering* 26 (3): 51. [https://doi.org/10.1007/s10664-020-09931-7][research_soremekun_2021]
- Sortino, M., S. Belfio, and G. Totis. 2015. "An Innovative Approach for Automatic Generation, Verification and Optimization of Part Programs in Turning." *Journal of Manufacturing Systems* 36: 168–81. [https://doi.org/10.1016/j.jmsy.2014.03.002][research_sortino_2015]
- Sri-iesaranusorn, Panyawut, Raula Gaikovina Kula, and Takashi Ishio. 2021. "Does Code Review Promote Conformance? A Study of OpenStack Patches." In *2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr52588.2021.00056][research_sriiesaranusor_2021]
- Steingartner, William. 2021. "Compiler Module of Abstract Machine Code for Formal Semantics Course." In *2021 IEEE 19th World Symposium on Applied Machine Intelligence and Informatics (SAMI)*. IEEE. [https://doi.org/10.1109/sami50585.2021.9378696][research_steingartner_2021]
- Stepanov, Daniil, Marat Akhin, and Mikhail Belyaev. 2021. "Type-Centric Kotlin Compiler Fuzzing: Preserving Test Program Correctness by Preserving Types." In *2021 14th IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst49551.2021.00044][research_stepanov_2021]
- Stern, Ari, and Alexander Tettenhorst. 2019. "Hodge Decomposition and the Shapley Value of a Cooperative Game." *Games and Economic Behavior* 113: 186–98. [https://doi.org/10.1016/j.geb.2018.09.006][research_stern_2019]
- Știrb, Iulia, and Gilbert-Rainer Gillich. 2023. "A Low-Level Virtual Machine Just-In-Time Prototype for Running an Energy-Saving Hardware-Aware Mapping Algorithm on C/C++ Applications That Use Pthreads." *Energies* 16 (19): 6781. [https://doi.org/10.3390/en16196781][research_stirb_2023]
- Stocco, Andrea, Brian Pulfer, and Paolo Tonella. 2023. "Model vs System Level Testing of Autonomous Driving Systems: A Replication and Extension Study." *Empirical Software Engineering* 28 (3): 73. [https://doi.org/10.1007/s10664-023-10306-x][research_stocco_2023]
- Stochel, Marek G., Piotr Cholda, and Mariusz R. Wawrowski. 2020. "Continuous Debt Valuation Approach (CoDVA) for Technical Debt Prioritization." In *2020 46th Euromicro Conference on Software Engineering and Advanced Applications (SEAA)*. IEEE. [https://doi.org/10.1109/seaa51224.2020.00066][research_stochel_2020]
- Stochel, Marek G., Piotr Cholda, and Mariusz R. Wawrowski. 2022. "Adopting DevOps Paradigm in Technical Debt Prioritization and Mitigation." In *2022 48th Euromicro Conference on Software Engineering and Advanced Applications (SEAA)*. IEEE. [https://doi.org/10.1109/seaa56994.2022.00055][research_stochel_2022]
- Stojković, Dušan, and Miroslav Popovic. 2025. "A Way to Identify Potential Functions for Vectorization for RISC-V." In *2025 12th International Conference on Electrical, Electronic and Computing Engineering (IcETRAN)*. IEEE. [https://doi.org/10.1109/icetran66854.2025.11114225][research_stojkovic_2025]
- Štrumbelj, Erik, and Igor Kononenko. 2013. "Explaining Prediction Models and Individual Predictions with Feature Contributions." *Knowledge and Information Systems* 41 (3): 647–65. [https://doi.org/10.1007/s10115-013-0679-x][research_strumbelj_kononenko_2013]
- Su, Haoran, Jun Ai, Dan Yu, and Hong Zhang. 2023. "An Evaluation Method for Large Language Models’ Code Generation Capability." In *2023 10th International Conference on Dependable Systems and Their Applications (DSA)*. IEEE. [https://doi.org/10.1109/dsa59317.2023.00118][research_su_2023]
- Su, Qingran, Xingze Li, Yuming Ren, Ruinan Qiu, Chunming Hu, and Yongfeng Yin. 2025. "Attention Transfer Reinforcement Learning for Test Case Prioritization in Continuous Integration." *Applied Sciences* 15 (4): 2243. [https://doi.org/10.3390/app15042243][research_su_2025]
- Su, Xing, Xiangke Liao, and Jingling Xue. 2017. "Automatic Generation of Fast BLAS3-GEMM: A Portable Compiler Approach." In *2017 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo.2017.7863734][research_su_2017]
- Sun, Haoyuan, David Grimsman, and Jason R. Marden. 2020. "Distributed Submodular Maximization with Parallel Execution." In *2020 American Control Conference (ACC)*. IEEE. [https://doi.org/10.23919/acc45564.2020.9147476][research_sun_2020]
- Sun, Xiaoming, Jialin Zhang, and Shuo Zhang. 2024. "Deterministic Streaming Algorithms for Non-Monotone Submodular Maximization." *Frontiers of Computer Science* 19 (6): 196404. [https://doi.org/10.1007/s11704-024-40266-4][research_sun_2024]
- Sun, Xiaobing, Tianchi Zhou, Gengjie Li, Jiajun Hu, Hui Yang, and Bin Li. 2017. "An Empirical Study on Real Bugs for Machine Learning Programs." In *2017 24th Asia-Pacific Software Engineering Conference (APSEC)*. IEEE. [https://doi.org/10.1109/apsec.2017.41][research_sun_2017]
- Suo, Chenyao, Jianrong Wang, Yongjia Wang, Jiajun Jiang, Qingchao Shen, and Junjie Chen. 2025. "DESIL: Detecting Silent Bugs in MLIR Compiler Infrastructure." *Proceedings of the ACM on Programming Languages* 9 (OOPSLA2): 3093–3119. [https://doi.org/10.1145/3763161][research_suo_2025]
- Susca, Mircea, Vlad Mihaly, Dora Morar, and Petru Dobra. 2022. "Worst-Case Execution Time Estimation for Numerical Controllers." In *2022 IEEE International Conference on Automation, Quality and Testing, Robotics (AQTR)*. IEEE. [https://doi.org/10.1109/aqtr55203.2022.9802027][research_susca_2022]
- Sutoyo, Edi, Paris Avgeriou, and Andrea Capiluppi. 2026. "Reducing Labeling Effort in Architecture Technical Debt Detection through Active Learning and Explainable AI." *Empirical Software Engineering* 31 (6): 183. [https://doi.org/10.1007/s10664-026-10916-1][research_sutoyo_2026]
- Suzanne, Thibault, and Antoine Miné. 2016. "From Array Domains to Abstract Interpretation under Store-Buffer-Based Memory Models." In *Static Analysis*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-662-53413-7\_23][research_suzanne_2016]
- Swain, Bradley, and Jeff Huang. 2018. "Towards Incremental Static Race Detection in OpenMP Programs." In *2018 IEEE/ACM 2nd International Workshop on Software Correctness for HPC Applications (Correctness)*. IEEE. [https://doi.org/10.1109/correctness.2018.00009][research_swain_2018]
- Tabassam, Nadra, and Roman Obermaisser. 2017. "Class-Based Query-Optimization for Minimizing Worst-Case Execution Times of Diagnostic Queries in Embedded Real-Time Systems." In *2017 IEEE 15th International Conference on Industrial Informatics (INDIN)*. IEEE. [https://doi.org/10.1109/indin.2017.8104849][research_tabassam_2017]
- Tackett, Justin, and David Grimsman. 2024. "The Forward-Reverse Greedy Algorithm for Distributed Submodular Maximization." In *2024 IEEE 63rd Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc56724.2024.10886209][research_tackett_2024]
- Takana, Norimasa, and Yoshihiro Oyama. 2026. "Hikami: A Lightweight Hypervisor for Emulating RISC-V Extension Semantics with Sail-Driven Auto-Generation." In *Proceedings of the 27th ACM SIGPLAN/SIGBED International Conference on Languages, Compilers, and Tools for Embedded Systems*. ACM. [https://doi.org/10.1145/3814943.3816171][research_takana_2026]
- Talaat, Mohamed Gamal, Mostafa Hassan, Mohamed Sayed, Mohanad Mohamed, and Islam Ahmed. 2025. "GrammLLM: Grammar-Guided LLM Test Generation for Compiler Validation." In *2025 37th International Conference on Microelectronics (ICM)*. IEEE. [https://doi.org/10.1109/icm66518.2025.11322450][research_talaat_2025]
- Talamali, Ibtissem, Razika Lounas, and Mohamed Mezghiche. 2024. "Formal Specification and Verification of MQTT Protocol Using CoQ Proof Assistant." In *2024 International Conference on Advanced Aspects of Software Engineering (ICAASE)*. IEEE. [https://doi.org/10.1109/icaase64542.2024.10850926][research_talamali_2024]
- Tallada, Marc Gonzalez, Joel Denny, Pedro Valero-Lara, Seyong Lee, Keita Teranishi, and Jeffrey S. Vetter. 2024. "eCC++: A Compiler Construction Framework for Embedded Domain-Specific Languages." In *2024 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)*. IEEE. [https://doi.org/10.1109/ipdpsw63119.2024.00129][research_tallada_2024]
- Tambon, Florian, Vahid Majdinasab, Amin Nikanjam, Foutse Khomh, and Giuliano Antoniol. 2023. "Mutation Testing of Deep Reinforcement Learning Based on Real Faults." In *2023 IEEE Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst57152.2023.00026][research_tambon_2023]
- Tamura, Raiki, Daisuke Kotani, Kazuyuki Shudo, and Yasuo Okabe. 2025. "Bringing Together Cross-ISA Checkpoint/Restoration and AOT Compilation of WebAssembly Programs." In *Proceedings of the 22nd ACM SIGPLAN International Conference on Managed Programming Languages and Runtimes*. ACM. [https://doi.org/10.1145/3759426.3760985][research_tamura_2025]
- Tan, Allen Jason A., Sherry Joy Alvionne S. Baquiran, and Anastacia B. Alvarez. 2025b. "Optimizing TinyEngine for the RISC-V Vector Extension." In *2025 International Symposium on Multimedia and Communications Technology (ISMAC)*. IEEE. [https://doi.org/10.1109/ismac65024.2025.11175984][research_tan_2025]
- Tan, Yong Kiam, Marijn J. H. Heule, and Magnus O. Myreen. 2023b. "Verified Propagation Redundancy and Compositional UNSAT Checking in CakeML." *International Journal on Software Tools for Technology Transfer* 25 (2): 167–84. [https://doi.org/10.1007/s10009-022-00690-y][research_tan_2023]
- Tan, Yong Kiam, Magnus O. Myreen, Ramana Kumar, Anthony Fox, Scott Owens, and Michael Norrish. 2016. "A New Verified Compiler Backend for CakeML." *ACM SIGPLAN Notices* 51 (9): 60–73. [https://doi.org/10.1145/3022670.2951924][research_tan_2016]
- Tan, Yi, Jintai Wang, and Liang He. 2025a. "Data Valuation Method Based on Federated Learning and Shapley Value." In *2025 International Joint Conference on Neural Networks (IJCNN)*. IEEE. [https://doi.org/10.1109/ijcnn64981.2025.11229084][research_tan_2025_b]
- Tan, Jingjing, Dongmei Zhang, Hongyang Zhang, and Zhenning Zhang. 2022. "One-Pass Streaming Algorithm for DR-Submodular Maximization with a Knapsack Constraint over the Integer Lattice." *Computers and Electrical Engineering* 99: 107766. [https://doi.org/10.1016/j.compeleceng.2022.107766][research_tan_2022]
- Tang, Zhongzheng, Jingwen Chen, and Chenhao Wang. 2024. "Greedy+Singleton: An Efficient Approximation Algorithm for k-Submodular Knapsack Maximization." *Theoretical Computer Science* 984: 114320. [https://doi.org/10.1016/j.tcs.2023.114320][research_tang_2024]
- Tang, Xin, Yanzhe Lei, and Chao Li. 2025b. "Heterogeneous Graph Data Valuation: A Shapley Value-Based Approach." In *2025 40th Youth Academic Annual Conference of Chinese Association of Automation (YAC)*. IEEE. [https://doi.org/10.1109/yac66630.2025.11150137][research_tang_2025_b]
- Tang, Bowen, and Katsuhisa Maruyama. 2026. "A Large-Scale Investigation into the Loss of Pull Request Data on GitHub." *IEEE Access* 14: 6927–43. [https://doi.org/10.1109/access.2026.3652670][research_tang_2026]
- Tang, Yungang, Yulin Wan, and Jianzhong Li. 2026a. "Improving the Accuracy and Stability of Privacy-Aware Shapley Data Valuation." *Discover Applied Sciences* 8 (7): 750. [https://doi.org/10.1007/s42452-026-08711-0][research_tang_2026_b]
- Tang, Shaojie, and Jing Yuan. 2023. "Streaming Adaptive Submodular Maximization." *Theoretical Computer Science* 944: 113644. [https://doi.org/10.1016/j.tcs.2022.11.030][research_tang_2023]
- Tang, Yixuan, Junwei Zeng, Jingxuan Zhang, Weiwei Li, and Zhiqiu Huang. 2025a. "CTDip: A Diversity-Guided Test Program Synthesis Approach for Boosting Compiler Bug Detection." *Empirical Software Engineering* 30 (3): 88. [https://doi.org/10.1007/s10664-025-10642-0][research_tang_2025]
- Tao, Yida, and Sunghun Kim. 2015. "Partitioning Composite Code Changes to Facilitate Code Review." In *2015 IEEE/ACM 12th Working Conference on Mining Software Repositories*. IEEE. [https://doi.org/10.1109/msr.2015.24][research_tao_2015]
- Tengeri, David, Arpad Beszedes, Tamas Gergely, Laszlo Vidacs, David Havas, and Tibor Gyimothy. 2015. "Beyond Code Coverage — An Approach for Test Suite Assessment and Improvement." In *2015 IEEE Eighth International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw.2015.7107476][research_tengeri_2015]
- Tengeri, David, Laszlo Vidacs, Arpad Beszedes, et al. 2016. "Relating Code Coverage, Mutation Score and Test Suite Reducibility to Defect Density." In *2016 IEEE Ninth International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw.2016.25][research_tengeri_2016]
- Thiselton, Emillie, and Christoph Treude. 2019. "Enhancing Python Compiler Error Messages via Stack." In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2019.8870155][research_thiselton_2019]
- Thomas, Deepak-George, Matteo Biagiola, Nargiz Humbatova, et al. 2025. "µ PRL: A Mutation Testing Pipeline for Deep Reinforcement Learning Based on Real Faults." In *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse55347.2025.00036][research_thomas_2025]
- Thomas, Jay, Ehsan Salehi, Alex Lim, and Stephen Di Camillo. 2024. "Analyzing Data Flow and Control Flow of Multicore Software: A Solution for Efficient Worst-Case Execution Time Analysis." In *2024 AIAA DATC/IEEE 43rd Digital Avionics Systems Conference (DASC)*. IEEE. [https://doi.org/10.1109/dasc62030.2024.10749649][research_thomas_2024]
- Thorve, Swapna, Chandani Sreshtha, and Na Meng. 2018. "An Empirical Study of Flaky Tests in Android Apps." In *2018 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme.2018.00062][research_thorve_2018]
- Tian, Ruiqin, Luanzheng Guo, Jiajia Li, Bin Ren, and Gokcen Kestor. 2021. "A High Performance Sparse Tensor Algebra Compiler in MLIR." In *2021 IEEE/ACM 7th Workshop on the LLVM Compiler Infrastructure in HPC (LLVM-HPC)*. IEEE. [https://doi.org/10.1109/llvmhpc54804.2021.00009][research_tian_2021]
- Tian, Shilei, Joseph Huber, John Tramm, Barbara Chapman, and Johannes Doerfert. 2022. "Just-in-Time Compilation and Link-Time Optimization for OpenMP Target Offloading." In *OpenMP in a Modern World: From Multi-device Support to Meta Programming*. Springer International Publishing. [https://doi.org/10.1007/978-3-031-15922-0\_10][research_tian_2022]
- Tine, Blaise-Pascal, Sudhakar Yalamanchili, Hyesoon Kim, and Jeff Vetter. 2019. "POSTER: Tango: An Optimizing Compiler for Just-In-Time RTL Simulation." In *2019 28th International Conference on Parallel Architectures and Compilation Techniques (PACT)*. IEEE. [https://doi.org/10.1109/pact.2019.00055][research_tine_2019]
- Tiotto, Ettore, Víctor Pérez, Whitney Tsang, et al. 2024. "Experiences Building an MLIR-Based SYCL Compiler." In *2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo57630.2024.10444866][research_tiotto_2024]
- Tirichine, Mohammed, Nassim Ameur, Nazim Bendib, et al. 2026. "A Reinforcement Learning Environment for Automatic Code Optimization in the MLIR Compiler." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11394838][research_tirichine_2026]
- Titzer, Ben L. 2024. "Whose Baseline Compiler Is It Anyway?" In *2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo57630.2024.10444855][research_titzer_2024]
- Tofte, Mads, and Jean-Pierre Talpin. 1997. "Region-Based Memory Management." *Information and Computation* 132 (2): 109–76. [https://doi.org/10.1006/inco.1996.2613][research_tofte_talpin_1997]
- Toprak, Hannan, and Ruken Zilan. 2026. "Automating Software Documentation with n8n and Large Language Models: A GitHub and Jira to Confluence Case Study." In *2026 5th International Informatics and Software Engineering Conference (IISEC)*. IEEE. [https://doi.org/10.1109/iisec69317.2026.11418473][research_toprak_2026]
- Trippel, Caroline. 2025. "Specification and Formal Verification of Hardware–Software Contracts for High-Assurance Computer Architectures." *Computer* 58 (8): 86–91. [https://doi.org/10.1109/mc.2025.3573841][research_trippel_2025]
- Troiber, Martin, Martin Schulz, Blaise Tine, and Hyesoon Kim. 2025. "Analysis of the RISC-V Vector Extension for Vulkan Graphics Kernels." In *2025 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)*. IEEE. [https://doi.org/10.1109/ispass64960.2025.00053][research_troiber_2025]
- Truong, Jacob, Van Nguyen, and Thanh Thi Nguyen. 2026. "An Overview of Evaluation and Enhancement Methods for Code Generation by Large Language Models." *Information and Software Technology* 197: 108185. [https://doi.org/10.1016/j.infsof.2026.108185][research_truong_2026]
- Tsai, Chung-Hsuan, Shi-Chun Tsai, and Shih-Kun Huang. 2021. "REST API Fuzzing by Coverage Level Guided Blackbox Testing." In *2021 IEEE 21st International Conference on Software Quality, Reliability and Security (QRS)*. IEEE. [https://doi.org/10.1109/qrs54544.2021.00040][research_tsai_2021]
- Tsoeunyane, Lekhobola, Simon Winberg, and Michael Inggs. 2018. "Automatic Configurable Hardware Code Generation for Software-Defined Radios." *Computers* 7 (4): 53. [https://doi.org/10.3390/computers7040053][research_tsoeunyane_2018]
- Tsoukalas, Dimitrios, Miltiadis Siavvas, Dionysios Kehagias, Apostolos Ampatzoglou, and Alexander Chatzigeorgiou. 2023. "A Practical Approach for Technical Debt Prioritization Based on Class-Level Forecasting." *Journal of Software: Evolution and Process* 36 (4): e2564. [https://doi.org/10.1002/smr.2564][research_tsoukalas_2023]
- Tsoupidi, Rodothea Myrsini, Musard Balliu, and Benoit Baudry. 2021. "Vivienne: Relational Verification of Cryptographic Implementations in WebAssembly." In *2021 IEEE Secure Development Conference (SecDev)*. IEEE. [https://doi.org/10.1109/secdev51306.2021.00029][research_tsoupidi_2021]
- Tu, Haoxin, He Jiang, Xiaochen Li, Zhilei Ren, Zhide Zhou, and Lingxiao Jiang. 2022. "Remgen: Remanufacturing a Random Program Generator for Compiler Testing." In *2022 IEEE 33rd International Symposium on Software Reliability Engineering (ISSRE)*. IEEE. [https://doi.org/10.1109/issre55969.2022.00057][research_tu_2022]
- Tu, Huy, and Tim Menzies. 2022. "DebtFree: Minimizing Labeling Cost in Self-Admitted Technical Debt Identification Using Semi-Supervised Learning." *Empirical Software Engineering* 27 (4): 80. [https://doi.org/10.1007/s10664-022-10121-w][research_tu_2022_b]
- Uchoa, Anderson, Caio Barbosa, Daniel Coutinho, et al. 2021. "Predicting Design Impactful Changes in Modern Code Review: A Large-Scale Empirical Study." In *2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr52588.2021.00059][research_uchoa_2021]
- Undheim, Trond Arne. 2026. "CREF-Lang: A Domain-Specific Language and Compiler for Cross-Domain Cascade-Risk Notation." *SoftwareX* 35: 102861. [https://doi.org/10.1016/j.softx.2026.102861][research_undheim_2026]
- Urban, Caterina, Pavle Subotić, and Filip Drobnjaković. 2025. "Static Analysis by Abstract Interpretation against Data Leakage in Machine Learning." *Science of Computer Programming* 246: 103338. [https://doi.org/10.1016/j.scico.2025.103338][research_urban_2025]
- Urbanek, Tomas, Zdenka Prokopova, Radek Silhavy, and Veronika Vesela. 2015. "Prediction Accuracy Measurements as a Fitness Function for Software Effort Estimation." *SpringerPlus* 4 (1): 778. [https://doi.org/10.1186/s40064-015-1555-9][research_urbanek_2015]
- Vaas, Steffen, Marc Reichenbach, and Dietmar Fey. 2016. "An Application-Specific Instruction Set Processor for Power Quality Monitoring." In *2016 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)*. IEEE. [https://doi.org/10.1109/ipdpsw.2016.143][research_vaas_2016]
- Vahabzadeh, Arash, Amin Milani Fard, and Ali Mesbah. 2015. "An Empirical Study of Bugs in Test Code." In *2015 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsm.2015.7332456][research_vahabzadeh_2015]
- Vahedifar, Mohammad Ali, Azim Akhtarshenas, Mohammad M. RafatPanah, and Maryam Sabbaghian. 2025. "Shapley-Based Data Valuation with Mutual Information: A Key to Modified K-Nearest Neighbors." In *2025 IEEE 35th International Workshop on Machine Learning for Signal Processing (MLSP)*. IEEE. [https://doi.org/10.1109/mlsp62443.2025.11204262][research_vahedifar_2025]
- van Dam, Tim, Maliheh Izadi, and Arie van Deursen. 2023. "Enriching Source Code with Contextual Data for Code Completion Models: An Empirical Study." In *2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr59073.2023.00035][research_vandam_2023]
- Vendome, Christopher. 2015. "A Large Scale Study of License Usage on GitHub." In *2015 IEEE/ACM 37th IEEE International Conference on Software Engineering*. IEEE. [https://doi.org/10.1109/icse.2015.245][research_vendome_2015]
- Vendome, Christopher, Gabriele Bavota, Massimiliano Di Penta, Mario Linares-Vásquez, Daniel German, and Denys Poshyvanyk. 2016. "License Usage and Changes: A Large-Scale Study on gitHub." *Empirical Software Engineering* 22 (3): 1537–77. [https://doi.org/10.1007/s10664-016-9438-4][research_vendome_2016]
- Vendome, Christopher, Mario Linares-Vasquez, Gabriele Bavota, Massimiliano Di Penta, Daniel German, and Denys Poshyvanyk. 2015. "License Usage and Changes: A Large-Scale Study of Java Projects on GitHub." In *2015 IEEE 23rd International Conference on Program Comprehension*. IEEE. [https://doi.org/10.1109/icpc.2015.32][research_vendome_2015_b]
- Venkat, Sruthi, and Preet Kanwal. 2018. "COpt: A High Level Domain-Specific Language to Generate Compiler Optimizers." In *2018 International Conference on Advanced Computation and Telecommunication (ICACAT)*. IEEE. [https://doi.org/10.1109/icacat.2018.8933593][research_venkat_2018]
- Ventovaara, Marcus, Arman Hasanbegovic, Jimmie Wiklandert, and Saad Mubeen. 2020. "Worst-Case Execution Time Estimation of Legacy Vehicular Embedded Functions: An Industrial Case Study." In *2020 IEEE International Conference on Industrial Technology (ICIT)*. IEEE. [https://doi.org/10.1109/icit45562.2020.9067160][research_ventovaara_2020]
- Vescan, Andreea, Radu Găceanu, and Arnold Szederjesi-Dragomir. 2023. "Neural Network-Based Test Case Prioritization in Continuous Integration." In *2023 38th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW)*. IEEE. [https://doi.org/10.1109/asew60602.2023.00014][research_vescan_2023]
- Vescan, Andreea, Adrian Pintea, Lukas Linsbauer, and Alexander Egyed. 2021. "Genetic Programming for Feature Model Synthesis: A Replication Study." *Empirical Software Engineering* 26 (4): 58. [https://doi.org/10.1007/s10664-021-09947-7][research_vescan_2021]
- Vetro, Antonio, Wolfgang Bohm, and Marco Torchiano. 2015. "On the Benefits and Barriers When Adopting Software Modelling and Model Driven Techniques: An External, Differentiated Replication." In *2015 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem.2015.7321210][research_vetro_2015]
- Vidacs, Laszlo, Ferenc Horvath, David Tengeri, and Arpad Beszedes. 2016. "Assessing the Test Suite of a Large System Based on Code Coverage, Efficiency and Uniqueness." In *2016 IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner.2016.69][research_vidacs_2016]
- Wallentowitz, Stefan, Bastian Kersting, and Dan Mihai Dumitriu. 2022. "Potential of WebAssembly for Embedded Systems." In *2022 11th Mediterranean Conference on Embedded Computing (MECO)*. IEEE. [https://doi.org/10.1109/meco55406.2022.9797106][research_wallentowitz_2022]
- Walshe, Thomas, and Andrew Simpson. 2020. "An Empirical Study of Bug Bounty Programs." In *2020 IEEE 2nd International Workshop on Intelligent Bug Fixing (IBF)*. IEEE. [https://doi.org/10.1109/ibf50092.2020.9034828][research_walshe_2020]
- Wan, Zhiyuan, David Lo, Xin Xia, and Liang Cai. 2017. "Bug Characteristics in Blockchain Systems: A Large-Scale Empirical Study." In *2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR)*. IEEE. [https://doi.org/10.1109/msr.2017.59][research_wan_2017]
- Wang, Haoyu. 2021. "Compression Optimization for Automatic Verification of Network Configuration." In *2021 6th International Conference on Intelligent Computing and Signal Processing (ICSP)*. IEEE. [https://doi.org/10.1109/icsp51882.2021.9408924][research_wang_2021]
- Wang, Zheer. 2024a. "Advancements and Challenges of Large Language Model-Based Code Generation and Completion." In *Proceedings of the 1st International Conference on Modern Logistics and Supply Chain Management*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0013271800004558][research_wang_2024_d]
- Wang, Haoyu, Junjie Chen, Chuyue Xie, et al. 2023c. "MLIRSmith: Random Program Generation for Fuzzing MLIR Compiler Infrastructure." In *2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE)*. IEEE. [https://doi.org/10.1109/ase56229.2023.00120][research_wang_2023_b]
- Wang, Wenbin, and Gan Cui. 2026. "A Shapley-Value Cooperative Game-Based Risk Decision Model for Natural Gas Pipeline Vulnerability." *Reliability Engineering & System Safety* 275: 112886. [https://doi.org/10.1016/j.ress.2026.112886][research_wang_2026]
- Wang, Xiangwei, Xinning Hui, Chunhua Liao, and Xipeng Shen. 2025b. "Reductive Analysis with Compiler-Guided Large Language Models for Input-Centric Code Optimizations." *Proceedings of the ACM on Programming Languages* 9 (PLDI): 797–821. [https://doi.org/10.1145/3729282][research_wang_2025_d]
- Wang, Qian, and Ralf Jung. 2024. "Rustlantis: Randomized Differential Testing of the Rust Compiler." *Proceedings of the ACM on Programming Languages* 8 (OOPSLA2): 1955–81. [https://doi.org/10.1145/3689780][research_wang_2024_b]
- Wang, Xinyu, and Tris Kee. 2025. "Integrating Shapley Value and Least Core Attribution for Robust Explainable AI in Rent Prediction." *Buildings* 15 (17): 3133. [https://doi.org/10.3390/buildings15173133][research_wang_2025_b]
- Wang, Liu, Ruiqing Li, Jiaxin Zhu, Guangdong Bai, and Haoyu Wang. 2021. "A Large-Scale Empirical Study of COVID-19 Themed GitHub Repositories." In *2021 IEEE 45th Annual Computers, Software, and Applications Conference (COMPSAC)*. IEEE. [https://doi.org/10.1109/compsac51774.2021.00124][research_wang_2021_b]
- Wang, Ye, Na Meng, and Hao Zhong. 2018a. "An Empirical Study of Multi-Entity Changes in Real Bug Fixes." In *2018 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme.2018.00038][research_wang_2018]
- Wang, Zheng, and Michael O'Boyle. 2018. "Machine Learning in Compiler Optimization." *Proceedings of the IEEE* 106 (11): 1879–1901. [https://doi.org/10.1109/jproc.2018.2817118][research_wang_2018_c]
- Wang, Jianlin, Chao Peng, and Zhenbing Zeng. 2020. "A Formal Proof of the Soundness of the Hybrid CPS Clock Theory." In *2020 International Symposium on Theoretical Aspects of Software Engineering (TASE)*. IEEE. [https://doi.org/10.1109/tase49443.2020.00022][research_wang_2020]
- Wang, Yi, Youhua Shi, Chao Wang, and Yajun Ha. 2015. "FPGA-Based SHA-3 Acceleration on a 32-Bit Processor via Instruction Set Extension." In *2015 IEEE International Conference on Electron Devices and Solid-State Circuits (EDSSC)*. IEEE. [https://doi.org/10.1109/edssc.2015.7285111][research_wang_2015]
- Wang, Xingxin, Shibo Tang, and Wei Hu. 2022b. "Towards Automatic Property Generation for SoC Security Verification." In *2022 19th International SoC Design Conference (ISOCC)*. IEEE. [https://doi.org/10.1109/isocc56007.2022.10031448][research_wang_2022]
- Wang, Huanting, Zhanyong Tang, Cheng Zhang, et al. 2022a. "Automating Reinforcement Learning Architecture Design for Code Optimization." In *Proceedings of the 31st ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3497776.3517769][research_wang_2022_b]
- Wang, Zihao, Pei Wang, Qinkun Bao, and Dinghao Wu. 2023d. "Source Code Implied Language Structure Abstraction through Backward Taint Analysis." In *Proceedings of the 18th International Conference on Software Technologies*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0012129000003538][research_wang_2023_c]
- Wang, Dingbang, Yu Zhao, Lu Xiao, and Tingting Yu. 2023b. "An Empirical Study of Regression Testing for Android Apps in Continuous Integration Environment." In *2023 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. IEEE. [https://doi.org/10.1109/esem56168.2023.10304799][research_wang_2023_d]
- Wang, Da, and YingXue Zhou. 2024. "An Innovative Machine Learning Workflow to Research China’s Systemic Financial Crisis with SHAP Value and Shapley Regression." *Financial Innovation* 10 (1): 103. [https://doi.org/10.1186/s40854-023-00574-3][research_wang_2024_c]
- Wang, Yue, Zhide Zhou, Zhilei Ren, Dong Liu, and He Jiang. 2023a. "A Comprehensive Study of WebAssembly Runtime Bugs." In *2023 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner56733.2023.00041][research_wang_2023]
- WanXin, Shang, Wu Tao, Yang Fei, Chen Xi, Chen JingJue, and Yu ZhenXia. 2022. "CUDA Acceleration of Worst-Case Execution Time Analysis Based on Model Checking." In *2022 Tenth International Conference on Advanced Cloud and Big Data (CBD)*. IEEE. [https://doi.org/10.1109/cbd58033.2022.00044][research_wanxin_2022]
- Webb, Brae J., Ian J. Hayes, and Mark Utting. 2023. "Verifying Term Graph Optimizations Using Isabelle/HOL." In *Proceedings of the 12th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3573105.3575673][research_webb_2023]
- Wei, Xiaoyang, Zhengdi Wang, and Shuangyuan Yang. 2023. "An Automatic Generation and Verification Method of Software Requirements Specification." *Electronics* 12 (12): 2734. [https://doi.org/10.3390/electronics12122734][research_wei_2023]
- Weingarten, Lennart, Kamalika Datta, and Rolf Drechsler. 2025. "ForMAt: Formal Verification of Scalable Multiply and Accumulate Units." In *2025 Forum on Specification & Design Languages (FDL)*. IEEE. [https://doi.org/10.1109/fdl68117.2025.11165398][research_weingarten_2025]
- Weissnegger, Ralph, Markus Pistauer, Christian Kreiner, Markus Schuß, Kay Römer, and Christian Steger. 2016. "Automatic Testbench Generation for Simulation-Based Verification of Safety-Critical Systems in UML." In *Proceedings of the 6th International Joint Conference on Pervasive and Embedded Computing and Communication Systems*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0005997700700075][research_weissnegger_2016]
- Wen, Elliott, and Jens Dietrich. 2023. "WasmSlim: Optimizing WebAssembly Binary Distribution via Automatic Module Splitting." In *2023 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)*. IEEE. [https://doi.org/10.1109/saner56733.2023.00069][research_wen_2023]
- Wen, Shasha, Xu Liu, and Milind Chabbi. 2015. "Runtime Value Numbering: A Profiling Technique to Pinpoint Redundant Computations." In *2015 International Conference on Parallel Architecture and Compilation (PACT)*. IEEE. [https://doi.org/10.1109/pact.2015.29][research_wen_2015]
- Widyasari, Ratnadira, Gede Artha Azriadi Prana, Stefanus Agus Haryono, Shaowei Wang, and David Lo. 2022. "Real World Projects, Real Faults: Evaluating Spectrum Based Fault Localization Techniques on Python Projects." *Empirical Software Engineering* 27 (6): 147. [https://doi.org/10.1007/s10664-022-10189-4][research_widyasari_2022]
- Wilson, Edwin B. 1927. "Probable Inference, the Law of Succession, and Statistical Inference." *Journal of the American Statistical Association* 22 (158): 209–12. [https://doi.org/10.1080/01621459.1927.10502953][research_wilson_1927]
- Windsor, Matt, Alastair F. Donaldson, and John Wickerson. 2022. "High-Coverage Metamorphic Testing of Concurrency Support in C Compilers." *Software Testing, Verification and Reliability* 32 (4): e1812. [https://doi.org/10.1002/stvr.1812][research_windsor_2022]
- Wipfli, Max, Gamze İslamoğlu, Navaneeth Kunhi Purayil, Angelo Garofalo, and Luca Benini. 2026. "Vmxdotp: A RISC-V Vector ISA Extension for Efficient Microscaling (MX) Format Acceleration." In *2026 Design, Automation & Test in Europe Conference (DATE)*. IEEE. [https://doi.org/10.23919/date69613.2026.11539385][research_wipfli_2026]
- Wu, Yin, Jiayi Ban, Songling Li, Zhen Zhang, Yonglun Huang, and Shidi Ruan. 2025b. "Intelligent Power Grid Startup Scheme Based on Rule Reasoning and System Compilation." In *2025 IEEE Madhya Pradesh Section Conference (MPCON)*. IEEE. [https://doi.org/10.1109/mpcon66082.2025.11256702][research_wu_2025_c]
- Wu, Mingyuan, Minghai Lu, Heming Cui, Junjie Chen, Yuqun Zhang, and Lingming Zhang. 2023. "JITfuzz: Coverage-Guided Fuzzing for JVM Just-in-Time Compilers." In *2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse48619.2023.00017][research_wu_2023]
- Wu, Jiang, Xiankai Meng, Jianjun Xu, and Haoyu Zhang. 2020b. "Reliable Compilation Optimization Phase-Ordering Exploration with Reinforcement Learning." In *2020 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*. IEEE. [https://doi.org/10.1109/smc42975.2020.9283132][research_wu_2020_b]
- Wu, Qinqin, Yaoxin Pan, Famao Mei, and Mingxin Lu. 2024a. "Efficient Shapley Value Driven Federated Learning System for Smart Grid." In *2024 IEEE 6th International Conference on Power, Intelligent Computing and Systems (ICPICS)*. IEEE. [https://doi.org/10.1109/icpics62053.2024.10796417][research_wu_2024_b]
- Wu, Huifeng, Yi Yan, Danfeng Sun, and Rene Simon. 2019a. "A Customized Real-Time Compilation for Motion Control in Embedded PLCs." *IEEE Transactions on Industrial Informatics* 15 (2): 812–21. [https://doi.org/10.1109/tii.2018.2826140][research_wu_2019]
- Wu, Yiwen, Yang Zhang, Tao Wang, and Huaimin Wang. 2020a. "Dockerfile Changes in Practice: A Large-Scale Empirical Study of 4,110 Projects on GitHub." In *2020 27th Asia-Pacific Software Engineering Conference (APSEC)*. IEEE. [https://doi.org/10.1109/apsec51365.2020.00033][research_wu_2020]
- Xavier, Laerte, João Eduardo Montandon, Fabio Ferreira, Rodrigo Brito, and Marco Tulio Valente. 2022. "On the Documentation of Self-Admitted Technical Debt in Issues." *Empirical Software Engineering* 27 (7): 163. [https://doi.org/10.1007/s10664-022-10203-9][research_xavier_2022]
- Xia, Jing, and Yanhui Li. 2017. "Could We Predict the Result of a Continuous Integration Build? An Empirical Study." In *2017 IEEE International Conference on Software Quality, Reliability and Security Companion (QRS-C)*. IEEE. [https://doi.org/10.1109/qrs-c.2017.59][research_xia_2017_b]
- Xia, Jing, Yanhui Li, and Chuanqi Wang. 2017. "An Empirical Study on the Cross-Project Predictability of Continuous Integration Outcomes." In *2017 14th Web Information Systems and Applications Conference (WISA)*. IEEE. [https://doi.org/10.1109/wisa.2017.53][research_xia_2017]
- Xia, Chunqiu Steven, Yuxiang Wei, and Lingming Zhang. 2023. "Automated Program Repair in the Era of Large Pre-Trained Language Models." In *2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse48619.2023.00129][research_xia_2023]
- Xiao, Tao, Zhili Zeng, Dong Wang, Hideaki Hata, Shane McIntosh, and Kenichi Matsumoto. 2024. "Quantifying and Characterizing Clones of Self-Admitted Technical Debt in Build Systems." *Empirical Software Engineering* 29 (2): 54. [https://doi.org/10.1007/s10664-024-10449-5][research_xiao_2024]
- Xie, Shanshan, Wenxiu Hu, Jiaxing Duan, and Zuhui Xia. 2026. "Dynamic Valuation of Data Assets via Multi-Agent Reinforcement Learning and Shapley Value." *Information Processing & Management* 63 (8): 104943. [https://doi.org/10.1016/j.ipm.2026.104943][research_xie_2026]
- Xie, Yuchong, and Dongdong She. 2025. "HFuzz: Havoc Mode Guided Fuzzing." In *2025 IEEE/ACM International Workshop on Search-Based and Fuzz Testing (SBFT)*. IEEE. [https://doi.org/10.1109/sbft66712.2025.00018][research_xie_2025]
- Xie, Weiqiang, Xiao Yu, Yuqing Zhang, and He Wang. 2020. "An Improved Shapley Value Benefit Distribution Mechanism in Cooperative Game of Cyber Threat Intelligence Sharing." In *IEEE INFOCOM 2020 - IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS)*. IEEE. [https://doi.org/10.1109/infocomwkshps50562.2020.9162739][research_xie_2020]
- Xu, Dianxiang, Omar El Ariss, Yunkai Liu, and Abdulrahman Alatawi. 2017. "Statistical Unigram Analysis for Source Code Repository." In *2017 IEEE Third International Conference on Multimedia Big Data (BigMM)*. IEEE. [https://doi.org/10.1109/bigmm.2017.13][research_xu_2017]
- Xu, Caixu, Hui Guo, Caicun Cen, Minglang Chen, Xiongjie Tao, and Jie He. 2025. "Efficient Program Optimization through Knowledge-Enhanced LoRA Fine-Tuning of Large Language Models." *Journal of Supercomputing* 81 (8): 1006. [https://doi.org/10.1007/s11227-025-07378-5][research_xu_2025]
- Xu, Zirui, and Vasileios Tzoumas. 2022. "Resource-Aware Distributed Submodular Maximization: A Paradigm for Multi-Robot Decision-Making." In *2022 IEEE 61st Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc51059.2022.9993308][research_xu_2022_b]
- Xu, Wenzheng, He Xue, Jing Li, et al. 2024a. "Approximation Algorithm for Connected Submodular Function Maximization Problems." In *2024 IEEE 44th International Conference on Distributed Computing Systems (ICDCS)*. IEEE. [https://doi.org/10.1109/icdcs60910.2024.00106][research_xu_2024]
- Xu, Kangwei, Grace Li Zhang, Xunzhao Yin, Cheng Zhuo, Ulf Schlichtmann, and Bing Li. 2024b. "Automated C/C++ Program Repair for High-Level Synthesis via Large Language Models." In *2024 ACM/IEEE 6th Symposium on Machine Learning for CAD (MLCAD)*. IEEE. [https://doi.org/10.1109/mlcad62225.2024.10740262][research_xu_2024_b]
- Yadav, Rohan, Alex Aiken, and Fredrik Kjolstad. 2022. "DISTAL: The Distributed Tensor Algebra Compiler." In *Proceedings of the 43rd ACM SIGPLAN International Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3519939.3523437][research_yadav_2022]
- Yang, Yixiao. 2023a. "Improve Model Testing by Integrating Bounded Model Checking and Coverage Guided Fuzzing." *Electronics* 12 (7): 1573. [https://doi.org/10.3390/electronics12071573][research_yang_2023]
- Yang, Yixiao. 2023b. "Improving Code Completion by Solving Data Inconsistencies in the Source Code with a Hierarchical Language Model." *Electronics* 12 (7): 1576. [https://doi.org/10.3390/electronics12071576][research_yang_2023_c]
- Yang, Chang. 2026. "A Calculus for Web Services Choreography: Formal Semantics, Projection, and Correctness." In *2026 5th Asia Conference on Algorithms, Computing and Machine Learning (CACML)*. IEEE. [https://doi.org/10.1109/cacml68972.2026.11507087][research_yang_2026]
- Yang, Zhibin, Jean-Paul Bodeveix, Mamoun Filali, Kai Hu, Yongwang Zhao, and Dianfu Ma. 2015. "Towards a Verified Compiler Prototype for the Synchronous Language SIGNAL." *Frontiers of Computer Science* 10 (1): 37–53. [https://doi.org/10.1007/s11704-015-4364-y][research_yang_2015]
- Yang, Xuejun, Yang Chen, Eric Eide, and John Regehr. 2011. "Finding and Understanding Bugs in C Compilers." In *Proceedings of the 32nd ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/1993498.1993532][research_yang_2011]
- Yang, Chenyuan, Yinlin Deng, Runyu Lu, et al. 2024c. "WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models." *Proceedings of the ACM on Programming Languages* 8 (OOPSLA2): 709–35. [https://doi.org/10.1145/3689736][research_yang_2024_e]
- Yang, Aidan Z. H., Sophia Kolak, Vincent Hellendoorn, Ruben Martins, and Claire Le Goues. 2025b. "Revisiting Unnaturalness for Automated Program Repair in the Era of Large Language Models." In *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*. IEEE. [https://doi.org/10.1109/icse55347.2025.00089][research_yang_2025_b]
- Yang, Heechan, Ahcheong Lee, Kyutae Cho, and Yunsam Kim. 2026. "Industrial Application of Deep Learning Based Fault Localization with Mutation Features." In *2026 IEEE International Conference on Software Testing, Verification and Validation (ICST)*. IEEE. [https://doi.org/10.1109/icst69053.2026.00032][research_yang_2026_b]
- Yang, Yuting, Rui Wang, Youchen Wang, Xu Miao, Bing Liu, and Shan Jiang. 2022b. "Simulink Model Static Analysis Results Based on Abstract Interpretation." In *2022 9th International Conference on Dependable Systems and Their Applications (DSA)*. IEEE. [https://doi.org/10.1109/dsa56465.2022.00087][research_yang_2022]
- Yang, Ruiqi, Dachuan Xu, Yukun Cheng, Chuangen Gao, and Ding-Zhu Du. 2019. "Streaming Submodular Maximization under Noises." In *2019 IEEE 39th International Conference on Distributed Computing Systems (ICDCS)*. IEEE. [https://doi.org/10.1109/icdcs.2019.00042][research_yang_2019]
- Yang, Ruiqi, Dachuan Xu, Yukun Cheng, Yishui Wang, and Dongmei Zhang. 2021. "Streaming Algorithms for Robust Submodular Maximization." *Discrete Applied Mathematics* 290: 112–22. [https://doi.org/10.1016/j.dam.2020.05.001][research_yang_2021]
- Yang, Ruiqi, Dachuan Xu, Longkun Guo, and Dongmei Zhang. 2020. "Sequence Submodular Maximization Meets Streaming." *Journal of Combinatorial Optimization* 41 (1): 43–55. [https://doi.org/10.1007/s10878-020-00662-5][research_yang_2020]
- Yang, Ruiqi, Dachuan Xu, Longkun Guo, and Dongmei Zhang. 2022a. "Regularized Two-Stage Submodular Maximization under Streaming." *Science China Information Sciences* 65 (4): 140602. [https://doi.org/10.1007/s11432-020-3420-9][research_yang_2022_b]
- Yang, Sichao, and Ye Yang. 2024. "FormalEval: A Method for Automatic Evaluation of Code Generation via Large Language Models." In *2024 2nd International Symposium of Electronics Design Automation (ISEDA)*. IEEE. [https://doi.org/10.1109/iseda62518.2024.10617643][research_yang_2024_d]
- Yang, Conghui, Lei Yu, Huafeng Su, and Xiang Zhou. 2025a. "APICoder: A Multi-Role Large Language Model Framework for API Service Call Code Generation." In *2025 IEEE International Conference on Web Services (ICWS)*. IEEE. [https://doi.org/10.1109/icws67624.2025.00109][research_yang_2025]
- Yang, Peixin, Ziyao Zeng, Lin Zhu, et al. 2024a. "Bug Numbers Matter: An Empirical Study of Effort-Aware Defect Prediction Using Class Labels versus Bug Numbers." *Software: Practice and Experience* 55 (1): 49–78. [https://doi.org/10.1002/spe.3363][research_yang_2024]
- Yao, Jinyang, Xinyan Duan, He Wang, et al. 2026. "Evaluation and Benefit Modeling of Auto-Vectorization Cost Models for RISC-V RVV." In *2026 5th International Conference on Electronics, Integrated Circuits and Communication Technology (EICCT)*. IEEE. [https://doi.org/10.1109/eicct69950.2026.11564611][research_yao_2026]
- Yaraghi, Ahmadreza Saboor, Mojtaba Bagherzadeh, Nafiseh Kahani, and Lionel C. Briand. 2023. "Scalable and Accurate Test Case Prioritization in Continuous Integration Contexts." *IEEE Transactions on Software Engineering* 49 (4): 1615–39. [https://doi.org/10.1109/tse.2022.3184842][research_yaraghi_2023]
- Ye, Qianchuan, and Benjamin Delaware. 2019. "A Verified Protocol Buffer Compiler." In *Proceedings of the 8th ACM SIGPLAN International Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/3293880.3294105][research_ye_2019]
- Ye, Lintao, Bin Du, and Zhi-Wei Liu. 2025. "Offline and Online Distributed Submodular Maximization under a Partitioned Matroid Constraint." In *2025 IEEE 64th Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc57313.2025.11312887][research_ye_2025]
- Ye, Hanchen, Cong Hao, Jianyi Cheng, et al. 2022. "ScaleHLS: A New Scalable High-Level Synthesis Framework on Multi-Level Intermediate Representation." In *2022 IEEE International Symposium on High-Performance Computer Architecture (HPCA)*. IEEE. [https://doi.org/10.1109/hpca53966.2022.00060][research_ye_2022]
- Ye, Zhentao, Ruyi Ji, Yingfei Xiong, and Xin Zhang. 2026. "Accelerating Syntax-Guided Program Synthesis by Optimizing Domain-Specific Languages." *Proceedings of the ACM on Programming Languages* 10 (POPL): 1066–93. [https://doi.org/10.1145/3776679][research_ye_2026]
- Ye, Lintao, and Shreyas Sundaram. 2020. "Distributed Maximization of Submodular and Approximately Submodular Functions." In *2020 59th IEEE Conference on Decision and Control (CDC)*. IEEE. [https://doi.org/10.1109/cdc42340.2020.9304492][research_ye_2020]
- Yi, Zijian, Cheng Ding, August Shi, and Milos Gligoric. 2026. "Understanding and Finding JIT Compiler Performance Bugs." *Proceedings of the ACM on Programming Languages* 10 (OOPSLA1): 1237–65. [https://doi.org/10.1145/3798245][research_yi_2026]
- Yi, Gaolei, Xinyi Wang, and Yichen Wang. 2020. "An Empirical Study of Counterexample-Guided Fuzzing for Neural Networks Verification." In *2020 7th International Conference on Dependable Systems and Their Applications (DSA)*. IEEE. [https://doi.org/10.1109/dsa51864.2020.00022][research_yi_2020]
- Yi, Qiuping, Yifan Yu, and Guowei Yang. 2024. "Compatible Branch Coverage Driven Symbolic Execution for Efficient Bug Finding." *Proceedings of the ACM on Programming Languages* 8 (PLDI): 1633–55. [https://doi.org/10.1145/3656443][research_yi_2024]
- Yildiz, Abdullah, Deniz Iskender, Gulce Ozlu, H. Fatih Ugurdag, Baris Aktemur, and Sezer Goren. 2019. "Software UART: A Use Case for VSCPU Worst-Case Execution Time Analyzer." In *2019 4th International Conference on Computer Science and Engineering (UBMK)*. IEEE. [https://doi.org/10.1109/ubmk.2019.8907220][research_yildiz_2019]
- Ying, Zhihao, Dave Towey, Anthony Bellotti, Caslon Chua, and Zhi Quan Zhou. 2025. "Metamorphic Relation Patterns for Metamorphic Testing, Exploration and Robustness." *Software Testing, Verification and Reliability* 35 (2): e70003. [https://doi.org/10.1002/stvr.70003][research_ying_2025]
- Yingzhe, Liu. 2026. "Academic English Writing Generation-Evaluation Closed-Loop System Driven by Large Language Model: Adversarial Training and Cognitive Logic Verification." *Natural Language Processing Journal* 16: 100215. [https://doi.org/10.1016/j.nlp.2026.100215][research_yingzhe_2026]
- Yli-Huumo, Jesse, Andrey Maglyas, and Kari Smolander. 2016. "How Do Software Development Teams Manage Technical Debt? – an Empirical Study." *Journal of Systems and Software* 120: 195–218. [https://doi.org/10.1016/j.jss.2016.05.018][research_ylihuumo_2016]
- Yoo, S., and M. Harman. 2012. "Regression Testing Minimization, Selection and Prioritization: A Survey." *Software Testing, Verification and Reliability* 22 (2): 67–120. [https://doi.org/10.1002/stvr.430][research_yoo_harman_2012]
- Yoon, Seongho, and Jin-Young Choi. 2025. "Formal Specification and Verification of Smart Contract-Based Loan Management System Using TLA+." *IEEE Access* 13: 62060–70. [https://doi.org/10.1109/access.2025.3558081][research_yoon_2025]
- Young, H. P. 1985. "Monotonic Solutions of Cooperative Games." *International Journal of Game Theory* 14 (2): 65–72. [https://doi.org/10.1007/bf01769885][research_young_1985]
- Yousofvand, Leila, Seyfollah Soleimani, Vahid Rafe, and Sajad Esfandyari. 2024. "Automatic Program Bug Fixing by Focusing on Finding the Shortest Sequence of Changes." *Artificial Intelligence Review* 57 (2): 39. [https://doi.org/10.1007/s10462-023-10686-y][research_yousofvand_2024]
- Yu, Liang, Emil Alégroth, Panagiota Chatzipetrou, and Tony Gorschek. 2023. "Automated NFR Testing in Continuous Integration Environments: A Multi-Case Study of Nordic Companies." *Empirical Software Engineering* 28 (6): 144. [https://doi.org/10.1007/s10664-023-10356-1][research_yu_2023]
- Yu, Tianyi, Omar Ragheb, Stephen Wicklund, and Jason Anderson. 2024a. "MLIR-to-CGRA: A Versatile MLIR-Based Compiler Framework for CGRAs." In *2024 IEEE 35th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*. IEEE. [https://doi.org/10.1109/asap61560.2024.00045][research_yu_2024_b]
- Yu, Xinglong, Yi Sun, Yifan Zhao, Honglin Kuang, and Jun Han. 2024b. "RVCE-FAL: A RISC-V Scalar-Vector Custom Extension for Faster FALCON Digital Signature." In *2024 Design, Automation & Test in Europe Conference & Exhibition (DATE)*. IEEE. [https://doi.org/10.23919/date58400.2024.10546713][research_yu_2024]
- Yu, Chak Shun, Christoph Treude, and Mauricio Aniche. 2019. "Comprehending Test Code: An Empirical Study." In *2019 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme.2019.00084][research_yu_2019]
- Yuan, Jun, Qiang Zhao, Wei Wang, Xiangsheng Meng, Jun Li, and Qin Li. 2022. "Audio Denoising Coprocessor Based on RISC-V Custom Instruction Set Extension." *Acoustics* 4 (3): 538–53. [https://doi.org/10.3390/acoustics4030033][research_yuan_2022]
- Zachariaova, Marcela, Michaela Kekelyova-Beleova, and Zdenek Kotasek. 2016. "Regression Test Suites Optimization for Application-Specific Instruction-Set Processors and Their Use for Dependability Analysis." In *2016 Euromicro Conference on Digital System Design (DSD)*. IEEE. [https://doi.org/10.1109/dsd.2016.50][research_zachariaova_2016]
- Zacharopoulos, Georgios, Lorenzo Ferretti, Giovanni Ansaloni, Giuseppe Di Guglielmo, Luca Carloni, and Laura Pozzi. 2019. "Compiler-Assisted Selection of Hardware Acceleration Candidates from Application Source Code." In *2019 IEEE 37th International Conference on Computer Design (ICCD)*. IEEE. [https://doi.org/10.1109/iccd46524.2019.00024][research_zacharopoulos_2019]
- Zampetti, Fiorella, Gianmarco Fucci, Alexander Serebrenik, and Massimiliano Di Penta. 2021. "Self-Admitted Technical Debt Practices: A Comparison between Industry and Open-Source." *Empirical Software Engineering* 26 (6): 131. [https://doi.org/10.1007/s10664-021-10031-3][research_zampetti_2021]
- Zha, Junpeng, Hongjin Liang, and Xinyu Feng. 2022. "Verifying Optimizations of Concurrent Programs in the Promising Semantics." In *Proceedings of the 43rd ACM SIGPLAN International Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3519939.3523734][research_zha_2022]
- Zhang, Chenwei. 2025. "Large Language Model Generation Safety: A Comprehensive Investigation." In *Proceedings of the 2nd International Conference on Applied Physics and Mathematics*. SCITEPRESS - Science and Technology Publications. [https://doi.org/10.5220/0014756900004940][research_zhang_2025_h]
- Zhang, Rui, Michael D. Bond, and Yinqian Zhang. 2022b. "Cape: Compiler-Aided Program Transformation for HTM-Based Cache Side-Channel Defense." In *Proceedings of the 31st ACM SIGPLAN International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3497776.3517778][research_zhang_2022]
- Zhang, Chen, Bihuan Chen, Siqi Wu, Lei Zhao, Xin Peng, and Wenyun Zhao. 2026f. "A Large-Scale Empirical Study of Configurations, Errors, and Warnings for Compilation in Continuous Integration." *Empirical Software Engineering* 31 (3): 64. [https://doi.org/10.1007/s10664-025-10798-9][research_zhang_2026_e]
- Zhang, Chaolin, Jiqiu Deng, Hui Zhang, Longbo Li, Liji Sun, and Xiao Ma. 2026d. "GeoIR-Compiler: A Geospatial Intermediate Representation and Compilation Framework for Chinese Urban Spatial Question Answering." *ISPRS International Journal of Geo-Information* 15 (7): 310. [https://doi.org/10.3390/ijgi15070310][research_zhang_2026_b]
- Zhang, Xiao, Yaoyao Ding, Bolin Sun, Yang Hu, Tatiana Shpeisman, and Gennady Pekhimenko. 2026e. "Hexcute: A Compiler Framework for Automating Layout Synthesis in GPU Programs." In *2026 IEEE/ACM International Symposium on Code Generation and Optimization (CGO)*. IEEE. [https://doi.org/10.1109/cgo68049.2026.11395194][research_zhang_2026_c]
- Zhang, Yu, Yongbing Gao, Weihao Li, Zirong Su, and Lidong Yang. 2024a. "Chinese Generation and Security Index Evaluation Based on Large Language Model." In *2024 International Conference on Asian Language Processing (IALP)*. IEEE. [https://doi.org/10.1109/ialp63756.2024.10661189][research_zhang_2024_c]
- Zhang, Zhenning, Longkun Guo, Linyang Wang, and Juan Zou. 2021a. "One-Pass Streaming Algorithm for Monotone Lattice Submodular Maximization Subject to a Cardinality Constraint." *Concurrency and Computation: Practice and Experience* 35 (17): e6645. [https://doi.org/10.1002/cpe.6645][research_zhang_2021_c]
- Zhang, Zhenning, Longkun Guo, Linyang Wang, and Juan Zou. 2021b. "A Streaming Model for Monotone Lattice Submodular Maximization with a Cardinality Constraint." In *Parallel and Distributed Computing, Applications and Technologies*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-69244-5\_32][research_zhang_2021_b]
- Zhang, Quan, Yujie Huang, Yujie Cai, Yalong Pang, and Jun Han. 2018. "Design of RLWE Cryptoprocessor Based on Vector-Instruction Extension with RISC-V Architecture." In *2018 14th IEEE International Conference on Solid-State and Integrated Circuit Technology (ICSICT)*. IEEE. [https://doi.org/10.1109/icsict.2018.8564985][research_zhang_2018]
- Zhang, Jiaming, Jiahao Lu, Dongsheng Liu, et al. 2023b. "Flexible and Efficient Implementation of CRYSTALS-KYBER SIMD RISC-V Coprocessor Based on Customized Vector Instruction-Set Extension." In *2023 IEEE Asian Solid-State Circuits Conference (A-SSCC)*. IEEE. [https://doi.org/10.1109/a-sscc58667.2023.10347942][research_zhang_2023]
- Zhang, Hongyang, and Wenchang Luo. 2025. "Streaming Algorithms for Non-Monotone DR-Submodular Maximization under a Knapsack Constraint on the Integer Lattice." *4OR* 23 (3): 303–27. [https://doi.org/10.1007/s10288-025-00593-z][research_zhang_2025_e]
- Zhang, Hongyang, and Wenchang Luo. 2026. "A Streaming Algorithm for Non-Monotone Regularized Submodular Maximization." *Operations Research Letters* 67: 107456. [https://doi.org/10.1016/j.orl.2026.107456][research_zhang_2026_f]
- Zhang, Yue, Justin Murphy, and Akond Rahman. 2025b. "Come for Syntax, Stay for Speed, Write Secure Code: An Empirical Study of Security Weaknesses in Julia Programs." *Empirical Software Engineering* 30 (2): 58. [https://doi.org/10.1007/s10664-024-10606-w][research_zhang_2025_b]
- Zhang, Ruiyong, Hongkun Qiu, Yajie Wang, Yisheng Xiao, and Jize Wang. 2019. "Design and Development of Bridge AI Bid Program Based on Double-Hand Solver." In *2019 Chinese Control And Decision Conference (CCDC)*. IEEE. [https://doi.org/10.1109/ccdc.2019.8833178][research_zhang_2019]
- Zhang, Pengcheng, Bin Ren, Hai Dong, and Qiyin Dai. 2022a. "CAGFuzz: Coverage-Guided Adversarial Generative Fuzzing Testing for Image-Based Deep Learning Systems." *IEEE Transactions on Software Engineering* 48 (11): 4630–46. [https://doi.org/10.1109/tse.2021.3124006][research_zhang_2022_b]
- Zhang, Lan, Anoop Singhal, Qingtian Zou, Xiaoyan Sun, Peng Liu, and Hsiao-Ying Lin. 2025a. "Can AI Fix Buggy Code? Exploring the Use of Large Language Models in Automated Program Repair." *Computer* 58 (7): 122–28. [https://doi.org/10.1109/mc.2025.3527407][research_zhang_2025_f]
- Zhang, Qirun, Chengnian Sun, and Zhendong Su. 2017. "Skeletal Program Enumeration for Rigorous Compiler Testing." In *Proceedings of the 38th ACM SIGPLAN Conference on Programming Language Design and Implementation*. ACM. [https://doi.org/10.1145/3062341.3062379][research_zhang_2017]
- Zhang, Yanzhi, and Tao Wang. 2021. "CCEyes: An Effective Tool for Code Clone Detection on Large-Scale Open Source Repositories." In *2021 IEEE International Conference on Information Communication and Software Engineering (ICICSE)*. IEEE. [https://doi.org/10.1109/icicse52190.2021.9404141][research_zhang_2021]
- Zhang, Yi, Yu Wang, Linzhang Wang, and Ke Wang. 2025f. "Synchronized Behavior Checking: A Method for Finding Missed Compiler Optimizations." *Proceedings of the ACM on Programming Languages* 9 (OOPSLA2): 1541–68. [https://doi.org/10.1145/3763105][research_zhang_2025]
- Zhang, Chengming, Haoye Wang, Chuyang Xu, Jiakun Liu, Kui Liu, and Zhongxin Liu. 2026a. "Can Test Cases Generated by Large Language Models Facilitate Automated Program Repair?" *Empirical Software Engineering* 31 (3): 68. [https://doi.org/10.1007/s10664-026-10802-w][research_zhang_2026_g]
- Zhang, Weichuang, Yiquan Wang, Xinzhou Zhang, et al. 2026b. "CODO: An Automated Compiler for Comprehensive Dataflow Optimization." In *2026 ACM/IEEE 53rd Annual International Symposium on Computer Architecture (ISCA)*. IEEE. [https://doi.org/10.1109/isca66397.2026.00018][research_zhang_2026_d]
- Zhang, Huan, Qingyang Yan, Weihuan Min, Chenyuan Zhang, Li Kuang, and Yingjie Xia. 2025c. "EvoAPR: Enhancing Large Language Models for Automatic Program Repair with Genetic Algorithm and Dynamic LoRA." In *2025 IEEE International Conference on Web Services (ICWS)*. IEEE. [https://doi.org/10.1109/icws67624.2025.00123][research_zhang_2025_g]
- Zhang, Ruxin, Shanxin Zhang, and Linbo Xie. 2026g. "Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models." *Software Quality Journal* 34 (2): 14. [https://doi.org/10.1007/s11219-026-09751-w][research_zhang_2026_h]
- Zhao, Yaxin, Lina Gong, Wenhua Yang, and Yu Zhou. 2024a. "How Accessibility Affects Other Quality Attributes of Software? A Case Study of GitHub." *Science of Computer Programming* 231: 103027. [https://doi.org/10.1016/j.scico.2023.103027][research_zhao_2024_b]
- Zhao, Yifan, Dan Hao, and Lu Zhang. 2023. "Revisiting Machine Learning Based Test Case Prioritization for Continuous Integration." In *2023 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme58846.2023.00032][research_zhao_2023]
- Zhao, Jianzhou, Santosh Nagarakatte, Milo M. K. Martin, and Steve Zdancewic. 2012. "Formalizing the LLVM Intermediate Representation for Verified Program Transformations." In *Proceedings of the 39th annual ACM SIGPLAN-SIGACT symposium on Principles of programming languages*. ACM. [https://doi.org/10.1145/2103656.2103709][research_zhao_2012]
- Zhao, Zhongyuan, Weiguang Sheng, Jinchao Li, Pengfei Ye, Qin Wang, and Zhigang Mao. 2021. "Similarity-Aware Architecture/Compiler Co-Designed Context-Reduction Framework for Modulo-Scheduled CGRA." *Electronics* 10 (18): 2210. [https://doi.org/10.3390/electronics10182210][research_zhao_2021]
- Zhao, Jinman, Seyed Aryan Vahabpour, Xingyu Yue, Kai-Ting Amy Wang, and Tarek S. Abdelrahman. 2025b. "PolyMorphous: An MLIR-Based Polyhedral Compiler with Loop Transformation Primitives." In *2025 IEEE International Parallel and Distributed Processing Symposium (IPDPS)*. IEEE. [https://doi.org/10.1109/ipdps64566.2025.00041][research_zhao_2025]
- Zhao, Jiayu, Chunwei Xia, and Zheng Wang. 2025a. "Leveraging Compilation Statistics for Compiler Phase Ordering." In *2025 IEEE International Parallel and Distributed Processing Symposium (IPDPS)*. IEEE. [https://doi.org/10.1109/ipdps64566.2025.00054][research_zhao_2025_b]
- Zheng, Haisheng, Zhuolun He, Shuo Yin, Yuzhe Ma, and Bei Yu. 2026. "CombRewriter: Enabling Combinational Logic Simplification in MLIR-Based Hardware Compiler." In *2026 31st Asia and South Pacific Design Automation Conference (ASP-DAC)*. IEEE. [https://doi.org/10.1109/asp-dac66049.2026.11420469][research_zheng_2026]
- Zheng, Wenlong, and Baojian Hua. 2023. "A Comprehensive Study of Bugs in Embedded WebAssembly Virtual Machines." In *2023 3rd International Conference on Computer Science, Electronic Information Engineering and Intelligent Control Technology (CEI)*. IEEE. [https://doi.org/10.1109/cei60616.2023.10528174][research_zheng_2023]
- Zhioua, Zeineb, Yves Roudier, and Rabea Boulifa Ameur. 2017. "Formal Specification and Verification of Security Guidelines." In *2017 IEEE 22nd Pacific Rim International Symposium on Dependable Computing (PRDC)*. IEEE. [https://doi.org/10.1109/prdc.2017.51][research_zhioua_2017]
- Zhong, Hao, and Zhendong Su. 2015. "An Empirical Study on Real Bug Fixes." In *2015 IEEE/ACM 37th IEEE International Conference on Software Engineering*. IEEE. [https://doi.org/10.1109/icse.2015.101][research_zhong_2015]
- Zhou, Jianyi, and Dan Hao. 2017. "Impact of Static and Dynamic Coverage on Test-Case Prioritization: An Empirical Study." In *2017 IEEE International Conference on Software Testing, Verification and Validation Workshops (ICSTW)*. IEEE. [https://doi.org/10.1109/icstw.2017.74][research_zhou_2017]
- Zhou, Zhide, He Jiang, Zhilei Ren, Yuting Chen, and Lei Qiao. 2022. "LocSeq: Automated Localization for Compiler Optimization Sequence Bugs of LLVM." *IEEE Transactions on Reliability* 71 (2): 896–910. [https://doi.org/10.1109/tr.2022.3165378][research_zhou_2022]
- Zhou, Lifeng, and Pratap Tokekar. 2019. "An Approximation Algorithm for Distributed Resilient Submodular Maximization: Extended Abstract." In *2019 International Symposium on Multi-Robot and Multi-Agent Systems (MRS)*. IEEE. [https://doi.org/10.1109/mrs.2019.8901088][research_zhou_2019]
- Zhou, Lifeng, Vasileios Tzoumas, George J. Pappas, and Pratap Tokekar. 2020. "Distributed Attack-Robust Submodular Maximization for Multi-Robot Planning." In *2020 IEEE International Conference on Robotics and Automation (ICRA)*. IEEE. [https://doi.org/10.1109/icra40945.2020.9197243][research_zhou_2020]
- Zhou, Shufan, Hao Zhong, and Beijun Shen. 2018. "SLAMPA: Recommending Code Snippets with Statistical Language Model." In *2018 25th Asia-Pacific Software Engineering Conference (APSEC)*. IEEE. [https://doi.org/10.1109/apsec.2018.00022][research_zhou_2018]
- Zhu, Bin, and Kun Xie. 2025. "A Domain-Specific Compiler for Embedded DSP Development Based on Component Code Generation: Architecture and Correctness." In *2025 6th International Conference on Machine Learning and Computer Application (ICMLCA)*. IEEE. [https://doi.org/10.1109/icmlca66850.2025.11336697][research_zhu_2025]
- Zhuykov, Roman, Vahagn Vardanyan, Dmitry Melnik, Ruben Buchatskiy, and Eugeniy Sharygin. 2015. "Augmenting JavaScript JIT with Ahead-of-Time Compilation." In *2015 Computer Science and Information Technologies (CSIT)*. IEEE. [https://doi.org/10.1109/csitechnol.2015.7358262][research_zhuykov_2015]
- Ziftci, Celal, and Diego Cavalcanti. 2020. "De-Flake Your Tests: Automatically Locating Root Causes of Flaky Tests in Code at Google." In *2020 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. IEEE. [https://doi.org/10.1109/icsme46990.2020.00083][research_ziftci_2020]
- Zou, Weiqin, Xin Xia, Weiqiang Zhang, Zhenyu Chen, and David Lo. 2015. "An Empirical Study of Bug Fixing Rate." In *2015 IEEE 39th Annual Computer Software and Applications Conference*. IEEE. [https://doi.org/10.1109/compsac.2015.57][research_zou_2015]
- Zou, Weiqin, Weiqiang Zhang, Xin Xia, Reid Holmes, and Zhenyu Chen. 2019. "Branch Use in Practice: A Large-Scale Empirical Study of 2,923 Projects on GitHub." In *2019 IEEE 19th International Conference on Software Quality, Reliability and Security (QRS)*. IEEE. [https://doi.org/10.1109/qrs.2019.00047][research_zou_2019]
- Zubair, Fida, Maryam Al-Hitmi, and Cagatay Catal. 2025. "The Use of Large Language Models for Program Repair." *Computer Standards & Interfaces* 93: 103951. [https://doi.org/10.1016/j.csi.2024.103951][research_zubair_2025]
- Zubert, Mariusz, and Arkadiusz Łuczyk. 2024. "LLVM Library for a Dedicated Processor Instruction Set – a Case Study." In *2024 31st International Conference on Mixed Design of Integrated Circuits and System (MIXDES)*. IEEE. [https://doi.org/10.23919/mixdes62605.2024.10613932][research_zubert_2024]

### Primary Sources, Non-Peer-Reviewed

- Abnane, Ibtissam, Ali Idri, and Alain Abran. 2017. "Empirical Evaluation of Fuzzy Analogy for Software Development Effort Estimation." In *Proceedings of the Symposium on Applied Computing*. ACM. [https://doi.org/10.1145/3019612.3019905][research_abnane_2017]
- Acharya, Jagrit, and Gouri Ginde. 2025. "Can We Enhance Bug Report Quality Using LLMs?: An Empirical Study of LLM-Based Bug Report Generation." In *Proceedings of the 29th International Conference on Evaluation and Assessment in Software Engineering*. ACM. [https://doi.org/10.1145/3756681.3756995][research_acharya_2025]
- Adiyoso, Wibisono, and Yeremia Alfa Susetyo. 2023. "Pembangunan Compiler Domain Specific Language Sebagai Generator Form HTML Menggunakan Python Sly." *Jurnal Indonesia: Manajemen Informatika dan Komunikasi* 4 (2): 449–61. [https://doi.org/10.35870/jimik.v4i2.231][research_adiyoso_2023]
- Agostini, Nicolas Bohm, Serena Curzel, Vinay Amatya, et al. 2022. "An MLIR-Based Compiler Flow for System-Level Design and Hardware Acceleration." In *Proceedings of the 41st IEEE/ACM International Conference on Computer-Aided Design*. ACM. [https://doi.org/10.1145/3508352.3549424][research_agostini_2022]
- Agrawal, Vishakha. 2025. "MLIR: A Panacea for ML Compiler Challenges?" *Interantional Journal of Scientific Research in Engineering and Management* 09 (01): 1–7. [https://doi.org/10.55041/ijsrem10701][research_agrawal_2025]
- Ahmad, Sabrina, Riftika Rizawanti, Terry Woodings, and Intan Ermahani A. Jalil. 2022. "MCBRank Method to Improve Software Requirements Prioritization." *International Journal of Advanced Computer Science and Applications* 13 (7). [https://doi.org/10.14569/ijacsa.2022.0130728][research_ahmad_2022]
- Aho, Alfred V., Mahadevan Ganapathi, and Steven W. K. Tjiang. 1989. "Code Generation Using Tree Matching and Dynamic Programming." *ACM Transactions on Programming Languages and Systems* 11 (4): 491–516. [https://doi.org/10.1145/69558.75700][research_aho_ganapathi_1989]
- Akanbi, Johnson Oluwatobi, Allen Akinkitan Ajose, and Kareem Afiss Emiola. 2022. "Code Generation Techniques in Compiler Design: Conceptual and Structural Review." *International Journal of Recent Engineering Science* 9 (3): 1–6. [https://doi.org/10.14445/23497157/ijres-v9i3p101][research_akanbi_2022]
- Akbar, Shayan A., and Avinash C. Kak. 2020. "A Large-Scale Comparative Evaluation of IR-Based Tools for Bug Localization." In *Proceedings of the 17th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3379597.3387474][research_akbar_2020]
- Al-Refai, Hasan, and Khaldoun Batiha. 2017. "Enhancing Formal Specification and Verification of e-Commerce Protocol." *Journal of Advanced Computer Science & Technology* 6 (1): 13–19. [https://doi.org/10.14419/jacst.v6i1.6713][research_alrefai_2017]
- Alaluf, Naor, Alina Ene, Moran Feldman, Huy L. Nguyen, and Andrew Suh. 2022. "An Optimal Streaming Algorithm for Submodular Maximization with a Cardinality Constraint." *Mathematics of Operations Research* 47 (4): 2667–90. [https://doi.org/10.1287/moor.2021.1224][research_alaluf_2022]
- Alecsandro Bacin, Fabio, Braulio Adriano de Mello, Giancarlo Dondoni Salton, and Samuel Da Silva Feitosa. 2025. "A Systematic Review about Large Language Models (LLMs) Applied to Code Generation." *Revista Brasileira de Computação Aplicada* 17 (3): 1–13. [https://doi.org/10.5335/rbca.v17i3.16310][research_alecsandrobaci_2025]
- Aleen, Farhana, Vyacheslav P. Zakharin, Rakesh Krishaniyer, Garima Gupta, David Kreitzer, and Chang-Sun Lin. 2016. "Automated Compiler Optimization of Multiple Vector Loads/stores." In *Proceedings of the ACM International Conference on Computing Frontiers*. ACM. [https://doi.org/10.1145/2903150.2903169][research_aleen_2016]
- Alfayez, Reem, Wesam Alwehaibi, Robert Winn, Elaine Venson, and Barry Boehm. 2020. "A Systematic Literature Review of Technical Debt Prioritization." In *Proceedings of the 3rd International Conference on Technical Debt*. ACM. [https://doi.org/10.1145/3387906.3388630][research_alfayez_2020]
- Alfayez, Reem, Celia Chen, Pooyan Behnamghader, Kamonphop Srisopha, and Barry Boehm. 2017. "An Empirical Study of Technical Debt in Open-Source Software Systems." In *Disciplinary Convergence in Systems Engineering Research*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-62217-0\_9][research_alfayez_2017]
- Aljebreen, Ghader, Reem Alnanih, Fathy Eassa, Maher Khemakhem, Kamal Jambi, and Muhammed Usman Ashraf. 2025. "Binary–Source Code Matching Based on Decompilation Techniques and Graph Analysis." *International Journal of Advanced Computer Science and Applications* 16 (5). [https://doi.org/10.14569/ijacsa.2025.0160525][research_aljebreen_2025]
- Allen, Frances E. 1970. "Control Flow Analysis." In *Proceedings of a symposium on Compiler optimization -*. ACM Press. [https://doi.org/10.1145/800028.808479][research_allen_1970]
- Almeida, José Bacelar, Manuel Barbosa, Manuel L. Correia, et al. 2021. "Machine-Checked ZKP for NP Relations: Formally Verified Security Proofs and Implementations of MPC-in-the-Head." In *Proceedings of the 2021 ACM SIGSAC Conference on Computer and Communications Security*. ACM. [https://doi.org/10.1145/3460120.3484771][research_almeida_2021]
- Alpay, Aksel, and Vincent Heuveline. 2025. "Adaptivity in AdaptiveCpp: Optimizing Performance by Leveraging Runtime Information during JIT-Compilation." In *Proceedings of the 13th International Workshop on OpenCL and SYCL*. ACM. [https://doi.org/10.1145/3731125.3731127][research_alpay_2025]
- Alqarni, Mansour, and Akramul Azim. 2022. "Low Level Source Code Vulnerability Detection Using Advanced BERT Language Model." *Proceedings of the Canadian Conference on Artificial Intelligence*. [https://doi.org/10.21428/594757db.b85e6625][research_alqarni_2022]
- Althar, Raghavendra Rao, and Debabrata Samanta. 2020. "Building Intelligent Integrated Development Environment for IoT in the Context of Statistical Modeling for Software Source Code." In *Studies in Big Data*. Springer Singapore. [https://doi.org/10.1007/978-981-15-7965-3\_7][research_althar_2020]
- Amdahl, Gene M. 1967. "Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities." In *Proceedings of the April 18-20, 1967, spring joint computer conference on - AFIPS '67 (Spring)*. ACM Press. [https://doi.org/10.1145/1465482.1465560][research_amdahl_1967]
- Ankush Jitendrakumar Tyagi. 2025. "Enhancing Compiler Design for Machine Learning Workflows with MLIR." *International Journal of Science and Research Archive* 16 (2): 1397–1405. [https://doi.org/10.30574/ijsra.2025.16.2.2463][research_ankushjitendra_2025]
- Antony, Paulson K., Nikshith Narayan Ramesh, Pranav Suryadevara, and A. Prathiba. 2025. *RISC-V Processor Hardware Modelling with Custom Instruction Set for SHA-3 Acceleration*. Wiley. [https://doi.org/10.1002/9781394272549.ch7][research_antony_2025]
- Apa, Cecilia, Martin Solari, Diego Vallespir, and Guilherme Horta Travassos. 2020. "A Taste of the Software Industry Perception of Technical Debt and Its Management in Uruguay: A Survey in Software Industry." In *Proceedings of the 14th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. ACM. [https://doi.org/10.1145/3382494.3421463][research_apa_2020]
- Aradhya, Sumalatha, and N. K. Srinath Dr. 2018. "Intrinsic Compilation Model to Enhance Performance of Real Time Application in Embedded Multi Core System." *International Journal of Engineering and Technology* 10 (3): 854–64. [https://doi.org/10.21817/ijet/2018/v10i3/181003098][research_aradhya_2018]
- Arasteh, Bahman, Seyed Salar Sefati, Shiva Shami, and Mehrdad Abdollahian. 2024. "Discretized Optimization Algorithms for Finding the Bug-Prone Locations of a Program Source Code." In *Decision-Making Models*. Elsevier. [https://doi.org/10.1016/b978-0-443-16147-6.00019-0][research_arasteh_2024]
- Ashouri, Amir H., Shayan Shirahmad Gale Bagi, Kavin Satheeskumar, et al. 2026. "Protean Compiler: An Agile Framework to Drive Fine-Grain Phase Ordering." *ACM Transactions on Architecture and Code Optimization* 23 (3): 1–26. [https://doi.org/10.1145/3831596][research_ashouri_2026]
- Askar, Ammar, Fabian Fleischer, Christopher Kruegel, Giovanni Vigna, and Taesoo Kim. 2025. "MALintent: Coverage Guided Intent Fuzzing Framework for Android." In *Proceedings 2025 Network and Distributed System Security Symposium*. Internet Society. [https://doi.org/10.14722/ndss.2025.230125][research_askar_2025]
- Astuti, Marni, Ardian Prabowo, Esa Rengganis Sullyarta, and Yasrin Zabidi. 2023. "Optimization of Production Planning Using Integer Linear Programming Method (Case Study of Bakpia Menik)." *Compiler* 12 (2): 109. [https://doi.org/10.28989/compiler.v12i2.1919][research_astuti_2023]
- Atanassov, Atanas. 2024. "Developing Situational Conditions and Program Codes for Parallel Situational Analysis Solver Based on Conic Umbra/sunlit Models." *Aerospace Research in Bulgaria* 36: 15–28. [https://doi.org/10.3897/arb.v36.e02][research_atanassov_2024]
- Auerbach, Joshua S., Martin Hirzel, Louis Mandel, Avraham Shinnar, and Jérôme Siméon. 2017. "Handling Environments in a Nested Relational Algebra with Combinators and an Implementation in a Verified Query Compiler." In *Proceedings of the 2017 ACM International Conference on Management of Data*. ACM. [https://doi.org/10.1145/3035918.3035961][research_auerbach_2017]
- Austin, and Linda J. McCall. 2017. "Prpa Repercussions & Implications for Real World Study by Citizen Scientist Avocational Paleontologists." In *Geological Society of America Abstracts with Programs*. Geological Society of America. [https://doi.org/10.1130/abs/2017ne-290436][research_anon_2017]
- Averill, Charles, Ilan Buzzetti, Alex Bellon, and Kevin W. Hamlen. 2026. "LAPSE: Automatic, Formal Fault-Tolerant Correctness Proofs for Native Code." In *Proceedings 2026 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2026.23046][research_averill_2026]
- Ayeoribe, Olarewaju Peter. 2026. "Instruction Set Optimization for FM-Type Digital Signal Processor (DSP) Architectures with Integration of DVB-T2 TV Systems." *Applied Information Technology and Computer Science (AICOMS)* 5 (1): 21–28. [https://doi.org/10.58466/35jafg24][research_ayeoribe_2026]
- Azevedo, Ivanildo, Ana Paula Vasconcelos, Eudis Teixeira, and Sergio Soares. 2025. "Reimagining Studies’ Replication: A Validity-Driven Analysis of Threats in Empirical Software Engineering." In *Anais do XXXIX Simpósio Brasileiro de Engenharia de Software (SBES 2025)*. Sociedade Brasileira de Computação. [https://doi.org/10.5753/sbes.2025.11270][research_azevedo_2025]
- Baek, Soyeon, and Sungho Lee. 2024. "Extracting Invariants from Conditional Branches for Abstract Value Refinement in Static Analysis Targeting LLVM IR." *KIISE Transactions on Computing Practices* 30 (10): 519–24. [https://doi.org/10.5626/ktcp.2024.30.10.519][research_baek_2024]
- Bandyopadhyay, Biswadeb. 2022. "A Comprehensive Study on Code Coverage Analysis for Effective Test Development/Enhancement Methodology." *American Journal of Science & Engineering* 3 (2): 31–36. [https://doi.org/10.15864/ajse.3205][research_bandyopadhyay_2022]
- Banerjee, Kunal, and Chandan Karfa. 2018. "Compiler-Agnostic Translation Validation." In *Proceedings of the 11th Innovations in Software Engineering Conference*. ACM. [https://doi.org/10.1145/3172871.3180078][research_banerjee_2018]
- Bansal, Sorav, and Alex Aiken. 2006. "Automatic Generation of Peephole Superoptimizers." In *Proceedings of the 12th international conference on Architectural support for programming languages and operating systems*. ACM. [https://doi.org/10.1145/1168857.1168906][research_bansal_aiken_2006]
- Barany, Gergö. 2018. "Finding Missed Compiler Optimizations by Differential Testing." In *Proceedings of the 27th International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3178372.3179521][research_barany_2018]
- Barboni, Morena, Filippo Lampa, Andrea Morichetta, and Andrea Polini. 2026. "Neural-MCTS Test Prioritization for Smart Contract Mutation Testing." *Distributed Ledger Technologies: Research and Practice*: 3828728. [https://doi.org/10.1145/3828728][research_barboni_2026]
- Barrière, Aurèle, Sandrine Blazy, Olivier Flückiger, David Pichardie, and Jan Vitek. 2020. *CoreJIT: A Replication Package for Article "Formally Verified Speculation and Deoptimization in a JIT Compiler "*. Association for Computing Machinery (ACM). [https://doi.org/10.1145/3410263][research_barriere_2020]
- Basit Ur Rahim, Muhammad Abdul. 2025. "Ensuring Reliability in Self-Adaptive Systems: A Framework for Formal Specification and Verification." *Contemporary Mathematics*: 6553–69. [https://doi.org/10.37256/cm.6520256223][research_basiturrahim_2025]
- Bass, Julian Michael. 2022. "Technical Debt, Software Evolution and Legacy." In *Agile Software Engineering Skills*. Springer International Publishing. [https://doi.org/10.1007/978-3-031-05469-3\_20][research_bass_2022]
- Basso, Matteo, Aleksandar Prokopec, Andrea Rosà, and Walter Binder. 2023. "Optimization-Aware Compiler-Level Event Profiling." *ACM Transactions on Programming Languages and Systems* 45 (2): 1–50. [https://doi.org/10.1145/3591473][research_basso_2023]
- Bauckholt, Florian, and Thorsten Holz. 2024. "WebAssembly as a Fuzzing Compilation Target (Registered Report)." In *Proceedings of the 3rd ACM International Fuzzing Workshop*. ACM. [https://doi.org/10.1145/3678722.3685531][research_bauckholt_2024]
- Bavota, Gabriele. 2026. "Technical Perspective: Fusing Large Language Models with Completion Engines for Automated Program Repair." *Communications of the ACM* 69 (4): 88–88. [https://doi.org/10.1145/3789228][research_bavota_2026]
- Bavota, Gabriele, and Barbara Russo. 2016. "A Large-Scale Empirical Study on Self-Admitted Technical Debt." In *Proceedings of the 13th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/2901739.2901742][research_bavota_2016]
- Beringer, Lennart. 2021. "Functional Representations of SSA." In *SSA-based Compiler Design*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-80515-9\_6][research_beringer_2021]
- Bhatia, Aaditya, Foutse Khomh, Bram Adams, and Ahmed Hassan. 2026. "An Empirical Study of Self-Admitted Technical Debt in Machine Learning Software." *ACM Transactions on Software Engineering and Methodology* 35 (8): 1–41. [https://doi.org/10.1145/3785001][research_bhatia_2026]
- Biggar, Paul, and David Gregg. 2021. "Building SSA in a Compiler for PHP." In *SSA-based Compiler Design*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-80515-9\_24][research_biggar_2021]
- Bik, Aart, Penporn Koanantakool, Tatiana Shpeisman, Nicolas Vasilache, Bixia Zheng, and Fredrik Kjolstad. 2022. "Compiler Support for Sparse Tensor Computations in MLIR." *ACM Transactions on Architecture and Code Optimization* 19 (4): 1–25. [https://doi.org/10.1145/3544559][research_bik_2022]
- Birnbaum, Z. W. 1968. *On the Importance of Different Components in a Multicomponent System*. Defense Technical Information Center. [https://doi.org/10.21236/ad0670563][research_birnbaum_1968]
- Blackburn, Stephen M., Amer Diwan, Matthias Hauswirth, et al. 2016. "The Truth, the Whole Truth, and Nothing but the Truth: A Pragmatic Guide to Assessing Empirical Evaluations." *ACM Transactions on Programming Languages and Systems* 38 (4): 1–20. [https://doi.org/10.1145/2983574][research_blackburn_2016]
- Bleier, Jakob, and Martina Lindorfer. 2023. "Of Ahead Time: Evaluating Disassembly of Android Apps Compiled to Binary OATs through the ART." In *Proceedings of the 16th European Workshop on System Security*. ACM. [https://doi.org/10.1145/3578357.3591219][research_bleier_2023]
- Bodin, Martin, Thomas Jensen, and Alan Schmitt. 2015. "Certified Abstract Interpretation with Pretty-Big-Step Semantics." In *Proceedings of the 2015 Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/2676724.2693174][research_bodin_2015]
- Boehm, Matthias, Matteo Interlandi, and Chris Jermaine. 2023. "Optimizing Tensor Computations: From Applications to Compilation and Runtime Techniques." In *Companion of the 2023 International Conference on Management of Data*. ACM. [https://doi.org/10.1145/3555041.3589407][research_boehm_2023]
- Böhm, Corrado, and Giuseppe Jacopini. 1966. "Flow Diagrams, Turing Machines and Languages with Only Two Formation Rules." *Communications of the ACM* 9 (5): 366–71. [https://doi.org/10.1145/355592.365646][research_bohm_jacopini_1966]
- Bokati, Laxman, Olga Kosheleva, Vladik Kreinovich, and Nguyen Ngoc Thach. 2024. "Why Shapley Value and Its Variants Are Useful in Machine Learning (and in Other Applications)." In *Studies in Systems, Decision and Control*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-43601-7\_10][research_bokati_2024]
- Botor, Tomáš, and Hashim Habiballa. 2018. "Compiler Optimization for Scientific Computation in C/C++." In *AIP Conference Proceedings*, vol. 2040. Author(s). [https://doi.org/10.1063/1.5079067][research_botor_2018]
- Bourke, Timothy, Lélio Brun, and Marc Pouzet. 2018. "Towards a Verified Lustre Compiler with Modular Reset." In *Proceedings of the 21st International Workshop on Software and Compilers for Embedded Systems*. ACM. [https://doi.org/10.1145/3207719.3207732][research_bourke_2018]
- Bruns, Niklas, Vladimir Herdt, Daniel Große, and Rolf Drechsler. 2022a. "Efficient Cross-Level Processor Verification Using Coverage-Guided Fuzzing." In *Proceedings of the Great Lakes Symposium on VLSI 2022*. ACM. [https://doi.org/10.1145/3526241.3530340][research_bruns_2022]
- Bryksin, Timofey, Victor Petukhov, Ilya Alexin, et al. 2020. "Using Large-Scale Anomaly Detection on Code to Improve Kotlin Compiler." In *Proceedings of the 17th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3379597.3387447][research_bryksin_2020]
- Buchbinder, Niv, and Moran Feldman. 2025. "Deterministic Algorithm and Faster Algorithm for Submodular Maximization Subject to a Matroid Constraint." *SIAM Journal on Computing*: FOCS24-85-FOCS24-114. [https://doi.org/10.1137/24m1698122][research_buchbinder_2025]
- Buchbinder, Niv, Moran Feldman, Joseph Seffi, and Roy Schwartz. 2015. "A Tight Linear Time (1/2)-Approximation for Unconstrained Submodular Maximization." *SIAM Journal on Computing* 44 (5): 1384–1402. [https://doi.org/10.1137/130929205][research_buchbinder_2015]
- Buchwald, Sebastian, Andreas Fried, and Sebastian Hack. 2018. "Synthesizing an Instruction Selection Rule Library from Semantic Specifications." In *Proceedings of the 2018 International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3168821][research_buchwald_2018]
- Buchwald, Sebastian, Denis Lohner, and Sebastian Ullrich. 2016. "Verified Construction of Static Single Assignment Form." In *Proceedings of the 25th International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/2892208.2892211][research_buchwald_2016]
- Calamo, Marco, and Jacopo Rossi. 2025. "Programming Large Language Models." In *Engineering Information Systems with Large Language Models*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-92285-5\_6][research_calamo_2025]
- Carminati, Andreu, Renan Augusto Starke, and Rômulo Silva de Oliveira. 2017. "Combining Loop Unrolling Strategies and Code Predication to Reduce the Worst-Case Execution Time of Real-Time Software." *Applied Computing and Informatics* 13 (2): 184–93. [https://doi.org/10.1016/j.aci.2017.03.002][research_carminati_2017]
- Chakravarthi, Veena S., and Shivananda R. Koteshwar. 2025. "Application-Specific Instruction Set Processor." In *SOC-Based Solutions in Emerging Application Domains*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-85044-8\_7][research_chakravarthi_2025]
- Chang, Juneseo, and Daejin Park. 2023. "Work-in-Progress: Searching Optimal Compiler Optimization Passes Sequence for Reducing Runtime Memory Profile Using Ensemble Reinforcement Learning." In *Proceedings of the International Conference on Embedded Software*. ACM. [https://doi.org/10.1145/3607890.3608460][research_chang_2023]
- Chaplygin, A. A. 2025. "Modeling and Implementation of Common LISP Functional Language Compiler." *Proceedings of the Southwest State University* 29 (3): 99–112. [https://doi.org/10.21869/2223-1560-2025-29-3-99-112][research_chaplygin_2025]
- Charles, Henri-Pierre, and Victor Lomüller. 2015. "Is Dynamic Compilation Possible for Embedded Systems?" In *Proceedings of the 18th International Workshop on Software and Compilers for Embedded Systems*. ACM. [https://doi.org/10.1145/2764967.2782785][research_charles_2015]
- Chaudhary, Neha, and O. P. Sangwan. 2016. "Assessment and Comparison of Fuzzy Based Test Suite Prioritization Method for GUI Based Software." *International Journal of Advanced Computer Science and Applications* 7 (1). [https://doi.org/10.14569/ijacsa.2016.070131][research_chaudhary_2016]
- Chayan, Bhatt, and Singhal Sunita. 2023. "Hybrid Metaheuristic Technique for Optimization of Virtual Machine Placement in Cloud." *INTERNATIONAL JOURNAL of FUZZY LOGIC and INTELLIGENT SYSTEMS* 23 (3): 353–64. [https://doi.org/10.5391/ijfis.2023.23.3.353][research_chayan_2023]
- Chelini, Lorenzo, Tobias Gysi, Tobias Grosser, Martin Kong, and Henk Corporaal. 2020. "Automatic Generation of Multi-Objective Polyhedral Compiler Transformations." In *Proceedings of the ACM International Conference on Parallel Architectures and Compilation Techniques*. ACM. [https://doi.org/10.1145/3410463.3414635][research_chelini_2020]
- Chen, Yihan, Huanhuan Chen, Yuan Yao, Ping Yu, Feng Xu, and Xiaoxing Ma. 2025a. "Exploiting Booster Pass Chain for Compiler Phase Ordering." In *Proceedings of the 16th International Conference on Internetware*. ACM. [https://doi.org/10.1145/3755881.3755899][research_chen_2025_b]
- Chen, Junjie, Jiaqi Han, Peiyi Sun, Lingming Zhang, Dan Hao, and Lu Zhang. 2019a. "Compiler Bug Isolation via Effective Witness Test Program Generation." In *Proceedings of the 2019 27th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/3338906.3338957][research_chen_2019]
- Chen, Junjie, Haoyang Ma, and Lingming Zhang. 2020a. "Enhanced Compiler Bug Isolation via Memoized Search." In *Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering*. ACM. [https://doi.org/10.1145/3324884.3416570][research_chen_2020_b]
- Chen, Junjie, and Chenyao Suo. 2022. "Boosting Compiler Testing via Compiler Optimization Exploration." *ACM Transactions on Software Engineering and Methodology* 31 (4): 1–33. [https://doi.org/10.1145/3508362][research_chen_2022]
- Chen, Xiaomeng, Hui Zhang, Hanli Bai, Chunming Yang, Xujian Zhao, and Bo Li. 2020b. "Runtime Prediction of High-Performance Computing Jobs Based on Ensemble Learning." In *Proceedings of the 2020 4th International Conference on High Performance Compilation, Computing and Communications*. ACM. [https://doi.org/10.1145/3407947.3407968][research_chen_2020]
- Chin, Wen-Long. 2022. "Logic Synthesis with Design Compiler." In *Principles of Verilog Digital Design*. CRC Press. [https://doi.org/10.1201/9781003187196-10][research_chin_2022]
- Chippagi, Harinagarjun. 2023. "Evaluation of Coverage Metrics for Assessing Test Suite Effectiveness in RISC-V Core Verification." *International Journal on Recent and Innovation Trends in Computing and Communication* 11 (9): 5680–83. [https://doi.org/10.17762/ijritcc.v11i9.11427][research_chippagi_2023]
- Chouchen, Moataz, Mahi Begoug, and Ali Ouni. 2026. "Beyond Single Code Changes: An Empirical Study of Topic-Based Code Review Practices in Gerrit for OpenStack." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793381][research_chouchen_2026]
- Choudhury, Ziaul, Anish Gulati, and Suresh Purini. 2023. "FlowPix: Accelerating Image Processing Pipelines on an FPGA Overlay Using a Domain Specific Compiler." *ACM Transactions on Architecture and Code Optimization* 20 (4): 1–25. [https://doi.org/10.1145/3629523][research_choudhury_2023]
- Chow, Fred. 2021. "Redundancy Elimination." In *SSA-based Compiler Design*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-80515-9\_11][research_chow_2021]
- Chvatal, V. 1979. "A Greedy Heuristic for the Set-Covering Problem." *Mathematics of Operations Research* 4 (3): 233–35. [https://doi.org/10.1287/moor.4.3.233][research_chvatal_1979]
- Ciano, Tiziana, and Massimiliano Ferrara. 2024. "Shapley Value in Machine Learning Modeling: Optimizing Decision-Making in Coworking Spaces." *Applied Mathematical Sciences* 18 (9): 419–41. [https://doi.org/10.12988/ams.2024.919155][research_ciano_2024]
- Cito, Jürgen, and Harald C. Gall. 2016. "Using Docker Containers to Improve Reproducibility in Software Engineering Research." In *Proceedings of the 38th International Conference on Software Engineering Companion*. ACM. [https://doi.org/10.1145/2889160.2891057][research_cito_2016]
- Clopper, C. J., and E. S. Pearson. 1934. "The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial." *Biometrika* 26 (4): 404–13. [https://doi.org/10.1093/biomet/26.4.404][research_clopper_pearson_1934]
- Codabux, Zadia, and Christopher Dutchyn. 2020. "Profiling Developers through the Lens of Technical Debt." In *Proceedings of the 14th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. ACM. [https://doi.org/10.1145/3382494.3422172][research_codabux_2020]
- Codabux, Zadia, and Byron J. Williams. 2016. "Technical Debt Prioritization Using Predictive Analytics." In *Proceedings of the 38th International Conference on Software Engineering Companion*. ACM. [https://doi.org/10.1145/2889160.2892643][research_codabux_2016]
- Cohen, Eldan, and Mariano P. Consens. 2018. "Large-Scale Analysis of the Co-Commit Patterns of the Active Developers in Github's Top Repositories." In *Proceedings of the 15th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3196398.3196436][research_cohen_2018]
- Condori-Fernandez, Nelly, Maria Fernanda Granda, and Tanja E. J. Vos. 2018. "Towards a Functional Requirements Prioritization with Early Mutation Testing." In *Proceedings of the 5th International Workshop on Requirements Engineering and Testing*. ACM. [https://doi.org/10.1145/3195538.3195539][research_condorifernand_2018]
- Conte, Salvatore Pio, Simone Cosenza, Giacomo Lancellotti, and Giovanni Agosta. 2026. "Compiling Linear Algebra Workloads from C to Quantum Circuits via Multi Level Intermediate Representation." In *Proceedings of the 23rd ACM International Conference on Computing Frontiers: Workshops and Special Sessions*. ACM. [https://doi.org/10.1145/3801488.3806071][research_conte_2026]
- Conway, Melvin E. 1963. "Design of a Separable Transition-Diagram Compiler." *Communications of the ACM* 6 (7): 396–408. [https://doi.org/10.1145/366663.366704][research_conway_1963]
- Cooper, Keith D., and Linda Torczon. 2023a. "Intermediate Representations." In *Engineering a Compiler*. Elsevier. [https://doi.org/10.1016/b978-0-12-815412-0.00010-3][research_cooper_2023]
- Cooper, Keith D., and Linda Torczon. 2023b. "Introduction to Optimization." In *Engineering a Compiler*. Elsevier. [https://doi.org/10.1016/b978-0-12-815412-0.00014-0][research_cooper_2023_b]
- Cooper, Keith D., and Linda Torczon. 2023c. "Syntax-Driven Translation." In *Engineering a Compiler*. Elsevier. [https://doi.org/10.1016/b978-0-12-815412-0.00011-5][research_cooper_2023_c]
- Corral, Ane, Iñigo Díez de Ulzurrun, Alfonso Rodríguez, Sergio Hernández, and Eduardo Casanueva. 2026. "An Embedded RISC-V Vector Extension for Edge-Oriented Acceleration." In *Proceedings of the 23rd ACM International Conference on Computing Frontiers: Workshops and Special Sessions*. ACM. [https://doi.org/10.1145/3801488.3806237][research_corral_2026]
- Cousot, Patrick. 2015. "Verification by Abstract Interpretation, Soundness and Abstract Induction." In *Proceedings of the 17th International Symposium on Principles and Practice of Declarative Programming*. ACM. [https://doi.org/10.1145/2790449.2790451][research_cousot_2015]
- Coviello, Carmen, Simone Romano, and Giuseppe Scanniello. 2018. "An Empirical Study of Inadequate and Adequate Test Suite Reduction Approaches." In *Proceedings of the 12th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement*. ACM. [https://doi.org/10.1145/3239235.3240497][research_coviello_2018]
- Cui, Shuang, Kai Han, Jing Tang, He Huang, Xueying Li, and Zhiyu Li. 2023b. "Streaming Algorithms for Constrained Submodular Maximization." *ACM SIGMETRICS Performance Evaluation Review* 51 (1): 65–66. [https://doi.org/10.1145/3606376.3593573][research_cui_2023_b]
- Cui, Tianming, Pen-Chung Yew, Stephen McCamant, and Antonia Zhai. 2025a. "DeCOS: Data-Efficient Reinforcement Learning for Compiler Optimization Selection Ignited by LLM." In *Proceedings of the 39th ACM International Conference on Supercomputing*. ACM. [https://doi.org/10.1145/3721145.3725765][research_cui_2025_b]
- Curtis, Christopher, Daniel Grissom, and Philip Brisk. 2018. "A Compiler for Cyber-Physical Digital Microfluidic Biochips." In *Proceedings of the 2018 International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3168826][research_curtis_2018]
- Cytron, Ron, Jeanne Ferrante, Barry K. Rosen, Mark N. Wegman, and F. Kenneth Zadeck. 1991. "Efficiently Computing Static Single Assignment Form and the Control Dependence Graph." *ACM Transactions on Programming Languages and Systems* 13 (4): 451–90. [https://doi.org/10.1145/115372.115320][research_cytron_1991]
- Dantas, Emanuel, Alexandre Costa, Marcus Vinicius, Mirko Perkusich, Hyggo Almeida, and Angelo Perkusich. 2019. "An Effort Estimation Support Tool for Agile Software Development: An Empirical Evaluation." In *International Conferences on Software Engineering and Knowledge Engineering*, vol. 2019. KSI Research Inc. and Knowledge Systems Institute Graduate School. [https://doi.org/10.18293/seke2019-141][research_dantas_2019]
- De Boer, Martin, Stijn De Gouw, Jonas Klamroth, Christian Jung, Mattias Ulbrich, and Alexander Weigl. 2023. "Formal Specification and Verification of JDK’s Identity Hash Map Implementation." *Formal Aspects of Computing* 35 (3): 1–26. [https://doi.org/10.1145/3594729][research_deboer_2023]
- de la Torre, Juan Carlos, José Miguel Aragón-Jurado, Javier Jareño, Bernabé Dorronsoro, and Patricia Ruiz. 2025. "A Two-Step Approach to Find Short Compilation Transformation Sequences for Optimal Software Runtime Performance." In *Proceedings of the Genetic and Evolutionary Computation Conference Companion*. ACM. [https://doi.org/10.1145/3712255.3726624][research_delatorre_2025]
- de la Torre, Juan Carlos, Javier Jareño, José Miguel Aragón-Jurado, Sébastien Varrette, and Bernabé Dorronsoro. 2024. "Source Code Obfuscation with Genetic Algorithms Using LLVM Code Optimizations." *Logic Journal of the IGPL* 33 (5): jzae069. [https://doi.org/10.1093/jigpal/jzae069][research_delatorre_2024]
- de Moura, Ana Lúcia, and Roberto Ierusalimschy. 2009. "Revisiting Coroutines." *ACM Transactions on Programming Languages and Systems* 31 (2): 1–31. [https://doi.org/10.1145/1462166.1462167][research_moura_ierusalimschy_2009]
- de Ruck, Dairo, Jef Jacobs, Jorn Lapon, and Vincent Naessens. 2025. "dAngr: Lifting Software Debugging to a Symbolic Level." In *Proceedings 2025 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2025.23014][research_deruck_2025]
- Demange, Delphine, and Yon Fernandez de Retana. 2016. "Mechanizing Conventional SSA for a Verified Destruction with Coalescing." In *Proceedings of the 25th International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/2892208.2892222][research_demange_2016]
- Deng, LiangJun, Hang Lei, Zheng Yang, et al. 2023. "Formal Verification Platform as a Service: WebAssembly Vulnerability Detection Application." *Computer Systems Science and Engineering* 45 (2): 2155–70. [https://doi.org/10.32604/csse.2023.027680][research_deng_2023]
- Deng, Chaoyi, Jialong Wu, Ningya Feng, Jianmin Wang, and Mingsheng Long. 2025. "CompilerDream: Learning a Compiler World Model for General Code Optimization." In *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2*. ACM. [https://doi.org/10.1145/3711896.3736887][research_deng_2025]
- Deole, Akshay, Vanita Agarwal, and Vaishali Ingale. 2024. "Implementation of Application Specific Instruction Set Processor for Approximate Computing." *Wseas Transactions on Computers* 23: 204–10. [https://doi.org/10.37394/23205.2024.23.19][research_deole_2024]
- Detofeno, Thober, Andreia Malucelli, and Sheila Reinehr. 2022. "PriorTD: A Method for Prioritization Technical Debt." In *Proceedings of the XXXVI Brazilian Symposium on Software Engineering*. ACM. [https://doi.org/10.1145/3555228.3555238][research_detofeno_2022]
- Dey, Tonmoy, Yixin Chen, and Alan Kuhnle. 2023. "DASH: A Distributed and Parallelizable Algorithm for Size-Constrained Submodular Maximization." *Proceedings of the AAAI Conference on Artificial Intelligence* 37 (4): 3941–48. [https://doi.org/10.1609/aaai.v37i4.25508][research_dey_2023]
- Dhahbi, S., and I. Schmitt. 2026. "P30: Möbius-Shapley: Native Feature Attribution for Quantum Logic." In *Poster*. AMA Service GmbH, Von-Münchhausen-Str. 49, 31515 Wunstorf, Germany. [https://doi.org/10.5162/iccc2026/p30][research_dhahbi_2026]
- Dickerson, Mitchel, Anand Srinivasan, and Michael Franz. 2026. "Practical Python FPGA Acceleration with Fast Just-In-Time Compilation and Configuration." *ACM Transactions on Architecture and Code Optimization* 23 (1): 1–25. [https://doi.org/10.1145/3797265][research_dickerson_2026]
- Ding, Chen, Dong Chen, Fangzhou Liu, Benjamin Reber, and Wesley Smith. 2022a. "CARL: Compiler Assigned Reference Leasing." *ACM Transactions on Architecture and Code Optimization* 19 (1): 1–28. [https://doi.org/10.1145/3498730][research_ding_2022_b]
- Ding, Junhua, Dongmei Zhang, and Xin-Hua Hu. 2016. "An Application of Metamorphic Testing for Testing Scientific Software." In *Proceedings of the 1st International Workshop on Metamorphic Testing*. ACM. [https://doi.org/10.1145/2896971.2896981][research_ding_2016]
- Doerfert, Johannes, Marc Jasper, Joseph Huber, et al. 2022. "Breaking the Vendor Lock: Performance Portable Programming through OpenMP as Target Independent Runtime Layer." In *Proceedings of the International Conference on Parallel Architectures and Compilation Techniques*. ACM. [https://doi.org/10.1145/3559009.3569687][research_doerfert_2022]
- Donaldson, Alastair F., and Andrei Lascu. 2016. "Metamorphic Testing for (Graphics) Compilers." In *Proceedings of the 1st International Workshop on Metamorphic Testing*. ACM. [https://doi.org/10.1145/2896971.2896978][research_donaldson_2016]
- Du, Xianda, and Ke Qin. 2026. "RE-APR: Reasoning-Enhanced Automated Program Repair via Large Language Models." In *Proceedings of the 2026 9th International Conference on Software Engineering and Information Management*. ACM. [https://doi.org/10.1145/3796315.3796332][research_du_2026]
- Duan, Hui, and Giray Okten. 2025. "Derivative-Based Shapley Value for Global Sensitivity Analysis and Machine Learning Explainability." *International Journal for Uncertainty Quantification* 15 (1): 1–16. [https://doi.org/10.1615/int.j.uncertaintyquantification.2024051548][research_duan_2025]
- Dupont de Dinechin, Benoît. 2021. "SSA Form and Code Generation." In *SSA-based Compiler Design*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-80515-9\_18][research_dupontdedinech_2021]
- Durieux, Thomas, Claire Le Goues, Michael Hilton, and Rui Abreu. 2020. "Empirical Study of Restarted and Flaky Builds on Travis CI." In *Proceedings of the 17th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3379597.3387460][research_durieux_2020]
- Dzulqarnain, Muhammad Faqih, Abdul Fadlil, and Imam Riadi. 2024. "Improving the Accuracy of Batik Classification Using Deep Convolutional Auto Encoder." *Compiler* 13 (2): 123. [https://doi.org/10.28989/compiler.v13i2.2649][research_dzulqarnain_2024]
- Ebner, Dietmar, Andreas Krall, and Bernhard Scholz. 2021. "Instruction Code Selection." In *SSA-based Compiler Design*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-80515-9\_19][research_ebner_2021]
- Ebrahim, Fahad, and Mike Joy. 2023. "Source Code Plagiarism Detection with Pre-Trained Model Embeddings and Automated Machine Learning." In *Proceedings of the Conference Recent Advances in Natural Language Processing - Large Language Models for Natural Language Processings*. INCOMA Ltd., Shoumen, BULGARIA. [https://doi.org/10.26615/978-954-452-092-2\_034][research_anon_2023]
- Ecker, Wolfgang, and Johannes Schreiner. 2017. "Metamodeling and Code Generation in the Hardware/Software Interface Domain." In *Handbook of Hardware/Software Codesign*. Springer Netherlands. [https://doi.org/10.1007/978-94-017-7267-9\_32][research_ecker_2017]
- Efthymiou, Stavros, Marco Lazzarin, Andrea Pasquale, and Stefano Carrazza. 2022. "Quantum Simulation with Just-in-Time Compilation." *Quantum* 6: 814. [https://doi.org/10.22331/q-2022-09-22-814][research_efthymiou_2022]
- Elkhouly, Reem, Mohammad Alshboul, Akihiro Hayashi, Yan Solihin, and Keiji Kimura. 2019. "Compiler-Support for Critical Data Persistence in NVM." *ACM Transactions on Architecture and Code Optimization* 16 (4): 1–25. [https://doi.org/10.1145/3371236][research_elkhouly_2019]
- Enders, Steffen, Eva-Maria C. Behner, Niklas Bergmann, et al. 2023. "Dewolf: Improving Decompilation by Leveraging User Surveys." In *Proceedings 2023 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2023.23001][research_enders_2023]
- Endo, Fernando A., Arthur Perais, and André Seznec. 2017. "On the Interactions between Value Prediction and Compiler Optimizations in the Context of EOLE." *ACM Transactions on Architecture and Code Optimization* 14 (2): 1–24. [https://doi.org/10.1145/3090634][research_endo_2017]
- Eom, Jueon, Seyeon Jeong, and Taekyoung Kwon. 2024. "Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation." In *Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3650212.3680389][research_eom_2024]
- Epasto, Alessandro, Vahab Mirrokni, and Morteza Zadimoghaddam. 2017. "Bicriteria Distributed Submodular Maximization in a Few Rounds." In *Proceedings of the 29th ACM Symposium on Parallelism in Algorithms and Architectures*. ACM. [https://doi.org/10.1145/3087556.3087574][research_epasto_2017]
- Even-Mendoza, Karine, Arindam Sharma, Alastair F. Donaldson, and Cristian Cadar. 2023. "GrayC: Greybox Fuzzing of Compilers and Analysers for C." In *Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3597926.3598130][research_evenmendoza_2023]
- Fakhoury, Sarah, Aaditya Naik, Georgios Sakkas, Saikat Chakraborty, Madan Musuvathi, and Shuvendu Lahiri. 2024. "Exploring the Effectiveness of LLM Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation." In *Proceedings of the 2024 IEEE/ACM 46th International Conference on Software Engineering: Companion Proceedings*. ACM. [https://doi.org/10.1145/3639478.3643525][research_fakhoury_2024]
- Fanyi Zhao, Mingzhuo Yu, and Chuankai Luo. 2024. "A Comparative Evaluation of Prompting Strategies for Code Generation with Large Language Models." *Journal of Global Engineering Review* 2 (1): 1–11. [https://doi.org/10.66372/jger.v2i1.1][research_fanyizhao_2024]
- Feige, Uriel. 1998. "A Threshold of Ln n for Approximating Set Cover." *Journal of the ACM* 45 (4): 634–52. [https://doi.org/10.1145/285055.285059][research_feige_1998]
- Feischl, Christof, and Roman Kern. 2026. "Large Language Models for Code Translation: An in-Depth Analysis of Code Smells and Functional Correctness." *ACM Transactions on Software Engineering and Methodology* 35 (8): 1–40. [https://doi.org/10.1145/3777383][research_feischl_2026]
- Felbinger, Hermann, Franz Wotawa, and Mihai Nica. 2016. "Empirical Study of Correlation between Mutation Score and Model Inference Based Test Suite Adequacy Assessment." In *Proceedings of the 11th International Workshop on Automation of Software Test*. ACM. [https://doi.org/10.1145/2896921.2896923][research_felbinger_2016]
- Felderer, Michael, and Guilherme Horta Travassos. 2020. "The Evolution of Empirical Methods in Software Engineering." In *Contemporary Empirical Methods in Software Engineering*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-32489-6\_1][research_felderer_2020]
- Feldman, Moran, Paul Liu, Ashkan Norouzi-Fard, Ola Svensson, and Rico Zenklusen. 2026. "Streaming Submodular Maximization under Matroid Constraints." *Mathematics of Operations Research* 51 (1): 299–332. [https://doi.org/10.1287/moor.2023.0276][research_feldman_2026]
- Felfernig, Alexander. 2021. "AI Techniques for Software Requirements Prioritization." In *Artificial Intelligence Methods for Software Engineering*. WORLD SCIENTIFIC. [https://doi.org/10.1142/9789811239922\_0002][research_felfernig_2021]
- Ferrante, Jeanne, Karl J. Ottenstein, and Joe D. Warren. 1987. "The Program Dependence Graph and Its Use in Optimization." *ACM Transactions on Programming Languages and Systems* 9 (3): 319–49. [https://doi.org/10.1145/24039.24041][research_ferrante_1987]
- Fraser, Christopher W., David R. Hanson, and Todd A. Proebsting. 1992. "Engineering a Simple, Efficient Code-Generator Generator." *ACM Letters on Programming Languages and Systems* 1 (3): 213–26. [https://doi.org/10.1145/151640.151642][research_fraser_1992]
- Gan, Maohua, Zeynep YÜCel, Akito Monden, and Kentaro Sasaki. 2020. "Empirical Evaluation of Mimic Software Project Data Sets for Software Effort Estimation." *IEICE Transactions on Information and Systems* E103.D (10): 2094–2103. [https://doi.org/10.1587/transinf.2019edp7150][research_gan_2020]
- Gao, Bingyu, Ziming Wang, Mengyu Yao, et al. 2026. "PredComp: Predicting Compiler Optimization Options with Multi-Stage Learning." *ACM Transactions on Architecture and Code Optimization* 23 (2): 1–25. [https://doi.org/10.1145/3820771][research_gao_2026]
- Garoche, Pierre-Loïc. 2019. "Floating-Point Semantics of Analyzed Programs." In *Formal Verification of Control System Software*. Princeton University Press. [https://doi.org/10.23943/princeton/9780691181301.003.0009][research_garoche_2019]
- Garrido-Lucero, Felipe, Benjamin Heymann, Maxime Vono, Patrick Loiseau, and Vianney Perchet. 2024. "DU-Shapley: A Shapley Value Proxy for Efficient Dataset Valuation." In *Advances in Neural Information Processing Systems 37*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/079017-0063][research_garridolucero_2024]
- Gauthier, Louis, Virgile Prevosto, and Julien Signoles. 2024. "A Semantics of Structures, Unions, and Underspecified Terms for Formal Specification." In *Proceedings of the 2024 IEEE/ACM 12th International Conference on Formal Methods in Software Engineering (FormaliSE)*. ACM. [https://doi.org/10.1145/3644033.3644380][research_gauthier_2024]
- Georgakoudis, Giorgis, Konstantinos Parasyris, and David Beckingsale. 2025. "Proteus: Portable Runtime Optimization of GPU Kernel Execution with Just-in-Time Compilation." In *Proceedings of the 23rd ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3696443.3708939][research_georgakoudis_2025]
- Georgiou, Kyriakos, Zbigniew Chamski, Andres Amaya Garcia, David May, and Kerstin Eder. 2020. "Lost in Translation: Exposing Hidden Compiler Optimization Opportunities." *Computer Journal* 65 (3): 718–35. [https://doi.org/10.1093/comjnl/bxaa103][research_georgiou_2020]
- Ghammam, Anwar, and Mohamed Almukhtar. 2026. "AI Builds, We Analyze: An Empirical Study of AI-Generated Build Code Quality." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793563][research_ghammam_2026]
- Ginsbach, Philip, Lewis Crawford, and Michael F. P. O'Boyle. 2018. "CAnDL: A Domain Specific Language for Compiler Analysis." In *Proceedings of the 27th International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3178372.3179515][research_ginsbach_2018]
- Girault, Alain. 2025. "Toward a Formally Verified Compiler for a Synchronous, Functional, Data-Flow Programming Language." *Communications of the ACM* 69 (1): 92–92. [https://doi.org/10.1145/3768311][research_girault_2025]
- Gliwa, Peter. 2021a. "Practical Examples of Timing Problems." In *Embedded Software Timing*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-64144-3\_6][research_gliwa_2021]
- Gliwa, Peter. 2021b. "Timing Analysis Techniques." In *Embedded Software Timing*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-64144-3\_5][research_gliwa_2021_b]
- Goli, Alireza, and Taha Keshavarz. 2022. "Just-in-Time Scheduling in Identical Parallel Machine Sequence-Dependent Group Scheduling Problem." *Journal of Industrial and Management Optimization* 18 (6): 3807. [https://doi.org/10.3934/jimo.2021124][research_goli_2022]
- Gomes, Tchalisson Brenne S., Diogo Alves de Moura Loiola, and Alcemir Rodrigues Santos. 2024. "Technical Debt Tools: A Survey and an Empirical Evaluation." *Journal of Software Engineering Research and Development* 12 (1). [https://doi.org/10.5753/jserd.2024.3591][research_gomes_2024]
- Gonçalves dos Santos, Marcela, Sylvain Hallé, and Fábio Petrillo. 2025. "Mutation Testing for Industrial Robotic Systems." *Electronic Proceedings in Theoretical Computer Science* 436: 31–47. [https://doi.org/10.4204/eptcs.436.5][research_goncalvesdossa_2025]
- Gong, Qingin, Suixiang Gao, Fengmin Wang, and Ruiqi Yang. 2024. "Multipass Streaming Algorithms for Regularized Submodular Maximization." *Tsinghua Science and Technology* 29 (1): 76–85. [https://doi.org/10.26599/tst.2023.9010026][research_gong_2024]
- Gorius, Jean-Michel, Arthur Perais, and Erven Rohou. 2026. "Exploring Instruction Set Extension Emulation for Long-Term Support of RISC-V Processors." In *Proceedings of the 23rd ACM International Conference on Computing Frontiers: Workshops and Special Sessions*. ACM. [https://doi.org/10.1145/3801488.3807478][research_gorius_2026]
- Gourdin, Léo. 2023. "Lazy Code Transformations in a Formally Verified Compiler." In *Proceedings of the 18th ACM International Workshop on Implementation, Compilation, Optimization of OO Languages, Programs and Systems*. ACM. [https://doi.org/10.1145/3605158.3605848][research_gourdin_2023_b]
- Gromova, Ekaterina. 2016. "The Shapley Value as a Sustainable Cooperative Solution in Differential Games of Three Players." In *Static & Dynamic Game Theory: Foundations & Applications*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-43838-2\_4][research_gromova_2016]
- Grotov, Konstantin, Sergey Titov, Vladimir Sotnikov, Yaroslav Golubev, and Timofey Bryksin. 2022. "A Large-Scale Comparison of Python Code in Jupyter Notebooks and Scripts." In *Proceedings of the 19th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3524842.3528447][research_grotov_2022]
- Guan, Nan. 2016a. "FIFO Cache Analysis for WCET Estimation." In *Techniques for Building Timing-Predictable Embedded Systems*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-27198-9\_3][research_guan_2016]
- Guan, Nan. 2016b. "MRU Cache Analysis for WCET Estimation." In *Techniques for Building Timing-Predictable Embedded Systems*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-27198-9\_2][research_guan_2016_b]
- Guo, Luanzheng, Rizwan A. Ashraf, Ryan D. Friese, and Gokcen Kestor. 2022. "Towards Supporting Semiring in MLIR-Based COMET Compiler." In *Proceedings of the International Conference on Parallel Architectures and Compilation Techniques*. ACM. [https://doi.org/10.1145/3559009.3569683][research_guo_2022]
- Guo, Jingdong, Chaopeng Dong, Yimo Ren, et al. 2026b. "Understanding Binary Code Similarity for Real-World Vulnerability Detection: A Large-Scale Empirical Study." *Proceedings of the ACM on Software Engineering* 3 (FSE): 657–77. [https://doi.org/10.1145/3797125][research_guo_2026]
- Gupta, Ankita, and Chetna Gupta. 2021. "A Collaborative Effort-Benefit-Value Analysis Model to Support Requirements Reuse for Software Requirements Prioritization." *International Journal of Software Innovation* 9 (1): 37–51. [https://doi.org/10.4018/ijsi.2021010104][research_gupta_2021]
- Gupta, Priya, Terala ManiKiran, Mailapalli Purushotham, L. Jeya Suriya, Rasamsetty Naga Venkata, and Sambhudutta Nanda. 2023. "Efficient Compiler Design for a Geometric Shape Domain-Specific Language: Emphasizing Abstraction and Optimization Techniques." *ICST Transactions on Scalable Information Systems*. [https://doi.org/10.4108/eetsis.4346][research_gupta_2023]
- Gussoni, Andrea, Alessandro Di Federico, Pietro Fezzardi, and Giovanni Agosta. 2019. "Performance, Correctness, Exceptions: Pick Three." In *Proceedings 2019 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2019.23093][research_gussoni_2019]
- Gustafson, John L. 1988. "Reevaluating Amdahl's Law." *Communications of the ACM* 31 (5): 532–33. [https://doi.org/10.1145/42411.42415][research_gustafson_1988]
- Hafizhah, Nurul, and Ahmad Tri Hidayat. 2024. "Automated Testing to Evaluate Employee Attendance System Performance Using Gtmetrix." *Compiler* 13 (2): 131. [https://doi.org/10.28989/compiler.v13i2.2685][research_hafizhah_2024]
- Haidl Michael, Hagedorn Bastian, and Gorlatch Sergei. 2016. "Programming GPUs with C++14 and Just-In-Time Compilation." In *Advances in Parallel Computing*. IOS Press. [https://doi.org/10.3233/978-1-61499-621-7-247][research_haidlmichael_2016]
- Haj-Yihia, Jawad, Yosi Ben Asher, Efraim Rotem, Ahmad Yasin, and Ran Ginosar. 2015. "Compiler-Directed Power Management for Superscalars." *ACM Transactions on Architecture and Code Optimization* 11 (4): 1–21. [https://doi.org/10.1145/2685393][research_hajyihia_2015]
- Hakimi, Yacine, Riyadh Baghdadi, and Yacine Challal. 2025. "Supporting Dynamic Program Sizes in Deep Learning-Based Cost Models for Code Optimization." *ACM Transactions on Architecture and Code Optimization* 22 (2): 1–25. [https://doi.org/10.1145/3727638][research_hakimi_2025]
- Halmans, Sjoerd, Lavinia Paganini, Alexander Serebrenik, and Alexander Nolte. 2026. "HackRep: A Large-Scale Dataset of GitHub Hackathon Projects." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793305][research_halmans_2026]
- Hamdi, Fatmaelzahra, Ramadan Moawad, and Amr Mansour Mohsen. 2026. "A Systematic Literature Review on Automated Program Repair Using Large Language Models." *JUCS - Journal of Universal Computer Science* 32 (7): 1031–70. [https://doi.org/10.3897/jucs.171035][research_hamdi_2026]
- Han, Yanan, Gang Chen, and Bin Han. 2023. "An Improved Method for Test Case Prioritization in Continuous Integration Based on Reinforcement Learning." In *Atlantis Highlights in Engineering*. Atlantis Press International BV. [https://doi.org/10.2991/978-94-6463-262-0\_99][research_han_2023]
- Hanley, James A., and Abby Lippman-Hand. 1983. "If Nothing Goes Wrong, Is Everything All Right?: Interpreting Zero Numerators." *JAMA* 249 (13): 1743. [https://doi.org/10.1001/jama.1983.03330370053031][research_hanley_1983]
- Haque, Obaidul, Anwar Hossen, and Sharmin Akter. 2020. "A Cooperative Game Theory Application in Chicks Brood Food Allocation by Using Shapley Value Method in Good Years Data." *ITEGAM- Journal of Engineering and Technology for Industrial Applications (ITEGAM-JETIA)* 5 (25). [https://doi.org/10.5935/jetia.v6i25.692][research_haque_2020]
- Harish, M. S. M. S., and D. Jayadevappa. 2018. "Design & Simulation of 64-Bit Hybrid Processor Instruction Set Using Verilog." *International Journal of Engineering & Technology* 7 (4.36): 373. [https://doi.org/10.14419/ijet.v7i4.36.23809][research_ms_2018]
- Harrold, M. Jean, Rajiv Gupta, and Mary Lou Soffa. 1993. "A Methodology for Controlling the Size of a Test Suite." *ACM Transactions on Software Engineering and Methodology* 2 (3): 270–85. [https://doi.org/10.1145/152388.152391][research_harrold_1993]
- Hartley, Tim, Foivos S. Zakkak, Andy Nisbet, Christos Kotselidis, and Mikel Luján. 2022. "Just-In-Time Compilation on ARM—a Closer Look at Call-Site Code Consistency." *ACM Transactions on Architecture and Code Optimization* 19 (4): 1–23. [https://doi.org/10.1145/3546568][research_hartley_2022]
- Haßler, Keno, and Dominik Maier. 2021. "WAFL: Binary-Only WebAssembly Fuzzing with Fast Snapshots." In *Reversing and Offensive-oriented Trends Symposium*. ACM. [https://doi.org/10.1145/3503921.3503924][research_haler_2021]
- Hausladen, Jürgen, Florian Gerstmayer, Thomas Jerabek, and Martin Horauer. 2017. "Integration of Static Worst-Case Execution Time and Stack Usage Analysis for Embedded Systems Software in a Cloud-Based Development Environment." In *Volume 9: 13th ASME/IEEE International Conference on Mechatronic and Embedded Systems and Applications*. American Society of Mechanical Engineers. [https://doi.org/10.1115/detc2017-67402][research_hausladen_2017]
- Hayashi, Akihiro, Jisheng Zhao, Michael Ferguson, and Vivek Sarkar. 2015. "LLVM-Based Communication Optimizations for PGAS Programs." In *Proceedings of the Second Workshop on the LLVM Compiler Infrastructure in HPC*. ACM. [https://doi.org/10.1145/2833157.2833164][research_hayashi_2015]
- He, Wenju, Maosu Zhao, Yuxin Zou, and Feng Zou. 2023. "Profile Guided Optimization Transfer-Learning for OpenCL/SYCL Kernel Compilation and Runtime." In *International Workshop on OpenCL*. ACM. [https://doi.org/10.1145/3585341.3585359][research_he_2023]
- He, Yan, Zixuan Zhou, and Eun-Soon Im. 2024. *Codes for Machine Learning and Shapley Value Analysis*. The Hong Kong University of Science and Technology Library. [https://doi.org/10.14711/dataset/9zoato][research_he_2024]
- Heckel, Kade. 2023. "Neuroevolutionary Compiler Control for Code Optimization." In *Proceedings of the Companion Conference on Genetic and Evolutionary Computation*. ACM. [https://doi.org/10.1145/3583133.3596380][research_heckel_2023]
- Heidari Iman, Mohammad Reza. 2025a. "Automatic Generation of Assertions for Functional Verification." In *Advanced Techniques for Assertion-Based Verification in Hardware Designs Using Data Mining Algorithms*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-90410-3\_4][research_heidariiman_2025_b]
- Heidari Iman, Mohammad Reza. 2025b. "Automatic Generation of Assertions for Security Verification." In *Advanced Techniques for Assertion-Based Verification in Hardware Designs Using Data Mining Algorithms*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-90410-3\_6][research_heidariiman_2025]
- Heim, Bettina. 2018. "Compiler and Language Design for Quantum Computing (Keynote)." In *Proceedings of the 27th International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3178372.3183636][research_heim_2018]
- Heo, Ingoo, Minsu Kim, Yongje Lee, et al. 2015. "Implementing an Application-Specific Instruction-Set Processor for System-Level Dynamic Program Analysis Engines." *ACM Transactions on Design Automation of Electronic Systems* 20 (4): 1–32. [https://doi.org/10.1145/2746238][research_heo_2015]
- Herbold, Steffen, Alexander Trautsch, and Benjamin Ledel. 2020. "Large-Scale Manual Validation of Bugfixing Changes." In *Proceedings of the 17th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3379597.3387504][research_herbold_2020]
- Hilbig, Aaron, Daniel Lehmann, and Michael Pradel. 2021. "An Empirical Study of Real-World WebAssembly Binaries: Security, Languages, Use Cases." In *Proceedings of the Web Conference 2021*. ACM. [https://doi.org/10.1145/3442381.3450138][research_hilbig_2021]
- Himschoot, Peter. 2020a. "Conclusion: Debugging Blazor WebAssembly." In *Practical Blazor Debugging*. Apress. [https://doi.org/10.1007/978-1-4842-6592-5\_8][research_himschoot_2020]
- Himschoot, Peter. 2020b. "Targeting Both Blazor Server and Blazor WebAssembly." In *Practical Blazor Debugging*. Apress. [https://doi.org/10.1007/978-1-4842-6592-5\_3][research_himschoot_2020_b]
- Hongbo, Zhou, and Zhao Chunyan. 2015. "14. Compilation of Dictionaries of the Chinese Language." In *The Language Situation in China, Volume 3*. DE GRUYTER. [https://doi.org/10.1515/9781501503146-015][research_hongbo_2015]
- Hora, Andre. 2026. "GitEvo: Code Evolution Analysis for Git Repositories." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793327][research_hora_2026_b]
- Hora, Andre, and Gordon Fraser. 2026. "Understanding Bug-Reproducing Tests: A First Empirical Study." In *Proceedings of the 7th ACM/IEEE International Conference on Automation of Software Test*. ACM. [https://doi.org/10.1145/3793654.3793752][research_hora_2026]
- Hosseini, Iman, and Brendan Dolan-Gavitt. 2022. "Beyond the C: Retargetable Decompilation Using Neural Machine Translation." In *Proceedings 2022 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2022.23009][research_hosseini_2022]
- Hsu, Chin-Chia, Che-Yu Wu, Hsu-Chun Hsiao, and Shih-Kun Huang. 2018. "INSTRIM: Lightweight Instrumentation for Coverage-Guided Fuzzing." In *Proceedings 2018 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2018.23014][research_hsu_2018]
- Hu, Qinheping, John Cyphert, Loris D'Antoni, and Thomas Reps. 2020a. *Artifact for Article: Exact and Approximate Methods for Proving Unrealizability of Syntax-Guided Synthesis Problems*. Association for Computing Machinery (ACM). [https://doi.org/10.1145/3395631][research_hu_2020]
- Hu, Daijin, Nan Wang, Zilong Cheng, and Yilong Yang. 2026a. "Empirical Study on Real-Time System Modeling and Code Generation Based on Simulink/SCADE." *Manned Spaceflight* 32 (1): 88–96. [https://doi.org/10.3724/zrht.1674-5825.2025039][research_hu_2026_b]
- Humbatova, Nargiz, Gunel Jahangirova, and Paolo Tonella. 2021. "DeepCrime: Mutation Testing of Deep Learning Systems Based on Real Faults." In *Proceedings of the 30th ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3460319.3464825][research_humbatova_2021]
- Ibriwesh, Iyas, Sin-Ban Ho, Ian Chai, and Chuie-Hong Tan. 2018. "Prioritizing Solution-Oriented Software Requirements Using the Multiple Perspective Prioritization Technique Algorithm: An Empirical Investigation." *Concurrent Engineering* 27 (1): 68–79. [https://doi.org/10.1177/1063293x18808559][research_ibriwesh_2018]
- Ilesanmi, Solanke, Alomaja Victor Ojumu, Ajayi Abiodun Folurera, and Ajao Aisha Omorinbola. 2021. "Empirical Investigation of Cloud, Grid and Virtualization Using Compiler Optimization Level for Threads Processes." *International Journal of Innovative Research in Computer Science & Technology* 9 (5). [https://doi.org/10.21276/ijircst.2021.9.5.5][research_ilesanmi_2021]
- Imran, Muhammad, Vittorio Cortellessa, Davide Di Ruscio, Riccardo Rubei, and Luca Traini. 2024. "An Empirical Study on Code Coverage of Performance Testing." In *Proceedings of the 28th International Conference on Evaluation and Assessment in Software Engineering*. ACM. [https://doi.org/10.1145/3661167.3661196][research_imran_2024]
- Inozemtseva, Laura, and Reid Holmes. 2014. "Coverage Is Not Strongly Correlated with Test Suite Effectiveness." In *Proceedings of the 36th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/2568225.2568271][research_inozemtseva_holmes_2014]
- Ioannidis, John P. A. 2005. "Why Most Published Research Findings Are False." *PLoS Medicine* 2 (8): e124. [https://doi.org/10.1371/journal.pmed.0020124][research_ioannidis_2005]
- Iqbal, Danish, Sher Badshah, and Irfan Kazim. 2022. "The Influence of Cost Drivers on Effort Estimation in Distributed Software Development." In *The International Conference on Evaluation and Assessment in Software Engineering 2022*. ACM. [https://doi.org/10.1145/3530019.3531331][research_iqbal_2022]
- Iqbal, Salwa, and Kashif Sheikh. 2024. "Machine Learning Based Compiler Optimization Technique." *Sukkur IBA Journal of Emerging Technologies* 7 (1): 37–47. [https://doi.org/10.30537/sjet.v7i1.1428][research_iqbal_2024]
- Islam, Md Ashraful, and Kenji Kise. 2023. "Resource-Efficient RISC-V Vector Extension Architecture for FPGA-Based Accelerators." In *Proceedings of the 13th International Symposium on Highly Efficient Accelerators and Reconfigurable Technologies*. ACM. [https://doi.org/10.1145/3597031.3597047][research_islam_2023]
- Izawa, Yusuke, Hidehiko Masuhara, Carl Friedrich Bolz-Tereick, and Youyou Cong. 2022. "Threaded Code Generation with a Meta-Tracing JIT Compiler." *Journal of Object Technology* 21 (2): 2:1. [https://doi.org/10.5381/jot.2022.21.2.a1][research_izawa_2022]
- Jain, Shashank Mohan. 2021. "WebAssembly Module Internals: Sections and Memory Model." In *WebAssembly for Cloud*. Apress. [https://doi.org/10.1007/978-1-4842-7496-5\_2][research_jain_2021]
- Jakhar, Amit Kumar, and Kumar Rajnish. 2015. "An Empirical Approach for Estimation of the Software Development Effort." *International Journal of Multimedia and Ubiquitous Engineering* 10 (2): 97–110. [https://doi.org/10.14257/ijmue.2015.10.2.09][research_jakhar_2015]
- Jaskirat, Kaur, and Kaur Navdeep. 2026. "A Rigorous Empirical Benchmark of Machine Learning Models for Software Effort Estimation." *International Journal of Performability Engineering* 22 (4): 188. [https://doi.org/10.23940/ijpe.26.04.p2.188199][research_jaskirat_2026]
- Jayatilaka, Tarindu, Hideto Ueno, Giorgis Georgakoudis, EunJung Park, and Johannes Doerfert. 2021. "Towards Compile-Time-Reducing Compiler Optimization Selection via Machine Learning." In *50th International Conference on Parallel Processing Workshop*. ACM. [https://doi.org/10.1145/3458744.3473355][research_jayatilaka_2021]
- Jensen, J. L. W. V. 1906. "Sur Les Fonctions Convexes Et Les Inégalités Entre Les Valeurs Moyennes." *Acta Mathematica* 30 (0): 175–93. [https://doi.org/10.1007/bf02418571][research_jensen_1906]
- Jesus, Ricardo, and Michèle Weiland. 2024. "Evaluating and Optimising Compiler Code Generation for NVIDIA Grace." In *Proceedings of the 53rd International Conference on Parallel Processing*. ACM. [https://doi.org/10.1145/3673038.3673104][research_jesus_2024]
- Jeyaram, Anitha Gracy, Chandrakumar Thangavel, Parthasarathy Sudhaman, Vaishnavi Vijayaragavan, and Premnitin Premkanth. 2025. "Software Effort Estimation Using Validated Accuracy Points for Open-Source Packaged Software." *International Journal of Productivity and Quality Management* 46 (4): 481–99. [https://doi.org/10.1504/ijpqm.2025.150888][research_jeyaram_2025]
- Ji, Zhenlan, Pingchuan Ma, Zongjie Li, Zhaoyu Wang, and Shuai Wang. 2025. "Causality-Aided Evaluation and Explanation of Large Language Model-Based Code Generation." *Proceedings of the ACM on Software Engineering* 2 (ISSTA): 1374–97. [https://doi.org/10.1145/3728938][research_ji_2025]
- Jian, Zexin, Shuhui Jia, Chunwei Xia, Di Wang, and Chenxi Wang. 2026. "RV-IR: An MLIR-Based Architecture-Aware Intermediate Representation for Heterogeneous RISC-V AI Acceleration." In *Proceedings of the 40th ACM International Conference on Supercomputing - Workshops*. ACM. [https://doi.org/10.1145/3774895.3812195][research_jian_2026]
- Jimoh, Yusuf O., Jiawei Zhang, Hyuma Umeda, Bhavin J. Shastri, and Paul R. Prucnal. 2026. "An Ultralow-Latency Constrained Quadratic Program (QP) Solver Based on an Integrated Photonic Recurrent Neural Network." In *CLEO 2026*. Optica Publishing Group. [https://doi.org/10.1364/cleo\_si.2026.sw2d.7][research_jimoh_2026]
- Jones, R. 2023. "An Extension to the RISC-V Instruction Set Architecture for Quantum Systems." *IET Conference Proceedings* 2023 (25): 65–67. [https://doi.org/10.1049/icp.2023.3273][research_jones_2023]
- Jones, Timothy, and David J. Pearce. 2016. "A Mechanical Soundness Proof for Subtyping over Recursive Types." In *Proceedings of the 18th Workshop on Formal Techniques for Java-like Programs*. ACM. [https://doi.org/10.1145/2955811.2955812][research_jones_2016]
- Jorgensen, Paul C. 2018. "Equivalence Class Testing." In *Software Testing*. Auerbach Publications. [https://doi.org/10.1201/b15980-7][research_jorgensen_2018]
- Jureczko, Marian, Łukasz Kajda, and Paweł Górecki. 2020. "Code Review Effectiveness: An Empirical Study on Selected Factors Influence." *IET Software* 14 (7): 794–805. [https://doi.org/10.1049/iet-sen.2020.0134][research_jureczko_2020]
- Just, René, Darioush Jalali, Laura Inozemtseva, Michael D. Ernst, Reid Holmes, and Gordon Fraser. 2014. "Are Mutants a Valid Substitute for Real Faults in Software Testing?" In *Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/2635868.2635929][research_just_2014]
- Kadam, Sandeep U., Sagar B. Shinde, Yogesh B. Gurav, Sunil B. Dambhare, and Chaitali R. Shewale. 2022. "A Novel Prediction Model for Compiler Optimization with Hybrid Meta-Heuristic Optimization Algorithm." *International Journal of Advanced Computer Science and Applications* 13 (10). [https://doi.org/10.14569/ijacsa.2022.0131068][research_kadam_2022]
- Kaestner, Daniel, Gernot Gebhard, Christian Huembert, Markus Pister, Simon Wegener, and Christian Ferdinand. 2025. "Determining Worst-Case Execution Time Bounds for Multi-Core Processors." In *SAE Technical Paper Series*, vol. 1. SAE International. [https://doi.org/10.4271/2025-01-0155][research_kaestner_2025]
- Kalle, Sushma, Nehal Ameen, Hyunguk Yoo, and Irfan Ahmed. 2019. "CLIK on PLCs! Attacking Control Logic with Decompilation and Virtual PLC." In *Proceedings 2019 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2019.23074][research_kalle_2019]
- Kamkin, Alexander Sergeevich, Mikhail Yurievich Litvinov, and Ivan Aleksandrovich Grigorov. 2024. "Open-Source MLIR-Based Intermediate Representation for Applica-Tion-Specific Streaming Computers." *Proceedings of the Institute for System Programming of the RAS* 36 (5): 31–46. [https://doi.org/10.15514/ispras-2024-36(5)-3][research_kamkin_2024]
- Kang, Seokhyeon, Moohyun Song, Taeyoon Kim, et al. 2025. "HybridServe: Adaptive WebAssembly-Container Runtime Selection for Edge Serverless Computing." In *Proceedings of the 11th International Workshop on Serverless Computing*. ACM. [https://doi.org/10.1145/3774899.3775011][research_kang_2025]
- Kang, Sungmin, and Shin Yoo. 2022. "Language Models Can Prioritize Patches for Practical Program Patching." In *Proceedings of the Third International Workshop on Automated Program Repair*. ACM. [https://doi.org/10.1145/3524459.3527343][research_kang_2022]
- Kao, Chien-Lung. 2025. "From Source to Bytecode: How.py Becomes.pyc." In *CPython*. Apress. [https://doi.org/10.1007/979-8-8688-1769-4\_13][research_kao_2025]
- Kapitsaki, Georgia, Loukas Chatzivasili, Maria Papoutsoglou, and Matthias Galster. 2024. "An Exploratory Study on Soft Skills Present in Software Positions in Cyprus: A Quasi-Replication Study." In *Proceedings of the 18th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement*. ACM. [https://doi.org/10.1145/3674805.3686681][research_kapitsaki_2024]
- Karampatsis, Rafael-Michael, Hlib Babii, Romain Robbes, Charles Sutton, and Andrea Janes. 2020. "Big Code != Big Vocabulary: Open-Vocabulary Models for Source Code." In *Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3377811.3380342][research_karampatsis_2020]
- Karp, Richard M. 1972. "Reducibility among Combinatorial Problems." In *Complexity of Computer Computations*. Springer US. [https://doi.org/10.1007/978-1-4684-2001-2\_9][research_karp_1972]
- Karuppusamy, P. 2020. "Effective Test Suite Optimization for Improving the Coverage Standards Using Hybrid Wrapper Filter Memetic Algorithm." *Journal of Soft Computing Paradigm* 2 (2): 83–91. [https://doi.org/10.36548/jscp.2020.2.001][research_karuppusamy_2020]
- Kaur, Harguneet, and Arvinder Kaur. 2022. "An Empirical Study of Aging Related Bug Prediction Using Cross Project in Cloud Oriented Software." *Informatica* 46 (8). [https://doi.org/10.31449/inf.v46i8.4197][research_kaur_2022]
- Khaldi, Dounia, Pierre Jouvelot, François Irigoin, Corinne Ancourt, and Barbara Chapman. 2015. "LLVM Parallel Intermediate Representation: Design and Evaluation Using OpenSHMEM Communications." In *Proceedings of the Second Workshop on the LLVM Compiler Infrastructure in HPC*. ACM. [https://doi.org/10.1145/2833157.2833158][research_khaldi_2015]
- Khan, Maryam. 2026. "Integrating Large Language Models in Software Engineering Education: A Pilot Study through GitHub Repositories Mining." In *Proceedings of the 41st ACM/SIGAPP Symposium on Applied Computing*. ACM. [https://doi.org/10.1145/3748522.3780033][research_khan_2026]
- Khan, Md Asif, Akramul Azim, Ramiro Liscano, et al. 2024. "Machine Learning-Based Test Case Prioritization Using Hyperparameter Optimization." In *Proceedings of the 5th ACM/IEEE International Conference on Automation of Software Test (AST 2024)*. ACM. [https://doi.org/10.1145/3644032.3644467][research_khan_2024]
- Khan, Sara, and Saurabh Pal. 2022. "An Improvement to Test Case Prioritization Techniques Using Machine Learning." In *Lecture Notes in Networks and Systems*. Springer Nature Singapore. [https://doi.org/10.1007/978-981-19-3148-2\_34][research_khan_2022]
- Kia, Solmaz S. 2026. "Submodular Maximization Subject to Uniform and Partition Matroids: From Theory to Practical Applications and Distributed Solutions." In *Encyclopedia of Systems and Control Engineering*. Elsevier. [https://doi.org/10.1016/b978-0-443-14081-5.00090-8][research_kia_2026]
- Kiam Tan, Yong, Magnus O. Myreen, Ramana Kumar, Anthony Fox, Scott Owens, and Michael Norrish. 2019. "The Verified CakeML Compiler Backend." *Journal of Functional Programming* 29: e2. [https://doi.org/10.1017/s0956796818000229][research_kiamtan_2019]
- Kim, Sung Dae, and Myung Hoon Sunwoo. 2017. "Application-Specific Instruction Set Processors for Video Processing." In *Multimedia Image and Video Processing*. CRC Press. [https://doi.org/10.1201/b11716-31][research_kim_2017]
- Kimura, Yoshiki, Kanemitsu Ootsu, Tatsuya Tsuchiya, and Takashi Yokota. 2021. "Development of RISC-V Based Soft-Core Processor with Scalable Vector Extension for Embedded System." In *Proceedings of the the 8th International Virtual Conference on Applied Computing & Information Technology*. ACM. [https://doi.org/10.1145/3468081.3471061][research_kimura_2021]
- Kingsly Stephen, R., and T. Archana. 2025. "Optimization, Machine Learning, and Fuzzy Logic: Machine Learning Fundamentals and Introduction to Machine Learning." In *Advances in Computational Intelligence and Robotics*. IGI Global Scientific Publishing. [https://doi.org/10.4018/979-8-3693-7352-1.ch001][research_kingslystephen_2025]
- Klemmer, Lucas, and Daniel Große. 2025. "A Formally Verified Microcoded RISC-V Platform." In *Versatile Hardware Analysis Techniques*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-83093-8\_4][research_klemmer_2025]
- Klemmer, Lucas, Manfred Schlägl, and Daniel Große. 2022b. "RVVRadar: A Framework for Supporting the Programmer in Vectorization for RISC-V." In *Proceedings of the Great Lakes Symposium on VLSI 2022*. ACM. [https://doi.org/10.1145/3526241.3530388][research_klemmer_2022]
- Koitz-Hristov, Roxane, Lukas Stracke, and Franz Wotawa. 2022. "Checked Coverage for Test Suite Reduction: Is It Worth the Effort?" In *Proceedings of the 3rd ACM/IEEE International Conference on Automation of Software Test*. ACM. [https://doi.org/10.1145/3524481.3527216][research_koitzhristov_2022]
- Kostin, Victor, Sergey Solovyev, Hongwei Liu, and Andrey Bakulin. 2017. "HSS Cluster-Based Direct Solver for Acoustic Wave Equation." In *International Meeting for Applied Geoscience & Energy*, vol. 1. Society of Exploration Geophysicists. [https://doi.org/10.1190/segam2017-17443086.1][research_kostin_2017]
- Koutcheme, Charles, and Arto Hellas. 2024. "Propagating Large Language Models Programming Feedback." In *Proceedings of the Eleventh ACM Conference on Learning @ Scale*. ACM. [https://doi.org/10.1145/3657604.3664665][research_koutcheme_2024]
- Koutsoumpas, Vasileios. 2015. "A Formal Approach Based on Fuzzy Logic for the Specification of Component-Based Interactive Systems." *Electronic Proceedings in Theoretical Computer Science* 178: 62–76. [https://doi.org/10.4204/eptcs.178.6][research_koutsoumpas_2015]
- Kozanidis, Nicholas, Roberto Verdecchia, and Emitza Guzman. 2022. "Asking about Technical Debt: Characteristics and Automatic Identification of Technical Debt Questions on Stack Overflow." In *Proceedings of the 16th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement*. ACM. [https://doi.org/10.1145/3544902.3546245][research_kozanidis_2022]
- Koziolek, Heiko, and Anne Koziolek. 2024. "LLM-Based Control Code Generation Using Image Recognition." In *Proceedings of the 1st International Workshop on Large Language Models for Code*. ACM. [https://doi.org/10.1145/3643795.3648385][research_koziolek_2024]
- Kumar, Hemant, and Vipin Saxena. 2024. "Machine Learning for Test Case Prioritization in Continuous Integration: A Comprehensive Analysis." *International journal Advanced Networking and Applications* 17 (02): 6218–28. [https://doi.org/10.35444/ijana.2024.15609][research_kumar_2024_b]
- Kunčar, Ondřej. 2015. "Correctness of Isabelle's Cyclicity Checker: Implementability of Overloading in Proof Assistants." In *Proceedings of the 2015 Conference on Certified Programs and Proofs*. ACM. [https://doi.org/10.1145/2676724.2693175][research_kuncar_2015]
- Kurudirek, Abdullah, Melek Azra Kurudirek, and Kadriye Afra Kurudirek. 2025. "An Innovation Study on Luggage Wheel Design for Seamless Travel." *Compiler* 14 (1): 9. [https://doi.org/10.28989/compiler.v14i1.2819][research_kurudirek_2025]
- Kusumaningrum, Nurwijayanti, and Reza Ananda. 2021. "STERILIZER CHAMBER DESIGN WITH TELEGRAM-BASED INTERNET OF THINGS (IoT) APPLICATIONS." *Compiler* 10 (2): 89. [https://doi.org/10.28989/compiler.v10i2.1111][research_kusumaningrum_2021]
- Kusumaningrum, Nurwijayanti, and Yogi Setiawan. 2022. "Design of Automatic Aircraft Parking System Module Visually Guidance Display Using ESP32 Microcontroller as Practical Media." *Compiler* 11 (1): 15. [https://doi.org/10.28989/compiler.v11i1.1231][research_kusumaningrum_2022]
- Kusumaningrum, Anggraini, and Rolas Sianturi. 2015. "Perancangan Pengamanan Server Secara Otomatis Menggunakan Metode Adam (Automatic Event Detection and Activity Monitoring)." *Compiler* 4 (2). [https://doi.org/10.28989/compiler.v4i2.92][research_kusumaningrum_2015]
- Kwon, Jung-Hoon, and Jong-Min Bae. 2016. "Development of a Code Generation Support System in Integrated Development Environment of an Educational Compiler." *Journal of the Korea Society of Computer and Information* 21 (11): 159–66. [https://doi.org/10.9708/jksci.2016.21.11.159][research_kwon_2016]
- Kwon, Seungwan, Jaeseong Kwon, Wooseok Kang, Juneyoung Lee, and Kihong Heo. 2024. "Translation Validation for JIT Compiler in the V8 JavaScript Engine." In *Proceedings of the IEEE/ACM 46th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3597503.3639189][research_kwon_2024]
- Laboudi, Fatima Zohra, Kamilia Menghour, and Labiba Souici-Meslati. 2025. "Swarm Intelligence for Software Effort Estimation: An Empirical Study." *International Journal of Software Engineering and Knowledge Engineering* 35 (12): 1685–1712. [https://doi.org/10.1142/s0218194025500482][research_laboudi_2025]
- Lachmann, R. 2018. "12.4: Machine Learning-Driven Test Case Prioritization Approaches for Black-Box Software Testing." In *Proceeding - ettc2018*. AMA Service GmbH, Von-Münchhausen-Str. 49, 31515 Wunstorf, Germany. [https://doi.org/10.5162/ettc2018/12.4][research_lachmann_2018]
- Lai, Hung-Ming, and Jenq-Kuen Lee. 2022. "Efficient Support of the Scan Vector Model for RISC-V Vector Extension." In *Workshop Proceedings of the 51st International Conference on Parallel Processing*. ACM. [https://doi.org/10.1145/3547276.3548518][research_lai_2022]
- Lai, Hung-Ming, Jenq-Kuen Lee, and Yuan-Shin Hwang. 2023. "Enhancing LLVM Optimizations for Linear Recurrence Programs on RVV." In *Proceedings of the 52nd International Conference on Parallel Processing Workshops*. ACM. [https://doi.org/10.1145/3605731.3605904][research_lai_2023]
- Lai, Jyun-Kai, and Wuu Yang. 2021. "Hyperchaining Optimizations for an LLVM-Based Binary Translator on x86-64 and RISC-V Platforms." In *50th International Conference on Parallel Processing Workshop*. ACM. [https://doi.org/10.1145/3458744.3473348][research_lai_2021]
- Lam, Wing, Kıvanç Muşlu, Hitesh Sajnani, and Suresh Thummalapenta. 2020. "A Study on the Lifecycle of Flaky Tests." In *Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3377811.3381749][research_lam_2020]
- Lambert, Matthew A., and B. David Saunders. 2017. "Compiler Auto-Vectorization of Matrix Multiplication Modulo Small Primes." In *Proceedings of the International Workshop on Parallel Symbolic Computation*. ACM. [https://doi.org/10.1145/3115936.3115943][research_lambert_2017]
- Lan, Yunhao, Larry Tang, Naifeng Zhang, Youngjin Eum, James Hoe, and Franz Franchetti. 2025. "A RISC-V Vector Extension for Multi-Word Arithmetic." In *Proceedings of the SC '25 Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis*. ACM. [https://doi.org/10.1145/3731599.3767530][research_lan_2025]
- Lancellotti, Giacomo, Francesco Rosnati, Leonardo Ignazio Pagliochini, and Giovanni Agosta. 2026a. "Quantum Circuit Synthesis from C via Multi-Level Intermediate Representation." In *Proceedings of the 41st ACM/SIGAPP Symposium on Applied Computing*. ACM. [https://doi.org/10.1145/3748522.3779947][research_lancellotti_2026]
- Landi, William. 1992. "Undecidability of Static Analysis." *ACM Letters on Programming Languages and Systems* 1 (4): 323–37. [https://doi.org/10.1145/161494.161501][research_landi_1992]
- Larose, Octave, Michael Vollmer, and Stefan Marr. 2026. "AST, Bytecode, and the Space in Between: An Exploration of Interpreter Design Tradeoffs." *Journal of Object Technology* 25 (1): 1:1. [https://doi.org/10.5381/jot.2026.25.1.a15][research_larose_2026]
- Lasnier, Pascal Y., Jeremy Yallop, and Magnus O. Myreen. 2026b. *CPP '26 Artifact: Brack: A Verified Compiler for Scheme via CakeML*. Association for Computing Machinery (ACM). [https://doi.org/10.1145/3747413][research_lasnier_2026_b]
- Latifis, Ioannis, Karthick Parashar, Grigoris Dimitroulakos, et al. 2016. "Matlab to C Compilation Targeting Application Specific Instruction Set Processors." In *Proceedings of the 2016 Design, Automation & Test in Europe Conference & Exhibition (DATE)*. Research Publishing Services. [https://doi.org/10.3850/9783981537079\_0426][research_latifis_2016]
- Latifis, Ioannis, Karthick Parashar, Grigoris Dimitroulakos, et al. 2017. "A MATLAB Vectorizing Compiler Targeting Application-Specific Instruction Set Processors." *ACM Transactions on Design Automation of Electronic Systems* 22 (2): 1–28. [https://doi.org/10.1145/2996182][research_latifis_2017]
- Lavazza, Luigi, Geng Liu, and Roberto Meli. 2020. "Using Extremely Simplified Functional Size Measures for Effort Estimation: An Empirical Study." In *Proceedings of the 14th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. ACM. [https://doi.org/10.1145/3382494.3410691][research_lavazza_2020]
- Lavazza, Luigi, and Sandro Morasca. 2017. "On the Evaluation of Effort Estimation Models." In *Proceedings of the 21st International Conference on Evaluation and Assessment in Software Engineering*. ACM. [https://doi.org/10.1145/3084226.3084260][research_lavazza_2017]
- Lefeuvre, Romain, Maïwenn Le Goasteller, Jessie Galasso, Benoit Combemale, Quentin Perez, and Houari Sahraoui. 2026. "Modeling Sampling Workflows for Code Repositories." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793369][research_lefeuvre_2026]
- Lei, Hanwen, Ding Li, and Yao Guo. 2025. "Furina: A Light-Weight WebAssembly Runtime for ICS." In *Proceedings of the 2025 Workshop on Re-design Industrial Control Systems with Security*. ACM. [https://doi.org/10.1145/3733823.3764514][research_lei_2025]
- Leopoldseder, David, Lukas Stadler, Thomas Würthinger, Josef Eisl, Doug Simon, and Hanspeter Mössenböck. 2018b. "Dominance-Based Duplication Simulation (DBDS): Code Duplication to Enable Compiler Optimizations." In *Proceedings of the 2018 International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3168811][research_leopoldseder_2018]
- Leroy, Xavier. 2009. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52 (7): 107–15. [https://doi.org/10.1145/1538788.1538814][research_leroy_2009]
- Li, Tianchi. 2019. "Haskell Compiler Testing Automation Based on Equivalence-Modulo-Inputs Method." In *Proceedings of the 2019 International Conference on Modeling, Simulation and Big Data Analysis (MSBDA 2019)*. Atlantis Press. [https://doi.org/10.2991/msbda-19.2019.25][research_li_2019]
- Li, Hao, Chengchen Hu, Peng Zhang, and Lei Xie. 2016. "Modular SDN Compiler Design with Intermediate Representation." In *Proceedings of the 2016 ACM SIGCOMM Conference*. ACM. [https://doi.org/10.1145/2934872.2959061][research_li_2016]
- Li, Fengjie, Jiajun Jiang, Jiajun Sun, and Hongyu Zhang. 2025f. "Hybrid Automated Program Repair by Combining Large Language Models and Program Analysis." *ACM Transactions on Software Engineering and Methodology* 34 (7): 1–28. [https://doi.org/10.1145/3715004][research_li_2025_i]
- Li, Zheng, Jiping Liu, Shunqing Xu, Hengyuan Liu, and Yong Liu. 2025d. "An Environment Adaptation Agent of Reinforcement Learning in Continuous Integration Test Case Prioritization." *International Journal of Software Engineering and Knowledge Engineering* 36 (02): 311–41. [https://doi.org/10.1142/s0218194025500792][research_li_2025_e]
- Li, Zongjie, Pingchuan Ma, Huaijin Wang, et al. 2022d. "Unleashing the Power of Compiler Intermediate Representation to Enhance Neural Program Embeddings." In *Proceedings of the 44th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3510003.3510217][research_li_2022]
- Li, Yau-Tsun Steven, and Sharad Malik. 1995. "Performance Analysis of Embedded Software Using Implicit Path Enumeration." In *Proceedings of the 32nd ACM/IEEE conference on Design automation conference - DAC '95*. ACM Press. [https://doi.org/10.1145/217474.217570][research_li_malik_1995]
- Li, Zujie, Huabiao Qin, and Yixiang Xie. 2025b. "Applying Knowledge-Guided Deep Reinforcement Learning with Graph Neural Networks for Compiler Optimization." In *Proceedings of the 4th International Conference on Computer, Artificial Intelligence and Control Engineering*. ACM. [https://doi.org/10.1145/3727648.3727682][research_li_2025_h]
- Li, Han, Haoqi Ren, and Jun Wu. 2017. "Domain Specific Compiler for Coordinated Signal Processing in 5G Testbed." In *Proceedings of the Workshop on Smart Internet of Things*. ACM. [https://doi.org/10.1145/3132479.3132487][research_li_2017]
- Li, Shaohua, and Zhendong Su. 2023. "Finding Unstable Code via Compiler-Driven Differential Testing." In *Proceedings of the 28th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 3*. ACM. [https://doi.org/10.1145/3582016.3582053][research_li_2023_c]
- Li, Xiao, Jiajia Sun, Yongguang Zhang, Xiaokang Yin, and Shengli Liu. 2025c. "Binary Similarity Detection Based on Intermediate Representation Graph Fusion." In *Proceedings of the 2025 4th International Conference on Cryptography, Network Security and Communication Technology*. ACM. [https://doi.org/10.1145/3723890.3723908][research_li_2025_k]
- Liang, Jingjing, Sebastian Elbaum, and Gregg Rothermel. 2018. "Redefining Prioritization: Continuous Prioritization for Continuous Integration." In *Proceedings of the 40th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3180155.3180213][research_liang_2018]
- Liang, Zhanhao, Hanming Sun, Wenhan Shang, et al. 2025a. "Calibro: Compilation-Assisted Linking-Time Binary Code Outlining for Code Size Reduction in Android Applications." In *Proceedings of the 23rd ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3696443.3708955][research_liang_2025_b]
- Lima, Jackson A. Prado, Willian D. F. Mendonça, Silvia R. Vergilio, and Wesley K. G. Assunção. 2020. "Learning-Based Prioritization of Test Cases in Continuous Integration of Highly-Configurable Software." In *Proceedings of the 24th ACM Conference on Systems and Software Product Line: Volume A - Volume A*. ACM. [https://doi.org/10.1145/3382025.3414967][research_lima_2020]
- Lima, Jackson Antonio do Prado, and Silvia Regina Vergilio. 2023. "An Evaluation of Ranking-to-Learn Approaches for Test Case Prioritization in Continuous Integration." *Journal of Software Engineering Research and Development*. [https://doi.org/10.5753/jserd.2023.2142][research_lima_2023]
- Lima, Jackson A. Prado, and Silvia R. Vergilio. 2020. "Multi-Armed Bandit Test Case Prioritization in Continuous Integration Environments: A Trade-off Analysis." In *Proceedings of the 5th Brazilian Symposium on Systematic and Automated Software Testing*. ACM. [https://doi.org/10.1145/3425174.3425210][research_lima_2020_b]
- Lindholm, Tim, Frank Yellin, Gilad Bracha, Alex Buckley, and Daniel Smith. 2023. "The Java® Virtual Machine Specification: Java SE 21 Edition." Oracle. Accessed October 24, 2026. [https://docs.oracle.com/javase/specs/jvms/se21/html/index.html][ref_jvm_spec]
- Listiawan, Indra, Zaidir Zaidir, Sugeng Winardi, and Mohammad Diqi. 2024. "Optimising Bcrypt Parameters: Finding the Optimal Number of Rounds for Enhanced Security and Performance." *Compiler* 13 (1): 1. [https://doi.org/10.28989/compiler.v13i1.2111][research_listiawan_2024]
- Liu, XinYi. 2024. "Fuzzing Guided by Context-Sensitive Branch Coverage." In *Fifth International Conference on Computer Communication and Network Security (CCNS 2024)*, edited by Zhiyong Xiong, Zhaolong Ning. SPIE. [https://doi.org/10.1117/12.3038243][research_liu_2024_d]
- Liu, Tommy, and Amanda S. Barnard. 2021. "Fast Derivation of Shapley Based Feature Importances through Feature Extraction Methods for Nanoinformatics." *Machine Learning: Science and Technology* 2 (3): 035034. [https://doi.org/10.1088/2632-2153/ac0167][research_liu_2021_b]
- Liu, Binbin, Wei Dong, Yating Zhang, Daiyan Wang, and Jiaxin Liu. 2020. "Boosting Component-Based Synthesis with Control Structure Recommendation." In *Proceedings of the 1st ACM SIGSOFT International Workshop on Representation Learning for Software Engineering and Program Languages*. ACM. [https://doi.org/10.1145/3416506.3423579][research_liu_2020]
- Liu, C. L., and James W. Layland. 1973. "Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment." *Journal of the ACM* 20 (1): 46–61. [https://doi.org/10.1145/321738.321743][research_liu_layland_1973]
- Liu, Heming, Xian Lin, Xin Zheng, and Shuting Cai. 2024b. "Convex: A RISC-V Instruction Set Extension Scheme for Accelerating Convolution Operations on MCUs." In *Proceedings of the 2024 8th International Conference on High Performance Compilation, Computing and Communications*. ACM. [https://doi.org/10.1145/3675018.3675029][research_liu_2024]
- Liu, Fei, Yanping Shao, Zhouquan Liu, et al. 2025c. "RISC-TAE: Instruction Set Extension for Transformer Model Acceleration." In *Proceedings of the International Conference on Compilers, Architecture, and Synthesis for Embedded Systems*. ACM. [https://doi.org/10.1145/3742872.3757073][research_liu_2025]
- Liu, Mugeng, Haiyang Shen, Yixuan Zhang, Hong Mei, and Yun Ma. 2025e. "WebAssembly for Container Runtime: Are We There Yet?" *ACM Transactions on Software Engineering and Methodology* 34 (6): 1–22. [https://doi.org/10.1145/3712197][research_liu_2025_b]
- Liu, Zhibo, and Shuai Wang. 2020. "How Far We Have Come: Testing Decompilation Correctness of C Decompilers." In *Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3395363.3397370][research_liu_2020_b]
- Liu, Jiawei, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. 2023b. "Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation." In *Advances in Neural Information Processing Systems 36*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/075280-0943][research_liu_2023_b]
- Liu, Yujie, Mingxuan Zhu, Jinhao Dong, Junzhe Yu, and Dan Hao. 2024a. "Compiler Bug Isolation via Enhanced Test Program Mutation." In *Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering*. ACM. [https://doi.org/10.1145/3691620.3695074][research_liu_2024_c]
- LLVM Project. n.d.. "LLVM Language Reference Manual." LLVM Documentation. Accessed October 24, 2026. [https://llvm.org/docs/LangRef.html][ref_llvm_langref]
- Loose, Nils, Nico Winkel, Kristoffer Hempel, Felix Mächtle, Julian Hans, and Thomas Eisenbarth. 2026. "Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing." In *Proceedings of the 19th ACM/IEEE International Workshop on Search-Based and Fuzz Testing*. ACM. [https://doi.org/10.1145/3786155.3788582][research_loose_2026]
- Lovász, L. 1983. "Submodular Functions and Convexity." In *Mathematical Programming The State of the Art*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-642-68874-4\_10][research_lovasz_1983]
- Lu, Kuang-Chen, Ben Greenman, Carl Meyer, Dino Viehland, Aniket Panse, and Shriram Krishnamurthi. 2022. "Gradual Soundness: Lessons from Static Python." *Art, Science, and Engineering of Programming* 7 (1): 2. [https://doi.org/10.22152/programming-journal.org/2023/7/2][research_lu_2022]
- Lu, Ganfeng, and Jiping Zheng. 2021. "Fixed-Size Video Summarization over Streaming Data via Non-Monotone Submodular Maximization." In *Proceedings of the 2nd ACM International Conference on Multimedia in Asia*. ACM. [https://doi.org/10.1145/3444685.3446285][research_lu_2021]
- Lücke, Martin Paul, Oleksandr Zinenko, William S. Moses, Michel Steuwer, and Albert Cohen. 2025. "The MLIR Transform Dialect: Your Compiler Is More Powerful than You Think." In *Proceedings of the 23rd ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3696443.3708922][research_lucke_2025]
- Lund, Carsten, and Mihalis Yannakakis. 1994. "On the Hardness of Approximating Minimization Problems." *Journal of the ACM* 41 (5): 960–81. [https://doi.org/10.1145/185675.306789][research_lund_yannakakis_1994]
- Luo, Kailun, and Yongmei Liu. 2019. "Automatic Verification of FSA Strategies via Counterexample-Guided Local Search for Invariants." In *Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence*. International Joint Conferences on Artificial Intelligence Organization. [https://doi.org/10.24963/ijcai.2019/251][research_luo_2019]
- Luo, Qi, Kevin Moran, and Denys Poshyvanyk. 2016a. "A Large-Scale Empirical Comparison of Static and Dynamic Test Case Prioritization Techniques." In *Proceedings of the 2016 24th ACM SIGSOFT International Symposium on Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/2950290.2950344][research_luo_2016_b]
- Luo, Xuan, and Jian Pei. 2024. "Applications and Computation of the Shapley Value in Databases and Machine Learning." In *Companion of the 2024 International Conference on Management of Data*. ACM. [https://doi.org/10.1145/3626246.3654680][research_luo_2024]
- Luo, Qi, Denys Poshyvanyk, and Mark Grechanik. 2016b. "Mining Performance Regression Inducing Code Changes in Evolving Software." In *Proceedings of the 13th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/2901739.2901765][research_luo_2016]
- Luppen, Zachary A., Dae Young Lee, and Kristin Y. Rozier. 2021a. "A Case Study in Formal Specification and Runtime Verification of a CubeSat Communications System." In *AIAA Scitech 2021 Forum*. AIAA 2021-0997. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2021-0997][research_luppen_2021]
- Luppen, Zachary A., Dae Young Lee, and Kristin Y. Rozier. 2021b. "Correction: A Case Study in Formal Specification and Runtime Verification of a CubeSat Communications System." In *AIAA Scitech 2021 Forum*. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2021-0997.c1][research_luppen_2021_b]
- Luu, Quang-Hung, Huai Liu, Tsong Yueh Chen, and Hai L. Vu. 2022. "Testing Ocean Software with Metamorphic Testing." In *Proceedings of the 7th International Workshop on Metamorphic Testing*. ACM. [https://doi.org/10.1145/3524846.3527341][research_luu_2022]
- Lv, Lanxiang, Ningan Chao, Dongliang Xiong, and Kai Huang. 2026. "FWHT-RVV: A RISC-V Vector Processor with FWHT Instruction Extension for Edge LLM Inference." *IEICE Electronics Express* 23 (12): 20260182–20260182. [https://doi.org/10.1587/elex.23.20260182][research_lv_2026]
- Lyu, Shing, and Andrew Rzeznik. 2023. "High-Performance Web Frontend Using WebAssembly." In *Practical Rust Projects*. Apress. [https://doi.org/10.1007/978-1-4842-9331-7\_4][research_lyu_2023]
- Ma, Mingyuan. 2022. "Application of an Improved Shapley Value Method in Cooperative Alliance Game." In *Lecture Notes on Data Engineering and Communications Technologies*. Springer International Publishing. [https://doi.org/10.1007/978-3-031-05484-6\_109][research_ma_2022]
- Ma, Zining, Honglan Jiang, Hongpeng Li, Yong Wu, Chenchen Deng, and Leibo Liu. 2023a. "Design of DMS-RRIP Replacement Algorithm for L1-Cache of RISC-V-Based Single-Core Embedded Processor." In *Second International Conference on Electronic Information Technology (EIT 2023)*, edited by Wendong Xiao, Lu Leng. SPIE. [https://doi.org/10.1117/12.2685759][research_ma_2023_b]
- Ma, Haoyang, Qingchao Shen, Yongqiang Tian, Junjie Chen, and Shing-Chi Cheung. 2023b. "Fuzzing Deep Learning Compilers with HirGen." In *Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3597926.3598053][research_ma_2023]
- Ma, Dekang, and Fuli Shi. 2025. "Research on Coverage-Guided Fuzzing Technique Based on Magma Dataset." In *Proceedings of the 2025 International Conference on Software Engineering and Computer Applications*. ACM. [https://doi.org/10.1145/3747912.3747940][research_ma_2025]
- Madkour, Abdelrahman, Ross Mawhorter, Stacy Marsella, Adam M. Smith, and Steven Holtzen. 2024. "Ahead-of-Time Compilation for Diverse Samplers of Constrained Design Spaces." In *Proceedings of the 19th International Conference on the Foundations of Digital Games*. ACM. [https://doi.org/10.1145/3649921.3656986][research_madkour_2024]
- Mahathevan, Kabilan, Yining Zhang, Muhammad Ali Gulzar, and Kirshanthan Sundararajah. 2026. "TenSure: Fuzzing Sparse Tensor Compilers (Registered Report)." In *Proceedings 2026 International Fuzzing Workshop*. Internet Society. [https://doi.org/10.14722/fuzzing.2026.23006][research_mahathevan_2026]
- Mahida, Ankur. 2021. "A Review on Continuous Integration and Continuous Deployment (CI/CD) for Machine Learning." *International Journal of Science and Research (IJSR)* 10 (3): 1967–70. [https://doi.org/10.21275/sr24314131827][research_mahida_2021]
- Maier, Dominik, Otto Bittner, Julian Beier, and Marc Munier. 2022. "FitM: Binary-Only Coverage-Guided Fuzzing for Stateful Network Protocols." In *Proceedings 2022 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2022.23008][research_maier_2022]
- Maity, Satanu, and Manojit Ghose. 2026. "SAGE: A Compiler-Assisted Reinforcement Learning-Based Offloading Approach under near-Memory Processing Paradigm." *ACM Transactions on Architecture and Code Optimization* 23 (1): 1–23. [https://doi.org/10.1145/3778361][research_maity_2026]
- Majeti, Deepak, Kuldeep S. Meel, Rajkishore Barik, and Vivek Sarkar. 2016. "Automatic Data Layout Generation and Kernel Mapping for CPU+GPU Architectures." In *Proceedings of the 25th International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/2892208.2892210][research_majeti_2016]
- Majumder, Abhilash. 2025. "FormalGym: Deep Reinforcement Learning Agent Based Formal Compiler Optimization Framework." In *Proceedings of the International Conference on Research in Adaptive and Convergent Systems*. ACM. [https://doi.org/10.1145/3769002.3769975][research_majumder_2025]
- Marcelino, Cynthia, Noah Krennmair, Thomas Werner Pusztai, and Stefan Nastic. 2025. "Lumos: Performance Characterization of WebAssembly as a Serverless Runtime in the Edge-Cloud Continuum." In *Proceedings of the 15th International Conference on the Internet of Things*. ACM. [https://doi.org/10.1145/3770501.3770515][research_marcelino_2025]
- Marcelino, Cynthia, and Stefan Nastic. 2023. "CWASI: A WebAssembly Runtime Shim for Inter-Function Communication in the Serverless Edge-Cloud Continuum." In *Proceedings of the Eighth ACM/IEEE Symposium on Edge Computing*. ACM. [https://doi.org/10.1145/3583740.3626611][research_marcelino_2023]
- Marsad, Faiz, and Nimmi Weeraddana. 2026. "OSSGameBench: A Large-Scale Dataset of Development Activities in Open-Source Video Games." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793313][research_marsad_2026]
- Martin, Nathan. 2025. "Data Valuation with Leave-One-Out (LOO) Test and Shapley Methods." *Journal of Science & Engineering* 1 (3): 72. [https://doi.org/10.64804/t6yn4h63][research_martin_2025]
- Martin Jeremy M.R. 2019. "Testing and Verifying Parallel Programs Using Data Refinement." In *Concurrent Systems Engineering Series*. IOS Press. [https://doi.org/10.3233/978-1-61499-949-2-491][research_martinjeremymr_2019]
- Martins, Luiz G. A., Ricardo Nobre, João M. P. Cardoso, Alexandre C. B. Delbem, and Eduardo Marques. 2016. "Clustering-Based Selection for the Exploration of Compiler Optimization Sequences." *ACM Transactions on Architecture and Code Optimization* 13 (1): 1–28. [https://doi.org/10.1145/2883614][research_martins_2016]
- Masoudi, Tina. 2025. "Investigating the Role of Formal Verification in Software Development: From Automatic Specification Generation to Usability of Verification Languages." In *Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/3696630.3731465][research_masoudi_2025]
- Massalin, Henry. 1987. "Superoptimizer: A Look at the Smallest Program." In *Proceedings of the second international conference on Architectual support for programming languages and operating systems*. ACM. [https://doi.org/10.1145/36206.36194][research_massalin_1987]
- Matteo R. Donelli. 2025. "Compiler-Assisted Optimization Using Neural Code Embeddings for Heterogeneous Architectures." *Journal of Multidisciplinary Knowledge* 5 (2): 165–70. [https://doi.org/10.36676/jmk.v5.i2.93][research_matteordonelli_2025]
- Mazurowski, John, and P. A. Dowben. 2024. "A Compilation of Experimental Binary Alloy Surface Segregation Studies." In *Surface Segregationphenomena*. CRC Press. [https://doi.org/10.1201/9781003574958-13][research_mazurowski_2024]
- McKee, Derrick, Nathan Burow, and Mathias Payer. 2023. "Accurate Compiler and Optimization Independent Function Identification Using Program State Transformations." In *Proceedings 2023 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2023.23003][research_mckee_2023]
- Mece, Elinda Kajo, Hakik Paci, and Kleona Binjaku. 2020. "The Application of Machine Learning in Test Case Prioritization: A Review." *European Journal of Electrical Engineering and Computer Science* 4 (1). [https://doi.org/10.24018/ejece.2020.4.1.128][research_mece_2020]
- Meehl, Paul E. 1967. "Theory-Testing in Psychology and Physics: A Methodological Paradox." *Philosophy of Science* 34 (2): 103–15. [https://doi.org/10.1086/288135][research_meehl_1967]
- Menendez, David, and Santosh Nagarakatte. 2016. "Termination-Checking for LLVM Peephole Optimizations." In *Proceedings of the 38th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/2884781.2884809][research_menendez_2016_b]
- Merazga, Ammar, Djamel Rahem, Fateh Moulahcene, Djemai Kebbal, Rostom Khelaf, and Imad Benacer. 2025. "Worst-Case Execution Time Analysis of a Real-Time System Based on Arduino in CAN Network." *Engineering, Technology & Applied Science Research* 15 (3): 23467–78. [https://doi.org/10.48084/etasr.10990][research_merazga_2025]
- Merz, Stephan. 2019. "Formal Specification and Verification." In *Concurrency: the Works of Leslie Lamport*. Association for Computing Machinery. [https://doi.org/10.1145/3335772.3335780][research_merz_2019]
- Meshveliani, S. D. 2020. "On a Machine-Checked Proof for Fraction Arithmetic over a GCD Domain." *Programming and Computer Software* 46 (2): 110–19. [https://doi.org/10.1134/s0361768820020073][research_meshveliani_2020]
- Miné, Antoine. 2017. "Tutorial on Static Inference of Numeric Invariants by Abstract Interpretation." *Foundations and Trends® in Programming Languages* 4 (3–4): 120–372. [https://doi.org/10.1561/2500000034][research_mine_2017]
- Mirrokni, Vahab, and Morteza Zadimoghaddam. 2015. "Randomized Composable Core-Sets for Distributed Submodular Maximization." In *Proceedings of the forty-seventh annual ACM symposium on Theory of Computing*. ACM. [https://doi.org/10.1145/2746539.2746624][research_mirrokni_2015]
- Mirzasoleiman, Baharan, Stefanie Jegelka, and Andreas Krause. 2018. "Streaming Non-Monotone Submodular Maximization: Personalized Video Summarization on the Fly." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11529][research_mirzasoleiman_2018]
- Miyamoto, Vania Furuguem, Silvia Maria Soares de Araujo Pereira, and José Luis Menegotto. 2024. "Rule Modeling for Automatic Verification of RDC-50 Requirements in EAS." In *Connections Exploring Interdisciplinarity in Health*. Seven Editora. [https://doi.org/10.56238/sevened2024.025-014][research_miyamoto_2024]
- Mogensen, Torben Ægidius. 2017a. "Intermediate-Code Generation." In *Undergraduate Topics in Computer Science*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-66966-3\_6][research_mogensen_2017]
- Mogensen, Torben Ægidius. 2017b. "Machine-Code Generation." In *Undergraduate Topics in Computer Science*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-66966-3\_7][research_mogensen_2017_b]
- Mogensen, Torben Ægidius. 2024a. "Intermediate-Code Generation." In *Undergraduate Topics in Computer Science*. Springer International Publishing. [https://doi.org/10.1007/978-3-031-46460-7\_6][research_mogensen_2024]
- Mogensen, Torben Ægidius. 2024b. "Machine-Code Generation." In *Undergraduate Topics in Computer Science*. Springer International Publishing. [https://doi.org/10.1007/978-3-031-46460-7\_7][research_mogensen_2024_b]
- Molnar, Arthur-Jozsef, and Simona Motogna. 2020. "Long-Term Evaluation of Technical Debt in Open-Source Software." In *Proceedings of the 14th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. ACM. [https://doi.org/10.1145/3382494.3410673][research_molnar_2020]
- Monniaux, David. 2023. "Completeness in Static Analysis by Abstract Interpretation: A Personal Point of View." In *Intelligent Systems Reference Library*. Springer Nature Singapore. [https://doi.org/10.1007/978-981-19-9601-6\_6][research_monniaux_2023]
- Moreno, Carlos, Sean Kauffman, and Sebastian Fischmeister. 2016. "Efficient Program Tracing and Monitoring through Power Consumption — With a Little Help from the Compiler." In *Proceedings of the 2016 Design, Automation & Test in Europe Conference & Exhibition (DATE)*. Research Publishing Services. [https://doi.org/10.3850/9783981537079\_0829][research_moreno_2016]
- Moron, Konrad, and Stefan Wallentowitz. 2025. "Benchmarking WebAssembly for Embedded Systems." *ACM Transactions on Architecture and Code Optimization* 22 (3): 1–21. [https://doi.org/10.1145/3736169][research_moron_2025]
- Morton, Kairo, William Hallahan, Elven Shum, Ruzica Piskac, and Mark Santolucito. 2020. "Grammar Filtering for Syntax-Guided Synthesis." *Proceedings of the AAAI Conference on Artificial Intelligence* 34 (02): 1611–18. [https://doi.org/10.1609/aaai.v34i02.5522][research_morton_2020]
- Moskalenko, Oleksandr. 2025. "Application of WebAssembly for High-Performance Client-Side Media Content Analysis." *American Journal of Engineering and Technology* 7 (10): 139–45. [https://doi.org/10.37547/tajet/volume07issue10-17][research_anon_2025]
- Mpeis, Paschalis, Pavlos Petoumenos, Kim Hazelwood, and Hugh Leather. 2022. "Object Intersection Captures on Interactive Apps to Drive a Crowd-Sourced Replay-Based Compiler Optimization." *ACM Transactions on Architecture and Code Optimization* 19 (3): 1–25. [https://doi.org/10.1145/3517338][research_mpeis_2022]
- Muros, Francisco Javier. 2019. "The Shapley and Position Values to Design Coalitional Networks." In *Springer Theses*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-10489-4\_4][research_muros_2019]
- Na, Yeoul, Seon Wook Kim, and Youngsun Han. 2016. "JavaScript Parallelizing Compiler for Exploiting Parallelism from Data-Parallel HTML5 Applications." *ACM Transactions on Architecture and Code Optimization* 12 (4): 1–25. [https://doi.org/10.1145/2846098][research_na_2016]
- Nagy, Stefan, Anh Nguyen-Tuong, Jason D. Hiser, Jack W. Davidson, and Matthew Hicks. 2021. "Same Coverage, Less Bloat: Accelerating Binary-Only Fuzzing with Coverage-Preserving Coverage-Guided Tracing." In *Proceedings of the 2021 ACM SIGSAC Conference on Computer and Communications Security*. ACM. [https://doi.org/10.1145/3460120.3484787][research_nagy_2021]
- Nakamura, Ibuki, Yutaro Kashiwa, Bin Lin, and Hajimu Iida. 2026. "Understanding Self-Admitted Technical Debt in Test Code: An Empirical Study." *ACM Transactions on Software Engineering and Methodology* 35 (9): 1–35. [https://doi.org/10.1145/3786791][research_nakamura_2026]
- Nakanishi, Atsushi. 2025. "Automated Generation and Evaluation of Vocabulary Tests: A Large Language Model Approach." In *INTED Proceedings*, vol. 1. IATED. [https://doi.org/10.21125/inted.2025.0016][research_nakanishi_2025]
- Nakao, Masahiro, and Hitoshi Murai. 2020. "Implementation and Performance Evaluation of Omni Compiler." In *XcalableMP PGAS Programming Language*. Springer Singapore. [https://doi.org/10.1007/978-981-15-7683-6\_2][research_nakao_2020]
- Nakata, Yuki, and Katsuya Matsubara. 2025. "Self-Hosted WebAssembly Runtime for Runtime-Neutral Checkpoint/Restore in Edge-Cloud Continuum." In *Proceedings of the 3rd International Workshop on Middleware for the Computing Continuum*. ACM. [https://doi.org/10.1145/3774898.3778040][research_nakata_2025]
- Nayebi, Fatih, Alain Abran, and Jean-Marc Desharnais. 2015. "Automated Selection of a Software Effort Estimation Model Based on Accuracy and Uncertainty." *Artificial Intelligence Research* 4 (2). [https://doi.org/10.5430/air.v4n2p45][research_nayebi_2015]
- Nazar, Rogelio, and Irene Renau. 2016. "A Taxonomy of Spanish Nouns, a Statistical Algorithm to Generate It and Its Implementation in Open Source Code." In *Proceedings of the Language Resources and Evaluation Conference*. European Language Resources Association (ELRA). [https://doi.org/10.63317/55dbkcxk94vf][research_nazar_2016]
- Nemhauser, G. L., and L. A. Wolsey. 1978. "Best Algorithms for Approximating the Maximum of a Submodular Set Function." *Mathematics of Operations Research* 3 (3): 177–88. [https://doi.org/10.1287/moor.3.3.177][research_nemhauser_wolsey_1978b]
- Nesterenko, O. V. 2024. "The Method of Requirements Prioritization in Software Engineering." *Problems in Programming*, no. 2–3: 132–39. [https://doi.org/10.15407/pp2024.02-03.132][research_anon_2024]
- Ngadiyono, Ngadiyono, and Hero Wintolo. 2015. "Penerapan Pemrosesan Paralel Untuk Menguji Waktu Rendering Design Web Dengan Framework Terhadap Processor Melalui Lan, Router Dan Ekstranet." *Compiler* 4 (1). [https://doi.org/10.28989/compiler.v4i1.88][research_ngadiyono_2015]
- Ngo, Van-Chan, Jean-Pierre Talpin, Thierry Gautier, Loïc Besnard, and Paul Le Guernic. 2015. "Modular Translation Validation of a Full-Sized Synchronous Compiler Using off-the-Shelf Verification Tools." In *Proceedings of the 18th International Workshop on Software and Compilers for Embedded Systems*. ACM. [https://doi.org/10.1145/2764967.2775291][research_ngo_2015]
- Nguyen, ThanhVu, Timos Antonopoulos, Andrew Ruef, and Michael Hicks. 2017. "Counterexample-Guided Approach to Finding Numerical Invariants." In *Proceedings of the 2017 11th Joint Meeting on Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/3106237.3106281][research_nguyen_2017]
- Nguyen, Anh Tuan, Hoan Anh Nguyen, and Tien N. Nguyen. 2016. "A Large-Scale Study on Repetitiveness, Containment, and Composability of Routines in Open-Source Projects." In *Proceedings of the 13th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/2901739.2901759][research_nguyen_2016]
- Niharika, Nakod. 2025. "Achieving High-Integrity Software Quality and Security through Automated Code Analysis, Testing, and Advanced Code Coverage with the LDRA Tool Suite." *International Journal of Innovative Science and Research Technology*: 732–39. [https://doi.org/10.38124/ijisrt/25jul468][research_niharika_2025]
- Nongpoh, Bernard, Marwan Nour, Michaël Marcozzi, and Sébastien Bardin. 2022. "Fine-Grained Coverage-Based Fuzzing." In *Proceedings FUZZING 2022 - 1st International Fuzzing Workshop*. Internet Society. [https://doi.org/10.14722/fuzzing.2022.23007][research_nongpoh_2022]
- Nozaki, Ai, Takuya Kojima, Hiroshi Nakamura, and Hideki Takase. 2024. "MLIR-Based Homomorphic Encryption Compiler for GPU." In *14th International Symposium on Highly Efficient Accelerators and Reconfigurable Technologies (HEART 24))*. ACM. [https://doi.org/10.1145/3665283.3665343][research_nozaki_2024]
- OBrien, David, Sumon Biswas, Sayem Imtiaz, Rabe Abdalkareem, Emad Shihab, and Hridesh Rajan. 2022. "23 Shades of Self-Admitted Technical Debt: An Empirical Study on Machine Learning Software." In *Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/3540250.3549088][research_obrien_2022]
- Odim, M. O., S. A. Arekete, B. O. Oguntunde, and A. O. Lawal. 2023. "'A Multi-Pass Compiler with Code Optimized Abstract Syntax Tree'." *International Journal of Software & Hardware Research in Engineering* 11 (5). [https://doi.org/10.26821/ijshre.11.5.2023.110409][research_odim_2023]
- Ogenrwot, Daniel, and John Businge. 2026. "How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull Requests." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793603][research_ogenrwot_2026]
- Oh, Ji-Yeon. 2016. "Buddhist Studies on Seokbosangjeol and Tasks Ahead: Focus on the Compilation of Buddhist Annotations on Seokbosangjeol." *Bul Gyo Hak Bo* 77: 331. [https://doi.org/10.18587/bh.2016.12.77.331][research_oh_2016]
- Oh, Selim, and Seulbae Kim. 2026. "Detecting Compiler-Introduced Security Bugs via IR Mutation and Coverage-Guided Fuzzing." In *Proceedings of the 19th European Workshop on Systems Security*. ACM. [https://doi.org/10.1145/3803525.3804981][research_oh_2026]
- Oh, Hyeong-Seok, Ji Hwan Yeo, and Soo-Mook Moon. 2015. "Bytecode-to-C Ahead-of-Time Compilation for Android Dalvik Virtual Machine." In *Design, Automation & Test in Europe Conference & Exhibition (DATE), 2015*. IEEE Conference Publications. [https://doi.org/10.7873/date.2015.0927][research_oh_2015]
- Oliveira, Fernando, and Júlio Mattos. 2020. "Analysis of WebAssembly as a Strategy to Improve JavaScript Performance on IoT Environments." In *Anais Estendidos do X Simpósio Brasileiro de Engenharia de Sistemas Computacionais (SBESC Estendido 2020)*. Sociedade Brasileira de Computação - SBC. [https://doi.org/10.5753/sbesc\_estendido.2020.13102][research_oliveira_2020]
- Ostrand, Thomas J., and Elaine J. Weyuker. 2002. "The Distribution of Faults in a Large Industrial Software System." In *Proceedings of the 2002 ACM SIGSOFT international symposium on Software testing and analysis*. ACM. [https://doi.org/10.1145/566172.566181][research_ostrand_weyuker_2002]
- Owen, Guillermo. 1972. "Multilinear Extensions of Games." *Management Science* 18 (5-part-2): 64–79. [https://doi.org/10.1287/mnsc.18.5.64][research_owen_1972]
- ÖZkilbaÇ, Bahadır, and Tevhit Karacali. 2022. "Design of RISC Processor with IEEE754 Standard Floating-Point Instruction Set in FPGA Using VHDL for Digital Signal Processing Applications." *Erzincan Üniversitesi Fen Bilimleri Enstitüsü Dergisi* 15 (3): 699–714. [https://doi.org/10.18185/erzifbed.1077921][research_ozkilbac_2022]
- Padhi, Amit, and Mark Willis. 2019. "Accurate Quasi-SV Traveltimes in 3D Transversely Isotropic Media with Vertical Axis of Symmetry Using a High-Order Fast-Sweeping-Based Eikonal Solver." In *International Meeting for Applied Geoscience & Energy*, vol. 1. Society of Exploration Geophysicists. [https://doi.org/10.1190/segam2019-3216245.1][research_padhi_2019]
- Padhi, Amit, Mark Willis, and Xiaomin Zhao. 2017. "Accurate Quasi-P Traveltimes in 3D Transversely Isotropic Media Using a High-Order Fast-Sweeping-Based Eikonal Solver." In *International Meeting for Applied Geoscience & Energy*, vol. 1. Society of Exploration Geophysicists. [https://doi.org/10.1190/segam2017-17587724.1][research_padhi_2017]
- Pan, Haolin, Hongyu Lin, Haoran Luo, et al. 2025a. "Compiler-R1: Towards Agentic Compiler Auto-Tuning with Reinforcement Learning." In *Advances in Neural Information Processing Systems 38*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/085713-2951][research_pan_2025]
- Pan, Haolin, Yin Zhang, Mingjie Xing, and Yanjun Wu. 2025b. "Navigating the SIMD Optimization Maze: A Reinforcement Learning Approach to Library and Compiler Co-Optimization." In *International Conferences on Software Engineering and Knowledge Engineering*, vol. 2025. KSI Research Inc. [https://doi.org/10.18293/seke2025-076][research_pan_2025_b]
- Papadakis, Mike, Donghwan Shin, Shin Yoo, and Doo-Hwan Bae. 2018. "Are Mutation Scores Correlated with Real Fault Detection?: A Large Scale Empirical Study on the Relationship between Mutants and Real Faults." In *Proceedings of the 40th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3180155.3180183][research_papadakis_2018]
- Paraman, Padma Priya Dharishini, and Prakriya V. Ramana Murthy. 2023. "Analysis of Benchmark Program Results of Worst Case Execution Time for Multithreaded Programs." *Indonesian Journal of Electrical Engineering and Computer Science* 29 (2): 990. [https://doi.org/10.11591/ijeecs.v29.i2.pp990-1005][research_paraman_2023]
- Park, HyukWoo, SungKook Kim, and Soo-Mook Moon. 2017. "Advanced Ahead-of-Time Compilation for Javascript Engine: Work-in-Progress." In *Proceedings of the 2017 International Conference on Compilers, Architectures and Synthesis for Embedded Systems Companion*. ACM. [https://doi.org/10.1145/3125501.3125512][research_park_2017]
- Park, Hyukwoo, Sungkook Kim, Jung-Geun Park, and Soo-Mook Moon. 2018. "Reusing the Optimized Code for JavaScript Ahead-of-Time Compilation." *ACM Transactions on Architecture and Code Optimization* 15 (4): 1–20. [https://doi.org/10.1145/3291056][research_park_2018]
- Parry, Owain, Gregory M. Kapfhammer, Michael Hilton, and Phil McMinn. 2022. "What Do Developer-Repaired Flaky Tests Tell Us about the Effectiveness of Automated Flaky Test Detection?" In *Proceedings of the 3rd ACM/IEEE International Conference on Automation of Software Test*. ACM. [https://doi.org/10.1145/3524481.3527227][research_parry_2022]
- Parsert, Julian, and Elizabeth Polgreen. 2024. "Reinforcement Learning and Data-Generation for Syntax-Guided Synthesis." *Proceedings of the AAAI Conference on Artificial Intelligence* 38 (9): 10670–78. [https://doi.org/10.1609/aaai.v38i9.28938][research_parsert_2024]
- Păsăreanu, Corina S., Rody Kersten, Kasper Luckow, and Quoc-Sang Phan. 2019. "Symbolic Execution and Recent Applications to Worst-Case Execution, Load Testing, and Security Analysis." In *Advances in Computers*. Elsevier. [https://doi.org/10.1016/bs.adcom.2018.10.004][research_pasareanu_2019]
- Patel, Radha, Willow Ahrens, and Saman Amarasinghe. 2025. "SySTeC: A Symmetric Sparse Tensor Compiler." In *Proceedings of the 23rd ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3696443.3708919][research_patel_2025]
- Patil, Abhinandan H., Neena Goveas, and Krishnan Rangarajan. 2018. "Generating Effective Test Suite for Multiparameter Software Using ACTS Tool and Its Verification Using Code Coverage Tools." *International Journal of Scientific & Engineering Research* 9 (8): 1579–82. [https://doi.org/10.14299/ijser.2018.08.04][research_patil_2018]
- Pavlidakis, Manos, Chris Kitching, Nicholas Tomlinson, and Michael Søndergaard. 2024. "SCALE-Ahead-Of-Time Compilation of CUDA for AMD GPUs." In *Proceedings of the 25th International Middleware Conference: Demos, Posters and Doctoral Symposium*. ACM. [https://doi.org/10.1145/3704440.3704782][research_pavlidakis_2024]
- Peker, Melih, and Ozcan Ozturk. 2023. "Fast Compiler Optimization Flag Selection." In *Proceedings of the 34th International Workshop on Rapid System Prototyping*. ACM. [https://doi.org/10.1145/3625223.3649273][research_peker_2023]
- Pelayo-Benedet, Tomás, Kevin Borgolte, and Ricardo J. Rodríguez. 2026. "Does Representation Matter? Evaluating IRs for LLM-Based Binary Decompilation." In *Proceedings 2026 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2026.23077][research_pelayobenedet_2026]
- Petrović, Goran, and Marko Ivanković. 2018. "State of Mutation Testing at Google." In *Proceedings of the 40th International Conference on Software Engineering: Software Engineering in Practice*. ACM. [https://doi.org/10.1145/3183519.3183521][research_petrovic_2018_b]
- Phan, Hung, and Ali Jannesari. 2022. "Heterogeneous Graph Neural Networks for Software Effort Estimation." In *Proceedings of the 16th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement*. ACM. [https://doi.org/10.1145/3544902.3546248][research_phan_2022]
- Pietri, Antoine, Diomidis Spinellis, and Stefano Zacchiroli. 2020. "The Software Heritage Graph Dataset: Large-Scale Analysis of Public Software Development History." In *Proceedings of the 17th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3379597.3387510][research_pietri_2020]
- Pina, Diogo, Carolyn Seaman, and Alfredo Goldman. 2022. "Technical Debt Prioritization: A Developer's Perspective." In *Proceedings of the International Conference on Technical Debt*. ACM. [https://doi.org/10.1145/3524843.3528096][research_pina_2022]
- Plangger, Richard, and Andreas Krall. 2016. "Vectorization in PyPy's Tracing Just-In-Time Compiler." In *Proceedings of the 19th International Workshop on Software and Compilers for Embedded Systems*. ACM. [https://doi.org/10.1145/2906363.2906384][research_plangger_2016]
- Polikarpova, Nadia, Julian Tschannen, and Carlo A. Furia. 2018. "A Fully Verified Container Library." *Formal Aspects of Computing* 30 (5): 495–523. [https://doi.org/10.1007/s00165-017-0435-1][research_polikarpova_2018]
- Pop, Paul, Mirela Alistar, Elena Stuart, and Jan Madsen. 2016. "Compilation for Operation Execution Time Variability." In *Fault-Tolerant Digital Microfluidic Biochips*. Springer International Publishing. [https://doi.org/10.1007/978-3-319-23072-6\_12][research_pop_2016]
- Popovic, Jovan, Dragan Bojic, and Nenad Korolija. 2015. "Analysis of Task Effort Estimation Accuracy Based on Use Case Point Size." *IET Software* 9 (6): 166–73. [https://doi.org/10.1049/iet-sen.2014.0254][research_popovic_2015]
- Prabhu, Tarun, and William Gropp. 2017. "DAME: Runtime-Compilation for Data Movement." *International Journal of High Performance Computing Applications* 32 (5): 760–74. [https://doi.org/10.1177/1094342017695444][research_prabhu_2017]
- Proy, Julien, Karine Heydemann, Alexandre Berzati, and Albert Cohen. 2017. "Compiler-Assisted Loop Hardening against Fault Attacks." *ACM Transactions on Architecture and Code Optimization* 14 (4): 1–25. [https://doi.org/10.1145/3141234][research_proy_2017]
- Puri, Swati, and Sheena Singh. 2016. "Techniques of Test Case Prioritization." *International Journal of Scientific Engineering and Research* 4 (4): 63–65. [https://doi.org/10.70729/ijser15755][research_puri_2016]
- Puspaningrum, Alifia, Fachrul Pralienka Bani Muhammad, and Esti Mulyani. 2021. "Flower Pollination Algorithm for Software Effort Coefficients Optimization to Improve Effort Estimation Accuracy." *JUITA: Jurnal Informatika* 9 (2): 139. [https://doi.org/10.30595/juita.v9i2.10511][research_puspaningrum_2021]
- Putra, Ananda Adhitya, Fajar Khanif Rahmawati, Sri Mulyani, Maria Asumpta Deny Kusumaningrum, Gunawan Gunawan, and Rully Medianto. 2024. "Passenger Queue Simulation Analysis and Optimization at the Check-in Counter of Yogyakarta International Airport." *Compiler* 13 (2): 107. [https://doi.org/10.28989/compiler.v13i2.2653][research_putra_2024]
- Qasim, Awais, Syed Asad Raza Kazmi, and Ilyas Fakhir. 2015. "Executable Semantics for the Formal Specification and Verification of E-Agents." *Indian Journal of Science and Technology* 8 (16). [https://doi.org/10.17485/ijst/2015/v8i16/55160][research_qasim_2015]
- Qian, Peng, Xinlei Ying, Jiashui Wang, et al. 2025. "FreeWavm: Enhanced WebAssembly Runtime Fuzzing Guided by Parse Tree Mutation and Snapshot." *Proceedings of the ACM on Software Engineering* 2 (ISSTA): 159–81. [https://doi.org/10.1145/3728877][research_qian_2025]
- Qian, Ruixiang, Quanjun Zhang, Chunrong Fang, and Lihua Guo. 2022. "Investigating Coverage Guided Fuzzing with Mutation Testing." In *Proceedings of the 13th Asia-Pacific Symposium on Internetware*. ACM. [https://doi.org/10.1145/3545258.3545285][research_qian_2022]
- Qu, Xinxue (Shawn), Francis Bilson Darku, and Hong Guo. 2026. "Shapley Value-Based Feature Attribution for Data Masking." *MIS Quarterly* 50 (1): 145–76. [https://doi.org/10.25300/misq/2025/18502][research_qu_2026]
- Quiring, Benjamin, John Reppy, and Olin Shivers. 2021. "3CPS: The Design of an Environment-Focussed Intermediate Representation." In *33rd Symposium on Implementation and Application of Functional Languages*. ACM. [https://doi.org/10.1145/3544885.3544889][research_quiring_2021]
- Rahman, Shanto, and August Shi. 2024. "FlakeSync: Automatically Repairing Async Flaky Tests." In *Proceedings of the IEEE/ACM 46th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3597503.3639115][research_rahman_2024]
- Ramakrishnan, Shankar, and E. K. Girisan. 2025. "An Explainable Deep Learning Model in Improving Test Case Prioritization for Continuous Integration Testing." *International Journal of Science and Research (IJSR)*: 703–10. [https://doi.org/10.21275/sr25813194634][research_ramakrishnan_2025]
- Ramasundaram, T. 2020. "TABU Search Prioritized Ant Colony Metaheuristic Optimization Based Dynamic Symbolic Genetic Technique for High Coverage Test Suite Generation." *Journal of Advanced Research in Dynamical and Control Systems* 12 (01-Special Issue): 324–36. [https://doi.org/10.5373/jardcs/v12sp1/20201079][research_t_2020]
- Ramler, Rudolf, Thomas Wetzlmaier, and Claus Klammer. 2017. "An Empirical Study on the Application of Mutation Testing for a Safety-Critical Industrial Software System." In *Proceedings of the Symposium on Applied Computing*. ACM. [https://doi.org/10.1145/3019612.3019830][research_ramler_2017]
- Ravedutti Lucio Machado, Rafael, Jan Eitzinger, and Harald Köstler. 2025. "P4IRS: An Intermediate Representation and Compiler for Parallel and Performance-Portable Particle Simulations." *International Journal of High Performance Computing Applications* 40 (5): 621–42. [https://doi.org/10.1177/10943420251405928][research_raveduttilucio_2025]
- Rawat, Pradeep Singh, and Prateek Kumar Soni. 2024. "Efficient Virtual Machine Allocation Technique Based on Hybrid Approach." In *Advanced Computing Techniques for Optimization in Cloud*. Chapman and Hall/CRC. [https://doi.org/10.1201/9781003457152-5][research_rawat_2024]
- Ray, Baishakhi, Daryl Posnett, Premkumar Devanbu, and Vladimir Filkov. 2017. "A Large-Scale Study of Programming Languages and Code Quality in GitHub." *Communications of the ACM* 60 (10): 91–100. [https://doi.org/10.1145/3126905][research_ray_2017]
- Ray, Baishakhi, Daryl Posnett, Vladimir Filkov, and Premkumar Devanbu. 2014. "A Large Scale Study of Programming Languages and Code Quality in Github." In *Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/2635868.2635922][research_ray_2014]
- Refnaldi, Refnaldi, Sri Novianti, and Aryuliva Adnan. 2019. "Alumni’s Perception on Program Specification of ELT Program at UNP (Based on AUN-QA Criteria)." In *Proceedings of the Sixth of International Conference on English Language and Teaching (ICOELT 2018)*. Atlantis Press. [https://doi.org/10.2991/icoelt-18.2019.27][research_refnaldi_2019]
- Regehr, John, Alastair Reid, and Kirk Webb. 2005. "Eliminating Stack Overflow by Abstract Interpretation." *ACM Transactions on Embedded Computing Systems* 4 (4): 751–78. [https://doi.org/10.1145/1113830.1113833][research_regehr_2005]
- Reijers, Niels, and Chi-Sheng Shih. 2019. "Improved Ahead-of-Time Compilation of Stack-Based JVM Bytecode on Resource-Constrained Devices." *ACM Transactions on Sensor Networks* 15 (3): 1–44. [https://doi.org/10.1145/3341170][research_reijers_2019]
- Reis, Luís, João Bispo, and João M. P. Cardoso. 2017. "Compiler Techniques for Efficient MATLAB to OpenCL Code Generation." In *Proceedings of the 5th International Workshop on OpenCL*. ACM. [https://doi.org/10.1145/3078155.3078186][research_reis_2017]
- Resmi, V., and S. Vijayalakshmi. 2019. "Analogy-Based Approaches to Improve Software Project Effort Estimation Accuracy." *Journal of Intelligent Systems* 29 (1): 1468–79. [https://doi.org/10.1515/jisys-2019-0023][research_resmi_2019]
- Rezgui, Rayhane, Mohammed Saeed, and Paolo Papotti. 2021. "Automatic Verification of Data Summaries." In *Proceedings of the 14th International Conference on Natural Language Generation*. Association for Computational Linguistics. [https://doi.org/10.18653/v1/2021.inlg-1.27][research_rezgui_2021]
- Rice, H. G. 1953. "Classes of Recursively Enumerable Sets and Their Decision Problems." *Transactions of the American Mathematical Society* 74 (2): 358–66. [https://doi.org/10.1090/s0002-9947-1953-0053041-6][research_rice_1953]
- Rizvi, Sheenu, S. Q. Abbas, and Rizwan Beg. 2015. "Empirical Application of Simulated Annealing Using Object-Oriented Metrics to Increase the Accuracy in Software Effort Estimation." *International Journal on Computational Science & Applications* 5 (6): 39–53. [https://doi.org/10.5121/ijcsa.2015.5603][research_rizvi_2015]
- Rizwan, Syed, Wang Tiantian, Su Xiaohong, and Salahuddin. 2017. "Empirical Study on Software Bug Prediction." In *Proceedings of the 2017 International Conference on Software and e-Business*. ACM. [https://doi.org/10.1145/3178212.3178221][research_rizwan_2017]
- Rodrigues, Tiago B., Alexandre Rodrigues, Manuel Goulão, Pedro Tomás, and Leonel Sousa. 2025. "Accelerating NTT with RISC-V Vector Extension for Fully Homomorphic Encryption." *IACR Transactions on Cryptographic Hardware and Embedded Systems* 2025 (4): 711–36. [https://doi.org/10.46586/tches.v2025.i4.711-736][research_rodrigues_2025]
- Rodriguez Ferrandez, Ivan, Alvaro Jover Alvarez, Matina Maria Trompouki, Leonidas Kosmidis, and Francisco J. Cazorla. 2023. "Worst Case Execution Time and Power Estimation of Multicore and GPU Software: A Pedestrian Detection Use Case." *ACM SIGAda Ada Letters* 43 (1): 111–17. [https://doi.org/10.1145/3631483.3631502][research_rodriguezferra_2023]
- Rokotyanskaya, Violyetta Valeryevna, and Vadim Sergeevich Abramov. 2023. "Studying WebAssembly and Comparison of Its Performance with JavaScript." *Vestnik of Astrakhan State Technical University. Series: Management, computer science and informatics* 2023 (2): 93–100. [https://doi.org/10.24143/2072-9502-2023-2-93-100][research_rokotyanskaya_2023]
- Romano, Alan, and Weihang Wang. 2023a. "Automated WebAssembly Function Purpose Identification with Semantics-Aware Analysis." In *Proceedings of the ACM Web Conference 2023*. ACM. [https://doi.org/10.1145/3543507.3583235][research_romano_2023]
- Romano, Alan, and Weihang Wang. 2023b. "When Function Inlining Meets WebAssembly: Counterintuitive Impacts on Runtime Performance." In *Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/3611643.3616311][research_romano_2023_b]
- Rosenthal, Robert. 1979. "The File Drawer Problem and Tolerance for Null Results." *Psychological Bulletin* 86 (3): 638–41. [https://doi.org/10.1037/0033-2909.86.3.638][research_rosenthal_1979]
- Rossi, Davide, and Stefano Zacchiroli. 2022. "Geographic Diversity in Public Code Contributions: An Exploratory Large-Scale Study over 50 Years." In *Proceedings of the 19th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3524842.3528471][research_rossi_2022]
- Rothermel, Gregg, and Mary Jean Harrold. 1997. "A Safe, Efficient Regression Test Selection Technique." *ACM Transactions on Software Engineering and Methodology* 6 (2): 173–210. [https://doi.org/10.1145/248233.248262][research_rothermel_harrold_1997]
- Roze, K., and D. Radchenko. 2017. "Multi-Level Physical Hierarchy Floorplanning Using IC COMPILER II." *ELECTRONICS: Science, Technology, Business* 4 (164): 72–79. [https://doi.org/10.22184/1992-4178.2017.164.4.72.79][research_roze_2017]
- Saad, Mootez, and Tushar Sharma. 2024. "Naturalness of Attention: Revisiting Attention in Code Language Models." In *Proceedings of the 2024 ACM/IEEE 44th International Conference on Software Engineering: New Ideas and Emerging Results*. ACM. [https://doi.org/10.1145/3639476.3639774][research_saad_2024]
- Sabou, Marta, Dietmar Winkler, and Stefan Biffl. 2020. "Empirical Software Engineering Experimentation with Human Computation." In *Contemporary Empirical Methods in Software Engineering*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-32489-6\_7][research_sabou_2020]
- Sadaei, Hossein Javedani, Salvatore Loguercio, Mahdi Shafiei Neyestanak, Ali Torkamani, and Daria Prilutsky. 2023. "Zoish: A Novel Feature Selection Approach Leveraging Shapley Additive Values for Machine Learning Applications in Healthcare." In *Biocomputing 2024*. WORLD SCIENTIFIC. [https://doi.org/10.1142/9789811286421\_0007][research_sadaei_2023]
- Saha, Prashanta, and Upulee Kanewala. 2018. "Fault Detection Effectiveness of Source Test Case Generation Strategies for Metamorphic Testing." In *Proceedings of the 3rd International Workshop on Metamorphic Testing*. ACM. [https://doi.org/10.1145/3193977.3193982][research_saha_2018]
- Sajati, Haruno, Astika Ayuningtyas, and Dwi Kholistyanto. 2017. "Penerapan Eigenface Untuk Computer Based Test (Cbt) Penerimaan Mahasiswa Baru Sekolah Tinggi Teknologi Adisutjipto." *Compiler* 6 (2). [https://doi.org/10.28989/compiler.v6i2.228][research_sajati_2017]
- Santos, Fernando Fernandes Dos, Luigi Carro, Flavio Vella, and Paolo Rech. 2024a. "Assessing the Impact of Compiler Optimizations on GPUs Reliability." *ACM Transactions on Architecture and Code Optimization* 21 (2): 1–22. [https://doi.org/10.1145/3638249][research_santos_2024_b]
- Santos, Sofia, João Saraiva, and Francisco Ribeiro. 2024b. "Large Language Models in Automated Repair of Haskell Type Errors." In *Proceedings of the 5th ACM/IEEE International Workshop on Automated Program Repair*. ACM. [https://doi.org/10.1145/3643788.3648012][research_santos_2024_c]
- Sanusi, Bashir, Emmanuel Ogunshile, Mehmet Aydin, and Stephen Olabiyisi. 2024. "Assuring Correctness, Testing, and Verification of X-Compiler by Integrating Communicating Stream X-Machine." In *Proceedings of the 2024 6th International Conference on Software Engineering and Development*. ACM. [https://doi.org/10.1145/3686614.3686622][research_sanusi_2024]
- Saputra, Andika Bayu. 2020. "Implementation of Genetic Algorithm in College Scheduling System Ftti Unjani Yogyakarta." *Compiler* 9 (1). [https://doi.org/10.28989/compiler.v9i1.656][research_saputra_2020]
- Saputro, Halim Teguh, Usman Nurhasan, and Vivi Nur Wijayaningrum. 2025. "Programming Assessment in E-Learning through Rule-Based Automatic Question Generation with Large Language Models." *Journal of Applied Informatics and Computing* 9 (6): 3356–62. [https://doi.org/10.30871/jaic.v9i6.10901][research_saputro_2025]
- Satapathy, Shashank Mouli, and Santanu Kumar Rath. 2017. "Empirical Assessment of Machine Learning Models for Effort Estimation of Web-Based Applications." In *Proceedings of the 10th Innovations in Software Engineering Conference*. ACM. [https://doi.org/10.1145/3021460.3021468][research_satapathy_2017]
- Sawasdee, Bunyarit, and Twittie Senivongse. 2025. "An Empirical Study on Software Developer-Related Factors and Technical Debt in Open-Source Software Projects." In *Proceedings of the 2025 9th International Conference on Software and e-Business*. ACM. [https://doi.org/10.1145/3789037.3789048][research_sawasdee_2025]
- Schkufza, Eric, Rahul Sharma, and Alex Aiken. 2013. "Stochastic Superoptimization." In *Proceedings of the eighteenth international conference on Architectural support for programming languages and operating systems*. ACM. [https://doi.org/10.1145/2451116.2451150][research_schkufza_2013]
- Schkufza, Eric, Michael Wei, and Christopher J. Rossbach. 2019. "Just-In-Time Compilation for Verilog: A New Technique for Improving the FPGA Programming Experience." In *Proceedings of the Twenty-Fourth International Conference on Architectural Support for Programming Languages and Operating Systems*. ACM. [https://doi.org/10.1145/3297858.3304010][research_schkufza_2019]
- Schoch, Stephanie, Haifeng Xu, and Yangfeng Ji. 2022. "CS-Shapley: Class-Wise Shapley Values for Data Valuation in Classification." In *Advances in Neural Information Processing Systems 35*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/068431-2505][research_schoch_2022]
- Schuiki, Fabian, Andreas Kurth, Tobias Grosser, and Luca Benini. 2020b. *Replication Package for Paper: LLHD: A Multi-Level Intermediate Representation for Hardware Description Languages*. Association for Computing Machinery (ACM). [https://doi.org/10.1145/3395654][research_schuiki_2020_b]
- Schulte, Eric, Jason Ruchti, Matt Noonan, David Ciarletta, and Alexey Loginov. 2018. "Evolving Exact Decompilation." In *Proceedings 2018 Workshop on Binary Analysis Research*. Internet Society. [https://doi.org/10.14722/bar.2018.23008][research_schulte_2018]
- Scott, Ezequiel, Fredrik Milani, and Dietmar Pfahl. 2020. "Data Science and Empirical Software Engineering." In *Contemporary Empirical Methods in Software Engineering*. Springer International Publishing. [https://doi.org/10.1007/978-3-030-32489-6\_8][research_scott_2020]
- Segall, Richard S. 2020. "Open Source Software (OSS) for Big Data." In *Advances in Computer and Electrical Engineering*. IGI Global. [https://doi.org/10.4018/978-1-7998-2768-9.ch002][research_segall_2020]
- Serrano, Manuel. 2022. "On JavaScript Ahead-of-Time Compilation Performance (Keynote)." In *Proceedings of the 19th International Conference on Managed Programming Languages and Runtimes*. ACM. [https://doi.org/10.1145/3546918.3560825][research_serrano_2022]
- Serrano, Alejandro, and Jurriaan Hage. 2019. "A Compiler Architecture for Domain-Specific Type Error Diagnosis." *Open Computer Science* 9 (1): 33–51. [https://doi.org/10.1515/comp-2019-0002][research_serrano_2019]
- Sethi, Ravi, and J. D. Ullman. 1970. "The Generation of Optimal Code for Arithmetic Expressions." *Journal of the ACM* 17 (4): 715–28. [https://doi.org/10.1145/321607.321620][research_sethi_ullman_1970]
- Shafigh, Saman, Boualem Benatallah, Carlos Rodríguez, and Mortada Al-Banna. 2021. "Why Some Bug-Bounty Vulnerability Reports Are Invalid?: Study of Bug-Bounty Reports and Developing an out-of-Scope Taxonomy Model." In *Proceedings of the 15th ACM / IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. ACM. [https://doi.org/10.1145/3475716.3484193][research_shafigh_2021]
- Shankar, Vasuki. 2025. "Advancements in AI-Based Compiler Optimization Techniques for Machine Learning Workloads." *International Journal of Computer Sciences and Engineering* 13 (3): 70–77. [https://doi.org/10.26438/ijcse/v13i3.7077][research_shankar_2025]
- Shanmuganathan, M., and K. Kajendran. 2018. "Flaws of Quantification Method as Applied to Software Requirements Prioritization." *International Journal of Engineering Research and* V6 (02). [https://doi.org/10.17577/ijertcon091][research_mshanmuganatha_2018]
- Shapley, L. S. 1953. "17. a Value for n-Person Games." In *Contributions to the Theory of Games (AM-28), Volume II*. Princeton University Press. [https://doi.org/10.1515/9781400881970-018][research_shapley_1953]
- Sharma, Tushar. 2024. "Multi-Faceted Code Smell Detection at Scale Using DesigniteJava 2.0." In *Proceedings of the 21st International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3643991.3644881][research_sharma_2024]
- Sharma, Sheetal, and Swati V. Chande. 2023. "Optimizing Test Case Prioritization Using Machine Learning Algorithms." *Journal of Autonomous Intelligence* 6 (2): 661. [https://doi.org/10.32629/jai.v6i2.661][research_sharma_2023_b]
- Sharma, Pushti, Gurpreet Singh, and Navneet Kaur. 2023a. "Data Valuation Using Shapley Value in Machine Learning." In *AIP Conference Proceedings*, vol. 2916. AIP Publishing. [https://doi.org/10.1063/5.0178097][research_sharma_2023_c]
- Sharma, Mayank, Pingshi Yu, and Alastair F. Donaldson. 2023b. "RustSmith: Random Differential Compiler Testing for Rust." In *Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3597926.3604919][research_sharma_2023]
- Sharna, Mayank Mohan, Akshat Agrawal, and \*B. Suresh Kumar. 2019. "Test Case Design and Test Case Prioritization Using Machine Learning." *International Journal of Engineering and Advanced Technology* 9 (1): 2742–48. [https://doi.org/10.35940/ijeat.a9762.109119][research_anon_2019_b]
- Sharrad, Joanna, Olaf Chitil, and Meng Wang. 2018. "Delta Debugging Type Errors with a Blackbox Compiler." In *Proceedings of the 30th Symposium on Implementation and Application of Functional Languages*. ACM. [https://doi.org/10.1145/3310232.3310243][research_sharrad_2018]
- She, Dongdong, Adam Storek, Yuchong Xie, Seoyoung Kweon, Prashast Srivastava, and Suman Jana. 2024. "FOX: Coverage-Guided Fuzzing as Online Stochastic Control." In *Proceedings of the 17th ACM/IEEE International Workshop on Search-Based and Fuzz Testing*. ACM. [https://doi.org/10.1145/3643659.3648562][research_she_2024]
- Shen, Zefan. 2021. "The Impact of Undefined Behavior on Compiler Optimization." In *2021 2nd European Symposium on Software Engineering*. ACM. [https://doi.org/10.1145/3501774.3501781][research_shen_2021]
- Shi, Changqing, Rui Chen, Yufei Sun, et al. 2026. "CKTI: A Domain-Specific Compiler for Lowering CUDA Kernels to Triton-IR." In *Proceedings of the 40th ACM International Conference on Supercomputing*. ACM. [https://doi.org/10.1145/3797905.3800551][research_shi_2026]
- Shi, Zhaoyi, Jun Gao, and Xin Guan. 2024. "Machine Learning-Driven GCC Loop Unrolling Optimization: Compiler Performance Enhancement Strategy Based on XGBoost." *Journal of Circuits, Systems and Computers* 34 (01): 2550035. [https://doi.org/10.1142/s0218126625500355][research_shi_2024_b]
- Shimizu, Takuya, Ryuichi Yoshizawa, Kaoru Otsuka, Yudai Fujiwara, and Yuichi Sugiyama. 2025. "Shepherd: High-Precision Coverage Inference for Response-Guided Blackbox Fuzzing (Registered Report)." In *Proceedings of the 34th ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3713081.3731719][research_shimizu_2025]
- Shin, Yongwon, Juseong Park, Sungjun Cho, and Hyojin Sung. 2023. "PIMFlow: Compiler and Runtime Support for CNN Models on Processing-in-Memory DRAM." In *Proceedings of the 21st ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3579990.3580009][research_shin_2023]
- Shobeiri, Seyedamir, and Mojtaba Aajami. 2022. "Shapley Value Is an Equitable Metric for Data Valuation." *Iraqi Journal for Electrical and Electronic Engineering* 18 (2): 9–14. [https://doi.org/10.37917/ijeee.18.2.2][research_shobeiri_2022]
- Shreyas Madhav, A. V., Siddarth Singaravel, and A. Karmel. 2021. "Memory Utilization and Machine Learning Techniques for Compiler Optimization." *ITM Web of Conferences* 37: 01021. [https://doi.org/10.1051/itmconf/20213701021][research_shreyasmadhav_2021]
- Shyshatska, Olena, Liubomyr Matiichuk, and Andrii Shyshatskyy. 2025. "Specification and Verification of a Formal Model for a Real-Time System Using TLA+." *Central Ukrainian Scientific Bulletin. Technical Sciences* 2 (11(42)): 38–44. [https://doi.org/10.32515/2664-262x.2025.11(42).2.38-44][research_anon_2025_b]
- Sigweni, Boyce, Martin Shepperd, and Tommaso Turchi. 2016. "Realistic Assessment of Software Effort Estimation Models." In *Proceedings of the 20th International Conference on Evaluation and Assessment in Software Engineering*. ACM. [https://doi.org/10.1145/2915970.2916005][research_sigweni_2016]
- Silva, Wilamis Kleiton Nunes da. 2026. "Hybrid Model for Improving the Accuracy of Software Development Team Effort Estimation with Genetic Algorithm-Optimized Regression Ensembles." In *Anais do XXIX Congresso Ibero-Americano em Engenharia de Software (CIbSE 2026)*. Sociedade Brasileira de Computação. [https://doi.org/10.5753/cibse.2026.42458][research_silva_2026]
- Simmons, Joseph P., Leif D. Nelson, and Uri Simonsohn. 2011. "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant." *Psychological Science* 22 (11): 1359–66. [https://doi.org/10.1177/0956797611417632][research_simmons_2011]
- Sivalingam, Saravanan Madderi, and Pavan Kumar Prathapagiri. 2025. "An Efficient Load Balance Using Virtual Machine Migration Hybrid Optimization Technique in Cloud Computing." *Indonesian Journal of Electrical Engineering and Computer Science* 38 (2): 1265. [https://doi.org/10.11591/ijeecs.v38.i2.pp1265-1272][research_sivalingam_2025]
- Sobolewski, Jakub. 2025. *Muttest: Mutation Testing*. The R Foundation. [https://doi.org/10.32614/cran.package.muttest][research_sobolewski_2025]
- Soluian, O., and L. Lіushenko. 2025. "Research of WebAssembly Usage for High-Performance Code Development in Web Applications." *System technologies* 3 (158): 188–200. [https://doi.org/10.34185/1562-9945-3-158-2025-19][research_soluian_2025]
- Spaeh, Fabian Christian, Alina Ene, and Huy Nguyen. 2025. "Online and Streaming Algorithms for Constrained k-Submodular Maximization." *Proceedings of the AAAI Conference on Artificial Intelligence* 39 (19): 20567–74. [https://doi.org/10.1609/aaai.v39i19.34266][research_spaeh_2025]
- Spampinato, Daniele G., and Markus Püschel. 2016. "A Basic Linear Algebra Compiler for Structured Matrices." In *Proceedings of the 2016 International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/2854038.2854060][research_spampinato_2016]
- Spieker, Helge, Arnaud Gotlieb, Dusica Marijan, and Morten Mossige. 2017. "Reinforcement Learning for Automatic Test Case Prioritization and Selection in Continuous Integration." In *Proceedings of the 26th ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3092703.3092709][research_spieker_2017]
- Srinivasa Rao Kongarana. 2024. "Nonlinear Reinforcement Learning-Based Dynamic Test Case Prioritization with Anomaly Detection for Continuous Integration." *Communications on Applied Nonlinear Analysis* 32 (1s): 122–42. [https://doi.org/10.52783/cana.v32.2114][research_srinivasaraoko_2024]
- Srinivasan, Madhusudan, Morteza Pourreza Shahri, Indika Kahanda, and Upulee Kanewala. 2018. "Quality Assurance of Bioinformatics Software: A Case Study of Testing a Biomedical Text Processing Tool Using Metamorphic Testing." In *Proceedings of the 3rd International Workshop on Metamorphic Testing*. ACM. [https://doi.org/10.1145/3193977.3193981][research_srinivasan_2018]
- Stacy, Brook, Jason Hauzel, Mikael Lindvall, Adam Porter, and Mihai Pop. 2022. "Metamorphic Testing in Bioinformatics Software: A Case Study on Metagenomic Assembly." In *Proceedings of the 7th International Workshop on Metamorphic Testing*. ACM. [https://doi.org/10.1145/3524846.3527340][research_stacy_2022]
- Stepanov, Daniil, and Vladimir Itsykson. 2022. "Backend Bug Finder — A Platform for Effective Compiler Fuzzing." *Information and Control Systems*, no. 6: 31–40. [https://doi.org/10.31799/1684-8853-2022-6-31-40][research_stepanov_2022]
- Stepanov, Oleksandr, and Halyna Klym. 2025. "A Quantitative Analysis of Webassembly Integration: Architectural Patterns, Tooling, and Performance Evaluation." *Electronics and Information Technologies* 32: 837. [https://doi.org/10.30970/eli.32.10][research_stepanov_2025]
- Su, Ruoyu, Matteo Esposito, Davide Taibi, and Valentina Lenarduzzi. 2026. "Running Large Language Models at Scale for Mining Software Repositories: Lessons Learned from HPC-Based Batch Inference." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793383][research_su_2026]
- Su, ChiaHui, Chia-Hua Ku, Jenq Kuen Lee, and Kuan-Hsun Chen. 2024. "TreeHouse: An MLIR-Based Compilation Flow for Real-Time Tree-Based Inference." *ACM Transactions on Embedded Computing Systems*: 3704727. [https://doi.org/10.1145/3704727][research_su_2024]
- Subrahmanyam, V., and M. V. Siva Prasad. 2025. "AI-Driven Test Case Generation for Continuous Integration of Software Development." *International Journal of Science and Research (IJSR)*: 711–13. [https://doi.org/10.21275/sr25916082410][research_subrahmanyam_2025]
- Subramanyan, Bala. 2025. "Cwamr: Reimagining a Capabilitybased Webassembly Runtime via Cheri-Based Compartmentalization." In *Computer Science and Information Technology Trends 2025*. Academy & Industry Research Collaboration. [https://doi.org/10.5121/csit.2025.151407][research_subramanyan_2025]
- Sülün, Emre, Metehan Saçakçı, and Eray Tüzün. 2024. "An Empirical Analysis of Issue Templates Usage in Large-Scale Projects on GitHub." *ACM Transactions on Software Engineering and Methodology* 33 (5): 1–28. [https://doi.org/10.1145/3643673][research_sulun_2024]
- Sun, Aoyuan, Yue Tu, Yuhao Gu, Chunyu Chen, Jiangsu Du, and Xianwei Zhang. 2025. "Archs: A WebAssembly Runtime for Cross-Host Heterogeneous Computing in Serverless." In *Proceedings of the 2025 9th International Conference on High Performance Compilation, Computing and Communications*. ACM. [https://doi.org/10.1145/3774949.3774968][research_sun_2025]
- Suo, Chenyao, Junjie Chen, Shuang Liu, Jiajun Jiang, Yingquan Zhao, and Jianrong Wang. 2024. "Fuzzing MLIR Compiler Infrastructure via Operation Dependency Analysis." In *Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3650212.3680360][research_suo_2024]
- Supriyatna, Made Indrayana, Dwi Indriyani, S. Kamilia Aziz, and Ikhomaha Bian Immama. 2025. "Optimasi Pemanfaatan Air Menggunakan Program Solver Di Bendungan Jragung Semarang: OPTIMIZATION OF WATER UTILIZATION USING THE SOLVER PROGRAM AT THE JRAGUNG DAM, SEMARANG." *Ge-STRAM: Jurnal Perencanaan dan Rekayasa Sipil* 8 (2): 124–31. [https://doi.org/10.25139/jprs.v8i2.10926][research_supriyatna_2025]
- Tan, Yong Kiam, Scott Owens, and Ramana Kumar. 2015. "A Verified Type System for CakeML." In *Proceedings of the 27th Symposium on the Implementation and Application of Functional Programming Languages*. ACM. [https://doi.org/10.1145/2897336.2897344][research_tan_2015]
- Tan, Jingjing, Yue Sun, Yicheng Xu, and Juan Zou. 2023a. "Streaming Algorithms for Non-Submodular Maximization on the Integer Lattice." *Tsinghua Science and Technology* 28 (5): 888–95. [https://doi.org/10.26599/tst.2022.9010031][research_tan_2023_b]
- Taneja, Jubi, Zhengyang Liu, and John Regehr. 2020. "Testing Static Analyses for Precision and Soundness." In *Proceedings of the 18th ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3368826.3377927][research_taneja_2020]
- Tang, Yiting. 2024. "Large Language Models Meet Automated Program Repair: Innovations, Challenges and Solutions." *Applied and Computational Engineering* 113 (1): 57–65. [https://doi.org/10.54254/2755-2721/2024.18303][research_tang_2024_b]
- Tang, Xin, Quanyan Gao, and Chao Li. 2026b. "LTSV: Layered Type-Constrained Shapley Value for Heterogeneous Graph Data Valuation." In *Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2*. ACM. [https://doi.org/10.1145/3770855.3817695][research_tang_2026_c]
- Tarashev, Nikola, Kostas Tsatsaronis, and Claudio Borio. 2015. "Risk Attribution Using the Shapley Value: Methodology and Policy Applications." *Review of Finance* 20 (3): 1189–1213. [https://doi.org/10.1093/rof/rfv028][research_tarashev_2015]
- Terres, Luiz Paulo Grafetti, and Samuel da Silva Feitosa. 2025. "Differential Fuzzing Go Compilers Using LLMs: A Methodological Proposal." In *Anais da IX Escola Regional de Engenharia de Software (ERES 2025)*. Sociedade Brasileira de Computação. [https://doi.org/10.5753/eres.2025.16857][research_terres_2025]
- Thangamani, Arun, Tiago Trevisan Jost, Vincent Loechner, Stéphane Genaud, and Bérenger Bramas. 2023a. *Artifact for Lifting Code Generation of Cardiac Physiology Simulation to Novel Compiler Technology*. Association for Computing Machinery (ACM). [https://doi.org/10.1145/3554349][research_thangamani_2023]
- Thangamani, Arun, Tiago Trevisan Jost, Vincent Loechner, Stéphane Genaud, and Bérenger Bramas. 2023b. "Lifting Code Generation of Cardiac Physiology Simulation to Novel Compiler Technology." In *Proceedings of the 21st ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3579990.3580008][research_thangamani_2023_b]
- Thier, Patrick, M. Anton Ertl, and Andreas Krall. 2018. "Fast and Flexible Instruction Selection with Constraints." In *Proceedings of the 27th International Conference on Compiler Construction*. ACM. [https://doi.org/10.1145/3178372.3179501][research_thier_2018]
- Thomson, William. 2019. "The Shapley Value, a Crown Jewel of Cooperative Game Theory." In *Handbook of the Shapley Value*. Chapman and Hall/CRC. [https://doi.org/10.1201/9781351241410-1][research_thomson_2019]
- Tian, Yongqiang, Xiaorong Zhang, Fengwei Yang, et al. 2025. "Runtime Prediction Model for High Performance Computing Jobs Based on Dual Dimensional Feature Fusion." In *Proceedings of the 2025 9th International Conference on High Performance Compilation, Computing and Communications*. ACM. [https://doi.org/10.1145/3774949.3774960][research_tian_2025]
- Tirpankar, Tanmay, Cayden Lund, and Ganesh Gopalakrishnan. 2025. "CIRE: LLVM Analysis for Floating-Point Rounding Error Affected by Precision and Optimizations." In *Proceedings of the SC '25 Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis*. ACM. [https://doi.org/10.1145/3731599.3767479][research_tirpankar_2025]
- Titzer, Ben. 2025. "WebAssembly: How Low Can a Bytecode Go?: New Performance and Capabilities." *Queue* 23 (3): 31–47. [https://doi.org/10.1145/3746172][research_titzer_2025]
- Toeppe, Benny, Amine Barrak, and Emna Ksontini. 2026. "A Large-Scale Dataset of MCP Implementations on GitHub." In *Proceedings of the 23rd International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3793302.3793311][research_toeppe_2026]
- Tong, Weixi, and Tianyi Zhang. 2024. "CodeJudge: Evaluating Code Generation with Large Language Models." In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*. Association for Computational Linguistics. [https://doi.org/10.18653/v1/2024.emnlp-main.1118][research_tong_2024]
- Toosi, Farshad Ghassemi. 2023. "Source Code Features and Their Dependencies: An Aggregative Statistical Analysis on Open-Source Java Software Systems." *Applied Computer Systems* 28 (2): 221–31. [https://doi.org/10.2478/acss-2023-0022][research_toosi_2023]
- Tran, Tan D., Canh V. Pham, and Dung T. K. Ha. 2025. "k-Submodular Maximization under Individual Knapsack Constraints: Applications and Streaming Algorithm." *Asia-Pacific Journal of Operational Research* 43 (04): 2550035. [https://doi.org/10.1142/s0217595925500356][research_tran_2025]
- Uzayr, Sufyan bin. 2022. "Preprocessing and Compilation." In *Mastering C++ Programming Language*. CRC Press. [https://doi.org/10.1201/9781003214762-6][research_uzayr_2022]
- Vaishnavi, V., S. Parthasarathy, Chandrakumar Thangavel, Anitha Gracy, and P. Premnitin. 2023. "Software Effort Estimation Using Validated Accuracy Points for Open-Source Packaged Software." *International Journal of Productivity and Quality Management* 1 (1): 10060668. [https://doi.org/10.1504/ijpqm.2023.10060668][research_v_2023]
- Venkanna, Mood, and Rameshwar Rao. 2018. "Static Worst-Case Execution Time Optimization Using DPSO for ASIP Architecture." *Ingeniería Solidaria* 14 (25): 1–11. [https://doi.org/10.16925/.v14i0.2230][research_venkanna_2018_b]
- Venkanna, Mood, Rameshwar Rao, and P. Chandra Sekhar. 2018. "PSO Based Optimization of Worst-Case Execution Time for ASIP Application." *International Journal of Engineering & Technology* 7 (3.3): 252. [https://doi.org/10.14419/ijet.v7i2.33.14162][research_venkanna_2018]
- Venkatesan, S. 2025. "Towards Autonomous Code Optimization: A Reinforcement Learning Framework for Compiler Design." *International Journal of Applied Mathematics* 38 (11s): 1790–1813. [https://doi.org/10.12732/ijam.v38i11s.1286][research_svenkatesan_2025]
- Versluis, Gerald. 2017a. "Creating and Running Tests with Xamarin Test Cloud." In *Xamarin Continuous Integration and Delivery*. Apress. [https://doi.org/10.1007/978-1-4842-2716-9\_5][research_versluis_2017]
- Versluis, Gerald. 2017b. "Integrating Tests into Your Builds." In *Xamarin Continuous Integration and Delivery*. Apress. [https://doi.org/10.1007/978-1-4842-2716-9\_6][research_versluis_2017_b]
- Voetberg, M., and Brian Nord. 2023. "DeepSurveySim: Simulation Software and Benchmark Challenges for Astronomical Observation Scheduling." In *DeepSurveySim: Simulation Software and Benchmark Challenges for Astronomical Observation Scheduling*. US DOE. [https://doi.org/10.2172/2246791][research_voetberg_2023]
- Vraný, Jan, and Boris Shingarov. 2024. "Tinyrossa: A Compiler Framework for Vertical, Verified Construction of Smalltalk VMs." In *Companion Proceedings of the 8th International Conference on the Art, Science, and Engineering of Programming*. ACM. [https://doi.org/10.1145/3660829.3660838][research_vrany_2024]
- Wang, Chao. 2024b. "Compilation Optimization Methods in the Customization of Reconfigurable Accelerators." In *Domain-Specific Computer Architectures for Emerging Applications*. Chapman and Hall/CRC. [https://doi.org/10.1201/9780429355080-13][research_wang_2024_e]
- Wang, Xingbo, Chenxi Feng, Xinyu Kang, Yuru Li, Yucong Huang, and Terry Tao Ye. 2025a. "Logic Gate Network Inference Acceleration with RISC-V Custom Instruction Set." In *Proceedings of the 22nd ACM International Conference on Computing Frontiers*. ACM. [https://doi.org/10.1145/3719276.3725178][research_wang_2025]
- Wang, Haoyu, Hao Li, Li Li, Yao Guo, and Guoai Xu. 2018b. "Why Are Android Apps Removed from Google Play?: A Large-Scale Empirical Study." In *Proceedings of the 15th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3196398.3196412][research_wang_2018_b]
- Wang, Yuanchao, Ye Tian, Hongmei Wei, and Fei Wang. 2026. "Large Language Models for Binary Decompilation: Paradigms, Evaluation, and Challenges." In *Proceedings of the 2026 6th International Conference on Computer Network Security and Software Engineering*. ACM. [https://doi.org/10.1145/3803633.3803666][research_wang_2026_b]
- Wang, Honglian, Sijing Tu, Lutz Oettershagen, and Aristides Gionis. 2025c. "Streaming Stochastic Submodular Maximization with on-Demand User Requests." In *Advances in Neural Information Processing Systems 38*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/085713-4155][research_wang_2025_c]
- Wang, Yanzhao, and Fei Xie. 2024. "Enhancing Translation Validation of Compiler Transformations with Large Language Models." *International Journal of Software Engineering and Knowledge Engineering* 35 (01): 45–57. [https://doi.org/10.1142/s0218194024500475][research_wang_2024]
- Wang, Bo, Yingfei Xiong, Yangqingwei Shi, Lu Zhang, and Dan Hao. 2017. "Faster Mutation Analysis via Equivalence Modulo States." In *Proceedings of the 26th ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3092703.3092714][research_wang_2017]
- Waseem, Saad, Aicha Moussaid, Ricardo Chavez Tapia, S. M. Zahid Hasan, Iván Porres Paltor, and Sebastien Lafond. 2025. "Dynamic Test Case Prioritization and Selection for Continuous Integration Using Reinforcement Learning." In *Information Systems Engineering and Management*. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-91481-2\_10][research_waseem_2025]
- Wegman, Mark N., and F. Kenneth Zadeck. 1991. "Constant Propagation with Conditional Branches." *ACM Transactions on Programming Languages and Systems* 13 (2): 181–210. [https://doi.org/10.1145/103135.103136][research_wegman_zadeck_1991]
- Wei, Anjiang, Pu Yi, Zhengxi Li, Tao Xie, Darko Marinov, and Wing Lam. 2022. "Preempting Flaky Tests via Non-Idempotent-Outcome Tests." In *Proceedings of the 44th International Conference on Software Engineering*. ACM. [https://doi.org/10.1145/3510003.3510170][research_wei_2022]
- Werner, Michael, Lorenzo Servadei, Robert Wille, and Wolfgang Ecker. 2020. "Automatic Compiler Optimization on Embedded Software through k-Means Clustering." In *Proceedings of the 2020 ACM/IEEE Workshop on Machine Learning for CAD*. ACM. [https://doi.org/10.1145/3380446.3430631][research_werner_2020]
- Wham, Drew C. 2024. "Deployment and Integration of Machine Learning Methods with Continuous Integration/Continuous Delivery." *Journal of Advancement Analytics* 24: 56–63. [https://doi.org/10.1353/jaa.00007][research_wham_2024]
- Wienand, Tobias, Lukas Bernhard, and Flavio Toffalini. 2026. "TYPEFUZZ: Type Coverage Directed JavaScript Engine Fuzzing (Registered Report)." In *Proceedings 2026 International Fuzzing Workshop*. Internet Society. [https://doi.org/10.14722/fuzzing.2026.23005][research_wienand_2026]
- Wilhelm, Reinhard, Jakob Engblom, Andreas Ermedahl, et al. 2008. "The Worst-Case Execution-Time Problem—Overview of Methods and Survey of Tools." *ACM Transactions on Embedded Computing Systems* 7 (3): 1–53. [https://doi.org/10.1145/1347375.1347389][research_wilhelm_2008]
- Wintolo, Hero, and Lalu Septian Dwi Paradita. 2015. "Layanan Cloud Computing Berbasis Infrastructure as a Service Menggunakan Android." *Compiler* 4 (2). [https://doi.org/10.28989/compiler.v4i2.91][research_wintolo_2015]
- Winton, Jonathan, and Francis Palma. 2023. "Improving Software Requirements Prioritization through the Lens of Constraint Satisfaction." *Proceedings of the Canadian Conference on Artificial Intelligence*. [https://doi.org/10.21428/594757db.09e3d60c][research_winton_2023]
- Witthoft, Carl. 2025. *rFocal: Run 'FOCAL' Language Source Code*. The R Foundation. [https://doi.org/10.32614/cran.package.rfocal][research_witthoft_2025]
- Wong, W. Eric, Joseph R. Horgan, Saul London, and Aditya P. Mathur. 1995. "Effect of Test Set Minimization on Fault Detection Effectiveness." In *Proceedings of the 17th international conference on Software engineering - ICSE '95*. ACM Press. [https://doi.org/10.1145/225014.225018][research_wong_1995]
- Wu, Tianyi. 2017. "Automatic Generation of the AADL ALISA Verification Plan with ATL." *International Journal of Performability Engineering*. [https://doi.org/10.23940/ijpe.17.07.p14.11111122][research_wu_2017]
- Wu, Jiaqi, Lingfeng Bao, Xiaohu Yang, Xin Xia, and Xing Hu. 2024b. "A Large-Scale Empirical Study of Open Source License Usage: Practices and Challenges." In *Proceedings of the 21st International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3643991.3644900][research_wu_2024]
- Wu, Xiao, Junzhou He, Liyan Huang, Cai Fu, and Weihang Wang. 2025c. "WBSan: WebAssembly Bug Detection for Sanitization and Binary-Only Fuzzing." In *Proceedings of the ACM on Web Conference 2025*. ACM. [https://doi.org/10.1145/3696410.3714622][research_wu_2025]
- Wu, Hongrun, Haiyang Liu, and Yutao Ma. 2018. "Empirical Study on Developer Factors Affecting Tossing Path Length of Bug Reports." *IET Software* 12 (3): 258–70. [https://doi.org/10.1049/iet-sen.2017.0159][research_wu_2018]
- Wu, Xiaojie, Qiming Sun, and Yuanheng Wang. 2026. "Designing Quantum Chemistry Algorithms with Just-in-Time Compilation." *Journal of Chemical Physics* 164 (19): 194102. [https://doi.org/10.1063/5.0314659][research_wu_2026]
- Wu, Zhaolin, Yang Yang, Zheng Li, and Ruilian Zhao. 2019b. "A Time Window Based Reinforcement Learning Reward for Test Case Prioritization in Continuous Integration." In *Proceedings of the 11th Asia-Pacific Symposium on Internetware*. ACM. [https://doi.org/10.1145/3361242.3361258][research_wu_2019_b]
- Wu, Jingwen, Jiajing Zheng, Zhenyu Yang, and Zhongxing Yu. 2025a. "Compiler Optimization Testing Based on Optimization-Guided Equivalence Transformations." In *Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering*. ACM. [https://doi.org/10.1145/3696630.3728528][research_wu_2025_b]
- Xiao, Yao, Nesreen K. Ahmed, Mihai Capotă, et al. 2025. "A Graph-Based Learning Framework for Compiler Loop Auto-Vectorization." *Intelligent Computing* 4: 0113. [https://doi.org/10.34133/icomputing.0113][research_xiao_2025]
- Xiao, Shanlin, Tsuyoshi Isshiki, Dongju Li, and Hiroaki Kunieda. 2017. "Design of an Application Specific Instruction Set Processor for Real-Time Object Detection Using AdaBoost Algorithm." *IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences* E100.A (7): 1384–95. [https://doi.org/10.1587/transfun.e100.a.1384][research_xiao_2017]
- Xiao, Lei, Huaikou Miao, and Ying Zhong. 2018. "Test Case Prioritization and Selection Technique in Continuous Integration Development Environments: A Case Study." *International Journal of Engineering & Technology* 7 (2.28): 332. [https://doi.org/10.14419/ijet.v7i2.28.13207][research_xiao_2018]
- Xu, Bowen, Amirreza Shirani, David Lo, and Mohammad Amin Alipour. 2018. "Prediction of Relatedness in Stack Overflow: Deep Learning vs. SVM: A Reproducibility Study." In *Proceedings of the 12th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement*. ACM. [https://doi.org/10.1145/3239235.3240503][research_xu_2018]
- Xu, Yufan, Qiwei Yuan, Erik Curtis Barton, Rui Li, P. Sadayappan, and Aravind Sukumaran-Rajam. 2022. "Effective Performance Modeling and Domain-Specific Compiler Optimization of CNNs for GPUs." In *Proceedings of the International Conference on Parallel Architectures and Compilation Techniques*. ACM. [https://doi.org/10.1145/3559009.3569674][research_xu_2022]
- Yahyaoui, Khadidja. 2022. *Hybrid Approach Based on Multi-Agent System and Fuzzy Logic for Mobile Robot Autonomous Navigation*. Wiley. [https://doi.org/10.1002/9781119902881.ch7][research_yahyaoui_2022]
- Yang, Yilu. 2024. "Bridging Efficacy and Efficiency: Innovations in Shapley Value Estimation for Model-Agnostic Data Valuation in Machine Learning." In *Fourth International Conference on Signal Processing and Machine Learning (CONF-SPML 2024)*, edited by Sana Ullah Jan. SPIE. [https://doi.org/10.1117/12.3027116][research_yang_2024_c]
- Yang, Chen, Junjie Chen, Xingyu Fan, Jiajun Jiang, and Jun Sun. 2023. "Silent Compiler Bug De-Duplication via Three-Dimensional Analysis." In *Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3597926.3598087][research_yang_2023_b]
- Yang, Wenzhang, Cuifeng Gao, Xiaoyuan Liu, Yuekang Li, and Yinxing Xue. 2024b. "Rust-Twins: Automatic Rust Compiler Testing through Program Mutation and Dual Macros Generation." In *Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering*. ACM. [https://doi.org/10.1145/3691620.3695059][research_yang_2024_b]
- Yang, Xin, Raula Gaikovina Kula, Norihiro Yoshida, and Hajimu Iida. 2016. "Mining the Modern Code Review Repositories: A Dataset of People, Process and Product." In *Proceedings of the 13th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/2901739.2903504][research_yang_2016]
- Yarom, Yuval. 2022. "Automating Cryptographic Code Generation." In *Proceedings of the 2022 Workshop on Attacks and Solutions in Hardware Security*. ACM. [https://doi.org/10.1145/3560834.3564147][research_yarom_2022]
- Yedida, Rahul, and Tim Menzies. 2022. "How to Improve Deep Learning for Software Analytics: (A Case Study with Code Smell Detection)." In *Proceedings of the 19th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3524842.3528458][research_yedida_2022]
- Yu, Liguo. 2016. "From Android Bug Reports to Android Bug Handling Process: An Empirical Study of Open-Source Development." *International Journal of Open Source Software and Processes* 7 (4): 1–18. [https://doi.org/10.4018/ijossp.2016100101][research_yu_2016]
- Yu, Jintao, Tom Hogervorst, and Razvan Nane. 2017. "A Domain-Specific Language and Compiler for Computation-in-Memory Skeletons." In *Proceedings of the Great Lakes Symposium on VLSI 2017*. ACM. [https://doi.org/10.1145/3060403.3060474][research_yu_2017]
- Yubin, Qu, Wong W. Eric, and Li Dongcheng. 2022. "Empirical Research for Self-Admitted Technical Debt Detection in Blockchain Software Projects." *International Journal of Performability Engineering* 18 (3): 149. [https://doi.org/10.23940/ijpe.22.03.p1.149157][research_yubin_2022]
- Zacchiroli, Stefano. 2022. "A Large-Scale Dataset of (Open Source) License Text Variants." In *Proceedings of the 19th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3524842.3528491][research_zacchiroli_2022]
- Zakrani, Abdelali, Mustapha Hain, Abdelwahed Namir, and Faculte des Sciences Ben M’sik. 2018. "Software Development Effort Estimation Using Random Forests: An Empirical Study and Evaluation." *International Journal of Intelligent Engineering and Systems* 11 (6): 300–311. [https://doi.org/10.22266/ijies2018.1231.30][research_anon_2018]
- Zeng, Junwei, Yixuan Tang, Jingxuan Zhang, Weiwei Li, and Zhiqiu Huang. 2024. "Detecting Optimizing Compiler Bugs via History-Driven Test Program Mutation." In *Proceedings of the 15th Asia-Pacific Symposium on Internetware*. ACM. [https://doi.org/10.1145/3671016.3671387][research_zeng_2024]
- Zeng, Dewen, Wenlong Tian, Haozhao Wang, Jianfeng Lu, Weijun Xiao, and Zhiyong Xu. 2026. "Ripple Shapley: Data Influence Attribution in One Federated Training Run." *Proceedings of the AAAI Conference on Artificial Intelligence* 40 (33): 28085–93. [https://doi.org/10.1609/aaai.v40i33.40034][research_zeng_2026]
- Zhang, Yixuan, Shangtong Cao, Haoyu Wang, et al. 2023a. "Characterizing and Detecting WebAssembly Runtime Bugs." *ACM Transactions on Software Engineering and Methodology* 33 (2): 1–29. [https://doi.org/10.1145/3624743][research_zhang_2023_b]
- Zhang, Kai, Shigang Li, and Xueying Wang. 2026c. "Compiler-ASR: Bridging the IR-to-Assembly Gap for Compiler Optimization via Architecture-Specific Reward." In *Proceedings of the 40th ACM International Conference on Supercomputing - Workshops*. ACM. [https://doi.org/10.1145/3774895.3812196][research_zhang_2026]
- Zhang, Junwei, Zhongxin Liu, Lingfeng Bao, Zhenchang Xing, Xing Hu, and Xin Xia. 2024b. "Inside Bug Report Templates: An Empirical Study on Bug Report Templates in Open-Source Software." In *Proceedings of the 15th Asia-Pacific Symposium on Internetware*. ACM. [https://doi.org/10.1145/3671016.3671401][research_zhang_2024]
- Zhang, Guangyi, Qiyu Liu, and Aristides Gionis. 2025e. "Shapley-Based Data Valuation for Weighted \$k\$-Nearest Neighbors." In *Advances in Neural Information Processing Systems 38*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/085713-1615][research_zhang_2025_d]
- Zhang, Yue, Melih Sirlanci, Ruoyu Wang, and Zhiqiang Lin. 2024c. "When Compiler Optimizations Meet Symbolic Execution: An Empirical Study." In *Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security*. ACM. [https://doi.org/10.1145/3658644.3670372][research_zhang_2024_b]
- Zhang, Guangyi, Yanhao Wang, Chengliang Chai, Qiyu Liu, and Wei Wang. 2025d. "Localized Data Shapley: Accelerating Valuation for Nearest Neighbor Algorithms." In *Advances in Neural Information Processing Systems 38*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/085713-1276][research_zhang_2025_c]
- Zhao, Wenxuan, Ruiying Zeng, and Yangfan Zhou. 2024b. "Wapplique: Testing WebAssembly Runtime via Execution Context-Aware Bytecode Mutation." In *Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis*. ACM. [https://doi.org/10.1145/3650212.3680340][research_zhao_2024]
- Zhao, Yu, Feng Zhang, Emad Shihab, Ying Zou, and Ahmed E. Hassan. 2016. "How Are Discussions Associated with Bug Reworking?: An Empirical Study on Open Source Projects." In *Proceedings of the 10th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement*. ACM. [https://doi.org/10.1145/2961111.2962591][research_zhao_2016]
- Zhao, Qi, and Chunling Zhong. 2023. "Cooperative Game Amongst Prefabricated Building Chain Stakeholders Based on Improved Shapley Value Method." *International Journal of Computer Applications in Technology* 71 (1): 33. [https://doi.org/10.1504/ijcat.2023.131064][research_zhao_2023_b]
- Zhong, Hao. 2022. "Enriching Compiler Testing with Real Program from Bug Report." In *Proceedings of the 37th IEEE/ACM International Conference on Automated Software Engineering*. ACM. [https://doi.org/10.1145/3551349.3556894][research_zhong_2022]
- Zhong, Ming, Fang Lv, Lulin Wang, et al. 2025. "VEGA: Automatically Generating Compiler Backends Using a Pre-Trained Transformer Model." In *Proceedings of the 23rd ACM/IEEE International Symposium on Code Generation and Optimization*. ACM. [https://doi.org/10.1145/3696443.3708931][research_zhong_2025]
- Zhou, Hao, and Jingling Xue. 2016. "A Compiler Approach for Exploiting Partial SIMD Parallelism." *ACM Transactions on Architecture and Code Optimization* 13 (1): 1–26. [https://doi.org/10.1145/2886101][research_zhou_2016]
- Zhu, Meina. 2025. "Large Language Models for Computer Programming Education: A Systematic Review of Empirical Study." In *AERA 2025*. AERA. [https://doi.org/10.3102/ip.25.2182044][research_zhu_2025_b]
- Zhu, Hong, Patrick A. V. Hall, and John H. R. May. 1997. "Software Unit Test Coverage and Adequacy." *ACM Computing Surveys* 29 (4): 366–427. [https://doi.org/10.1145/267580.267590][research_zhu_1997]
- Zhuykov, R., and E. Sharygin. 2017. "Ahead-of-Time Compilation of JavaScript Programs." *Programming and Computer Software* 43 (1): 51–59. [https://doi.org/10.1134/s036176881701008x][research_zhuykov_2017]
- Zia, Masooma. 2026. "Performance Evaluation of the Uetrv-Pcore Using RISC-V Microbenchmarks: Impact of Compiler Optimizations on a Five-Stage RISC-V Pipeline." *International Journal of Engineering Applied Sciences and Technology* 10 (10): 01–06. [https://doi.org/10.33564/ijeast.2026.v10i10.001][research_zia_2026]
- Zimmerle, Carlos, Kiev Gama, Fernando Castor, and José Murilo Mota Filho. 2022. "Mining the Usage of Reactive Programming APIs: A Study on GitHub and Stack Overflow." In *Proceedings of the 19th International Conference on Mining Software Repositories*. ACM. [https://doi.org/10.1145/3524842.3527966][research_zimmerle_2022]
- Zou, Xiaofeng, Yuanxi Peng, and Qing Zhang. 2023. "Design and Implementation of a Compiler Supporting RISC-V Custom Cryptographic and Vector Instructions." In *Proceedings of the 7th International Conference on Computer Science and Application Engineering*. ACM. [https://doi.org/10.1145/3627915.3628090][research_zou_2023]
- Телегин, В.А. 2023. "AHEAD-OF-TIME and JUST-IN-TIME technologies." *Vestnik of Russian New University. Series «Complex systems: models, analysis, management»*, no. 4: 171–75. [https://doi.org/10.18137/rnu.v9187.23.04.p.171][research_anon_2023_c]
- 徐, 明毅. 2019. "Research on Instruction Set Architecture of 40-Bit Processor." *Computer Science and Application* 09 (09): 1667–82. [https://doi.org/10.12677/csa.2019.99186][research_anon_2019]

### Secondary Sources

- Sohl, Joar. 2015. *Efficient Compilation for Application Specific Instruction Set DSP Processors with Multi-Bank Memories*. Linköping University Electronic Press. [https://doi.org/10.3384/diss.diva-113702][research_sohl_2015]

### Tertiary Sources

- Mosel, Ulrike. 2018. "Corpus Compilation and Exploitation in Language Documentation Projects." In *The Oxford Handbook of Endangered Languages*, edited by Kenneth L. Rehg, Lyle Campbell. Oxford University Press. [https://doi.org/10.1093/oxfordhb/9780190610029.013.14][research_mosel_2018]

### Related Posts

- Sechter, Brendan. 2026. "The Stream Processor as Compiler and the Compiler as Stream Processor." *Brendan A R Sechter's Development Blog*, April 17. [https://sgeos.github.io/compilers/streaming/series/2026/04/17/stream\_processor\_as\_compiler\_and\_compiler\_as\_stream\_processor.html][related_post_compilers_streaming]
- Sechter, Brendan. 2026. "The Self-Hosted Silicon Compiler." *Brendan A R Sechter's Development Blog*, July 10. [https://sgeos.github.io/hdl/hardware/self-hosting/2026/07/10/self\_hosted\_silicon\_compiler.html][related_post_self_hosted_silicon]
- Sechter, Brendan. 2026. "Getting Started with Keleusma 0.2.2." *Brendan A R Sechter's Development Blog*, July 11. [https://sgeos.github.io/rust/embedded/programming/2026/07/11/keleusma\_0\_2\_2\_getting\_started.html][related_post_keleusma_022]
- Sechter, Brendan. 2026. "Keleusma's Self-Hosting Strategy." *Brendan A R Sechter's Development Blog*, July 12. [https://sgeos.github.io/compilers/self-hosting/keleusma/2026/07/12/keleusma\_self\_hosting\_strategy.html][related_post_keleusma_self_hosting]
- Sechter, Brendan. 2026. "Keleusma Research Spike: What a Verified Bound Says About the Code That Actually Runs." *Brendan A R Sechter's Development Blog*, August 8. [https://sgeos.github.io/engineering/compilers/verification/2026/08/08/do\_proven\_bounds\_survive\_compilation.html][related_post_a371]
- Sechter, Brendan. 2026. "Keleusma Research Spike: What It Costs to Compile a Data Structure Whose Shape Is Already Decided." *Brendan A R Sechter's Development Blog*, August 9. [https://sgeos.github.io/engineering/compilers/verification/2026/08/09/cost\_of\_compiling\_aggregates.html][related_post_a372]

[ref_jvm_spec]: https://docs.oracle.com/javase/specs/jvms/se21/html/index.html
[ref_llvm_langref]: https://llvm.org/docs/LangRef.html
[related_post_a371]: {% post_url 2026-08-08-do_proven_bounds_survive_compilation %}
[related_post_a372]: {% post_url 2026-08-09-cost_of_compiling_aggregates %}
[related_post_compilers_streaming]: {% post_url 2026-04-17-stream_processor_as_compiler_and_compiler_as_stream_processor %}
[related_post_keleusma_022]: {% post_url 2026-07-11-keleusma_0_2_2_getting_started %}
[related_post_keleusma_self_hosting]: {% post_url 2026-07-12-keleusma_self_hosting_strategy %}
[related_post_self_hosted_silicon]: {% post_url 2026-07-10-self_hosted_silicon_compiler %}
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
[research_allamanis_sutton_2013]: https://doi.org/10.1109/msr.2013.6624029
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
[research_andrews_2005]: https://doi.org/10.1109/icse.2005.1553583
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
[research_basili_weiss_1984]: https://doi.org/10.1109/tse.1984.5010301
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
[research_conforti_cornuejols_1984]: https://doi.org/10.1016/0166-218x(84)90003-9
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
[research_demillo_1978]: https://doi.org/10.1109/c-m.1978.218136
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
[research_dyer_2013]: https://doi.org/10.1109/icse.2013.6606588
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
[research_ferdinand_wilhelm_1999]: https://doi.org/10.1023/a:1008186323068
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
[research_jensen_1906]: https://doi.org/10.1007/bf02418571
[research_jensen_2022]: https://doi.org/10.5220/0010838700003116
[research_jesus_2024]: https://doi.org/10.1145/3673038.3673104
[research_jeyaram_2025]: https://doi.org/10.1504/ijpqm.2025.150888
[research_jha_2023]: https://doi.org/10.1109/icst57152.2023.00057
[research_ji_2025]: https://doi.org/10.1145/3728938
[research_jia_harman_2011]: https://doi.org/10.1109/tse.2010.62
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
[research_khuller_1999]: https://doi.org/10.1016/s0020-0190(99)00031-9
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
[research_lattner_adve_2004]: https://doi.org/10.1109/cgo.2004.1281665
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
[research_leroy_2003]: https://doi.org/10.1023/a:1025055424017
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
[research_nemhauser_1978]: https://doi.org/10.1007/bf01588971
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
[research_pnueli_1998]: https://doi.org/10.1007/bfb0054170
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
[research_puschner_burns_2000]: https://doi.org/10.1023/a:1008119029962
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
[research_rice_1953]: https://doi.org/10.1090/s0002-9947-1953-0053041-6
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
