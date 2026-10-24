#!/usr/bin/env python3
"""The literature-survey pipeline, driven by one TOML file per article.

WHY. A370 to A372 each carried `harvest.py`, `select.py`, `gen_master.py` and
`assemble.py`, and two hundred and twenty-six `harvest.py` files exist under
`tmp/`. Between A371 and A372, `gen_master.py` differed only in its paths and
in a statistics file A372 added, and the harvest and select scripts differed
mainly in their queries and patterns. Every fix landed in one copy. A372's
anchor-reservation fix, its order-free qualifiers and its pool-size pass were
each learned by an article that then had to be copied forward by hand.

THE CONFIGURATION IS THE ARTICLE'S PART. Queries, anchor patterns and cluster
definitions are the article's own argument, so they stay with the article in
`tmp/<article>/survey.toml`. Everything else is here. TOML literal strings,
`'...'`, take no escapes, so a pattern is written exactly as the regular
expression it is, with no doubled backslashes.

  python3 _lib/harvest.py harvest  CONFIG    registry rounds into pool files
  python3 _lib/harvest.py select   CONFIG    store filter, junk filter, gate, audit, clusters
  python3 _lib/harvest.py master   CONFIG    deduplicate, subtract hand citations, anchor
  python3 _lib/harvest.py assemble CONFIG    expand markers into the draft

THE CONFIGURATION, every key shown. Paths are relative to the repository root.

  article = "A372"
  workdir = "tmp/a372"
  era_cutoff = 2014                  # period is up to and including this year

  [harvest]
  rows = 100
  queries = ['...']                  # or queries_file = "queries.txt", one per line
  [[harvest.round]]
  label = "JP"
  pool = "cr_J_period"               # workdir/<pool>.json
  src = "journal"                    # recorded on each selected record
  filter = "type:journal-article,until-pub-date:2014-12-31"

  [select]
  strong = ['\\bunboxed\\b', 'layout(?=.*(?:struct|record))']
  audit_seeds = [20260809, 19951231, 20170601]
  audit_n = 30
  output = "select1.json"
  [[select.cluster]]
  name = "representation_and_boxing"
  patterns = ['\\bunbox']

  [master]
  hand = "hand_research.json"        # {anchor: {text, url}} of the hand citations
  output = "master.json"
  stats = "stats.json"

  [assemble]
  body = "body.md"
  draft = "_drafts/x.markdown"
  published = "_posts/2026-08-09-x.markdown"   # refuses to run once this exists

MARKERS in the body, expanded by `assemble`.

  {{L:cluster:N}} {{M:cluster:N}}    N period or modern entries, 0 for all that remain
  {{COUNT:L:cluster}} {{COUNT:M:cluster}}   pool sizes before any picking
  {{COUNT_ADJACENT}}                 the `other` cluster, both eras
  {{PERIOD_TOTAL}} {{MODERN_TOTAL}} {{HAND_COUNT}} {{HARVEST_COUNT}} {{TOTAL}}
  {{RAW}} {{KEPT}} {{DISCARDED}} {{QUERY_COUNT}} {{DEDUP}} {{TITLE_DROP}} {{HAND_DUP}}
  {{RESEARCH}}                       the merged research list and its definitions

Every figure is computed from the files on disk, never transcribed, because a
transcribed count goes stale the moment the harvest is re-run.
"""

import argparse
import collections
import json
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "_research"))


class ConfigError(ValueError):
    pass


TOP_KEYS = {"article", "workdir", "era_cutoff", "harvest", "select", "master", "assemble"}
SECTION_KEYS = {
    "harvest": {"rows", "queries", "queries_file", "round"},
    "select": {"strong", "audit_seeds", "audit_n", "output", "cluster", "order_free", "hyphen_tolerant"},
    "master": {"hand", "output", "stats"},
    "assemble": {"body", "draft", "published"},
}


def load_config(path):
    """The configuration, validated, with paths resolved against the repository root."""
    import tomllib
    with open(path, "rb") as fh:
        cfg = tomllib.load(fh)
    extra = set(cfg) - TOP_KEYS
    if extra:
        raise ConfigError(f"{path}: unknown keys {sorted(extra)}")
    for k in ("article", "workdir"):
        if not isinstance(cfg.get(k), str) or not cfg[k]:
            raise ConfigError(f"{path}: {k} is required")
    if not isinstance(cfg.get("era_cutoff"), int):
        raise ConfigError(f"{path}: era_cutoff must be a year")
    for sec, keys in SECTION_KEYS.items():
        extra = set(cfg.get(sec, {})) - keys
        if extra:
            raise ConfigError(f"{path}: [{sec}] unknown keys {sorted(extra)}")
    cfg["workdir"] = os.path.join(ROOT, cfg["workdir"])
    h = cfg.get("harvest", {})
    if "queries_file" in h:
        with open(os.path.join(ROOT, h["queries_file"]), encoding="utf-8") as fh:
            h["queries"] = [q.split("#", 1)[0].strip() for q in fh if q.split("#", 1)[0].strip()]
    for r in h.get("round", []):
        if set(r) != {"label", "pool", "src", "filter"}:
            raise ConfigError(f"{path}: each [[harvest.round]] needs exactly label, pool, src, filter")
    for c in cfg.get("select", {}).get("cluster", []):
        if set(c) != {"name", "patterns"} or c["name"] == "other":
            raise ConfigError(f"{path}: each [[select.cluster]] needs name and patterns, "
                              "and `other` is reserved for the unclustered")
    for p in cfg.get("select", {}).get("strong", []) + [
            p for c in cfg.get("select", {}).get("cluster", []) for p in c["patterns"]]:
        try:
            re.compile(p)
        except re.error as e:
            raise ConfigError(f"{path}: bad pattern {p!r}: {e}") from e
    return cfg


def _need(cfg, sec, *keys):
    s = cfg.get(sec)
    if not s or any(k not in s for k in keys):
        raise ConfigError(f"[{sec}] needs {', '.join(keys)}")
    return s


def _work(cfg, name):
    return os.path.join(cfg["workdir"], name)


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _dump(obj, path):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1)


# ---------------------------------------------------------------- harvest

def harvest(cfg):
    """Run every query in every round, adding new DOIs to each round's pool file.

    A pool file is a JSON object keyed by DOI, so re-running adds rather than
    duplicates. A query that fails is reported and counted, and the command
    exits 1, because a silently skipped query is a smaller literature.
    """
    import fetch
    h = _need(cfg, "harvest", "queries", "round")
    rows = h.get("rows", 100)
    os.makedirs(cfg["workdir"], exist_ok=True)
    failed = 0
    for rnd in h["round"]:
        path = _work(cfg, rnd["pool"] + ".json")
        out = _load(path) if os.path.exists(path) else {}
        start = len(out)
        for q in h["queries"]:
            items = fetch.get_json(f"{fetch.CROSSREF}?" + urllib.parse.urlencode(
                {"query.bibliographic": q, "rows": str(rows), "filter": rnd["filter"]}))
            if items is None:
                print(f"{rnd['label']} FAILED {q!r}", flush=True)
                failed += 1
                continue
            items = (items.get("message") or {}).get("items") or []
            new = 0
            for it in items:
                doi = (it.get("DOI") or "").strip().lower().rstrip(".")
                if not doi or doi in out:
                    continue
                title, authors, year, venue = fetch.crossref_fields(it)
                if not title:
                    continue
                out[doi] = {"doi": doi, "title": title.strip(), "authors": authors,
                            "year": year, "venue": venue, "query": q}
                new += 1
            print(f"{rnd['label']} {len(items):3d} hits, {new:3d} new, total {len(out):5d}  {q}", flush=True)
        _dump(out, path)
        print(f"\n{rnd['label']} {start} -> {len(out)}, {len(out) - start} added\n", flush=True)
    return 1 if failed else 0


# ---------------------------------------------------------------- select

# A SUPERSET OF `gate.normalise`, kept separate so no existing gate changes
# meaning. A hyphen written as U+2010 refused a directly relevant record once,
# and a soft hyphen or a no-break space defeats a literal anchor the same way.
_TYPO = {"\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-", "\u2014": "-", "\u2015": "-",
         "\u2212": "-", "\u00ad": "", "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"',
         "\u00a0": " ", "\u2009": " ", "\u202f": " "}


def normalise(s):
    out = s or ""
    for a, b in _TYPO.items():
        out = out.replace(a, b)
    return out


def hyphen_tolerant(pat):
    """A literal space also matches a hyphen or a slash. Strictly widening."""
    return pat.replace(" ", "[ \\-/]")


_QUALIFIED = re.compile(r"^(.*?)\(\?=\.\*(.*)\)$", re.S)


def order_free(pat):
    """`X(?=.*Q)` becomes `^(?=.*X)(?=.*Q)`, so the qualifier may precede the anchor.

    Written as a trailing lookahead, a qualifier must FOLLOW its anchor, and A371
    lost 303 records to titles that named the qualifier first. The loss is
    silent, because a missed match returns a smaller corpus rather than an error.
    """
    m = _QUALIFIED.match(pat)
    return pat if not m else f"^(?=.*{m.group(1)})(?=.*{m.group(2)})"


# PROCEEDINGS FURNITURE IS ON-SUBJECT BY EVERY ANCHOR AND IS NOT A WORK.
JUNK = re.compile(r"^\s*(?:session details|front matter|back matter|"
                  r"table of contents|contents|index|editorial|erratum|"
                  r"corrigendum|author index|subject index|"
                  r"list of (?:reviewers|contributors)|proceedings of|preface|"
                  r"foreword|acknowledge?ments)\b", re.I)


def compile_clusters(clusters):
    return [(c["name"], re.compile("|".join(f"(?:{p})" for p in c["patterns"]), re.I)) for c in clusters]


def cluster_of(compiled, title, venue=""):
    """The first cluster whose patterns match title and venue, else `other`."""
    text = normalise(f"{title} {venue}")
    for name, pat in compiled:
        if pat.search(text):
            return name
    return "other"


def era(year, cutoff):
    return "undated" if not year else ("period" if int(year) <= cutoff else "modern")


def select(cfg):
    """Filter the pools to the article's subject and assign clusters."""
    import gate as gatelib
    import homonyms
    import refs
    s = _need(cfg, "select", "strong", "cluster")
    recs = []
    for rnd in _need(cfg, "harvest", "round")["round"]:
        path = _work(cfg, rnd["pool"] + ".json")
        if not os.path.exists(path):
            print(f"WARNING pool {rnd['pool']} absent, the survey is incomplete")
            continue
        for doi, v in _load(path).items():
            recs.append({"src": rnd["src"], "doi": doi, "title": v["title"],
                         "authors": v.get("authors") or [], "year": v.get("year"),
                         "venue": v.get("venue") or "", "url": f"https://doi.org/{doi}"})
    print(f"harvested {len(recs)} records")
    # A DOI in two pools keeps the later pool's record, in round order.
    kept_h, dropped_h = homonyms.filter_records({r["doi"]: r for r in recs})
    print(f"accumulated rejection store and noise patterns removed {len(dropped_h)}")
    recs = list(kept_h.values())
    n = len(recs)
    recs = [r for r in recs if not JUNK.match(refs.clean(r.get("title", "")))]
    print(f"junk-title filter removed {n - len(recs)} proceedings-furniture records")
    pats = s["strong"]
    if s.get("hyphen_tolerant", True):
        pats = [hyphen_tolerant(p) for p in pats]
    if s.get("order_free", True):
        pats = [order_free(p) for p in pats]
    g = gatelib.Gate(pats, name=cfg["article"])
    kept, dropped = gatelib.select(recs, g, key=lambda r: normalise(r.get("title", "")))
    print(f"anchor gate kept {len(kept)} and dropped {len(dropped)}")
    # ONE CLEAN SAMPLE IS ONE SAMPLE. Independent seeds, because one draw of thirty
    # from thousands misses a family occupying one percent more often than not.
    for seed in s.get("audit_seeds", [20260809, 19951231, 20170601]):
        gatelib.audit(kept, dropped, seed=seed, n=s.get("audit_n", 30))
    compiled = compile_clusters(s["cluster"])
    counts = collections.Counter()
    for r in kept:
        r["cluster"] = cluster_of(compiled, r["title"], r.get("venue", ""))
        counts[r["cluster"]] += 1
    print("\n-- CLUSTER COUNTS --")
    for name, _ in compiled + [("other", None)]:
        print(f"   {name:28s} {counts.get(name, 0):5d}")
    eras = collections.Counter(era(r.get("year"), cfg["era_cutoff"]) for r in kept)
    print(f"\n-- ERA at the {cfg['era_cutoff']} cutoff --  period {eras['period']}  "
          f"modern {eras['modern']}  undated {eras['undated']}")
    _dump(kept, _work(cfg, s.get("output", "select1.json")))
    print(f"\nwrote {len(kept)} selected records")
    return 0


# ---------------------------------------------------------------- master

# THE CORPUS CHECKER'S CONTRACTIONS AND MORE, so a record that survives here also
# passes `_verify.py`. A partial list means a record survives selection and then
# fails the corpus check.
BANNED = re.compile(
    r"\b(?:can't|won't|don't|doesn't|didn't|isn't|aren't|wasn't|weren't|"
    r"haven't|hasn't|hadn't|shouldn't|wouldn't|couldn't|it's|that's|there's|"
    r"here's|what's|let's|we're|they're|you're|I'm|we've|they've|you've|I've|"
    r"we'll|they'll|you'll|I'll|he's|she's|who's|ain't|shan't)\b", re.I)
# A DOUBLED WORD IN A TITLE IS USUALLY A REGISTRY CONCATENATION. The lookahead
# excludes a hyphen, because `Based on On-Orbit` is not a repeat.
DOUBLED = re.compile(r"\b(\w+)\s+\1(?![-\w])", re.I)


def master(cfg):
    """Deduplicate, drop titles the corpus checker would refuse, subtract hand citations, anchor.

    THE HAND SET IS READ FROM ITS OWN FILE, NOT FROM THE DRAFT. The draft is
    this pipeline's output, so once assembled it carries every harvested
    reference too, and reading it once treated the whole harvest as cited and
    emitted a master set of one record.

    THE HAND ANCHORS ARE RESERVED. `assign_anchors` builds a stem from first
    author and year, so without the reservation a harvested record can take a
    hand-cited anchor and the prose citation resolves to the wrong paper. That
    happened to two A372 citations before it was fixed.
    """
    import refs
    m = _need(cfg, "master", "hand")
    sel = _load(_work(cfg, cfg.get("select", {}).get("output", "select1.json")))
    hand = _load(_work(cfg, m["hand"]))
    hand_urls = {(v["url"] or "").strip().lower().rstrip(".") for v in hand.values()}
    hand_titles = {refs.fold(v["text"])[:70] for v in hand.values()}
    print(f"hand-selected: {len(hand_urls)} identifiers, {len(hand_titles)} titles")
    records = []
    for r in sel:
        doi = (r.get("doi") or "").strip().lower().rstrip(".")
        records.append({"authors": r.get("authors") or [], "year": str(r.get("year") or ""),
                        "title": r.get("title") or "",
                        "url": f"https://doi.org/{doi}" if doi else (r.get("url") or ""),
                        "doi": doi, "venue": r.get("venue") or "", "cluster": r["cluster"],
                        "pool": r.get("src") or "crossref", "kind": "research"})
    stats = {}
    before = len(records)
    records, dups = refs.dedupe(records)
    stats["dedup"] = len(dups)
    print(f"records {before} -> {len(records)} after title-and-year deduplication ({len(dups)} dropped)")
    for key, rx, what in (("contraction", BANNED, "a contraction"), ("doubled", DOUBLED, "a doubled word")):
        n = len(records)
        records = [r for r in records if not rx.search(refs.clean(r["title"]))]
        stats[key] = n - len(records)
        print(f"dropped {n - len(records)} whose verbatim title carries {what}")
    n = len(records)
    records = [r for r in records if r["title"].strip() and r["year"]]
    print(f"dropped {n - len(records)} untitled or undated")
    n = len(records)
    records = [r for r in records if r["url"].lower().rstrip(".") not in hand_urls
               and refs.fold(r["title"])[:70] not in hand_titles]
    stats["hand_dup"] = n - len(records)
    print(f"dropped {n - len(records)} already cited by hand")
    out = refs.assign_anchors(records, taken=tuple(sorted(hand)), kind="research")
    _dump(out, _work(cfg, m.get("output", "master.json")))
    _dump(stats, _work(cfg, m.get("stats", "stats.json")))
    print(f"\nmaster: {len(out)} anchored records")
    for cl, k in collections.Counter(r["cluster"] for r in out.values()).most_common():
        print(f"  {k:5d}  {cl}")
    return 0


# ---------------------------------------------------------------- assemble

MARKER = re.compile(r"\{\{([LM]):([a-z_]+):(\d+)\}\}")


def surname(a):
    """A registry family-name field is not reliably a family name.

    Some deposits store `Pike, Lee`, so the part before the comma is taken, and
    one stores the literal entity `&NA;` where an author should be.
    """
    a = re.sub(r"<[^>]+>", " ", a or "").split(",")[0]
    a = re.sub(r"\s+", " ", a).strip()
    return "" if a in ("&NA;", "&NA", "NA") else a


def entry_text(rec):
    """Visible link text, surname and year leading.

    Markup and line breaks are removed before use, because a list entry must be
    one line, and square brackets become parentheses, because a bracket in a
    title would close the link text early.
    """
    import refs
    authors = [x for x in (surname(a) for a in (rec.get("authors") or [])) if x]
    who = ("" if not authors else authors[0] if len(authors) == 1
           else f"{authors[0]} and {authors[1]}" if len(authors) == 2 else f"{authors[0]} and others")
    title = re.sub(r"<[^>]+>", " ", rec.get("title") or "")
    title = re.sub(r"\s+", " ", refs.clean(title)).strip().rstrip(" .")
    title = title.replace("[", "(").replace("]", ")")
    lead = ", ".join(p for p in (who, rec.get("year") or "") if p)
    return f"{lead}, {title}" if lead else title


def assemble_text(cfg, body):
    """The draft text with every marker expanded. Raises ConfigError on any leftover."""
    m = _need(cfg, "master", "hand")
    mast = _load(_work(cfg, m.get("output", "master.json")))
    hand = _load(_work(cfg, m["hand"]))
    cutoff = cfg["era_cutoff"]
    period, modern = {}, {}
    for anchor, rec in mast.items():
        y = rec.get("year") or ""
        bucket = modern if (y.isdigit() and int(y) > cutoff) else period
        bucket.setdefault(rec["cluster"], []).append((anchor, rec))
    for bucket in (period, modern):
        for recs in bucket.values():
            recs.sort(key=lambda ar: (-int(ar[1]["year"] or 0), ar[1]["title"].lower()))
    used, counts = {}, {}

    def pick(kind, cluster, count):
        pool = (period if kind == "L" else modern).setdefault(cluster, [])
        n = len(pool) if count == 0 else count
        if len(pool) < n:
            raise ConfigError(f"marker {kind}:{cluster}:{count} wants {n}, pool holds {len(pool)}")
        picked, pool[:] = pool[:n], pool[n:]
        for anchor, rec in picked:
            used[anchor] = (entry_text(rec), rec["url"])
        counts[f"{kind}:{cluster}"] = counts.get(f"{kind}:{cluster}", 0) + len(picked)
        return "\n".join(f"- [{entry_text(r)}][{a}]" for a, r in picked)

    # POOL SIZES FIRST. A count-0 marker drains its cluster, so a size reported
    # after picking would read as zero, a silent loss rather than an error.
    body = re.sub(r"\{\{COUNT:([LM]):([a-z_]+)\}\}",
                  lambda x: f"{len((period if x.group(1) == 'L' else modern).get(x.group(2), [])):,}", body)
    raw = sum(len(_load(_work(cfg, r["pool"] + ".json"))) for r in cfg["harvest"]["round"]
              if os.path.exists(_work(cfg, r["pool"] + ".json")))
    kept = len(_load(_work(cfg, cfg.get("select", {}).get("output", "select1.json"))))
    st = _load(_work(cfg, m.get("stats", "stats.json")))
    figures = {
        "COUNT_ADJACENT": len(modern.get("other", [])) + len(period.get("other", [])),
        "PERIOD_TOTAL": sum(len(v) for v in period.values()),
        "MODERN_TOTAL": sum(len(v) for v in modern.values()),
        "HAND_COUNT": len(hand), "HARVEST_COUNT": len(mast), "TOTAL": len(mast) + len(hand),
        "RAW": raw, "KEPT": kept, "DISCARDED": raw - kept,
        "QUERY_COUNT": len(cfg["harvest"]["queries"]),
        "DEDUP": st["dedup"], "TITLE_DROP": st["contraction"] + st["doubled"], "HAND_DUP": st["hand_dup"],
    }
    for k, v in figures.items():
        if k != "QUERY_COUNT":
            body = body.replace("{{" + k + "}}", f"{v:,}")
        else:
            body = body.replace("{{" + k + "}}", f"{v}")
    for x in [x for x in MARKER.finditer(body) if int(x.group(3)) != 0]:
        body = body.replace(x.group(0), pick(x.group(1), x.group(2), int(x.group(3))), 1)
    while True:  # bounded: each pass removes one marker and none is ever added
        x = MARKER.search(body)
        if not x:
            break
        body = body.replace(x.group(0), pick(x.group(1), x.group(2), 0), 1)
    merged = {a: (v["text"], v["url"]) for a, v in hand.items()}
    clash = sorted(set(merged) & set(used))
    if clash:
        raise ConfigError(f"harvested anchors collide with hand anchors: {clash}")
    merged.update(used)
    order = sorted(merged)
    if "{{RESEARCH}}" not in body:
        raise ConfigError("the body carries no {{RESEARCH}} placeholder")
    body = body.replace("{{RESEARCH}}", "\n".join(f"- [{merged[a][0]}][{a}]" for a in order) + "\n\n"
                        + "\n".join(f"[{a}]: {merged[a][1]}" for a in order))
    left = [x for x in re.findall(r"\{\{[^}]+\}\}", body.replace("{% post_url", "@@"))
            if not x.startswith("{{site")]
    if left:
        raise ConfigError(f"unexpanded markers survive: {sorted(set(left))[:8]}")
    return body, used, counts, period, modern


def assemble(cfg, out_path=None):
    """Write the assembled draft. Refuses once the article is published.

    A PUBLISHED ARTICLE MAKES THIS A HAZARD. It writes to the draft path, so a
    rerun would recreate a draft duplicating the published post and collide on
    date and URL. It refuses rather than warns, because a warning printed above
    a successful run is not read.
    """
    a = _need(cfg, "assemble", "body", "draft")
    if a.get("published") and os.path.exists(os.path.join(ROOT, a["published"])) and not out_path:
        raise ConfigError(f"REFUSING TO RUN. {cfg['article']} is published at {a['published']}. "
                          "Edit the published post directly.")
    body = open(_work(cfg, a["body"]), encoding="utf-8").read()
    text, used, counts, period, modern = assemble_text(cfg, body)
    with open(out_path or os.path.join(ROOT, a["draft"]), "w", encoding="utf-8") as fh:
        fh.write(text)
    left = {f"{e}:{k}": len(v) for e, b in (("L", period), ("M", modern)) for k, v in b.items() if v}
    print(f"harvested {len(used)}, unused pool remaining {sum(left.values())} {left or ''}")
    for k in sorted(counts):
        print(f"  {counts[k]:5d}  {k}")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(prog="harvest.py", description=__doc__.split("\n")[0])
    ap.add_argument("command", choices=["harvest", "select", "master", "assemble"])
    ap.add_argument("config")
    ap.add_argument("--out", help="assemble only: write here instead of the draft, even if published")
    a = ap.parse_args(argv[1:])
    try:
        cfg = load_config(a.config)
        if a.command == "assemble":
            return assemble(cfg, a.out)
        return {"harvest": harvest, "select": select, "master": master}[a.command](cfg)
    except (ConfigError, OSError, KeyError) as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
