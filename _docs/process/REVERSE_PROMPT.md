# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-24
**Task**: Draft and publish A155 "Communications and the Link Budget for Off-Grid Space Colonization Analogs" as the third per-subsystem deep-dive following A153 and A154, designed to function as a general off-grid communications system guide with space-colonization as contextual flavour

---

## Verification

### A155 Published as Third Subsystem Deep-Dive

A155 "Communications and the Link Budget for Off-Grid Space Colonization Analogs" published at `_posts/2026-07-01-communications_and_the_link_budget_for_off_grid_space_colonization_analogs.markdown` with front-matter date `2026-07-01 09:00:00 +0000`. 28 references across Reference (25) and Related Post (3) categories. 1,544 lines. MathJax enabled with sixteen display equations and twenty-seven inline expressions. Third per-subsystem deep-dive in the analog-facilities category following A153 and A154. Treats the communications layer under the framing that the link budget is the architectural keystone, with antenna aperture, transmit power, modulation, forward error correction strength, and operating frequency all dimensioned against the required signal-to-noise margin.

### Article Structure

The article opens on the link-budget-as-keystone framing referencing the closure problem analogous to electrical generation-load and water supply-demand mismatch from A153 and A154. The link budget derivation walks the Friis transmission equation in both linear and decibel form, the free-space path loss in general form and the engineering form with kilometre and megahertz units, the effective isotropic radiated power and gain-over-temperature figure of merit equations, the parabolic antenna gain and three-decibel beamwidth, the Johnson-Nyquist thermal noise floor with the correct minus-one-hundred-nineteen dBm calculation at one hundred kelvin and one megahertz, the Shannon-Hartley capacity bound and the energy-per-bit to noise-spectral-density formulation, the link margin definition, and a worked example for a twelve gigahertz Ku-band geostationary uplink yielding eleven decibels of margin. The dependent components section walks antennas (parabolic, omnidirectional, phased array, horn), transmitters and power amplifiers, receivers and low-noise amplifiers with 0.8 to 1.5 decibel noise figures, modems and forward error correction with BPSK at 9 decibels through higher-order QAM schemes, LDPC and concatenated turbo codes, the networking layer under the Institute of Electrical and Electronics Engineers 802.3 Ethernet and 802.11 wireless standards with 802.11s mesh, and the power supply and cooling considerations. A new Doppler Shift and Motion Considerations section covers the non-relativistic Doppler shift equation with worked examples for low Earth orbit Starlink terminals yielding 280 kilohertz at Ku-band, Mars orbital relays, and Mars cruise spacecraft tracked by the Deep Space Network. The latency, bandwidth, and protocol considerations section treats the Mars three to twenty-two minute and lunar 1.3 second light-time delay, the Transmission Control Protocol degradation under multi-minute delays, the Delay-Tolerant Networking Bundle Protocol substitution, and the bandwidth ranges for Mars UHF relay, X-band direct-to-Earth, and the DSOC optical demonstrator. The no-radio-frequency architectures section covers free-space optical and physical data transport. The terrestrial-only cheats section enumerates broadband Internet, cellular, and low Earth orbit constellations. The space-only options section covers the NASA Deep Space Network at Goldstone, Madrid, and Canberra with seventy-metre and thirty-four-metre antennas, the European Space Agency Estrack network at New Norcia, Cebreros, and Malargüe, the Mars Relay Network with MRO, Mars Odyssey, Mars Express, and ExoMars Trace Gas Orbiter after the MAVEN mission conclusion announced June 2026, the lunar relay constellation through LunaNet and ESA Moonlight, and the deep-space optical communications through DSOC with the primary mission concluded September 2025. The keystone-breakdown section covers solar conjunction blackout with X-band 5 degree and Ka-band 2 to 3 degree thresholds (most recent January 2026, next early 2028), entry-descent-landing plasma sheath, and deep outer solar system Voyager regime at 160 bps from 24 billion kilometres. The generalisation section walks five representative non-space use cases. The conclusion explicitly acknowledges the article's dual role as both a space-colonization-analog deep-dive and a general off-grid communications system guide.

### Research Agent Pass

Research agent verified the Friis transmission equation linear and dB forms, the free-space path loss 32.45 constant for kilometre and megahertz, the Shannon-Hartley capacity bound, the parabolic antenna gain with aperture efficiency 0.55 to 0.70 for well-designed dishes, the parabolic three-decibel beamwidth approximately 70 lambda over D in degrees, the Johnson-Nyquist thermal noise with Boltzmann constant 1.380649 times ten to the minus twenty-three joules per kelvin (exact since 2019 SI redefinition), the Doppler shift non-relativistic limit, the NASA Deep Space Network three sites with one seventy-metre antenna and multiple thirty-four-metre antennas each with Madrid adding DSS-53 in February 2022, the ESA Estrack three deep-space thirty-five-metre antennas with the upcoming DSA-4 at New Norcia inaugurated October 2025 entering service March 2026, the Mars Relay Network active orbiters after MAVEN mission conclusion 3 June 2026, the NASA Laser Communications Relay Demonstration with first ILLUMA-T link 5 December 2023, the Psyche DSOC launch 13 October 2023 with first light 14 November 2023, the 267 Mbps from 16 million kilometres in November 2023, the distance record from 494 million kilometres on 3 December 2024, and the primary mission concluded 2 September 2025, the Starlink 2026 figures of approximately 10,000 active satellites with 25 to 50 millisecond latency, the Iridium 66 satellites with Iridium NEXT completed January 2019, the Globalstar 25 second-generation satellites with announced 54-satellite expansion and Amazon acquisition agreement April 2026, the TDRSS planned phaseout in favour of commercial relay, the HF radio 3 to 30 megahertz ionospheric skywave, the VHF and UHF ITU allocations, the IEEE 802.11s mesh, the FCC Part 95 personal radio services, the CCSDS Space Packet Protocol and CFDP standards, the IEEE 802.11ax Wi-Fi 6, 802.11ax 6 GHz Wi-Fi 6E, and 802.11be Wi-Fi 7 published September 2024, the ITU-R Radio Regulations 2024 edition entered force 1 January 2025 after WRC-23, the CCSDS FEC codes including LDPC AR4JA and concatenated turbo, the terrestrial free-space optical 500 metre typical year-round availability, and the Mars solar conjunction January 2026 most recent with next opposition February 2027 and next superior conjunction approximately early 2028.

Critical factual corrections applied include MAVEN removed from active Mars relay list with the mission conclusion announced 3 June 2026 explicitly noted, the DSOC primary mission framed as concluded September 2025 with the November 2023 first link at 267 Mbps from 16 million kilometres and the December 2024 distance record from 494 million kilometres and the possible reactivation under consideration following the May 2026 Mars flyby, the solar conjunction blackout specification expanded with X-band Sun-Earth-Probe angle below approximately five degrees and Ka-band below approximately two to three degrees, the Mars solar conjunction schedule corrected with the most recent January 2026 and next early 2028 rather than late 2026 to early 2027, the polar codes removed from CCSDS-standard list with LDPC and concatenated turbo codes substituted, URL replacements for the NASA Deep Space Network page (Wikipedia), the LCRD page (Wikipedia), the LunaNet page (Wikipedia), the FCC root (Wikipedia), and the Space Telecommunications Radio System (Software-Defined Radio Wikipedia) along with the IETF RFC 9171 page for the Bundle Protocol, and the receiver noise floor calculation corrected from minus one hundred twenty-nine dBm to minus one hundred nineteen dBm to match the stated system noise temperature of one hundred kelvin at one megahertz bandwidth per Johnson-Nyquist.

### Engineering Math Additions

In response to reviewer feedback during the drafting cycle, the article math content expanded from the initial eleven display equations and twenty inline expressions to sixteen display equations and twenty-seven inline expressions, with the additions covering the effective isotropic radiated power $EIRP = P_T \cdot G_T$ in both linear and decibel forms with the regulatory motivation that regulators measure EIRP rather than conducted transmit power, the gain-over-temperature figure of merit $G/T = G_R - 10 \log_{10}(T_{sys})$ in decibels per kelvin as the receive-side counterpart to EIRP, the energy-per-bit to noise-spectral-density ratio $E_b/N_0 = (S/N) \cdot (B/R_b)$ with $N_0 = k T_{sys}$ as the standard link-budget formulation that factors out bandwidth and data rate from modulation and coding performance, and the non-relativistic Doppler shift $\Delta f / f_0 = v_{radial}/c$ in a new Doppler and Motion Considerations subsection with worked examples for low Earth orbit Starlink terminals yielding 280 kilohertz at Ku-band, Mars orbital relays, and Mars cruise spacecraft tracked by the Deep Space Network.

### Reference and Style Verification

Reference integrity confirmed at 25 of 25 reference anchors defined and used, zero missing, zero unused, zero duplicate definitions, plus three related-post anchors. Prose style confirmed with no contractions, no em-dashes or en-dashes in the body, no prose colons or semicolons outside the YAML front matter, the timestamps, and the console.log debug tag, and no prose parentheticals (the only parentheses are math notation for decibel units, slant ranges, and math symbols). Acronyms spelled out on first use, including NASA as the National Aeronautics and Space Administration, ESA as the European Space Agency, IEEE as the Institute of Electrical and Electronics Engineers, UHF as ultra high frequency, BPSK as Binary phase-shift keying, QPSK as Quadrature phase-shift keying, EIRP as effective isotropic radiated power, MAVEN as a NASA spacecraft name, DSOC as Deep Space Optical Communications, LCRD as Laser Communications Relay Demonstration, DSN as Deep Space Network (via link text), CCSDS as Consultative Committee for Space Data Systems, ITU as International Telecommunication Union, and FCC as Federal Communications Commission.

Numerical sanity checks confirmed across the link budget worked example with 49 dBi at 3-metre Ku-band dish, 40 dBi at 1-metre Ku-band dish, 205 decibel free-space path loss at 36,000 kilometres and 12 gigahertz, -89 dBm received signal, -119 dBm noise floor (corrected from -129 dBm during review), 11 decibel link margin, 280 kilohertz Doppler shift at 7 kilometres per second relative velocity and 12 gigahertz carrier, and 3 to 7 times 10 to the minus 5 fractional Doppler for Mars cruise.

URL spot check confirms all 25 unique URLs respond 200 except Iridium which returns 403 to curl as a known bot-detection block on the canonical iridium.com URL.

### Build Verification

The local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push. The system Jekyll-based rendering of the prior analog-facilities category articles confirmed under `future: true` in `_config.yml`, which permits the forward-dated post to render in the deploy build. The analog-facilities category permalink is `/aerospace/engineering/space-studies/analog-facilities/2026/07/01/communications_and_the_link_budget_for_off_grid_space_colonization_analogs.html`.

---

## Release Announcement

New Blog Post: Communications and the Link Budget for Off-Grid Space Colonization Analogs

The third per-subsystem deep-dive in the analog-facilities category follows A153 on electricity and A154 on water. The article treats the communications layer under the framing that the link budget is the architectural keystone for any radio frequency communications system, with antenna aperture, transmit power, modulation choice, forward error correction strength, and operating frequency all dimensioned against the required signal-to-noise margin. The article is explicitly designed to function as a general off-grid communications system guide with space-colonization as contextual flavour.

Key takeaways:
- The link budget is the architectural keystone analogous to the battery bank in electrical systems and the storage tank in water systems, with the Friis transmission equation, the free-space path loss, the Shannon-Hartley capacity bound, the effective isotropic radiated power, the gain-over-temperature figure of merit, and the link margin together determining whether the chosen architecture closes the link at the target data rate and error rate.
- The dependent components in order of dependency cover antennas spanning parabolic dishes through phased arrays, transmitters and power amplifiers, receivers and low-noise amplifiers, modems and forward error correction through LDPC and concatenated turbo codes, the networking layer under the Institute of Electrical and Electronics Engineers 802 standards, and the power supply and cooling considerations.
- The actual space mission can exercise options that the terrestrial analog cannot reproduce, including the NASA Deep Space Network at Goldstone Madrid and Canberra, the ESA Estrack network, the Mars Relay Network after the June 2026 MAVEN mission conclusion, the lunar relay constellation through LunaNet and ESA Moonlight, and the deep-space optical communications through DSOC with the primary mission concluded September 2025.
- The keystone framing breaks down at the solar conjunction blackout with the X-band 5 degree and Ka-band 2 to 3 degree Sun-Earth-Probe angle thresholds, at the entry-descent-landing plasma sheath, and at the deep outer solar system Voyager regime operating at 160 bits per second from over 24 billion kilometres. The engineering content generalises to residential cabin, remote research station, disaster relief, maritime vessel, and forward operating base contexts.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/space-studies/analog-facilities/2026/07/01/communications_and_the_link_budget_for_off_grid_space_colonization_analogs.html

#OffGrid #Communications #LinkBudget #DeepSpaceNetwork #Starlink #DSOC #LCRD #Doppler #SpaceComms #SpaceStudies

---

## Action Items for the Human Pilot

- Review A155 (published) for tone, accuracy, and completeness as the third per-subsystem deep-dive in the analog-facilities category.
- The article doubles as a general off-grid communications system guide that the space-colonization context flavours but does not constrain in applicability. Confirm this dual framing is correct for the intended audience.
- A155 is forward-dated to 2026-07-01 and is currently visible under `future: true` in `_config.yml` even though nothing references it. If invisibility until the date arrives is preferred, switch `future: false` on a per-deploy basis or hold the publish.
- The next available article number is A156, available for the next per-subsystem deep-dive. The previously proposed sequence places A156 at food production and closed ecological systems, then A157 habitat and physical operations, A158 waste and sewage, A159 garbage and transportation, with the Venus cloudtop buoyant analog as the closing A160 article.

---

## Notes

- Next available article number: A156.
- 0 release candidates from the analog-facilities category.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published through A155.
- A155 is the third per-subsystem deep-dive in the analog-facilities category following A153 (electricity) and A154 (water), treating the communications subsystem under the link-budget-as-keystone framing. The article explicitly functions as a general off-grid communications system guide that the space-colonization context flavours but does not constrain, with the link-budget reasoning, the dependent-component logic, the standards references, and the architecture choices applying without modification to residential off-grid cabin, remote research station, disaster relief installation, maritime vessel at extended range, and military forward operating base contexts.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack; `future: true` is enabled in `_config.yml` to permit forward-dated posts to render in the deploy build.
