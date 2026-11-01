#!/usr/bin/env python3
"""Whether `_docs/process/HANDOFF.md` is valid for the repository it sits in.

    python3 _lib/blog.py handoff               # the startup check, parent against HEAD~1
    python3 _lib/blog.py handoff --uncommitted  # before the handoff's own commit, against HEAD

WHAT VALID MEANS. The handoff records the commit it describes as its Parent commit, and its
own commit sits directly on top, so after that commit `git rev-parse HEAD~1` must name the
parent. The Session Startup Protocol in `CLAUDE.md` asks every session to make that comparison
and to report a stale handoff rather than trust it. Seven articles, A359 to A365, each carried a
private `handoff_check.py` that made it, and this is the part they shared.

A CHECK RUN AT THE WRONG MOMENT CONFIRMS THE WRONG THING. Before the handoff is committed, the
state it describes is HEAD, and after it is HEAD~1. One of the scratch copies compared the stamp
to HEAD after the push and reported the handoff's own commit as a disagreement. The moment is
therefore a flag, defaulting to the startup case.

ONLY THE CURRENT BLOCK COUNTS. A refreshed handoff keeps earlier blocks headed `## Validity
(superseded, ...)`, each with its own parent. The block read here is the first heading that is
exactly `## Validity`.

WHAT IS NOT CHECKED, AND WHY. The scratch copies also checked article-specific claims such as a
drafted count, a list of named commits and a series index. Those are prose, change shape with
every refresh, and a checker that invents its own expectation fails on nothing, which A363's
copy did. `progress.py` already checks drafted counts in the channels that must be current. The
branch is reported but does not decide validity, because a worktree on its own branch is a
legitimate place to read a `master` handoff. Every other commit the block names is reported if
it does not exist in the repository, which is a typing error rather than staleness.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "_docs", "process", "HANDOFF.md")

_HEADING = re.compile(r"^## Validity[ \t]*$", re.M)
_NEXT = re.compile(r"^## ", re.M)
_PARENT = re.compile(r"\*\*Parent commit\*\*[^`\n]*`([0-9a-f]{7,40})`")
_BRANCH = re.compile(r"\*\*Branch\*\*[^`\n]*`([^`\n]+)`")
_HASH = re.compile(r"`([0-9a-f]{7,40})`")


class HandoffError(ValueError):
    """The handoff has no current Validity block or the block records no parent."""


def validity_block(text):
    """The text of the current `## Validity` section, without superseded ones."""
    m = _HEADING.search(text)
    if not m:
        raise HandoffError("no '## Validity' heading")
    rest = text[m.end():]
    end = _NEXT.search(rest)
    return rest[:end.start()] if end else rest


def parse(text):
    """{'parent', 'branch', 'commits'} from the current block. Branch may be None."""
    block = validity_block(text)
    parent = _PARENT.search(block)
    if not parent:
        raise HandoffError("the Validity block records no Parent commit")
    branch = _BRANCH.search(block)
    commits = []
    for h in _HASH.findall(block):
        if h not in commits:
            commits.append(h)
    return {"parent": parent.group(1), "branch": branch.group(1) if branch else None,
            "commits": commits}


def _git(*args):
    """Stripped stdout, or None when git fails."""
    r = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def git_resolve(rev):
    """The full commit a revision names, or None when it names no commit."""
    return _git("rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}")


def verdict(info, resolve, ref, branch):
    """(valid, lines) for parsed handoff `info`. `resolve` maps a revision to a full hash or None.

    Valid exactly when the recorded parent and `ref` resolve to the same commit. A parent that
    resolves to nothing is invalid, not an error, because a handoff copied from another clone
    names a commit this one never had.
    """
    want, got = resolve(info["parent"]), resolve(ref)
    lines = []
    if got is None:
        lines.append(f"INVALID  {ref} does not resolve, so there is no parent to compare")
        valid = False
    elif want is None:
        lines.append(f"INVALID  recorded parent {info['parent']} is not a commit in this repository")
        valid = False
    elif want != got:
        lines.append(f"INVALID  recorded parent {info['parent']} but {ref} is {got[:12]}, "
                     "so the handoff is stale and must not be trusted")
        valid = False
    else:
        lines.append(f"VALID    recorded parent {info['parent']} is {ref}")
        valid = True
    if info["branch"] and branch and info["branch"] != branch:
        lines.append(f"note     handoff names branch {info['branch']}, checkout is on {branch}")
    for h in info["commits"]:
        if h != info["parent"] and resolve(h) is None:
            lines.append(f"note     {h} named in the Validity block is not a commit here")
    return valid, lines


def main(argv):
    args = argv[1:]
    if any(a in ("-h", "--help") for a in args):
        print(__doc__)
        return 0
    unknown = [a for a in args if a not in ("--uncommitted",) and not a.startswith("--file=")]
    if unknown:
        print(f"unknown argument {unknown[0]}\nusage: blog.py handoff [--uncommitted] [--file=PATH]")
        return 2
    path = next((a.split("=", 1)[1] for a in args if a.startswith("--file=")), PATH)
    ref = "HEAD" if "--uncommitted" in args else "HEAD~1"
    try:
        with open(path, encoding="utf-8") as fh:
            info = parse(fh.read())
    except OSError as e:
        print(f"cannot read {path}: {e}")
        return 2
    except HandoffError as e:
        print(f"INVALID  {e}")
        return 1
    valid, lines = verdict(info, git_resolve, ref, _git("rev-parse", "--abbrev-ref", "HEAD"))
    for line in lines:
        print(line)
    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
