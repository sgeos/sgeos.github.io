# Common Errors

> **Navigation**: [Reference](./README.md) | [Documentation Root](../README.md)

A catalogue of recurring factual, numerical, and stylistic errors observed during article drafting, with the corrected fact and the canonical source.

This catalogue is intended as a quick reference during research and review. It is not exhaustive. New errors should be added with the date and the source of the correction.

## Numerical Errors

### Receiver Noise Floor at T=100 K, B=1 MHz

Frequently miscomputed as -129 dBm. The correct value is **-119 dBm**.

Verify by deriving from $kTB$: $1.38 \times 10^{-23} \times 100 \times 10^6 = 1.38 \times 10^{-15}$ W = -118.6 dBm. Or from the -174 dBm/Hz reference at 290 K, adjusting for the lower temperature and the 1 MHz bandwidth.

### LiOH Stoichiometric Mass Ratio for CO2 Absorption

The mass of lithium hydroxide consumed per mass of carbon dioxide absorbed is approximately **1.09**, not 0.7 or other values seen in informal sources.

Verify from the stoichiometric reaction $2 \mathrm{LiOH} + \mathrm{CO}_2 \rightarrow \mathrm{Li}_2\mathrm{CO}_3 + \mathrm{H}_2\mathrm{O}$: $\frac{2 \times 23.95}{44.01} = 1.088$.

### Residential Cold-Water Velocity

Typical residential cold-water pipe velocity is **1 to 2 m/s**, not 3 m/s. Match worked examples to realistic values. A 3 m/s figure in a 15 mm pipe is uncomfortably fast and dramatically increases the Darcy-Weisbach head loss.

## Date Errors

### MAVEN as Active Mars Relay

The Mars Atmosphere and Volatile Evolution mission concluded **3 June 2026** after loss of contact in December 2025. Use MRO, Mars Odyssey, Mars Express, and ExoMars Trace Gas Orbiter as the current Mars relay set.

### Akatsuki Operational Status

The JAXA Akatsuki Venus orbiter was officially declared mission terminated on **18 September 2025** after loss of contact in April 2024. Frame as "operated 2010 to mission termination September 2025" rather than ongoing in 2026.

### DSOC Primary Mission

The Deep Space Optical Communications experiment on the Psyche spacecraft concluded its primary technology demonstration on **2 September 2025**. Frame as "demonstrated" or "operated through 2025" rather than ongoing.

### WHO Drinking-Water Guidelines Edition

As of June 2026, the World Health Organization Guidelines for Drinking-Water Quality fourth edition incorporates the **first, second, and third addenda through 18 June 2026**. The third addendum was published on that date.

### Mars Solar Conjunction Schedule

The most recent Mars superior conjunction occurred in January 2026. The next Mars opposition is in February 2027. The next Mars superior conjunction is in early 2028.

## Acronym and Naming Errors

### Polar Codes in CCSDS

Polar codes are 5G New Radio standards, not CCSDS standards. CCSDS uses LDPC AR4JA family and concatenated turbo codes. Do not include polar codes when listing CCSDS-standard FEC.

### Composting Toilet Standard

The governing US standard for composting toilets is **NSF/ANSI 41**, not ASTM F1869. ASTM F1869 actually covers gypsum concrete moisture, an unrelated topic.

### Apollo LRV Speed and Traverse

The Apollo Lunar Roving Vehicle cruise speed is approximately **13 km/h**, with an **18 km/h** record set on Apollo 17. The total Apollo 17 surface traverse was approximately **35.9 km**, not the 92 km that appears in some informal sources (the 92 km figure is the theoretical total range from both batteries combined).

### Biosphere 2 Caloric Closure

Biosphere 2 Mission One produced approximately **80 percent** of crew calories from intensive horticulture across the 2,000 m² cropping area, not the 50 percent that appears in some informal sources. The 80 percent figure is from Silverstone and Nelson 1996.

### Yuegong-365 Food Self-Sufficiency

The Yuegong-365 mission achieved approximately **98 percent overall system closure** with **approximately 80 percent food self-sufficiency**. Do not conflate the two figures. The 80 percent is the food fraction specifically.

### Sceye Stratospheric Airship Designation

The current Sceye flagship designation is **SE2**, not SK-1. The SE2 completed a 12-day, 6,400-mile stratospheric endurance flight ending 6 April 2026 at altitude above 52,000 ft.

### Lighter-Than-Air Research

The Sergey Brin lighter-than-air programme is **LTA Research**. The Pathfinder 1 airship is its first demonstrator. The Wikipedia article is at the slug `Pathfinder_1_(airship)` rather than under the company name.

## URL Errors

### NSF/ANSI Standards URLs

The canonical `nsf.org/standards-development/...` URLs for NSF/ANSI standards return 403 to curl due to bot-detection. The URLs are correct; the curl check is being blocked. See [URL Verification](../process/URL_VERIFICATION.md) for the catalogue of canonical sites that 403 to curl.

### NASA Page Drift

NASA mission pages frequently drift across `nasa.gov/missions/`, `nasa.gov/feature/`, `nasa.gov/centers/`, and `science.nasa.gov/missions/`. When a NASA URL returns 404, the canonical replacement is often the Wikipedia article for the mission, with the new NASA URL not yet stabilised.

### Aquarius Reef Base Depth

Aquarius Reef Base sits at approximately **18 metres** depth (60 feet), not 20 metres. Source: Wikipedia and Florida International University.

## Stylistic Errors

### Filler Adjectives, Above All "Specific"

Added 2026-08-05. The single most damaging stylistic error in this corpus to date.

`specific` escalated to **46.2 uses per thousand words** in the worst article against a natural
corpus rate near 1.7, and one series used `specifically` as an adjective, producing ungrammatical
prose such as "the specifically Gulf oil states" and "the specifically Saudi ratio". Remediation
touched 110 files.

**No instruction caused it.** Every writing and process document was searched and none encourages
the word. It was self-imitation drift, an agent calibrating to its own prior output while
drafting a series. The documented exemplar articles were measured and are clean at 0.0 to 1.6 per
thousand, so imitation of a named model was not the vector either.

**It survived every context reset because nothing could see it.** The publication review verified
punctuation and reported prose style clean on the worst offenders in the corpus. The gap was in
the checks, not in the rules.

Three sibling formulas from the same drift: `the comprehensive treatments` closing a citation 234
times, `The framework provides` or `The framework has` opening 106 of 273 sentences in one
article, and `X admits the compact form` introducing a display equation 130 times.

The word-frequency check in [Style Verification](../process/STYLE_VERIFICATION.md) now detects
this class. The rules are in the Diction and Repetition section of the
[Style Guide](../writing/STYLE_GUIDE.md). Do not strip a word from an article whose subject is
that word: `specific impulse` in a propellant article is a technical term, not a tic.

### LoRa as Mesh Protocol

LoRa is a point-to-point spread-spectrum physical layer, not a mesh protocol. LoRaWAN is a star-topology MAC. Mesh networking over LoRa is provided by third-party protocols such as Meshtastic, MeshCore, and Reticulum.

### Madrid Protocol on Antarctic Waste

The Antarctic Treaty Protocol on Environmental Protection (Madrid Protocol, 1991) requires waste removal "to the maximum extent practicable," not an absolute ban. Some categories such as treated sewage may be disposed in situ under defined conditions.

## Adding to This Catalogue

When the publication review or the research agent surfaces a new recurring error, add it here with:

- The incorrect claim as commonly stated.
- The correct claim and the canonical source.
- A brief verification snippet or citation.

The catalogue grows by accretion. It does not need to be exhaustive to be useful.

## Related Sections

- [URL Verification](../process/URL_VERIFICATION.md) for the URL-check procedure and 403 catalogue
- [Research Agent](../process/RESEARCH_AGENT.md) for the verification workflow
- [Publication Review](../process/PUBLICATION_REVIEW.md) for the review pass
