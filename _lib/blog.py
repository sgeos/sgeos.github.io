#!/usr/bin/env python3
"""One command line for the whole library.

    python3 _lib/blog.py                      # list every command
    python3 _lib/blog.py COMMAND [ARGS...]    # run one; COMMAND --help for its options

WHY ONE ENTRY POINT. The library was bypassed by one-shot scripts because using
a module took an import and a script while retyping its loop took neither. A
command line for every module removes the reason, and one place that lists them
removes the search. Modules that carry their own command line are dispatched to
it unchanged, so `python3 _lib/edits.py ...` and `python3 _lib/blog.py edits ...`
are the same command. The small commands defined here wrap modules that are
otherwise only imported.
"""

import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Modules with their own `main(argv)` or `_main(argv)`, and what they do.
DISPATCH = {
    "edits": ("edits", "apply or check a TOML edit file against a post"),
    "registry": ("registry", "Crossref and OpenAlex search, abstracts, DOI metadata, work types"),
    "harvest": ("harvest", "the survey pipeline: harvest, select, master, assemble"),
    "sources": ("sources", "validate the source database, render, write or check References"),
    "import": ("sources_import", "fetch-crossref, pin-wiki and import a post into the source database"),
    "diction": ("diction", "word, phrase, opener, shape and creep checks against the corpus"),
    "numbers": ("numcheck", "recompute every number a claims file names, and prove each can fail"),
    "campaign": ("campaign", "status or run a corpus campaign file, dry run by default"),
    "text": ("textscan", "context search in saved sources, wikitext reference stripping"),
    "render": ("render", "audit a built site for defects a reader would see"),
    "resolve": ("resolve", "whether a post's cited identifiers resolve at all"),
}

LOCAL = {
    "lint": "invariant scan of one post, defects and conventions",
    "reflow": "rewrap a post's paragraphs, --write to save",
    "audit": "equation gaps, citation gaps, thin sections, primary fraction",
    "refs": "reference integrity of a post: unused, undefined and unlisted anchors",
    "post": "a post's structure: sections, equations, definitions",
    "booklinks": "check book links against the titles and authors they claim (network)",
}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def cmd_lint(args):
    import lint
    if len(args) != 1:
        print("usage: blog.py lint POST")
        return 2
    rows = lint.scan(_read(args[0]))
    for sev, check, detail in rows:
        print(f"  {sev:10s} {check:28s} {detail}")
    s = lint.summary(_read(args[0]))
    print(f"{s['defects']} defect(s), {s['conventions']} convention finding(s)")
    return 1 if s["defects"] else 0


def cmd_reflow(args):
    import reflow
    write = "--write" in args
    paths = [a for a in args if not a.startswith("--")]
    if len(paths) != 1:
        print("usage: blog.py reflow POST [--write]")
        return 2
    text = _read(paths[0])
    out = reflow.reflow_post(text)
    changed = sum(1 for a, b in zip(text.split("\n"), out.split("\n")) if a != b) + abs(
        len(text.split("\n")) - len(out.split("\n")))
    if write and out != text:
        with open(paths[0], "w", encoding="utf-8") as fh:
            fh.write(out)
    print(f"{'wrote' if write and out != text else 'would change'} about {changed} line(s) in {paths[0]}")
    return 0


def cmd_audit(args):
    import audit
    if not args:
        print("usage: blog.py audit POST [CUTOFF_YEAR]")
        return 2
    audit.report(args[0], int(args[1]) if len(args) > 1 else None)
    return 0


def cmd_refs(args):
    import refs
    if len(args) != 1:
        print("usage: blog.py refs POST")
        return 2
    problems = refs.integrity(_read(args[0]))
    print(json.dumps(problems, indent=1, default=list) if problems else "no reference integrity problems")
    return 1 if problems else 0


def cmd_post(args):
    import post
    if len(args) != 1:
        print("usage: blog.py post POST")
        return 2
    text = _read(args[0])
    for s in post.sections(text):
        print(f"  {s[0] if isinstance(s, tuple) else s}")
    print(f"{len(post.equations(text))} display equation(s), {len(post.definitions(text))} definition(s), "
          f"{len(post.used_anchors(text))} anchor(s) used")
    return 0


def cmd_booklinks(args):
    import booklinks
    if len(args) != 1:
        print("usage: blog.py booklinks POST")
        return 2
    rows = booklinks.check(_read(args[0]))
    for r in rows:
        print(f"  {r}")
    return 0


def usage():
    print(__doc__.strip().split("\n\n")[0] + "\n")
    print("Commands:")
    for name, (_mod, what) in sorted({**DISPATCH, **{k: (None, v) for k, v in LOCAL.items()}}.items()):
        print(f"  {name:10s} {what}")
    print("\nAlso at the repository root: _verify.py (the corpus gate), _verify_citations.py (citations),"
          " _check.sh (the deploy gate).")


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help", "help"):
        usage()
        return 0
    cmd, rest = argv[1], argv[2:]
    if cmd in DISPATCH:
        mod = importlib.import_module(DISPATCH[cmd][0])
        entry = getattr(mod, "main", None) or getattr(mod, "_main", None)
        if entry is not None:
            return entry([DISPATCH[cmd][0] + ".py"] + rest)
        # Modules whose command line lives under `if __name__ == "__main__"`.
        import runpy
        sys.argv = [DISPATCH[cmd][0] + ".py"] + rest
        try:
            runpy.run_path(os.path.join(HERE, DISPATCH[cmd][0] + ".py"), run_name="__main__")
        except SystemExit as e:
            return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
        return 0
    local = globals().get(f"cmd_{cmd}")
    if cmd in LOCAL and local:
        return local(rest)
    print(f"unknown command {cmd!r}\n")
    usage()
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
