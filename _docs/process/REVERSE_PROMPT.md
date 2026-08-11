# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: Pathological word usage pass on A370, plus a corpus-wide scan. **Committed, not pushed.**
**Not published.** **No published article was edited.**

---

## The `specific` Problem Is A False Positive And I Can Show It

You named `specific` as the example. **It is the highest-rate word in the corpus at 15.07 per thousand, and
it is not a defect.**

The two worst articles are `rocket_propellant_chemistry_a_design_tradeoff_space` at 68 uses and
`rocket_propellant_chemistry_cryogenic_liquid_propellants` at 71. **Fifty-nine of the 68 and seventy of the
71 are the phrase "specific impulse."** Corpus-wide, 44 percent of all 1,006 uses are terms of art, being
specific impulse, specific excess power, specific energy, specific heat, specific fuel consumption, specific
strength and specific thrust. None of them can be paraphrased.

**A rate cannot tell a term of art from a tic, and only the neighbouring words separate them.** When
filler-only uses are isolated, the worst article in the corpus has **6 of them at 1.59 per thousand**. There
is no `specific` problem left to fix.

**The same false positive covers `key`.** It flags at 18.26 per thousand in the Solana article and 10.80 in
the SSH one, and it is public keys, private keys, key pairs and key files throughout.

---

## The Real Corpus-Wide Tic Is `rather`, And It Was In A370

**`rather` appears 3,803 times across the corpus and 99.7 percent of those are "rather than."** It sits at or
above the verifier's 5.0 per thousand limit in **22 articles**, more than every other tic-class word
combined.

A370 carried **54 uses at 5.41 per thousand, which is 4.2 times the corpus median**. Twenty-one decorative
uses were rewritten, leaving **32 at 3.27 per thousand**.

**The replacements were deliberately varied so that one tic did not simply become another.** They are spread
across "and not" at 17, "instead of" at 3, a comma contrast, and two places where the sentence was split
instead. The construction check confirms the result, with **`and not` at 1.74 against a peer maximum of 2.66
and `instead of` at 0.31 against 6.62**.

**Where the contrast is load-bearing the phrase was kept**, as in "a coverage loss rather than a correctness
loss" and "found by writing rather than by testing."

---

## A370 Is Otherwise Clean And The Remaining Outliers Are Its Subject

- **0 constructions above the corpus maximum** against 297 peers.
- **0 tics above the peer maximum** against 253 peers, across a 70-word enumerated tic class.
- **21 words sit above the peer maximum and 20 of them are subject vocabulary**, being suspension, chunk,
  callback, coroutine, discriminator, sentinel, terminating, yielded and convention. No peer wrote about
  coroutines, so a peer maximum of zero is not a standard. `harvested` is the twentieth and is new prose
  about the survey.
- `convention` sits at exactly 5.00 per thousand and does not trip the verifier.

---

## What I Found In The Corpus And Did Not Touch

**I edited no published article.** These are reported for your decision rather than acted on.

| Article | Word | Uses | Rate | Assessment |
|---|---|---|---|---|
| `spacex_history_generality_forcing` | `configuration` | 201 | 10.3 | **Likely genuine** |
| `spacex_history_decomposability` | `configuration` | 154 | 14.9 | **Likely genuine** |
| `spacex_history_value_capture` | `configuration` | 94 | 9.6 | **Likely genuine** |
| `spacex_history_governance` | `configuration` | 92 | 6.0 | **Likely genuine** |
| `hardware_description_languages_state_of_the_practice` | `substantial` | 29 | 10.5 | **Likely genuine** |
| four articles | `framework` | 16 to 21 | 5.2 to 7.3 | Unassessed |

**The `configuration` case does not look like a term of art.** Its collocations are "configuration the" 39,
"configuration that" 17, "configuration exhibits" 10, "configuration comprises" 9 and "configuration
constitutes" 8, which is **an abstract noun serving as a generic sentence subject** in article after
article. It also forms the compound "decomposability configuration" 25 times. That is the shape of a tic,
unlike "specific impulse."

`substantial` at 29 uses is a vague intensifier, with "substantial adoption" 7 times.

**These four SpaceX articles are live**, so fixing them is a rewrite of published work and is your call, not
mine. The two draft warnings, `factor` in `x_planes_martin_marietta_x24` and `configuration` in
`claude_code_getting_started_over_ssh`, are **both false positives**, being "load factor" and "a factor of"
in the first and "configuration file" in the second.

---

## Verification

- `python3 _verify.py` **0 errors, 21 warnings**, the unchanged baseline, from the repository root. **A370
  appears in no word-frequency warning.**
- **Isolated production build with drafts, exit 0**, with 0 unfilled markers, 0 unresolved references, 31
  matched display-math delimiter pairs and 0 empty list items.
- **Reflow verified content-preserving and a fixed point**, checked by comparing the token stream before and
  after rather than assumed.
- **Prose scan clean** of em dashes, en dashes, contractions, prose semicolons and italics. The single
  semicolon is the permitted `console.log` debug tag.
- `lint.scan` **clean**.

---

## Next

Your call. **A370 has had all four passes plus this one**, is committed, **is not pushed**, and is **not
published**. I did not push because only the publication-review prompt authorises that.

The open question is whether you want the `configuration` and `substantial` findings acted on in the
published SpaceX and hardware-description-language articles.

The X-Planes series is unchanged at **thirty-seven of seventy-two**, none published, with **A334, the Boeing
X-37, next** whenever you want it.
