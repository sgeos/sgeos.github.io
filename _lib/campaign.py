#!/usr/bin/env python3
"""Corpus campaigns: the strategy of the fix5, fix6, retrofit and cite passes, with the concrete logic supplied.

WHY. Between 7 and 22 October 2026 at least nine corpus-wide campaigns ran over
A297 to A368, the survey filter rebuild, the canonical sections, two survey
retrofits, an audit, the citation pass, the word pass, the pilot decision pass
and a cross-article sweep. Each re-implemented the same machinery in scratch,
selection, snapshots, rerun-safe application, gates before and after, a
progress ledger, resumption after an interrupted agent, and seeded sampling
for audit, and each relearned some of the same lessons. This module is that
machinery once. What a campaign actually does, its screen, its reading rule,
its edits and its gates, is supplied as functions in a campaign file.

A CAMPAIGN FILE is a Python module defining `CAMPAIGN`.

    from campaign import Campaign, Stage, Change
    def targets():               # which articles, by name and path
        return {"A384": "_posts/2026-08-20-mercury_as_colony_and_launch_site.markdown"}
    def fix_spelling(ctx):       # one stage: read files, return proposed changes
        text = ctx.read(ctx.path)
        return [Change(ctx.path, text.replace("color", "colour"))]
    def gate(ctx, proposed):     # problems with the proposed texts, empty if none
        return []
    CAMPAIGN = Campaign("spelling", targets, [Stage("fix", fix_spelling)], gates=[gate])

    python3 _lib/campaign.py status CAMPAIGN.py
    python3 _lib/campaign.py run CAMPAIGN.py [--apply] [--only A384] [--stage fix] [--redo]

THE RULES IT ENFORCES, each from a recorded defect.

  DRY RUN IS THE DEFAULT. `survey_tool.py resample` had no dry run and
  overwrote three sample files. Nothing is written without `--apply`.

  A STAGE PROPOSES, THE RUNNER WRITES. A stage returns the whole new text of
  each file it changes, and the runner writes all of them or none, after the
  gates pass on the proposed texts. A stage that wrote files itself could not
  be gated, and an agent killed mid-edit left half-applied drafts.

  SNAPSHOT BEFORE EVERY WRITE, NEVER RESTORE AUTOMATICALLY. Each file is copied
  to the campaign's state directory before it is changed. The copies are for
  reference and diff. Swapping a copy back into place reverted later work more
  than once, so recovery is a fixed-forward edit and this module has no restore.

  STAGES READ THE CURRENT FILE. Rebuilding from HEAD or from a frozen copy
  restored truncated labels in A307 and A308. `ctx.read` reads the working
  tree, and nothing here reads git.

  PROGRESS IS A LEDGER, SO AN INTERRUPTED RUN RESUMES. Usage limits killed
  agents mid-edit. Each completed stage is appended to `ledger.jsonl` with a
  hash of every file it wrote, and a rerun skips completed stages unless
  `--redo`. A stage whose files changed since it completed is reported, since
  someone edited after it.

  GATES RUN BEFORE AND AFTER. Before a stage, the gates run on the current
  files, so a failure that was already there is not blamed on the stage. After,
  they run on the proposed texts, and a NEW problem refuses the write.

  SAMPLES ARE SEEDED, DRAWN BEFORE READING AND RECORDED. A sample below the
  threshold understated contamination three times, so `escalate` compares the
  Wilson interval, not the point estimate, with the threshold.
"""

import argparse
import hashlib
import importlib.util
import json
import math
import os
import random
import re
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)


class CampaignError(RuntimeError):
    pass


class Change:
    """A proposed whole-file replacement. `path` is relative to the repository root."""

    def __init__(self, path, text):
        if not isinstance(path, str) or not isinstance(text, str):
            raise CampaignError("Change takes a path and the new text, both strings")
        self.path, self.text = path, text


class Stage:
    """A named step. `run(ctx)` returns a list of Change, possibly empty."""

    def __init__(self, name, run, note=""):
        if not re.fullmatch(r"[a-z][a-z0-9_-]*", name):
            raise CampaignError(f"stage name {name!r} must be lower-case letters, digits, - or _")
        self.name, self.run, self.note = name, run, note


class Context:
    """What a stage sees: the target's name and path, and read access to the tree."""

    def __init__(self, campaign, target, path, apply):
        self.campaign, self.target, self.path, self.apply = campaign, target, path, apply
        self.state = os.path.join(campaign.state_dir, target)

    def read(self, path):
        with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
            return fh.read()

    def scratch(self, name):
        """A path in this target's state directory, for a stage's own working files."""
        os.makedirs(self.state, exist_ok=True)
        return os.path.join(self.state, name)


def _hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


class Campaign:
    """Targets, ordered stages and gates. `state_dir` defaults to tmp/campaigns/<name>."""

    def __init__(self, name, targets, stages, gates=(), state_dir=None, protected=()):
        if not re.fullmatch(r"[a-z][a-z0-9_-]*", name):
            raise CampaignError(f"campaign name {name!r} must be lower-case letters, digits, - or _")
        names = [s.name for s in stages]
        if len(set(names)) != len(names) or not stages:
            raise CampaignError("stages must be non-empty with unique names")
        self.name, self.targets, self.stages, self.gates = name, targets, list(stages), list(gates)
        self.state_dir = state_dir or os.path.join(ROOT, "tmp", "campaigns", name)
        # Paths no stage may change, such as the shared rejection store, which
        # holds judgements relative to one article and must not be written by a
        # campaign over many.
        self.protected = {os.path.normpath(p) for p in protected}
        self.ledger = os.path.join(self.state_dir, "ledger.jsonl")

    # ---------------------------------------------------------------- ledger

    def entries(self):
        if not os.path.exists(self.ledger):
            return []
        with open(self.ledger, encoding="utf-8") as fh:
            return [json.loads(line) for line in fh if line.strip()]

    def done(self):
        """{(target, stage): latest completion entry}."""
        out = {}
        for e in self.entries():
            if e.get("status") == "done":
                out[(e["target"], e["stage"])] = e
        return out

    def _log(self, **entry):
        os.makedirs(self.state_dir, exist_ok=True)
        entry["time"] = time.strftime("%Y-%m-%dT%H:%M:%S")
        with open(self.ledger, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, sort_keys=True) + "\n")

    # ---------------------------------------------------------------- gates

    def _gate(self, ctx, texts):
        problems = []
        for g in self.gates:
            try:
                problems += [f"{g.__name__}: {p}" for p in (g(ctx, texts) or [])]
            except Exception as e:  # noqa: BLE001  a crashing gate is a failed gate
                problems.append(f"{g.__name__} raised {type(e).__name__}: {e}")
        return problems

    # ---------------------------------------------------------------- running

    def run(self, apply=False, only=None, stage=None, redo=False, out=print):
        """Run every pending stage for every target. Returns the number of failures."""
        targets = self.targets()
        if only:
            missing = sorted(set(only) - set(targets))
            if missing:
                raise CampaignError(f"unknown targets {missing}")
            targets = {t: targets[t] for t in only}
        stages = [s for s in self.stages if stage is None or s.name == stage]
        if not stages:
            raise CampaignError(f"unknown stage {stage!r}")
        done = self.done()
        failures = 0
        for target, path in sorted(targets.items()):
            for st in stages:
                if (target, st.name) in done and not redo:
                    out(f"  {target:8s} {st.name:16s} done earlier, skipped")
                    continue
                ctx = Context(self, target, path, apply)
                failures += not self._run_stage(ctx, st, out)
        return failures

    def _run_stage(self, ctx, st, out):
        changes = st.run(ctx) or []
        if not all(isinstance(c, Change) for c in changes):
            raise CampaignError(f"stage {st.name} must return a list of Change")
        paths = [os.path.normpath(c.path) for c in changes]
        if len(set(paths)) != len(paths):
            raise CampaignError(f"stage {st.name} changed one file twice for {ctx.target}")
        hit = sorted(set(paths) & self.protected)
        if hit:
            out(f"  {ctx.target:8s} {st.name:16s} REFUSED, protected paths {hit}")
            self._log(target=ctx.target, stage=st.name, status="refused", detail=f"protected {hit}")
            return False
        current = {}
        for c in changes:
            full = os.path.join(ROOT, c.path)
            current[c.path] = open(full, encoding="utf-8").read() if os.path.exists(full) else None
        real = [c for c in changes if current[c.path] != c.text]
        before = set(self._gate(ctx, {p: t for p, t in current.items() if t is not None}))
        after = set(self._gate(ctx, {c.path: c.text for c in changes}))
        new = sorted(after - before)
        if new:
            out(f"  {ctx.target:8s} {st.name:16s} GATE FAILED, nothing written")
            for p in new[:10]:
                out(f"      {p}")
            self._log(target=ctx.target, stage=st.name, status="gate-failed", detail=new[:20])
            return False
        if not ctx.apply:
            out(f"  {ctx.target:8s} {st.name:16s} would change {len(real)} file(s)"
                + (f", existing problems {len(before)}" if before else ""))
            return True
        snap = os.path.join(ctx.state, f"pre_{st.name}")
        for c in real:
            if current[c.path] is not None:
                dest = os.path.join(snap, c.path)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copyfile(os.path.join(ROOT, c.path), dest)
        for c in real:
            full = os.path.join(ROOT, c.path)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as fh:
                fh.write(c.text)
        self._log(target=ctx.target, stage=st.name, status="done",
                  wrote={c.path: _hash(c.text) for c in real})
        out(f"  {ctx.target:8s} {st.name:16s} wrote {len(real)} file(s)")
        return True

    def status(self, out=print):
        """Each target's stages, marking files edited since their stage completed."""
        done = self.done()
        for target in sorted(self.targets()):
            cells = []
            for st in self.stages:
                e = done.get((target, st.name))
                if not e:
                    cells.append(f"{st.name}:pending")
                    continue
                drift = [p for p, h in e.get("wrote", {}).items()
                         if not os.path.exists(os.path.join(ROOT, p))
                         or _hash(open(os.path.join(ROOT, p), encoding="utf-8").read()) != h]
                cells.append(f"{st.name}:done" + ("(edited since)" if drift else ""))
            out(f"  {target:8s} " + "  ".join(cells))


# ------------------------------------------------------------ helpers for stages

def edit_change(path, text, specs):
    """A Change from `edits` specs, rerun-safe, so a repeated stage is a no-op."""
    import edits
    out, _report = edits.apply_specs(text, specs, rerun=True)
    return Change(path, out)


def sample(population, n, seed, exclude=()):
    """A seeded sample drawn before reading, excluding records already read.

    Returns (sample, record), where the record names the population size, the
    seed and the exclusions, so a reviewer can redraw exactly what was read.
    """
    if not isinstance(seed, int):
        raise CampaignError("seed must be an integer, so the sample can be redrawn")
    pool = sorted(set(population) - set(exclude))
    picked = random.Random(seed).sample(pool, min(n, len(pool)))
    return picked, {"population": len(pool), "excluded": len(set(population) & set(exclude)),
                    "seed": seed, "n": len(picked)}


def wilson(k, n, z=1.959964):
    """The Wilson score interval for k successes in n trials, at 95 percent by default."""
    if n <= 0 or not 0 <= k <= n:
        raise CampaignError(f"wilson needs 0 <= k <= n and n > 0, got {k} of {n}")
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, centre - half), min(1.0, centre + half)


def escalate(k, n, threshold):
    """Whether a sampled rate calls for reading everything.

    THE UPPER BOUND, NOT THE POINT ESTIMATE, is compared with the threshold.
    Three samples under the threshold understated contamination, 3.0 against
    3.7, 2.7 against 4.8 and 4.0 against about 6.5 percent.
    """
    return wilson(k, n)[1] >= threshold


def chunks(rows, size, directory, stem="chunk"):
    """Write rows to numbered reading files of at most `size` lines. Returns the paths.

    Only files written here may be read back as readings. A cross-reference file
    that happened to match the reading glob once overrode 1,466 readings.
    """
    if size < 1:
        raise CampaignError("chunk size must be positive")
    os.makedirs(directory, exist_ok=True)
    paths = []
    for i in range(0, len(rows), size):
        p = os.path.join(directory, f"{stem}_{i // size:02d}.txt")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("\n".join(rows[i:i + size]) + "\n")
        paths.append(p)
    with open(os.path.join(directory, f"{stem}_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump([os.path.basename(p) for p in paths], fh)
    return paths


def read_verdicts(directory, vocabulary, stem="verdicts"):
    """{key: (code, reason)} from `<stem>_NN.txt` files, each line `key<TAB>code<TAB>reason`.

    Strict, because a reading is a judgement that will be applied. An unknown
    code, a duplicate key or a malformed line is an error, and only files named
    in the chunk manifest's numbering are read.
    """
    manifest = os.path.join(directory, "chunk_manifest.json")
    allowed = None
    if os.path.exists(manifest):
        allowed = {re.sub(r"^chunk_", f"{stem}_", n) for n in json.load(open(manifest))}
    out = {}
    for name in sorted(os.listdir(directory)):
        if not re.fullmatch(rf"{re.escape(stem)}_\d+\.txt", name) or (allowed and name not in allowed):
            continue
        for i, line in enumerate(open(os.path.join(directory, name), encoding="utf-8"), 1):
            if not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                raise CampaignError(f"{name}:{i}: expected key, tab, code")
            key, code, reason = parts[0], parts[1], "\t".join(parts[2:])
            if code not in vocabulary:
                raise CampaignError(f"{name}:{i}: unknown verdict {code!r}, allowed {sorted(vocabulary)}")
            if key in out:
                raise CampaignError(f"{name}:{i}: {key} judged twice")
            out[key] = (code, reason)
    return out


def relocate(quote, text):
    """The line number of the single line containing `quote`, or an error.

    Ledger line numbers drift with every edit above them, so a ledger cites a
    verbatim quote and the line is found again. Zero or several matches is
    reported, never guessed.
    """
    hits = [i for i, line in enumerate(text.splitlines(), 1) if quote in line]
    if len(hits) != 1:
        raise CampaignError(f"quote found on {len(hits)} lines: {quote[:60]!r}")
    return hits[0]


def replace_section(text, heading, body):
    """Text with the `## heading` section replaced by `body`, or appended when absent."""
    block = f"## {heading}\n\n{body.strip()}\n"
    pat = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    if pat.search(text):
        return pat.sub(lambda _m: block + "\n", text, count=1).rstrip("\n") + "\n"
    return text.rstrip("\n") + "\n\n" + block


def mutation_check(verifier, text, mutations):
    """Mutations that the verifier fails to catch. Empty means every check can fail.

    `verifier(text)` returns True when the text passes. Each mutation is a
    function of the text, and a mutation that does not change the text is itself
    reported, since it tests nothing.
    """
    if not verifier(text):
        raise CampaignError("the verifier fails the unmutated text, so mutations prove nothing")
    missed = []
    for m in mutations:
        bent = m(text)
        if bent == text:
            missed.append(f"{m.__name__}: did not change the text")
        elif verifier(bent):
            missed.append(f"{m.__name__}: passed the verifier")
    return missed


# ------------------------------------------------------------ command line

def load(path):
    spec = importlib.util.spec_from_file_location("campaign_file", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    c = getattr(mod, "CAMPAIGN", None)
    if not isinstance(c, Campaign):
        raise CampaignError(f"{path} defines no CAMPAIGN")
    return c


def main(argv):
    ap = argparse.ArgumentParser(prog="campaign.py", description=__doc__.split("\n")[0])
    ap.add_argument("command", choices=["status", "run"])
    ap.add_argument("file", help="campaign file defining CAMPAIGN")
    ap.add_argument("--apply", action="store_true", help="write; without it nothing is written")
    ap.add_argument("--only", action="append", help="a target name, repeatable")
    ap.add_argument("--stage", help="run one stage")
    ap.add_argument("--redo", action="store_true", help="rerun stages the ledger records as done")
    a = ap.parse_args(argv[1:])
    try:
        c = load(a.file)
        if a.command == "status":
            c.status()
            return 0
        failures = c.run(apply=a.apply, only=a.only, stage=a.stage, redo=a.redo)
    except (CampaignError, OSError) as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1
    if not a.apply:
        print("dry run, nothing written; pass --apply to write")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
