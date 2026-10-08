# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-10-07
**Task**: **DECISION 5 REBUILT ARTICLE BY ARTICLE, DECISION 6 REPAIRED, AND THE KNOWN EXISTING DEFECTS FIXED.** Committed, NOT pushed, NOT published.

**DECISION 6, `c6112fa`.** All 48 wrong Open Library links in 18 published posts now point to the cited work. Each expected title and author surname was written out by hand from the citing sentence (`tmp/repair/ol_resolve.py`), and every new key was confirmed against its work record. Rolfe and Staples resolves to a 1986 work that lists Staples alone, and Zeihan's work title drops its leading article.

**DECISION 5, the survey filters, `15dbdbb`.**
- **15,469 off-topic records were removed from 62 articles**, taking the series from 286,913 research references to 271,444.
- **Ten early articles dropped nothing**, A297 to A301, A303, A306 and A310 to A312.
- **How each record was judged.** One agent per article read every screen candidate and a seeded sample of 300 unflagged records, and often every title. Each homonym found became a pattern that was swept through the whole survey. The drops, patterns and sample results are in `tmp/fix5/<ART>/`, and per-article results are in `tmp/fix5/PROGRESS.md`.
- **The tool spliced into the drafts and never reassembled them** (`tmp/fix5/survey_tool.py`). Each record was removed from its definition, its list lines and its citation runs. Cluster rows, tables and totals were recounted, and `tmp/fix5/check5.py` checks every article.
- **Generated citation lists inside sentences in A318 to A323** were spliced by ruling, since removing one listed work changes no claim. **Hand-chosen prose citations of off-topic works** in A302 to A317 were removed in a separate pass. Where a sentence made a false claim about the work it cited, that clause was removed, and each case is quoted in `tmp/fix5/PROGRESS.md`.
- **Every present-state survey number was recomputed, never matched**, from each article's own counting rule, reproduced first against the committed draft. Statements narrating a past pass were left as history. Each article's Source Base gained a paragraph dated 7 October 2026 recording the rebuild.
- **Contaminated prose rewritten from each article's own facts.** A344 had X-45 and X-46 text. A343 had X-45A text. A354 had X-56 flutter text, including a histogram that did not exist.
- **A365's 72 research links** had been written as the bare DTIC or NTRS host page. They now point to their DOIs or NTRS citations, recovered by rerunning the generator's own assignment.

**EXISTING DEFECTS FIXED**, each logged in `tmp/fix5/flagfix_log.jsonl`:
- A341: three orders of magnitude, six defects, twelve percent, and a named section.
- A339: four occasions, and two position references.
- A340, A351, A352, A357 and A364: position references.
- A360: a clause pointing to a pairwise test that does not exist, removed.
- A365: "fiveth" twice, and three lower-case sentence starts.
- A335, A342, A344 and A308: acronyms expanded.
- A363: capitals emphasis.
- A358: a count given in dollars.
- A362: the Reynolds range reconciled.
- A338: 2.6 was estimated, not measured, and a citation escaped.
- A337: the 13 percent attributed to scale.
- A350: three sweeps.
- A353: the gate named at its first use.
- A334: two landing sites, not three runways.
- A351: the shrinking-decade claim qualified.
- A361: grammar.

**GATES.**
- `_verify.py` reports 0 errors and 0 warnings.
- A build of all 72 changed drafts is clean, and the rendered audit has no findings.
- The A368 ledger has 70 records and 0 failed quotes. 219 quotations were relocated, and two were re-quoted with repair notes after A335's and A365's lines were corrected.
- `calc368.py` runs and `verify368.py` passes 1,845 checks.
- check5 prints RESULT PASS for all 72 articles.
- **Article verifiers.** Several dateline checks now skip only lines that name the 3 or 7 October 2026 repair date. A352's verifier was stripping the wrong citation form, and that is fixed.

**NOT FIXED, NEEDS THE PILOT OR A SOURCE.**
- A318 line 447 states 28.4 percent period against 34.9 percent contemporary, and no rule reproduces it.
- Several hand-written counts cannot be recomputed: A326's 365 and 108, A327's 268, A332's 175, 680 and forty-three, A346's 131, and A330's 1,692.
- A313 keeps two doubtful airborne-sensor works.
- `tmp/a365/refs365.py` still writes bare host URLs when a record has no DOI.
- The prose-citation agent started `verify_urls` by mistake. It sends network requests only and writes nothing to the drafts.

---

**Date**: 2026-10-07
**Task**: **THE PILOT'S SIX DECISIONS EXECUTED, EXCEPT DECISION 5'S REBUILD, WHICH STOPS AT ITS SCOPE REPORT. Committed, NOT pushed, NOT published.**

**DONE AND COMMITTED, NOT PUSHED, NOT PUBLISHED.**
- **Decision 1, `95dae6e`.** A297 now writes the assignment as a relation and asks four questions. The X-44 and X-42 fail the function condition. Injectivity fails at four pairs: X-11 and X-12, X-32 and X-35, X-46 and X-47, X-63 and X-64. Monotonicity fails once, the X-49A of 23 May 2003 after the X-50A of 13 February 2002, and the X-76 is a skip. There are two clusters. A368 no longer corrects A297. Its comparison table has ten rows, seven confirmed, and its errors section lists the two repaired aircraft-article errors.
- **Decision 2, `e59f20f`.** A364's and A365's Epistemic State each carry a dated note. It says the X-68A and X-76A rows first appeared in the public register between 15 January and 1 February 2026, and cites the three archived captures. A364's note adds that the X-67 skip is visible only through the X-68A row. A365's two sentences saying the row was readable at its date are corrected.
- **Decisions 3 and 4, `da1b458`.** **70 of 70 per-designation articles now carry every canonical section once, in canonical order**, with The Contemporary Literature before Where the Framing Breaks Down.
  - **43 articles changed**, A321 to A323 and A328 to A367.
  - **A Comparison With Ground Prediction section was written for each of the 33 lacking one.**
  - **Other missing sections were mapped first.** Where an article held the content under a topical heading, the heading was renamed or grouped under the canonical one. New prose was written only where content was absent, from each article's own facts and anchors.
  - **No existing prose line changed except these.** Position references that moves made false, now naming the section. The reduced-order sentences in A336, A349 and A364. A334's landing count, now seven, since OTV-8 is in orbit by the article's own table. A reworded duplicate in A353. A364's and A365's source counts, made stale by decision 2's three archive references.
  - **A368's ledger was relocated by verbatim search.** Three class quotations were re-quoted from the new sentences with dated notes, giving 763 quotations, 0 failed. `verify368.py` passes 1,845 checks.
  - **Article verifiers.** A359's, A363's and A364's verifiers were updated for the changes. The A349 and A350 verifiers' citation pattern predated the 3 October escape repair and is fixed.
- **Gates.** `_verify.py` 0 errors and 0 warnings. A build of all 44 changed drafts is clean, and the rendered audit has no findings.

**DECISION 6, OPEN LIBRARY. The recheck is complete and needs the pilot.**
- **All 567 works return 200 from the JSON record.** The HTML page now serves a `verify_human` challenge with status 200, so the check reads `/works/<key>.json` and compares the registry title and author with the citation.
- **48 definitions resolve to the wrong work. None is in the X-Planes series.** All are in PUBLISHED posts of the March 2026 economic-history series and the July 2026 computing and aerospace series. Examples: Etkin, Dynamics of Flight, resolves to The Silver Chair, and Hodges on Turing to a book on Ernst Cassirer.
- **Candidate keys were searched and none applied.** 29 candidates were found and 14 are unresolved, in `tmp/repair/ol_candidates.json`. The title and author rule is too weak for one-word titles, since Cameron's France and the Economic Development of Europe matched Summer in France. **Each candidate needs a human reading before a published post is edited.**

**DECISION 5, THE SURVEY FILTERS. Measured and stopped at the planned checkpoint.**
- **Scope.** There are 286,913 research references across the series, titled from the harvest caches, all but 748.
- **Two screens.** The union of the A367 and A368 refusal patterns flags 4,443. Absence of any aerospace or engineering vocabulary flags 15,616.
- **Neither screen is a verdict.** A sample of the refusal hits is about half clear homonyms, such as atrial flutter in the X-56 survey and a Venus plasma paper in the X-37 survey, and half on topic. The vocabulary screen flags the anomaly articles' deliberate cross-disciplinary clusters, such as look-alike drug names for the X-52, at 64 to 74 percent.
- **A rebuild therefore means a per-article reading of what each gate admitted.**
- **Worse, two surveys carry another article's prose, confirmed.** A344, the X-47, has literature cluster prose describing the X-45 and X-46. A354, the X-57, has gate and literature prose describing the X-56's flutter survey and a histogram it does not contain. **Survey prose may be contaminated elsewhere**, so the rebuild should regenerate prose from each article's own data and not only filter records.
- **Generators are out of step with their drafts** for at least A353 to A357, through the 3 October label repair and today's restructure. **A rebuild must splice into drafts, not reassemble wholesale.**

**EXISTING DEFECTS THE SECTION AGENTS FOUND, NOT EDITED, for the pilot.** The full list is in `tmp/fix6/QUEUE.md`. Examples:
- A337 states 4,655 records reaching the list out of 4,557 admitted.
- A341 says "four orders of magnitude" for a factor of a thousand.
- A365 has "fiveth" twice.
- Stale "survey below" references in A339, A340 and A351.
- A358's symbol table gives a count in dollars.
- A362 contradicts itself on the Reynolds range.
- A334 says "three runways", which the article does not support.

---

**Date**: 2026-10-07
**Task**: **HANDOFF REWRITTEN AND RESTAMPED at parent `6a74fc9`, with the pilot's six repair decisions slotted for execution after compaction. Nothing executed. Committed, NOT pushed.**

**THE PILOT'S DECISIONS, ALL SLOTTED, WITH EXECUTION PLANS IN `HANDOFF.md`.**
1. **Correct A297's three errors** (the backwards injectivity definition, monotonicity at the X-76, the third cluster) **and rewrite A368 as if A297 had always been right.**
2. **Add a small dated note to A364's and A365's Epistemic State** that their register rows were not public until January 2026.
3. **Write a `Comparison With Ground Prediction` section for each of the 33 articles lacking one**, A334 through A367 except A358.
4. **Give every article all canonical sections in the same order.** Measured: 43 of 70 per-designation articles need work, A321 through A323 and A328 through A367. Three interpretations are recorded for the pilot to confirm: article-specific sections stay, the opener and closer are exempt, and literature comes before framing.
5. **Rebuild each affected article's filter and regenerate its survey**, measuring the off-topic scope first.
6. **Recheck the 567 Open Library links slowly.**

**Correction to the previous report.** It said the ground-prediction section became a convention partway through the series. **It is the reverse**: A298 through A333 have it and A334 onward mostly do not.

**A third line published A377 in this tree, so the next available article number is A378.** `3d55f0b` reached the remote in that line's push. `6a74fc9` and this commit are unpushed. `_verify.py` reports 0 errors and 0 warnings across 305 posts.

---

**Date**: 2026-10-03
**Task**: **SERIES REPAIR, CITATION FORMAT COMPLETED. Committed, NOT pushed.** The five largest drafts, A340 through A344, held back from the repair commit pending proof, are now escaped, 55,515 citations. Each draft's HTML was rendered with the site's kramdown options before and after and is byte-identical, the slowest proof, A341, taking 4 hours 14 minutes because the unescaped original is the slow form. **All 22 drafts are now proved and escaped, 123,832 citations in all, and no X-Planes draft carries the unescaped form.** The five drafts then built fully together in 36 seconds and the rendered audit has no findings. `_verify.py` reports 0 errors and 0 warnings, the A368 ledger holds all 764 quotations, and `verify368.py` passes 1,827 checks.

Of three background watcher shells, one was stuck on a condition that matched its own command and one duplicated another, and both were stopped. A redundant sequential render of the X-46 was stopped as well. **The items needing the pilot are unchanged from the repair report below.**

---

**Date**: 2026-10-03
**Task**: **A377 PUBLISHED on the pilot's instruction, committed and PUSHED. The article is LIVE.**

**PUBLICATION.**
- **Path.** `_drafts/strategic_fragrance_application.markdown` moved by `git mv` to `_posts/2025-10-05-strategic_fragrance_application.markdown`. `_publish.sh` was not used, since it fails under BSD sed on this platform.
- **Address.** `/lifestyle/fragrance/war-gaming/2025/10/05/strategic_fragrance_application.html`.
- **The corpus is now 305 posts.**
- **The two-commit pattern was satisfied across the five passes.** The draft state in `_drafts/` was committed five times before the move, so this commit is the publication half.
- **Back-dated by a year**, so `future: false` does not apply and the post rendered on the first build rather than waiting for its date.
- **No `redirects/` entry is owed**, the URL being new rather than moved.
- **`lifestyle` and `fragrance` are new categories for the corpus.** Neither is shadowed. `sgeos/lifestyle`, `sgeos/fragrance` and `sgeos/war-gaming` all return 404 from the GitHub API, so no project pages take the path prefix. **Changing any category now moves the URL and owes a redirect.**

**THE OTHER LINE'S IN-FLIGHT WORK WAS ALREADY PUSHED.** `3d55f0b`, the X-Planes series repair, went up with the earlier A377 push on the pilot's decision to push master as it stood, and `git merge-base --is-ancestor` confirms it is on `origin/master`. The working tree was clean and nothing was unpushed when this publication began, so there was nothing further to push for that line.

**FINAL PUBLISHED STATE.** 7,748 lines, 45 display equations, 196 inline expressions, a 11-table apparatus and 2,612 reference definitions, of which 2,525 are the survey corpus. Verdict: the conventional three-spray and four-spray doctrines are **partially supported**.

**VERIFICATION BEFORE THE PUSH.** `./_check.sh` passed in full, being `_verify.py` at 0 errors and 0 warnings over 305 posts, a production build, and the rendered audit with no findings over 471 pages.

**RELEASE ANNOUNCEMENT, for the pilot to review before posting.**

```
New Blog Post: Strategic Fragrance Application Under the Three-Spray and Four-Spray Scenarios

Conventional advice tells you to put three or four sprays of fragrance on your pulse points, and
almost never says what that is meant to achieve, for whom, at what distance, or for how long. This
article treats the question as a planning problem, models how a dose becomes a concentration at
somebody else's nose, and adjudicates six ordinary scenarios against stated limits on detection,
collateral and overkill.

Key takeaways:
- The detection radius grows only as the square root of the spray count, so the fourth spray buys
  about fifteen percent more perceived intensity and under an hour of extra life.
- In a small shared office no spray count works at all, because past about twenty minutes the room
  rather than the wearer becomes the source, and everyone in it is a receiver.
- The wearer is the one receiver whose perception the application itself has degraded, so any plan
  that leaves reapplication to the wearer's judgement ends in overapplication.

You can read the full article here:
https://sgeos.github.io/lifestyle/fragrance/war-gaming/2025/10/05/strategic_fragrance_application.html

Let me know your thoughts. I would love to hear about where you have seen a plan fail because its
success measure was read off the least reliable instrument available!

hashtag#DecisionAnalysis hashtag#Modeling hashtag#AppliedScience hashtag#IndoorAirQuality
hashtag#Olfaction hashtag#Wargaming hashtag#TechnicalWriting
```

---

**Date**: 2026-10-03
**Task**: **A377 PATHOLOGICAL WORD USAGE PASS, a fifth pass on the pilot's instruction. Committed. NOT published.** The four numbered passes were pushed earlier at `3a46445`. No X-Planes file was touched.

**MEASUREMENT.** `_lib/diction.py` with `'_posts/*.markdown'` passed explicitly as the peer set, 260 to 304 published peers. **The default peer glob is the article's own directory**, which for a draft means comparing A377 against 72 X-Planes drafts written in the same stretch, and the style guide forbids exactly that.

**THE ENUMERATED TIC CLASS IS CLEAN.** 0 of 70 watched words at or above the peer maximum. `specific`, the word that caused the original corpus-wide problem, stands at 7 uses and 0.45 per thousand against a peer maximum of 15.07.

**THE 59 RELATIVE OUTLIERS ARE THE SUBJECT.** `fragrance` 117, `spray` 91, `dose` 58, `wearer` 53. No published peer is about fragrance, so each scores an unbounded ratio. This is the documented limitation of a relative check and not a finding.

**WHAT THE DISCOVERED-FORMULA CHECK FOUND, WHICH NOTHING ENUMERATED COULD SEE.**
- **`and found` opened eighteen sentences.** Eight rotated to observed, showed, recorded, reported, after which, with and which proved. Now 4, at 1.03 times the peer maximum.
- **`this article` 37 to 23.** Fourteen rewritten to name the referent, which is the better sentence: `the car calculation above`, `the transport section`, `the application plan`.
- **`rather than` 42 to 28**, rotated across and not, not, instead of, in place of.
- **`and colleagues on` four times in four consecutive lines** of one Epistemic State list, now first authors with one note that four have several.

**ONE EXEMPTION, DECIDED AND NOT EDITED.** `course of action`, 8 uses, 7.52 times the peer maximum. `collocate` reports a 100 percent top-collocate share with seven distinct content-word qualifiers, which is the style guide's term-of-art signature twice over, and the wargaming register was the pilot's instruction. **No `_verify_exemptions.yml` entry was added**, because `_verify.py` does not warn on it, its threshold being 5.0 per thousand against `course` at 0.51. An entry against a check that never fires is the noise that file exists to prevent.

**THE SUBSTITUTION CHECK CAUGHT THE PASS INSTALLING A FORMULA.** Diffing the formula list against the pre-pass state found `of the room` introduced at 4 uses by one of the `this article` rewrites. Reworded. **The diff is now clean in both directions, nothing introduced and nothing grown.** `and not` rose from 10 to 15 through the `rather than` rotation and is left at 0.95 against a peer maximum of 2.82, recorded in `tmp/a377/findings.md` as the one number to re-measure next pass rather than assume.

**A SAFEGUARD STOPPED THIS PASS TWICE AND NO WORK WAS LOST.** Every edit was applied by script to the article before the turn narrated anything, so both turns lost only narration. **Logged in `WORK_DURABILITY.md` as a second incident**, whose common factor with the A365 one is a long passage bound for the channel and not the subject, a diction report being by construction a list of fragments of the author's own prose stripped of context. The entry says a diction pass is among the most exposed passes in the workflow, which was not obvious in advance.

**VERIFICATION.** `_verify.py` 0 errors 0 warnings. `verify377.py` 0 failures. Prose rules clean. `lint.py` clean. 45 of 45 displays render and the render audit reports no findings. 7,748 lines, 2,612 references.

**STILL NOT PUBLISHED, AND THAT REMAINS A PILOT DECISION.**

---

**Date**: 2026-10-03
**Task**: **A377 PUBLICATION REVIEW, the fourth and last of four passes. Committed, NOT published.** **Push status is a pilot decision, recorded below.** No X-Planes file was touched.

**THE NEW REQUIREMENT AND HOW IT WAS MET.** The pilot asked that the article serve as a comprehensive survey and review of the contemporary literature, with no length or reference limit.
- **Harvest.** 115 Crossref queries returned 15,061 distinct records.
- **Gate.** The title gate is written for this subject, with keep and refuse guard titles that it passes hyphenated and unhyphenated. It was tuned against seeded random samples of both kept and dropped records, seeds 20261003, 7741 and 31415, each read.
  - **Too permissive** at first. It admitted plant furocoumarin chemistry, mouse and gerbil chemosignals, fly and fish olfaction, car-park carbon monoxide, antenna near-field transforms, outdoor terpene–ozone chemistry, microbial skatole, questionnaire translations and retail coupon listings.
  - **Too narrow** at first. It dropped bare perfume titles, flavour-and-fragrance analysis and two-zone exposure models.
- **Excluded by design, and the article says so.** Coronavirus smell loss, environmental odour nuisance, electronic noses and food flavour.
- **Result.** 2,541 works in sixteen clusters, median year 2014, 47.7 percent from 2015, 518 before 2000, and 100 dated 2026, which postdate the editorial date. **All 2,541 are cited in cluster rows.**
- **Read for the prose.** 77 selected works had their abstracts fetched. 59 are discussed, of which five are named by title only.

**WHAT THE SURVEY CHANGED IN THE ARTICLE.**
- **Adaptation timing.** Pierce and Simons 2018 and Hintschich 2024 show significant adaptation at five and ten minutes, which brackets the assumed time constant.
- **The wearer's own nose.** **Beekman 2022 measured perfume degrading its wearer's threshold and discrimination**, which is direct evidence for the article's central restraint.
- **Differences between wearers.** Hadjiefstathiou 2025 attaches between-wearer evaporation differences to skin, not sex, so H3 stands with a qualification.
- **Exposure models.** The two-zone near-field and far-field model is standard in occupational hygiene and cosmetic spray exposure.
- **Thermal plume.** It carries floor-level material up at up to four times the ambient concentration.
- **Spray inhalation.** Pump sprays release about 0.5 percent respirable droplets.
- **Three gaps, stated in the conclusion.** No study measures detection by others as a function of spray count, compares body application points, or tests the advice on distance, rubbing or moisturising.

**OTHER REVIEW FIXES.**
- **Acronyms.** ASPCA and NIOSH were used before being spelled out, and EDEN and QRA were never expanded.
- **Chanel's advice.** Its advice to apply to garment linings was added; the advice was confirmed through its search listing because the page returns 403.
- **Diction.** The formula "could not be retrieved", at 2.5 times the corpus maximum, was rotated, and one garbled sentence was rewritten.
- **Display text.** 25 duplicated display texts in the survey were disambiguated.

**VERIFICATION.**
- **Survey statistics.** Every stated survey statistic recomputes through `_lib/survey.py`, and all 16 rows pass the row-count gate.
- **Link text.** Survey link text matches the registry display everywhere.
- **Identifiers.** 250 of 250 seeded-sample DOIs resolve, and all 35 hand-cited DOIs resolve.
- **Non-DOI URLs.** These return 200, apart from documented bot responses from Chanel, NIOSH, the Met (429), the CDC secondary page (307 loop) and EUR-Lex (202).
- **Rendering.** 45 of 45 displays render, the render audit is clean, `_verify.py` reports 0 errors and 0 warnings, and `verify377.py` reports 0 failures. The page weighs about 915 KB.

**PUSH, A PILOT DECISION.** **The X-Planes line committed `3d55f0b` on top of A377's third pass, marked NOT pushed, with some proofs still running.** It changes `_verify.py`, which CI runs. Pushing master pushes it, so A377 was not pushed without the pilot deciding.

---

**Date**: 2026-10-03
**Task**: **SERIES REPAIR on the pilot's instruction to address every repair that can be completed without input. Committed, NOT pushed, NOT published.**

**REPAIRED, EACH CHECKED AGAINST A SOURCE OR A GATE.**
- **A302, X-5.** The paragraph of X-4 history is replaced with the X-5's record from Hallion's NASA history of Dryden, read in full: the contractor programme ended in October 1951, the Air Force flew a six-flight evaluation in December 1951, and the NACA flew 133 flights from 1952 to late 1955, while the second aircraft was flown only by Bell and the Air Force. The unsupported Yeager mention and its now-uncited definition were removed, and Hallion 1984 was added as a research reference.
- **A346, X-49.** The allocation is redated from 2004 to the register's 23 May 2003 in all three places. The 2004 transfer to the Army is kept as a separate event, and the register is added as a cited primary.
- **A350.** The duplicated `## The Contemporary Literature` heading is removed.
- **A324.** `book_jenkins` now reads "Dennis R. Jenkins 2000, Hypersonics Before the Shuttle", verified against the Open Library work.
- **Related-post lists.** A356 and A357, 116 entries showing raw anchor slugs, and A365 through A368, 278 entries showing `a297 framing`-style labels, now carry article titles from each target's front matter. The A367 and A368 assemblers build them that way.
- **A367's literature filter.** The `S + r"?"` construction, which demanded a separator where it meant an optional one, is fixed. The filter admits 172 more records, 76 of them propfan and turboprop work, which took the propeller cluster from 146 to 222. It now removes 16 quadrotor titles, and two newly exposed homonyms, Toray T700 carbon fibre and planar VTOL, became refusal cases.
  - **A367's report-server names** are trimmed to surnames.
  - **A367 now has 8,588 lines and 3,882 definitions.** Its survey figures are regenerated, the Source Base records the repair with its figures, and `verify367.py` runs 578 checks with all mutations caught.
- **A352 through A355.** Their literature rows now open with a bold count, 56 rows, and A352's and A355's tables were checked against their runs and agree.
- **The corpus row rule widened.** `_verify.py` and `_lib/survey.py` accepted only `records`, so the `works` rows of A365 through A368, and now A352 through A355, were never gated. A planted wrong count passed before the change and is caught after it. `test_lib.py` passes 125 of 125.
- **A335 and A337.** Each had a duplicated subsection heading, a systems subsection repeated in the literature, and the literature copies are renamed "... in the Literature".
- **Citation link text, series-wide.** 14 repeated trailing years such as "Pole, 1946 1946" and 38 en and em dashes in link text were fixed, link text being prose under the house rules.
- **A368.** Its error section now reports the A302 and A346 errors as repaired. The ledger quotations those repairs moved were relocated by verbatim search, none edited, and `verify368.py` asserts the repairs are in place.
- **Citation format: 17 of 22 drafts escaped**, 68,317 citations changed from `[[text][anchor]]` to `\[[text][anchor]\]`, each draft's HTML rendered with the site's kramdown options before and after and proved byte-identical, the slowest proof taking 41 minutes. The five largest, A340 through A344, stay unescaped until their comparisons, still running after up to two hours, finish. All 35 changed drafts were built fully together in 46 seconds and the rendered audit has no findings.

**NEEDS THE PILOT, WITH THE OBVIOUS OPTIONS.**
- **A297's errors**, the backwards definition of injectivity, monotonicity placed at the X-76, and a predicted third cluster. Option one: leave A297 as it is, so that A368 corrects it and A368's comparison stays true. Option two: correct A297 with a pointer to A368, which then means rewording A368's comparison as a record of what A297 first said.
- **A364 and A365 Epistemic State.** Option one: add a dated statement that their register rows were not public until January 2026. Option two: leave them, since A366 and A368 state it.
- **33 articles have no `## Comparison With Ground Prediction` section**, which became a series convention partway through. Option one: leave them and exempt the early articles in the checker. Option two: write the section for each, which is new content. Option three: add a short section to each saying what flight returned against prediction, where the article already says it.
- **Six articles break the expected section order**, A351 through A354 with the Source Base early and A336 and A359 differently. Option one: move each Source Base to sit before Epistemic State. Option two: leave them, since A336's reduced order is deliberate.
- **The older literature surveys have off-topic records**, titles such as "soil-machine system" and "Even-Even Nuclei" in A323 through A336. Option one: rebuild each gate and regenerate its survey prose. Option two: remove the off-topic records and their counts by hand. Option three: leave them and state it.
- **The Open Library links are unresolved.** 192 of 567 returned 200 before the server refused connections, which looks like rate limiting. Option one: recheck slowly later. Option two: accept them as they are.
- **The handoff** carries stale text, the X-49's 2004 date and the late-series ordering claim, and needs a rewrite and restamp, which the pilot's handoff prompt governs.

**VERIFICATION.** `_verify.py` reports 0 errors and 0 warnings across 304 posts. `verify367.py` runs 578 checks and `verify368.py` 1,827, all passing. The A367 stub build is clean, `_lib/render.py` has no findings, and all 40 of A367's displays match.

---

**Date**: 2026-10-03
**Task**: **A377 PRIMARY-REFERENCE REVIEW, the third of four passes. Committed, NOT pushed, NOT published.** No X-Planes file was touched.

**FINAL STATE.**
- **References.** 74 to 87, being 37 research works, 9 primary documents, 3 books, 17 encyclopedic references, 11 guidance pages, 5 history sources, 3 commentary pieces and 2 data sources.
- **Size.** Lines 2,104 to 2,204. Display equations hold at 45.

**ADDED, AND HOW EACH WAS READ.**
- **Read in full or in the relevant passage.**
  - Rimmel's *Book of Perfumes* (1865), from the Cornell scan on the Internet Archive, for eau de Cologne as citrus water and for kyphi at sunset.
  - Plutarch on kyphi's sixteen ingredients.
  - The 1900 DeVilbiss atomizer patent record.
  - An EPA-registered bear spray label, Counter Assault 55541-2, at 2.0 percent capsaicinoids.
  - The Access Board's fragrance-free recommendation, which partly answers the CDC policy surviving only secondhand.
- **Read in abstract.**
  - **Dalton and Wysocki 1996.** Two weeks of home exposure raised thresholds that stayed raised for up to two weeks. This turns the article's claim of across-days adaptation from assertion into measurement.
  - **Zaynoun 1977.** Phototoxicity depends on the ethanol vehicle and the skin site.
  - **Api 2020.** The QRA2 aggregate-exposure revision.
- **Cited for their titles alone.** Clapeyron in its 1843 translation, Clausius 1850, and Whissell-Buechy and Amoore 1973. The article claims nothing beyond what those titles state.
- **Hall 1966** is now the source for the proxemic zones, and Wikipedia's ethanol article for the density.

**NOT FOUND.** No retrievable primary for the Gaussian plume, since Turner's workbook could not be obtained, for Tapputi, or for the CDC 2009 policy text. The article says so.

**VERIFICATION.**
- Every new URL returns 200, except three Wiley DOIs that return 403 to the fetcher and are confirmed in Crossref.
- `_verify.py` reports 0 errors and 0 warnings.
- `verify377.py` reports 0 failures.
- The scratch production build and render audit are clean.

**THE NEXT PASS IS THE PUBLICATION REVIEW.**

---

**Date**: 2026-10-03
**Task**: **A377 EQUATION-DENSITY REVIEW, the second of four passes. Committed, NOT pushed, NOT published.** No X-Planes file was touched.

**FINAL STATE.**
- **Mathematics.** Display equations **17 to 45** and inline expressions 119 to 195. Every new display has its symbols defined before it and a worked example after it.
- **Size.** Lines 1,807 to 2,104 and H3 sections 39 to 43.
- **References.** 73 to 74. Kimber, Dearman and Basketter 2008 was added to support the claim that dose per unit area drives sensitisation, which was checked against the abstract.

**BEST NEW RESULTS.**
- **The room-regime number contains no dose.** Its value is pi u a squared r squared divided by V times the quantity lambda minus one over tau. Above one the room is the source, and no spray count changes that. It is 5.09 for the shared office, which the model's room-to-plume ratio approaches as 4.74 at four hours and 5.06 at eight, 0.12 for open plan and 0.048 at dinner. This makes the doctrine's "check the room before the wearer" rule exact.
- **Distance alone bounds selectivity.** With collateral held at 0.2, intended detection cannot exceed 0.75 in the offices or 0.93 at dinner at any dose.
- **Each spray buys less time than the last.** The added detection life is tau times the log of N plus one over N, about 125 minutes for the second spray and 52 for the fourth.
- **Doubling the spray distance quarters the areal dose**, which gives the conventional distance advice a sensitisation rationale it does not usually state.

**WHAT VERIFICATION CAUGHT.**
- **One display equation rendered as inline math** because no blank line followed its closing delimiter. **`_verify.py`, which has a display-demotion check, and `_lib/render.py` both passed it.** A comparison of source displays against rendered `\[` blocks found it, and all 45 now render. **This is a gap in the corpus tooling worth a pilot decision.**
- **"is as follows" reached the corpus maximum** after three new introductions used it. Those three were reworded, and the phrase now appears five times.

**VERIFICATION.**
- `tmp/a377/verify377.py` now also checks every new worked number, with 0 failures.
- `_verify.py` reports 0 errors and 0 warnings, and the scratch production build renders clean.

---

**Date**: 2026-10-03
**Task**: **A377 DRAFTED, *Strategic Fragrance Application Under the Three-Spray and Four-Spray Scenarios*, the first of four passes. Committed, NOT pushed, NOT published.** This is a second line, independent of the X-Planes line, and it touched no X-Planes file.

**FINAL STATE OF THE DRAFTING PASS.**
- **File.** `_drafts/strategic_fragrance_application.markdown`, editorial date 2025-10-05, categories `lifestyle fragrance war-gaming`, standalone.
- **Size.** 1,807 lines, about 10,200 words of author prose, 21 H2 and 39 H3 sections, 11 tables.
- **Mathematics.** 17 display equations and 119 inline expressions, each display preceded by its symbol definitions and followed by a worked example.
- **References.** 73 definitions. All 28 DOIs were checked against Crossref, which corrected three titles the research agent had supplied.

**THE ADJUDICATION.** The hypothesis that the conventional three-spray and four-spray doctrines are sound is **partially supported**.
- **Dose.** The smallest adequate eau de parfum dose is one spray for dinner and the interview, none in a small shared office, five as a single application in an open-plan office, and six outdoors. **Four sprays split three and one match the single five.**
- **Placement.** The conventional points survive on geometry rather than pulse. The sternum and nape are the best points, and the wrist is the weakest.
- **Wearer.** Every men-versus-women difference with a physical basis resolves to clothing or hair.

**WHAT VERIFICATION CAUGHT.**
- **The main adjudication table was missing from the assembled draft.** A substitution ran its generator from the wrong directory and inserted an empty string. The recomputation harness found it by failing on every table cell, and it was repaired before commit.
- **A research agent attributed a 1979 cosmetic-chemistry paper to Berglund.** It is by Moskowitz, Chandler, Moldawer and Laterra, and the claimed exponent range was not on the page. Both were corrected from the page itself.

**VERIFICATION.**
- `tmp/a377/verify377.py` recomputes every worked number and table cell, with 0 failures.
- `_verify.py` reports 0 errors and 0 warnings across 304 posts and the drafts. **That run used the working-tree `_verify.py`, which carries uncommitted modifications that are not mine.**
- A production build in a scratch copy with A377 placed as a post succeeds, and `_lib/render.py` reports no findings over 471 pages.
- **Not done.** Full-text reading of sources marked snippet-only, and a URL sweep.

**PILOT DECISIONS.**
- **Categories.** `lifestyle fragrance war-gaming` is still the placeholder the pilot accepted. `lifestyle` and `fragrance` are new categories. The category `humor` exists in the corpus and was deliberately not used.
- **Uncommitted work not mine.** `_lib/survey.py`, `_verify.py` and 27 X-Planes drafts carry uncommitted modifications that predate this session's edits, presumably the X-Planes line's. **They were left untouched and are not in this commit.**

---

**Date**: 2026-10-03
**Task**: **A368 PUBLICATION REVIEW, the fourth and last of four passes. Committed and PUSHED on the pilot's instruction, NOT published.** **All seventy-two X-Planes articles now have all four passes complete.**

**FINAL STATE.**
- **Size.** 11,394 lines and 67,108 words, of which about 14,400 are prose outside the citation runs.
- **Mathematics.** 45 display equations, 103 inline expressions and a 40-entry symbol table.
- **References.** 5,348 reference definitions: 36 primaries, 5,241 research works and 71 related posts. Of the research works, 46 are hand-chosen primaries read for their abstracts, and 1,580 of the 5,195 swept works are report-server records, 30.4 percent.
- **Structure.** 21 H2 and 33 H3 sections with 12 tables.
- **Survey pool.** 17,869 records, of which 5,657 were admitted to 12 clusters.

**THE LITERATURE REVIEW NOW DISCUSSES EVERY CLUSTER BY CONTENT, AS THE STANDING DIRECTIVE ASKS.** Four paragraphs were added, each written from abstracts fetched for this pass.
- **Vertical flight.** A 2026 study calls the tiltrotor conversion one of the most complex and hazardous aspects of tiltrotor operation. The whirl-flutter testbed is still producing validation data. A swept-tip proprotor tested to 200 knots found analysis predicting stability trends but not torsion. These are the limits the X-76 stops its rotor to avoid. NASA's newest vertical-flight research aircraft is presented as RAVEN rather than as an X number.
- **Institutions.** NASA's 2021 sustainable-aviation overview describes the most substantial change since jet engines and swept wings converged, which is the programme behind the X-66. The National Research Council assessments are cited for their titles.
- **Engineering history.** Loftin's configuration history and Henderson and Huff's history of jet-noise research are discussed as the literature's nearest longitudinal views.
- **The report literature.** Dryden's 2007 bibliography of nearly 2,900 reports from 1946 to 2006 is now part of the review.

The Dryden histories by Hallion and Wallace are now discussed from their abstracts instead of their titles.

**FIXES.**
- **A self-contradiction.** "No skip was an accident of bookkeeping" contradicted the article's own point that the 58 and 67 followed from the rule.
- **Two claims rescoped.** "The founding-year number's first descendant" was unverifiable, and "no work in the survey treats the designation sequence" overstated a check that was made on titles only.
- **Gate-bug wording.** The gate-bug sentence overstated what the defect had excluded.
- **Acronyms.** NASA was used before it was spelled out, and MANTA was not expanded.
- **Vantage point.** The Epistemic State now says the survey's 2026 works postdate the article's date.

`verify368.py` asserts every one of these, together with every new abstract claim.

**VERIFICATION.**
- **`verify368.py` runs 1,821 checks with 0 failures**, and all planted mutations across the four passes were caught.
- `_verify.py` reports 0 errors and 0 warnings, and the series checker, the style check and the symbol check are all clean.
- The stub build is clean, `_lib/render.py` has no findings, all 45 displays match, and no inline span carries an emphasis tag.

**PUSHED, NOT PUBLISHED.** The pilot decisions still open are:
- the misplaced X-4 paragraph in A302;
- the X-49 date in A346;
- the separator bug in A367's gate, which affects 203 admission decisions, and its untrimmed author names;
- the Epistemic State sections of A364 and A365.

**The series is complete in draft. Publication has never been authorised.**

---

**Date**: 2026-10-03
**Task**: **A368 PRIMARY-REFERENCE REVIEW, the third of four passes. Committed, NOT pushed, NOT published.**
- **Counts.** Reference primaries rose from **11 to 36** and definitions from 5,323 to 5,348; research works hold at 5,241, of which 46 are hand primaries. Lines went from 11,340 to 11,390, and display equations hold at 45.
- **Sources read.** Every new primary was read from a saved copy or verified by title through Crossref.
- **Verifier.** It now asserts each new primary statement verbatim in its saved source. `verify368.py` runs **1,799 checks with 0 failures**.

**LARGEST YIELD: THE ALLOCATION PROCEDURE ITSELF EXPLAINS A CHOSEN NUMBER.** The register compiler's account of the allocation steps states three things:
- a written request must include a suggestion for the new designation;
- a number can be requested "when the requester particularly likes" it;
- the control point's recommendation "may or may not be identical to the one proposed", with the final decision at Air Force headquarters.

**A chosen number is therefore a suggestion the deciding office accepted**, and the article now says so, citing the procedure rather than inferring it.

**SECOND YIELD: AN INDEPENDENT CHECK ON THE CREW CODING.** The compiler's appendix of unmanned military X-planes lists 19 research numbers. **The ledger codes 17 of them uncrewed, none crewed, and leaves only the X-41 and X-51 unstated**, and it codes all four NASA-only uncrewed vehicles uncrewed. Reading the two unstated vehicles as the appendix does would strengthen the crewed-share result.

**THIRD: THE X-50 REQUESTER IS RECONCILED.** The compiler's directory entry says the 50 was assigned "at the request of Boeing and DARPA" for a "50/50 mix of helicopter and fixed-wing aircraft". The register's note names DARPA and Boeing's programme manager named Boeing, so all three accounts are now stated together.

**ADDED.**
- **Register and procedure.** The missing-designations page, for the X-39, X-52, X-58 and X-67 in the compiler's words, and the allocation-procedure page.
- **The 1951 fold.** The compiler's X-9 and X-10 pages, giving the RTV-A redesignations of 1951.
- **The register lag.** The 15 January 2026 register capture, which is the lag's lower bound. I checked that the saved capture has neither row and the 1 February capture both.
- **Flight dates and award record.** NASA's X-53 fact sheet, dating the last flights to March 2005, and the federal award record for the X-62 figures.
- **Programme documents.** The Air Force Research Laboratory's ARISE fact sheet.
- **Founding-year numbers.** The F-47 public affairs correspondence and Bell's X-76 release. The F-47 is now stated with its three official meanings rather than as a founding-year number alone.
- **Legislation and editions.** The National Aeronautics and Space Act of 1958 for the dissemination clause, the 1998 edition of the official list, and the compiler's unmanned appendix.
- **Statistical-method originals.** Eleven original method papers, each verified by title: Kendall 1938, Wilson 1927, Fisher 1922, 1935 and 1950, Cochran 1954, Woolf 1955, Shannon 1948, Pielou 1966, Dunn 1961, and Fleiss, Tytun and Ury 1980.
- **Dryden histories.** The flight research centre's histories, already in the swept survey, are now discussed in the review and cited for their titles.

**ADDRESSES.** All 36 primary addresses were requested. 29 return 200. Two `.mil` pages return 403, as is usual for that domain. Five publisher DOIs return 403 or 202, and each of those was verified by title through Crossref.

**VERIFICATION.**
- `_verify.py` reports 0 errors and 0 warnings, and the series checker, the style check and the symbol check are all clean.
- The stub build is clean, `_lib/render.py` has no findings, and all 45 displays match.

**NOT PUSHED.** The decisions on A302, A346, A367 and the A364/A365 Epistemic State sections are still the pilot's.

---

**Date**: 2026-10-03
**Task**: **A368 EQUATION-DENSITY REVIEW, the second of four passes. Committed, NOT pushed, NOT published.** Display equations **18 to 45**, inline expressions 87 to 103, the symbol table 32 to 40 entries, lines 11,220 to 11,340, references held at 5,323. `eqscan.py` listed the prose lines carrying figures with no display nearby, and every figure that a relation produced now has its relation shown. All values come from `eqpass368.py`, which reads only counts and dates already in the ledger, the register and the draft.

**BEST NEW RESULT: AN IDENTITY OVER THE POINTER WALK THAT GIVES THE SKIPPED NUMBERS A SECOND ROUTE.** The positive parts of the advances telescope to the span of the walk, 76 minus 44, which is 32. The numbers passed over, 11, less the one backfill, the X-49, give 10 numbers permanently skipped in the register era. That equals the direct count of numbers from 44 to 76 with no research row: the 52, 58, 67 and 69 through 75. **The two routes could have disagreed and do not.**

**OTHER ADDITIONS.**
- **Crew.** The difference in crewed share is 0.462. The odds ratio is 7.46 with a Woolf interval of 2.28 to 24.4, and among aircraft it is 34.0, with an interval of 3.72 to 310 that is wide because the X-10 alone fills the early uncrewed cell.
- **Fisher's test.** The two-sided summation rule and the Bonferroni product are displayed: 7 times 0.00109 is 0.0077.
- **Clustering.** The P1 dispersion is now displayed, together with the closed-form chi-square tail for even degrees of freedom, which the verifier uses as its second route.
- **Sponsors.** A worked 1950s entropy of 1.12 bits is shown, with an evenness measure that makes the 1950s the least even decade, 0.704 against 0.937 for the 2000s.
- **Shares with Wilson intervals.** Measurement is 0.385, between 0.276 and 0.506, which is the sense of "about two fifths". Ended unflown is 15 of 65. Designated after flight is 5 of 20. Mixed among comparisons that reached flight data is 20 of 27, with an interval excluding one half.
- **Totality.** The unassigned set is decomposed 1 plus 1 plus 2 plus 7, and the share is 0.842 if the X-23 is counted as unassigned.
- **Kendall pair accounting.** 250 plus 1 plus 2 equals 253.
- **Register lag.** The lag is bounded at 148 to 165 days for the X-68A and 87 to 104 days for the X-76A, so the register published each row three to five months after allocation.
- **Other values.** The founding-year span is 329 days, the drone out-of-sequence share 9 of 69, the officiality sum and official share 21 of 31, the flown shares 47 of 76 and 47 of 65, the power inputs, and the first article's X-1 information of 4.32 bits.

**VERIFICATION.**
- **`verify368.py` runs 1,750 checks with 0 failures.** Each new display is recomputed by a second route: the walk identity by telescoping and by direct gap count, the 1950s entropy by recounting sponsor classes from the ledger, Woolf by direct formula, Wilson by the quadratic's roots, and the lags from the archive dates. Five further planted mutations of new displays were all caught.
- **The other gates are clean.** Style has 0 findings and the symbol check passes, after two designation subscripts were moved inside text. `_verify.py` reports 0 errors and 0 warnings. The stub build is clean, `_lib/render.py` has no findings, all 45 displays match, and no inline span carries an emphasis tag.

**NOT PUSHED.** The defects reported in the drafting pass in A302, A346 and A367 still await the pilot, as does the A364 and A365 Epistemic State decision.

---

**Date**: 2026-10-03
**Task**: **A368 DRAFTED, *X-Planes: Synthesis and What the Designation Became*, the first of four passes. Committed, NOT pushed, NOT published.** **Seventy-two of seventy-two drafted**, so every article in the series now exists. `_drafts/x_planes_synthesis_what_designation_became.markdown`, editorial date 2025-12-16, series index 72. **11,220 lines, 64,324 words of which about 12,000 are prose outside the citation runs and reference lists, 18 display equations, 87 inline expressions, a 32-entry symbol table and 5,323 reference definitions**, being 11 primaries, 5,241 research works of which 46 are hand-chosen primaries read for their abstracts and 1,580 of the 5,195 swept works are report-server records at 30.4 percent, and 71 related posts, in 21 H2 and 33 H3 sections with 12 tables, from a pool of 17,869 with 5,657 admitted to 12 clusters.

**THE METHOD IS NEW TO THE SERIES. THE SEVENTY EARLIER ARTICLES WERE READ AS DATA.** Ten parallel extractors each read seven articles and wrote one record per article: contractor, sponsors, designation date, first and last flight, outcome, crew, vehicle kind, keystone and its class, the ground-comparison verdict and the reason a vehicle never flew. **Every stated value carries a line number and a verbatim quotation, and all 764 quotations were checked by script against the drafts, with none failing.** Twenty-one further coding decisions carry their own checked quotations. `calc368.py` counts over the ledger and the register. `verify368.py` recomputes everything by second routes: Fisher by exact integers, chi-square by the even-degrees closed form, Kendall by inversions over a different register parser, and Wilson by the quadratic's roots. **It runs 1,714 checks with 0 failures, and 15 planted mutations were all caught**, the last two only after the verifier was changed to check every occurrence of a repeated figure.

**FINDINGS.**
- **Crew.** The crewed share of vehicles fell from 19 of 27 before 1990 to 7 of 29 after (Fisher 0.00109). Among aircraft alone it fell from 17 of 18 to 7 of 21 (0.00016). With the eight unstated crews assigned against the finding, the probabilities are 0.044 and 0.0062.
- **Purpose.** The measurement share fell from 48.3 to 31.4 percent, with Fisher at 0.204, so **the first article's prediction of rising non-informational purpose is not established**. About 131 vehicles per period would be needed.
- **Order.** Over the register-dated numbers Kendall's tau is 0.984, with **one inversion, the X-49 after the X-50**.
- **Skips.** Every skip in the register era has a recorded cause. Two are numerology (50 and 76), one a refusal (53) and two were taken by the drone series (59 and 68). The share of advances equal to one is 16 of 22.
- **Clustering.** The index of dispersion by decade is 2.90 to 3.18 (p 0.0013 to 0.0031). **There is no third cluster in the 2010s and 2020s**, which the first article predicted.
- **Designated after flight.** Five of the 20 flown vehicles with both dates were designated after their first flight, the earliest the X-9 of 1951.
- **Ground comparison.** No article records flight contradicting ground prediction outright, and 20 of 47 are mixed.
- **Founding-year numbers.** The register note for the YFQ-48A says its number follows the F-47.

**THE FIRST ARTICLE IS CORRECTED IN PLACE IN THIS ONE, NOT EDITED.**
- **Injectivity.** A297 defines injectivity backwards. The X-44 is a failure of the assignment to be a function, and injectivity fails at four pairs: X-11 and X-12, X-32 and X-35, X-46 and X-47, X-63 and X-64.
- **Monotonicity.** A297's claim that monotonicity fails at the X-76 is wrong. The X-76 is a skip.
- **The third cluster** it predicted is absent.

**THE OPENING CHECK RAN AT THE END OF DRAFTING AND FOUND NINE OVERCLAIMS, ALL CORRECTED AND ASSERTED ABSENT.** Among them:
- "became a choice of symbol", when two of 76 numbers were chosen.
- "record outcomes as often as they authorise attempts", from 5 of 20.
- "the government stopped describing its research aircraft in public", when only the register's official descriptions stopped.
- "usually bought by a laboratory", which was never measured.
- "in every period".
- Two sentences citing the internal handoff notes.

**FOUR THINGS FOUND IN PUSHED ARTICLES, REPORTED AND NOT REPAIRED.**
- **A302 contains a misplaced X-4 paragraph.** Its line 554 gives the X-4's first-airframe ten flights, the "lemon" remark, the second airframe's twenty contractor flights and the February 1950 handover, while A302 dates the X-5's first flights to 1951 and A301 carries the same X-4 details.
- **A346 dates the filling of the X-49 vacancy to 2004**, while the register dates the X-49A to 23 May 2003.
- **A367's gate had an optional-separator bug.** `S + r"?"` makes a lazy one-or-more, not an optional separator, so unhyphenated compounds such as `propfan` were never matched. Run on A367's own pool, the intended gate changes 203 of 12,957 admission decisions. No other article's gate contains the construction.
- **A367's report-server names are untrimmed.** Its surname parser kept full names for newer records of the form First Last, so its link texts read `Benjamin M Simmons 2026`. A368's parser trims them, including a suffix after a comma.

**ONE MEASUREMENT WAS ABANDONED AND THE ARTICLE SAYS SO.** A title count of report-server records per designation, meant to test the thinning after 2000, failed for three reasons. X-ray sources such as Cyg X-1 swamp the X-1, the server tokenises `X-43` and `X-43A` differently, and the X-24 returned zero title matches in its first 100. No number from it appears in the article.

**VERIFICATION.**
- `_verify.py` reports 0 errors and the 2 expected `progress-stale` warnings, which this update clears. The series checker, the style check and the symbol check are all clean.
- The stub build took 16 seconds, `_lib/render.py` has no findings, all 18 displays match, and no inline span carries an emphasis tag.

**NOT PUSHED.** The pilot decision on A364's and A365's Epistemic State sections is still open. **The four defects above need the pilot's decision before anyone edits those articles.**

---

**Date**: 2026-10-03
**Task**: **A367 PUBLICATION REVIEW, the fourth and last of four passes. Committed and PUSHED, NOT
published.** Seventy-one of seventy-two drafted. **Final state 8,298 lines, 55,686 words, 40 display equations, 95 inline expressions, a 51-entry symbol table and 3,737 reference definitions**, being 66 primaries, 3,601 research works of which 17 are hand-chosen primaries with abstracts and 616 of the 3,584 swept works are report-server records at 17.2 percent, and 70 related posts, in 16 H2 and 55 H3 sections with 6 tables, from a pool of 12,957.

**THE LITERATURE SECTION MAPPED THE FIELD BUT DID NOT REVIEW IT, AND THE STANDING DIRECTIVE ASKS FOR A REVIEW.** A new subsection, "What the Literature Establishes, and Where It Is Moving", is written from abstracts fetched for this pass. It makes four points and records one silence.

- **The stopped-rotor revival is divided.** Brown and Ahuja keep the rotor as a cruise lifting surface, while the X-76 removes it.
- **Whirl flutter is the most active experimental subject in the survey.** The Maryland rig is flutter-free to 200 kt but loses chord damping above 175. ATTILA found torsion trending to negative damping. Splitting one tip rotor into two more than doubled the instability speed. **That literature is the measure of what the X-76 avoids.**
- **The convertible engine has had no new literature in the pool since 1996**, and both finalists used separate engines.
- **The hover data underpinning runway independence are from the 1980s.**
- **No work in the survey reports a stop-fold conversion in flight.**

Works without retrievable abstracts are cited for their titles, and the prose says so. Brown and Ahuja's forum paper was added as the seventeenth hand primary, because it is the record that carries the abstract.

**OTHER DEFECTS FIXED.**

- "Nothing else in common" with Bell's design, said of Aurora's, which shares the uncrewed concept, the speed goal and the engine types.
- "The first folding tiltrotor demonstrator to be built", when at the date it was funded to manufacture and not built.
- "The most authoritative technical fact … at any date."
- "States it the same way in every document", when the budget books phrase it differently.
- Two negative-existence claims that were not scoped to the documents read.
- "Largest by far" for a cluster 34 percent larger than the next.
- Dittmar and Hall's helical-tip-Mach work, described as more than its abstract supports.
- An unexpanded ATTILA.
- **The conclusion now carries the competitor's identical engine choice**, the primary pass's main finding, which it previously omitted.

**THE OPENING WAS CHECKED AGAINST THE ANALYSIS AGAIN AND HELD**, having been corrected at the end of the drafting pass, which is the first article in four where the publication check found nothing in the opening.

**VERIFICATION.** `verify367.py` runs 569 checks with 0 failures, and every withdrawn wording is asserted absent. All 75 quotations are found verbatim in 109 saved sources. `_verify.py` reports 0 errors and 0 warnings across 304 posts. The stub build is clean, `_lib/render.py` has no findings and all 40 displays match. The style check has zero findings. The scan's single prose semicolon is the debugging tag and its single parenthetical is the register row quoted verbatim, both as in earlier articles. All 66 primary addresses returned 200 in the previous pass.

**PUSHED, NOT PUBLISHED.** One article remains, **A368, the closing synthesis**. The pilot decision on A364's and A365's Epistemic State sections is still open.

---

**Date**: 2026-10-03
**Task**: **A367 PRIMARY-REFERENCE REVIEW, the third of four passes. Committed, NOT pushed, NOT
published.** Seventy-one of seventy-two drafted. References **3,724 to 3,736**, reference primaries **54 to 66**, hand-chosen research primaries **12 to 16**, lines 8,250 to 8,282, H3 sections 53 to 54, display equations held at 40.

**THE LARGEST YIELD IS THE COMPETITOR'S OWN DOCUMENTS.** Aurora's releases of May and October 2024 say its Phase 1B fan-in-wing demonstrator carried "off-the-shelf turbofan and turboshaft engines". **So both finalists answered the solicitation's existing-engine rule with two kinds of engine.** That is the strongest evidence that the separate-engine choice belongs to the rule rather than to Bell, which the draft could only infer. The October release also dates the schedule slip: flight testing was still planned for 2027 in October 2024 and for 2028 by July 2025.

**WHAT NOW RESTS ON A PRIMARY THAT DID NOT BEFORE.**

- **The T700 lineage of the CT7.** It now rests on the New Zealand regulator's 2020 acceptance report and General Electric's 2004 release.
- **The CT7-8's American approval, 29 September 2000.** It comes from the same report and General Electric's 2000 release.
- **The PW308C's primary certificate, Transport Canada's E-31.** The 2007 New Zealand report also gives its application, the Falcon 2000EX, and its rating, 7,002 lb. **The European sheet's 31.15 kN is 7,003 lb, so two regulators agree to within a pound.**
- **The single exhaust and the absent cockpit glazing.** These are now read from DARPA's own artist's concept, marked as a picture and as postdating.
- **The per-mission design-number rule.** It is quoted from the 2020 instruction.
- **The three flight standards the solicitation names.** They are identified by catalogue entry and not read, and the prose says so.
- **The third award notice**, previously missing.
- **Four report primaries.** These are Felker's hover and download work and the SR-7A helical tip Mach study.

**THE ASSUMED XV-15 HOVER TIP SPEED IS NOW CHECKED AGAINST A MEASUREMENT.** It is Mach 0.69 at sea level, inside the 0.60 to 0.73 over which the full-scale XV-15 rotor hover test measured performance and found very little effect of tip Mach number.

**A GAP REPORTED RATHER THAN FILLED.** The 1985 test's tabulated figure of merit did not survive text extraction. So the 0.75 remains a named assumption, and the prose says that no value is quoted from the reports.

**NOT FOUND.** No issue of the CT7 data sheet dated before this article's date is archived, so issue 10, four days after the date, remains the source of the base-model ratings. The New Zealand report of 2020 corroborates the family's power range from inside the date. DARPA's 2023 and 2024 news releases are rendered by script in their archived copies and could not be read.

**VERIFICATION.** `verify367.py` runs 547 checks, and all 66 quotations are found verbatim in 88 saved sources. All 66 primary reference addresses return 200; that does not verify a citation, but it excludes a dead one. `_verify.py` reports 0 errors and 0 warnings. The stub build is clean, the render audit has no findings, all 40 displays match, the style check has zero findings and `symcheck.py` passes.

**NOTHING PUSHED.** **Next prompt: the publication review of A367**, which also pushes. The pilot decision on A364's and A365's Epistemic State sections is still open.

---

**Date**: 2026-10-02
**Task**: **A367 EQUATION-DENSITY REVIEW, the second of four passes. Committed, NOT pushed, NOT
published.** Seventy-one of seventy-two drafted. Display equations **18 to 40**, lines 8,109 to 8,250, inline expressions 60 to 95, the symbol table 41 entries to 51, references held at 3,724, sections unchanged at 16 H2 and 53 H3.

**A scan drove the pass.** `eqscan.py` listed 77 prose lines carrying a figure with no display within six lines. Most were dates, counts and citation runs. Twenty-two were results, and each is now displayed, computed in `eqpass367.py`, and re-derived in `verify367.py` by a different route.

**THE BEST NEW RESULT IS THAT THE HOVER WAKE'S DYNAMIC PRESSURE EQUALS THE ROTOR'S THRUST PER UNIT DISK AREA**, $q\_w = (1+d)\,w$, with the density cancelling. So the downwash load on the ground and on people is fixed by disk loading alone, at any altitude and on any day: 695 Pa at the XV-15's loading and 3,160 Pa at 60 psf. **That makes the stop-fold trade of rotor size for cruise speed exact in its downwash cost.**

**OTHER ADDITIONS.**

- **A cruise ceiling for an assumed lift-to-drag ratio.** At 15,000 lb, a ratio of 6 confines the aircraft to about 16,700 ft and a ratio of 10 reaches about 31,200 ft.
- **The jet's static thrust is 0.47 to 0.88 of the weight**, so even a vectored jet could not hover the aircraft.
- **The jet's cruise thrust power is 0.79 of the turboshafts' continuous power.**
- **The advance ratio at the objective is 1.85, against the XV-15's 0.75 at 300 knots.**
- **The gearbox reduction falls from about 40 to 19 as disk loading rises from 13.2 to 60 psf.**
- **A turbofan-count generalisation of the drag ceiling.**
- **Programme interval, money and budget identities**, and the survey's admission share and mean cluster count.

**ONE FINDING CHANGED THE PROSE.** The money identity showed that the three recorded Phase 1A obligations, 15,194,105 dollars, already exceed the solicitation's Phase 1A figure by 194,105 dollars before Bell is counted. **So the planning figure was not a cap, and the bound on Bell's Phase 1 value, which assumed the 75 million was a ceiling, is now stated as resting on a premise the first sub-phase did not meet.**

**METHOD.**

- **A mutation test exposed a blind spot**, and it is closed. A display that is a pure symbolic identity has no number to recompute, so it was unchecked. `verify367.py` now asserts thirteen symbolic displays verbatim, and it tests the wake identity algebraically on 50 random inputs.
- **My first mutation was a `sed` that did not apply**, so its "not caught" result was meaningless. Mutations are now applied in Python, which asserts that the target exists.
- **A nested `\text{}` inside `\mathrm{}`** would have defeated the symbol checker's label stripping, so it was simplified.

**GATES.** `verify367.py` runs 517 checks with 0 failures, and all 52 quotations are found in saved sources. `_verify.py` reports 0 errors and 0 warnings across 304 posts. The stub build is clean, `_lib/render.py` has no findings, all 40 display blocks match, the style check has zero findings and `symcheck.py` passes.

**NOTHING PUSHED.** **Next prompt: the primary-reference review of A367.** The pilot decision on A364's and A365's Epistemic State sections is still open.

---

**Date**: 2026-10-02
**Task**: **A367 DRAFTED, X-Planes: Bell Textron X-76 SPRINT, the first of four passes. Committed, NOT
pushed, NOT published.** Seventy-one of seventy-two drafted. `_drafts/x_planes_bell_textron_x76_sprint.markdown`, editorial date 2025-12-15, series index 71, full order and documentation-poor. **8,109 lines, 52,274 words of which about 14,100 lie outside the citation runs and reference lists, 18 display equations, 60 inline expressions, a 41-entry symbol table and 3,724 reference definitions**, being 54 primaries, 3,600 research works of which 12 are hand-chosen primaries with abstracts and 624 are report-server records, 620 of them among the 3,588 swept works at 17.3 percent, and 70 related posts, in 16 H2 and 53 H3 sections with 6 tables, from a pool of 12,957.

**THE KEYSTONE IS THAT THE TURBOFAN IS A DRAG BUDGET.** With thrust lapsing as density times a swept factor, the largest equivalent drag area the PW308C can push is $2F\_0\varphi/(\rho\_0V^2)$, the density cancelling, so it is 0.60 to 0.84 square metres at 400 knots at every altitude in the solicitation's band. The two CT7-8s, 3,758 kW at take-off, would hover about 30,800 lb at the XV-15's disk loading, twice the solicitation's heaviest guidance, and the bare engines are 16.3 percent of 15,000 lb. **Both point, as inferences, to an aircraft at or above the top of its guidance or at a high disk loading.** At the XV-15's airplane-mode tip speed a proprotor reaches a helical tip Mach number of 1.00 at 450 knots and 25,000 ft.

**THE PRIMARY BASE IS UNUSUALLY DEEP FOR AN UNFLOWN AIRCRAFT.**

- **The solicitation itself**, HR001123S0031, its proposers' day slides and its questions and answers, all from the federal contracting portal. They give the demonstrator guidance, 8,000 to 15,000 lb, at least 400 knots between 15,000 and 30,000 ft, existing engines with no core changes, crew left to the proposer, no disk loading limit, and a 42-month goal to first flight.
- **Three of four Phase 1A contracts in the award record, each with thirteen offers.** Bell's instrument is absent, consistent with an other transaction, which the solicitation allowed. The record bounds Bell's Phase 1 at 31,347,488 dollars if the 75 million held.
- **Four budget books**, with the same year restated three ways, a scaled demonstrator becoming a demonstrator, and a ground station in the plans.
- **The two engine data sheets.** **The PW308C is approved for multiple-engine installation only**, so a single installation lies outside its civil certificate's assumption.
- **The 1972 full-scale folding rotor test**, set aside for lack of a convertible engine, and McArdle's 1988 finding that a convertible engine beats separate lift and cruise engines. **The X-76 takes the separate-engine path the earlier literature judged heavier**, and the solicitation's existing-engine rule is the stated reason, as an inference.
- **A 2008 DARPA stop-fold tilt rotor study** to the Bell Boeing Joint Project Office, and fourteen Bell patents, each cited for its abstract.

**NEW FINDINGS.** Phase 2 is dated May, June and July 2025 by three sources. **Textron's investor-relations mirror misdates two Bell releases by exactly a year**, while Bell's newsroom is correct. **The register's trailing plus** has four readings: a model-name suffix, as in the Air Force's own "Tri 60-5+"; the enhanced PW308C of 2011; the solicitation's no-core-change upgrade; and truncation. The register's combination syntax makes truncation least likely. The schedule has slipped at least eight months against the solicitation's goal.

**THE OPENING FAILED THE CHECK AGAINST THE ANALYSIS AGAIN, AND THIS TIME AT THE END OF THE DRAFTING PASS, AS A366 DIRECTED.** It stated three engines and a single turbofan as fact, where the article takes the turbofan count as a reading. It called the drag ceiling altitude-independent without its lapse assumption. It said four budget books lay inside the date, when three do, and it said Bell's patents describe "the mechanism". All five places were corrected before commit.

**METHOD.** `verify367.py` runs 323 checks and imports no measurement module. It re-parses the register with an HTML parser, recomputes the hover envelope by bisection, the drag ceiling by thrust over dynamic pressure at four altitudes, and the atmosphere by integrating the hydrostatic equation. **It finds all 52 quotations verbatim in saved sources**, and it caught three injected defects, a stale number, a misquotation and a missing blank line after a display. **Two quotations were paraphrased because the source has a typographical slip or parentheses.** Separately, my own "$15M" in prose would have rendered as mathematics, and the symbol check caught it as a stray `i`.

**GATES.** `_verify.py` reports 0 errors. The only warnings are the expected `progress-stale` pair, which this update clears. The stub build runs in 17 seconds, `_lib/render.py` finds nothing across 540 pages, all 18 display blocks match, the style check has zero findings and `symcheck.py` passes.

**NOTHING PUSHED.** **Next prompt: the equation-density review of A367.** The pilot decision on A364's and A365's Epistemic State sections is still open.

---

**Date**: 2026-10-02
**Task**: **A366 PUBLICATION REVIEW, the fourth and last of four passes. Committed and PUSHED, NOT
published.** Seventy of seventy-two drafted. **Final state 4,669 lines, 29,682 words, 42 display equations, 105 inline expressions, a 33-entry symbol table and 1,974 reference definitions**, being 24 primaries, 1,881 research works of which 13 are hand-chosen primaries and 59 are report-server records at 3.14 percent, and 69 related posts, in 11 H2 and 42 H3 sections with 9 tables, from a pool of 15,522.

**THE OPENING FAILED THE CHECK AGAINST THE ARTICLE'S OWN ANALYSIS FOR THE THIRD ARTICLE RUNNING.** It said the first reading was the only one consistent with the allocation rate. The reserved-block reading needs no allocations, so it is consistent too. **The rule to check the opening by name against the analysis has now caught a real defect in A364, A365 and A366.**

**OTHER DEFECTS FIXED.**

- Two false superlatives about cluster sizes.
- A sentence placing all three founding-year numbers in an anniversary run-up, which the F-47A does not fit.
- A claim that the series' earlier anomaly gaps were all public for years. That is false for the X-67's, and A364 does not record it.
- 'DARPA chose it' for the X-50, which contradicts the article's own finding of two requesters.
- Two timing errors, 'in a day' and 'the eleven months before the semiquincentennial.'
- A stale reports-server count of 26 of 161 that ignored the aimed sweep.
- A dangling pronoun and a stale promise of a further audit.
- An F-35 overclaim.

Eleven self-references were cut or varied, because 'article' was the only content-independent word above five per thousand. The F-47 file's metadata date, 17 June 2025, falls inside the dateline and is stated as such.

**VERIFICATION.** `verify366.py` runs 745 checks, and every withdrawn wording is asserted absent with its replacement present. `_verify.py` reports 0 errors and 0 warnings across 304 posts. The stub build and render audit are clean, all 42 display blocks are matched, and the style and symbol checks are clean. All 23 reports-server addresses return 200, and a random sample of 80 identifiers all resolve.

**PUSHED, NOT PUBLISHED.** Two articles remain, **A367, the X-76A to Bell Textron for SPRINT**, and A368, the closing synthesis. **A367 inherits this article's register reading, the engine cell, and the dating of the row's publication.** The pilot decision on whether A364's and A365's Epistemic State sections should record that the register rows they rely on were not public at their dates is still open.

---

**Date**: 2026-10-02
**Task**: **A366 PRIMARY-REFERENCE REVIEW, the third of four passes. Committed, NOT pushed, NOT
published.** Seventy of seventy-two drafted. References **1,935 to 1,974**, reference primaries **16 to 24**, research works **1,850 to 1,881** of which 13 are hand-chosen primaries verified by title, report-server citations **41 to 59** and their share **2.22 to 3.14 percent**, lines 4,566 to 4,662, display equations 40 to 42, the pool 11,384 to 15,522.

**THE LARGEST YIELD.** NASA's *American X-Vehicles* inventory, SP-2003-4531, was found by the aimed sweep. It gives the X-50A precedent a second primary. It reports DARPA's 50/50 reasoning and quotes Boeing's programme manager saying that Boeing got the number out of sequence by special request. **It also predicted in early 2003 that the X-49 would be issued with the next request, and it was.** So the earlier chosen number has two different requesters in three accounts, which is the same open question of agency the X-76 has.

**WHAT ELSE NOW RESTS ON A PRIMARY.**

- Each founding year: the Declaration transcript, Public Law 114-196, the National Security Act of 1947, and the Army's own quotation of the 14 June 1775 resolution.
- The 1994 instruction's next-available sentence, quoted from its text.
- DARPA's XRQ-73 announcement. **It calls an unmanned designation an X-plane**, and the article now says so.

**A CORRECTION OF METHOD.** My first wording attributed arguments to three papers I had read only by title. I fetched the registry abstracts and rewrote each sentence to follow its abstract. I also dropped a superlative that I could not support, and the Numerical Commemoration study is cited for its title alone, which the prose states.

**THE AIMED SWEEP WAS MEASURED.** Forty questions in the designation system's own vocabulary added 4,138 records to the pool, and the gate admitted 30. Report-server citations went from 41 to 59, which is 2.22 to 3.14 percent. That is small, and it is the honest result for a subject that is not engineering. Two new homonyms became refusal cases. **Two defence-registry PDFs refuse every client**, an edition of the instruction catalogued in 1997 and the Navy's 2012 report on naming vessels, so both stay as swept records. **Two newly cited pages now return 403 to the address sweep.** The IARPA and Army pages were read earlier with browser headers, and saved copies are under `tmp/a366/prim/`.

**VERIFICATION.** `verify366.py` runs 716 checks, and every new quotation is read back from its saved copy. `_verify.py` reports 0 errors and 0 warnings. The stub build is clean, the render audit has no findings, all 42 display blocks are matched, and the style and symbol checks are clean.

**NOTHING PUSHED.** **Next prompt: the publication review of A366.** It also pushes. The pilot decision on A364's and A365's Epistemic State sections is still open.

---

**Date**: 2026-10-02
**Task**: **A366 EQUATION-DENSITY REVIEW, the second of four passes. Committed, NOT pushed, NOT
published.** Seventy of seventy-two drafted. Display equations **14 to 40**, lines 4,402 to 4,566, inline expressions 38 to 105, the symbol table 17 entries to 33, references held at 1,935, sections and tables unchanged at 11 H2, 42 H3 and 9 tables.

**The scan listed 61 prose lines with a figure and no nearby display, and about two dozen were results.** Each is now displayed, computed in `eqpass366.py` and re-derived in `verify366.py` by a different route.

**ONE DRAFTING-PASS SENTENCE WAS WRONG IN KIND AND IS REPLACED.** It said a clustering factor of about eight orders of magnitude would be needed to rescue the unreleased-allocations reading. Eight orders is the ratio of the tail to a 0.05 threshold, not a clustering factor. **The clustering factor is 23.51**, a rate of 19.67 new research numbers a year through that autumn, and the article now states both quantities by name.

**TWO ADDITIONS ARE LABELLED AS SCALES AND NOT TESTS.**

- The founding-year range probability of 0.00320 assumes a uniform null that nobody holds, over a window drawn after the cluster was seen.
- The serial-number estimator is applied to show how a chosen number misleads, not to estimate anything.

**A DEFECT THE PASS INTRODUCED AND CAUGHT.** Two new display blocks were followed directly by text and rendered as prose, so the page showed 38 of 40. `mathrot.py` reported the mismatch. The blank lines were added and a verifier check now forbids the pattern.

**VERIFICATION.** `verify366.py` runs 679 checks and the floor on display equations is now 40. `_verify.py` reports 0 errors and 0 warnings across 304 posts. The stub build is clean, `_lib/render.py` reports no findings, all 40 display blocks are matched, and `symcheck.py` and `stylecheck.py` are clean.

**NOTHING PUSHED.** **Next prompt: the primary-reference review of A366.** The pilot decision from the drafting pass is still open, namely whether A364's and A365's Epistemic State sections should record that the register rows they rely on were not public at their dates.

---

**Date**: 2026-10-02
**Task**: **A366 DRAFTED, *X-Planes: X-69 through X-75, the Leapfrogged Block*, the first of four
passes. Committed, NOT pushed, NOT published.** Seventy of seventy-two drafted. Editorial date
2025-12-14, series index 70, designation-anomaly class under the reduced order. **4,402 lines, 14
display equations, 38 inline expressions, a 17-entry symbol table and 1,935 reference definitions**,
being 16 primaries read directly, 1,850 research works across 12 clusters from a pool of 11,384, and
69 related posts.

**THE BLOCK IS SEVEN SKIPS MADE AT ONCE SO THAT ONE NUMBER COULD BE CHOSEN.** The handoff framed three
readings, and the record separates them. Seven unreleased allocations would all have to fall in the 61
days between the X-68A and the X-76A, and at the series' own rate that has a Poisson tail of 1.83e-10.
A reserved block has no instrument in the 2020 instruction. The instruction refuses requests in skipped
sequences and gives the allocating office an unconditioned discretion to skip, so the X-76A is that
discretion exercised or a request the text says is not accepted. **DARPA's statement of 9 March 2026
calls the 76 a deliberate nod to 1776**, and the article uses it while saying it postdates the
dateline by 85 days.

**THE HANDOFF'S PREMISE WAS PARTLY WRONG AND THE ARTICLE SAYS WHERE.** It said no allocation in the
register carries any of the seven numbers. **No research row does, but the XRQ-72A, XRQ-73A and
YMV-75A carry 72, 73 and 75 in other basic missions**, and the YMV-75A turned out to be the key to the
whole article.

**FOUR FINDINGS THE EARLIER ANOMALY ARTICLES DID NOT HAVE.**

- **The public register did not show the X-68A or the X-76A until between 15 January and 1 February
  2026**, by archived copies. **A364 and A365 therefore also state register facts that were not public
  at their own dates.** Neither article records this. **I did not change them, and it is the pilot's
  call whether their Epistemic State sections should say so.**
- The compiler wrote a sentence naming the X-77 reading and removed it after DARPA's statement, under a
  last-updated stamp that never changed, so his pages must be dated by archive capture.
- **The X-76A is the third founding-year design number in 329 days**, after the YMV-75A for the Army's
  1775 and the F-47A for the Air Force's 1947. Air Force public affairs emails released under the
  Freedom of Information Act name General Allvin as the F-47's decider, in consultation with the
  Secretary of Defense. This is the only named chooser of a design number the article found.
- **The 2020 rule describes 6 of the 23 allocation events made since it took effect, or 7 if the
  RQ-170 row is set aside.** Two parsers disagreed, and that disagreement is how the sensitivity was
  found.

**THE ARTICLE ENDS ON A TEST THAT CAN BE CHECKED LATER.** If the next research designation is the X-69A,
the X-49 precedent governs in practice. If it is the X-77A, the 2020 text governs as written. No X-69
or X-77 is public as of 2 October 2026.

**VERIFICATION.** `verify366.py` runs 632 checks and imports no measurement module. It re-parses the
register with an HTML parser, reads every quotation back from its saved source, and recomputes the
Poisson tail from the upper sum. `_verify.py` reports 0 errors and 0 warnings across 304 posts. The
stub build took 15 seconds. `_lib/render.py` reports no findings across 539 pages. There are 14
display blocks, matched source to rendered, and zero emphasis spans in mathematics. `symcheck.py` and
`stylecheck.py` are clean. **Two `.mil` primaries return 403 to the address sweep.** Both were read
earlier in the session with browser headers, and copies are saved under `tmp/a366/`.

**INHERITED INSTRUMENTS THAT WERE STALE.** `count.py` was pointed at the X-66 draft, and `rendercheck.py`
expects script-tag mathematics this site no longer emits. Both were retargeted or read around, and
neither affects a stated figure.

**CORRECTIONS MADE ON THE PILOT'S INSTRUCTION, in the same commit:**

- The `HANDOFF.md` paragraph that still called the eight re-dated drafts uncommitted.
- The TASKLOG note that still called A376 unpublished, its Part 1 of 2 wording and its `progress-stale`
  wording.
- Two more stale statements found while correcting: the TASKLOG status and the draft summary both still
  called A365 not fully pushed.
- **TASKLOG had no history row for any of A365's five commits or the repair day's six.** The row count
  never changed across those commits, so the rows were never written rather than destroyed. Two rows
  were reconstructed from the commit log and are labelled as reconstructed.

**NOTHING PUSHED**, per the rhythm for pass one. **Next prompt: the equation-density review of A366.**

---

**Date**: 2026-10-02
**Task**: **ALL SEVEN PILOT DECISIONS EXECUTED.** The mathematics repair is applied and
committed, 133 rendered spans to 0 across 61 published posts, byte-identical to the rehearsal
and re-verified by a fresh production build. The A358/A359 officiality repair is done in place,
both drafts now stating the three-way split of 21, 9 and 1, with A358's chronology scoped to
fully dated rows and A360's two error-narrating passages rewritten to make the same argument
impersonally, every repaired figure recomputed from the register before the edit and asserted
after it. The eight drafts the second line re-dated to 2126 are committed exactly as they stand.
`sa.html` is deleted. The A376 attribution stands, by decision. **A366 is slotted as *X-Planes:
X-69 through X-75, the Leapfrogged Block***, editorial date 2025-12-14, series index 70, seven
designations absent from the released record at once against the single skips of A355 and A364.
**The handoff follows this commit and the push follows the handoff, on the pilot's instruction.**

---

**Date**: 2026-10-02
**Task**: **SERIES REPAIR SWEEP on the pilot's instruction.** Every open repair was examined, one
was found to need no further input and its execution is FULLY REHEARSED AND MEASURED, one that
looked executable turned out to carry an editorial fork, and the rest were already marked as the
pilot's. **Nothing in the live tree or the published corpus was changed.** One commit, this
channels update.

**THE MATHEMATICS REPAIR IS READY AND REHEARSED END TO END, AWAITING ONE WORD.** The fixer
escapes, inside inline mathematics spans only, the underscore shape kramdown opens emphasis on
and every bare asterisk, both rules measured by A362 and A363. Rehearsed in an isolated twin
build pair under `tmp/mathrepair/`:

- **61 source files edited, 313 inline spans**, 127 files without `mathjax: true` skipped
  untouched. Display blocks untouched by construction.
- **133 corrupted rendered spans across 37 pages fall to 0 across 0**, measured by
  `mathcorpus.py` over the built twin, and the sweep also disarms every latent single-asterisk
  and underscore case in the same pass, which is the difference between 313 edits and 133 breaks.
- **38 pages differ between the fixed and unfixed twins and every one differs only inside its
  inline mathematics**, proven by blanking the spans and comparing the remainder byte for byte.
- The rendered audit over the fixed twin reports no findings.

**THE TWIN COMPARISON CAUGHT REAL COLLATERAL DAMAGE BEFORE IT COULD SHIP.** The fixer's first
version walked into a 2016 article's shell listing, where `${DB_NAME}.* TO '${DB_USER}'` reads
as an inline span to a naive dollar regex, and escaped the glob star inside a published GRANT
command. **Two pages differed outside mathematics and that is how it was caught.** The fixer now
gates on the front matter and masks fenced and inline code, and the rerun shows zero pages
differing outside mathematics. `tmp/mathrepair/fixmath.py` records the failure in its own
comments.

**THE A358 AND A359 OFFICIALITY REPAIR TURNS OUT TO CARRY AN EDITORIAL FORK AND STAYS YOURS.**
The facts are settled and re-verified today from the register: the research series is 21 fully
official, 7 cell-marked, 2 row-marked and 1 span-marked of 31, A358's split accounts for 30 of
31, A359's places the span row where its markup denies. **But A360 narrates both errors in its
own prose as the justification for its three-state recomputation**, so repairing the two
originals falsifies A360's paragraph about them. That coupling is why the repair survived six
articles, and the choice between an errata convention and an in-place repair with A360 rewritten
is an editorial policy decision. A358's register-wide sentence, 539 rows, 86 and 17, was also
re-verified today and is exactly right, so no repair touches it under any option.

**EVERYTHING ELSE OPEN NEEDS THE PILOT AND THE OPTIONS ARE IN TODAY'S REPLY**: the eight drafts
re-dated to 2126, `sa.html`, the A376 attribution in pushed history, the push of what is now
nine commits, and the A366 subject.

---

**Date**: 2026-10-02
**Task**: **A365 ADDENDUM ON THE PILOT'S INSTRUCTION, citing the two walled documents by their
nominal addresses. Committed, not pushed, not published.** All four passes remain complete and
this is a fifth, small commit on the same article.

**THE INSTRUCTION WAS TO LINK THE NOMINAL ADDRESS WHERE ONE EXISTS AND THE LOGIN PAGE WHERE ONE
DOES NOT, AND BOTH CASES OCCURRED.** The solicitation HR001120S0037 has a real portal address that
serves an application shell to a client without a session, and it is now cited by that address.
The compatibility handbook's own record number inside the standards repository is not
discoverable without a session and was not guessed, so it is cited by the repository's public
search page, with the handbook named in full in the prose, by designation, date and supersession,
so a reader with access can find it in one step.

**THE DISTINCTION BETWEEN A READING AND AN ADDRESS IS KEPT STRUCTURAL.** The two definitions live
in their own named group in the reference tooling, excluded from the read-directly count the
source base states, which stays at 20. The prose at each citation says no claim rests on either
document's content, the source base says it again with the mechanism, and the epistemic state
records both. The handbook's naming also bought the article a sentence it lacked, that the pit
drop belongs to a prescribed test catalogue, with the standard-practice claim still resting on
the swept literature rather than on the unread handbook.

**No other reference was identified as nominally good and excluded for verification alone.** The
two DTIC reports surfaced during the pass are known only by search-result titles, which is an
identity too thin to cite even as an address, and the unfunded-priorities letter has no public
address at all.

**Gate: everything.** `_verify.py` 0 errors and 0 warnings across 304 posts, `verify365.py` 120
checks with 0 disagreeing, stub build clean, rendered audit no findings, 42 display blocks
matching, style scan clean, and both address URLs confirmed live at commit time, 47,709 and
32,888 bytes.

**Eight commits now await a push instruction.**

---

**Date**: 2026-10-02
**Task**: **A365 PUBLICATION REVIEW, the fourth and last of four passes. Committed, NOT PUSHED and
NOT PUBLISHED**, publication of the series never having been authorised. **Sixty-nine of
seventy-two drafted, three remain.** Five A365-line commits now await a push instruction,
alongside the handoff and durability commits, seven unpushed in all.

**FINAL STATE 2,893 lines, 21,933 words, 42 display equations, 133 inline expressions, a 78-entry
symbol table and 546 reference definitions**, in 16 H2 and 77 H3 sections, citing 458 distinct
works across 11 clusters from a pool of 4,711, with 72 report primaries at 15.7 percent, median
year 2009 and a range from 1935 to 2026, plus 20 primaries read directly.

**THE PASS'S BEST CATCH IS THE OPENING SENTENCE, WHICH THE ARTICLE'S OWN OFFICIALITY ANALYSIS
REFUTED.** The draft opened by saying the Department has released exactly one word about this
aeroplane. By the register's own marking scheme the row's unmarked cells are official data, so the
Department has released the date, the maker, the engine and the sponsor as well as the name.
**A364's publication review caught an opening its own table refuted, and this is the same defect
in the same position.** The opening now says every official word is an item of bookkeeping and
that what the aircraft is for has no official word but the name, which is the sharp claim that
survives the article's own evidence, and the conclusion and the section title were corrected with
it.

**FOUR MORE DEFECTS, EACH CAUGHT BY A SCAN.** The source base said the first sweep asked seven
dozen questions where it asked thirty-nine, a sentence that contradicted its own neighbour, and
the whole passage is now slot-driven from the sweep's cover record. A sentence said the sponsor
holds a twentieth of the register's research rows where five of thirty-one is a sixth. The
identity printed 29.9 beside a ratio printed 30 while calling them the same number, false as
printed, and both now print at the same precision. And a sentence-initial slot rendered lowercase.

**TWO INSTRUMENT CORRECTIONS.** The dateline scan's label carried A362's editorial date through
two passes while its filter was right, an inherited instrument modelling the previous article
until every constant is retargeted. And the primary count the prose states had gone stale at 19
when the reference set grew to 20, because the emitter ran before the regeneration, which is the
pipeline-ordering defect the recompute rule exists to prevent, now re-run in order.

**ONE CORRECTION TO MY OWN PREVIOUS REPORT.** It said the two fact-sheet snapshots postdate the
editorial date. They do not. The snapshots are of 1 and 4 December 2025, both inside the date, so
the pages cited are the pages as they stood at the time, and the epistemic state now says exactly
that. The award record is the opposite case, read in October 2026 with amounts reflecting
modifications through May 2026, and the epistemic state now carries that too.

**THE EPISTEMIC STATE ALSO GAINED** the UCAV expansion at first occurrence, the scoping of the
name's official standing to the article's date, and the narrowing of the engine-cell claim to the
only independent published statement, since the press items derive from the register.

**AND ONE THING THE REGISTER SAYS ABOUT A366 THAT THE TASKLOG NOW RECORDS.** The register carries
no research row between the X-68A of 20 August 2025 and the X-76A of 20 October 2025, so
designations 69 through 75 are absent from the released record and the next article is likely an
absence article. **I nearly wrote a contractor's name into the TASKLOG for A366 from nothing**,
caught it against the register before committing, and the subject determination belongs to the
pilot's prompt.

**Gate: `_verify.py` 0 errors and 0 warnings across 304 posts.** `verify365.py` 120 checks, 0
disagreeing. Stub build clean in fifteen seconds, rendered audit no findings across 539 pages, 42
display blocks matching in both delimiters, every symbol resolving, style scan clean in every
category with the four semicolons the register quotation and the debug tag, structure scan showing
the required sections present and in order. The spelled-number sweep ran over every sentence
mixing a spelled number with a digit, fifty-four of them, and the identity-precision defect above
is what it caught.

**AWAITING THE PILOT.** A push instruction for the seven unpushed commits. The A366 subject
prompt. And the two standing items, the corrupted mathematics in published posts and the A358 and
A359 officiality repair, both unchanged.

---

**Date**: 2026-10-02
**Task**: **A365 PRIMARY-REFERENCE REVIEW, the third of four passes. Committed, not pushed. NOT
PUBLISHED**, and publication of the series has never been authorised. **Sixty-nine of seventy-two
drafted, three remain.** The publication pass remains.

**17 primaries to 20, and the pass was about which documents carry the load rather than about the
count.** 2,879 lines and 21,772 words, references 543 to 546, the swept 458 untouched.

**THREE LOAD-BEARING ANCHORS MOVED ONTO PRIMARY DOCUMENTS.**

- **The launch aircraft's weights are now the service fact sheet's**, current as of April 2019,
  read from a public archive snapshot because the service's site refuses every client. The
  comparison's midpoint moved 2.5 percent and the factor between the two mass fractions moved from
  29 to 30, every downstream figure recomputed through the slots.
- **The cruise missile's mass and the word turbofan are now the manufacturer's own datasheet**,
  which strengthens the engine-designation contradiction because the register says turbojet and
  the engine's maker says turbofan in its own document.
- **The atmosphere subsection's constants now carry the 1976 standard itself**, an image-only scan
  whose two defining pages were read as page images per A364's practice. The adopted-constants
  table and the layer-gradient table give exactly the four constants the article uses, and one
  nuance came back from the reading: the defining relations take geopotential height, which the
  article now says, the difference at this altitude being under two parts in ten thousand.
- **The carried missile's dimensions and baseline weight now carry the service's sheet**, retrieved
  on a delayed background retry after both public archives rate-limited this address for most of
  the pass. The modelling mass stays the heavy-variant encyclopedia figure BY A STATED CHOICE,
  since a programme flying in 2026 carries current missiles, and the sensitivity is stated: every
  mass fraction is linear in it and no conclusion moves.

**A SMALL FINDING ABOUT THE FACT SHEETS THEMSELVES.** Both of the service's sheets convert their
own pound figures to kilograms incorrectly, the aircraft's take-off weight printed 291 kilograms
low and the missile's launch weight 1.2 kilograms low. The article therefore quotes both documents
by their pounds, converts at the definition of the pound, and the verifier asserts both
discrepancies so neither can silently become the article's own.

**THE ADDRESS SWEEP CAUGHT AN INVENTED URL, WHICH IS THE PASS'S METHOD FINDING.** The first pass
wrote the register's address as `mds-addendum.html` from memory, a plausible path that returns
404. The register lives at `412015-L(addendum).html`, confirmed from the site's own index and from
A364's definition. **A remembered identifier is a fabricated identifier**, the corpus rule A364
earned with an invented DOI, enforced here a second time by the same instrument. Every one of the
20 primary URLs now resolves with substantive content.

**WHAT THE PASS COULD NOT GET, STATED RATHER THAN HIDDEN.** The engine's thrust figure appears in
neither manufacturer document and remains encyclopedia-sourced, and it is the weakest link in the
chain, anchoring the thrust-to-weight table, the climb gradients and the mass sweep's brackets.
The discipline's governing test-procedure handbook is officially distributed through a
login-walled repository and was not readable through any route tried, so it is not cited. The
broad agency announcement remains named and unread, the archive's index confirming no snapshot of
it exists. Two documents the press derives from, an unfunded-priorities letter and the
solicitation, are now both recorded as unretrievable primaries. The thin literature clusters were
probed once more through the aeronautics reports server and stayed thin, so the honest negatives
stand.

**Gate: `_verify.py` 0 errors and 0 warnings across 304 posts.** `verify365.py` 115 to 120 checks,
0 disagreeing, the new ones asserting both fact-sheet conversion discrepancies and both stated
dimensions against their inch originals. Stub build clean, rendered audit no findings across 539
pages, 42 display blocks matching in both delimiters, style scan clean in every category. The
fighter-side constants in the verifier moved to the fact sheet's pound figures independently of
the calculation module's copies, so the two routes stay separate.

**FOR THE PUBLICATION PASS.** The dateline paragraph in the epistemic state should gain the
archive-snapshot dates for the two fact sheets, both of which postdate the editorial date. The
conclusion's factor of 29 became 30 through the slots and reads correctly, and the identity
sentence's spelled-out fifteen held, but **spelled-out numbers near slot-driven figures are where
a stale word hides**, and the publication pass should sweep for them.

---

**Date**: 2026-10-02
**Task**: **A365 EQUATION-DENSITY REVIEW, the second of four passes. Committed, not pushed. NOT
PUBLISHED**, and publication of the series has never been authorised. **Sixty-nine of seventy-two
drafted, three remain.** Primary-reference and publication passes remain.

**24 display equations to 42 across 18 additions, 90 inline expressions to 132, the symbol table 53
to 78 entries**, 2,504 to 2,814 lines and 18,566 to 21,052 words, references held at 543 and
measured before and after. **Every addition is classical mechanics in classical mechanics
vocabulary**, on the pilot's instruction, which the subject accepted without strain because the
subject is two-body momentum, hydrostatics and rigid-body rotation wearing military nouns.

**THE BEST ADDITION IS THE PIT-TEST FIDELITY RATIO, WHICH NO SOURCE STATES AND MOMENTUM
CONSERVATION REQUIRES.** The one keystone-adjacent test in the budget books' plans is a pit drop of
a mass simulant from a clamped vehicle. Clamped, the cartridge impulse divides by the store's mass.
In flight the launcher recoils and the same impulse divides by the reduced mass, so flight
separation is faster than the pit's by exactly 1/(1-mu). **For a fighter that correction is 0.6
percent and the technique is faithful, which is why it is standard. For this vehicle it is 9.9
percent for one missile and 21.9 for the pair.** The standard ground test's fidelity degrades with
the very parameter the programme exists to study, and the open record does not say whether the
analysis carries the correction because it does not describe the analysis.

**THE SECOND BEST CLOSES THE MASS SWEEP FROM ABOVE BY CLASSICAL MECHANICS ALONE.** The climb
gradient is T/W minus 1/(L/D), a turbojet's thrust lapses roughly with density, and the density
ratio at cruise altitude is 0.31. At 1,400 kilograms the sea-level gradient of 22.7 degrees falls
to 2.9 at altitude. At 1,800 it falls to 1.0. **At 3,000 kilograms it is negative, so the upper
bracket of the mass sweep is no longer a plausibility argument but the mass beyond which the one
published engine cannot hold the flight condition every description of the programme requires.**

**THE REST, BRIEFLY.** The standard atmosphere derived from four constants, confirming the two
values the first pass asserted to within rounding. The factor of 29 shown to be an identity in the
two launcher masses alone, the missile cancelling. The amplification's derivative. The heave at
unchanged lift, alpha g, a 0.22 g uncommanded manoeuvre at the instant of release against a
fighter's 0.006. The retrim lift step. The ejection as a two-body problem with the reduced mass
explicit, and the launcher's share of every cartridge's energy proven equal to mu itself, 390
joules per shot into this vehicle's structure against half a percent into a fighter's. The
asymmetric-release roll transient worked to numbers, tens of degrees of bank in the half second
before any control responds, inertia estimate labelled. The ejector tip-off worked example,
assumptions stated. The Breguet relation derived in one line so the logarithm's position is earned
and not asserted. The marginal exchange, 4,901 metres per kilogram air-breathing against 1,371
rocket at the midpoint. The hinge equation and deployment time for the folding surfaces, with the
Newton's-third-law observation that a lagging panel delivers its whole hinge torque as uncancelled
roll to a vehicle that has no aerodynamic control at that moment. The pit-drop kinematics, and the
aerodynamic deviation term that grows as t squared exactly as gravity does, which is why timing
alone cannot separate mechanism from aerodynamics and why the store-separation literature exists.

**ONE INSTRUMENT CORRECTION.** `symcheck.py` flagged word superscripts in the fidelity ratio as
undeclared symbols, and the right fix was in the article rather than the checker, since a text
label inside mathematics belongs in upright type. The checker also learned that a second derivative
dot is a decoration, which is its own blind spot and not the page's.

**Gate: `_verify.py` 0 errors and 0 warnings across 304 posts.** `verify365.py` grew from 71 to 114
checks with 0 disagreeing, the new ones taking different routes from the displayed forms: the
atmosphere from its defining constants, the energy partition by explicit kinetic-energy
bookkeeping, both derivatives by central difference, the deployment closed form against a numerical
integration, and the heave from a written-out force balance. Stub build clean, rendered audit no
findings across 539 pages, 42 source display blocks matching 42 rendered in both delimiters, 133
inline spans and none carrying an emphasis tag, every symbol resolving against the 78-entry table.
Style scan zero findings in every category with the four semicolons remaining the register
quotation and the debug tag.

**FOR THE PRIMARY-REFERENCE PASS.** The three encyclopedia anchors stand as before and the equation
pass leaned on them harder, since the engine thrust now drives the climb table and the missile mass
drives the two-body results. Replacing them is now more valuable, not less. The atmosphere
subsection's constants are textbook values and could carry a standard-atmosphere citation.

---

**Date**: 2026-10-02
**Task**: **A365 FIRST PASS, the draft of *X-Planes: General Atomics X-68 LongShot*. Committed, not
pushed. NOT PUBLISHED**, and publication of the series has never been authorised. **Sixty-nine of
seventy-two drafted, three remain.** Equation, primary-reference and publication passes remain.

**FIRST-PASS STATE 2,504 lines, 18,566 words, 24 display equations, 90 inline expressions, a 53-entry
symbol table and 543 reference definitions**, in 16 H2 and 74 H3 sections, citing 458 distinct works
across 11 clusters from a pool of 4,711, with 72 report primaries at 15.7 percent, median year 2009,
range 1935 to 2026, plus 17 primaries read directly.

**THE KEYSTONE IS NAMED BY THE GOVERNMENT AND IT IS NOT THE RANGE.** Four budget justification books
inside the editorial date, and a fifth outside it, carry the sentence that the programme will address
the stability and control challenges of launching air-to-air missiles from a relatively small unmanned
vehicle. **So the subject is a store mass fraction.** A fighter releasing one of these missiles sheds
0.616 percent of itself and a vehicle of this class releasing two sheds 17.94 percent, a factor of 29,
and the article derives the centre-of-gravity shift, the static-margin change, the retrim demand, the
two parallel-axis inertia corrections, the asymmetric-release rolling moment and the ejector recoil
from that one ratio.

**THE REACH BENEFIT IS THE MOTIVATION AND IT IS ARITHMETIC, STATED AS A COST.** A missile's reach is
logarithmic in its speed ratio, so doubling it with its own motor takes the propellant fraction from
0.402 to 0.746 and leaves nothing for a warhead, while the carrier flies the same distance on a fuel
fraction of 0.013. **A first pass reported a terminal-energy gain of six thousand and that figure was
an artefact**, because a missile with a 114 kilometre decay length cannot fly the 500 kilometres the
expression assumed. The exponential is a reach ceiling and the article says so.

**THREE FINDINGS FROM THE PRIMARY RECORD.**

- **The Department has released one word about this aeroplane and it is the name.** The register's
  description is `Longshot; Experimental air-launched UCAV for air-to-air engagements.` and the markup
  puts only `Longshot` outside the unofficial span. **It is the only research row in the register with
  a span-level mark**, 13 rows carrying one register-wide.
- **The concept changed exactly once and the budget books date it to an eleven-month window.** A
  weapon system with multi-mode propulsion became an air-launched unmanned vehicle carrying existing
  missiles between the book of May 2021 and the book of April 2022. **The award record corroborates
  it independently**, holding the multi-mode wording verbatim in Northrop Grumman's contract
  description from January 2021, and the single-mode cruise-missile engine is the physical trace.
- **The demonstration of the keystone appears in the plans of exactly one book.** PB2024 planned
  flight demonstrations validating separation of the missile from the vehicle. PB2025 replaced it with
  validating the vehicle's separation from the host aircraft, which is carriage release and a
  different test. What stands in the record instead is a ground pit drop of a mass simulant.
  **Captive carry meanwhile slipped two fiscal years across three books, each planning it for its own
  budget year.** Stated as an observation about documents and not a claim about engineering.

**FIVE THINGS I GOT WRONG AND CORRECTED, RECORDED BECAUSE THEY ARE THE USEFUL PART.**

- **I "corrected" three of the handoff's register counts and the handoff was right.** General Atomics
  holds 16 rows and 13 rows name Williams, exactly as it said. I had measured on `register.rows()`,
  which drops rows whose date will not parse, against the handoff's `meas.all_rows()`. **Mixing two
  instruments' populations is already in `VERIFICATION_TRAPS.md` and I did it anyway.**
- **The subject gate passed a clean two-sided audit while refusing the subject.** It admitted 17.9
  percent, and the refused pile held the F-15 store-separation loads report, powered missile
  separation from an F/A-18, in-flight captive store loads, the cavity door papers and the
  aircraft-store interface standards. **The audit passed because its keep cases were copied from the
  homonym probe's output, which lists what the patterns already match.** A keep sample drawn from what
  a gate admits cannot measure what it refuses. Redrawn from the refused pile, it failed on 24 cases
  at once.
- **The gate's organising principle was wrong.** Boundary-layer, flow, leading-edge and turbulent
  separation are the word's largest aeronautical users, and **they are aerodynamics, so no guard that
  asks whether a title is aeronautical can exclude them.** The gate now requires a word naming a
  carried object and admits `separation` nowhere on its own. Retail was the other unguarded collision
  and the first probe's sample was too small to show it.
- **A hyphen defeated a cluster pattern rather than a guard.** The series has recorded hyphens
  defeating guards, which admits wrongly and is loud. **A hyphen defeating a cluster pattern refuses
  wrongly and is silent**, because the record is simply not in the output. Separator tolerance is now
  applied once, centrally.
- **A verifier pattern matched the wrong sentence.** The draft states a burnout speed twice and
  `burnout speed of ([\d,]+)` took the motor's actual figure where the check wanted the doubled-reach
  demand. Eleven of twelve first-run disagreements were the verifier's own bugs and the draft was
  right in all eleven.

**Gate: `_verify.py` 0 errors and 0 warnings across 304 posts.** `verify365.py` 71 checks, 0
disagreeing, importing none of the measurement or emitter modules and parsing the register and the
budget books again with different patterns. Stub build clean in 15 seconds, rendered audit no findings
across 539 pages, 24 source display blocks matching 24 rendered in both delimiters, 98 inline spans
and none carrying an emphasis tag. Symbol check 53 declared and every token resolving. Style scan
zero contractions, zero em and en dashes, zero prose colons, zero prose parentheticals, zero capitals
as emphasis, and four semicolons all inside the verbatim register quotation or the debug tag.

**QUESTION FOR THE PILOT.** Three load-bearing anchors come from an encyclopedia rather than a
primary source: the engine's thrust through the cruise missile that shares it, the missile's mass, and
the host aircraft's masses. The keystone comparison uses the missile's mass and the engine anchors the
whole mass sweep. **I propose the primary-reference pass replace all three**, and I have not done so
in this pass because it is that pass's work.

**AND ONE PROCESS NOTE.** The first attempt at this draft ended when a safeguard flagged the turn
after fourteen minutes of research, with no draft on disk and the findings only in the conversation.
The research survived because it had been written to files and **the findings did not, because they
had only been said.** That is now documented in general terms as
[`_docs/process/WORK_DURABILITY.md`](./WORK_DURABILITY.md), committed separately, and this draft was
composed section by section to disk for that reason.

---

**Date**: 2026-10-02
**Task**: **A364 PUBLICATION REVIEW, the fourth and last of four passes. Committed and PUSHED on the
pilot's instruction. STILL NOT PUBLISHED**, and publication of the series has never been authorised.
**Sixty-eight of seventy-two drafted, four remain.**

**FINAL STATE 5,214 lines, 36,167 words, 68 display equations, 185 inline expressions, an 85-entry
symbol table and 1,315 reference definitions**, in 9 H2 and 54 H3 sections with 20 tables, citing 1,228
research records across 15 clusters from a pool of 14,384, with 159 report primaries at 12.1 percent,
median year 2011, range 1900 to 2026.

**THE REVIEW REFUTED THE ARTICLE'S OPENING SENTENCE, WHICH IS THIS SERIES' RECURRING DEFECT IN ITS MOST
VISIBLE POSITION.** It read that the X-67 is the only designation in this series whose entry in the
register is an analogy. **The compiler's own notes refute it.** His note on the XRQ-73A derives the
number 73 from the XRQ-72A because one programme follows the other, and his note on the YFQ-44A says the
number is out of sequence like the YFQ-42A's. **The article's own table two sections later lists both.**
The opening is now a comparison against a named comparison set, which is what the superlative rule asks
for, and the narrower claim it makes is that the 67 is derived from another number's derivation while
the 73 is derived from a programme relationship. **The counter-examples are in the article.**

**AND A SECOND ABSOLUTE WAS WRONG IN THE ARTICLE'S FAVOUR.** It said that searching the register for the
string X-67 finds the note and nothing else. **The string does not occur in the register at all**, not
even in the note, whose text says X-series. The two occurrences anywhere in the compiler's work are both
in the separate compilation of missing designations. **The register does not deny the X-67. It has no
X-67 in it.**

**A THIRD WAS TOO STRONG BECAUSE THE PRIMARY PASS HAD MADE IT SO.** The article said the
lowest-never-allocated definition cannot be computed from the public record at all. **The primary pass
had just added two documents that reach back before the register**, so the claim is now that no public
document this article has found is a complete history of allocations, which is the reason the quantity is
not computable and is a narrower statement than the one it replaced.

**FOUR SELF-RANKINGS WERE SCOPED AND ONE CONTRASTIVE CLAIM NARROWED.** The sharpest statement this
article can make became the only statement carrying both a date and a document. The article's own best
document became the document this article relies on most. The deepest difference between the borrowings
became the difference that matters most to a register. The only corroboration available became the only
corroboration this article has found.

**FOUR HAND-WRITTEN SOURCES WERE DEFINED, SWEPT, AND NEVER CITED IN THE BODY**, among them **all three
Baldwin and Clark entries, which is the modularity theory the whole commonality section rests on** and
whose title the source base already tells a story about. **A reference that appears only in its own
bibliography entry is a reference the article does not actually make.** All four are now cited where
they belong, and the verifier asserts that no hand-written source is body-uncited.

**A DATELINE PROBLEM THE GENRE PROVIDES FOR BUT THE ARTICLE HAD NOT HANDLED.** Three statements are
dated after the editorial date of 2025-12-12, all of them measurements the article made of itself rather
than events in the subject. **The genre requires the Epistemic State to say so and it did not.** A
vantage-point subsection now names all three, states that no event in the subject postdates the dateline,
and says plainly that **the hostname claim is about the date it was checked and is the only claim in the
article that could change without any document changing.**

**AND ONE PROSE COLON OF MY OWN.** The other two the scan reports are a quotation from the 1962
regulation and a document title inside a citation.

**TWO QUOTATION TRANSCRIPTIONS WERE CORRECTED AGAINST THE SCAN.** The 1962 regulation says design
redesignations and the article had the singular; and a paraphrase of the publication duty omitted that
the required description is unclassified. **A quotation must be exact and a paraphrase must not drop a
qualifier.**

**DICTION WENT FROM THREE FORMULAIC CONSTRUCTIONS TO NONE ABOVE CONCERN, AND ZERO WORDS REACH THE PEER
MAXIMUM.** Against 260 published peers no enumerated tic word reaches the maximum, `rather` being the
highest at 0.74 of it. The discovered-formula scan found the contrast device **X and not about Y** six
times, **the article says so** four times, **nothing at all** five times and **a draft of this** six
times. Each was varied across a rotation rather than replaced by one substitute, taking them to three,
two, three and two. **`is an inference` was left at nine and the reason is recorded**, since eight of
the nine are the Epistemic State's inference list where the parallel construction is the section's
function.

**AN INSTRUMENT WAS READING MATHEMATICS AS PROSE AND THE TWO STYLE CHECKERS DISAGREED.**
`pubreview.py style` reported **193 prose semicolons and eight prose parentheticals**, every one of them
a `\;` or a `\bigl(` inside a display block. Its stripper removed the `$$` delimiter lines and left the
block body, **because A363 wrote display blocks on one line and A364 writes them over three.** That is
the same defect the display-equation counter had in the equation pass. **Two instruments disagreeing
about the same question means one of them is wrong**, and the block is now removed as a block.

**STRUCTURE, GENRE AND INTEGRITY FOUND CLEAN.** Nine top-level sections in the designation anomaly's
reduced order, with the Epistemic State, Out of Scope and Conclusion at positions six, seven and eight
of nine and the Epistemic State before the end. No contraction, em dash, en dash, capitalised emphasis or
author parenthetical. No anchor undefined and no definition unused. **The apparent 1,232 orphaned anchors
are the corpus convention and A363 shows 4,452 of the same kind**, being research records cited by their
own bullet in the references listing.

**ON THE STANDING DIRECTIVE.** No length limit and no reference limit are permissions, and the genre
document forbids padding an anomaly article in the same breath. **At 1,315 definitions this is the
thinnest reference base of the four designation anomalies and the article measures why rather than
asserting it**, the report-primary share of 12.1 percent and the product-family cluster's one primary in
366 records both being reported in the article. **Nothing was added to reach a number.**

**VERIFICATION.** `verify_numbers.py` **373 checks**, passing, up from 347, now including that every
hand-written source is cited in the body, that the vantage-point statement is present, and that the
withdrawn opening and the withdrawn search claim are absent while their replacements are present.
`_verify.py` 0 errors and 0 warnings across 304 posts. `_lib/render.py` no findings across 538 pages.
`mathrot.py` 68 source display blocks against 68 rendered with zero emphasis tags. `symcheck.py` passing
across 85 declared symbols. `stylecheck.py` zero findings. `emrisk.py` and `astrisk.py` both confirm the
article adds nothing to the corpus-wide corrupted-maths count. **Twenty hand-written addresses, fifteen
fetched, four confirmed against the bibliographic index after a publisher refused the client, and one
returning neither**, that one being the Department's own portal for a document read from a web archive.

**ONE PILOT ITEM REMAINS.** The corrupted mathematics in published posts, re-measured by A363 in the
rendered pages as 133 spans across 37 pages, 104 underscore-driven and 29 asterisk-driven.

**THE WORKING TREE STILL CARRIES EIGHT DRAFTS THIS LINE DID NOT TOUCH**, re-dated from 2026-08-14
through 21 to 2126, uncommitted and excluded from this commit, as is the untracked `sa.html`.

**Date**: 2026-10-02
**Task**: **A364 PRIMARY-REFERENCE REVIEW, the third of four passes. Committed, not pushed, NOT
published.** **Reference definitions 1,164 to 1,315**, research records 1,081 to 1,228, report
primaries **110 to 159** and the share **9.5 to 12.1 percent**, lines 4,573 to 5,158, words 30,926 to
35,511, now 9 H2 and 53 H3 sections with 20 tables. Display equations held at 68.

**THE PASS'S LARGEST YIELD CAME FROM READING THE DOCUMENTS A SENTENCE THE ARTICLE ALREADY QUOTED HAD
NAMED.** The 2020 instruction states that the designator format was established on 18 September 1962 by
Air Force Regulation 66-11, Army Regulation 700-26 and Bureau of Naval Weapons Instruction 13100.7. **The
article quoted that sentence and had read none of the three.** They are one document issued three times
over, the register's compiler hosts a scan of it, and **it was read in full as nineteen page images
because the scan carries no text layer.**

**IT DEFINES THE DESIGN NUMBER IN WORDS EVERY LATER EDITION DROPPED.** `Design Number. The sequence
number of each new design of the same basic mission or type aircraft.` **The founding definition does not
say the number identifies major design changes. It says the number IS a sequence number**, which is
exactly the claim the equation pass's increment test was built to check and which the register fails in
nearly three quarters of its steps.

**AND WHERE THE MODERN INSTRUCTION OFFERS NO TEST FOR WHAT COUNTS AS A NEW DESIGN, THE 1962 DOCUMENT
OFFERS THREE WORKED EXAMPLES**, being a change in the number of engines, a change of the wing from
straight to swept or delta, and a change or relocation of the empennage. **All three are the airframe's
shape or its propulsion and not one is mission equipment.** A genus holds exactly those three constant
and swaps exactly what the 1962 test ignores. **The system that wrote the definition would have refused a
species a design number, and the system that inherited the definition without the examples gave one.**
The series letter's logistic-support criterion, by contrast, survives almost word for word from 1962
through the 2004 list and the 2005 and 2020 instructions, **so the keystone's only concrete test is
sixty-three years old rather than a recent form of words.**

**THE FOUNDING DOCUMENT ALSO DEFINES BOTH OF THE LETTERS THIS DESIGNATION CARRIES, ON FACING PAGES.** X
as a status prefix meaning experimental and X as a basic mission and type symbol meaning research. **And
it defines Q as a MODIFIED MISSION symbol meaning drone, not as a basic mission**, so a modified mission
symbol could not carry a design-number series of its own. **The designation XQ-67A could not have been
written in 1962**, and not because the aeroplane did not exist.

**AND IT STATES THE ARRANGEMENT THE WHOLE ARTICLE HAS BEEN CIRCLING.** `The requesting service will
indicate the desired mission or type symbols. The assignment agency will assign the applicable design
number.` **In 1962 the requester named the mission and the agency chose the number.** The 2020
instruction tells the requester to research the next-in-series from the last approved design number and
request it. **The responsibility for choosing a design number moved from the office that keeps the
sequence to the office that wants the number**, which is the precondition for a number carrying
information at all.

**THE CAVEAT THE EQUATION PASS CARRIED IS RESOLVED AND THE ANSWER NARROWS THE CLAIM.** Four editions have
now been read. **The 2005 edition, Air Force Instruction 16-401(I) of 14 April 2005, still says the
coordinating office will assign and reserve the next available consecutive design number, and the word
skip appears nowhere in it.** So the change falls between 2005 and 2020 and it is two changes, the
quantity moving from the next available number to one above the last approved, and the duty moving from
the agency to the requester. **The X-49A of 2003 and the X-58's skip of 2018 fall under the old pair and
the X-67's skip of 2025 under the new one.** The 2005 edition also calls the 16 in F-16A **the sixteenth
MDS requested** where the 2020 edition says **approved**, and a requested ordinal and an approved ordinal
differ whenever a request is refused.

**A CORRECTION, AND IT IS AN UNDER-CITATION OF THE ARTICLE'S OWN BEST DOCUMENT.** The article attributed
the cancellation of the public list to the register's compiler and to secondary coverage. **It is in DAFI
16-401 itself, twice in the text and once in its summary of changes**, which names the cancellation of
DoD 4120.15-L as the publicly accessible database and directs other Federal agencies and the public to
`data.af.mil` for the latest version. **And Change 1 of 31 August 2018 to the list, read for this pass
from a public web archive after the Department's portal refused every client, cancels nothing**; it
reassigns the office of primary responsibility and the words retire, cancel and the successor address
appear nowhere in it. **So the cancellation is a 2020 act of the Air Force instruction and not a 2018 act
of the Department list.**

**THE INSTITUTIONAL FINDING NOW HAS A BEFORE-PICTURE.** The founding regulation required the assignment
agency to publish an unclassified listing of assigned designations not less frequently than every six
months. **The October 1998 edition is approved for public release with distribution unlimited and gives
three routes to a copy.** The 2020 instruction gives one address and it does not resolve.

**AND AN INFERENCE BECAME A DOCUMENTED FACT.** The article divided the research series' absences into
those inside the register's window and those outside it, and said this series had written three of the
outside ones as real allocations. **The 2004 list carries the X-41A, the X-42A and the X-43A as approved
designators with sponsors and engine entries**, so the division is now the government's own record rather
than an inference from neighbouring articles.

**ONE MORE COUNTERPOINT FOR THE KEYSTONE, FROM THE SAME INSTRUCTION.** The 2020 issue's summary of
changes records one addition to the designator alphabet, **a status prefix `e` meaning digitally
developed, defined as aircraft engineered in a virtual environment**, and it is the only lowercase symbol
in the scheme. **In the same issue that cancelled the public list the system added a letter for how an
aeroplane was engineered and added nothing for whether it shares a chassis with another aeroplane.**

**THE AIMED THIRD SWEEP WAS AIMED AT A MEASUREMENT AND ITS RESULT IS MEASURED BOTH WAYS.** Running the
per-cluster primary share first returned the three largest clusters carrying almost nothing, being
product families at 0 primaries, modularity at 1 and commonality at 3. **The homonym probe had already
said why**, since the reports server holds 421 records for `commonality` and they are space station,
lunar and Martian hardware commonality. **The first sweep asked in aeronautical words and the server's
commonality literature is spacecraft.** Fifty-three questions in the server's own vocabulary, plus
fifteen clusters' worth of the two registries, took the pool from 9,505 to 14,384 and **bought 49 report
primaries, commonality going from 1.8 to 6.3 percent, variety and cost from 4.8 to 15.7 and flexibility
from 2.9 to 17.5.**

**AND THE HONEST RESULT IS IN THE ROW IT WAS AIMED AT HARDEST.** Product families, the largest cluster at
366 records, went from **0 report primaries to 1.** Questions about families of vehicles, derivative
designs, growth versions and common airframes bought one record. **Product family design is a
manufacturing and management literature and no rephrasing moves it into a server that does not hold it.**
Four clusters gained nothing at all, two of them deliberately.

**THE FIRST SWEEP'S COMPLETE COVERAGE TURNED OUT TO BE A PROPERTY OF ITS PHRASING.** It retrieved 745 of
745. **The third sweep retrieved 1,795 of 2,966 and walked out on two questions**, because those
questions reach a literature large enough to walk out of, and the article now says so rather than
claiming reach.

**TWO INSTRUMENTS WERE NARROWED RATHER THAN SATISFIED.** `stylecheck.py` flagged the parentheses in
`AFI 16-401(I)`, which is the document's official name and cannot be removed without misnaming it. **A
parenthetical is the author interrupting, and an interruption is preceded by a space while a name suffix
is not**, so the check now requires whitespace before the parenthesis. It also now excludes inline code
spans, on the ground it already applies to tables and reference definitions, **because an identifier in a
code span is apparatus and not the author's punctuation.**

**AND A DUPLICATE KEY IN A DICT LITERAL WAS FIXED BEFORE IT COULD BITE.** Merging the second sweep into
the gate runner left `source` assigned twice in one literal, where the later silently won. **It happened
to be correct and it is the kind of defect that survives until somebody reorders the lines**, so the
source is now normalised once and the sweep number recorded separately.

**VERIFICATION.** `verify_numbers.py` **347 checks**, passing, up from 322, **with the third sweep's
before-and-after measured against a frozen baseline rather than claimed**, including assertions that the
merge lost no record, that the product-family cluster's honest negative is still negative, and that the
third sweep did NOT achieve complete coverage. `_verify.py` 0 errors and 0 warnings across 304 posts.
`_lib/render.py` no findings across 538 pages. `mathrot.py` 68 source display blocks against 68 rendered
with zero emphasis tags. `symcheck.py` passing across 85 declared symbols. `stylecheck.py` zero findings.
**Twenty hand-written addresses, fifteen fetched, four registry-confirmed and one returning neither**,
that one being the Department's own portal for a document this pass obtained from a web archive instead.

**THE PERIOD PROFILE, BESIDE THE FRACTION.** Of 1,228 research definitions, 1,170 carry a year, the
median is 2011, the range runs 1900 to 2026, **426 records are from 2015 onward at 36.4 percent and 214
predate 2000.**

**WHAT REMAINS NAMED AND UNREAD.** DoD Directive 4505.6 of 6 July 1962, which the founding regulation
implements, and DoD Directive 4120.15 of 2 May 1985, under which the lists are reissued. **Both are named
in documents this pass read and neither has been read.** The Broad Agency Announcement of September 2020
also remains unread.

**THE WORKING TREE STILL CARRIES EIGHT DRAFTS THIS LINE DID NOT TOUCH**, re-dated to 2126, uncommitted,
and excluded from this commit, as is the untracked `sa.html`.

**Date**: 2026-10-02
**Task**: **A364 EQUATION-DENSITY REVIEW, the second of four passes. Committed, not pushed, NOT
published.** **Display equations 26 to 68**, lines 4,020 to 4,573, words 26,616 to 30,926, inline
expressions 124 to 185, the symbol table 50 entries to 85, references held at 1,164, in 9 H2 and 48 H3
sections with 18 tables.

**A SCAN DROVE THE PASS AND IT FOUND 172 CANDIDATES.** `eqscan.py` lists every prose line carrying a
figure with no display block within six lines, after excluding dates, years, designation numbers,
contract numbers, document numbers and status codes, **because none of those is a result**. The author
then decided which candidates were relations. **The excluded families are measured rather than assumed**,
and the exclusions are why the output was readable at all.

**THE PASS ADDED ONE NEW MEASUREMENT AND IT TESTS THE INSTRUCTION'S OWN DEFINITION OF A DESIGN
NUMBER.** The instruction says the 16 in F-16A is the sixteenth approved designator for a fighter, which
is a claim with a testable consequence. **The ordinal form cannot be tested against this register**,
because it opens in August 1998 and most series were already numbering, **so the claim was differenced**
and each new design number should exceed the previous new one by exactly one. **The research series gives
15 of 22 steps exactly one, or 68.2 percent, and the unmanned series 9 of 29.**

**AND THE FIRST VERSION OF THAT MEASUREMENT WAS WRONG IN TWO WAYS, BOTH NOW RECORDED IN THE ARTICLE.**
It counted the X-40B as a new design number, **which is the register's own edge misread as a government
decision**, since a series letter of B or later is evidence that the number predates the row. And it
conflated skipping with out-of-order allocation, **because an allocation below the pointer makes its own
increment negative and inflates the next one by the same amount.** A second measure was added for that,
the advance of the running maximum, with the identity that the advance is zero exactly when the
allocation is at or below the pointer.

**THE POINTER MEASURE PRODUCES THE ARTICLE'S CLEANEST TABLE.** The research series has 22 steps, **16
advances of exactly one, 5 greater than one and 1 of zero**, and the five gaps are exactly this series'
own five documented losses, being the 49 passed for a round fifty, the refused 52, the borrowed 58, this
article's 67, and the leapfrogged 69 to 75. **Eleven numbers skipped and exactly one ever filled.**

**AND THE RESEARCH SERIES IS THE BEST-BEHAVED SEQUENCE IN THE REGISTER, WHICH SHARPENS THE FINDING.**
Among the three basic missions with at least twenty steps the rates are 72.7 percent for the research
series, 51.5 for missiles and 44.8 for unmanned, against 50.4 percent register-wide. **The X-67 was lost
from the one numbering sequence that mostly does follow the rule.**

**THE PASS'S LARGEST FINDING IS THAT THE RULE CHANGED, AND WRITING DOWN THE RELATION IS WHAT FOUND
IT.** The pointer passed the 49 on 2002-02-13 and the X-49A was allocated 464 days later, filling a gap
the pointer had already crossed. **The joint instruction of 9 September 1994, in force at the time, says
the office will assign the next available consecutive design number**, and a passed number is available.
**The 2020 instruction replaced that with the last approved design number and added a refusal of requests
in reverse or skipped sequences.** So the X-49A is the instruction obeyed under one rule and would be
refused under the other. **The X-67 is the first number in the research series to be skipped under a rule
that makes skipping permanent**, and the X-58's slot was recoverable for its first two years while
nobody wanted it.

**A CLAIM WAS WRONG AND THE ARITHMETIC CORRECTED IT INTO SOMETHING STRONGER.** A draft said the three
competing definitions of the next number all coincided at 67. **The lowest-never-allocated definition
returns 1 over this register**, because the X-1 through the X-36 are outside the window, **so the
quantity the 1994 instruction named is not derivable from the only public source of the thing it
governs.** Of the two definitions that are computable, **both gave 67 on the day the X-68A was approved**,
which is sharper than the claim it replaced.

**THE KEYSTONE'S FORMAL STATEMENT WAS ADDED AND IT IS TWO DIFFERENT FAILURES RATHER THAN ONE.** For a
design number to index a purpose the purpose map must be injective, and **6 of 490 distinct descriptions
are shared across numbers**. For it to index an organisation the maker map must be well defined, and
**27 of 235 mission-and-number pairs name more than one leading firm**. So the purpose map is a function
and is not injective, while the maker map is not a function at all.

**AND THAT EXPOSED A DENOMINATOR THE ARTICLE WAS QUOTING TWO WAYS.** The same 27 numbers are 11.5
percent of all pairs and 26.2 percent of the pairs carrying more than one row. **Both were in the
article and neither named its denominator**, which is now displayed as two fractions with the same
numerator.

**THE COMMONALITY MODEL GAINED ITS DERIVATIVES AND ITS LIMITS, AND THE LIMITS BOUND THE PROGRAMME'S
CLAIM.** The sharing slope tends to minus one as the family grows, so **no family however large saves
more unit cost than the fraction it shares**, which at three fifths is 60.00 percent against the 13.63
percent three species actually reach. Inverting the cost factor for the family size needed, **a thirty
percent saving at those parameters needs about nineteen species on one chassis** and the programme named
two. The linear-penalty curvature is displayed and is negative, which is why that model has no interior
optimum, and **the quadratic threshold's limit is 300 percent**, so a large enough family tolerates a
tripling of cost before an interior optimum appears.

**AND THE REFRESH ARGUMENT GAINED THE DERIVATIVE THAT MAKES IT A CLAIM ABOUT EVERY INTERVAL.** The
shortfall's gradient is 0.08940 per year at a three-year freeze against 0.01238 at fifteen, a ratio of
7.218, **so the first year of delay costs about seven times what the fifteenth does.** The long-freeze
asymptote is also displayed and is within a tenth of a point of the exact value at fifteen years.

**THE SURVEY'S OWN BOOKKEEPING IS NOW RELATIONS RATHER THAN ASSERTIONS.** The pool identity, the
officiality partition into four exhaustive and disjoint states, the absence partition into inside and
outside the register's window, the reference-base partition into four provenances, the coverage ratio,
the report-primary share and the mean clusters per record. **Each is asserted in the verifier**, so a
record or a row falling into none of a partition's parts, or into two, fails the build rather than
quietly changing a total.

**FOUR SYMBOL COLLISIONS ARRIVED WITH THE PASS AND THREE WERE RESOLVED BY RENAMING.** The pool took a
capital pi because the part count is $P$, the cluster set took a script form because the common part
count is $C$, the discriminant took a capital theta because $\Delta$ is a difference throughout, and
**a row inside the well-definedness condition took $w$ because $r$ is the progress ratio.** Three further
pairs differ only in case and the article says so, since $D$ counts refused records while $d$ is a design
number.

**AND `symcheck.py` HAD A BLIND SPOT THAT THIS PASS WOULD HAVE WALKED STRAIGHT PAST.** It treated
`\mathcal` as structural and stripped its contents, **so every script letter was invisible and the five
new script sets this pass added would have been validated by nothing.** It now keeps the script form as
a compound token, and it immediately reported four undeclared sets. The symbol table is 85 entries and
every token resolves.

**VERIFICATION.** `verify_numbers.py` **322 checks**, passing, up from 256, **with every new gradient
re-evaluated by a central difference on the function it is the gradient of, every limit by evaluation at
ten to the fortieth, the inversion by a round trip through the forward relation, and the increment and
pointer walks redone with a different loop and sort key.** The two walks are asserted to agree on their
step count. `_verify.py` **0 errors and 0 warnings across 304 posts**, the two `progress-stale` warnings
having resolved themselves when the other line published its series. `_lib/render.py` no findings across
538 pages. `mathrot.py` **68 source display blocks against 68 rendered brackets** with zero emphasis
tags. `stylecheck.py` zero findings. `emrisk.py` and `astrisk.py` both confirm the article adds nothing
to the corpus-wide corrupted-maths count.

**THREE VERIFIER DEFECTS WERE FOUND BY IT FAILING, WHICH IS THE PATTERN THIS SERIES KEEPS MEETING.** The
emitter divided the pointer's eleven skipped numbers by the allocation rate where the prose defines the
quantity over the ten numbers actually absent, **the difference being the X-49 which the pointer skipped
and which is present in the register.** A limit check at ten to the ninth failed by three quarters of a
percent, because the sharing slope goes as a power of 0.2345 and a billion is not large at that
exponent. **And a tolerance derived from the last printed digit failed on a correctly rounded figure**,
because the computed value carried floating-point noise eight parts in a billion beyond the exact half.

**THE WORKING TREE CARRIES EIGHT DRAFTS THIS LINE DID NOT TOUCH.** `android_development_on_freebsd`,
`android_unit_testing`, three `claude_code_getting_started` drafts, `phoenix_json_api_authentication_with_guardian`
and two solana drafts have been re-dated from 2026-08-14 through 21 to **2126**, a century forward, day
and time preserved. **They are uncommitted, they are not this line's work, and they are excluded from
this commit.** The untracked `sa.html` is excluded as before.

**Date**: 2026-10-02
**Task**: **A364, X-Planes: X-67, the Slot Taken by XQ-67A, DRAFTED.** Committed, not pushed, and
**NOT PUBLISHED**, publication of the series never having been authorised. **Sixty-eight of
seventy-two drafted, four remain.** The three remaining passes on this article are equation density,
primary references and the publication review.

**STATE 4,020 lines, 26,616 words, 26 display equations, 124 inline expressions, a 50-entry symbol
table and 1,163 reference definitions**, in 9 H2 and 42 H3 sections with 16 tables, citing 1,081
research records across 15 clusters from a pool of 9,505 distinct records. **This is the shortest of
the four designation anomalies and that is deliberate**, the genre document being explicit that
padding an anomaly article is worse than leaving it short.

**THE KEYSTONE IS THAT THE REGISTER'S ENTRY FOR THIS DESIGNATION IS AN ANALOGY.** The compiler writes
that just like the X-58 the slot was skipped after the allocation of the XQ-67A, and that is the whole
of the public reasoning. **The X-58's entry carries reasoning, a confidence grading and the claim that
the slot is empty. The X-67's carries none of the three.** His treatment of the rest of the family
shows he is not being careless, since he writes `unclear` for the XRQ-72A and `probably` for the
XRQ-73A. **He is citing a precedent rather than withholding an argument**, and the X-67 is the point
at which a precedent becomes a rule.

**SO THE ARTICLE HAD TO SUPPLY THE EVIDENCE THE REGISTER ASSERTS WITHOUT, AND THERE IS A TEST.** A
borrowed number should equal its claimed source series' next number at the moment of the borrowing and
should equal no other series' next number. **Run against every out-of-sequence unmanned design number
carrying a full date, the test fires twice in six, on 58 and 67, naming the research series both times
and matching nothing on the other four.** A null model drawing uniformly from two-digit numbers above
the unmanned ceiling gives a tail probability of 0.03159, about one in 31.7, **which the article
reports as weak alone and decisive in combination with three other facts.**

**AND THE INSTRUCTION SHOWS THE QUESTION OF WHO SKIPPED IT IS MALFORMED.** Two sentences neither the
X-58 article nor any other in this series had cited. The request procedure defines the next designator
from **the last approved design number** of the same basic mission, and the eligibility criteria state
that **requests are not accepted for designators in reverse or skipped sequences**. **Nobody had to
decide to skip the X-67. Somebody had to ask for the X-68**, 763 days later, and from that approval
the number was unrequestable for ever. **The X-58 article concluded the absence was permitted and
unexplained. This one adds that it is irreversible by rule and names the moment it became so.**

**THREE READINGS OF THE X-68A AND THE RECORD CHOOSES NONE.** That the design-number pool is shared
across basic missions in practice, which the instruction's own definition denies. That the allocating
office exercised its unconditioned discretion to skip. That the pointer was read off a list sorted by
design number within a vehicle type, which places the XQ-67A among the sixty-sevens. **All three
predict an X-68A, no X-67 row and no public document**, so the article states that the slot is
unrequestable, states when, and declines to say who.

**AND THE COMPILER'S OWN NEXT-NUMBER FIGURE CANNOT SETTLE IT, BECAUSE IT PRESUPPOSES THE ANSWER.** He
publishes the next available research number as 69 while the register carries an X-76A, so his
convention is one above the highest number **he judges** to have been allocated in sequence. **He
applies it consistently across the research, unmanned and fighter series, which is the test of whether
it is a convention or an error**, and it is not the convention the instruction states. Read literally
the instruction gives 77.

**THE SECOND CASE FALLS ON THE FAR SIDE OF A LINE THE FIRST DID NOT, AND THIS IS THE DEEPEST
DIFFERENCE.** The XQ-58A's description is official Department wording and the XQ-67A's carries the
mark saying it is not. **So in 2017 the government said what the aeroplane taking the number was for
and in 2023 it did not.** What survives the mark is the date, the designation, the contractor and the
engine. **The government will officially record which engine is in the aeroplane that consumed the
X-67 and will not officially record what it is for.**

**THE AEROPLANE WAS BUILT TO DENY THE PREMISE THE NUMBER RESTS ON, AND THAT IS WHY IT IS IN THE
ARTICLE AT ALL.** A design number marks a major design change within a basic mission, presuming one
design identity. The Off-Board Sensing Station existed to prove a common chassis carrying replaceable
species, which the laboratory called a genus and species approach in those words. **By the
instruction's own criterion a species belongs on a series letter**, the only concrete test it offers
for that level being whether the change alters the logistics support of the vehicle, **and a common
chassis is built so that it does not.**

**THE REGISTER SHOWS THE SAME THING FROM BOTH SIDES AND BOTH MEASUREMENTS ARE NEW.** Six pairs of
design numbers in the whole register carry identical official descriptions, and in five of the six the
contractor is the only differing field, so the number does not index the stated purpose. **Yet 27
design numbers survive a change of leading firm, one of them across seven firms and ten series
letters, so it does not index the designer either.** What it indexes is a request, and the instruction
never defines what a request is for.

**THE ARITHMETIC IS NEW TO THIS SERIES AND SAYS THE VALUE WOULD LIE IN THE CADENCE RATHER THAN THE
PARTS.** At three species and an eighty-five percent learning curve a three-fifths shared fraction
buys 13.63 percent of unit cost. **A sharing penalty linear in the shared fraction has no interior
optimum at all, which is the model telling the reader about its own linearity**, and a penalty rising
as the square has one only above three times the square of the sharing slope, 15.47 percent at three
species. **At a thirty percent penalty the optimum shared fraction is 44.63 percent, saving 4.76
percent, while full commonality is 0.48 percent worse than sharing nothing.** By contrast shortening
a design freeze from fifteen years to three takes the capability shortfall from 80.87 to 37.82
percent. **Every input to both calculations is unpublished and the article inverts the break-even
rather than asserting a saving it cannot measure.**

**THE AWARD RECORD CONTRADICTS THE REPORTED CONTRACT VALUES IN BOTH DIRECTIONS AT ONCE.** Trade
coverage reported matching 17,700,000 dollar contracts with a 49,000,000 dollar ceiling. **The award
record shows one at 67,986,112 dollar, 38.75 percent above that ceiling, and the other at 16,003,302
dollar, 9.59 percent short of its base.** One contract grew past the maximum its own option defined
and the other stopped before its minimum. **And the laboratory's own account of deciding at the end of
2021 disagrees with contemporary reporting placing the selection in February 2023**, by about a year,
which the article names and does not resolve.

**THE INSTITUTIONAL FINDING IS LARGER THAN THE DESIGNATION.** The request procedure requires research
into the last approved design number in an official source. **The printed list was cancelled in 2018,
and the hostname its cancellation notice named as successor returns no answer from the authoritative
nameservers for its own zone**, checked on 2 October 2026 with a sibling in the same zone resolving
normally. **The article states the narrow version**, which is that the official source is not reachable
publicly at the address its own cancellation notice named, since a Department network may resolve
internally. **So every public claim about the X-67, including every claim in this article, passes
through one private compiler's reconstruction obtained under the Freedom of Information Act.**

**AN OPEN DECISION IS RESOLVED AND THE RECORDED FIGURE WAS RIGHT.** The research series' officiality
split recomputes as 21 official, 7 with an unofficial description, 2 entirely unofficial rows and 1
partly, which agrees with the recorded twenty-one, nine and one **provided wholly unofficial merges
two different claims.** A row-level mark says the allocation itself is absent from officially released
data; a cell-level mark says the allocation is official and its stated purpose is the compiler's.
**The recorded figure is correct and the category is too coarse for this article, because the XQ-67A
is in the second group and that distinction is the whole comparison.**

**TWO MEASURED NEGATIVE RESULTS, BOTH REPORTED RATHER THAN HIDDEN.** The reports server holds 745
records across 62 questions and the sweep retrieved all 745, **which is the first complete coverage in
this series and a statement about the server rather than the sweep.** The report-primary share is 9.5
percent, the lowest recorded, against 30.6, 45.0, 39.5 and 28.3 in the preceding four articles,
because commonality and product family design are a manufacturing and management literature. **And the
programme's own vocabulary is unsearchable**, `common chassis aircraft` returning one record about a
different vehicle, `attritable aircraft` returning none, `genus` and `species` returning forty
biological and chemical results in forty, and `OBSS` returning ten about the Space Shuttle's Orbiter
Boom Sensor System.

**FIVE DEFECTS FOUND, AND FOUR OF THE FIVE WERE THE INSTRUMENT RATHER THAN THE SUBJECT.** A remembered
digital object identifier was written into the reference file **in the belief that it was correct** and
resolves to nothing, the real one having been in the harvest throughout, which is A363's placeholder
defect in a worse form because no rule about placeholders catches it. The subject gate **refused the
article's own foundational source** because its title carries no engineering noun. A frozen occurrence
count **returned zero for a phrase plainly in the article**, the body being hard-wrapped so the phrase
carries a newline. An inherited display-equation counter saw only one-line blocks and reported zero
against twenty-six. **And an officiality parser read one of the register's three markup levels and
reported a confident wrong count twice, at a different level each time.**

**VERIFICATION.** `verify_numbers.py` **256 checks**, passing, importing neither the measurement module
nor the derivation module and **parsing the register again with a different parser**, with the null
model's tail probability checked a second time by simulation and the commonality optimum found by a
golden-section search that does not know the first-order condition. `_verify.py` 0 errors and no new
warnings. `_lib/render.py` no findings across 550 pages. `mathrot.py` matching 26 source display
blocks against 26 rendered brackets with zero emphasis tags in any expression. `symcheck.py` passing
across 50 declared symbols after four collisions were resolved. `stylecheck.py` zero findings.
`emrisk.py` and `astrisk.py` both confirm the article adds nothing to the corpus-wide corrupted-maths
count. **Fifteen hand-written addresses, eleven fetched, four confirmed against the bibliographic
index after a publisher refused the client, and one returning neither**, that one being the
Department's own cancelled list which the article records as not read.

**A NOVELTY OVERCLAIM WAS CAUGHT AFTER THE FIRST COMMIT AND CORRECTED IN PLACE.** The article had
said that neither of the two instruction sentences it quotes had been cited by any earlier article in
this series. **Grepping every draft and post refutes half of it**, the X-58 article having cited the
research step in its non-standard-aircraft branch. **The eligibility criterion refusing requests in
skipped sequences is the one that is new, and it is also the one the irreversibility argument rests
on**, so the correction narrows the claim without weakening the argument and the article records it.

**TWO ITEMS REMAIN FOR THE PILOT AND BOTH ARE OLDER THAN THIS ARTICLE.** The corrupted mathematics in
published posts, re-measured by A363 in the rendered pages as 133 spans across 37 pages. And the
publication decision on A376, which is line two of the handoff. **The A358 and A359 officiality
correction is resolved above.**

**Date**: 2026-10-02
**Task**: **A376 IS PUBLISHED and the `war_with_china` series is complete at three articles.**
Published on the pilot's instruction as
`_posts/2026-08-13-balance_of_power_after_war_with_china.markdown`, following a pathological word
usage pass in which **the enumerated tic class came back clean against 259 peers** and one
discovered formula was over the limit and is now under it. See the A376 sections below.

**THE PUBLICATION USED THE TWO-COMMIT PATTERN.** The draft commit is `3ce299f` and the move is its
successor. **A374 and A375 now read Part 1 of 3 and Part 2 of 3 and neither URL moved**, so no
`redirects/` entry is owed. **The `progress-stale` warnings are gone**, not by a tooling change but
because the two-concurrent-series condition that produced them no longer holds. `./_check.sh`
reports **0 errors and 0 warnings across 304 posts**, a clean build, and no rendered findings across
469 pages.

**ONE ITEM REMAINS OPEN ON THIS LINE AND IT IS NOT MINE TO DECIDE.** Commits `1dd90d0` and `33fd7fe`
carry this line's staged work under the other line's commit messages. The content is intact and
verified byte-identical on the remote; only the attribution is wrong, and the history was
deliberately not rewritten because those commits are pushed.

The previous report follows.

**Date**: 2026-10-01
**Task**: **A363, X-Planes: Boeing X-66, ALL FOUR PASSES COMPLETE.** Committed and **PUSHED** on the
pilot's instruction. **NOT PUBLISHED**, and publication of the series has never been authorised.
**Sixty-seven of seventy-two drafted, five remain.**

**FINAL STATE 10,795 lines, 59,564 words, 83 display equations, 188 inline expressions, an 84-entry
symbol table, 4,537 reference definitions, 21 H2 and 60 H3 sections and 24 tables**, citing 4,436
research records across 17 clusters with 1,256 report primaries at 28.3 percent, a period count of
1,790 at 42.6 percent, median year 2012 and a range from 1921 to 2026. **Four commits for four
passes**, which is the rhythm the handoff asks for.

**THE PUBLICATION REVIEW FOUND THE ARTICLE CONTRADICTING ITSELF, WHICH IS THIS SERIES' RECURRING
DEFECT.** A heading read *Three Things the FY2026 Supplement Says That Nothing Else Does* and the
first of the three was that it uses a word the agency's press item avoided. **The same paragraph
then conceded that the press item uses that word too**, for a different object. The concession was
right and the heading and lead were wrong. Both were rewritten and the honest statement now leads.

**THIRTEEN RANKINGS WERE SCOPED TO WHAT THE ARTICLE MEASURED AND ONE WAS SIMPLY FALSE.** It called
the centroid argument **the only independent confirmation** of a closed form that the same paragraph
confirms twice. It called the fold **the single largest number in this article** when the article
carries a ratio of 10,316. It ranked an input, a service to the reader, a thing an assertion can do,
and the most interesting passage of a contractor report. **Each now names its comparison set, is
marked as a judgement, or is gone.**

**AND A FACTUAL ERROR IN AN AERODROME CODE.** The article had the Boeing 747-8 at Code E. **It spans
about 68.4 metre, which is in the 65-to-80 band and is therefore Code F.** The aeroplane that reaches
Code E is the 777X with its wingtips folded, which the same sentence already named. **The corrected
passage is stronger**, because the 777X folding across a code boundary is precisely the manoeuvre
this article says the X-66A would need, and it is already certificated.

**THREE COMPUTED FIGURES WERE TYPED AS LITERALS AND ARE NOW SLOTS**, being the before-sweep primary
share and the gate's own pattern and test-case counts. **That is the A362 defect class**, where one
hard-coded pool size went stale by two thousand records and the publication review had to find it by
hand.

**FOURTEEN SMALL COUNTS ARE NOW SPELLED AT THE EMITTER RATHER THAN IN THE PROSE**, so the convention
cannot drift when a count changes, and the verifier reads them back through the shared library's
words-to-integer helper.

**DICTION WENT FROM ONE WORD ABOVE THE PEER MAXIMUM TO ZERO.** `fairly` appeared three times where no
peer in seventy-five used it once. **It was not a hedge but the report's own criterion**, so the three
uses were varied across a rotation rather than deleted, to an equal footing, like-for-like, and on
equal terms.

**FOUND CLEAN.** Prose style, with every parenthetical and both semicolons outside maths proving to be
inside block quotations except one statutory subsection citation that cannot be written otherwise.
Structure, all twelve of the genre's sections present and in order among twenty-one. The dateline,
with every post-dateline year proving to be a future date stated by a primary document. Reference
integrity, with no anchor undefined and no definition unused.

**VERIFICATION.** `verify_numbers.py` **158 checks** and `neweqns.py` **94 checks**, both passing,
the latter importing neither the calculation module nor the equation pass's own. `_verify.py` 0
errors and no new warnings. `_lib/render.py` no findings across 549 pages. `mathrot.py` matching 83
source display blocks against 83 rendered brackets with zero emphasis tags in any expression.
`symcheck.py` passing across 84 declared symbols. **Thirty-five hand-written addresses, 25 reached
and 10 refused by one publisher's bot policy, every one of those ten verified in the registry by
title, venue and year.** `emrisk.py` and `astrisk.py` both confirm A363 adds nothing to the
corpus-wide corrupted-maths count.

**TWO ITEMS REMAIN FOR THE PILOT AND BOTH ARE OLDER THAN THIS ARTICLE.** The A358 and A359
officiality correction, now surviving five articles. And the corrupted mathematics in published
posts, which this article's new instruments have **re-measured in the rendered pages as 133 spans
across 37 pages, 104 underscore-driven and 29 asterisk-driven**, where the recorded figure was 72
source-side pairs and the asterisk cause was outside the existing instrument's model entirely.

The older reports follow, newest first. **Nothing below this block was rewritten.**

---

## A376, Pathological Word Usage Pass

**Lines 4,442 to 4,440, author prose 21,118 words once quoted material is excluded.** Display
equations held at 89, references at 202. **NOT PUBLISHED.**

**THE ENUMERATED TIC CLASS IS CLEAN AND THAT IS THE MAIN RESULT.** Against **259 published peers**,
**zero of the seventy watched tic words reach the corpus maximum**. `specific`, the word that caused
the original corpus-wide problem, stands at **3 uses and 0.13 per thousand against a natural rate
near 1.7**, so the article is below ordinary usage rather than above it. The seventeen words that do
exceed every peer are all subject nouns, and each was checked by collocation rather than asserted
clean. `great` is 71 percent `great power`, `share` carries six distinct content modifiers, `median`
four. Those are the documented term-of-art signature.

**WHAT THE ENUMERATED CHECKS COULD NOT SEE WAS A SENTENCE SHAPE.** `tics` tests seventy known words
and `report` tests twenty-two known constructions, so a formula peculiar to one article is invisible
to both. Scoring every repeated sequence against the peer maximum found **`which is a` at 1.37 times
the highest rate in any article this author has written**, carried by `which is a reason to` five
times and `which is a defensible X` four times. A second family, `worth noting` and `worth stating`
and their relatives, stood at **1.02 times the maximum with its head member used by no peer ever**.
**Both are now under the maximum**, at 18 and 2 uses, across 29 edits.

**A QUOTATION IS OTHER PEOPLE'S WORDS AND THE INSTRUMENT WAS COUNTING THEM AS MINE.** `prose` strips
reference link text on exactly that ground and keeps block quotations. With 124 of them, **7.0
percent of what the instrument attributed to the author was quoted material**, and the bias runs one
way, because a larger denominator lowers every rate and a lowered rate hides a tic. Every figure
above was recomputed with quotations stripped from **both** sides, since correcting only the article
is the opposite error. **The clean verdict survived the correction**, moving `rather` from 0.86 to
0.94 of the maximum without crossing it.

**I BROKE THE ANTI-SUBSTITUTION RULE WHILE OBEYING IT.** Four of the replacements reached for `should
therefore be`, turning a construction used once into one used four times. Only diffing the introduced
phrases against the original caught it, and two were varied back. **Checking the target construction
alone reports success**, which is why the rule now says to re-measure what the edit introduced.

**TWO EDITS WERE GRAMMATICALLY WRONG AND ONE DROPPED A CLAIM.** Two replacements hung an independent
clause off a relative clause, which the originals did not do, and were repaired. One conjoined two
facts where the original asserted a causal relation between them, and the relation was restored.
**All three were found by reading the passages, not by any check**, which is the standing limit on
this kind of pass.

**TWO MEASUREMENTS WENT INTO THE LIBRARY RATHER THAN A SCRATCH DIRECTORY.** `diction.py` records that
its predecessor was lost after being copied into four article directories, so `author_prose`,
`quoted_share` and `phrase_outliers` are now in `_lib/diction.py` with a `formulas` CLI mode and
**four new tests, 124 of 124 passing**. **`prose` is deliberately unchanged**, because every rate
`_verify.py` has reported and every exemption reason recorded against one was measured with
quotations included. **`_verify.py` output and `tics` output were diffed before and after and are
byte-identical**, so the other line sees no change.

**NOT ACTED ON, WITH REASONS.** `sets out the` sits at 1.93 times the maximum on **2 uses** against a
peer maximum of 0.05 per thousand, which is small-number noise. `which is not` at 1.13 on 4 uses, all
four substantively different. `this article` at 84 uses is heavy self-reference but 0.83 of the
maximum, and `rather than` at 98 is the article's core contrast device at 0.93. **Acting on those
would be churn, and an unactioned measurement is only acceptable with a reason recorded.**

**VERIFICATION.** `_verify.py` 0 errors and the same 2 known `progress-stale` warnings. Scratch
production build with A376 staged as a post, **469 pages, `_lib/render.py` no findings**. **89 source
display blocks against 89 rendered brackets.** Inline dollar parity even at 24. No unresolved
reference pair, no unrendered Liquid, no raw delimiter. No em-dash, en-dash, semicolon, parenthesis
or contraction in any added line.

## A363, Publication Review

**Lines 10,784 to 10,795, words 59,517 to 59,564.** Display equations held at 83, references at
4,537, the symbol table at 84. Committed and **PUSHED**. **NOT PUBLISHED.**

### The Article Contradicted Itself and the Heading Was the Wrong Half

**A heading read *Three Things the FY2026 Supplement Says That Nothing Else Does*, and the first of
the three was that the supplement uses the word pause where the agency's press item avoided it.**
Three sentences later the same paragraph conceded that the press item uses the word too, applied to
the flight-demonstrator work rather than to the project. **The concession was correct and the
heading and the bold lead were not.**

The heading is now *Three Things the FY2026 Supplement Says Plainly*, and the lead states what is
actually true, which is that **the agency used both words on the same day for different objects and
the budget document is the one that says so without a headline over it.** This is the defect class
this series keeps meeting, an article refuted by something it says about itself a few lines later.

### Thirteen Rankings Scoped, and One That Was False

**One was not a scoping problem but an error.** The article called the centroid argument **the only
independent confirmation** of the root-moment closed form, in a paragraph that goes on to report a
second confirmation by quadrature at six stations. **It is one of two and now says so.**

**One was false on its face.** The fold was **the single largest number in this article**, which
carries a ratio of 10,316 to one and a factor of 18.17. The intended claim was about effect size and
it now reads **the largest aerodynamic effect this article computes**.

**The rest named no comparison set.** The induced-drag fraction was **the single most important
input** and is now one of the two quantities every condition is written in. Reading three budget
books was **the only way** to see the money and is now the route this article took. A declared
symbol table was **the only instrument this corpus has found** that catches a collision and now
simply catches them. Setting three figures side by side was **the most useful service this article
can perform** and is now what a reader needs. An assertion refuting its own docstring was **the most
useful thing an assertion can do** and the sentence survives without the ranking. The aeroelastic
passages were **the most interesting single thing** in the report and are now the ones this article
found hardest to summarise. The flutter margin was **the single largest soft spot** and is now the
only named soft spot that could change the exponent rather than the coefficient, **which is the
reason, and the reason is what was missing.**

**Two rankings were kept with their reasons attached.** The gate-box claim is now explicitly an
inference and the one the article would defend first **because a reader can check it in one line**.
The homonym measurements now carry outside the subject **because the registries do not change
between articles**, rather than being the most transferable thing in the article.

### A Factual Error in an Aerodrome Code

**The article placed the Boeing 747-8 at Code E.** It spans about 68.4 metre, the Code F band runs
from 65 to 80, and the 747-8 is therefore **Code F**. The aeroplane that reaches Code E is the
**777X with its wingtips folded**, at about 64.8 metre against 71.8 unfolded, and the same sentence
had already named it for a different purpose.

**The corrected passage is stronger than the error was.** A wide-body that folds its wingtips across
a code boundary is precisely the manoeuvre this article argues the X-66A depends on, **and it is
already certificated**, which is the best available reason to think the gate box is negotiable for
an aeroplane worth negotiating for.

### Three Literals That Should Have Been Slots

**A362 shipped a stale pool size because one figure in the article was a hard-coded literal rather
than a slot, and the publication review had to find it by hand.** This pass scanned every numeric
literal in the prose mechanically, excluding quotations, tables, maths, dates, designations and
instrument numbers.

**Three survived the exclusions as computed quantities.** The primary share before the third sweep,
and the gate's own pattern count and its two test-case counts. **All three are now emitted**, so a
change to the gate or a re-run of the sweep cannot leave the prose behind.

**One more was a citation gap rather than a staleness risk.** The demonstrator's span of 145 feet was
attributed to trade coverage with no reference, and now says in terms that it comes from secondary
aerospace coverage and **from no primary document this article has read**.

### Small Counts, Spelled at the Emitter

**Fourteen small counts were numerals where the convention asks for words.** The fix is applied in
`emit.py` rather than in the prose, so the convention holds when a count changes, and
`verify_numbers.py` reads them back through `_lib/survey.py`'s words-to-integer helper rather than
parsing them as integers. **A convention enforced in prose is a convention that drifts.**

### Diction, One Word and Not a Hedge

**`fairly` appeared three times and no peer in seventy-five used it once.** Inspection showed it was
not a hedge but the Phase IV report's own criterion, rendered as *done fairly*, *made fairly* and
*made fairly* again. **The word carried meaning and the phrasing repeated**, which the style guide
says to fix by varying across a rotation rather than by substituting one replacement. The three now
read **put on an equal footing**, **like-for-like** and **on equal terms**. Diction reports zero
words at or above the peer maximum, and the one construction above the corpus maximum is *in other
words*, inside a quotation.

### What Was Found Clean, With the Exceptions Named

**Prose style.** Zero em-dashes, en-dashes, contractions and prose colons. **Nine parentheticals and
two semicolons, every one of which proved to be inside a block quotation or the mandated debug tag,
except a single statutory subsection citation** which cannot be written otherwise.

**Structure.** All twelve of the research-aircraft genre's sections present and in the prescribed
order among twenty-one, with the Epistemic State, Out of Scope and Conclusion in the last three body
positions and References last.

**The dateline.** Fourteen prose years after December 2025, every one of them a future date stated
by a primary document, being the agreement's seven-year term and its milestone schedule, the budget
books' out-year projections and the Ames paper's 2035 technology level.

**Reference integrity.** No anchor used without a definition and no definition unused, checked in
`verify_numbers.py` rather than by eye.

### Verification

`verify_numbers.py` **158 checks**, `neweqns.py` **94 checks**, both passing. `_verify.py` 0 errors
and no new warnings across 303 posts. The stub build succeeds against checksum-matched bytes.
`_lib/render.py` reports no findings across 549 pages. `mathrot.py` matches 83 source display blocks
against 83 rendered brackets with zero emphasis tags. `symcheck.py` passes. `stylecheck.py` reports
only the statutory citation. **Thirty-five hand-written addresses, 25 reached and 10 refused by one
publisher's bot policy, all ten registry-verified by title, venue and year.**


## A363, Primary-Reference Review

**4,064 reference definitions to 4,537, report primaries 1,035 to 1,256, the primary share 26.1 to
28.3 percent, the period count 1,641 to 1,790, and the record base's earliest year 1930 to 1921.**
Lines 9,546 to 10,767, words 53,128 to 59,396, tables 19 to 24. Committed, **NOT PUSHED**, **NOT
PUBLISHED**.

### The Aim Was Measured Before the Sweep Was Written

`before_after.py` computed the per-cluster primary share first, which is A362's rule. **The result
named `span_constraint` as the cluster with 37 records and ZERO report primaries**, and it is the
cluster carrying this article's own keystone. The other five thinnest were `aspect_ratio` at 11.9
percent, `alt_config` at 12.1, `gust_loads` at 17.1, `mdo` at 17.9 and `thin_transonic` at 24.1.

**The eighty questions were then written in the report literature's own vocabulary rather than the
subject's.** A journal asks about airport compatibility and a report asks about *airplane
characteristics for airport planning*. A journal asks about multidisciplinary optimisation and a
report names its code, being FLOPS or ACSYNT. **That is the whole difference between a sweep that
buys primaries and one that buys more of what the pool already has.**

**It worked where there was report literature.** `aspect_ratio` went from 11.9 to **23.4 percent**
and from 64 primaries to **167**, `fuel_burn` from 28.8 to **36.2**, `thin_transonic` from 24.1 to
**30.5**, `high_lift` from 32.2 to **36.1**, `mdo` from 17.9 to **20.1**. The pool went from 14,967
to 18,863 and the gated set from 4,238 to 4,744. **And the lifting-line vocabulary reached the
foundations**, bringing in **Munk's 1921 NACA Report 121 on the minimum induced drag of aerofoils**,
a 1922 report on the effect of aspect ratio on lift-curve slope, and a **1935 analysis of a strut
with a single elastic support in the span**, which is this article's jury strut by another name.

### And It Bought Nothing Where It Mattered Most

**Fourteen questions in the airport-planning vocabulary, nine of them returning no records at all,
bought one record and zero primaries.** `span_constraint` is still at exactly zero.

**The honest reading is that this is a fact about where the knowledge lives rather than a failure of
the sweep.** Airport design is a regulator's and an airport planner's subject. It is published as
advisory circulars and aerodrome annexes, not as technical reports, and a research-report server
therefore has almost none of it. **The constraint this article argues is binding has no research
literature because it is not a research question**, and that belongs in the article for the same
reason A362's three-record air-budget result did.

### The Paper the Article Said It Had Not Read

**The Phase IV report's recommendation list asked for an equivalent conceptual-level optimisation of
cantilever and truss-braced aircraft of the same technology level, to allow a more fair and
transparent comparison. A NASA Ames team published it in January 2025 and it is on the reports
server.** The article had cited it from a publisher identifier and said in terms that it had not
read it. **It is now read in full.**

**What it holds equal is the point.** Same payload of 33,750 pound, same 3,400-nautical-mile design
range, same design Mach number, same 2035 technology, same advanced direct-drive turbofan, **same
wing-fold rule above 118 feet**, and **a tube-and-wing weight calibration applied to both** rather
than each contractor's own.

| Mission | Boeing Phase IV | Ames, fuel in wings | Ames, body tanks |
|---|---|---|---|
| 900 nautical mile | 7.2 percent | **1.65 percent** | 5.71 percent |
| About 3,400 to 3,500 | 9.0 percent | 7.51 percent | 9.39 percent |

**Boeing's economic-mission figure is 4.36 times the Ames figure for a wing that must carry its own
fuel.** At the long mission the three agree within a point. **The disagreement is about the mission
and not about the aerodynamics.**

**The two causes it names and ranks are exactly the two the drafting pass had identified and could
not price.** Fuel volume, rated Significant, because the thin high-aspect-ratio wing cannot carry
all the fuel without a significant increase in planform area. Weight calibration, rated Moderate,
because the empty weight and fuel burn both rise under the tube-and-wing calibration.

### A Fourth Independent Route to the Keystone

**Its like-for-like pair is the closest thing to a measurement of the weight elasticity that this
subject's public record contains.** Four readings give **-0.00384, -0.12956, -0.00282 and +0.09926**,
every one below the exact fixed-lift target of **0.299033**, the largest short by **66.8 percent**,
and **three of four negative**, meaning the braced aeroplane at aspect ratio 19.57 weighs less than
the cantilever at 13.

**An elasticity from a pair is not a derivative** and the article says so, because the two aeroplanes
differ in span, area, thrust and altitude too. **What it establishes is magnitude**, and the
magnitude agrees with the three readings computed from the Phase IV group weight statement, which ran
from 0.0775 to 0.2749. **Four routes, one conclusion.**

**And it prices the truss directly against a cantilever of the same technology**, which is the
comparison the Phase IV report said had not been made fairly. Wing plus strut is **24.58 percent**
heavier on the contractor's calibration and **28.10 percent** on the harsher one, while **the wing
alone is only 1.38 and 4.28 percent heavier**. **The strut is almost the whole penalty**, which is a
direct measurement of the derived claim that a geometrically similar truss buys a coefficient rather
than an exponent.

### The Limit on the Keystone's Reach

**The braced aeroplane needs 25.65 percent more sea-level static thrust and cruises 4,250 feet
higher, with a 12.92 percent better start-of-climb lift-to-drag ratio.** The paper says it spends
more time climbing, which pronounces the engine-efficiency differences.

**So the aerodynamic advantage is real and the short mission spends it.** The optimality conditions
derived in this article are cruise-fuel conditions, and **an aspect ratio chosen to minimise cruise
fuel is being chosen against the wrong objective for the mission this class flies most often.** The
article now states that as a limit and does not derive a climb-inclusive condition.

### The Circular Corrected the Article a Second Time

**The article had cited the FAA's airport design circular for a table it had read in a NASA
memorandum. This pass read the circular.** Its Table 1-2 gives every bound in **both** unit systems,
and its front matter settles the question.

> Throughout this AC, U.S. customary units are used followed with "soft" (rounded) conversion to metric units. The U.S. customary units govern.

**So 118 feet and 36 metre are one boundary written twice and the circular declares which writing
governs.** The 1.3228-inch gap is the rounding the circular warns about, not a disagreement between
two authorities. **The article's framing was recast and every downstream passage with it**, and the
reproduced table now prints both unit columns as the circular does.

### Three More Primaries Each Replaced an Assertion

**The non-optimum factor now has a source.** A 1981 Grumman methodology prepared for NASA describes
the whole class of wing weight equations as a rational bending-material model with regression
constants absorbing **non-optimum weight, minimum gages and secondary loads**, which is what the
article had asserted in its own words. **The same report names flutter and divergence as the penalty
that can change an exponent**, which is the article's own named soft spot.

**The methodological thesis now has a source too.** A 2016 NASA Langley paper deriving an
aero-structural efficiency metric states that the trade differs by objective in one sentence, and
its metric is the lift-to-drag ratio that would give the same fuel consumption with a weightless
wing, coming out eleven to twelve percent below the aerodynamic value for a 737-class aeroplane.
**This article reaches the same place by the derivative route.**

**And the stationary aspect ratio turns out not to be novel.** A 1980 study under NASA contract
NAS1-16000 developed a business jet with an **aspect ratio 25 strut-braced high wing**, reported fuel
savings above twenty percent, and noted the higher cruise altitude and lower wing loading that the
2025 comparison rediscovered as a cost. **The article records the coincidence of magnitude and
declines to claim more**, because the report does not say how the 25 was chosen and a business jet is
a different class.

### What Could Not Be Got, and One Repair

**Volumes II, III and IV of the Phase IV final report are not held by the reports server at all.**
The article now says they are unavailable through this channel rather than merely unread.

**A quotation was restructured rather than altered.** The Ames summary contains a contraction and
`_verify.py` flagged it, correctly, since its contraction check does not exclude block quotations as
`stylecheck.py` does. **The source's own phrases are kept inline and its contraction is not
reproduced**, which keeps the corpus at no new warnings without putting words into a source's mouth.

### Instruments

`before_after.py` the per-cluster measurement, run twice to produce the before-and-after table.
`harvest3.py` the aimed sweep, 80 reports-server questions plus 15 and 15. `primhunt.py` the
document hunt, eleven targets and eight full texts. `fairpair.py` the like-for-like arithmetic.
`urlcheck2.py` re-run across 35 addresses.


## A363, Equation-Density Review

**38 display equations to 82, 130 inline expressions to 188, the symbol table 61 entries to 84,
9,540 lines to 9,546 and 50,183 words to 53,128.** Committed, **NOT PUSHED**, **NOT PUBLISHED**.

### What the Scan Looked For

The governing rule is the genre document's. **If the prose names a result, relies on a relation, or
quotes a value that some relation produced, the relation is shown.** A crude scan over 454
paragraphs found 139 verbal signatures of a relation in use, 87 of them in paragraphs with no
adjacent display equation, and each was then judged by hand. **Forty-four equations were added.**

### The Largest Addition Corrected the Article's Own Keystone

**The two optimality conditions rested on linearising the Breguet exponential, and this aeroplane's
usable fuel is 29,028 pound of a 145,000 pound take-off weight.** A fuel fraction of 20.0 percent
is not small, and at that fraction the linearisation overstates fuel by **11.585 percent**.

Carrying the exponential through introduces exactly one factor and nothing else changes.
**Phi equals X e-to-the-minus-X over one minus e-to-the-minus-X**, which is **0.892462** here, and
the differential of the logarithm of fuel becomes the differential of the logarithm of weight plus
Phi times the differential of the logarithm of the exponent. **Both conditions then follow
immediately.** At fixed cruise lift coefficient **nu-star equals Phi delta**, which is **0.299033**
against the drafted 0.335065. At fixed wing area **nu-star equals Phi delta over one minus Phi plus
two Phi delta**, which is **0.423797** against the drafted one half. **Both reduce to the drafted
forms as the fuel fraction vanishes**, checked at three vanishing fractions rather than asserted.

**The curvature gains one term.** It is **Phi delta times open bracket n plus one minus delta minus
Phi delta close bracket, plus Phi-prime times X times delta squared**, which also reduces correctly
and which evaluates to **0.503772** against the linearised 0.613125. **The closed form was checked
against a second difference on the exact objective, agreeing to seven decimal places, and
Phi-prime against a central difference at three hundred random points.**

**Every figure moves in the direction that strengthens the conclusion.** The stationary aspect ratio
falls from 25.100 to **23.754**, the shortfall from 28.29 to **21.41 percent**, the penalty from
1.9024 to **0.9481 percent**, and the required exponents from 2.4376 and 3.6376 to **2.1755 and
3.0832**. **The conclusion survives every weight reading and the margin narrows**, the
deliberately over-generous reading now short by **8.07 percent** rather than by the margin the
linearised figures implied, and the article says so in those terms.

**AND IT CLOSED A GAP THE DRAFTING PASS HAD TO APOLOGISE FOR.** The linearised 1.9024 percent sat
**above** the Phase II report's independently optimised bound of under 1.4 percent and needed an
explanation. The exact 0.9481 percent sits **below** it and needs none. **A discrepancy the article
was prepared to explain away turned out to be an artefact of its own approximation.**

### The Lift Equation Found a Defect in the Primary Record

**Writing down $C_L = W/(qS)$ was enough to show that the drag buildup's three stated conditions do
not hold together.** It gives a cruise altitude of 40,000 feet, Mach 0.80 and a lift coefficient of
0.695. At maximum take-off weight the lift coefficient at 40,000 feet is **0.5594**. The stated
0.695 requires either a weight **24.2 percent above maximum take-off weight** or an altitude of
**44,515 feet**, and the report's own optimum cruise altitude at maximum take-off weight, in a
different table of the same document, is **44,437 feet**. **The two differ by 78 feet, which is
0.175 percent.**

**So the lift coefficient belongs to the optimum altitude and the altitude printed beside it does
not.** It is a bookkeeping entry rather than an error of substance, since a drag buildup is properly
a function of Mach number and lift coefficient. **It is recorded because this article uses that lift
coefficient in every subsequent calculation.**

**The inversion that found it hit its bracket edge and returned it on the first attempt**, with the
direction test inverted, so the production version asserts the root is bracketed before searching.

### Two More Independent Closures, and a Closed Form That Replaced a Scan

**The equivalent flat plate area closes on the published parasite drag.** Dividing the buildup's own
27.7722 square feet by the reference area gives **0.0188017** against the published **0.01880**, an
error of **0.0092 percent**. It also prices the truss in drag, the strut and jury being **12.422
percent of the parasite drag area** and **0.0023356** as a coefficient.

**The Korn turning point has a closed form.** Substituting the secant of sweep makes the relation a
cubic whose derivative is a quadratic, so the turning point is a positive root. It gives **53.8022
degrees** at the Mach 0.80 thickness and **52.3000** at the Phase III thickness, against **53.80**
and **52.30** from a scan of seven and a half thousand angles, **with the peak values agreeing to
six decimal places**. The drafting pass had only the scan.

**The prop influence coefficient also turned out to be elementary.** The unit-load denominator is
exactly **eta cubed over three**, confirmed against quadrature to nine decimals at six stations, so
the prop force needs no numerical self-influence at all and the beam stiffness cancels.

**And the percentage-point distinction became exact.** The ratio between a percentage-point change
in a reduction and a percentage change in fuel is **the baseline over the compared value**, which is
**2.3279**. The drafting pass said about two and a half.

### A New Instance of a Documented Corruption Class

**Kramdown pairs ASTERISKS inside inline mathematics exactly as it pairs underscores, and
`emrisk.py` is blind to it.** Writing `$\nu^{*}$` twice in one paragraph produced `\nu^{<em>}` and
`\nu^{</em>}` in the rendered page.

**The rule was probed against kramdown directly rather than modelled**, which is A362's lesson about
this exact defect. Two bare asterisks in one paragraph of inline mathematics pair. One survives
alone. `\*` is inert because kramdown eats the escape. **Display blocks pass through untouched**,
so a display equation carries a bare asterisk correctly and only inline spans need escaping.

**`astrisk.py` is new and predicts it from source. `mathcorpus.py` is new and MEASURES it in the
rendered pages**, which is the only authority. Reading all 549 built pages finds **133 corrupted
mathematical spans across 37 pages, 104 underscore-driven and 29 asterisk-driven**, consistent with
the recorded 72 source-side pairs once the unit is matched since a pair corrupts two spans.
**A363 itself carries none.**

### Three Instruments Failed And Each Failure Was Instructive

**A token count found three display blocks with prose on the same line.** Dollar pairs came to 164
against 79 counted blocks, which cannot both be true. **A display block with text after its closing
delimiter is a paragraph and not a block.** A375 lost four equations to the same class.

**`mathrot.py` reported a mismatch on a page that was correct.** A LaTeX line break with optional
row spacing, `\\[4pt]`, contains the display opener the counter looked for, so the piecewise
atmosphere definition produced two more openers than closers. **The counter now requires that a
delimiter not be preceded by another backslash.** The equation pass hit this the moment it used a
`cases` environment, which the series had never done.

**`neweqns.py` CHECKED THE ATMOSPHERE AGAINST A TABLE IT COULD NOT SOURCE, WHICH IS THE A362 DEFECT
IN A NEW UNIT.** That article put five-thousand-FOOT values against a key in metres. This one typed
tabulated values from memory, failed, and then added a geometric-to-geopotential conversion **in the
wrong direction** to explain the mismatch it had itself caused, which made the high-altitude entries
fail worse. **A check against numbers the author cannot source is not a check.** What replaced it is
the two defining temperatures, the agreement of the two pressure branches at the tropopause, the
barometric exponent against its definition, and **the hydrostatic equation by central difference at
six hundred random altitudes**, which tests the model against the physics rather than against a
printout.

**A fourth failure was smaller and worth one line.** The presence checks for the new display
relations were written as regular expressions, and `\Phi` is a bad escape, so the check crashed
rather than running. **A presence test for a literal string has no business being a pattern.**

### Seven Symbol Collisions Were Resolved Before They Shipped

The new relations introduced seven base letters that would have carried two meanings each. The
established meaning kept its letter and the newer arrival was renamed. **Cap separation yielded `h`
to geopotential altitude. The flat plate area took script F because `f(u)` is the moment shape
function. Fuel volume took script V because `V` is airspeed. The record set took script R because
`R` is range. The budget projection took script P because `P` is the prop force. Block fuel per seat
took beta because `b` is span. The milestone payment took mu because `m_f` is the fuel mass.**
`symcheck.py` then needed the trigonometric functions and the layout directives added to its
structural set, since neither had appeared in this series before.

### Instruments Added This Pass

`calc2.py` the new quantities, `exact.py` the exact Breguet derivation with its limits, `neweqns.py`
94 independent checks, `astrisk.py` the asterisk prediction, `mathcorpus.py` the rendered corpus
measurement, `count.py` the structure count. `mathrot.py` and `symcheck.py` repaired.


## A363, X-Planes: Boeing X-66, Drafting Pass

**9,160 lines, 50,183 words, 38 display equations, 130 inline expressions, a 61-entry symbol
table, 4,064 reference definitions, 21 H2 sections, 54 H3 sections and 17 tables.** Committed,
**NOT PUSHED**. **NOT PUBLISHED.**

### The Keystone, and Why It Is Infrastructural Rather Than Aerodynamic

The aspect-ratio trade is derived from the lift distribution outward. An elliptic spanload gives a
root bending moment of **L b over three pi**, checked three ways. Cap area is moment over the
product of allowable stress and box depth, and integrating it across a straight-taper wing gives
bending material proportional to **the three-halves power of aspect ratio at fixed area and
thickness ratio, and to the inverse first power of thickness ratio**. The exponent is derived and
then measured numerically as 1.5000.

**The optimality condition then splits in two, which is the analytical result worth keeping.**
Holding wing area and cruise condition makes induced drag proportional to weight squared over
aspect ratio, so the stationary point is **nu equals one half exactly**, with the induced-drag
fraction cancelling out of the condition entirely. Holding cruise lift coefficient instead gives
**nu equals delta**. Both are exact, both are parameter-free in their own terms, and they call for
different aspect ratios on the same aeroplane.

**Every reading of the weight data puts this aeroplane below both stationary points.** Counting
only the 7,488 pound of bending material the report identifies gives nu of 0.0775 against a
required 0.5. Counting the whole wing group and the whole truss group at the three-halves power
gives 0.2062. **The falsifiable form is that the wing and truss together would have to grow as
the 3.64 power under one criterion or the 2.44 power under the other.**

**And then the tone reverses, because the optimum is flat and the flatness has a closed form.**
The curvature at the fixed-lift stationary point is exactly **delta times (n + 1 - 2 delta)**,
which is 0.6131 here, so a 28.3 percent shortfall costs **1.90 percent** in fuel. **The Phase II
report, by a full multidisciplinary optimisation over span limits nine years earlier, reported
under 1.4 percent for all further span beyond 170 feet.** Two routes sharing no arithmetic agree
on magnitude and sign, and the gap is explained by the field-length and range constraints the
optimisation had active and the expansion does not see.

### The Gate Box, Which the Dead Reference Forced Into Better Shape

**The address sweep found the ICAO publications page unreachable.** Replacing it meant going to
the Airplane Design Group table reproduced in NASA/TM-20250002858, and that table is **in feet
with exclusive bounds**. Group III runs from 79 feet up to but not including 118, and Group IV
from 118 up to but not including 171.

**So the fold station is not near a boundary. It is exactly on one, to the inch, with a margin of
exactly zero.** And because the bound is exclusive, a span of exactly 118.000 feet is a Group IV
aeroplane. The memorandum's own wording is **less than 118 feet**, while the Phase IV report puts
the fold **at 118 feet**. **Whether that is a rounding, an unrecorded inch, or a genuine gap
between two NASA documents is not settled by the record and the article says so.** ICAO's bound of
36 metre is 118.1102 feet, **1.3228 inch looser**, so the same fold clears Code C and not Group III.

**The fold is worth 35.96 percent in lift-to-drag ratio**, because the Code C box permits aspect
ratio 9.427 at this area against the 19.565 the fold buys. **And 9.427 is essentially the aspect
ratio of the conventional single-aisle fleet**, whose own comparison baseline in the report carries
10.41. The inference the article draws, and labels as an inference, is that **the aspect ratio of
the fleet is an airport number rather than a structural one**.

### Three Expectations This Article Overturned By Deriving Them

**The truss buys a coefficient and not a power.** A truss whose attachment station, dihedral and
proportions scale with span leaves the exponent at exactly three halves, and since the optimum
moves as the coefficient to the power minus two fifths, halving the bending material would move
the optimum aspect ratio by about thirty-two percent and the fuel consequence by very little.
**That is the uncomfortable corollary, because it says the truss's structural achievement cannot
by itself be worth much in fuel**, and the value has to be in the fold and in the thin wing.

**The absolute weight model is wrong and the way it is wrong is the point.** The cantilever
estimate landed at 0.909 times the published **braced** bending material, which looks like a
validation and is a coincidence of two large errors in opposite directions, since a cantilever
must be heavier. With the brace included the model is low by a factor of **7.88**, which is
non-optimum material. **A constant factor does not touch a logarithmic derivative**, which is
exactly why the keystone survives being unable to predict the absolute weight.

**And an assertion refuted the docstring of the function it guarded.** The Korn relation's
inversion for sweep was written with a bracket from zero to seventy degrees and a docstring
claiming monotonicity. The relation turns over at **53.8 degrees** because the thickness and lift
terms grow as the inverse square and cube of the cosine, so both ends of the bracket fell below
the target and **the assertion refused to run rather than returning the wrong root**.

### What the Korn Relation Found That Nothing Else Did

**Both configurations sit the same distance below their own drag-divergence Mach number.** With a
single supercritical constant of 0.95 the margins are **0.0203** for the Mach 0.745 predecessor
and **0.0181** for the Mach 0.80 configuration, **differing by 0.00212**, and the difference stays
below **0.00672** across the whole plausible range of that constant. Neither margin was an input.
**So the ten degrees of sweep and the thickness reduction Phase IV added are, to within a few
thousandths in Mach number, exactly what the relation requires to buy 0.055 in cruise Mach.** The
thinning alone is worth **4.86 degrees** of sweep and cost about **28.7 percent** in bending
material, which is a prediction the volume read here cannot check.

### What the Primary Record Admits About Itself

**A flutter correction turned a forty percent margin negative.** At Mach 0.92 the raw
doublet-lattice model gave margins near forty percent and the computational-fluid-dynamics
adjusted model produced multiple mechanisms with margins as low as **minus 7.5 percent**, with the
report saying the adjustments **completely changed the character of the analysis results**. It also
says the method is incapable of capturing the nonlinear flow features and that a braced wing's
redundant load path requires prestressed modes about a large deformation state. **That is the
largest soft spot in this article's own keystone**, because flutter-driven stiffness is the term
that could push the exponent above three halves and it is unmodelled at the critical condition.

**And the report's own recommendation list undercuts the figures everybody quotes.** It asks for
**equivalent conceptual-level design, sizing and optimization studies of cantilever and
truss-braced wing aircraft of the same technology level to allow a more fair and transparent
comparison**, which is a statement by the organisation with the most to gain that the comparison
has not been made fairly. A January 2025 paper appears to answer it and is cited from its registry
record only. **Then it asks for the preliminary design of a demonstrator, which is the one
recommendation that was carried out.**

### The Programme, From the Signed Instrument

**Twenty-seven funded milestones totalling exactly 425 million dollar**, checked against the
appendix's own stated total rather than merely summed. **98.824 percent is paid before first
flight**, which is itself worth 1.5 million dollar against a largest milestone 18.17 times that.
Boeing signed 12 January 2023 and NASA the next morning, so the seven-year term expires 13 January
2030 while the last milestone falls due August 2029.

**The agreement has no pause in it.** The word appears zero times. Article 20 offers termination by
mutual consent, termination thirty days after notice of a missed milestone, and unilateral
termination on four grounds. **The pause landed between Milestone 9 in February 2025 and Milestone
10, the Wing and Strut Critical Design Review, due May 2025**, which is the gate at which the wing
would have been committed to fabrication, and the activity announced as retained is wing research.
Through February 2025 the agreement had reached **153 million dollar, 36.00 percent**.

**The award record holds one contract under the project's name, for 41,198 dollar of desk models**,
and nine truss-braced-wing research contracts totalling **21,420,664.42 dollar**, of which
**80LARC21F0101 at 615,042 dollar is a dedicated task for truss-braced wing structural weight
estimation**, the quantity the keystone turns on. **Three budget books show the Integrated Aviation
Systems Program line falling 67.8 percent for fiscal year 2029 between two successive
justifications**, and aeronautics overall falling 37.0 percent.

### The Sweep, the Gate, and What the Audit Changed

**Two sweeps, 150 reports-server questions, a pool of 14,967, a gate keeping 4,238 across 17
clusters.** The first sweep retrieved 98.2 percent of what the server reported and only one
question hit the wall. **Nine questions returned nothing and seven were rescued by rephrasing in
the vocabulary the registry's own titles use.**

**The homonym measurements are the transferable part.** `SUGAR` returns astrophysical ice
analogues, carbonaceous meteorites, Coccidioides immitis and blood sugar, one of ten aeronautical,
and **`sugar aircraft` returns ten of ten**. **`aspect ratio` is aeronautical at the reports server
and zero of ten aeronautical in the bibliographic index**, which is the second registry-dependent
homonym this series has recorded. `strut` returns zero of ten wing braces and `truss` two of ten,
while **`braced wing` returns ten of ten**.

**THE TWO-SIDED AUDIT CHANGED THE GATE IN BOTH DIRECTIONS AND THE REFUSED SIDE MATTERED MORE.**
Reading thirty admitted records found six that should not have been there, so a bare `aeroelastic`
now needs an aeronautical noun, a bare `net zero` needs aviation, a bare `open rotor` needs an
airframe, and a rotary-wing exclusion family was added. **Reading thirty refused records found an
entire missing cluster**, being a joined-wing research aircraft, a tandem-wing spacing study and a
blended-wing-body pre-design, none of which any pattern admitted. **`alt_config` now holds 448
records and is the third largest in the article. A gate audited only on what it keeps cannot find
an absence.**

**One tightening failed twice on the same title.** Narrowing `aeroelastic` left an aeroelastic
**panel** paper admitted, first because the qualifier list contained the words `model` and
`analysis`, which qualify nothing, and then because the leak was in a second pattern entirely.
**A panel, a plate and a shell are aeroelastic and are not wings.**

### The Verifier Found Three Faults In Itself

**`verify_numbers.py` passes 104 checks and the first three runs failed inside the checker.** Its
first quadrature design was eight million evaluations and timed out, when the taper integral does
not depend on aspect ratio and needed computing once. It then compared the article's rounded
display strings at full precision and reported **eleven failures that were all the article's own
rounding**, so the tolerance is now derived from the last printed digit. And a regex conversion
moved explicit tolerances into a `scale` parameter, **rescaling one slot by ten thousand**, which
the check caught as a 999,934 percent error. **A verifier that fails on its own display precision
is measuring the wrong thing.**

### Instruments

`meas.py` the physics with every loop bounded in its header. `calc.py` the driver.
`verify_numbers.py` 104 checks, importing nothing from `meas.py` by design. `gate_and_cluster.py`
139 patterns, nine exclusion families, 29 keep cases and 43 refusal cases with every refusal
re-tested hyphenated. `run_gate.py`, deliberately not named `select.py`. `homprobe.py` the homonym
measurements. `harvest.py` and `harvest2.py`. `resolve_years.py` with its success-rate floor,
resolving 785 of 965 at 0.813. `build_refs.py`, `emit.py` 233 slots, `assemble.py` which reports
unused slots as well as unfilled ones, `series_line.py` which generates the opening line from the
same mapping that emits its definitions. **`stylecheck.py` is new**, checking the project's prose
rules on prose only after stripping tables, headings, quotations, maths and reference definitions,
and checking that each acronym is expanded before its first bare use. `urlcheck2.py`, `symcheck.py`
with trigonometric operators added, `mathrot.py`, `rendercheck.py`, `emrisk.py`, `site_build.sh`.

### Verification State

`_verify.py` 0 errors and 4 warnings, all four `progress-stale` and all four resolved by this
commit's channel updates. The stub build takes about fifteen seconds. `_lib/render.py` reports no
findings across 549 pages. `mathrot.py` matches 38 source display blocks against 38 rendered
brackets with zero emphasis tags inside any expression. **`emrisk.py` confirms A363 adds nothing
to the corpus-wide count of 72 corrupted expressions in 38 files**, which remains an open pilot
decision. `symcheck.py` passes. `stylecheck.py` reports one finding, which is the statutory
citation `51 U.S.C. 20113(e)` and cannot be written otherwise.

### A Placeholder Identifier Was Caught Before It Shipped

**A reference was entered with the digital object identifier `10.2514/6.2026-0000` as a placeholder
while the real one was looked up.** The real identifier is `10.2514/6.2026-4344`. **A fabricated
identifier that resolves to nothing is worse than no citation at all**, and the record is omitted
rather than cited because the article's dateline is December 2025 and a 2026 conference paper cannot
be used in the body.


## A362, Publication Review

**Lines 8,775 to 8,777, words 67,925 to 67,992, the symbol table 100 entries to
102.** Display equations held at 46, references at 3,804.
Committed and **PUSHED** on the pilot's instruction. **NOT PUBLISHED**, and publication of the
series has never been authorised.

### A Claim This Review Refuted by Counting

**The article said `hingeless control` returned seventy-two records from the reports server of
which every one was a helicopter. It is 61 of 72.** The review counted
all 72 titles instead of trusting the sample that had been read, and
11 do not carry rotorcraft vocabulary. **Most of those are rotorcraft work under
other words**, being higher harmonic control, flap-lag stability in forward flight, ground
resonance and a vertical and short take-off conference. **Two are not rotorcraft at all.** They
are the DARPA, Air Force Research Laboratory, NASA and Northrop Grumman Smart Wing programme,
**which shares the hingeless vocabulary because it is about a wing with no discrete moving
surface**, and which this article's sweep never asked for. The corrected count and the Smart Wing
finding are both in the body.

### Seven Rankings Were Scoped to What Had Been Measured

**The superlative scan returned forty-five hits and seven were rankings this article had not
earned.** That the aircraft is the first in the series able to be compared with itself, a ranking
across sixty-six articles. That `CRANE` is the least useful query in the sweep, a ranking over
roughly two hundred probes where ten were read by hand. That a declared symbol table is the only
instrument that catches a collision. That the air architecture is the single largest uncertainty in
the analysis, where the amplification range is wider. That the differencing design is the single
most important decision in the aircraft. That this article's vocabulary is the worst the series has
met, across vocabularies never measured. And that asking the detail endpoint was the only way to
tell a catalogue gap from a literature gap. **Each is now scoped to what was checked**, and the
rankings that survive are the ones with a measurement behind them, such as the air budget being the
thinnest of fifteen clusters.

### A Stale Figure an Emitter Had Hard-Coded

**The empty-cluster message said the sweep retrieved 18,432 records and the pool is 20,430.** The
figure was written into `emit_clusters.py` as a literal after the second sweep and the third sweep
moved it. **The article therefore stated a number its own source base contradicted**, which is the
defect the slot discipline exists to prevent and which survived because this one number was not a
slot. It now reads the pool from the gate statistics.

### An Acronym Reached the Reader as a Subscript

**`AFC` appeared first in the authority-ratio equation as a subscript and was never expanded.**
`symcheck.py` could not see it because it strips `\mathrm{...}` before comparing symbols, so a
subscript that is itself an unexpanded acronym passed every check the article had. The prose that
introduces the equation now spells it out and both subscripted force increments are declared,
taking the symbol table to 102.

### Small Counts and Dollar Figures

**The article spelled fourteen, eighteen and twenty-five and wrote `4 move no money`,
`5 times out of 5`, `2 of the 5 quoted cases`, `8 questions` and `where 6 still did not`.** Counts
are now spelled and measured quantities keep their numerals, so eight percent of core flow and 1.5
percent stay as they were. **Eleven dollar figures carried a meaningless `.00`** against the
article's own `192,823 dollars`, and the one figure with real cents keeps them. **And a cluster
heading read `1 records.`**

### What Was Checked and Found Clean

**Prose style.** No em dashes, no en dashes, no contractions, no capitals as emphasis. Three
findings and all three are permitted, being a colon inside a code span quoting what a registry
emits, the semicolon in the mandated debug tag, and a parenthetical inside a block quotation of the
register's own description.

**Structure.** All eighteen sections in the order the research-aircraft genre prescribes, with the
Epistemic State, Out of Scope and Conclusion present and last.

**Diction.** Zero content-independent words at or above the peer maximum. Forty-six words exceed it
and every one is the subject or a proper noun, being the contractor, the programme, the agency, the
plenum, the effectors, the fiscal years and the budget books.

**Thirty URLs.** Every one verified. Nine publisher addresses refused the fetcher and all nine are
confirmed in the registry by title, venue and year. **Two were flagged thin and both were false
positives of this review's own byte threshold**, the encyclopedia's pages being plain markup with no
boilerplate and the federal award service being a JavaScript application whose markup is a shell by
construction.

**Numbers.** `verify_numbers.py` runs **160 checks with none failing**, `neweqns.py` a further 52.
`_verify.py` reports 0 errors and 0 warnings across 302 posts. The rendered audit reports no
findings across 546 pages, source and rendered display blocks both count 46, and no
inline expression in the page carries an emphasis tag.


## A362, Primary-Reference Review

**Report primaries 1,387 to 1,464, a share of 38.1 to 39.5 percent, the
period count 1,205 to 1,274 and its share 34.4 to
35.7 percent.** Research records 3,636 to 3,709, reference
definitions 3,658 to 3,804, lines 8,516 to 8,773 and words 64,114 to
67,817. Display equations held at 46 and inline at 228. Committed,
**not pushed**, which is the rhythm. **Not published.**

**BOTH THE COUNT AND THE SHARE ROSE, WHICH THE GENRE DOCUMENT WARNS IS UNUSUAL.** A reference pass
normally raises the period count while lowering the recent share, because it adds older primaries
faster than recent ones and the denominator grows with them. **This sweep was aimed at one
registry's literature rather than at the subject broadly**, so primaries arrived faster than
anything else. The median year did not move, staying at 2007, and the earliest record
moved back ten years to 1927.

### Seven Claims Were Second-Hand and the Audit Began by Saying So

**Every threshold in the article was read through one review.** The regime boundary of three to
five percent, the reduced-frequency band, the measured response at 0.08 percent, the reattachment
at 0.34 percent, the modified-coefficient thresholds, the velocity-ratio condition, the caution
against comparing momentum coefficients across configurations and the attribution of the
definition to Poisson-Quinton. **A pass that exists to prefer primaries has to start by listing
what is not one.**

**Nine originals were located and four could be read in full, and all four are agency reports.**
Every journal item the review names is paywalled. **The upgrade from second-hand to first-hand was
available only where the work was also published as a report**, which is the practical reason this
corpus prefers the report literature, and six items are now carried at registry-record strength
and quoted for nothing.

### The Report That Reversed the Equation Pass

**Seifert and Pack, AIAA 2000-2542, read in full, demonstrated oscillatory separation control at
chord Reynolds numbers as high as forty million** and state that the Reynolds number has a very
weak effect on the pressure distributions and spectra of a deliberately fully turbulent baseline.

**The equation-density pass had argued the opposite way round.** It computed this aircraft's
Reynolds number at 11.44 million, compared it with the low-Reynolds experiments whose
thresholds the article had borrowed, found a gap of one to nearly three orders of magnitude and
concluded that the thresholds were the part most likely to be wrong at flight scale. **The X-65A
flies at 0.715 times that report's sixteen million and 0.286 times the
forty million it quotes.** It is inside the demonstrated range, not beyond it. **The strong form of
the argument is withdrawn in the body rather than quietly softened**, and what remains is the
narrow and correct form, that transferring a threshold differs from transferring a phenomenon.

**And the report quotes the coefficients it used, on a definition identical to this article's.**
Oscillatory momentum coefficients of 0.03 to 0.32 percent, with its own stated
uncertainty of plus or minus twenty-five percent. **This article's wing-referenced
0.0945 percent sits inside that band**, reaching 2 of 5 quoted cases
with no concentration at all. **At that report's own Mach number of 0.25 the same bleed budget
delivers 0.5579 percent, which is 1.74 times its highest quoted value.** So the
air is sufficient where the method is proved and marginal only where this aircraft wants to fly.

### The Primary Names This Article's Keystone as the Open Problem

**Among its proposals for future work is overcoming the lack of sufficient control authority,
especially at high speeds.** That is the conclusion this article derived from the Mach dependence
of a bleed-fed momentum coefficient. **The article now says the constraint was derived here and
discovered elsewhere**, which is the second time in three passes that a primary has shown a result
to be a rediscovery.

### The Targeted Sweep Returned Little and the Little-ness Is the Finding

**Eighty-six new questions were asked of the two report registries and the per-cluster share was
computed before any of them were written.** Five clusters were thin. **The one the pass most wanted
to fix moved least.** The air budget stood at 9.1 percent of 77 records and now
stands at 12.5 percent of 80. **Thirty-five dedicated questions across both
registries bought three records.**

**The reason is measurable and it is not the sweep's.** A reports server asked for a secondary air
system returns two hundred and seven records of a seal workshop, because inside an engine secondary
air means internal cooling. Asked for an aircraft air supply system it returns electric-propulsion
impedance and direct-current power supplies. The defence registry asked what bleed air costs in
engine performance returns two hundred records of which three pass the gate and none is about bleed
air. **What a bleed costs an engine is known to the companies that build engines and is in neither
public registry**, so the article's refusal to put a number on the thrust penalty is a gap in the
record rather than in its research.

**Two clusters did move.** Conventional actuation went 25.6 to 35.1 percent, because
hinge moments and actuation power are what the agency reports of the 1960s and 1970s are full of.
**Control without a hinge did not move at all, staying at 50.0 percent**, which says that
literature is genuinely journal-held.

### The Programme's Own Ancestor Has No Report Literature

**The CRANE manager named Micro Adaptive Flow Control as the work CRANE descends from and neither
registry holds a report about it.** The reports server returns two 1995 summer faculty fellowship
programmes, a Spacelab life-sciences experiment and a paper on the importance of properties in
modelling. The defence registry returns one hundred and twenty-one records of which two pass the
gate and both concern adaptive structures. **A DARPA programme leaves no report literature in a
NASA registry because it was never a NASA programme.**

### Four Method Findings

**THE SAME WORK IS HELD TWICE AND ONLY ONE IDENTIFIER CARRIES THE FILE.** A request for the
flight-Reynolds report's full text returned nothing, and the duplicate record of the same work
carries both a portable document and a plain-text rendering. **A null answer from a registry is
usually a measurement about the literature and this one was about the catalogue.**

**SERENDIPITY IS RECORDED AS SERENDIPITY.** Three of the better allocation records came from a
question about secondary power extraction, being a 1997 report on tailless aircraft control
allocation and two of 1999 on robust nonlinear control of tailless aircraft. **A sweep that found
its best records for one cluster while asking about another has not demonstrated a method.**

**A REWRITE SILENTLY DELETED A DISPLAY EQUATION.** Replacing a span from one heading to another
swallowed a third heading between them, taking the moment relation and its table. **Every figure
still reconciled, every slot still filled, `_verify.py` passed and the rendered audit passed**,
because a missing equation is not a defect in anything that remains. The verifier now carries a
floor at the equation pass's own count, and the first version of that floor used a dotted-all flag
that made its pattern greedy across newlines and reported one equation where there were
forty-six.

**AND A DOUBLED BACKSLASH LEFT A LITERAL ONE IN THE PAGE.** An escaped citation written with two
backslashes rather than one renders the backslash, and it was found by counting brackets in the
rendered page against display blocks in the source, 47 against 46, where the extra was not an
equation at all.

### Verification

`verify_numbers.py` runs **141 checks with none failing**, up from 111, now including the pass's
before-and-after figures recomputed from a frozen baseline, the four primaries read in full, the
withdrawn Reynolds wording, the air-budget negative result, the equation floor and the doubled
escape. `_verify.py` reports **0 errors and 0 warnings**, and it caught an undefined anchor when the
new primaries were cited before being defined. The rendered audit reports **no findings across 546
pages**, source and rendered display blocks both count **46**, and no inline expression
in the page carries an emphasis tag.


## A362, Equation-Density Review

**Display equations 21 to 46, inline expressions 113 to 228, the symbol
table 48 entries to 100, lines 8,281 to 8516 and words 60,403 to
64114.** Reference definitions unchanged at 3721. Committed, **not pushed**, which
is the rhythm. **Not published.**

### What Was Missing Was the Ground the Whole Article Stands On

**Twenty-five relations were added and most of them had been in use since the drafting pass
without ever appearing.** The standard atmosphere, the speed of sound, the total conditions, the
corrected-flow invariant, the compressor temperature ratio, the two mass-flow routes, the core
flow, the aspect ratio, the wing loading and the lift coefficient were all computed and none was
shown. **The genre rule is that a relation the prose relies on gets displayed, and an article
that tabulates a standard-atmosphere pressure without showing where it comes from fails it.**

**The additions that are findings rather than bookkeeping are three.**

### The Reynolds Number Gap, Which Quantifies Why the Aeroplane Exists

**The drafting pass asserted that Reynolds number is why a flight demonstrator is needed and
never computed it.** On the mid-sweep chord at Mach 0.7 and thirty thousand feet the X-65A flies
at **11.44 million**, by Sutherland's law for the viscosity, checked against the published
sea-level value.

**The experiments this article borrows its thresholds from ran at between 19.1 and
497.6 times less.** The measured reattachment at 0.34 percent was obtained at one hundred
thousand. The modified-coefficient thresholds at twenty-three thousand. **Every number used to
decide whether the bleed budget is adequate was measured one to nearly three orders of magnitude
below the condition it is applied to**, and the article now says so and says the direction of the
error is not known in advance, since a boundary layer that separates later needs less control
while being less receptive to it.

### Sharing One Plenum Is an Advantage, and the Limit Is Pi Squared Over Two

**The drafting pass said the constraint set is a simplex rather than a box and left the
impression that sharing is a penalty.** The algebra says otherwise and the algebra is now shown.
The demanded moment is the effectiveness matrix times the demand vector, three axes need full row
rank, and the reachable set is the image of the admissible set. **A box maps to a zonotope and a
simplex maps to the convex hull of its vertices' images.**

**Held at the same total air, the shared plenum reaches 4.9360 times the moment area that
equal fixed per-effector shares would reach**, at fourteen effectors. **The ratio converges to an
exact closed form**, the hull tending to a half disc and the equal-share zonotope to the
reciprocal of pi, so the limit is pi squared over two, 4.9348. At a hundred effectors the
computed ratio sits within a part in ten thousand of it. **Both areas were also checked against a
rejection sample over an exactly computed bounding box, and the unit square and unit triangle by
hand.**

**So the cost of one supply is not a smaller reachable set. It is that the set is no longer a
box**, so the allocator cannot be a per-axis gain and has to solve a programme. The geometry is
labelled illustrative in the text, because the effector positions are not published.

### The Air's Price, Now Stated

**Bleeding 1.860 percent of total engine flow is also the floor on the thrust it costs**,
and the compressor work already spent on each kilogram is 334.1 kilojoule at a temperature
ratio of 2.3241. **The article states the inequality and declines to compute the true loss**,
which needs an engine deck. And the bleed inversion is now displayed, so the fractions are
derived rather than tabulated: 6.77 percent of core flow reaches the lowest measured
threshold and 253.95 percent would be needed for super-circulation, **which is two and a
half times the core flow the engine has.**

### Four Defects, and Two Were in the Checks

**THE FIRST EQUATION CHECK FAILED FOUR TIMES AND THREE WERE ITS OWN REFERENCE VALUES.** Its
standard-atmosphere table carried the 1976 values at five thousand FEET against a key in METRES.
**A unit confusion in a test accuses the code of the test's own mistake**, and this is the fourth
time in this series an equation pass has failed in the check rather than the article.

**THE FOURTH FAILURE WAS A MONTE CARLO WHOSE BOUNDING BOX MISSED THE EXTREME POINTS.** It
reported a hull area BELOW the closed form, which for a coarse outer approximation is impossible,
and that impossibility is how it was spotted. The bounding box is exact and needed no sampling.

**AND THE RENDERED PAGE CARRIED TWO CORRUPTED EXPRESSIONS THAT NOTHING SAW.** Kramdown does not
protect `$...$` from markdown processing, so an underscore opened emphasis in one expression and
closed it in another, putting an `<em>` tag inside the mathematics. **`_verify.py` passed,
`_lib/render.py` passed, and the equations still rendered.** It was found by reading a snippet of
the page by eye.

**THE FIRST FIX WAS BUILT ON A GUESS AND MADE IT WORSE, TWO CORRUPTED SPANS BECOMING THREE.** It
braced every subscript on a wrong model of the flanking rule. **A direct probe of kramdown
settled the rule in five lines**, and the measured behaviour is that an underscore opens when the
character before it is not a word character and closes when the character after it is not.
Escaping the openers works and costs nothing, because kramdown consumes the backslash and MathJax
receives the underscore. **Nine spans carry the escape and the rendered page now carries none of
the tags.**

**THE DEFECT IS PRE-EXISTING AND CORPUS-WIDE, AND THE FIRST COUNT OF IT WAS WRONG TOO.** A scan
built on the pre-probe flanking rule reported fifteen pairs across ten files. **Rebuilt on the
measured rule it reports seventy-two pairs across thirty-eight files**, of which **thirty-five are
published posts carrying sixty-nine pairs** and three are drafts carrying three. The heaviest is a
projection-series post with seven. **Two of the drafts are this series' own**, being the opener and
A361, and the third is A334.

**A362 is fixed and the other thirty-seven are reported and untouched**, because editing the
mathematics of published posts is the pilot's call and not a side effect of an equation-density
review. **The wrong count had already been written into these files and was corrected before the
commit**, which is the only reason it is not in the history table as a fact.

### Verification

`verify_numbers.py` now runs **111 checks with none failing**, up from sixty-three, and
`neweqns.py` runs **fifty-two** more against published table values, independent routes and
hand-checkable cases. `symcheck.py` reports 100 declared symbols with every token
used resolving to one, after **two more collisions were renamed**, the lapse rate off `L` which
`\Delta L` and `C_L` were already using, and the tropopause conditions off `T_t` and `p_t` which
are the plenum's. `_verify.py` reports **0 errors and 0 warnings**. The rendered audit reports
**no findings across 546 pages**, and **source display blocks and rendered blocks both count
46**.


## A362, X-Planes: Aurora Flight Sciences X-65 CRANE, Drafting Pass

### The Keystone, Which Cancelled Altitude Twice and Exactly

**The momentum coefficient an engine-bled flow-control effector can deliver is exactly
independent of altitude.** Corrected mass flow makes the bled flow proportional to ambient
pressure, the compressible identity makes dynamic pressure proportional to ambient pressure, and
those cancel. **Then a second cancellation nobody asked for**, because corrected flow divides by
the square root of the compressor-face total temperature while a choked jet fed from that same
air multiplies by it. **The inlet total-condition factor cancels once as well.** What survives is
the inlet's own total-pressure recovery over the square of the Mach number, verified identical to
twelve significant figures across ninety-one altitudes from sea level to forty-five thousand feet.

**The other architecture varies by 7.92 times over the same band**, so the published
phrase `a pressurized source` conceals which behaviour this aircraft has. **The article's
prediction is that two flights at one Mach number and two altitudes settle it.**

**AND A MONOTONICITY CHECK REFUTED A BOUND THE ARTICLE HAD ASSERTED.** The Mach factor was
claimed monotone to about Mach 1.9. It turns at exactly Mach 1.4142, independently of the
specific-heat ratio, and the minimum has the closed form gamma to the power gamma over gamma
minus one, halved. **Three routes agree to one part in ten to the fifteenth.**

### The Result That Had to Be Withdrawn, and the Review That Withdrew It

**THE DRAFTING PASS INVENTED A BAND AND A PRIMARY REFUTED IT.** The first version asserted that
separation control needs a momentum coefficient between 0.005 and 0.02, computed that engine
bleed cannot reach it, and made that the central difficulty. **An open-access review, read in
full, reports the separation-control to super-circulation threshold at three to five percent and
a measured lift response at 0.08 percent.** The wing-referenced coefficient computed here is
0.0945 percent, so it reaches the smallest value at which a response has been measured, and
needs a concentration factor of only 3.60 to reach a measured reattachment threshold.
**The conclusion reversed and the reversal favours the aircraft.**

**The same review names the article's own quantity.** What this article derived as an
amplification identity, the ratio of the lift increment to the momentum coefficient, the
literature calls the actuation efficiency and already reports as falling through the regime
transition. **No novelty is claimed and the article says so in its own text.**

**It also cautions against the use the article makes of the momentum coefficient**, because many
combinations of mass flow and jet velocity give one value, and the parameter that separates them
is the velocity ratio, which must exceed unity. **It is 2.083 here.** And because a higher
velocity ratio beats a higher mass flow at the same momentum, **the single-stage centrifugal
compressor that forces hot full-cycle bleed is favourable in exactly that dimension**, which is a
reason not to precool the air and was not looked for.

### Where Flow Control Loses to a Hinge

**The authority ratio is altitude-independent and falls as the square of the Mach number.** At an
amplification of thirty against a surface worth 0.05 in lift coefficient, the crossover is Mach
0.485, flow control delivering 5.15 times the hinge's authority at Mach 0.2 and
0.567 of it at Mach 0.7. **For a conventional aeroplane the hard case for control power
is slow flight. For this one it is fast flight**, and an envelope expanded upward walks from the
easy end to the hard one.

### The Award Record Names What the Narrative Does Not

**Twenty-five offers, three awards, and the downselect visible as an exercised option.** Aurora
Flight Sciences, Lockheed Martin and Georgia Tech Research Corporation each hold a Phase 0
contract reporting twenty-five offers received. Aurora and Lockheed each exercised an option in
mid-2021 and **Georgia Tech never exercised one at all**, leaving 45.1 percent of its ceiling
unused, so the record dates a cut no source states in words. **Georgia Tech was also cost no fee
where both companies were cost plus fixed fee.**

**The Phase 2 and Phase 3 contract carries 94,372,238 dollars against a press figure of forty-two
million**, because the two phases went onto one instrument. **Its last obligation is 16 January
2025 and the only action after it is a zero-dollar change order on 11 February 2025**, which is
the pause appearing as an absence. The period of performance expired on 2 October 2025, sixty-nine
days before the article's dateline, with the fuselage unfinished. **The restructured co-investment
appears nowhere in the record, because a contractor's cost share is not federal spending.**

### Seven Budget Books, and a Milestone That Slipped Two Fiscal Years

Every CRANE line in every DARPA justification book from the fiscal year 2020 request to the
fiscal year 2026 request was read. **The three columns of an exhibit are a prior-year actual, a
current-year estimate and a budget-year request, so one fiscal year appears in three consecutive
books wearing three hats**, and reading the disagreement as inconsistency would be wrong.

**Fiscal year 2020 came in 81.33 percent above its request and every year since has come in
below, at a mean shortfall of 16.29 percent.** The programme asked 200.507 million
dollars across seven years and expects 179.416 million. **The critical design review was
promised in four consecutive books for three different fiscal years.** The fiscal year 2026
request of 4.000 million is the only round number among seven figures carrying three decimals.

### The Vocabulary Is the Worst the Series Has Met

**`CRANE` returns a logging-crane fatality, a mobile-gantry-crane fatality and two collections of
nursery rhymes, with nothing aeronautical in ten results.** `novel effectors`, the literal phrase
in the programme's title, returns fungal and oncological effectors. `control authority` is
bibliographic authority control, ten of ten. `fluidic oscillator` is an American Water Works
Association standard for cold-water meters. **`momentum coefficient`, the article's keystone
parameter, returns microchannel accommodation, rarefied momentum exchange and an evolutionary
optimiser.**

**AND ONE HOMONYM DEPENDS ON WHICH REGISTRY YOU ASK, WHICH IS NEW TO THIS SERIES.**
`hingeless control` returned ten of ten on subject from the bibliographic index, every one about
flow-control effectors, and seventy-two records from the reports server of which every one is a
helicopter rotor hub. **The same two words name two unrelated subjects and the right anchor
differs by registry.** The gate carries a rotorcraft guard because a probe was read, not because
an audit failed.

**The keystone parameter is almost never in a title.** Twelve titles in nearly twenty thousand
name it and the gate admits eleven. **The parameter is a method rather than a subject**, which is
a third case beside a query that failed and a literature that was thin.

### What the Audit and the Checkers Caught

**The two-sided audit changed the gate twice.** A refused co-flow jet paper revealed an entire
effector family with no anchor. A refused reconfigurable-control record revealed fifty-nine
control-allocation records of which forty were being refused, **and twenty-eight effectors on
three axes is an allocation problem by construction**, so that cluster exists because refusals
were read.

**A GUARD WAS DEFEATED BY A HYPHEN AND THE SHARED LIBRARY CANNOT REPAIR IT.** The library flattens
intraword hyphens only after an unflattened pattern has failed. **A guard is a negative lookahead,
so a guard that fails to fire is a guard that admits**, and the record is admitted before
flattening is tried. Two further guards leaked when refusal cases were re-tested with hyphens,
having passed because the test used the spelling the probe returned.

**THE YEAR RESOLVER FAILED ON ALL 1,321 RECORDS AND RAISED NOTHING.** It read the raw response's
`publications` field from a library function that had already consumed and discarded it. **An
empty year is a legitimate value, so a total parser failure and a dateless registry are the same
observation**, and the only instrument that can separate them is a success-rate floor, which the
file now carries.

**A ZERO-COUNT CLUSTER IS INVISIBLE IN A COUNTER.** The statistics looked for zero values and
found none, because `collections.Counter` never creates a key it did not count. **The one empty
cluster is a finding**, being that not one record in 18,432 names this programme, this
aircraft or this contractor.

**`symcheck.py` FOUND TWO REAL SYMBOL COLLISIONS.** The letter A served as the amplification and
as the choked throat area, and f served as a dimensionless factor and as a frequency. Both were
renamed.

### Verification

**8,281 lines built from eleven body files with every number filled from a slot**, so no
figure is typed into the prose. `verify_numbers.py` runs sixty-three checks and all pass,
re-deriving the atmosphere against published table values, the altitude invariance across
ninety-one altitudes, the turning point by three routes, the amplification identity and the
survey statistics from the reference base. `_verify.py` reports **0 errors**. The stub build took
fifteen seconds and the rendered audit reports **no findings across 546 pages**. **Source display
equations and rendered display blocks both count 21**, which is the check A375 earned
when four of its equations folded into a paragraph.

---

## Next

**Await the pilot's prompt.** By the rhythm the next prompt is A362's equation-density review.


## A361, X-Planes: Invocon X-64

**FINAL STATE 8,873 lines, 67,030 words, 39 display equations, 231 inline expressions, a
90-entry symbol table, 3,934 reference definitions**, with **3,837 research records cited
across 15 clusters and 1,726 report primaries at 45.0 percent**, median year 2003, period
share 87.7 percent, from one sweep retrieving 23,960 records of which 23,824 were distinct.

### The Register Says One Thing and the Laboratory Says Another

**A360 established that the X-63A and X-64A rows are identical in every cell that describes
the machine.** This article found the government document that contradicts the impression
that leaves. The laboratory's own background paper on its rocket propulsion organisation,
cleared September 2022, says **each company has their own launch vehicle and chosen approach**
and ties each designation to its company.

**THAT DOCUMENT HAD NEVER BEEN USED BY THIS SERIES AND NO SWEEP WOULD HAVE FOUND IT.** It is
a public-affairs PDF on a laboratory web site with no report identifier, and it was reached
through the encyclopedia entry's own source list. **A source list at the foot of a secondary
is a retrieval channel**, and it is the channel that produced the sentence this article is
built on. It also quantifies the modularity half of ARISE, which A360 said the fact sheet did
not, the portfolio seeking **70 percent less development time and 50 percent less cost**.

**Two slips in that primary are recorded rather than smoothed.** It writes `into the 22nd
century` twice where it means the twenty-first, and it names nitrogen tetroxide with Aerozine
50 in one sentence and with monomethylhydrazine in the next, which are different fuels.

### A Name Is a Query and a Query Is Only as Good as Its Spelling

Invocon returns **81** award rows of wireless instrumentation, impact detection and radiation
monitors. KT Engineering returns **15**, and **every one of the seven rows the phrase
`segmented launch vehicle` returns in the whole record is this company's**. The announcement
writes `Troy7` and the award record writes `TROY 7`. **`Troy7` returns nothing in any of five
award families and `Troy 7` returns fifteen.** **And the spaced spelling imports a collision
the unspaced one avoided**, matching a router backup and a seven-inch rifle rail, so the more
findable query is the less precise one and both halves of that trade are stated.

### The Keystone, and a Timing Result That Reversed the Expected Answer

**An accelerometer is blind to gravity, which is what makes it the right instrument.** It
reads thrust minus drag over mass, so the largest term in the equation of motion is the one it
declines to see. **Recovering thrust needs a drag model and the drag term is the only one no
instrument on board can reduce.** Holding it to a tenth of A360's 5.3 percent effect needs a
drag model good to **2.65 percent** at a drag fraction of one fifth, and the drag fraction at
which the total error equals the effect is **0.209** for a quarter-accurate model.

**THE EXPECTATION WAS THAT THE CONFOUNDER PEAKS WHERE THE SIGNAL LIVES AND IT DOES NOT.**
Ambient pressure depends on position while drag depends on position and the square of speed,
and a rocket reaches altitude before it reaches speed. **Dynamic pressure peaks 2.10 to 2.48
times later than the half-signal time, and by then between 83.6 and 95.3 percent of the
pressure-time integral is collected.** The trajectory is the instrument.

### Two Power Laws Are Not a Trajectory

Taking A360's altitude exponent of 2 with a speed law linear in time returns a peak dynamic
pressure of **190 kilopascal** and a drag fraction above one, **and a drag fraction above one
describes a decelerating vehicle**. The repair removes an assumption rather than correcting
one, making the published cut-off altitude a constraint. **A model with one assumption too
many will usually tell you so somewhere, and rarely in the quantity you were computing.**

### The Shape, and the Same Polygon A360 Found in the Sky

Two published numbers give a fineness ratio of about five against the RS1's 14.67, so the
frontal area is 1.72 times as large and **one calibre of static margin costs 20 percent of
this vehicle's own length against 6.8 percent for the other**. The tip-over anisotropy is one
over the cosine of pi over N, **exactly the square root of two for four legs**, but the
footprint has N sides for every N where A360's control polygon had N or 2N, **and the
difference is a half-plane truncation rather than anything geometric**.

**Harmonic N sampled at N points has exactly the discrete mean of harmonic zero**, so a
four-legged vehicle with four taps would report its own legs' disturbance as a change in the
thrust-bearing mean, and both phases of harmonic mu need 2mu plus 1 sensors.

### The Equation Pass, 20 to 39

**The largest omission was a structural result that lived in the numerics and never reached
the page**, being the drag fraction in terms of thrust-to-weight and ballistic coefficient,
from which follows the relation that licenses the article's central comparison. Also added
were the geometry relations as scaling laws so the article says which figures are
consequences, the atmosphere's layer forms, the mass history, **the exact axial-force
decomposition that makes the zero-angle-of-attack approximation precise rather than merely
disclosed**, the slender-body slopes that explain why the legs must be fins, the support
function beside the lever arm, and the Fourier estimators with the counting bound. **One
symbol collision forced a change of notation**, A360's gamma for the ratio of specific heats
becoming kappa because gamma was already the flight-path angle.

### The Primary Pass Found a Literature the Drafting Pass Engaged None Of

**Determining thrust in flight is a settled discipline whose own review states this article's
premise in as many words.** That literature is about air-breathing engines, where an inlet
captures a momentum flux no body-mounted instrument can separate from drag, **which is why its
method is gas-path modelling and why a rocket may use an accelerometer**. The inverse was done
once in flight, the XB-70's drag measured by determining its thrust independently. **Thrust
minus drag is one observable and splitting it always costs a model of one side.**

**AND THE ESTABLISHED METHODOLOGY NAMES A TERM THIS BUDGET DOES NOT HAVE.** It separates bias
from precision and carries a model bias error, where this budget combines three terms in
quadrature as though all were random, and a drag model's error is more likely systematic than
random. **So the article now says plainly that it presents a sensitivity analysis and not an
uncertainty statement**, and that a single demonstrator flight is a single-sample experiment.

**Report primaries 45.0 percent against A360's 30.6**, from the fixed fetcher and from the
subject being a report literature rather than a conference one. **Three encyclopaedia anchors
dropped as superseded** by Barrowman, Moffat, and Shannon with Nyquist. **Barrowman 1967 read
in full confirms both halves of a displayed relation**, and the bibliographic index returns
gastrointestinal lymphatics for his name while the reports server holds the document under its
title, **so the two registries hold different literatures rather than the same literature to
different depths**. **Four sources are used from their abstracts alone and say so.**

### The Publication Review

**The superlative scan found four real defects in 158 ranking sentences.** A claim that the
1967 report is what `the whole practice rests on`, which is field-wide and now says it made the
method a convention. That `Invocon was never a launch company`, which an award record cannot
settle and now says the record gives no sign it had ever been one. That `the only image the
encyclopedia entry describes is a three-dimensional printed model`, **which is simply wrong**,
the entry crediting two images and captioning one, so the article now says no photograph of
flight hardware is identified as such in any source consulted. And a claim about `the only
claim this article makes without qualification`, now scoped to drag.

**The drafting-history scan took six instances to two.** The lever-arm inversion is now stated
as the tempting construction rather than as a previous draft, a reference to A360's own review
process became a reference to its finding, and the two kept are the defused coincidence, which
is epistemic content, and `What the Data Changed`, whose purpose is exactly that.

**ARMR first appeared inside a quotation and was never expanded before it.** A quotation cannot
be altered, so the expansion is now in the sentence introducing it.

**And the diction scan found one tic**, the laboratory's key sentence paraphrased four times
beyond its quotation, now twice.

**No unit is missing and no decision is stranded.** Forty recorded decisions were probed
against the article and all forty are present, **the one apparent miss being my probe using my
own report's phrasing rather than the article's**, which is the same class of false failure as
a check whose scope is wrong.

### Verification

| Gate | Result |
|---|---|
| `verify_numbers.py` | **1,531 checks, 0 failures** |
| `neweqns.py` | **466 checks on the new relations, 0 failures** |
| `symcheck.py` | 90 symbols, both directions, 39 display equations, 218 inline, 0 failures |
| `_verify.py` | 302 posts, **0 errors, 0 warnings** |
| `urlcheck.py` | 33 addresses, 30 fetched, **3 confirmed through the registry**, 0 unresolved |
| stub build | clean, **against checksum-matched bytes** |
| `_lib/render.py` | 545 pages, 172 carrying display math, **no findings** |
| rendered article | 912,434 bytes, 8,213 links, 18 tables, 0 unresolved brackets, 0 raw dollar pairs |

### What Comes Next

**A361 IS COMPLETE. FOUR PASSES, COMMITTED AND PUSHED, AND NOT PUBLISHED.** The next article
is **A362, the X-65**, editorial date 2025-12-10, series index 66. The register gives the
X-65A to Aurora Flight Sciences with an engines cell of `1 Williams FJ44-3A` and a DARPA
sponsor, which is the active-flow-control demonstrator.

**THE A358 AND A359 OFFICIALITY CORRECTION REMAINS THE PILOT'S DECISION AND IS UNTOUCHED.**

---

## A360, Publication Review

**THE PASS FOUND A SUBSTANTIVE PHYSICS ERROR, NOT ONLY PROSE DEFECTS**, and it found it by
refusing to let one of its own edits stand unverified.

### The Rule Is Modulo Four and the Article Said Parity

**The article claimed that on an even ring of thruster modules the direction of least
steering authority points straight at a module.** That is true only when **four divides the
module count**. At six, ten, fourteen, eighteen and twenty-two modules the module direction
is the direction of **greatest** authority, as it is at every odd count. The reason is that a
quarter turn is a whole number of module spacings exactly when four divides the count, so
that is the only case in which a module sits on the boundary of the forward half plane when
the command points at another module.

**The closed forms were never wrong**, because they depend only on the polygon's side count,
and every one of the article's authority figures stands unchanged. **What was wrong was the
statement about where the extremes sit**, which is the part an autopilot designer would use.

**HOW IT SURVIVED TWO PASSES IS THE USEFUL PART.** The numerical check evaluated **both**
candidate direction sets and took the extremes over their union, specifically so that it
would not have to assume which set held the maximum. That made the check correct and
**blind to the false rule**. Worse, the comment above it documented the false rule as the
justification for evaluating both sets, **so the wrong belief was written into the verifier
as the reason for the code that made the verifier immune to it.**

**AND I FOUND IT BY CHECKING MY OWN EDIT.** The publication review first replaced a
drafting-history sentence with a tidier one asserting that a naive check reports swapped
extremes `at every even module count`. That was an unverified structural claim, so it was
tested before being trusted, and the test refuted both it and the article's original
sentence. `check_extremal_parity` now pins the rule by enumeration against the modulo-four
condition. The suite is **652 checks to 699**.

### A Withdrawn Phrase Standing in Two Summarising Sections

**The primary-reference pass established that `roughly twice as permissive` is, in the
article's own words, true nowhere**, the correlation crossing the flat four tenths at
separation Mach 2.59 and being stricter below it, with 1.74 times as the correct figure at
the top of the fitted range.

**It then left that exact phrase standing in `What the Data Changed` and again in the
conclusion.** The article asserted in two places the phrasing it refuted in a third.

**No check could see it.** 652 checks passed. **A retracted wording carries no number to
recompute**, so a suite built on recomputing stated quantities is blind to it by
construction. This is the inconsistency the handoff predicted the fourth pass would inherit,
and it was worse than an unsoftened claim, because it was a self-contradiction.

### A Paragraph Refuted by the Paragraph After It

**The Source Base opened by calling the reports server's share thin and `a fact about this
subject rather than about the sweep`**, and closed by saying the primary-reference pass **is
where this imbalance has to be answered**. The subsection four lines below proves the
thinness was a defect in the shared fetcher, and the pass that would answer it had already
run. **Both readings stood in the article's own voice.** The emitter had regenerated the
paragraph's numbers and left the sentences interpreting them exactly as written.

### Caps Emphasis, Cleared Again

**Twelve shouted spans**, converted to bold sentence case. The corpus-wide sweep of commit
65e807f cleared caps emphasis across the series and **this article's third pass reintroduced
it**, five spans in the separation section and seven in the Source Base.

### The Drafting-History Scan, Decided Rather Than Swept

**Twenty candidate lines, reduced to seven.** The handoff was right that this mattered more
than usual, and right that the answer was neither to keep them all nor to cut them all.

**Cut as autobiography**, being sentences that told the reader about a previous draft rather
than about the subject: that the drafting pass implemented the atmosphere and cited an
encyclopedia for it; that the first draft of a sentence rounded two scale heights to
different numbers; that a verifier reported eighteen failures. **The separation section
carried six statements about its own drafting pass and now carries one.**

**Kept and reframed**, being sentences whose content is about the subject: the numerical
lesson that a central difference at a clamped boundary halves its own denominator, restated
as a fact about evaluating the derivative rather than about a first attempt; and the warning
that the regular-ring closed form does not apply to a ring with a module missing, restated
as the tempting move rather than as this article's mistake.

**Kept unaltered**, being the seven in sections licensed to narrate method: `What the Data
Changed`, whose whole purpose is to record what the work overturned, and `The Source Base`,
whose subject is the instrument.

### The Superlative Scan, Which Had Not Been Run

**158 ranking sentences, three real defects.**

**`The largest aerospike ever built is the XRS-2200`** is a ranking over the world's
aerospike hardware made from a survey of publications that **contains no size comparison**.
The corpus holds four toroidal-aerospike records and none of the 1970s large-engine
hardware that would settle it. Now scoped to the largest the survey documents.

**`the matched-expansion condition that every text states as a separate empirical fact`** is
a claim about every text ever written, from an article that read a handful. Now `texts
commonly state`.

**`Seven decades of publication`** sat directly beneath a table whose nine decade rows a
reader would count. Now **seven decades of continuous publication**, which ties it to the
verified continuity from 1956 and is exact to this article's dateline.

Also softened: **`the cheapest error to make`** to `among the cheapest`.

### One Sentence That Was Not Grammatical

`Written the other way round the expression is the negative of the loss, and the first
version of the numerical test was, which is how the sign was fixed` is elliptical past
readability. **The surviving content is the one a reader implementing the integral needs**,
which is that the integrand is the fitted nozzle's exit area minus the envelope's and not
the reverse.

### What Did Not Need Changing

**The style scan is clean.** No contractions, no parentheticals in this article's own voice,
no em-dashes or en-dashes, no prose colons or semicolons. The three parenthetical hits are
inside quoted primary material and were left exactly as the sources write them.

**No unit is missing.** A359 shipped a number with no unit past every numeric check. Twelve
bolded numbers were examined here and each carries its unit in the adjacent clause or is
dimensionless by construction.

**No decision was stranded in the process files.** A359 recorded a decision in `TASKLOG.md`
and this file that never reached the article. Twenty substantive claims the process files say
A360 carries were probed against the article and **all twenty are present**.

**The three numbers a fourth pass usually moves were left alone**, as the handoff directed.
Report primaries stay at 3,748 of 12,231, being 30.6 percent. Display equations stay at 46
and inline expressions at 187, with the symbol table at 73 rows checked in both directions.

### Verification

| Gate | Result |
|---|---|
| `verify_numbers.py` | **699 checks, 0 failures**, up from 652 |
| `neweqns.py` | 246 checks on the new relations, 0 failures |
| `symcheck.py` | 73 symbols, 46 display equations, 187 inline, 0 failures |
| `_verify.py` | 302 posts, **0 errors, 0 warnings** |
| stub site build | 40 seconds, clean |
| `_lib/render.py` | 543 pages, 172 carrying display math, **no findings** |
| `_lib/test_lib.py` | **120 of 120 passed** |
| rendered article | 2,274,470 bytes, 25,054 links, 0 unresolved references |

**The article is 25,796 lines and 159,263 words**, up 145 words, the increase being the
corrected modulo-four passage.

### What Comes Next

**A360 IS COMPLETE. FOUR PASSES, COMMITTED AND PUSHED, AND NOT PUBLISHED.** The next article
is **A361, the X-64**, editorial date 2025-12-09, series index 65, **which shares every word
of its register description with A360**.

**A361 cannot be built the way A360 was, and that is already measured.** `Invocon` and
`Troy7` return nothing at all from the bibliographic index and `KT Engineering` is flooded by
a mechanical-engineering journal with those initials. **Three contractors and no indexed
publications between them.** What A361 has instead is the federal award record, where the
recipient name returns decades of instrumentation contracts, and the contractor's own
physical description of a recoverable vehicle about twelve metres tall landing on four legs
that double as stabilising fins.

**THE A358 AND A359 OFFICIALITY CORRECTION REMAINS THE PILOT'S DECISION AND IS UNTOUCHED.**

---

## A360, Primary-Reference Review

**REPORT PRIMARIES 984 TO 3,748, FROM 10.4 PERCENT TO 30.6.** Research records 9,467 to
12,231, reference definitions 9,609 to 12,395, lines 20,167 to 25,796, words 117,925 to
159,118. **Every one of the fourteen clusters rose**, the range moving from 3.7 to 23.3
percent up to 14.8 to 49.0.

### The Reports Server Was Being Read One Page Deep, by Every Article in This Corpus

**THIS IS THE FINDING OF THE PASS AND IT IS NOT ABOUT THIS ARTICLE.** `fetch.ntrs_search`
passed its page specification as a single encoded object. **That server clamps such a
request to ten records AND SILENTLY IGNORES THE OFFSET INSIDE IT**, so six requests at six
different offsets return the identical ten records, which is what the probe found.
Passing the size and the offset as separate bracketed parameters is honoured.

**The question `plug nozzle` matches 242 records. The old call returned 10. The corrected
one returns all 242 with no duplicates.** The fourth sweep's reports-server return is
**10,160 records against 606 from the first three sweeps combined**, a factor of sixteen
and a half, and it is the direct cause of the primary fraction tripling.

**EVERY PRIMARY-REFERENCE PASS IN THIS SERIES HAS COMPLAINED THAT THE REPORTS FRACTION IS
THIN.** A359 said so, and this article's own drafting pass wrote that the imbalance was
`the third pass's problem arriving early`. **Part of that complaint was an instrument
reading its first page.** The fix is a parameter spelling, it is held by a test that runs
offline against a fake transport, and it is in the shared library where every later
article inherits it.

**AND THE SERVER REPORTS ITS OWN TOTAL, WHICH NOTHING WAS READING.** `fetch.ntrs_total` is
added, and with it the coverage of a sweep stops being an assumption. Across 89 questions
the server reported **32,488 matching records and returned 14,929**, which is 46.0 percent.
**That average hides a clean split.** Sixty-eight questions were taken to the bottom,
holding 7,798 between them and returning all 7,798. **Twenty-one hit this article's own
walk limit of 400 rather than the server's**, and **every one of the 17,559 records not
taken belongs to those twenty-one**, which are the broad organisational questions such as
`Marshall Space Flight Center engine`, holding 5,402 on its own. **The focused half of the
sweep is complete and the truncation is entirely of this article's choosing.**

**THE SAME MEASUREMENT CANNOT BE MADE OF THE BIBLIOGRAPHIC INDEX AND THE ARTICLE SAYS SO.**
That index performs a ranked retrieval rather than a boolean match, and asking it how many
records match `rocket nozzle performance` returns 2,406,511, which is not a count of
anything. **A coverage figure is worth quoting only where the denominator is a match
count.**

### A Read Primary Withdrew This Article's Sharpest Claim

**THE DRAFTING PASS SAID THE TRAJECTORY-OPTIMAL NOZZLE CANNOT BE BUILT.** That rested on a
separation threshold of four tenths taken from secondary accounts, and the pass said
plainly that it had not read the correlations.

**NASA Technical Paper 1207 has now been read in full and it changes three things.**

**It gives the attribution the drafting pass struck.** The four tenths belongs to
Summerfield, Foster and Swan in the Journal of Jet Propulsion for 1954, and the paper adds
that the value `is still quoted today ... although more recent studies have shown it to be
inadequate`. **The drafting pass went looking for exactly that attribution, found a 1953
paper by Scheller and Bierlein in the index instead, and removed the name rather than
assert it.** Removing it was right on the evidence then. **The paper that corrects it also
explains the confusion**, because Scheller and Bierlein are the early study that conflicted
with the others.

**It says the four tenths is for the wrong kind of nozzle.** Contoured nozzles, `the case
of most interest for modern nozzle design`, follow a different correlation, and the paper
fits a second-order curve to them between separation Mach 2.4 and 4.5.

**And applying that curve to this article's own nozzles takes the claim back.** The
criterion is local, so the nozzle is walked from throat to exit. **The trajectory optimum
separates only below about 3.3 to 3.7 megapascal of chamber pressure**, and above that it
runs attached with between 6.6 and 12.7 percent of margin in area ratio. **The chamber
pressure recovered from this engine's own instability frequency, 2.6 to 8.7 megapascal,
straddles that crossover.** So the honest claim is that the optimum sits pressed against
the limit rather than beyond it, which is weaker, better supported and more interesting.

**THE DRAFTING PASS'S ERROR HAS A NAME.** It used the more conservative of two criteria and
the conservative one is the one the primary calls inadequate. **A band taken on report is
not a band**, because a range quoted without its provenance hides which end belongs to
which kind of nozzle. The opening, the section, the reflection and the conclusion were all
corrected.

### Two Further Corrections the Checks Forced Out of My Own New Prose

**THE CRITERION AT MACH 3 IS 0.340 AND I WROTE 0.342**, which was arithmetic done in my
head and caught by a check that evaluated the polynomial.

**AND I SAID THE CONTOURED CORRELATION TOLERATES ROUGHLY TWICE THE OVER-EXPANSION, WHICH IS
TRUE NOWHERE.** It crosses the flat four tenths at separation Mach 2.59 and is **stricter
below that**, reaching 0.433 at the bottom of its fitted range. The old rule is 1.74 times
as restrictive at the top of the range and slightly less restrictive at the bottom. **A
nozzle of the area ratios this article discusses separates well above Mach 3, so the
permissive end applies here, but stating it without the crossing would have repeated the
error the section is about.**

### Twenty-Two Curated Primaries, Three Read in Full

**NASA SP-8120, the design-criteria monograph for liquid rocket engine nozzles**, which
supplies the J-2 case history the article was describing in the abstract. That engine was
given a deliberately nonoptimum contour to raise its exit pressure, suffered unsteady
asymmetric separation from a wall-pressure minimum, lost thrust chambers to the loads, and
ended up with a bolt-on diffuser and restraining arms from the test stand to the nozzle
skirt. **It also states, in the design community's own voice, that separation predictions
`are used only as a guide`**, which is the qualification this article makes independently.

**NASA Technical Paper 1207**, described above.

**The 1976 United States Standard Atmosphere.** **The drafting pass implemented that
atmosphere and cited an encyclopedia for it**, which is precisely the gap a
primary-reference pass exists to close.

The remaining nineteen are the four Lewis reports of 1954 to 1959 that founded the
plug-nozzle literature, the design monographs for turbopumps and combustion chambers, the
standard design text, the four LASRE reports covering the only aerospike that ever left
the ground, and the five X-33 reports covering the largest one ever built.

### Which Clusters Rose, and Why the Keystone Rose Least

**THE KEYSTONE WENT FROM 8.7 PERCENT TO 16.8, WHICH IS A NEAR DOUBLING AND STILL BELOW THE
ARTICLE'S OWN AVERAGE OF 30.6.** The largest gains were general rocket propulsion at plus
29.8 points, manufacture at plus 27.0 and named vehicles at plus 23.0. The smallest was the
wake cluster at plus 3.3, which was already among the richest.

**AND A359'S TEST SAYS THE REMAINING THINNESS IS A FACT ABOUT THE DISCIPLINE.** The three
thinnest clusters are exactly the three in which one publisher's conference proceedings
hold the largest share, being altitude compensation at 34 percent, the wake at 49 and the
fixed-nozzle limits at 51. **Half of the wake literature and half of the limits literature
is one conference series.** The general nozzle cluster beside them is 26 percent that
publisher and 29 percent reports, and general rocket propulsion is 29 and 49. **The
specifically aerospike subject is a conference literature and the rocket propulsion around
it is a report literature.**

### A Third Instance of the Cached-Measurement Defect, Caught Before It Bit

The family-cost cache added in the drafting pass was fingerprinted on the gate's patterns.
**The fourth sweep changed the pool rather than the gate**, which would have served the old
counts against new records. The fingerprint now covers the pool size as well. **That is the
trap this article documented two passes ago, one level up, and it was caught by looking for
it rather than by anything failing.**

### Verification

`_verify.py` **0 errors and 0 warnings** across 301 posts. Library tests **120 of 120**,
one added holding both halves of the pagination repair. **Article verifier 652 checks and 0
failures**, and **the relation verifier 246 checks and 0 failures**. **The symbol check
passes in both directions** at 73 declared symbols, 46 display equations and 187 inline
expressions. Diction **0 constructions above the corpus maximum**. **Zero contractions,
parentheses, colons, semicolons or dashes outside verbatim quotations.** The stub-isolated
production build succeeded in **19.2 seconds** with no Liquid error against checksum-matched
bytes, **the rendered audit reports no findings across 543 pages**, source and rendered
display-equation counts agree at **46**, the inline count at **187 balanced pairs**, and the
page carries zero raw dollar pairs, zero unresolved reference brackets and zero unrendered
Liquid.

---

## A360, Equation-Density Review

**DISPLAY EQUATIONS 15 TO 45, INLINE EXPRESSIONS 70 TO 181, LINES 19,915 TO 20,167, WORDS
114,090 TO 117,925.** A symbol table of **71 entries** is added and checked in both
directions.

**THE ARTICLE PERFORMED A WHOLE THERMODYNAMIC CALCULATION AND SHOWED NONE OF ITS
MACHINERY.** The drafting pass used the thrust coefficient in nine places and **never
defined it**. It used the area ratio without relating it to the throat, the isentropic
relations without writing them, the Vandenkerckhove constant not at all, and it quoted a
gain in percent without saying that the quantity is a ratio of two integrals. **The
throat area did not appear anywhere in the article.** That is the density gap, and it was
found by listing the symbols the mathematics uses and asking which had been introduced.

### What Was Added, and Which Additions Changed Something

**THE DEFINITIONAL LAYER.** The thrust coefficient and area ratio, the affine law in
coefficients, the Vandenkerckhove constant, the area-Mach and pressure-ratio relations,
the vacuum coefficient, and the split of specific impulse into characteristic velocity
times thrust coefficient. **That last one earns its place**, because it is why an article
about a vehicle with no published engine can quote a performance figure at all. The
characteristic velocity carries the propellant and the chamber, the thrust coefficient
carries the nozzle and the atmosphere, and **a claim about altitude compensation is a claim
about the second factor only**.

**THE STRUCTURE THE KEYSTONE ALREADY HAD AND DID NOT STATE.** The Fenchel-Young inequality,
which says exactly that every fixed nozzle lies at or below the envelope with equality only
at its own design point. The inverse transform, which says the family of bells and the
envelope carry the same information, so **an aerospike is a different point on a structure
that was already there rather than a new capability**. The envelope theorem and the
convexity, the second of which **has a physical reason rather than a formal one**, since a
higher ambient pressure selects a shorter nozzle, so the exit area falls as the ambient
rises and its negative is non-negative. **The envelope bends upward because the optimal
nozzle shrinks as the air thickens.**

**AND THE BREGMAN LOSS AS AN INTEGRAL**, which is the form that can be read off a picture.
The loss is the area between a horizontal line at the fitted exit area and the curve of the
area the envelope would have chosen. **The order of that subtraction was settled by a check
and not by inspection.** Written the other way round the expression is the negative of the
loss, and the first version of the numerical test was written that way, which is how the
sign was fixed before the relation reached the page.

**THE ATMOSPHERE, WHICH THE DRAFTING PASS USED AND NEVER SHOWED.** Both barometric forms,
the isothermal one being the limit of the other as the lapse rate goes to zero, the scale
height, and **a closed form for the pressure-time integral that says something the numbers
do not**. For an isothermal atmosphere climbed at a constant rate the integral saturates at
sea-level pressure times scale height over climb rate. **A rocket does not pay for the
atmosphere by the second. It pays once, and the bill is set by how fast it left.**

### One New Substantive Result

**THE EQUIVALENT GIMBAL ANGLE OF DIFFERENTIAL THROTTLING IS 0.91 DEGREES.** Converting the
ring's directional-average authority into the quantity a conventional stage would quote
gives a deflection whose sine is the throttle depth over pi times the ring radius over the
moment arm. At a throttle range of two tenths and a radius a quarter of the arm, that is
**under one degree**. **Differential throttling is adequate for trim and marginal for
anything faster**, and the article now says so with a number rather than leaving the reader
to assume the technique is a substitute for a gimbal. **The drafting pass had the authority
figure and never converted it into a unit anyone thinks in.**

### Three Defects in My Own New Work

**BOTH SCALE HEIGHTS ROUND TO 8,435 AND I PRINTED THEM AS 8,435 AND 8,434.** The sea-level
value is 8,434.9 metres and the isothermal value 8,434.5, a gap of four tenths of a metre
which is the lapse rate appearing in the fourth figure. **Rounding to whole metres makes
two numbers that agree look as though they disagree**, which is the opposite of what the
sentence was for. Caught by a check that compared the two roundings rather than the two
values.

**THE SYMBOL SCANNER'S PASS ORDER WAS WRONG THREE TIMES BEFORE IT WAS RIGHT.** Stripping
operators first breaks every declared name containing a macro, so `C_{F,\mathrm{vac}}`
stopped matching and reported a bare undeclared `C`. Stripping declared symbols first
breaks the operators instead, because a single-letter symbol such as `c` sits inside
`\frac`. **The only order in which no pass destroys another's input** is compound names
first as placeholders, macros second, bare letters last. Environment names then had to be
removed with their braces, because `\begin{cases}` leaves `{cases}` behind as three more
undeclared letters.

**AND ONE CONSTRUCTION WENT OVER THE CORPUS MAXIMUM BECAUSE OF THIS PASS.** `the second is`
reached six uses against a peer maximum of 0.34 per thousand, three of them added here by
the habit of writing `the first is` and `the second is` when introducing a pair of
relations. Three were varied and the rate is back under the maximum.

### Two Things Deliberately Not Added

**THE BASE PRESSURE OF A TRUNCATED PLUG IS NOT COMPUTED AND NOW SAYS SO IN AN EQUATION.**
The thrust splits exactly into the force on the wetted surface plus the base pressure times
the base area, and that decomposition is worth writing because it names the term this
article cannot evaluate. **A one-dimensional isentropic model does not produce a
recirculating turbulent base pressure**, so the regimes are classified by which quantity
sets that pressure and the magnitude is left to the literature.

**AND THE ASCENT PROFILE IS A GUESS WITH AN EXPONENT, WHICH THE EQUATION NOW SHOWS.** The
family is stated as a power law with the exponent swept from 1.5 to 3.0 rather than
described in prose, so a reader can see that two published points and a zero initial rate
do not determine a trajectory and that the spread is the honest measure of what that costs.

### Verification

`_verify.py` **0 errors and 0 warnings** across 301 posts. Library tests **119 of 119**.
**Article verifier 626 checks and 0 failures.** **A separate verifier for the new relations
runs 246 checks and 0 failures**, each relation evaluated against an independent route
rather than against the code that produced it. **The symbol check passes in both
directions**, every symbol in the mathematics declared and every declaration used, with the
macro allowlist confirming that all thirty macros are base TeX. Diction **0 constructions
above the corpus maximum** after three were varied. **Zero contractions, parentheses,
colons, semicolons or dashes outside verbatim quotations.** The stub-isolated production
build succeeded in **15.4 seconds** with no Liquid error against checksum-matched bytes,
**the rendered audit reports no findings across 543 pages**, and **source and rendered
display-equation counts agree at 45** with the inline count at **181 balanced pairs**, zero
raw dollar pairs, zero unresolved reference brackets and zero unrendered Liquid.

**AND THE BUILD WAS RUN TWICE FOR THE RIGHT REASON.** The first run finished against bytes
that three diction edits had already superseded, and a build of superseded bytes verifies
nothing about what ships, which is A345's lesson and which the frozen checksum made visible
immediately.

---

## A360, ABL Space Systems X-63, Drafting Pass

**TWO X NUMBERS WERE ISSUED ON ONE DAY WITH ONE DESCRIPTION AND THE DESCRIPTION IS IDENTICAL TO
THE BYTE.** The X-63A and the X-64A carry the same allocation date, the same sponsor cell, the
same engines cell and the same 101 characters. **Eleven descriptions repeat in the 539-row
register and ten of those repeats are munitions, targets and a ground station.** This pair is
the eleventh and the only duplicate among the 31 X rows.

**THE SPACE FORCE APPEARS IN THE X-PLANE REGISTER EXACTLY TWICE AND BOTH TIMES ARE HERE.** No
other row reads `USAF/USSF`. **And `1 rocket engine` appears in exactly two of 539 rows**, also
these, against an engines column that otherwise names a model. The X-60A, which A357 established
is a rocket, has an empty engines cell.

### A Correction to This Series' Own Arithmetic, Which Is the Most Important Thing Here

**THE REGISTER'S OFFICIALITY MARKUP HAS THREE STATES AND THE LAST TWO ARTICLES EACH SUMMARISED IT
IN TWO NUMBERS.** Recomputed from the saved page and confirmed by an independent re-parse of the
markup, the split is **436 official, 86 wholly unofficial and 17 partly unofficial** across the
register, and **21, 9 and 1 across the 31 X rows**.

**A358 gave the register-wide figures exactly right** as 86 and a further 17. It then gave the
X-row figures as 21 official and 9 not, **which accounts for 30 of 31 rows** because the partly
marked one has nowhere to go.

**A359 closed that sum by raising the official count to 22**, which places the partly marked row
on the official side. **That is the one side it cannot be on**, because the marking is the
compiler's statement that part of its wording is a reconstruction. A359's sentence reads `22 carry
official wording and 9 do not`.

**NEITHER ARTICLE IS PUBLISHED AND BOTH ARE PUSHED, SO THIS IS A DECISION RATHER THAN AN EDIT.**
A360 states the correct three-way split and says plainly that the previous two articles carried a
two-number version of it. **I have not touched A358 or A359.** The pilot may prefer that A359's
sentence be corrected at its source, in which case the change is one clause, and A358's needs a
third number rather than a different one.

### The Mathematics, Which Is an Identity That Removes the Vehicle

**THE INCREMENTAL VACUUM THRUST BOUGHT BY AN INCREMENT OF EXIT AREA IS THE EXIT PRESSURE ACTING ON
THAT INCREMENT, EXACTLY.** One line from the one-dimensional momentum equation. **So ambient
pressure is the variable conjugate to exit area**, the ideal altitude-compensating nozzle's thrust
curve is the Legendre transform of the vacuum thrust, every fixed nozzle is one of its tangent
lines, and **the loss of a fixed nozzle is a Bregman divergence** rather than being analogous to
one. The matched-expansion condition every text states separately is the transform's first-order
condition.

**AND THE DESIGN RULE THAT FALLS OUT WAS NOT ANTICIPATED.** The optimal fixed nozzle expands to
**the time-averaged ambient pressure of its own flight**, with nothing about the gas, the chamber
or the vehicle in it. **It emerged as an invariant before it was derived**, the same exit-pressure
fraction coming out of nine optimisations that shared no parameters, and it was then checked over
**one hundred independent searches across four trajectory shapes, five gas ratios and five chamber
pressures**. The optimal area ratios across that grid span 4.985 to 84.093, a factor of seventeen,
and every one produces an exit pressure equal to its own trajectory's mean ambient, worst
disagreement 4.2 parts in ten million.

**THE RULE THEN PUTS THE OPTIMUM SOMEWHERE IT CANNOT BE BUILT.** On the manufacturer's own
published first-stage trajectory the burn-averaged ambient pressure is 28.06 percent of sea level,
so the optimal nozzle sits at an exit-to-ambient ratio at liftoff of 0.2806, **inside the band
where an over-expanded nozzle separates from its own wall**. The bell is constrained twice and the
second constraint binds. **An aerospike has no divergent wall to separate from.**

**HALF OF THE ENTIRE PRESSURE-TIME INTEGRAL OF A 160 SECOND BURN IS COLLECTED IN THE FIRST 18 TO
34 SECONDS.** The altitude-compensation question is settled in the first fifth of the burn.

### The Other Half of the Programme, Where the Answer Reverses

**DIFFERENTIAL THROTTLING OF A RING OF MODULES GIVES A DIRECTIONAL AVERAGE AUTHORITY OF EXACTLY
THE THROTTLE DEPTH DIVIDED BY PI, AT EVERY MODULE COUNT FROM THREE UPWARD.** Not asymptotically.
More modules buy evenness rather than authority.

**AND THE EVENNESS DEPENDS ON PARITY.** The achievable moment set is a regular polygon with one
side per module when the count is even and **two sides per module when it is odd**, because a half
turn is a whole number of spacings only in the even case. **Nine modules steer as evenly as
eighteen and better than any even count below twenty. Eleven need twenty-four to beat them.** The
RS1 first stage carried nine engines in its first block and eleven in its second, both odd.

**AFTER A FAILURE THE RANKING REVERSES**, because a failure breaks the symmetry the parity argument
rests on. Nine modules keep 65.3 percent of guaranteed steering authority after losing one, twelve
keep 73.2, and **a four-module ring keeps none at all**, since no surviving module points toward
the gap.

### Findings From the Documents

**THE AWARD RECORD DOES NOT CONTAIN THIS PROGRAMME AND THE ANNOUNCEMENT SAYS WHY.** Twelve keywords
were put to the federal award system across five families of award type and the programme returns
nothing anywhere. **The instrument was a Space Enterprise Consortium other transaction agreement**,
which exists so that a company outside the Federal Acquisition Regulation can be paid, and which
does not appear where procurement contracts appear. **A359 found a government that spent
29,085,924.37 dollars without writing a designation down. This is the same silence produced on
purpose and explained in advance.**

**THE MANUFACTURER'S OWN TABLE DOES NOT CLOSE AND THE INCIDENT REPORT SETTLES IT.** The payload
user's guide gives nine engines at 12,100 pounds force and a total of 133,118, which is 22.24
percent more than the product. **133,118 divided by 12,100 is 11.0015**, and eleven engines give
133,100, a residual of 18 pounds force or 135 parts per million. **The company's static-fire report
describes firing all 11 first-stage engines and auto-aborting on Engine 10.** A nine-engine vehicle
has no Engine 10.

**A SUPPRESSED ENGINEERING PARAMETER WAS RECOVERED FROM A FAILURE REPORT.** No chamber pressure or
diameter is published for the E2 engine. The incident report names **a 4.5 kilohertz first
tangential mode**, and the first tangential mode of a cylindrical chamber fixes the diameter given
the speed of sound. Sweeping flame temperature, molar mass and the ratio of specific heats over 48
combinations gives **147 to 179 millimetres**, and adding a contraction ratio and a thrust
coefficient over 36 more gives **2.6 to 8.7 megapascal**. **That band sits inside the 3 to 10
megapascal band this article had assumed on general grounds several sections earlier**, which is
two routes sharing no input and agreeing.

**AND THE SAME REPORT QUANTIFIES WHAT MODULARITY COSTS.** Two of eleven engines went unstable
against a history of one occurrence in more than three hundred tests. **Two or more of eleven at
that rate has probability 6.0 parts in ten thousand, about one in 1,669**, and the observed rate is
54.5 times the historical one. **A modular engine is many small combustors sharing one manifold,
which is precisely a mechanism for correlating their start transients**, and the independence that
calculation assumes is what the incident falsified.

**THE SPONSOR SPELLS ITS OWN PROGRAMME TWO WAYS IN ONE DOCUMENT**, three times hyphenated and once
not, while its two web documents and the register are consistent and use the other form.

**AND THE `NEARLY 60 YEARS` IN THE AWARD ANNOUNCEMENT IS CHECKABLE AND CHECKS OUT.** 492 of this
article's 9,467 surveyed records name a plug, spike or altitude-compensating nozzle. The earliest
is a 1944 weather-rocket patent followed by a twelve-year silence, and **from 1956 the record is
continuous at every window length from five to ten years**, the largest later gap being four. That
is 63 years before the sentence, so the claim was modest rather than generous. **Seven decades of
publication and not one flight.**

### The Method Rules This Pass Earned

**EVERY CENTRAL NOUN OF THIS SUBJECT IS OWNED BY ANOTHER FIELD, WHICH IS A DIFFERENT SITUATION FROM
THE LAST SEVERAL ARTICLES.** There the homonyms were proper nouns and a qualifier fixed them. Here
`spike` is Spike Jonze and the spike lute, **`wake closure` is fatigue crack closure**, `open wake`
is Wake Forest University, `area ratio` is a regurgitant jet, `thrust coefficient` is a wind
turbine, **`gas generator` is nineteen-seventies coal gasification**, `annular` is a borehole and
**`altitude compensation` is a carburettor**. A bare `nozzle` returns ten results, one a diesel
injector. **So every pattern pins its noun with a second noun.**

**TWO GUARDS WRITTEN FOR UNRELATED REASONS TURNED OUT TO BE THE TWO THIS ARTICLE MOST NEEDED.**
`fracture`, earned by A335 against parachute opening loads, is the only thing standing between this
sweep and the crack-closure literature. `wind-energy`, earned by A341 against rotor aerodynamics,
is what refuses the wind-turbine thrust coefficient.

**A MEASUREMENT THAT DISAPPEARS ONCE IT IS ACTED ON CANNOT BE AUDITED.** The family-cost report
compared the current allow list against itself plus the tag, so the moment a family was opened on
that evidence the evidence reported zero. It now measures against the closed baseline and persists
the result to a file.

**A NEGATIVE LOOKAHEAD IN FRONT OF AN ALTERNATION GUARDS ONE CLAUSE, FOR THE FOURTH TIME IN THIS
SERIES.** Caught here before it ran, because the rule was written down.

**A `sys.path.insert` INSIDE A PER-RECORD FUNCTION IS A QUADRATIC COST THAT LOOKS LIKE SLOW
NETWORK.** `homonyms._anchor_stem` inserted a directory and imported once per harvested record, so
a thirty-thousand-record sweep left thirty thousand copies on the path. **Three thousand records
took 6.19 seconds and the same three thousand took 6.27 on the second pass with the path already
grown.** Hoisting the import and memoising the stem brings a repeated pass to 2.27 seconds. **Every
article in this corpus has been paying this.**

**A PAIRWISE CONTINUITY TEST IS DECIDED BY ITS SINGLE WORST GAP, WHEREVER THAT GAP FALLS.** The
first form of the `continuous from` test asked that no consecutive pair of publishing years differ
by more than three, and **one four-year gap in 1988 moved the answer from 1956 to 1992**. The
window form cannot be moved by one gap.

**A VERIFIER'S INDEPENDENT ROUTE DISAGREED WITH THE CLOSED FORM AND THE DISAGREEMENT WAS REAL
GEOMETRY.** The ring check evaluated the maximum at the module directions, which is right for an
odd ring and wrong for an even one, and reported eighteen failures with the two extremes swapped.
**For an even ring the direction of least authority points straight at a module.**

**A FORMULA'S ASSUMPTIONS MUST BE RECHECKED WHEN ITS SUBJECT CHANGES.** The engine-out section was
written twice, because the first version applied the regular-ring closed form to a ring with a
module missing. **It overstates the surviving authority by up to 2.62 and, at four modules, by all
of it.** No check was looking, and the error was found by asking whether the assumptions still held.

**A TABLE OF THRUST FIGURES IS NOT A DESCRIPTION OF ONE NOZZLE UNLESS THE TABLE SAYS SO.** The
difference of the payload guide's sea-level and vacuum thrusts divided by sea-level pressure would
give an exit area exactly, and it would mean nothing, **because two lines above the same document
says the two figures belong to two different engines.** Caught before it reached the page.

**TWO DEFECTS IN MY OWN PROSE WERE FOUND BY READING THE ASSEMBLED ARTICLE AND BY NOTHING ELSE.**
The first was date arithmetic, a three-year term from December 2019 ending in December 2022 against
an allocation of 20 April 2022, **written as four months where the answer is eight**. **Nothing in
the numeric suite was looking at dates**, because a month is not a quantity the calculation files
produce, and there is now a check that recomputes every interval the prose states between two named
dates. The second was an over-claim, that the chamber-pressure band recovered from the instability
frequency **sits inside** the band assumed independently. **It does not.** The recovered floor of
2.60 megapascal is below the assumed floor of 3, the two overlap over 93.5 percent of the recovered
band and 82.0 percent of the assumed one, and **overlap is the honest word**. The calculation had
only ever tested overlap; the prose promoted it to containment.

**AND I RAN THE WRONG BUILD FOR SIX HOURS.** `HANDOFF.md` says plainly that
`./_check.sh --drafts` scales superlinearly in link-definition count, that it took over three hours
by A340, and that **the agent runs the stub build per pass and the full corpus build at publication
absent instruction**. I started the full drafts build anyway, watched it hold one processor at a
hundred percent for five hours and forty-one minutes with an empty output directory, and only then
read the paragraph that forbids it. **The stub build it should have been took sixteen point nine
seconds.** The handoff had the answer before the work started, and the cost of not reading it was a
working day of wall clock. **A procedure written down is not a procedure followed**, which is this
pass's own theme arriving one more time.

**AND A SLOT IS THE ONLY DEFENCE AGAINST A SURVEY NUMBER GOING STALE.** Adding twenty-two
hand-written references moved the research count from 9,485 to 9,467, because a record that gains a
hand-written definition stops being auto-cited. **The prose said 9,485 and the verifier caught it.**
The repair was not to retype the number.

### Verification

`_verify.py` **0 errors and 0 warnings** across 301 posts, the two remaining warnings being the
progress counters in this file and `TASKLOG.md`, which this commit fixes. Library tests **119 of
119**. **Article verifier 608 checks, 0 failures**, including every number the prose states checked
against the file that produced it. **Identifier verification resolved 23 hand-written identifiers
through the registry against their claimed titles and years, and required a deliberately fabricated
identifier to return nothing.** Address sweep: 57 hand-written addresses, **two of which did not
exist and were replaced**, and 19 of which return 403 from `doi.org` redirecting into publisher
anti-bot pages, which is not a citation check either way. Diction **0 constructions above the
corpus maximum**. **The stub-isolated production build succeeded in 16.9 seconds with no Liquid error, against checksum-matched bytes**, and **the rendered audit reports no findings across 543 pages**, 171 of which carry display math. The article renders to 1,714,391 bytes with 19,474 links. Source and rendered display-equation counts agree at **15**, the inline count agrees at **70 balanced pairs**, and the page carries **zero raw dollar pairs, zero unresolved reference brackets, zero unexpanded slots, zero unrendered Liquid and zero double-escaped entities**. **Zero contractions, zero parentheses, zero colons and zero semicolons outside
verbatim quotations, and zero em or en dashes.** 

### What Is Open

**THE OFFICIALITY CORRECTION IS THE PILOT'S DECISION.** A360 states the right numbers; A358 and A359
still carry the two-number form and I have not edited them.

**A361 IS THE SIBLING DESIGNATION AND IT SHARES EVERY WORD OF ITS DESCRIPTION WITH THIS ONE.** This
article deliberately left it the instrumentation, the recovery gear and the question of what it
means for one programme to hold two numbers. **`Invocon` and `Troy7` return nothing at all from the
bibliographic index**, which is a measurement rather than a gap, and the award record returns
decades of instrumentation contracts under the Invocon name.

**AND `REVERSE_PROMPT.md` NOW HAS TWO WRITERS.** This report preserves the concurrent session's
below it rather than overwriting, which is a choice and not a convention.

---

## A376, Publication Review

**All four passes are complete. The article is committed and pushed and is NOT published.**
Lines 4,443, display equations 89, references 202 at 25.0 percent primary, prose about 23,100
words.

**THE REVIEW REFUTED A CLAIM THE ARTICLE HAD CARRIED THROUGH THREE PASSES.** It said that a
great-power war in which the belligerents hold a minority of world capability would be without
precedent, and that the resulting pool of non-participants was the novel feature of this case. The
same file that produced every other number in the article refutes it. Twenty wars with at least
twenty thousand battle deaths had less concentrated belligerents, among them the Russo-Japanese
War and the Gulf War. **The claim survived three passes because it was reasoned from the two world
wars rather than computed from the ninety-five wars in the file.** The article had a dataset
capable of testing its own central structural assertion and did not point it at it until the
fourth pass.

**COMPUTING IT RETURNED A BETTER RESULT THAN THE ONE IT REPLACED.** Belligerent concentration
predicts belligerent fortune at a correlation of minus 0.225 across seventy-six wars. The
prospective case sits at the ninety-sixth percentile of concentration, and ten of the twelve wars
in its band ended with the belligerents holding less than they started with, at a median of minus
five percent. That supports the article's conclusion by a different mechanism. Nobody captures
anything; concentrated belligerents simply have more to lose. The refuted claim was removed from
the opening, the bystander section, the agreements section, the gaps section and the conclusion.

**STRUCTURAL DAMAGE FROM THE REFERENCE PASS WAS FOUND AND REPAIRED.** Four subsections had been
duplicated, including two making the same allies argument, where the first said a quotation
appeared "earlier" when it appeared forty-six lines later. Four blocks on bystanders, official
assessments, shipping and the fiscal position had been inserted under the Alliances heading with
no topical relation to it. All eight were merged or relocated, and the article now has no
duplicate headings. Two directional references were wrong, one counting "the subsection after
next" when the target is three subsections later.

**THREE QUOTATIONS TAKEN FROM SUBAGENT REPORTS WERE VERIFIED DIRECTLY AND ONE WAS WRONG.** Clauset
and Eichengreen and Flandreau were confirmed verbatim from open-access copies. Lim and Cooper was
confirmed from the author manuscript, which spells "tradeoffs" where the article had hyphenated
it. **A one-character difference in a quotation is still a difference**, and the article now
quotes the verified text and says it is the accepted manuscript.

**A FOURTH CLAIM COULD NOT BE VERIFIED AND WAS REPLACED.** The article asserted that Allison's
project concedes there are no agreed metrics of national power. The page that was supposed to
carry that is dead, and the live essay does not say it. What the live essay does say is that the
cases use rise and rule "according to their conventional definitions, generally emphasizing rapid
shifts in relative GDP and military strength", which supports the same paragraph and is checkable.

**FOR THE PILOT.** The article is ready for a publication decision and has not been published. Its
editorial date is 2026-08-13, the slot is free of other posts, and `post_url` targets resolve
because both back-references point at articles already published. **Publishing will renumber the
series navigation on two live pages** from Part 1 of 2 and Part 2 of 2 to of 3, which is the only
outward-facing change beyond the new page itself.

## A376, Primary-Reference Pass

**References 86 to 202, lines 3,201 to 4,357, display equations 80 to 88, prose about 22,400
words.** Not published. One pass remains.

**THE PRIMARY SHARE WAS THE ASK AND IT ROSE.** Government documents went from 6 to 30 and datasets
from 12 to 20, so primary sources are now **25.0 percent of the external total against 10.5
percent in A375**. The substitutions are the substance of the pass. Alliance commitments are
quoted from the Washington Declaration, the Camp David statement and the Wilmington Declaration
rather than from descriptions of them, and reading them establishes that the Quad document
contains no mutual defence commitment and no extended deterrence language at all. Legislative
figures come from the public laws rather than the aggregates in circulation, which is how the
advanced manufacturing credit turned out to have moved from 25 to 35 percent in 2025. Taiwanese
energy dependence comes from the Taiwanese ministry at 94.62 percent.

**A SCAN DROVE THE PASS RATHER THAN A READ-THROUGH.** Counting citations against word count per
section returned 27 sections carrying none, three of them among the longest in the article.

**A 163-WORD STUB BECAME A SECTION.** `What the alternative instruments say` had asserted that the
instruments disagree while citing nothing at all. It now reports five with their own published
definitions and caveats, and carries the critique literature, including Carroll and Kenkel's
finding that the capability ratio **barely outperforms random guessing** at predicting dispute
outcomes, which is the sharpest objection to this article's own instrument and belongs in it.

**FORTY-FIVE EXISTING ANCHORS WERE NAMED IN PROSE WITHOUT LINKS.** The agreements, disagreements
and epistemic roll-call named authors the article had already defined references for. That was a
correctness defect before it was a density one.

**A PRIMARY DOCUMENT SUPPLIED THE ONE HISTORICAL CASE THE BYSTANDER ARGUMENT HAD LACKED.** Two
Foreign Relations documents record American officials in 1953 worrying about Japanese dependence
on Korean War special procurement, including the fear of "a drastic decline in United States
special procurement following a Korean armistice". That is a bystander gaining materially from a
war it did not join, recorded by the belligerent that was paying for it, as it happened, and it
falls in the same case this article's base rate assigns the largest stalemate effect to. Both
quotations were confirmed against the Department's own published text rather than taken from a
subagent's report.

**WHAT WAS DELIBERATELY NOT ADDED.** Several works the sweeps surfaced were left out because no
claim in the article needed them, and a reference that supports nothing is padding. Where a
quotation comes from a publisher-deposited abstract rather than an article body, the Epistemic
State says so by name.

**VERIFICATION.** `_verify.py` 0 errors across 303 posts, 245 checks across three harnesses with
none failing, build clean, rendered audit no findings across 468 pages, source-to-rendered display
count agreeing at 88, delimiters balanced with no blank-line defects and inline delimiters paired,
zero contractions and zero dashes in prose, zero bullet-list-only anchors, and all 200 reference
URLs swept returning 124 direct resolutions, 73 publisher refusals each confirmed registered by
DOI content negotiation, and 3 empty-202 responses from a publisher that answers that way.

## A376, Equation-Density Pass

**Display equations 39 to 80, lines 2,896 to 3,201, inline expressions 9 to 12, references held at
86.** Not published. The article now carries more display mathematics than either companion at
comparable length, A374 having 63 and A375 75.

**A SCAN DROVE THE PASS AND NOT A READ-THROUGH.** Every prose line carrying a figure with no
display block within six lines was listed, which returned 160 candidates across 42 sections and
made the thin sections obvious. The additions are mostly definitions the article had been carrying
in words, including the component share, the relative change with its equal-length prewar window,
the constant-membership share, the belligerent share and its bystander complement, the exact
contribution decomposition and the scenario map.

**THE SOURCE-TO-RENDERED COUNT CAUGHT EIGHT DEFECTS AND NOTHING ELSE WOULD HAVE.** Eight of the new
blocks closed flush against the following prose, which kramdown folds into inline mathematics.
`_verify.py`, the production build and the rendered audit all passed with them present. **A
scratch build carrying the real configuration and this draft alone now reports 80 source blocks
against 80 rendered**, and the published A375 in the same build reports 75, which is the control
that shows the method measures what it claims to.

**A SECOND RENDERING DEFECT PREDATED THIS PASS AND THE EQUATION WORK SURFACED IT.** Counting
unescaped dollar signs outside display blocks returned an odd number. The odd one was a currency
sign inside a quotation added during the drafting pass, which would have left MathJax with an
unterminated inline delimiter free to consume following text as mathematics. Currency signs inside
quotations are now escaped, the reader sees the character, and the rendered page carries no
literal backslash.

**A FIGURE WAS CHASED TO ITS SOURCE RATHER THAN LEFT IN AN EQUATION UNVERIFIED.** Writing the
ratio of the Iraq cost outturn to the top of the forecast range meant putting a specific number in
a display block, and that number had reached the draft through a subagent quoting a work it had
not retrieved. The open-access Chang and others paper was fetched and the sentence confirmed
verbatim, its two-column layout interleaving exactly as A375 recorded for scanned sources. The
article now attributes the figure to Chang and others attributing it to Bilmes, and says plainly
that it is not independently checked here.

**A THIRD HARNESS WAS ADDED AND DELIBERATELY KEPT SEPARATE.** `verify_derived.py` recomputes 53
pieces of arithmetic the article performs on figures it quotes. It is distinct from the two that
recompute from primary data because it cannot establish that a source says what the article
reports, only that the division printed beside a quoted pair is the division of that pair. The
Epistemic State now says so, and the stale count of 166 constants it carried was corrected to 238.

**VERIFICATION.** `_verify.py` 0 errors across 303 posts, 238 checks across three harnesses with
none failing, build clean, rendered audit no findings across 468 pages, 160 display delimiters
balanced with no blank-line defects, braces and `\left`/`\right` balanced in every block, zero
contractions and zero dashes in prose, all 86 references cited and alphabetically ordered.

## A376, Whether a War With China Would Change the Global Balance of Power, Drafting Pass

**The draft stands at 2,896 lines, 39 display equations, 86 references and about 16,300 words
of author prose**, at the editorial date 2026-08-13, categories `geopolitics military war-gaming`,
series `war_with_china` index 3. Not published. `_verify.py` reports zero errors, `./_check.sh`
builds clean, and the rendered audit finds nothing across 468 pages.

**THE ARTICLE'S SPINE IS COMPUTED RATHER THAN QUOTED.** Two Correlates of War files were
downloaded and the base rate was computed from them, which is the thing the surveyed literature
asserts without measuring. Across 95 inter-state wars the median belligerent gained about seven
percent of relative standing over the following decade, **but 38 percent of winners declined**.
Restricted to wars above 100,000 battle deaths, **every one of eleven losers declined, median
-41.8 percent, while winners gained a median 12.6 percent and more than a third of them still
fell**. The prewar trend has no predictive power for the postwar change, `r = -0.038`, which is an
informative null against the reading that wars merely ratify a trend already underway.

**THE VERSION IN USE WAS WRONG AND THE LANDING PAGE SAID SO.** Work began on National Material
Capabilities v6.0, which ends in 2016. The landing page is titled v7.0 and runs to 2022. Every
figure was recomputed. The base rates barely moved, since the historical data did not change,
but the headline year moved six years and the present-day ratio moved from 1.73 to 1.89.

**THE NUMBER HARNESS CAUGHT TWO ERRORS AND ONE OF THEM BECAME A SECTION.** 185 constants were
re-entered by hand and recomputed. One was a rounding error. The other was a claim that the
capability ratio has exceeded one in every year since 1995; it dips to 0.9987 in 2002. Tracing
that dip found a documented definitional break, the urban component switching from cities over
100,000 to United Nations agglomerations of 300,000 or more. **The break alone removes 2.117 index
points while every other component adds 0.927, and holding urban population at its 2001 share puts
the 2002 ratio at 1.14.** The one year this index does not place China ahead is an artefact.

**A CLAIM WAS WITHDRAWN AFTER A SUBAGENT CONTRADICTED IT.** The draft called the averaging rule a
defect. The codebook documents it, in the same paragraph that says the sums "may be slightly
greater than or less than 1.0". The section was rewritten to credit the documentation and to
contribute the magnitude instead, since the deviation reaches 1.0747 and misses one by more than a
thousandth in 183 of 207 years. **A second false claim, that the 2002 break was undocumented, was
also removed.** The honest contribution is narrower and survives.

**A VALIDATION STATISTIC WAS SHOWN TO BE THE RIGHT ANSWER TO THE WRONG QUESTION.** The project
validated the urban change by a panel correlation of 0.99 on CINC. That bounds the error for a
researcher using the whole panel and bounds nothing for a bilateral comparison, which is what
almost every citation of this index makes. For China the same change is 52 percent of one
component. **A later revision cuts recorded United States urban population by 44 percent in one
year, and the codebook names the United States as the most prominent case.**

**THE STRUCTURAL FINDING IS THE ONE WORTH KEEPING.** The belligerents of 1914 held 82 percent of
measured world capability and those of 1939 held 98. Two states fighting this war would hold about
36 percent, 45 on the widest plausible coalition. **There has never been a great-power war with a
bystander pool this large**, which is why the historical test of the bystander hypothesis returns
nothing and why the mechanism everyone asserts has not previously been testable.

**THE FINANCIAL SERIES WERE PULLED DIRECTLY AND REFUTED A POPULAR CLAIM.** The reserve-composition
data were retrieved from the Fund's own interface and parsed here. The dollar share fell from
75.03 percent in 1999-Q1 to 56.70 in 2026-Q2, **and it fell more slowly after the 2022 reserve
freeze than in the twenty-three years before it**, -0.64 against -0.68 points per year. **The
renminbi's share peaked at 2.85 percent in 2021-Q4, one quarter before the freeze**, and has lost
a quarter of that since. The accelerated-de-dollarisation claim does not survive the series.

**ONE INSTITUTIONAL FACT WAS READ RATHER THAN INFERRED.** The Joint War Committee listed-areas
circular of 16 September 2026 was retrieved and read in full. Taiwan, the Taiwan Strait, the South
China Sea, mainland China and Hong Kong appear nowhere in it, while the Southern Red Sea and
fourteen Middle Eastern entries do. **The market that prices war risk for the busiest container
waterway in the world is charging nothing extra for it.**

**THE RAND TABLE WAS READ OFF AN IMAGE BECAUSE COLOUR DOES NOT SURVIVE TEXT EXTRACTION.** On the
balance-of-power column the ten wars grade one green, six yellow, three red. That count agrees
with A375's independent figure and with a subagent's pixel reconstruction, so three routes concur.
**The three cases where every combatant was wrong are the three largest wars**, which is sharper
than the ratio alone.

**SIX SUBAGENTS SWEPT THE LITERATURE AND THEIR FINDINGS WERE NOT TAKEN ON TRUST.** Load-bearing
quotations were re-verified against retrieved documents, including both RAND volumes read in full
and the RAND commentary page fetched directly. One subagent reported a quotation it had discarded
after finding a summariser had produced text absent from the raw HTML, which is the reason nothing
from a summarising fetcher was used. Several quotations come from publisher-deposited abstracts
because the publishers refuse automated clients, **and the article labels those as abstracts
rather than as the authors' prose**.

**THE CONTRARY EVIDENCE IS IN THE ARTICLE RATHER THAN OMITTED.** Trade modelling puts a
non-belligerent ally's proportional output loss at nearly three times the American one, RAND
estimates Chinese losses at about four times American ones, and the one study taking
non-belligerents as its subject argues a war would derail Indian growth rather than advance it.
Each contradicts a limb of the arithmetic and each is stated as a challenge.

## A375, Pathological Word Usage Pass

**THE ENUMERATED TIC CLASS FOUND NOTHING, BEFORE OR AFTER.** `diction.py tics` reports 0 words at
or above the peer maximum and `report` reports 0 constructions above the corpus maximum. Its own
banner says the class is enumerated and not discovered, so the pass had to find what *this* article
invented. `tmp/a375/pathology.py` compares unigram, bigram and trigram rates against all 258
published posts, with quotations and mathematics stripped.

**THE PATHOLOGY WAS ONE CLUSTER: the article kept talking about itself.** `this article's` at 1.97
times the peer maximum, **`the article above` used six times and never once by any peer**, and it
was the opening sentence of six consecutive survey subsections.

**THE SIGNATURE WORD WAS ONE NO GATE WOULD FLAG.** `finding`, 45 uses, 33 of them the noun
labelling a conclusion, sitting at **2.24 against a peer maximum of 8.56**. **The case for cutting
was repetition and not frequency**, four near-identical bold openers inside one section. A reader
meets that formula four times in a few pages whatever the corpus says.

**THE PASS CAUGHT ITSELF OVER-CORRECTING TWICE.** Varying the six openers put `earlier` into five
of six replacements. Fixing that put `above` into four with two sharing a passive shape. And
redistributing attribution verbs pushed `report that` over the peer maximum. **Each was caught by
re-measuring, not by reading.** This is A374's failure mode recurring, and the lesson is that a
diction fix must be measured after it is applied, exactly like an equation pass.

**WHERE IT STOPPED IS RECORDED RATHER THAN SILENT.** `report that` stays at 1.37 times the maximum
because the peer set is not literature surveys. `own` stays because a source's own words is the
method. All six `article's own` uses stay because each marks the boundary between the article's
arithmetic and a source's.

---

## A375, What Rebuilding Would Take After a War With China, Publication Review

**ALL FOUR PASSES COMPLETE. Committed and PUSHED. NOT PUBLISHED, as instructed.**
References **97 to 222**, display equations **63 to 75**, lines **2,303 to 3,797**,
author prose about **12,800 to 21,000 words**, 16 sections and 40 subsections.

### The opening paragraph contradicted the article's own evidence

The first paragraph said **every major public wargame stops within about three weeks**.
Seventeen hundred lines later the article cites Stewart modelling the campaign
to the seizure of Taipei on **day 46**. The opening now gives the horizon precisely and says
that no public game located continues into the period the article is about, which is both true
and a stronger claim. The conclusion carried the same defect and was fixed with it.

### Three antecedent defects, two of them created by the previous pass

An inserted accountability-office paragraph displaced *the two brackets* from the build-duration
figures it referred to. An inserted note about the Archigos dataset split an attribution from the
figures it introduced, so published rates read as though they came from the current data file.
And **a forward reference was described as backward**, the workforce section citing a report
*cited above* that was first cited 106 lines **below**.
**Inserting a paragraph moves an antecedent, and no checker in this repository sees it.**

### What else the scans found

A date error, the bombing survey said to precede the econometrics by *thirty years* when 1945 to
2009 is more than half a century. A broken promise, the article undertaking to treat Taiwan's
missing reconstruction estimate *below as one of the gaps* when the gaps section did not contain
it; it is now the fifth gap and **the count is recomputed from the bullets**. Two overclaims in my
own prose, including a conclusion asserting that *every* correction made the secondary literature
look overconfident, which was false because two corrections were the article's own. Eleven ranking
claims scoped. Six acronyms expanded, four of which first appear inside quotations that cannot be
altered, so the expansion went into the introducing sentence.

### The survey section, and the finding that reorganised it

Fifteen clusters were added and **125 references**, every one confirmed in a registry with matching
authors, title, year and venue, with a finding attached only where an abstract or full text was
retrieved.

**The best single finding is that three incommensurable quantities wear the same units.** The
circulating cost estimates for a Taiwan contingency run from about two trillion dollars to about
ten, and that is not a disagreement about magnitude. The low end counts activity at risk and its
authors say in their own text that they do not estimate welfare. The middle counts modelled welfare
loss and is far smaller. The high end bundles destruction, mobilisation and panic behind a method
that could not be read. **The only properly specified input-output estimate located, a geological
survey model of a total gallium and germanium cutoff, lands at 3.4 billion dollars**, three orders
of magnitude below the headlines.

### The survey corrected this line's own headline finding

**The twenty-day liquefied natural gas figure is the commission's, carried in its footnotes, and
appears in no Taiwanese government energy series located.** The article now says so and sets
against it the one stockpile that is statutory, 60 days of petroleum held by industry plus 30 by
government. **Petroleum has a 90-day statutory reserve and the fuel the island is moving toward has
none.** Food supplies a third horizon at about six months, so the ordering is gas, coal, food, and
**the binding constraint in a long blockade is energy rather than starvation.**

### The reachability figure was nearly reported wrong

A sweep showed 89 of 219 addresses failing, 87 of them digital object identifiers, which looked
like a corpus problem. Tested individually, the registry resolves with a 302 every time and **the
publisher refuses the client**. The identifier works and the paywall does not. **Writing the
aggregate into the article would have recorded publisher bot policy as a fact about the citations.**

### Verification

`_verify.py` **0 errors and 0 warnings across 302 posts**. **111 arithmetic and structural
statements recheck by script with no failures**, up from 85, and they now include every stated
reference-composition figure recomputed from the list, the agreement and disagreement counts, and
the gap count. Diction reports **0 words at or above the peer maximum**. Build 12.7 seconds,
**rendered audit no findings across 458 pages**, and **source and rendered display counts agree at
75**, which is this line's mandatory check.

### What remains, and it is the pilot's decision

**A375 is finished and unpublished.** The only blocking item is the date.
**`_drafts/android_development_on_freebsd.markdown` still carries the same editorial date,
2026-08-12.** `_verify.py` builds its date map from `_posts` only, so two drafts sharing a date are
invisible while both are drafts and become a hard `date-collision` error the moment either
publishes. The run from 2026-08-20 onward is free of both posts and drafts. **That is a content
decision and it has not been made.**

---

## A375, What Rebuilding Would Take After a War With China, Primary-Reference Pass

**THREE OF FOUR PASSES COMPLETE. Committed, not pushed, not published. Only the publication
review remains.** References **78 to 97**, display equations **50 to 63**, lines **1,448 to
2,303**, author prose about **7,600 to 12,800 words**.

### The pass began by finding a defect the verifier structurally cannot see

**Four references were defined, listed and never cited in the argument.** `_verify.py`
reported zero unused anchors, and it was right on its own terms, because **the References
bullet list cites every anchor**, so a reference that appears only in that list satisfies the
unused-anchor check. The four were the Section 301 maritime report, the annual threat
assessment, the commission's Taiwan chapter and a War on the Rocks essay.

**All four turned out to be precisely the primary documents this pass wanted**, which is why
the defect mattered rather than being cosmetic. The check to run is a citation count against
the body text alone, excluding the bullet list. The article now carries 97 references and 97
cited in the body.

### The best single find is an energy figure that sits on the wargame horizon

The commission's Taiwan chapter reports the island holds storage for **20 days** of liquefied
natural gas and about **42 days** of coal. The published games end at about **21 days**.
**The modelled war ends at about the moment the island's gas runs out.**

That is not a finding about the games, which model an invasion rather than a blockade, and the
two quantities were measured by different people for different purposes. It is a finding about
the aftermath, and it joins to the Heim denial essay, which states that a defeated invasion is
plausibly followed by **a shift to blockade**. **Neither source makes the connection**, and
every reconstruction estimate in the article assumes electricity is available to rebuild with.

The same chapter supplies the thesis at the smallest scale anyone has tested it. Undersea
cables to the Matsu Islands were cut in 2023 and the islands were offline for weeks; cut again
in 2025, backup installed in between kept services running. **The repair time did not improve.
The redundancy did.**

### And the European bombing survey measured the thesis in 1945

In the anti-friction bearing industry, building destruction equalled about **half the preraid
floor space** while **machine tools destroyed equalled 12 percent of the original inventory**.
The survey adds that "it proved more difficult to put the plants out of operation than had been
foreseen". **The article's organising claim, that what bombing destroys is production rather
than the means of production, is a 1945 finding before it is a 2009 econometric one.**

### Six corrections came from reading the primaries behind secondary accounts

- **Japanese damage figures disagree with the survey Davis and Weinstein cite.** 2,510,000
  buildings against the paper's 2.2 million, 330,000 fatalities against three hundred
  thousand, and the important one is a difference of subject: **the survey's 40 percent is
  built-up area destroyed**, where the share who lost homes is about 30 percent. **An earlier
  draft additionally inserted the word urban into the paper's sentence**, producing a claim
  that matched neither source.
- **Quinlivan 1995 states no 20-per-thousand rule.** It is descriptive, sectioned by ratio
  band, and reaches 20 per thousand as a measured value in two cases. The norm was hardened by
  FM 3-24 of 2006, which credits nobody, and **the 2014 revision deleted the ratio entirely**.
  The number the central calculation uses is in no current doctrine.
- **Taiwan's population was stale and unsourced.** The ministry series is now cited and the
  requirement is **465,980 rather than 468,000**, with the declining trend stated.
- **The 395-ship figure is a 2023 projection and not a count**, and the 2025 edition of that
  report gives no fleet total at all.
- **The Ukrainian damage growth is the report's own 15.5 percent**, not a ratio of rounded
  inputs giving 16.
- **The Nature Food claim was too strong**, since the largest scenario assumes attacks on
  seven countries including China.

**One claim was strengthened instead.** The 2025 National Academies report, read in full,
carries **no economic recovery analysis and no recovery timescale for human systems**, and
names that as a research gap itself. **The only official study with a recuperation analysis is
the Office of Technology Assessment's of 1979**, which said that the effects which cannot be
calculated "are at least as important as those for which calculations are attempted".

### Two methodological findings worth keeping

**A failed string match is not evidence of a bad quotation.** Nineteen quotations verified on
first match; several more failed and were confirmed only after normalising for scanned
hyphenation, two-column interleaving, and a running header that fell inside a sentence.
Every quotation was confirmed against source text rather than against an agent's report of it,
and three delegated leads needed correction.

**The user agent cuts both ways.** Nine addresses answer a browser string and refuse an honest
one carrying a contact address, while `archive.dni.gov` and `documents.worldbank.org` do the
exact opposite. **A single-agent sweep therefore reports blocks that are properties of the
client**, and a two-agent sweep took reachability from 70 to 79 of 94. Separately, `osti.gov`
answered a throttled sweep with HTTP/2 stream resets rather than a status code, which is a
transport failure and must not be recorded as a 403. Both are now in `URL_VERIFICATION.md`.

### Verification

`_verify.py` **0 errors and 0 warnings across 302 posts**. **85 arithmetic statements
rechecked by script with no failures**, up from 53. Diction reports **0 words at or above the
peer maximum**, the earlier deliberate flags having fallen as the article grew. No prose
colons, semicolons, parentheses, dashes or contractions. Build 12.7 seconds, **rendered audit
no findings across 458 pages**, and **source and rendered display counts agree at 63**, which
is the mandatory check this line earned the hard way.

### What remains

**The publication review, which is the fourth pass.** Under the standing instruction it must
also make the article a comprehensive survey of the contemporary literature, with no length or
reference limit. **The 2026-08-12 date still collides with the
`android_development_on_freebsd` pre-release candidate**, invisible to the verifier while both
are drafts and a hard error the moment either publishes. That remains the pilot's content
decision and has not been made.

---

## A374 IS PUBLISHED AND LIVE

**PUBLISHED 2026-09-19 at the editorial date 2026-08-11.** Moved by `git mv` to
`_posts/2026-08-11-published_wargames_of_war_with_china.markdown` and live at
`/geopolitics/military/war-gaming/2026/08/11/published_wargames_of_war_with_china.html`.
**The two-commit pattern was followed**, the draft state having been committed across five earlier
commits and this being the publication move.

**THE INTERLOCK WAS VERIFIED BEFORE THE MOVE, NOT AFTER.** The 2026-08-11 date slot was free. All
three `post_url` targets were already published, so no build-breaking forward reference exists.
Nothing in the corpus forward-references this article. The article carries no series, so **no
navigation was renumbered on any live page**, which is the failure mode that renumbered four pages
when A373 published.

**THIS IS THE FIRST POST WHOSE FIRST CATEGORY IS `geopolitics`**, so it claims a new top-level path.
**Fifty-eight sibling repositories were checked** for a name matching `geopolitics`, `military` or
`war-gaming`, and none exists. That check is the one the `keleusma` shadowing incident exists to
force, and a live-site probe alone would not have answered it, since an unclaimed path and a shadowed
path both return 404 before publication.

**Deploy gate before pushing.** `_verify.py` 0 errors and 0 warnings across **302 posts**, build ok,
and the rendered audit reporting **no findings across 466 pages**.

### Draft release announcement, for the pilot to review

```
New Blog Post: What Published Wargames Say About a War With China

Everyone cites the same handful of Taiwan wargames and almost nobody reads them. I read them,
checked every number, and found that the most confident summaries get the headline result wrong.

Key takeaways:
- The invasion does not fail in "the vast majority" of the CSIS iterations. Nine of twenty-four
  ended in clear Chinese defeat, fourteen ended in stalemate, and the one Chinese victory came
  when the United States stayed out.
- The nuclear study finds that seven of eight nuclear uses began with a China team facing exactly
  the conventional defeat the other games treat as the happy ending.
- The economic consensus is an artefact of citation. Three original estimates exist and everything
  else re-cites them, and two estimates of the same blockade differ by nearly a factor of two
  because one prices trade disruption and the other a macroeconomic shock.
- The United States intelligence community says Chinese leaders have no current plan for 2027 and
  no fixed timeline, which contradicts the closing-window premise the whole genre assumes.

You can read the full article here:
https://sgeos.github.io/geopolitics/military/war-gaming/2026/08/11/published_wargames_of_war_with_china.html

Let me know your thoughts. I would love to hear how you handle load-bearing numbers that arrive
through a summary rather than from the source!

hashtag#Wargaming hashtag#NationalSecurity hashtag#Taiwan hashtag#Research hashtag#Verification
hashtag#DataQuality hashtag#Analysis
```

---

## A374, What Published Wargames Say About a War With China, Four Passes and a Diction Pass

**THE PATHOLOGICAL WORD-USAGE PASS FOUND AN OVER-CORRECTION I HAD INTRODUCED MYSELF.** `and not` ran
at **1.67 per thousand against a corpus median of 0.60** while `rather` had fallen to **0.28 against a
median of 4.00**. The equation pass had substituted `and not` for `rather than` and the survey pass had
raised it again, so avoiding the corpus-normal construction manufactured a replacement tic. That is the
failure `STYLE_GUIDE.md` names, and the fix was to restore `rather than` where the structure is
parallel rather than to invent a third formula. **34 constructions varied**, leaving `and not` at 0.28
and `rather` at 1.30, both below median. The `Let X be` equation opener went 16 to 5 across three
rotated forms, `were read from` 10 to 3, and `which is` 14 to 9. **Four were kept on purpose**, two
paraphrasing McGrady and one quoting TIDALWAVE, because editing a quotation to hit a rate is
falsification. The full diff was read line by line, an n-gram rescan confirmed no new formula, and the
rendered audit reports no findings across 466 pages.



**THE PUBLICATION REVIEW DOUBLED THE ARTICLE AND TRIPLED ITS REFERENCES, 32 TO 111.** On the pilot's
instruction the article now also serves as a comprehensive survey of the contemporary literature. A
new section of thirteen subsections covers the other operational wargames, the allied and European
games, invasion feasibility in the peer-reviewed journals, whether Taiwan is strategically decisive,
the nuclear escalation split, deterrence theory, blockade, the economic estimates, semiconductor
dependence, official assessments, wargaming as a method, and artificial intelligence in wargaming.
Four delegated research sweeps supplied leads and **every citation was verified here before use**,
which is why several leads did not survive into the article.

**THE OFFICIAL ASSESSMENT CONTRADICTS THIS ARTICLE'S OWN PREMISE.** The threat assessment of the
United States intelligence community, prepared with information available as of 14 March 2026, states
that **Chinese leaders do not currently plan to execute an invasion of Taiwan in 2027, nor do they have
a fixed timeline for achieving unification**, and that Chinese officials recognise an amphibious
invasion **would be extremely challenging and carry a high risk of failure**. The article was built on
a closing-window premise, so this now appears early in the premise section rather than buried in a
survey. It is the sharpest official contradiction of that premise available and it comes from the body
whose job is to assess Chinese intent.

**THE ECONOMIC LITERATURE IS SMALLER THAN IT LOOKS.** Only Bloomberg, Rhodium and the Institute for
Economics and Peace produce original numbers. The Commission, the German Marshall Fund and others
re-cite them, which manufactures a false impression of convergence. **The two blockade estimates differ
by a factor approaching two**, 2.8 percent of global output against 5 percent, because one prices trade
disruption and the other a macroeconomic shock. RAND's 2025 work prices sanctions alone and therefore
sits an order of magnitude below the war figures, so quoting it beside them would misrepresent both.

**THE SEMICONDUCTOR FIGURE NOW CARRIES ITS THRESHOLD AND ITS DATE.** The famous 92 percent is a 2019
measurement of capacity below 10 nanometres, where that capacity was about 2 percent of all capacity.
TrendForce measured 68 percent at 16 and 14 nanometres and below in 2023. The two are not in conflict,
and a claim quoted without its threshold cannot be checked.

**TWO INDEPENDENTLY DESIGNED GAMES LAND WITHIN EIGHT PERCENT OF EACH OTHER.** The Sasakawa hex-map
exercise destroyed 127 major Chinese ships where the CSIS base scenario averaged 138. **The starkest
number in the public record comes from the game members of Congress played**, where 40,000 of 50,000
landed troops became casualties in six days.

**THE METHOD CRITICS ARE NOW IN THE ARTICLE, AND THEY ARE WARGAME DESIGNERS.** Their case is that
wargames are about understanding and not knowledge, that a game often reveals more about its players
than about the war, and that combat wargames should not be repurposed to answer questions about
deterrence or war termination. One RAND study finds artificial intelligence least promising for games
**played as one-offs or a very limited number of times**, which describes most of the public Taiwan
games.



**THE PRIMARY-REFERENCE PASS CAUGHT A MISATTRIBUTION IN MY OWN DRAFTING PASS, AND THE PRIMARY SAYS
CLOSE TO THE OPPOSITE.** The drafting pass credited the Heritage Foundation's executive summary with
four TIDALWAVE figures, the culmination ratio, the five to seven and thirty-five to forty day
munitions brackets, and ninety percent of aircraft destroyed on the ground. **The archived executive
summary contains none of them.** They came from a search-engine summary and a news article.
heritage.org refuses every page to curl and to the fetcher, so **a Wayback snapshot of 14 April 2026
supplied the text the live site would not**, bylined Robert Greenway and Anna Gustafson. **The two
equations built on those figures were deleted** and the figures are now labelled press claims. **On
munitions the primary states that platform destruction, not munition exhaustion, limits combat power**
in the most intense cases, with part of the magazine never fired because the platforms are already
destroyed. That is a different failure from running out of missiles and it weakens the tidy reading
that stockpile depth is the binding constraint.

**THE SCENARIO YEARS NOW HAVE A SOURCED ORIGIN.** The drafting pass could say only that the reports
gave no rationale. The Senate Armed Services Committee stenographic transcript of 9 March 2021 carries
Admiral Davidson telling Senator Sullivan that the threat is manifest during this decade, in fact in
the next six years. **2021 plus six is 2027**, which is where CSIS at 2026, CNAS at 2027, the nuclear
game at 2028 and the Heritage exercise at 2030 cluster, and the TIDALWAVE summary independently says
many insiders point to 2027. The demographic-peak explanation the external summary offered remains
unsupported.

**THE PREMISE NOW CARRIES BEIJING'S OWN PRIMARY.** The 2022 white paper states that peaceful
reunification is the first choice and that force is not renounced. It announces no timetable. That is
the minimum the wargames assume and no more.

**All four passes complete. Committed and PUSHED on the pilot's instruction. NOT PUBLISHED**, and
publication was explicitly not requested.

Standalone analytical essay at editorial date **2026-08-11**, categories
`geopolitics military war-gaming`, **2,069 lines, 63 display equations, 53 inline expressions, 111
references, about 12,100 words.** Article number and date were chosen as the next free number after
the reserved X-Planes range and the only unused date between 2025-12-17 and 2026-08-19.

**THE SOURCE WAS AN EXTERNAL MODEL'S SUMMARY AND NINE OF ITS CLAIMS WERE WRONG.** The pilot supplied
an exchange with an external large language model. Every claim was checked against the primary
reports. **The largest error was that the invasion fails in the vast majority of the CSIS iterations.**
The counts give **9 decisive Chinese defeats, 14 stalemates and 1 PLA victory out of 24**, the victory
being the run where the United States stays out. **The second was that the record is uniform.** The
summary's own logistics citation was a news article about the Heritage Foundation's TIDALWAVE model,
**whose stated aim is to push the American culmination date beyond the PRC's, which implies the
United States culminates first**, and the summary did not say so. The blunter phrasing about
catastrophic defeat is a press claim and is not in the archived executive summary, as the
primary-reference pass established below. The other seven corrections are listed in the article's Epistemic State.

**THE KEYSTONE IS THAT THE TWO CSIS GAMES POINT AT THE SAME MOMENT FROM OPPOSITE SIDES.** The
conventional game treats destruction of the amphibious fleet as decisive. The nuclear game puts
**seven of its eight nuclear uses at Chinese first use while facing exactly that defeat**. The
conventional failure the external summary treated as the end of the gamble is where the nuclear games
locate the greatest danger. **This synthesis is marked as inference and is not stated in that form by
any single report.**

**EQUATION DENSITY WENT 12 TO 48 AND EVERY EQUATION IS ARITHMETIC ON A PUBLISHED FIGURE.** The opening
says so, because none of them models a war. The consistency checks close against the sources. **The
population balance leaves implied net migration at zero**, the crude rates recompute from the counts,
and **the Bloomberg dollar and percentage figures imply world output of about 98 and 110 trillion
dollars**, which are plausible for their years. **The equation pass also found something the drafting
pass had missed.** Comparing only midpoints hid that **the latest Bloomberg ratio of Chinese to
American loss, 1.7, falls below the entire RAND range of 2.5 to 7.**

**FOUR ASSUMPTIONS ARE MINE AND NOT THE SOURCES' AND ARE LISTED AS SUCH**, the one most likely to be
mistaken for a report finding being the independent forty percent loss per voyage behind the ship
survival figure.

**VERIFICATION, AND ONE LIMITATION THAT MATTERS.** `_verify.py` reports **0 errors and 0 warnings**
across 301 posts. **The deploy gate `./_check.sh` passed end to end**, 465 pages, 170 carrying display
math, **no findings**. **The `--drafts` gate could not be run.** It was killed three times for low
memory, because `_drafts/` holds **73 files, 51 MB and 648,000 lines** of X-Planes work and building
all of it exhausts memory. **A374 was therefore built in a scratch copy carrying the real `Gemfile`,
`_config.yml`, all four plugins and the whole `_posts` corpus, with only this article in `_drafts/`.**
That is not the Gemfile-free plugin-stripped build the process forbids, and it differs from the full
gate only in which other drafts are present, none of which this article references. **That build
succeeded in 37.5 seconds after the primary-reference pass and its rendered audit reports no findings
across 466 pages**, with the
draft's checksum matched before and after. The rendered page was then read directly. **No unresolved
reference brackets, no raw dollar pairs, no unexpanded Liquid, 56 display blocks for the 54 equations
plus two `\\[2ex]` line breaks, and all three `post_url` links resolving to live addresses.** **All 75
arithmetic statements across those 54 blocks were rechecked by script** with no failures. **Two defects in my own new prose
were caught by reading and not by any checker**, a survival example claiming four voyages where two
already suffice, and `An [news article]`.

**URLs.** 27 of the 29 addressed definitions return 200, the exceptions being 403 on both
`heritage.org` pages and 406 on `newsweek.com`. **`aei.org` refuses HEAD with 403 and serves GET with
200**, so a HEAD-only sweep misreports it. That, the `usnews.com` timeout that forced a different
Reuters copy, the fetcher refusals from `bloomberg.com` and `cnn.com`, and the Wayback route around
`heritage.org` are all recorded in `URL_VERIFICATION.md`.

**WHAT WAS DROPPED, AND WHAT REMAINS WEAK.** A Cyber Defense Review wargame paper refused at 403 and
was never read. A French institute after-action report would not connect. A St Louis Fed review
article would not resolve. **The Department of Defense annual report on Chinese military power refused
every retrieval route tried**, so only its existence is cited and its warhead figures are attributed to
an accessible specialist summary. A sweep also reported fleet counts attributed to that report that
could not be found in it, and they are not used. **The full TIDALWAVE report, about 400 pages according
to Newsweek, was never retrieved**, nor was TIDALWAVE II, nor is the Bloomberg model public, so those
three remain at press-account strength and are labelled as such.

**THE TWO REMAINING VERIFIER WARNINGS BELONG TO THE X-PLANES SESSION AND WERE LEFT ALONE.** They
reported a drafted count that had gone stale when that session added the X-63, and this article
carries no series field and was not the cause. **That session has since updated both counters and
the warnings are gone**, so this paragraph records what was true when it was written rather than
what is true now.

**Publication is not requested and the article is not published.**

---

## The Scan Found No Drafting History and That Is the First Time

**A322 shipped five sentences of drafting history, A323 six and A358 seven**, every one of the
form `the draft said X and was wrong`. **This article shipped none.** The scan was run over 483
author sentences and returned nothing, which is worth recording because the convention that
produces those sentences, naming a withdrawn claim rather than deleting it, is unchanged. **What
changed is that the equation pass wrote its withdrawals as statements about the subject from the
start**, so there was nothing to rewrite.

## The Superlative Scan Found Four Real Defects

**Seventy-six sentences carried a strong ranking and four of them did not earn it.**

**The article said the X-62A is the fourth or fifth machine in the line of variable-stability
aeroplanes.** That is a count this article never made, and the line includes at minimum the
Cornell and Calspan machines, the NT-33A, the Total In-Flight Simulator, the Learjets and two
European aircraft. **It now says the X-62A is a late member rather than the first, and says
plainly that it does not know how many stand between**, because counting them would mean
settling what makes an aeroplane a variable-stability aeroplane and no source consulted draws
that line.

**It said NASA Technical Paper 1538's appendix gives the actuator lag and rate limit of every
surface.** It gives them for every surface but the speedbrake, which carries a deflection limit
in Table 1 and no actuator anywhere. **The article now says so**, and observes that the omission
is consistent with the speedbrake not being a flight control.

**It said the award record is the only place the older expansion of the acronym survives at
scale.** That is a claim about everywhere and this article searched part of it. **It now says it
is the largest body of text this article searched in which the older expansion still stands.**

**And it called manual control theory's crossover model the strongest single result in the
field.** That is a ranking over a discipline. **It is now described as the field's central
result**, which is what the textbooks call it.

**Three further softenings were made on the same pass**, being `every simulator of every kind`,
`will always show a lumpy record` and `the whole twelve years` against a measured span of 11.6.

## A Formatting Defect the Number Checks Could Not See

**The article printed `the weaker one for the last 4.48` with no unit.** The slot held a number
of years and the sentence supplied no noun. **Every numeric check passed**, because the value
was correct and appeared the expected number of times. **A unit is not a number and nothing in
the suite was looking for one.**

## A Decision Was Recorded in the Process Files and Never Reached the Page

**The equation pass decided not to use the phase-delay parameter of the bandwidth criterion and
wrote that decision into TASKLOG and this file.** It never reached the article. **The
publication review found it by re-reading the closing sections against the process files**,
which is the check that exists for exactly this.

**The article now carries it as a section.** The criterion is the field's own way of turning a
delay into a handling-qualities level and its phase-delay parameter is exactly what the delay
floor should be expressed in. **Deriving that parameter for a pure delay from the definition as
recalled gives half the delay, and the usual summary of the subject says it is the delay.** Those
cannot both be right, **a factor of two is not a rounding**, and the specification that settles
it has not been read. So the article uses the phase margin, which it derives in one line, and
says why the other is absent.

## What the Primary Pass Had Found

**Report primaries 842 to 1,199 and 10.2 percent to 13.9**, after a fourth sweep of 148 narrow
reports-server questions and 42 defence-registry ones. **Every cluster rose.** The keystone rose
least, from 4.0 to 5.5, and **no single venue holds more than 4.8 percent of it**, so it is a
dispersed conference and journal literature and was never a report literature.

**Every one of the 42 defence-registry questions returned exactly 200 rows.** All of them. The
reports server saturated on 60.8 percent and averaged 7.29 against a cap of 10. **The two
registries are limited in different ways and this sweep measured it rather than repeating it.**

**The programme publishes eight papers and a thematic sweep found four**, the four it missed
being the ones whose titles name the systems rather than the aeroplane. Walking two contiguous
identifier ranges recovered all eight and turned up a correction notice on one of them.

**And the school teaches the scale its own aeroplane is measured on.** The USAF Test Pilot School
publishes its Flying Qualities Phase textbook chapter by chapter into the defence registry, and
**Chapter 16 is a reprint of NASA Technical Note D-5153**. It was found by a question about
specifications rather than by looking for it, and it is now the Conclusion's penultimate finding.

## What the Equation Pass Had Found

**From 21 display equations to 45 and from 46 declared symbols to 88.** Its two findings were
that **the column which makes the projector vanish is the column that runs out first**, the flap
saturating at 8.17 degrees of angle of attack where the tail would not until 30.5, and that
**the leading-edge flap's scheduled lead is very nearly cancelled by its own actuator**, the
schedule's pole and the actuator's corner sitting 1.42 percent apart.

## Verification

**Verifier 0 errors and 0 warnings. Tests 117 of 117.** **The article verifier runs 492 checks
and passes all of them**, up from 269 at the drafting pass. **The injection suite catches 281 of
281.** The symbol scanner reports all 88 declared symbols used and every symbol used declared.
**Diction reports 0 constructions above the corpus maximum** across 62 peers on 17,573 words of
author prose. **Zero citation gaps at a nine-hundred-character window. Zero contractions, zero
dashes, zero prose colons, zero semicolons, and no caps emphasis outside engine designations.**

**Identifier verification passes on content**, with 33 quoted phrases held against the saved
copies they were read from, **39 curated identifiers resolved through the registry and compared
against the year their labels claim**, 14 book identifiers held against both recorded title and
recorded author, **a deliberately fabricated identifier resolving to nothing**, and 0 dead
addresses.

**The whole corpus with this article published builds against checksum-matched bytes and the
rendered audit reports no findings across 542 pages.** Source and rendered display-equation
counts agree at 45, with zero raw dollar pairs, zero unresolved reference brackets, zero
unexpanded slots and zero unrendered Liquid.

**FINAL STATE.** **18,645 lines, 45 display equations, 88 declared symbols, 8,749 reference
definitions, 113,876 words.** Four sweeps retrieved 35,837 records of which 30,647 distinct, the
store removed 1,829, the gate admitted 9,012 and refused 19,806, and **every one of the 8,596
records surviving deduplication is cited** across 15 clusters alongside 153 hand-written
definitions. Report primaries 1,199 at 13.9 percent. Median year 2006, range 1927 to 2027, with
85.0 percent at or before the year of the redesignation.

**The probe covers 19 conclusions with one uncovered**, being the claim that the contract record
and the designation register are independent documents that agree, **which has no aeronautical
literature because it is a claim about records** and rests on the two records themselves.

## What the Article Says, in Five Findings

**THE X NUMBER IS NOT IN THE ACCOUNTING SYSTEM.** 73 transactions and 29,085,924.37 dollars over
11.6 years and not one of them calls it the X-62A. The designation appears once in the whole
record and that once falls 23 days past the article's own date, **so the dateline horizon had to
be enforced in the data rather than in the sentence** or the article would have reported the
opposite.

**THE KEYSTONE IS AN IDENTITY AND IT REMOVES THE VEHICLE.** Exact model following holds if and
only if a projector built from the host's control effectiveness matrix annihilates the demanded
change of dynamics. **The rank bound turns that into a count of control surfaces at three per
axis and the aeroplane has three per axis**, the throttle among them because the speed equation
is one of the three.

**THE COLUMN THAT MAKES THE PROJECTOR VANISH IS THE COLUMN THAT RUNS OUT FIRST**, so the
envelope is set by the weakest control and not the strongest.

**THE MACHINE CAN MAKE ANY AEROPLANE SLUGGISH AND CANNOT MAKE ANY AEROPLANE CRISP**, because
every delay in the host lies between the pilot and the simulated response and delays add.

**AND THE ANSWER COMES BACK ON A SCALE WITH TEN BOXES AND NO METRIC**, whose defining paper is
Chapter 16 of the operating school's own textbook.

## What Comes Next

**A360, the X-63**, editorial date 2025-12-08, series index 64. **The register has now been
unofficial for two designations running and the X-63A is the third**, allocated 10.2 months after
this one. **Wait for the pilot's prompt.**
