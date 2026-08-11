# Style Verification Scripts

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Verification scripts used during the publication review pass to check prose style, reference integrity, math density, and URL response.

## Style and Reference Integrity

A Python check that reports style violations and reference integrity in a single pass.

```python
import re
content = open('_drafts/article_filename.markdown').read()

# Prose style
print('Em-dashes:', content.count('—'))
print('En-dashes:', content.count('–'))
contr = re.findall(
    r"\b(don't|won't|can't|isn't|aren't|doesn't|didn't|wasn't|weren't|"
    r"it's|that's|there's|we're|they're|you're)\b",
    content, re.IGNORECASE)
print('Contractions:', len(contr))

# Math density
inline_math = re.findall(r'(?<!\$)\$([^\$\n]{1,80})\$(?!\$)', content)
print('Inline math:', len(inline_math))
display = re.findall(r'\$\$[^\$]+\$\$', content)
print('Display math:', len(display))

# Basic stats
print('Lines:', len(content.split('\n')))

# Reference integrity, all anchor namespaces (ref_, research_, related_post_, etc.)
used = set(re.findall(r'\]\[([a-z_0-9]+)\]', content))
defs = re.findall(r'^\[([a-z_0-9]+)\]:', content, re.MULTILINE)
defined = set(defs)
print('Refs used:', len(used), 'defined:', len(defined))
print('Missing:', used - defined)
print('Unused:', defined - used)
print('Definitions sorted:', defs == sorted(defs))
```

All zero counts for em-dashes, en-dashes, and contractions. Used and defined reference counts equal with empty missing and unused sets. Definitions sorted alphabetically.

## Word Frequency

The check above sees punctuation only. It reported prose style clean on an article using
`specific` 46.2 times per thousand words, because no check looked at word choice. This one does.

```python
import re
from collections import Counter

content = open('_drafts/article_filename.markdown').read()

# Strip what is not prose: front matter, fenced code, Jekyll highlight blocks,
# display math, headings, tables, link definitions, inline math, code spans.
body = re.sub(r'(?s)\A---.*?\n---\n', '', content)
body = re.sub(r'(?s)```.*?```', ' ', body)
body = re.sub(r'(?s)\{%\s*highlight.*?\{%\s*endhighlight\s*%\}', ' ', body)
body = re.sub(r'(?s)\$\$.*?\$\$', ' ', body)
body = re.sub(r'(?m)^(#|\||\[[^\]]+\]:|\s*[-*]\s*\[).*$', ' ', body)
body = re.sub(r'\$[^$\n]+\$|`[^`\n]+`|\{%.*?%\}', ' ', body)

words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]*", body)]
counts = Counter(words)
total = len(words)

# Content-independent words only. Ratio against the corpus is the WRONG
# discriminator: it surfaces topic vocabulary such as `kotlin` or `raycasting`.
WATCH = """specific specifically various comprehensive substantial substantially
particular significant considerable notable essential fundamental crucial critical
key core central primary framework configuration structure mechanism approach
aspect factor element component dimension context scenario distinct underlying
appropriate relevant robust effective efficient relatively typically largely
admits compact leverage utilize facilitate encompass underscore highlight
myriad nuanced holistic pivotal seamless intricate paradigm realm landscape""".split()

print(f'{total} prose words')
for w in WATCH:
    n = counts.get(w, 0)
    if n and n * 1000.0 / total >= 5.0:
        print(f'  {n:>4}  {n * 1000.0 / total:>6.1f}/1k  {w}')
```

A word above roughly 5 per thousand is a flag, not a verdict. Natural corpus rate for `specific`
is near 1.7. Decide each flag against the Diction and Repetition section of the
[Style Guide](../writing/STYLE_GUIDE.md): the word may be the article's subject, in which case
leave it. Also scan for a repeating sentence pattern, which the word counts will not catch.

## URL Response

A bash check that batches every URL in the draft through curl.

```bash
mkdir -p tmp
grep -oE "https?://[^ ]+" _drafts/article_filename.markdown | sort -u > tmp/urls.txt
while read url; do
  status=$(curl -sI -o /dev/null -w "%{http_code}" -L --max-time 10 "$url" 2>/dev/null)
  echo "$status $url"
done < tmp/urls.txt
```

Scratch goes in the project-local `tmp/`, which is gitignored, rather than the system `/tmp`.

Expect 200 responses across the board. See [URL Verification](./URL_VERIFICATION.md) for the catalogue of canonical sites that return 403 to curl despite the URL being correct.

**A 200 does not verify a citation.** It verifies that something is served at that address, not
that the something is the work being cited. A 2026-08-02 audit found thirteen citations whose
title and target did not correspond, every one of them returning 200, including one whose DOI
resolved to an entirely different paper in an unrelated field. For any citation carrying a DOI,
check the DOI against Crossref and confirm the returned title matches the citation. See the
section "An HTTP 200 Does Not Verify a Citation" in [URL Verification](./URL_VERIFICATION.md).

## Acronym Scan

A bash check that lists every multi-letter capitalised token, useful for finding acronyms that may not be spelled out on first use.

```bash
grep -onE "\b[A-Z]{2,}[A-Za-z]*\b" _drafts/article_filename.markdown \
  | awk -F: '{print $2}' \
  | sort -u
```

The reviewer scans the list, identifies any non-proper-noun acronyms not on the spell-out exemption list, and traces them to first body occurrence. See [Acronym Handling](../writing/ACRONYM_HANDLING.md) for the rule and exemption list.

## Numerical Spot-Check

A Python expression for re-deriving a specific worked example, run interactively in the publication shell.

```python
# Example: verify Hagen-Poiseuille pipeline flow
import math
D = 0.05         # 50 mm diameter, m
mu = 0.001       # water dynamic viscosity, Pa s
L = 100          # pipe length, m
dP = 1e5         # 1 bar pressure drop, Pa
Q = (math.pi * D**4 * dP) / (128 * mu * L)
print(f"{Q*1000:.2f} L/s")    # expect ~5 L/s for the stated inputs
```

Use the same expression form as the article's worked example so that any discrepancy reveals a transcription error rather than a notation mismatch.

## Combined Pre-Commit Check

Run the four scripts together as the final pass before the publish commit. Any failure stops the publication until the issue is addressed.

```bash
# 1. Style and reference integrity (Python script above)
# 2. URL response (Bash script above)
# 3. Acronym scan (Bash script above)
# 4. Numerical spot-check (per article, interactive)
```

A clean run produces zero style violations, zero missing or unused references, all URLs returning 200 or known 403, and the numerical re-derivations matching the article's stated values.

## Related Sections

- [Publication Review](./PUBLICATION_REVIEW.md) for the broader review pass
- [URL Verification](./URL_VERIFICATION.md) for URL response handling
- [Style Guide](../writing/STYLE_GUIDE.md) for the prose rules being verified
- [MathJax Conventions](../writing/MATHJAX_CONVENTIONS.md) for math density targets


## Rendered Output

**Every check above this section reads markdown source and therefore predicts what the renderer will
do rather than observing it.** Run corpus-wide on 2026-08-11, `_lib/lint.py` reported 1,596
defect-severity findings and the rendered pages carried none of them.

```sh
./_check.sh                          # _verify.py, a production build, then the rendered audit
./_check.sh --drafts                 # include drafts
./_check.sh --weights                # also report page weight
python3 _lib/render.py <site>        # the audit alone, against an existing build
python3 _lib/render.py <site> --weights
```

`render.py` flags only what a reader would see: an unresolved `[text][anchor]`, an unexpanded marker,
unrendered Liquid, raw `$$`, empty or nested-empty list items, double-escaped entities, and unbalanced
MathJax delimiters. **Markup inside `<pre>` and `<code>` is excluded**, because the Jekyll and MathJax
tutorial posts display that syntax as their subject.

**The math check counts by backslash-run parity**, since `\\[2mm]` is a LaTeX line break rather than a
delimiter and a block whose last line ends in a break closes as `\\\]`. Two earlier and more obvious
rules each reported correct pages as broken, and the second masked the first.

**`_preview.sh` cannot tell you whether the deploy will pass**, because it ends in `jekyll serve
--watch` and nothing can run after it. Use `./_check.sh`.

## Identifier Resolution

Distinct from citation verification and not a substitute for it.

```sh
python3 _lib/resolve.py <post.markdown>              # every identifier
python3 _lib/resolve.py <post.markdown> 250 20260811 # a seeded sample
```

`resolve.py` asks whether an identifier resolves at all. `_verify_citations.py` asks whether it
resolves to **the work it is cited as**. See the cadence and run record in
[URL Verification](./URL_VERIFICATION.md).

**Bot mitigation is not a citation failure.** Publishers answer 202 and 403 to robots and a Defense
Technical Information Center deposit refuses the connection outright, so those count as resolution and
the fallback asks the issuing registry, which is a different route rather than a retry.
