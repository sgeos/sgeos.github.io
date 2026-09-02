#!/usr/bin/env python3
"""Accumulated homonym knowledge for literature sweeps. Repo-level and durable.

WHY THIS EXISTS. Article sweeps were carried forward by copying a per-article
`read_and_dropped.json` from one working directory to the next. The chain grew
A317(35) -> A318(247) -> A319(388) -> A320(469) -> A321(481) -> A322(605) ->
A323(721) and then BROKE at A369, which rebuilt its filters from nothing and
consequently re-derived a lesson the corpus had already paid for. A copied file
is not a store. This module is the store.

TWO KINDS OF KNOWLEDGE LIVE HERE AND THEY ARE NOT INTERCHANGEABLE.

  1. PER-RECORD REJECTIONS, in rejected.json. Exact, keyed by digital object
     identifier where one is known and by anchor otherwise, each carrying the
     reason it was dropped and the article that dropped it. These need no
     judgement to reuse: a record judged off-topic once should not be read
     again. This is the reliable half.

  2. PATTERN LESSONS, in NOISE_PATTERNS below. A regex is a generalisation and
     therefore a risk, so ONLY PATTERNS ACTUALLY OBSERVED TO CONTAMINATE A
     SWEEP ARE LISTED, each with the incident that produced it. The 721
     rejection reasons are the raw material for extending this list, and
     extending it is a reading task rather than a counting one.

THE STANDING RULE, which cost several articles to learn. A filter earned in one
article is not automatically valid in the next, IN BOTH DIRECTIONS. Read the
venue histogram of every new sweep. Every contaminant recorded below was found
by reading samples, none by anticipating it.

AND THE COROLLARY THAT BIT A369: A WEAK ANCHOR IS WORSE THAN NO ANCHOR. A
relevance test built from `empirical`, `optimization`, `performance` and
`benchmark` admitted a study of industrial chiller faults, because the words
are common to every empirical field. Anchor on subject nouns.

Usage from an article script:

    import sys; sys.path.insert(0, "_research")
    import homonyms
    kept, dropped = homonyms.filter_records(records)   # records: {key: {...}}
    homonyms.record("10.1234/x", "Title", "wrong field", "A370")
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "rejected.json")

# Each entry is (pattern, incident). The incident is not decoration. It is the
# evidence that the pattern describes a real contaminant, and it is what lets a
# later reader decide whether the pattern still applies to a different subject.
NOISE_PATTERNS = [
    # ---- observed in the A369 compiler sweep, by reading the venue histogram
    (r"\bdielectric\b", "A369: 'binary translation' returned 45 records on the static "
                        "dielectric constants of BINARY LIQUID MIXTURES"),
    (r"\bliquid mixtur", "A369: same incident as dielectric"),
    (r"\blanguage corpora\b", "A369: 'code corpora' returned LINGUISTIC corpora"),
    (r"\bmeasure spaces\b", "A369: 'metric' returned MEASURE THEORY"),
    (r"\btrainee", "A369: 'interpreter' returned the training of HUMAN interpreters"),
    (r"\binterpreter training\b", "A369: same incident as trainee"),
    (r"\bchiller", "A369: an industrial CHILLER FAULT study reached the shortlist through "
                   "the word 'empirical' in a software-engineering venue"),
    (r"\bheat pump\b", "A369: same family as chiller"),
    (r"\bgene expression\b", "A369: 'expression' is a compiler term and a biology term"),
    (r"\bnative speaker", "A369: 'native code' versus NATIVE SPEAKERS"),
    (r"\bnative species\b", "A369: 'native code' versus NATIVE SPECIES"),

    # ---- A345, the X-48. Found by READING the two-sided audit and then measuring
    #      the specific family, not by suspecting it in advance.
    (r"\bforaminifer|\bmicrofossil", "A345: 'dynamically scaled model' is a free-flight "
                                     "aircraft and also a SINKING MARINE MICROFOSSIL, in "
                                     "'Estimation of sinking velocities using free-falling "
                                     "dynamically scaled models: foraminifera as a test case'"),
    # ---- A346, the X-49. THE FIRST OF THESE WAS FOUND BY A344 AND RECORDED ONLY AS
    #      PROSE. A344's publication review reported that its refused records included
    #      "a substantial literature on estimating the weight of a foetus" and wrote
    #      that into three process files. Nobody wrote it into this store, so when A346
    #      made `weight estimation` an anchor for its retrofit-cost argument, thirteen
    #      clinical records walked in. A lesson recorded as prose is not an instrument.
    (r"\bchildren\b|\bpaediatric|\bpediatric|\bobese\b|\bfetal\b|\bfoetal\b|"
     r"birth weight|\bgestational|\bantenatal|\bultrasound.{0,20}weight|"
     r"emergency department|\bpatients?\b.{0,30}weight",
     "A346: 'weight estimation' is what a rotorcraft designer does to an airframe and "
     "also what a clinician does to a child or a foetus. A344 met the same family from "
     "the other side, as records its gate refused, and recorded it only in prose"),
    (r"ducted (?:rocket|ramjet)|solid ducted|ramjet|scramjet.{0,20}duct|inlet buzz",
     "A346: a ducted propulsor is a helicopter anti-torque device and a DUCTED ROCKET "
     "is solid-propellant missile propulsion, which shares the word"),
    (r"air condition\w*|heat pump|\bHVAC\b|ventilation duct|chimney",
     "A346: 'ducted' also describes domestic air conditioning, which reached the pool "
     "through the same anchor"),
    (r"journal bearing|magnetic bearing|\bbearings?\b.{0,25}rotor|"
     r"rotor ?dynamic.{0,30}(?:bearing|shaft|machine|journal)|rotor balancing",
     "A346: 'rotor dynamics' is a helicopter subject and also the SHAFT-AND-BEARING "
     "discipline of turbomachinery, which shares the word and nothing else"),
    (r"surfactant|micellar|polymer(?:ic)? (?:solution|additive)|"
     r"drag reduc\w+.{0,30}(?:polymer|surfactant|solution|additive)",
     "A346: 'drag reduction' is a rotor hub fairing and also the POLYMER AND SURFACTANT "
     "chemistry of pipe flow, which is a larger literature than the aeronautical one"),

    (r"solid pitch|pycnometer|\bbitumen|\basphalt\b|coal tar",
     "A345: 'relative density' is the mass condition of a dynamic free-flight model "
     "and also the ASTM MATERIALS TEST for solid pitch by pycnometer, which reached "
     "the pool seven times"),
    (r"hydraulic jump|stilling basin|\bspillway\b|open[- ]channel flow",
     "A345: the Froude number is an aeroplane at matched dynamics and also the "
     "OPEN-CHANNEL HYDRAULICS of a hydraulic jump, which is where most of the "
     "Froude literature actually lives. Two escaped an aeronautical gate on "
     "'scale effects' plus 'air'"),
    (r"\bheliostat\b", "A345: 'wind tunnel test of a full-scale heliostat' is SOLAR "
                       "ENERGY, admitted on the wind tunnel alone"),
    (r"ion cyclotron|mass spectrometr|mass spectroscop",
     "A345: 'frequency sweep' is a flight-test excitation and also the SWEEP OF A MASS "
     "SPECTROMETER"),
    (r"guided wave signal|ultrasonic (?:noise|guided)",
     "A345: 'frequency sweep' and 'noise' both belong to ULTRASONIC NDT"),
    (r"\bchorus (?:rising|element|wave)", "A345: 'frequency sweep' is also a MAGNETOSPHERIC "
                                         "CHORUS EMISSION in space physics"),
    (r"heat (?:transfer|exchanger).{0,70}\btubes?\b|\btubes?\b.{0,70}heat (?:transfer|exchanger)",
     "A345: 'angle of attack' is an aeroplane and also the INCLINATION OF A HEAT "
     "EXCHANGER TUBE to the cross-flow"),

    # ---- carried from the X-Planes sweeps, where the recurring families were
    #      meteorology, marine engineering and spectroscopy sharing vocabulary
    #      with aerodynamics. See rejected.json for the individual judgements.
    (r"\bmeteorolog", "X-Planes: 'boundary layer' is aerodynamics and also the ATMOSPHERIC "
                      "boundary layer; 71 rejection reasons name meteorology"),
    (r"\bnerve block", "X-Planes: 'blocking' returned anaesthesia"),
    (r"\banaesth|\banesth", "X-Planes: same family as nerve block"),

    # ---- general field bleed, seen across several sweeps
    (r"\bpatient\b|\bclinic", "medical bleed, seen in most sweeps"),
    (r"\bvaccin|\bepidemi|\bmortality\b", "public-health bleed"),
    (r"\bblood pressure\b|\bcholesterol\b", "'lowering' is a compiler term and a medical one"),
    (r"\bclassroom\b|\bcurricul|\bpedagog", "'instruction' is a machine term and a TEACHING term"),
    (r"\bnanoparticle|\bcatalys", "'synthesis' is a program term and a CHEMICAL term"),
    (r"\bwireless sensor network", "'coverage' in sensor networks is a different problem"),
    (r"\bsupertanker|\bsingle[- ]screw\b|\bmarine propuls",
     "A324: MARINE PROPULSION, and it was CREATED by widening an anchor list. Adding "
     "`propulsive` so that 'Propulsive efficiency from an energy utilization standpoint' "
     "would pass also admitted 'the propulsive efficiency of single-screw supertankers'. "
     "Widening an anchor list has a price and this is the shape of it"),
    (r"\benergy height\b.{0,40}\b(?:channel|weir|flume|hydraulic)|\bspecific energy\b.{0,30}"
     r"\b(?:batter|cell|electrode)",
     "A324: ENERGY HEIGHT is a term of art in OPEN-CHANNEL HYDRAULICS and SPECIFIC ENERGY "
     "belongs to BATTERIES, which is now far larger than the aeronautical sense"),

    # ---- observed in the A334 spacecraft sweep, by reading the kept sample
    (r"\bmicrogrid|\bsmart grid\b|\bgrid-?connected\b|\beconomic dispatch\b|"
     r"\bpeak shaving\b|\bwind farm\b|\bphotovoltaic (?:plant|power station|farm)",
     "A334: DEPTH OF DISCHARGE and CYCLE LIFE are spacecraft battery terms and also "
     "GRID STORAGE terms. 'Optimized Economic Dispatch and Battery Sizing in Wind "
     "Microgrids: A Depth of Discharge Perspective' reached the kept set. The cell "
     "degradation physics is genuinely shared; the dispatch economics is not"),
    (r"\b5G\b|\b6G\b|\bhandover\b|\bthroughput\b|\brouting protocol\b|"
     r"\bmedium access\b|\bmodulation and coding\b|\bbit error rate\b",
     "A334: SATELLITE COMMUNICATIONS NETWORKING shares 'low earth orbit' with "
     "everything this series does. 'Handover Solutions for 5G Low-Earth Orbit "
     "Satellite Networks' passed a gate anchored on the orbit alone. The constellation "
     "is the same and the subject is not"),
    (r"\belectric vehicle\b|\bEV batter|\bplug-?in hybrid\b|\bautomotive batter|"
     r"\bsecond-?life\b|\bbattery reuse\b|\bechelon utilization\b",
     "A334: the ELECTRIC ROAD VEHICLE again, arriving this time through battery "
     "cycle life rather than through propulsion. Recorded in A331 as the largest "
     "body this series has had to exclude. The SECOND-LIFE and BATTERY REUSE "
     "literature is the same body arriving through end-of-life sorting"),
    (r"\boff-?grid\b|\bsolar PV\b|\bPV/batter|\bstandalone photovoltaic\b",
     "A334: 'Optimum battery depth of discharge for off-grid solar PV/battery "
     "system' passed a gate anchored on depth of discharge. TERRESTRIAL OFF-GRID "
     "SOLAR uses the article's exact relation for a different machine"),
    (r"\banode\b|\bcathode\b|\belectrolyte\b|\belectrode material|"
     r"\bsolid-?state batter|\bcoin cell\b",
     "A334: BATTERY ELECTRODE MATERIALS CHEMISTRY, which owns the phrases cycle "
     "life and capacity fade and is orders of magnitude larger than the spacecraft "
     "power literature. 'Biomimetic Spider-Web-Like Composites for Enhanced Rate "
     "Capability and Cycle Life' reached the kept set"),
    (r"\bcontact graph\b|\bdelay-?tolerant network|\brouting protocol\b|"
     r"\binter-?satellite link\b.{0,40}\b(?:capacity|throughput|handover)",
     "A334: SATELLITE NETWORKING again, this time through contact graph routing "
     "rather than through 5G. Same field, different entry point"),
    (r"\breefing\b.{0,40}\b(?:patell|knee|shoulder|capsul\w*\s+plicat|arthroscop|"
     r"surgical|ligament|instabilit)|\b(?:medial|capsular)\s+reefing\b",
     "A335: SURGICAL REEFING in orthopaedics, a tightening of soft tissue, shares the "
     "exact word with parachute reefing. 'Long-Term Outcomes of Medial Reefing for "
     "Recurrent Patellar Instability' reached the kept set"),
    (r"\bparachute\b.{0,40}\b(?:trial|metaphor|evidence-based|randomi[sz]ed)|"
     r"\b(?:infliximab|azathioprine|statin|placebo)\b",
     "A335: THE PARACHUTE METAPHOR IN MEDICINE, from the famous trial parody, is a "
     "recurring title device in clinical writing. 'Infliximab and Azathioprine: "
     "Bridge or Parachute?' reached the kept set"),
    (r"\bprobabilistic risk assessment\b.{0,60}\b(?:nuclear plant|offshore|drilling|"
     r"dose.response|health effect|chemical|pipeline|dam|seismic|flood)|"
     r"\b(?:dose.response|carcinogen|toxicolog)\w*\b.{0,40}\brisk assessment\b",
     "A335: PROBABILISTIC RISK ASSESSMENT is a method and not a subject. Nuclear "
     "plants, offshore drilling and dose-response toxicology all use it and none of "
     "them is a crewed spacecraft"),
    (r"\b(?:air|aerial)\s+refuel\w*\b.{0,40}\bdrogue\b|\bdrogue\b.{0,40}"
     r"\b(?:refuel|boom|receptacle|tanker)\b",
     "A335: THE AIR-REFUELLING DROGUE is a basket on a hose and shares its word with "
     "the stabilisation parachute. 'Fit Check and Flight Test of Universal Air "
     "Refueling Drogue' reached the kept set"),
    (r"\bflare\b.{0,40}\bparachute\b.{0,30}\bXM\d|\billumination system flare\b|"
     r"\bsurface:\s*parachute\b",
     "A335: the PARACHUTE FLARE again, this time written as 'Flare, Surface: "
     "Parachute XM183' so that the two words are separated and the earlier pattern "
     "missed it"),
    (r"\bODE\b|\bordinary differential equation\b|\bcalculus\b|\bteaching\b",
     "A335: THE PARACHUTE PROBLEM is a standard exercise in differential equations "
     "teaching. 'ODE Models for the Parachute Problem' reached the kept set"),
    (r"\bcrack\b|\bfatigue crack|\bstress intensity\b|\bfracture toughness\b",
     "A335: CRACK OPENING LOAD in fracture mechanics shares the exact phrase with "
     "PARACHUTE OPENING LOAD, which is the article's term of art. 'Observations on "
     "fatigue crack opening load determinations' reached the kept set"),
    (r"\bepoxy\b|\bresin\b|\blaminate\b|\bcomposite\b.{0,30}\bimpact tolerance\b|"
     r"\bimpact tolerance\b.{0,30}\bcomposite\b",
     "A335: IMPACT TOLERANCE means MATERIAL TOUGHNESS in composites and HUMAN "
     "ACCELERATION TOLERANCE in aeromedicine. 'Advanced epoxy composites of improved "
     "impact tolerance' reached the kept set through the aeromedical anchor"),
    (r"\bparachute flare\b|\billumination flare\b|\bflare\b.{0,25}\b(?:munition|"
     r"pyrotechnic|binder|candle)",
     "A335: THE PARACHUTE FLARE IS A PARACHUTE-SUSPENDED MUNITION and shares both "
     "words with this article. Carried forward from the flare entry in the homonym "
     "table and now observed directly"),
    (r"\bgull(?:y|ies)\b|\bdune\b|\bcrater count|\bstratigraph|\bregolith\b|"
     r"\bfluvial\b|\bglacial\b|\bpermafrost\b",
     "A334: MARS AND PLANETARY SURFACE GEOMORPHOLOGY, admitted by an aerobraking "
     "harvest through `planetary atmosphere`. Aerobraking AT a planet is adjacent and "
     "legitimate; the geology of the surface it brakes over is not"),
    (r"\binstrument landing system\b|\blocalizer\b|\bglide slope\b.{0,50}"
     r"\b(?:sideband|antenna|signal|radio|ILS)",
     "A334: the ILS GLIDE SLOPE is a radio navigation aid for conventional "
     "aircraft and shares the phrase `glide slope` with an unpowered spacecraft "
     "approach. 'Analysis of Instrument Landing System Glide Slope Performance "
     "Sensitivity to Sideband-Only Phase Variation' reached the kept set"),
    (r"\bstack\s*overflow\b.{0,60}\b(?:question|answer|post|comment|thread|"
     r"developer|community|site|user|tag|badge|reputation|snippet|survey)|"
     r"\b(?:question|answer|post|comment|thread|developer|community|mining|"
     r"crowd)\w*\b.{0,60}\bstack\s*overflow\b",
     "A371: STACK OVERFLOW THE WEBSITE against the stack overflow CONDITION. "
     "'On using Stack Overflow comment-edit pairs to recommend code maintenance "
     "changes' is a software-engineering paper about a question-and-answer site, "
     "and it reached a stack-bound cluster, which is a claim about the literature "
     "and not merely a stray record. Both word orders are matched because the site "
     "name may lead or trail"),
    (r"\bstatistical static timing\b|\bstatic timing analysis\b.{0,70}"
     r"\b(?:metal|interconnect|gate.level|netlist|VLSI|CMOS|transistor|die|wafer|"
     r"cell librar|process variation|waveform|circuit|clock tree|signoff|sign.off)|"
     r"\b(?:metal|interconnect|gate.level|netlist|VLSI|CMOS|transistor|wafer|"
     r"circuit|clock tree)\w*\b.{0,70}\bstatic timing analysis\b",
     "A371: VLSI STATIC TIMING ANALYSIS is a circuit-design field that shares the "
     "exact phrase `static timing analysis` with worst-case execution time analysis "
     "for software. 'A Novel Method for Reducing Metal Variation With Statistical "
     "Static Timing Analysis' and 'Equivalent Waveform Propagation for Static Timing "
     "Analysis' both reached a WCET cluster. The phrase alone cannot be filtered "
     "because genuine software timing papers use it, so the qualifier is the "
     "circuit vocabulary that software timing analysis never carries"),
    (r"\bjust.in.time\b.{0,60}\b(?:manufactur|inventory|supply chain|logistics|"
     r"delivery|construction|assembly line|lean|procurement|warehouse|teaching|"
     r"instruction|training|adaptive intervention|clinical)|"
     r"\b(?:manufactur|inventory|supply chain|logistics|construction|lean|"
     r"warehouse|teaching|classroom|nursing|clinical)\w*\b.{0,60}"
     r"\bjust.in.time\b",
     "A371: JUST-IN-TIME MANUFACTURING and JUST-IN-TIME INSTRUCTIONAL DELIVERY "
     "against just-in-time COMPILATION. The manufacturing sense predates the "
     "compiler sense and is far larger. 'A Dynamic Just-in-Time Component Delivery "
     "Framework for Off-Site Construction' and a speech-therapy study of "
     "'just-in-time programming' on an augmentative communication device both "
     "reached the kept set through the bare phrase"),
    (r"\bthinking like a compiler\b|\bcompiler\b.{0,60}\b(?:exam|grammatical task|"
     r"essay|second.language|foreign language learn|vocabulary acquisition|"
     r"classroom discourse)\b",
     "A371: THE COMPILER AS A METAPHOR in language teaching. 'Thinking Like a "
     "Compiler: A Systematic Approach to Solving Grammatical Tasks in Exams' is a "
     "pedagogy paper. This is the same shape as the parachute metaphor in clinical "
     "writing already recorded here. The pattern is deliberately narrow, because "
     "teaching COMPILER CONSTRUCTION is a legitimate and well-populated topic and a "
     "broad education filter would discard it"),
    (r"\bformal semantics\b.{0,60}\b(?:propositional attitude|natural language|"
     r"discourse|pragmatics|quantifier scope|montague|linguistic|utterance|"
     r"presupposition|modal logic of belief)|"
     r"\b(?:natural language|discourse|pragmatics|montague|linguistic|utterance)"
     r"\w*\b.{0,60}\bformal semantics\b",
     "A371: FORMAL SEMANTICS IN LINGUISTICS AND PHILOSOPHY OF LANGUAGE against "
     "programming-language semantics. 'Formal semantics for propositional "
     "attitudes' reached the kept set. The two fields share the exact phrase and "
     "some of their machinery, so only the linguistic subject matter distinguishes "
     "them. Formal VERIFICATION carries no equivalent ambiguity"),
    (r"^(?:unboxed|compiler|compcert|garbage collection|interpreter|bytecode|"
     r"layout|arena|aggregate)$",
     "A372: A ONE-WORD TITLE IDENTICAL TO A SUBJECT ANCHOR is book front or back "
     "matter and not a work. `Unboxed`, a chapter of an MIT Press book also titled "
     "`Unboxed`, reached the kept set, as did `Compiler` and `CompCert` as chapter "
     "titles. THIS IS A SUBSTANCE TEST AND NOT A SUBJECT TEST, and it is recorded "
     "here because the accumulated store is the only thing every sweep consults"),
    (r"^(?:cross.)?compiler,?\s*n\.?$|^sandboxing,?\s*n\.?$|"
     r"^garbage collection,?\s*n\.?$|^\w[\w\s-]{0,28},\s*(?:n|v|adj|adv)\.$",
     "A372: DICTIONARY HEADWORDS. An Oxford English Dictionary entry for the word "
     "`compiler` is typed as a book-chapter and its title matches every subject "
     "anchor perfectly, because the title IS the anchor. Three reached A371 and "
     "three reached A372 before an audit caught them. THE GATE HAS NO "
     "MINIMUM-SUBSTANCE TEST and a one-word headword passes it trivially, which is "
     "a different failure from a homonym and is caught by the same store"),
    (r"\bcompiler\b.{0,60}\b(?:medieval|manuscript|scribe|codex|florilegi|"
     r"anthologi[sz]|Bohemia|monastic|vernacular translation)|"
     r"\b(?:medieval|manuscript|scribe|codex|monastic)\w*\b.{0,60}\bcompiler\b",
     "A372: THE MEDIEVAL COMPILER, meaning the person who assembles a manuscript "
     "from sources, against the PROGRAM that translates code. A chapter titled "
     "`Compiler` in `Passionate Copying in Late Medieval Bohemia` reached A371's "
     "kept set. The word predates the computing sense by centuries"),
    (r"\bintermediate representation\b.{0,60}\b(?:speech|phonem|pinyin|acoustic|"
     r"dialect|handwriting|image caption|音)|"
     r"\b(?:speech|phonem|pinyin|acoustic|dialect)\w*\b.{0,60}"
     r"\bintermediate representation\b",
     "A372: THE INTERMEDIATE REPRESENTATION IN SPEECH AND SIGNAL PIPELINES against "
     "the COMPILER intermediate representation. 'Toward Unified Chinese "
     "Multi-Dialectal Speech Recognition via Pinyin Intermediate Representation' "
     "reached the code-generation cluster"),
    (r"\bgarbage collection\b.{0,70}\b(?:vehicle|truck|waste|municipal|refuse|bin|"
     r"kerbside|curbside|recycl|landfill|fee|route|household|sanitat|street|"
     r"municipal solid waste|solid waste|county|environmental cost|"
     r"IoT|sensor|smart city|bin level|ultrasonic|LoRa|monitoring system)|"
     r"\b(?:waste|municipal|refuse|landfill|recycl|sanitat|household|smart)\w*\b"
     r".{0,70}\bgarbage collection\b|\bsmart garbage\b",
     "A372: MUNICIPAL WASTE COLLECTION against the MEMORY-RECLAMATION sense. "
     "'Deep Learning Based Garbage Detection for Autonomous Garbage Collection "
     "Vehicles' and 'Garbage collection fees: according to regulations or in fact?' "
     "both reached the kept set. The waste sense is far larger than the computing "
     "one and shares the exact phrase"),
    (r"\b(?:facility|facilities|plant|factory|warehouse|logistics|hospital|office|"
     r"store|shop.floor|workshop|construction site|site|city|urban) layout\b|"
     r"\blayout of the (?:old )?city\b|\blayout\b.{0,50}\b(?:spatial syntax|urban|streetscape|land use)\b|"
     r"\bsystematic layout planning\b|\bwaffle.layout\b|"
     r"\blayout\b.{0,60}\b(?:heliostat|solar field|wind farm|MOSFET|"
     r"transistor|photovoltaic|substation)|"
     r"\blayout\b.{0,60}\b(?:manufactur|assembly line|production line|"
     r"material handling|supply chain|floor space|workstation)",
     "A372: FACILITY AND PLANT LAYOUT, an operations-research field that shares "
     "`layout optimisation` exactly with compiler data layout. 'Designing the "
     "Logistics Center Structure using the Systematic Layout Planning' and 'Plant "
     "Layout Optimization for Chemical Industry' reached the kept set"),
    (r"\bstructural layout\b|\blayout\b.{0,60}\b(?:wing|fuselage|airframe|"
     r"topology optimi|planform|truss|beam|load.bearing|reinforc)|"
     r"\b(?:wing|fuselage|airframe|planform)\w*\b.{0,60}\blayout\b",
     "A372: STRUCTURAL AND AEROSPACE LAYOUT against memory layout. 'Loading and "
     "planform shape influence on the wing structural layout through topology "
     "optimization' reached the kept set, which is notable because this corpus's "
     "OTHER long series is about aircraft and would want that record"),
    (r"\bcorpus\b.{0,60}\b(?:linguistic|discourse|subjectivity|lexic|"
     r"translation studies|sociolinguist|native speaker|written english|"
     r"spoken|text and corpus)|\b(?:linguistic|discourse|lexic|sociolinguist)"
     r"\w*\b.{0,60}\bcorpus\b",
     "A372: THE LINGUISTIC CORPUS against a corpus of PROGRAMS. 'A Corpus Study of "
     "Nested Sources for Subjectivity Analysis' and a review of 'Text and Corpus "
     "Analysis' reached the kept set. Corpus linguistics is the older and larger "
     "use of the word"),
    (r"\bdynamic dispatch\b.{0,70}\b(?:power|grid|generation|load|energy|"
     r"electricit|renewable|microgrid|unit commitment|intermittent)|"
     r"\b(?:power|grid|energy|electricit|renewable|microgrid)\w*\b.{0,70}"
     r"\bdynamic dispatch\b|\beconomic dispatch\b",
     "A372: POWER-SYSTEM DISPATCH against DYNAMIC METHOD DISPATCH. 'Review of "
     "Dynamic Dispatch Research Considering Intermittent Power Generation' reached "
     "the object-dispatch cluster, which is a claim about the literature and not "
     "merely a stray record"),
    (r"\bunboxed?\b.{0,50}\b(?:illustration|portfolio|photograph|archive|"
     r"manuscript|folder|carton|accession|finding aid)|"
     r"\b(?:box(?:es)? \d|folder|carton|accession)\b.{0,50}\bunboxed?\b",
     "A372: `UNBOXED` IN ARCHIVAL CATALOGUING against unboxed VALUES. 'Boxes 90-111: "
     "Miscellaneous Illustrations, Unboxed Illustrations and Portfolios' is a "
     "finding aid and reached the representation cluster"),
    (r"\bpeephole\b(?!.{0,40}\b(?:optimi[sz]|compil|code|instruction|window|"
     r"transformation))",
     "A371: THE PEEPHOLE AS AN OPTICAL AND CRITICAL-THEORY TERM against the "
     "PEEPHOLE OPTIMISATION. 'Beckett, Deleuze and the Televisual Event: Peephole "
     "Art' reached the kept set. The compiler sense practically always names the "
     "optimisation, so a negative lookahead is safe here where a bare rejection "
     "would not be"),
    (r"\bsemantic preservation\b.{0,70}\b(?:narrative|marketing|cultural|"
     r"translation quality|machine translation|LLM|summari[sz]ation|"
     r"natural language|discourse|localis|localiz)|"
     r"\b(?:narrative|marketing|cultural|machine translation|summari[sz]ation)"
     r"\w*\b.{0,70}\bsemantic preservation\b",
     "A371: SEMANTIC PRESERVATION IN NATURAL LANGUAGE GENERATION against SEMANTIC "
     "PRESERVATION IN COMPILATION, which is the exact theorem a verified compiler "
     "proves. 'Semantic Preservation in LLM-Based Cultural Narrative Generation for "
     "Marketing Communication Contexts' reached the verified-compilation cluster, "
     "which is the worst possible place for it to land"),
    (r"\btiming anomal\w*\b.{0,60}\b(?:market|stock|equity|return|trading|"
     r"calendar|investor|portfolio|crisis)|\b(?:market|stock|equity|trading|"
     r"investor|portfolio)\w*\b.{0,60}\btiming anomal",
     "A371: THE CALENDAR TIMING ANOMALY IN FINANCE against the PROCESSOR TIMING "
     "ANOMALY, which is the phenomenon where a locally faster execution produces a "
     "globally slower one. 'Investigation of Timing Anomalies in the Russian Stock "
     "Market in the Post-Crisis Period' reached a worst-case execution time cluster"),
    (r"\bjust.in.time\b.{0,50}\b(?:defect|bug|fault) (?:predict|detect)|"
     r"\b(?:defect|bug) prediction\b.{0,50}\bjust.in.time\b",
     "A371: JUST-IN-TIME DEFECT PREDICTION, a software-engineering term meaning "
     "prediction at commit time, against JUST-IN-TIME COMPILATION. This is a THIRD "
     "sense of the phrase in this corpus, after manufacturing and instructional "
     "delivery, and it is the one that survives a computing qualifier because it is "
     "itself computing. 'An exploratory study on just-in-time "
     "multi-programming-language bug prediction' reached a bytecode cluster"),
    (r"\bsign language\b|\b(?:simultaneous|court|medical|conference|community) "
     r"interpret(?:er|ing)\b|\binterpreter\b.{0,40}\b(?:deaf|hearing|"
     r"multilingual|bilingual|patient|clinic)",
     "A371: THE HUMAN INTERPRETER, and SIGN LANGUAGE most of all, against the "
     "PROGRAM interpreter. 'Sign Language Interpreter AI using machine learning "
     "algorithm' reached the kept set through an anchor qualified by `language`, "
     "which is exactly the wrong qualifier for this word"),
    (r"\bJava\b.{0,40}\b(?:field|basin|island|sea|volcano|seismic|earthquake|"
     r"tsunami|province|regenc|Indonesia|East Java|West Java|Central Java)|"
     r"\b(?:East|West|Central) Java\b|\bpre.stack (?:depth|time) migration\b|"
     r"\bpre.stack\b.{0,40}\b(?:seismic|imaging|migration|gather)",
     "A371: JAVA THE ISLAND against JAVA THE LANGUAGE, and PRE-STACK seismic "
     "imaging against the CALL STACK. 'Advanced technology imaging of the Mudi "
     "Field, East Java improvements utilizing pre-stack depth migration' carries "
     "both homonyms in one title and is geophysics"),
    (r"\btiming yield\b|\bgate.level\b.{0,70}\btiming\b|"
     r"\b(?:ASIC|CMOS|NBTI|netlist|standard cell|tape.?out|"
     r"multi.corner|process corner|combinational logic gate)\b.{0,70}\btiming\b|"
     r"\btiming\b.{0,70}\b(?:ASIC|CMOS|NBTI|netlist|standard cell|"
     r"multi.corner|process corner|nm (?:node|process|technology))\b",
     "A371: CIRCUIT TIMING SIGNOFF against SOFTWARE TIMING ANALYSIS, the broader "
     "sibling of the statistical-static-timing family already recorded above. "
     "'Reliability verification of a dual-car elevator ASIC in SCL 180-nm CMOS: "
     "NBTI aging, multi-corner timing' reached the kept set without using the exact "
     "phrase the earlier pattern required"),
    (r"\bpseudo.static analysis\b|\bstatic analysis\b.{0,70}\b(?:soil|pile|"
     r"foundation|bearing capacity|seismic|slope stability|embankment|retaining "
     r"wall|beam|truss|girder|reinforced concrete|masonry|shear wall|"
     r"geotechnical)|\b(?:soil|pile|foundation|bearing capacity|seismic|slope|"
     r"embankment|retaining wall|truss|girder|masonry|geotechnical|"
     r"offshore structure|uncertain structure|eigenvalue|frame structure|"
     r"sub.?frame|fatigue|graded plate|shell|laminate|chassis|bridge deck|"
     r"finite element|CAE)\w*\b"
     r".{0,70}\bstatic analysis\b|"
     r"\bstatic analysis of (?:offshore|uncertain|frame|shell|plate) structur|"
     r"\bnonlinear static analysis\b",
     "A371: STATIC ANALYSIS IN STRUCTURAL AND GEOTECHNICAL ENGINEERING, where it "
     "means analysis under static rather than dynamic loading, against static "
     "analysis of program text. 'Seismic Bearing Capacity of a Mounded Foundation "
     "Near a Down-Hill Slope by Pseudo-Static Analysis' and 'Static analysis of "
     "soil/pile interaction in layered soil by BEM/BEM coupling' both reached the "
     "kept set, two in a single sample of thirty"),
    (r"\bset.valued optimi[sz]ation\b|\bset optimi[sz]ation\b|"
     r"\bvector optimi[sz]ation\b",
     "A371: VECTOR OPTIMISATION AND SET OPTIMISATION in mathematical programming "
     "against SIMD VECTORISATION in a compiler. 'Vectorization in Set Optimization' "
     "and 'On vectorization strategies in set optimization' are the same homonym "
     "reached twice in one sweep"),
    (r"\bvirtual machine\b.{0,70}\b(?:cloud|data ?cent|hypervisor|migration|"
     r"consolidat|placement|provisioning|IaaS|OpenStack|CloudSim|elastic|host)|"
     r"\b(?:cloud|data ?cent|hypervisor|IaaS|OpenStack|CloudSim|"
     r"server consolidat)\w*\b.{0,70}\bvirtual machine",
     "A371: THE CLOUD VIRTUAL MACHINE against the LANGUAGE virtual machine. "
     "'Virtual Machine Allocation Policy in Cloud Computing Using CloudSim in Java' "
     "reached a bytecode cluster, which is a claim about the literature and not "
     "merely a stray record. The two senses share the exact phrase and one of them "
     "is far larger"),
    (r"\bcache replacement\b.{0,70}\b(?:web|proxy|CDN|content delivery|cloud|"
     r"mobile user|video|edge server|named data|information.centric|CCN|"
     r"content.centric|mobile|link quality|peer.to.peer|streaming)|"
     r"\b(?:web|proxy|CDN|content delivery|video sharing|edge server|"
     r"information.centric)\w*\b.{0,70}\bcache replacement\b",
     "A371: WEB AND CONTENT-DELIVERY CACHE REPLACEMENT against PROCESSOR CACHE "
     "REPLACEMENT, which is the sense that decides whether timing analysis is "
     "possible at all. 'Cache Replacement Algorithm of Video Sharing System for "
     "Mobile Users' and 'A Client-Side Cloud Cache Replacement Policy' reached a "
     "worst-case execution time cluster"),
    (r"\b(?:software|project|development) cost (?:model|estimat)|"
     r"\bcost estimation model\b|\bCOCOMO\b|\bfunction point analysis\b|"
     r"\bcritical chain\b|\bearned value\b|"
     r"\b(?:time and cost|cost and schedule) analysis\b",
     "A371: SOFTWARE COST ESTIMATION, meaning the money and effort a project "
     "consumes, against the COMPILER COST MODEL, meaning the time or space a "
     "program consumes. 'A Common Sense Approach to Software Cost Model Selection' "
     "reached the kept set. BOTH SENSES ARE COMPUTING, so a computing qualifier "
     "cannot separate them and only the subject matter can"),

    # ---- observed in the A341 sweep, by reading the kept sample the gate returned.
    #      Every one of these shares a whole phrase with the subject rather than a
    #      single word, which is why an aerospace qualifier does not separate them.
    (r"\bcavitat",
     "A341: the CONVERGENT-DIVERGENT NOZZLE is a rocket and jet term and also a "
     "HYDRAULIC one. 'Analysis of high-speed photography of cavitating flow in "
     "convergent-divergent nozzle' reached the kept set. Cavitation is liquid-phase "
     "and cannot occur in the flow this series is about"),
    (r"\bpilot (?:stage|valve|pressure|operated)\b|\bpilot-operated\b",
     "A341: 'PILOT' is the human being in the aeroplane and also the small first "
     "stage of a HYDRAULIC VALVE. 'Characteristic and oscillation tendency study for "
     "different seat geometries of the pilot stage of a valve' reached the kept set, "
     "carrying 'seat', 'oscillation' and 'pilot' at once"),
    (r"\b(?:insect|bird|avian|bat|butterfly|beetle)[- ]?(?:wing|flight|flapping)|"
     r"\bflapping[- ]wing\b|\bornithopter\b|\bfeathers?\b|\bbio-?inspired flight\b",
     "A341: BIOLOGICAL FLIGHT owns wing, flight, aerodynamics, lift and drag "
     "completely. 'Passive mechanisms in flying insects and applications in "
     "bio-inspired flapping-wing micro air vehicles' and 'Morphological effect of "
     "wing tip feathers on aerodynamics performance of a revolving wing' both "
     "reached the kept set"),
    (r"\bunderwater\b|\bsubmarines?\b|\bhydrofoil\b|\bautonomous underwater\b|\bglider fish\b",
     "A341: the BLENDED WING BODY is an aircraft configuration and also an "
     "UNDERWATER VEHICLE configuration, and the underwater literature uses the "
     "identical phrase. 'Synthetic jet-based active flow control for hydrodynamic "
     "enhancement of a blended-wing-body underwater vehicle' reached the kept set"),
    (r"\bwind turbines?\b|\bwind energy\b|\btidal turbine\b",
     "A341: TURBINE BLADES are aerofoils and the wind energy literature writes about "
     "them in the vocabulary of aerodynamics. Distinct from 'wind tunnel', which must "
     "survive, so the pattern is anchored on the whole phrase"),
    (r"\bships?\b|\bvessels?\b|\btwin-screw\b|\bship-steering\b|\bnaval architect",
     "A341: YAW, ROLL, RUDDER and AUTOPILOT are the whole vocabulary of SHIP steering "
     "as well as of flight. 'An internal model control approach to the design of "
     "yaw-rate-control ship-steering autopilots' and 'Dynamic inverse control of ship "
     "rudder roll/yaw stabilization' both reached the kept set. The boundary before "
     "'ship' protects AIRSHIP and RELATIONSHIP, which must survive"),
    (r"\broad vehicles?\b|\bautomobil|\bpassenger cars?\b|\bvehicle yaw rate\b|"
     r"\bthree-axle\b|\belectronic stability (?:control|program)\b",
     "A341: VEHICLE YAW RATE CONTROL is a road vehicle dynamics field with its own "
     "large literature using yaw, sideslip, stability and control identically. "
     "'Adaptive Yaw Control Of Three-Axle Road Vehicles' reached the kept set"),
    (r"\btall building|\bhigh-?rise\b|\bnatural ventilation\b|\bbuilding fa[cç]ade|"
     r"\bbridge deck\b|\bgirder\b|\bwind[- ]?induced vibration of (?:a )?(?:building|bridge)",
     "A341: WIND ENGINEERING for civil structures runs in wind tunnels, computes "
     "aerodynamic characteristics and reports crosswind effects. 'Wind Tunnel Studies "
     "On Tapered Tall Building With Aerodynamic Modification' reached the kept set"),
    # ---- A342, the Boeing X-45. THE CONTAMINANT FAMILIES OF A `unmanned` ANCHOR.
    #      The civil small-aircraft literature is now vastly larger than the combat
    #      one, so a gate anchored on `unmanned` admits it wholesale. The cut is by
    #      APPLICATION and never by PLATFORM, because the supervisory-control and
    #      cooperative-control literature legitimately uses small rotorcraft as
    #      testbeds and those results transfer to the subject. 38 of 39 quadrotor
    #      records survive these patterns and the one that does not is agricultural.
    (r"photogrammetr|precision agricultur|crop (?:monitor|yield|spray|health)|"
     r"land cover|remote sensing|oil spill|heritage|archaeolog|wildlife|"
     r"forest (?:fire|inventory)|power line inspection|parcel deliver|delivery drone|"
     r"\bfarming\b|vineyard|weed detect|disaster (?:response|management|assessment)|"
     r"search and rescue",
     "A342: CIVIL SMALL-AIRCRAFT APPLICATIONS reached the kept set through the bare "
     "`unmanned` anchor, being hyperspectral imaging for precision agriculture, flood "
     "monitoring, forest fire prevention and heritage documentation. The cut is by "
     "application and not by platform, so that cooperative-control work demonstrated on "
     "the same airframes survives"),
    (r"\bcellular\b|blockchain|\b5G\b|\b6G\b|internet of things|\bIoT\b|"
     r"non[- ]terrestrial network|base station|spectrum (?:sharing|allocation)|edge computing",
     "A342: THE AIRCRAFT AS A TELECOMMUNICATIONS NODE rather than as an aircraft. "
     "'Blockchain Technology Enabling UAV Cellular Communications' and 'Unmanned Aerial "
     "Vehicle Cellular Communication Operating in Non-terrestrial Networks' reached the "
     "kept set. The vehicle is incidental to those papers and the network is the subject"),
    (r"unmanned (?:ground|surface|underwater) vehicles?|\bUGVs?\b|\bUSVs?\b|\bAUVs?\b|"
     r"catamaran|autonomous (?:driving|car)\b|self[- ]driving|\brovers?\b|legged robot|"
     r"manipulator arm",
     "A342: UNMANNED GROUND, SURFACE AND UNDERWATER VEHICLES share `unmanned`, "
     "`autonomous`, `mission planning` and `cooperative control` completely with the "
     "subject. 'Vibration Suppression for Unmanned Catamaran' and 'Stingray: a fast small "
     "unmanned ground vehicle for urban combat' reached the kept set. Note that MARINE "
     "CORPS must survive, which is why the pattern names the vehicle types explicitly"),
    (r"microstrip|patch antenna",
     "A342: ANTENNA ENGINEERING shares radar cross section completely. Deliberately "
     "narrow, because radar absorbing material and frequency selective surfaces are "
     "genuinely aircraft signature subjects and an earlier draft of this pattern would "
     "have dropped 'Radioabsorbing material optimal using in the reduction of aircraft "
     "radar cross-section', which is exactly on subject"),

    # ---- A342, THE PUBLICATION REVIEW. Four more consequences of `unmanned`,
    #      found by a harvest aimed at the article's RESULTS rather than its topics.
    #      That harvest returned 1,446 records for the question `how many vehicles
    #      can one operator hold` and only a handful were about it, because the
    #      phrase `unmanned aerial vehicles` belongs to a literature two orders of
    #      magnitude larger than the combat one. The cut stays by APPLICATION.
    (r"detection (?:and (?:track|classif|recognit))?[^.]{0,20}\bof (?:small )?"
     r"(?:unmanned aerial|uavs?|drones?)\b|counter[- ]?(?:uas|uav|drone)|"
     r"anti[- ]drone|drone detect|radar recognition of|acoustic detection of (?:uav|drone)",
     "A342: COUNTER-UAS work treats the aircraft as the TARGET rather than as the "
     "subject, and shares `unmanned`, `radar` and `detection` completely. 'Radar "
     "recognition of multiple UAVs' and 'ON DETECTION OF UNMANNED AERIAL VEHICLES' "
     "reached the kept set. Note the pattern names detection OF the aircraft, so that "
     "detection BY it, which is a sensor-management subject this article touches, "
     "survives"),
    (r"vegetation index|\bndvi\b|multispectral|hyperspectral|orthomosaic|point cloud|"
     r"image (?:processing|classification|segmentation) (?:in|for|of|using) "
     r"(?:unmanned|uav|drone)|crop (?:load|yield|monitor|spray|health|estimation)|orchard",
     "A342: THE AIRCRAFT AS A CAMERA PLATFORM, where the imagery is the subject and the "
     "vehicle carries it. 'Crop load estimation in orchards' and 'Wheat Monitoring Using "
     "Unmanned Aerial Vehicle based Hyperspectral Imagery' reached the kept set through "
     "the bare `unmanned` anchor"),
    (r"\bagricultur|\bdisaster\b|traffic monitoring|industrial inspection",
     "A342: WIDENING THE CIVIL APPLICATION FAMILY ADDED IN THE DRAFT PASS, which named "
     "`precision agricultur` and `disaster (?:response|management|assessment)` and so "
     "missed 'Fixed-Winged Unmanned Aerial Vehicle Systems Utilized in Agriculture' and "
     "'Unmanned Aerial Vehicles for Post Disaster Surveys'. A pattern narrow enough to "
     "name its examples catches only its examples"),
    (r"wafer[- ]level|redistribution layer|\bcmos\b|\bvlsi\b|integrated circuit|"
     r"solder (?:joint|bump)|semiconductor packag|flip chip|hybrid bonding",
     "A342: FAN-OUT IS A SEMICONDUCTOR PACKAGING TERM AS WELL AS THIS ARTICLE'S "
     "KEYSTONE. Fan-out wafer-level packaging is a large and active field sharing the "
     "exact hyphenated term, and 'Redistribution Layer Routing for Fan-Out Wafer-Level "
     "Packaging' reached the kept set. A343 through A345 are unmanned combat aircraft "
     "resting on the same keystone and will meet it again. THE DISCRIMINATING WORDS ARE "
     "OFTEN IN THE CONTAINER AND NOT IN THE TITLE: a Springer chapter titled exactly "
     "`Fan-Out Technology` is separated from this article's keystone only by its book, "
     "`Flip Chip, Hybrid Bonding, Fan-In, and Fan-Out Technology`, which is why the "
     "pattern names that vocabulary and why a sweep that drops the venue field cannot "
     "catch it. AN EARLIER DRAFT OF THIS PATTERN ALSO NAMED `fan-in` AND WAS WRONG, "
     "because FAN-IN-WING is a lift-fan propulsion configuration and the pattern threw "
     "out 'Design Optimization of a Blended-Wing-Body Aircraft with Integrated "
     "Fan-in-Wing', which is exactly on subject. `flip chip` and `hybrid bonding` "
     "identify the container without it"),
    (r"_supp\d|supplementary material(?:s)? (?:for|of)\b",
     "A342: SUPPLEMENTARY-MATERIAL ARTEFACTS are not works. IEEE deposits a separate "
     "record whose title is the paper's title with `_supp1-<id>` appended, so the parent "
     "and its attachment both enter and the attachment is uncitable. Twenty-two reached "
     "the kept set"),

    # ---- A341, the publication review. A DELIBERATE WIDENING THAT WAS BUILT,
    #      MEASURED AND ABANDONED. It is recorded as a pattern with an empty effect
    #      because the useful knowledge is the refusal, not a filter.
    #
    #      A341's framing subject is an aircraft DESIGNATION collision, and its
    #      survey held nothing on designations. Eight queries were run for
    #      designation systems, nomenclature, records management, classification,
    #      archival practice and programme secrecy. They returned 1,510 records
    #      including Massachusetts tax valuations of 1771, tumour identifiers,
    #      salmonella serotype naming, dental implant designation systems, adoption
    #      secrecy and Chilean human rights archives.
    #
    #      DESIGNATION, CLASSIFICATION, RECORDS, IDENTIFIER, NOMENCLATURE and
    #      SECRECY are among the least discriminating words in any literature, and
    #      every discipline that names things uses all of them. Thirteen records
    #      survived an aerospace gate and every one was component nomenclature,
    #      being oxygen equipment, hydraulic systems, propulsion station numbering
    #      and aerofoil naming, which is the wrong sense of the word.
    #
    #      DO NOT WIDEN A GATE FOR THESE WORDS. The subject is not reachable by
    #      bibliographic harvest, and its real sources are the designation
    #      registries themselves. A weak anchor is worse than no anchor, and this
    #      is the sharpest instance the store holds.
    (r"\bsalmonella\b|\bserotype\b|\bdental implant\b|\btax valuation\b|"
     r"\badoption\b.{0,30}\bsecrecy\b|\bhuman rights\b.{0,30}\barchive",
     "A341: the residue of a designation and records harvest that was abandoned. These "
     "specific families reached the shortlist through DESIGNATION, CLASSIFICATION, RECORDS "
     "and SECRECY, which no aerospace qualifier can separate from their other senses. The "
     "harvest was removed rather than filtered and the full incident is in the comment above"),
    (r"\btime compressor\b|\bdelay lines?\b|\bcompressor\b(?=[^.]{0,30}\b(?:signal|pulse|radar|acoustic))",
     "A341: COMPRESSOR is a turbomachinery stage and also a SIGNAL PROCESSING device. "
     "'DELAY LINE TIME COMPRESSOR XT-1A' and its WOX-3A sibling reached the kept set "
     "through the turbomachinery anchor, from a Defense Technical Information Center "
     "harvest aimed at engine cycles"),
    (r"\bdeep ocean\b|\bocean (?:wave|profiler|surveillance|current)\b|\bcoastal\b|"
     r"\bwave (?:forces|spectra|shoaling)\b|\bbuoy\b",
     "A341: the MARINE pattern added earlier is anchored on ship and vessel and does not "
     "catch OCEAN. 'Deep Ocean Unmanned Vehicle Program' entered through the unmanned "
     "anchor and 'TABLES OF THE STATISTICAL DISTRIBUTION OF OCEAN WAVE FORCES' through drag"),
    (r"\bindex of thermal stress\b|\bhot-weather\b|\bheat strain\b|\bhypoxia\b|"
     r"\bacceleration tolerance\b|\bg-induced loss\b",
     "A341: AEROMEDICAL research is about the crew rather than the aeroplane and shares "
     "fighter, aircrew and flight completely. 'Fighter Index of Thermal Stress: Development "
     "of Interim Guidance for Hot-Weather USAF Operations' reached the kept set through the "
     "`fighter` anchor this article itself added"),
    (r"\brailways?\b|\brailroad|\brolling stock\b|\blocomotive|\bhigh-speed trains?\b",
     "A341: RAILWAY CROSSWIND aerodynamics is a real field using the aerodynamic "
     "vocabulary. 'Railway applications. Railway rolling stock power and control "
     "cables' reached the kept set. Note that SHOCK TRAIN is a scramjet isolator term "
     "and must survive, which is why the pattern does not contain a bare 'train'"),
]

_COMPILED = [(re.compile(p, re.I), why) for p, why in NOISE_PATTERNS]


def load():
    """The rejection store, keyed by digital object identifier, URL or anchor."""
    if not os.path.exists(STORE):
        return {}
    with open(STORE, encoding="utf-8") as fh:
        return json.load(fh)


def _anchor_stem(rec):
    """The anchor this record WOULD be given, computed the way `gen_master` does.

    THIS IS THE FIX FOR A STRUCTURAL GAP THAT MADE THREE QUARTERS OF THE STORE
    INERT. Of 728 rejections, 550 are keyed by anchor and 173 by identifier,
    because early sweeps recorded what they dropped after anchors had been
    assigned. But `filter_records` runs at HARVEST time, where a record is keyed
    by its digital object identifier and has no anchor yet, so `_keys_for` could
    never match an anchor-keyed entry and 550 lessons the corpus had paid for
    were invisible to the only step that would use them.

    Computing the prospective stem here closes that. It is the same function
    `gen_master` calls, so a record rejected in one article is recognised in the
    next before it is ever gated.
    """
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), "_lib"))
        import refs
    except Exception:  # noqa: BLE001
        return None
    title = rec.get("title") or ""
    if not title:
        return None
    try:
        return refs.anchor_stem(rec.get("authors") or [], rec.get("year") or "",
                                title, kind="research")
    except Exception:  # noqa: BLE001
        return None


# A STORED ANCHOR MAY CARRY A DISAMBIGUATION SUFFIX. `assign_anchors` appends
# `_2` or `_b` when two records share a stem, so a stored key can be the stem
# plus a suffix while a freshly computed stem never is. Both directions are
# tried, since the store holds whichever form the earlier article emitted.
_SUFFIX = re.compile(r"_(?:\d+|[b-z])$")


def _keys_for(rec, key):
    """Every identity a record might already be stored under."""
    out = {key}
    doi = rec.get("doi") or ""
    if doi:
        out.add(doi)
        out.add("https://doi.org/" + doi.replace("https://doi.org/", ""))
    stem = _anchor_stem(rec)
    if stem:
        out.add(stem)
        out.add(_SUFFIX.sub("", stem))
    if isinstance(key, str) and key.startswith("research_"):
        out.add(_SUFFIX.sub("", key))
    return {k for k in out if k}


def is_rejected(key, rec=None, store=None):
    store = load() if store is None else store
    for k in _keys_for(rec or {}, key):
        if k in store:
            return store[k]
    return None


def noise_hit(text):
    """The first pattern this text trips, with its incident, or None."""
    for rx, why in _COMPILED:
        if rx.search(text or ""):
            return rx.pattern, why
    return None


def filter_records(records, fields=("title", "venue")):
    """Split harvested records into kept and dropped.

    `records` is a mapping of key to record. Returns (kept, dropped) where
    dropped maps key to the reason, so the caller can report what was removed
    instead of silently truncating.
    """
    store = load()
    kept, dropped = {}, {}
    for key, rec in records.items():
        prior = is_rejected(key, rec, store)
        if prior:
            dropped[key] = f"previously rejected ({prior.get('article', '?')}): {prior.get('why', '')}"
            continue
        blob = " ".join(str(rec.get(f, "")) for f in fields)
        hit = noise_hit(blob)
        if hit:
            dropped[key] = f"noise pattern {hit[0]} :: {hit[1]}"
            continue
        kept[key] = rec
    return kept, dropped


def record(key, title, why, article, doi=""):
    """Append one judgement to the store and persist it.

    Judgements are additive and are never removed by tooling. If one turns out
    to be wrong, delete it by hand and say so in the article that found it.
    """
    store = load()
    entry = {"why": why, "article": article}
    if title:
        entry["title"] = title
    entry["key_kind"] = ("doi" if ("doi.org" in key or key.startswith("10.")) else
                         "url" if key.startswith("http") else "anchor")
    if doi:
        entry["doi"] = doi
    store[key] = entry
    with open(STORE, "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(store.items())), fh, indent=1, ensure_ascii=False)
    return entry


def _self_test():
    """A CHECKER THAT CANNOT FAIL IS NOT A CHECK.

    The anchor-stem path is the whole point of `_keys_for` and it is exercised
    only when a harvest happens to contain a previously rejected work, which is
    to say almost never during development. This asserts it directly.
    """
    store = load()
    anchors = [k for k in store if isinstance(k, str) and k.startswith("research_")]
    assert anchors, "the store holds no anchor-keyed rejections to test against"
    # reconstruct a plausible harvest record for one stored anchor and require a hit
    import refs as _r  # noqa: F401  (path already set by _anchor_stem)
    probe = {"title": "5th colloquium on industrial aerodynamics", "authors": [],
             "year": "1982", "doi": "10.0000/probe"}
    keys = _keys_for(probe, "10.0000/probe")
    assert "research_5th_colloquium_1982" in keys, (
        "the prospective anchor stem is not derived, so anchor-keyed rejections "
        "cannot fire at harvest time")
    kept, dropped = filter_records({"10.0000/probe": probe})
    assert dropped and not kept, "a stored anchor-keyed rejection did not fire"
    # and a record with no stored identity must survive
    clean = {"title": "A wholly unremarkable paper about nothing in particular",
             "authors": [], "year": "2026", "doi": "10.0000/clean"}
    kept, dropped = filter_records({"10.0000/clean": clean})
    assert kept and not dropped, "the filter rejects a record it has never seen"
    return f"self-test passed, {len(anchors)} anchor-keyed rejections now reachable"


def stats():
    store = load()
    kinds, arts = {}, {}
    for r in store.values():
        kinds[r.get("key_kind", "?")] = kinds.get(r.get("key_kind", "?"), 0) + 1
        arts[r.get("article", "?")] = arts.get(r.get("article", "?"), 0) + 1
    return {"records": len(store), "key_kinds": kinds, "articles": arts,
            "noise_patterns": len(NOISE_PATTERNS)}


if __name__ == "__main__":
    s = stats()
    print(f"{s['records']} rejection records, {s['noise_patterns']} noise patterns")
    print(" key kinds:", dict(sorted(s["key_kinds"].items())))
    print(" by article:", dict(sorted(s["articles"].items())))
