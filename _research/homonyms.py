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
    (r"\belectric vehicle\b|\bEV batter|\bplug-?in hybrid\b|\bautomotive batter",
     "A334: the ELECTRIC ROAD VEHICLE again, arriving this time through battery "
     "cycle life rather than through propulsion. Recorded in A331 as the largest "
     "body this series has had to exclude"),
]

_COMPILED = [(re.compile(p, re.I), why) for p, why in NOISE_PATTERNS]


def load():
    """The rejection store, keyed by digital object identifier, URL or anchor."""
    if not os.path.exists(STORE):
        return {}
    with open(STORE, encoding="utf-8") as fh:
        return json.load(fh)


def _keys_for(rec, key):
    """Every identity a record might already be stored under."""
    out = {key}
    doi = rec.get("doi") or ""
    if doi:
        out.add(doi)
        out.add("https://doi.org/" + doi.replace("https://doi.org/", ""))
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
