---
layout: post
mathjax: false
comments: true
title: "Long-Form Writing in the Age of Large Language Models"
date: 2026-02-25 09:10:40 +0000
categories: ai philosophy
---

<!-- A94 -->

Large Language Models can generate text at a pace
and volume that no individual human writer can match.
The tools that make writing easiest
also make writing most disposable.
A prompt entered into an LLM chat session
produces a response in seconds,
and that response is consumed and forgotten
just as quickly.
The session itself is ephemeral.
It exists in a transient context window,
and when the window closes,
the exchange leaves no durable trace on the open web.

This article argues that long-form writing
is more valuable in the LLM era than it has ever been.
The argument rests on two claims.
First, long-form posts are durable assets
that anchor the "Permanent Web"
and provide stable reference points
for both human readers and machine retrieval systems.
Unlike transient chat sessions and social media streams,
a published blog post has a URL,
a title, a date, section headings, and internal structure.
It is addressable, crawlable, and archivable.
Second, human-authored long-form content
is the high-fidelity ore required
to sustain the next generation of LLMs
and prevent the phenomenon known as
[model collapse][ref_model_collapse].
When models are trained on the outputs of other models,
they lose variance, shed nuance,
and converge on a narrow and repetitive distribution.
Human-authored structured prose
is the corrective that keeps the training pipeline viable.

These two claims are not speculative predictions.
They are inductive conclusions
drawn from the entire recorded history
of information technology.
The sections that follow trace that history
from biological memory through cuneiform tablets,
from the printing press through the search engine,
and from the search engine through the Large Language Model.
At no point in this 5,000-year record
has structured written information become less valuable
as information volume increased.
The pattern is the opposite.
Each information explosion
has increased the premium
on high-quality, structured, durable writing.
The LLM era is the latest instance of this pattern,
not an exception to it.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-25 09:10:40 +0000
```

## A Brief History of Information Storage

The history of information technology
is a history of three interrelated problems
that every civilization must solve.
The first is storage.
How does a society record information
so that it persists beyond the moment of creation?
The second is volume.
How does a society manage
the ever-increasing quantity of stored information?
The third is retrieval.
How does a society find specific information
within the accumulated store?

Every major advancement in information technology
represents a step-change in one or more of these three dimensions.
The progression from oral tradition to cuneiform,
from manuscripts to printed books,
from card catalogs to search engines,
and from search engines to Large Language Models
is a single continuous thread.
Long-form writing has been at the center
of this thread for its entire length.

### Pre-History and Biological Memory

Before writing, the only storage medium available
to human societies was biological memory.
[Walter J. Ong][book_orality_literacy]
documented the cognitive world of primary oral cultures
in *Orality and Literacy* (1982).
In these cultures,
all knowledge resided in the memories of living people.
When an elder died,
the knowledge that person carried died as well
unless it had been successfully transmitted
to another living person through speech.

Biological memory is lossy, sequential,
and offers no random access.
A person cannot "look up" an arbitrary fact
in memory the way a reader looks up a passage in a book.
Instead, oral cultures developed mnemonic devices
to compress and stabilize knowledge.
The formulaic epithets of Homeric epic poetry,
such as "rosy-fingered dawn" and "wine-dark sea,"
are not merely literary flourishes.
They are compression algorithms.
They provide fixed phrases
that anchor a reciter's memory
and reduce the cognitive burden of reproducing
long narratives from memory.

The fundamental limitation of biological memory
is that it cannot scale beyond the capacity
of living individuals and the bandwidth
of face-to-face communication.
A society that relies on oral tradition
can accumulate knowledge only as fast
as it can train new human carriers.
Knowledge volume is bounded
by the number of trained individuals,
and retrieval latency is bounded
by the time it takes to find and consult
the right person.

### Early Writing and the First Database

Writing was not invented for poetry.
It was invented for accounting.
[Denise Schmandt-Besserat][book_before_writing]
demonstrated in *Before Writing* (1992)
that the earliest precursors to
[cuneiform][ref_cuneiform] script
were clay tokens used in Mesopotamia
as early as 8000 BCE
to represent quantities of grain, oil, and livestock.
By approximately 3400 BCE,
the city of Uruk had developed cuneiform tablets
as a means of recording transactions
on a persistent medium.

The agricultural revolution created
an information technology problem
that biological memory could not solve.
When a society produces surplus grain,
it must track who produced how much,
who stored what, and who owes what to whom.
The first "database" was a grain ledger.
Writing arose to serve the infrastructure
of agricultural civilization
before it served any expressive or literary purpose.

The transition from oral memory to clay tablets
was a transition from sequential to random access.
An oral narrative must be traversed from beginning to end.
A collection of clay tablets can be consulted
in any order.
A scribe can pull a specific tablet
from a shelf without reading
every tablet that precedes it.
This shift from sequential to random access
is a recurring theme in the history
of information technology,
and it recurs in the transition from scrolls to codices,
from linear card catalogs to indexed databases,
and from keyword search to LLM-based retrieval.

### From Alphabet to Movable Type

The period between the agricultural revolution
and the invention of the printing press
spans roughly 4,800 years
and contains a series of innovations
in storage, encoding, retrieval, and computation
that collectively built the infrastructure
on which all subsequent information technology depends.
Mathematical and computational milestones
are interleaved here
because they represent parallel developments
in the mechanization of thought.

#### The Abacus

The [abacus][ref_abacus] appeared
in Mesopotamia around 2700 BCE
and subsequently spread to China, Rome,
and other civilizations.
It is the first dedicated computational device.
The abacus offloaded arithmetic
from biological memory to an external tool,
representing the earliest separation
of "storage" in the form of clay tablets
from "processing" in the form of the abacus.
This separation of storage and processing
is a fundamental architectural principle
that persists in every computing system built since.

#### The Alphabet

The [Phoenician alphabet][ref_phoenician_alphabet]
emerged around 1050 BCE
and reduced the symbol set
from hundreds of cuneiform signs
to approximately 22 consonants.
The [Greek alphabet][ref_phoenician_alphabet],
which appeared around 800 BCE,
added vowels and produced the first true alphabet
in which both consonants and vowels
are represented by distinct symbols.
This innovation lowered the barrier to literacy
by orders of magnitude.
A scribe no longer needed to memorize
hundreds of symbols to read and write.
The reduction in symbol count
is directly analogous to data compression.
A smaller encoding scheme
makes the same information
representable with less training
and lower error rates.

#### Euclid's Elements

[Euclid's *Elements*][ref_euclids_elements],
composed around 300 BCE,
is the first axiomatic system.
It organized geometric knowledge
into definitions, postulates, and propositions
derived by logical deduction.
Euclid demonstrated that complex knowledge
could be compressed into a small set of axioms
and deterministic inference rules,
and that the resulting system
could be transmitted faithfully
across centuries and languages
by anyone who could read the text
and follow the logical steps.

The *Elements* remained a standard textbook
for over two thousand years.
It is one of the most durable written documents
in human history
and an early proof that structured long-form writing
is the most reliable vessel
for transmitting formal reasoning across generations.

#### The Library of Alexandria and the Pinakes

The [Library of Alexandria][ref_library_of_alexandria],
founded around 295 BCE,
was the first attempt at comprehensive
information aggregation.
The [Pinakes][ref_pinakes],
compiled around 245 BCE by Callimachus,
organized the library's holdings by genre
and then alphabetically by author.
The Pinakes constituted the first systematic library catalog,
the first metadata-based retrieval system.
The Library of Alexandria is a precursor
to the "universal library" concept
that later manifests as the *Encyclopédie*,
the [Internet Archive][ref_internet_archive],
and Wikipedia.

#### The Antikythera Mechanism

The [Antikythera mechanism][ref_antikythera],
dating to approximately 100 BCE,
is a geared bronze instrument
recovered from a Greek shipwreck.
It computed the positions of the sun, moon, and planets
using mechanical gearing.
The Antikythera mechanism demonstrates
that the impulse to mechanize computation
predates the common era by at least two millennia.
It is the earliest known analog computer.

#### The Codex

The [codex][ref_codex],
which replaced the scroll
between the 1st and 4th centuries of the common era,
was a transition from sequential access to random access.
A scroll must be unrolled linearly to reach a given passage.
A codex can be opened to any page directly.
The codex doubled information density per unit of material
and is directly analogous to indexed file retrieval.
It was the first data structure
optimized for non-sequential lookup.

#### Paper

[Paper][ref_history_of_paper]
was developed by Cai Lun around 105 CE
and traveled westward to the Islamic world
via the Battle of Talas in 751 CE.
Paper reduced the cost of writing surfaces
by orders of magnitude compared to parchment.
By 1400, paper in Europe
cost approximately one-eighth
the price of parchment.
The cost reduction enabled
both Islamic manuscript culture
and the European print revolution.
Cheap writing surfaces
are a prerequisite for mass literacy,
and mass literacy is a prerequisite
for the information explosions that follow.

#### The House of Wisdom and Al-Khwarizmi

The [House of Wisdom][ref_house_of_wisdom] in Baghdad,
active from roughly the 8th through the 13th century,
preserved and translated Greek texts into Arabic.
[Muhammad ibn Musa al-Khwarizmi][ref_al_khwarizmi],
working in the House of Wisdom,
produced treatises that originated the words
"algorithm" and "algebra."
He formalized procedural problem-solving in written form,
demonstrating that writing down computational procedures
makes them transmissible and repeatable across centuries.
Ibn al-Nadim's *Fihrist* (987 CE)
indexed approximately 10,000 books,
the most comprehensive medieval bibliography.

Al-Khwarizmi's contribution is specifically relevant
to the thesis of this article.
An algorithm that exists only in one person's head
dies with that person.
An algorithm written down
and transmitted in structured long-form prose
persists for over a thousand years
and continues to shape the vocabulary
of every programmer alive today.

#### Astrolabes

[Astrolabes][ref_astrolabe],
developed around 150 BCE
and refined through medieval Islamic and European periods,
were analog computational instruments
for solving astronomical problems.
The astrolabe encoded complex spherical trigonometry
into a portable mechanical device,
serving as both reference tool and calculator.
Like the abacus,
the astrolabe offloaded computation from the human mind
to a physical instrument.
Unlike the abacus,
it required substantial written documentation
to use correctly,
reinforcing the dependence of computation on text.

#### Medieval Monasteries and Scriptoria

The [scriptoria][ref_scriptorium]
of medieval monasteries,
operating from roughly the 5th through the 12th century,
constituted an institutional copying pipeline
that preserved the classical corpus
through the European dark ages.
A lector dictated aloud
while scribes wrote in parallel.
Without this effort,
much of Aristotle, Ovid, and Pliny
would be permanently lost.

However, the scribal copying system
introduced systematic transmission errors.
Each copy drifted from the original.
Over generations of copying,
the accumulated errors compounded
and the transmitted text diverged
measurably from the author's original words.
This phenomenon is directly analogous
to [model collapse][ref_model_collapse]
in recursive AI training.
When each generation of output
is produced from the previous generation
rather than from an authoritative source,
variance is lost and errors accumulate.
The scriptoria demonstrate
that the problem of transmission fidelity
is not new to the LLM era.
It is as old as the act of copying text.

#### Fibonacci and Liber Abaci

[Fibonacci][ref_fibonacci]'s
*Liber Abaci* (1202)
introduced Hindu-Arabic numerals to Europe,
replacing Roman numeral computation
with a positional decimal system.
The treatise transformed European mathematics
and commerce.
It is another instance of long-form writing
serving as the vector for a paradigm shift.
The numerals themselves were not new.
They had been in use
in the Indian subcontinent and the Islamic world
for centuries.
What Fibonacci provided
was a comprehensive written explanation
in a European language
that made the system accessible
to European merchants and scholars.
The transmission medium was the written treatise.

#### East Asian Movable Type

Bi Sheng's ceramic [movable type][ref_movable_type]
appeared in China around 1040 CE,
and Korean metal movable type
produced the Jikji in 1377.
Both predated Gutenberg's press by centuries.
Gutenberg's contribution was not
the invention of movable type
but the first commercially viable, high-throughput
European system.
The distinction matters
because it illustrates a recurring pattern.
The invention of a technology
and its deployment at scale
are separate events,
and scale is what triggers information explosions.

### The First Information Explosion

Johannes Gutenberg's movable-type printing press,
operational by approximately 1440,
produced a step-change in storage and retrieval
that [Elizabeth Eisenstein][book_printing_press]
documented in *The Printing Press as an Agent of Change* (1979).
Before the press,
Europe contained tens of thousands of manuscripts.
By 1500, approximately eight million printed books
were in circulation.

The printing press solved
the transmission error problem
that had plagued the scribal copying system.
A printed book is identical to every other copy
produced from the same typeset.
Print enabled accumulation
rather than drift through scribal errors.
A reader in Florence and a reader in London
could consult the same text
and know that they were reading the same words.
This is the historical precedent
for the contemporary argument
that authoritative human-authored sources
serve as fixed reference points
in a landscape of synthetic variation.

The printing press also created
the first generation of metadata.
Tables of contents, indices, and page numbers
are printing-era inventions.
They made books randomly addressable.
A reader no longer needed to read a book linearly.
A reader could use an index to find specific topics.
This is the beginning of indexability,
the property that distinguishes
a durable reference document
from an ephemeral stream of text.

### The Early Modern Period

The printing press created an information surplus
that demanded new systems
for organization, transmission, and computation.
The period between the printing press
and the industrial revolution
is characterized by a series of innovations
that responded to this surplus.

#### Double-Entry Bookkeeping

[Double-entry bookkeeping][ref_double_entry_bookkeeping],
codified by Luca Pacioli
in [*Summa de Arithmetica*][book_summa_de_arithmetica] (1494),
standardized the ledger system
that had emerged in Italian city-states.
Like Sumerian grain accounting millennia earlier,
writing served commerce before it served literature.
Pacioli's treatise made the system
transmissible across languages and centuries.
A direct line runs from Sumerian grain ledgers
through Pacioli's printed treatise
to the standardized financial reporting
of the modern corporation.
At each step, the durability of the written record
was the mechanism of transmission.

#### Bibliotheca Universalis

Conrad Gessner's
[*Bibliotheca Universalis*][ref_bibliotheca_universalis] (1545)
was the first attempt at a universal bibliography
of printed works,
cataloging approximately 3,000 authors
and 10,000 titles.
It was an early recognition
that the print explosion required meta-information
to remain navigable.
The same principle applies today.
The web's information explosion
requires structured, well-titled, well-tagged
long-form documents
to remain navigable by both humans and machines.

#### Napier's Logarithms and Bones

John Napier published [logarithm][ref_logarithm] tables in 1614,
converting multiplication into addition
and dramatically accelerating computation.
His [Napier's Bones][ref_napiers_bones] (1617)
were a manual calculation aid
based on lattice multiplication.
Both represent the encoding of mathematical insight
into physical reference tools.
The logarithm table is a form of publication.
It encodes a mathematical relationship
in durable written form
so that anyone with access to the table
can perform calculations
that would otherwise require extensive mental effort.

#### The Slide Rule

The [slide rule][ref_slide_rule],
developed by William Oughtred around 1622,
is a portable analog computer based on Napier's logarithms.
It remained the primary computational tool
for engineers and scientists
for over three hundred years,
until the electronic calculator displaced it in the 1970s.
The slide rule's longevity
demonstrates that a physical tool
grounded in a well-documented mathematical principle
can outlast centuries of technological change.

#### Pascal's Pascaline

The [Pascaline][ref_pascaline],
built by Blaise Pascal in 1642,
was the first mechanical calculator
capable of addition and subtraction.
Pascal built it to assist his father's tax calculations.
A direct line runs from Sumerian grain ledgers
through Pacioli's bookkeeping
to Pascal's machine.
Writing created the accounting problem,
and computation arose to solve it.

#### Scientific Journals

The [*Journal des sçavans*][ref_journal_des_scavans] in Paris
and the
[*Philosophical Transactions of the Royal Society*][ref_philosophical_transactions]
in London both launched in 1665.
They formalized the long-form scientific paper
as the unit of knowledge transmission.
Peer review, citation,
and structured argumentation became the standard.
The scientific journal is the direct ancestor
of the modern research paper and the blog post.
Both forms share the same structural properties.
They have titles, authors, dates,
section headings, and reference lists.
These properties make them indexable, citeable,
and retrievable in ways
that conversational text is not.

#### Leibniz's Stepped Reckoner and Binary Arithmetic

Gottfried Wilhelm Leibniz built the
[stepped reckoner][ref_stepped_reckoner] in 1694,
a mechanical calculator
for all four arithmetic operations.
Leibniz also independently described the
[binary number][ref_binary_number] system.
His work on binary arithmetic
would not find practical application
for 250 years,
until electronic computers adopted it.
The gap between theoretical publication
and practical application
is itself an argument
for the durability of long-form writing.
Leibniz's binary treatise persisted in written form
long enough for engineers
in the 20th century to discover and implement it.

#### The Statute of Anne

The [Statute of Anne][ref_copyright_statute_anne] (1710)
was the first copyright law,
establishing authors' rights
over their printed works.
It created a legal framework
for durable written content as property.
Copyright is relevant to the contemporary thesis
because the legal status
of AI-generated text
and the copyrightability of training data
are active areas of legal dispute.
The Statute of Anne established the principle
that written works have economic value
tied to their authorship,
a principle that gains new salience
when machines can generate text
that mimics human authorship.

#### Newspapers and Periodicals

Newspapers, which proliferated
in the 17th and 18th centuries,
were mass-produced ephemeral print.
Unlike books, newspapers were designed
to be disposable.
A newspaper reports events of the day
and is replaced the next day
by a new edition.
This is the first large-scale instance
of the durability-ephemerality spectrum
that dominates the contemporary web.
Books persist. Newspapers do not.
Blog posts persist. Chat sessions do not.
The parallel is exact.

#### The Encyclopédie

The [*Encyclopédie*][ref_encyclopedie],
edited by Denis Diderot and Jean le Rond d'Alembert
and published between 1751 and 1772,
comprised 28 volumes
attempting to compile all human knowledge.
It was the largest collaborative writing project
of its era.
The *Encyclopédie* demonstrated
that long-form structured writing
could organize an entire civilization's knowledge
into a navigable, cross-referenced whole.
It is a direct ancestor of Wikipedia
and an antecedent of the comprehensive reference index.

#### Bayes' Theorem

[Bayes' theorem][ref_bayes_theorem],
developed by Thomas Bayes
and published posthumously in 1763,
provides the mathematical foundation
for updating beliefs given new evidence.
Bayes' theorem is relevant
to the thesis of this article
because LLM training
is fundamentally Bayesian in nature.
Models learn probability distributions from observed text.
The quality of the posterior distribution
depends on the quality of the prior observations.
If the prior observations are low-quality
or recursively generated synthetic text,
the posterior distribution degrades.
This is the mathematical core
of the model collapse problem.

#### The Chappe Optical Telegraph

The [Chappe optical telegraph][ref_chappe_telegraph] (1794)
was the first high-speed long-distance communication system,
using semaphore towers across France.
Transmission speed vastly exceeded the postal system,
but capacity was extremely limited.
Each message had to be short and encoded.
The telegraph is a precursor
to the bandwidth-latency tradeoffs of digital networks
and an early demonstration
that high-speed transmission
does not eliminate the need for durable storage.
A telegraph message is consumed and forgotten.
A book endures.

### The Industrial Revolution and Standardized Retrieval

The industrial revolution
produced a dramatic increase
in both literacy and bureaucratic record-keeping.
The "Bureaucratic Explosion"
generated volumes of written documentation
that exceeded any previous era's output.

#### Boolean Algebra

George Boole's
[*The Laws of Thought*][book_laws_of_thought] (1854)
reduced logical reasoning
to algebraic operations on true/false values.
Boolean algebra provided the mathematical foundation
for digital logic circuits
and, eventually, for search engine queries
and database operations.
Every database query
and every LLM attention mask
operates on Boolean foundations.
Boole's contribution, like Leibniz's binary arithmetic,
was published as long-form structured prose
and found practical application decades later.

#### The Dewey Decimal System and Public Libraries

The [Dewey Decimal Classification][ref_dewey_decimal] (1876)
was the first systematic metadata-based
retrieval system for libraries.
It assigned numeric codes to subjects,
enabling readers to locate books
without browsing the entire collection.
[Carnegie libraries][ref_carnegie_library]
democratized access to accumulated written knowledge
by funding public libraries across the United States
and the United Kingdom.

The Dewey Decimal system is significant
because it recognized and solved
the information volume problem at industrial scale.
When the number of books in a library
exceeded what any individual could browse,
the solution was not to reduce the number of books.
The solution was to build a better retrieval system.
This principle recurs at every subsequent scale.
The response to information volume
is always better indexing, never less writing.

### The Mechanization of Thought

The 19th and early 20th centuries
saw the convergence of mathematics and machinery.
These developments bridge the analog and digital eras
and explain why long-form writing
became the prerequisite for computation itself.

#### The Jacquard Loom

The [Jacquard loom][ref_jacquard_loom],
built by Joseph Marie Jacquard in 1804,
used punched cards to control weaving patterns.
It was the first instance
of encoding instructions
in a machine-readable format
separate from the machine itself.
The Jacquard loom directly inspired
[Charles Babbage][ref_babbage]'s
subsequent work on programmable computation.
Punched cards would remain
the dominant input medium
for computing systems for nearly two centuries.

#### Babbage's Analytical Engine and Ada Lovelace's Notes

Charles Babbage designed the
[Analytical Engine][ref_analytical_engine]
between 1837 and 1871
as the first general-purpose mechanical computer.
[Ada Lovelace][ref_lovelace]'s 1843 notes
on the Analytical Engine
constitute the first published computer program
and the first philosophical argument
that a machine could manipulate symbols
beyond pure number.

Lovelace's contribution was transmitted in writing,
in long-form structured prose.
Without the written record,
the concept of general-purpose computation
might have been lost for decades.
Babbage's machine was never completed in his lifetime.
What survived was the documentation.
The written description of the Analytical Engine
and Lovelace's commentary on it
persisted long enough
to influence the 20th-century pioneers
who built the first electronic computers.
This is a concrete historical example
of long-form writing
outlasting the physical technology it describes.

#### Lord Kelvin's Tide-Predicting Machines

Lord Kelvin's
[tide-predicting machines][ref_tide_predicting_machine] (1872)
were mechanical analog computers
that summed harmonic components
to predict tidal patterns.
They demonstrated that complex natural phenomena
could be modeled by mechanical computation,
provided the mathematical relationships
were first expressed in written form
and then encoded in gearing.

#### Hollerith's Punch Card Tabulator

[Herman Hollerith][ref_hollerith]'s
[punch card][ref_punched_card] tabulator (1890)
used punched cards to process the U.S. Census.
The Hollerith system reduced
the processing time for census data
from approximately eight years to one year.
Hollerith's company eventually became IBM.
Punched cards remained
the dominant data entry medium
for nearly a century.

#### Gödel's Incompleteness Theorems

[Gödel's incompleteness theorems][ref_godels_incompleteness] (1931)
proved that any sufficiently powerful formal system
contains true statements
that cannot be proved within the system.
The theorems established fundamental limits
on what formal reasoning can achieve.
They are relevant to the thesis of this article
because they demonstrated
that human mathematical insight
cannot be fully mechanized.
There will always be truths
that require human judgment to identify,
truths that cannot be derived
by any purely mechanical process.
This finding provides a theoretical basis
for the claim that human-authored content
is not merely currently useful
but permanently necessary.

#### Vannevar Bush's Differential Analyzer and "As We May Think"

Vannevar Bush built the
[differential analyzer][ref_differential_analyzer] in 1931,
one of the most powerful analog computers
of the pre-digital era.
He then wrote the essay
"[As We May Think][research_bush]" (1945),
published in *The Atlantic*,
which anticipated hypertext, information overload,
and the need for machine-assisted retrieval.
Bush proposed the "memex,"
a desk-sized device
that would allow a user
to store, retrieve, and annotate
a personal library of microfilmed documents.

Bush's essay is itself a canonical example
of long-form writing
that shaped the trajectory of technology.
The differential analyzer is a museum piece.
The essay remains in print,
accessible on the web,
and cited in virtually every history
of computing and information science.
The written document outlasted the machine.

#### Turing's Universal Machine

Alan Turing's 1936 paper
"[On Computable Numbers][research_turing]"
proved that a single machine
could simulate any other computational machine
given the right instructions.
The [Turing machine][ref_turing_machine]
is the theoretical foundation
for all programmable computers.
Turing's proof was published
as a mathematical paper
and transmitted to subsequent generations
in written form.

#### Shannon's Information Theory

Claude Shannon's 1948 paper
"[A Mathematical Theory of Communication][research_shannon]"
quantified information in bits
and established the theoretical limits
of data compression and transmission.
Every digital storage and communication system
operates within Shannon's framework.
Shannon published his work
as a long-form technical paper at Bell Labs.
Like Euclid's *Elements*,
like Al-Khwarizmi's treatises,
like Turing's proof,
Shannon's paper demonstrates
that the formal systems
underlying all of computation
were invented in writing
and disseminated through structured prose.

### Analog to Digital and Fragile Density

The transition from analog to digital storage
introduced a fundamental asymmetry.
A clay tablet survives millennia of neglect.
A magnetic tape becomes unreadable in decades.
Digital storage offers density
that analog media cannot match,
but at the cost of fragility.

The IBM 350 hard disk (1956)
could store five million characters.
A modern solid-state drive
stores trillions of characters.
But the clay tablets of Uruk,
inscribed five thousand years ago,
are still legible today.
No digital storage medium
manufactured in the 20th century
can make that claim.

Digital preservation faces three challenges.
Format obsolescence renders data unreadable
when the software that interprets it
is no longer maintained.
Hardware obsolescence renders data inaccessible
when the physical devices
that read a given medium are no longer produced.
Bit rot degrades data at the physical level
as magnetic domains decay
and electrical charges dissipate.

Stewart Brand articulated the paradox
of [information economics in 1984][research_brand].
Information wants to be expensive
because it is so valuable.
The right information at the right time
changes the course of events.
Information also wants to be free
because the cost of disseminating it
keeps falling.
The tension between these two impulses
defines the economics of digital content.
Long-form writing is expensive to produce
and cheap to disseminate.
Chat transcripts are cheap to produce
and cheap to disseminate.
The difference in production cost
corresponds to a difference in value.

### The Contemporary Era and Data Exhaust

The contemporary web produces
more text per day
than all prior human civilizations
produced in their entire histories combined.
Most of this text is ephemeral.
Social media posts, chat messages, and comment threads
are produced and consumed in minutes.
They exist behind authentication walls,
they are subject to platform moderation decisions,
they are algorithmically surfaced and buried,
and they are not reliably archived.

The statistics on
[link rot][ref_link_rot] are striking.
A 2024 [Pew Research Center study][research_pew_link_rot]
found that 25 percent of web pages
that existed between 2013 and 2023
were no longer accessible by October 2023.
A 2024 [Ahrefs study][research_link_rot_ahrefs]
found that 66.5 percent of links
were dead within nine years.
The "Permanent Web"
is not merely about files existing.
It is about files remaining addressable.

Tim Berners-Lee argued
in "[Cool URIs Don't Change][ref_cool_uris]" (1998)
that a URL should remain valid indefinitely.
Brewster Kahle argued
in "[Locking the Web Open][research_kahle]" (2015)
that the average life of a web page
is approximately one hundred days.
The gap between Berners-Lee's ideal
and Kahle's observation
defines the challenge
that long-form writing must address.

Social media platforms are walled gardens.
Content posted to a walled garden
is locked behind authentication,
subject to the platform's terms of service,
and dependent on the platform's continued operation.
When a platform changes its policies,
restricts its API, or shuts down entirely,
the content disappears.
Personal blogs and static sites are different.
They are hosted on open infrastructure,
addressable by stable URLs,
crawlable by search engines and archival services,
and independent of any single platform's decisions.

The [Internet Archive][ref_internet_archive]
serves as the modern Library of Alexandria.
It crawls and archives the open web.
But it can only archive content
that is publicly addressable.
A post on a social media platform
behind an authentication wall
is invisible to the Internet Archive.
A blog post on a static site
with a stable URL is preserved.

## Search Versus Synthesis

The history of information retrieval
can be divided into two eras.
In the first era,
the fundamental problem was finding information.
In the second era,
the fundamental problem is generating knowledge
from information already found.

The first era began
with manual indices and directories.
The Yahoo directory of the early 1990s
organized the web into human-curated categories.
[PageRank][ref_pagerank],
described by Sergey Brin and Larry Page
in their [1998 paper][ref_pagerank],
automated the process
by ranking pages based on link structure.
Search engines enabled users
to find specific web pages
using keyword queries.
The unit of retrieval was the page.
The input was a set of keywords.
The output was a ranked list of pages.

The second era is the LLM era.
The fundamental problem is no longer
finding a page that contains information.
The fundamental problem is synthesizing
a coherent response from a vast body of knowledge.
The input is a natural-language query
that may be ambiguous, underspecified,
or requiring contextual understanding.
The output is a generated response
that draws on patterns learned during training.

The transition from search to synthesis
changes the requirements
for the information that feeds the system.
In the search era, the system needed keywords.
In the synthesis era, the system needs context.
Long-form writing provides context
that a 280-character post
or a "Hey, how do I do X?" chat prompt lacks.
A blog post with a title, a date,
section headings, and internal hierarchies
is inherently "higher metadata"
than a chat log or tweet.
It provides structured context
that an LLM can learn from
more effectively than unstructured conversational text.

The Pinakes of the Library of Alexandria,
the Dewey Decimal Classification,
PageRank, and LLM training
are four instances of the same problem
at four different scales.
Each represents a society's attempt
to impose retrievable order
on a growing body of written knowledge.
At each scale, the solution depends on
the quality and structure
of the underlying written material.

## The Model Collapse Risk

[Model collapse][ref_model_collapse]
is the phenomenon
in which a Large Language Model,
trained on data that includes outputs
from other Large Language Models,
progressively loses the ability
to generate diverse and accurate text.
[Shumailov et al. (2024)][research_ai_models_collapse]
published the definitive study in *Nature*,
demonstrating that recursive training
on model-generated data
causes the output distribution to narrow.
Early collapse manifests
as the disappearance of tail-of-distribution data.
The model stops producing rare or unusual outputs.
Late collapse manifests
as a loss of variance.
The model's outputs become repetitive
and converge on a narrow set of patterns.

Jathan Sadowski coined the term "Habsburg AI" in 2023
to describe "a system so heavily trained
on the outputs of other generative AIs
that it becomes an inbred mutant,
with exaggerated features
and little ability to function."
The analogy to the Habsburg dynasty's
accumulation of genetic defects
through consanguineous marriage
captures the mechanism precisely.
Each generation of inbred output
narrows the gene pool of the training data.
Cory Doctorow described the same phenomenon
as the "[coprophagic AI crisis][research_doctorow]" in 2024,
a self-consuming cycle
in which models eat their own output
and lose the capacity for novelty.

The scale of the problem is quantifiable.
[Villalobos et al. (2024)][research_villalobos]
at Epoch AI projected
that high-quality language data
suitable for LLM training
will be effectively exhausted
in the near future.
The web is large,
but the subset of the web
that consists of high-quality,
well-structured, human-authored prose
is finite and growing
more slowly than the demand for training data.

The [FineWeb research][research_fineweb]
presented at NeurIPS 2024
demonstrated that the quality and register
of human-written text,
not merely its volume,
determines training outcomes.
Models trained on curated, high-quality text
outperform models trained on larger but noisier datasets.
This finding directly supports the thesis
that human-authored long-form content
is the "high-fidelity ore" in the training pipeline.

The historical parallel to model collapse
is the scribal copying system
of medieval scriptoria.
Each generation of copies
drifted further from the original.
The printing press solved this problem
by producing identical copies from a fixed master.
The contemporary equivalent
is the authoritative human-authored source.
A durable, addressable, long-form document
serves as a fixed reference point
against which synthetic outputs can be calibrated.

## The Library Paradox

Social media platforms
present themselves as public squares
where anyone can publish and be heard.
In practice, they are walled gardens.
Content posted to a social media platform
is locked behind authentication,
subject to the platform's content moderation policies,
algorithmically surfaced and buried,
and dependent on the platform's continued existence.
A user does not own the content
in any meaningful operational sense.
The platform can delete it,
suppress it, or make it inaccessible
at any time without appeal.

Personal blogs and static sites operate differently.
A blog post hosted on a static site
has a stable URL.
It is addressable by anyone with a web browser.
It is crawlable by search engines
and archival services.
It is independent of any single platform's decisions.
If the hosting provider changes,
the files can be migrated.
If the author chooses to preserve the content,
the content persists.

The paradox is this.
Social media platforms have audiences of billions
but produce content
that is structurally fragile.
Personal blogs have audiences of tens or hundreds
but produce content
that is structurally durable.
A blog post is a library book.
A tweet is a whisper in a crowd.
The library book can be found,
cataloged, archived, and referenced for decades.
The whisper is gone the moment it is uttered.

The Internet Archive
serves as the modern Library of Alexandria,
crawling and preserving the open web.
But like the original Library of Alexandria,
it is vulnerable.
It can only archive
what is publicly addressable on the open web.
Content behind walled gardens is invisible to it.
The more content migrates to walled gardens,
the less of the web is preserved.
Every blog post published on the open web
is a small contribution to the resilience
of the permanent record.

## Historical Conclusions

The history presented in the preceding sections
is not ornamental background.
It constitutes the epistemological basis for the thesis.
The following conclusions
are drawn inductively from the historical record.

### Writing Has Always Served Infrastructure Before Expression

Sumerian cuneiform recorded grain inventories,
not poetry.
Pacioli codified double-entry bookkeeping.
Scientific journals formalized knowledge transmission.
At every inflection point in the history
of information technology,
writing served the infrastructure of civilization
before it served individual expression.
Long-form blog posts in the LLM era
continue this pattern.
They are infrastructure
for the knowledge systems
that LLMs depend on.

### Every Information Explosion Has Required a Corresponding Retrieval Innovation

The printing press demanded tables of contents,
indices, and page numbers.
The industrial revolution
demanded the Dewey Decimal system
and public libraries.
The digital explosion demanded search engines.
The LLM era demands
high-quality human-authored training data.

Each explosion was resolved
not by reducing the volume of information
but by building better systems
to organize and retrieve it.
Long-form writing,
with its inherent structure
of titles, headings, and internal hierarchies,
is the most retrievable and indexable unit
of web content.

### Transmission Errors Accumulate Without Authoritative Sources

Scribal copying in medieval scriptoria
introduced systematic drift.
Each generation of copies
degraded further from the original.
This is precisely the mechanism of model collapse.
LLMs trained on synthetic data
lose variance and fidelity
with each recursive generation.

The historical solution was the printing press,
which eliminated scribal drift
by producing identical copies from a fixed master.
The contemporary equivalent
is the authoritative human-authored source.
A durable, addressable, long-form document
serves as a fixed reference point
against which synthetic outputs
can be calibrated.

### Computational Formalism Has Always Depended on Written Transmission

Euclid's axiomatic method,
Al-Khwarizmi's algorithms,
Lovelace's program notes,
Turing's proof,
and Shannon's theory
were all transmitted
as long-form written documents.
The formal systems that make computation possible
were invented in writing
and disseminated through structured prose.

LLMs are the latest in this lineage.
They are trained on text,
they produce text,
and they depend on the continued production
of high-fidelity text to avoid degradation.
The formal tools used to build LLMs
were themselves transmitted in long-form writing.
The training data that sustains LLMs
is long-form writing.
The thesis of this article is therefore
not an external claim about writing.
It is an observation about the recursive dependency
of the entire computational enterprise
on the written word.

## Conclusion

The history of information technology
is a history of writing becoming more,
not less, necessary as information volume grows.
This pattern holds from Sumerian grain ledgers
through the Library of Alexandria,
from the printing press through the search engine,
and from the search engine
through the Large Language Model.

Every long-form post published on the open web
is simultaneously a contribution to the permanent web
and a deposit in the training corpus
that sustains the next generation
of language models.
The dual function of long-form writing
as durable reference for humans
and as high-fidelity training data for machines
is not a coincidence.
It follows from the same structural properties.
Titles, dates, section headings,
internal hierarchies, and stable URLs
make a document both navigable by humans
and learnable by machines.

Writing long-form is not anachronistic.
It is infrastructural.
It has been infrastructural
for five thousand years.
The tools change.
The medium changes.
The underlying function of structured written prose
as the durable substrate of civilization's knowledge
does not change.

## Future Reading

- Ong, *Orality and Literacy* (1982)
- Eisenstein, *The Printing Press as an Agent of Change* (1979)
- Shumailov et al., "AI models collapse when trained on recursively generated data" (*Nature* 2024)
- Berners-Lee, "Cool URIs don't change" (1998)
- Bush, "As We May Think" (1945)
- Shannon, "A Mathematical Theory of Communication" (1948)
- Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936)
- Schmandt-Besserat, *Before Writing* (1992)
- Boole, *An Investigation of the Laws of Thought* (1854)
- Pacioli, *Summa de Arithmetica* (1494)

## References

- [Book, Before Writing][book_before_writing]
- [Book, Orality and Literacy][book_orality_literacy]
- [Book, Summa de Arithmetica][book_summa_de_arithmetica]
- [Book, The Laws of Thought][book_laws_of_thought]
- [Book, The Printing Press as an Agent of Change][book_printing_press]
- [Reference, Abacus][ref_abacus]
- [Reference, Analytical Engine][ref_analytical_engine]
- [Reference, Antikythera Mechanism][ref_antikythera]
- [Reference, Astrolabe][ref_astrolabe]
- [Reference, Bayes' Theorem][ref_bayes_theorem]
- [Reference, Bibliotheca Universalis][ref_bibliotheca_universalis]
- [Reference, Binary Number][ref_binary_number]
- [Reference, Carnegie Library][ref_carnegie_library]
- [Reference, Chappe Optical Telegraph][ref_chappe_telegraph]
- [Reference, Charles Babbage][ref_babbage]
- [Reference, Codex][ref_codex]
- [Reference, Cool URIs Don't Change][ref_cool_uris]
- [Reference, Cuneiform][ref_cuneiform]
- [Reference, Dewey Decimal Classification][ref_dewey_decimal]
- [Reference, Differential Analyzer][ref_differential_analyzer]
- [Reference, Double-entry Bookkeeping][ref_double_entry_bookkeeping]
- [Reference, Encyclopédie][ref_encyclopedie]
- [Reference, Euclid's Elements][ref_euclids_elements]
- [Reference, Fibonacci][ref_fibonacci]
- [Reference, Gödel's Incompleteness Theorems][ref_godels_incompleteness]
- [Reference, Herman Hollerith][ref_hollerith]
- [Reference, History of Paper][ref_history_of_paper]
- [Reference, House of Wisdom][ref_house_of_wisdom]
- [Reference, Internet Archive][ref_internet_archive]
- [Reference, Jacquard Loom][ref_jacquard_loom]
- [Reference, Journal des sçavans][ref_journal_des_scavans]
- [Reference, Library of Alexandria][ref_library_of_alexandria]
- [Reference, Link Rot][ref_link_rot]
- [Reference, Logarithm][ref_logarithm]
- [Reference, Ada Lovelace][ref_lovelace]
- [Reference, Model Collapse][ref_model_collapse]
- [Reference, Movable Type][ref_movable_type]
- [Reference, Muhammad ibn Musa al-Khwarizmi][ref_al_khwarizmi]
- [Reference, Napier's Bones][ref_napiers_bones]
- [Reference, PageRank][ref_pagerank]
- [Reference, Pascaline][ref_pascaline]
- [Reference, Philosophical Transactions of the Royal Society][ref_philosophical_transactions]
- [Reference, Phoenician Alphabet][ref_phoenician_alphabet]
- [Reference, Pinakes][ref_pinakes]
- [Reference, Punched Card][ref_punched_card]
- [Reference, Scriptorium][ref_scriptorium]
- [Reference, Slide Rule][ref_slide_rule]
- [Reference, Statute of Anne][ref_copyright_statute_anne]
- [Reference, Stepped Reckoner][ref_stepped_reckoner]
- [Reference, Tide-predicting Machine][ref_tide_predicting_machine]
- [Reference, Turing Machine][ref_turing_machine]
- [Research, AI Models Collapse When Trained on Recursively Generated Data][research_ai_models_collapse]
- [Research, A Mathematical Theory of Communication][research_shannon]
- [Research, As We May Think][research_bush]
- [Research, Coprophagic AI Crisis][research_doctorow]
- [Research, FineWeb Datasets for Large Language Models][research_fineweb]
- [Research, Link Rot Study][research_link_rot_ahrefs]
- [Research, Locking the Web Open][research_kahle]
- [Research, On Computable Numbers][research_turing]
- [Research, Stewart Brand on Information][research_brand]
- [Research, When Online Content Disappears][research_pew_link_rot]
- [Research, Will We Run Out of Data][research_villalobos]

[book_before_writing]: https://en.wikipedia.org/wiki/Denise_Schmandt-Besserat
[book_orality_literacy]: https://en.wikipedia.org/wiki/Walter_J._Ong
[book_summa_de_arithmetica]: https://en.wikipedia.org/wiki/Summa_de_arithmetica
[book_laws_of_thought]: https://en.wikipedia.org/wiki/The_Laws_of_Thought
[book_printing_press]: https://en.wikipedia.org/wiki/Elizabeth_Eisenstein
[ref_abacus]: https://en.wikipedia.org/wiki/Abacus
[ref_analytical_engine]: https://en.wikipedia.org/wiki/Analytical_engine
[ref_antikythera]: https://en.wikipedia.org/wiki/Antikythera_mechanism
[ref_astrolabe]: https://en.wikipedia.org/wiki/Astrolabe
[ref_bayes_theorem]: https://en.wikipedia.org/wiki/Bayes%27_theorem
[ref_bibliotheca_universalis]: https://en.wikipedia.org/wiki/Bibliotheca_Universalis
[ref_binary_number]: https://en.wikipedia.org/wiki/Binary_number
[ref_carnegie_library]: https://en.wikipedia.org/wiki/Carnegie_library
[ref_chappe_telegraph]: https://en.wikipedia.org/wiki/Chappe_telegraph
[ref_babbage]: https://en.wikipedia.org/wiki/Charles_Babbage
[ref_codex]: https://en.wikipedia.org/wiki/Codex
[ref_cool_uris]: https://www.w3.org/Provider/Style/URI
[ref_cuneiform]: https://en.wikipedia.org/wiki/Cuneiform
[ref_dewey_decimal]: https://en.wikipedia.org/wiki/Dewey_Decimal_Classification
[ref_differential_analyzer]: https://en.wikipedia.org/wiki/Differential_analyser
[ref_double_entry_bookkeeping]: https://en.wikipedia.org/wiki/Double-entry_bookkeeping
[ref_encyclopedie]: https://en.wikipedia.org/wiki/Encyclop%C3%A9die
[ref_euclids_elements]: https://en.wikipedia.org/wiki/Euclid%27s_Elements
[ref_fibonacci]: https://en.wikipedia.org/wiki/Liber_Abaci
[ref_godels_incompleteness]: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
[ref_hollerith]: https://en.wikipedia.org/wiki/Herman_Hollerith
[ref_history_of_paper]: https://en.wikipedia.org/wiki/History_of_paper
[ref_house_of_wisdom]: https://en.wikipedia.org/wiki/House_of_Wisdom
[ref_internet_archive]: https://en.wikipedia.org/wiki/Internet_Archive
[ref_jacquard_loom]: https://en.wikipedia.org/wiki/Jacquard_machine
[ref_journal_des_scavans]: https://en.wikipedia.org/wiki/Journal_des_s%C3%A7avans
[ref_library_of_alexandria]: https://en.wikipedia.org/wiki/Library_of_Alexandria
[ref_link_rot]: https://en.wikipedia.org/wiki/Link_rot
[ref_logarithm]: https://en.wikipedia.org/wiki/Logarithm
[ref_lovelace]: https://en.wikipedia.org/wiki/Ada_Lovelace
[ref_model_collapse]: https://en.wikipedia.org/wiki/Model_collapse
[ref_movable_type]: https://en.wikipedia.org/wiki/Movable_type
[ref_al_khwarizmi]: https://en.wikipedia.org/wiki/Muhammad_ibn_Musa_al-Khwarizmi
[ref_napiers_bones]: https://en.wikipedia.org/wiki/Napier%27s_bones
[ref_pagerank]: https://en.wikipedia.org/wiki/PageRank
[ref_pascaline]: https://en.wikipedia.org/wiki/Pascal%27s_calculator
[ref_philosophical_transactions]: https://en.wikipedia.org/wiki/Philosophical_Transactions_of_the_Royal_Society
[ref_phoenician_alphabet]: https://en.wikipedia.org/wiki/Phoenician_alphabet
[ref_pinakes]: https://en.wikipedia.org/wiki/Pinakes
[ref_punched_card]: https://en.wikipedia.org/wiki/Punched_card
[ref_scriptorium]: https://en.wikipedia.org/wiki/Scriptorium
[ref_slide_rule]: https://en.wikipedia.org/wiki/Slide_rule
[ref_copyright_statute_anne]: https://en.wikipedia.org/wiki/Statute_of_Anne
[ref_stepped_reckoner]: https://en.wikipedia.org/wiki/Stepped_reckoner
[ref_tide_predicting_machine]: https://en.wikipedia.org/wiki/Tide-predicting_machine
[ref_turing_machine]: https://en.wikipedia.org/wiki/Turing_machine
[research_ai_models_collapse]: https://www.nature.com/articles/s41586-024-07566-y
[research_shannon]: https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication
[research_bush]: https://en.wikipedia.org/wiki/As_We_May_Think
[research_doctorow]: https://pluralistic.net/2024/03/14/inhuman-centipede/
[research_fineweb]: https://arxiv.org/abs/2406.17557
[research_link_rot_ahrefs]: https://ahrefs.com/blog/link-rot-study/
[research_kahle]: https://blog.archive.org/2015/02/11/locking-the-web-open-a-call-for-a-distributed-web/
[research_turing]: https://en.wikipedia.org/wiki/Turing%27s_proof
[research_brand]: https://jods.mitpress.mit.edu/pub/issue3-brand
[research_pew_link_rot]: https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/
[research_villalobos]: https://arxiv.org/abs/2211.04325
