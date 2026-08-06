# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A303, the Convair X-6, drafted. Committed and **not pushed**, per the four-pass rhythm.
A297 through A302 are unchanged and pushed. **No article in this series is published.**

---

## The Class Judgement Went the Other Way

The genre document reserves a **documentation-poor** class at 150 to 400 lines and 20 to 60
references, and an aircraft that was never built is the obvious candidate for it. I let the record
decide instead of assuming, and the record said the opposite.

The Aircraft Nuclear Propulsion programme ran fifteen years, spent about a billion dollars, and left
a primary technical record **larger than that of most flown aircraft in this series**. A303 is
treated at full length. The draft stands at 995 lines and 287 references, and its contemporary share
is already 32.8 percent of dated references, inside the target range on the draft pass alone.

---

## The Primary Record Is in a Different Archive, and That Is the Finding

**ANP was an Atomic Energy Commission and Air Force programme, so its reports went to the AEC and are
held today by the Department of Energy**, discoverable through the Office of Scientific and Technical
Information rather than through the NASA Technical Reports Server.

My first NTRS harvest returned 203 documents of which twelve were ANP-relevant, and the natural
inference from that is that the record is thin. **That inference is exactly wrong.** An OSTI harvest
returned 322 documents from the programme era, including the founding NEPA report of 1947, the
Lexington Project minutes of 1948, Blizard's *Shield Optimization* of 1953, the Aircraft Reactor
Experiment operating reports, the HTRE test reports, and an unbroken decade of quarterly progress
reports.

This article introduces OSTI as a source archive for the series. **71 of its 287 references are OSTI
records against 14 from NTRS**, every one verified individually against the OSTI API. Anyone
retracing X-plane work into programmes run by other agencies will hit the same wall, so it is worth
having in the process record.

---

## What the Article Derives

The keystone is whether the shielding a reactor requires can be carried by an aircraft that still has
a reason to fly.

A B-36 at cruise needs **about 100 megawatts of thermal power**, which consumes **0.44 kilograms of
uranium-235 in a hundred hours** against 837 tonnes of kerosene for the same energy. That factor of
nearly two million is the entire attraction.

Against it stands **23.2 centimetres of lead**. Minimizing shield mass plus fuselage structure over
the reactor-to-crew separation gives an interior optimum at **10.1 metres**, which a 49 metre B-36
fuselage accommodates easily and which is the geometry the NB-36H actually used. The shield that
results weighs **37 tonnes, a fifth of gross weight and 95 percent of the B-36 maximum bomb load**. A
nuclear bomber buys unlimited range by surrendering the payload that made the range worth having.

**Two consequences follow from the exponential and they are the article's contribution.**

Shield thickness depends on the **logarithm** of reactor power, so a thousandfold increase costs under
nine centimetres of lead. The shield is a fixed overhead rather than a proportional cost, which means
small nuclear aircraft are not difficult but **excluded**, and the aircraft kept growing for that
reason.

The same logarithm means **accepting ten times the crew dose saves about two percent of the
aircraft**. The programme could not have been rescued by being braver with the crew, which is worth
stating because it is the obvious thing to wonder.

---

## The Durable Output Was a Reactor

The Aircraft Reactor Experiment ran at Oak Ridge in 1954 as **the world's first molten salt reactor**,
built because a molten salt core gives high temperature at low pressure, which is what an aircraft
wants. That concept is under active commercial development seventy years later while the aircraft
remains unbuilt, and the contemporary section traces the line directly, including a 2024 paper whose
subject is the Molten Salt Reactor Experiment itself.

A programme remembered as a failure produced a reactor technology that outlived it by generations.
The article argues that is a defect in how programmes are scored rather than in what this one did.

---

## Verification

287 references with zero undefined, zero orphaned, and zero duplicate URLs. All 177 meaningful-404
URLs at 200 **across three archives**. All 74 OSTI records and 12 NTRS records verified individually,
all 51 DOIs Crossref-resolved on author and title. `_verify.py` at the 0-error 21-warning corpus
baseline. Zero style violations. Isolated build succeeding with Part 7 navigation and zero unresolved
anchors.

**Independent re-derivation of all 20 worked values found one error**, a decay-heat energy integral
stated as 58 gigajoules that computes to 73. Corrected.

Four source discrepancies are recorded rather than resolved, since none is load-bearing. Programme
cost at one billion against seven billion dollars, crew shield at eleven against twelve tonnes, window
thickness at six against ten to twelve inches, and the NB-36H scrapped at Fort Worth in 1958 against
Carswell in 1957.

---

## What Remains

**Equations at 37 and lines at 995 are below the full-aircraft band**, and neither has been padded.
Both are the business of the passes that follow. The physics here is unusually rich in derivable
relations, so the equation pass has plenty to work with.

Word frequency shows `reactor` at 12.60 per thousand body words, `aircraft` at 12.04, and `shield` at
8.96, all of which are the article's subject, with `programme` at 5.88 and `than` at 5.04 worth a look
in the publication review.

**Publication order dependency is seven deep.** One commit unpushed.

---

## Categories

Still `aerospace history engineering`, still my assumption, now seven articles deep.
