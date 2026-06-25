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

## URL Response

A bash check that batches every URL in the draft through curl.

```bash
grep -oE "https?://[^ ]+" _drafts/article_filename.markdown | sort -u > /tmp/urls.txt
while read url; do
  status=$(curl -sI -o /dev/null -w "%{http_code}" -L --max-time 10 "$url" 2>/dev/null)
  echo "$status $url"
done < /tmp/urls.txt
```

Expect 200 responses across the board. See [URL Verification](./URL_VERIFICATION.md) for the catalogue of canonical sites that return 403 to curl despite the URL being correct.

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
