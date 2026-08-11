#!/bin/sh
# _check.sh
#
# Run locally exactly what CI runs, in the same order, so an author finds a gate
# failure before the deploy does.
#
#     ./_check.sh              # verify, build, audit rendered output
#     ./_check.sh --drafts     # include drafts in the build
#     ./_check.sh --weights    # also report page weight
#
# WHY THIS IS SEPARATE FROM _preview.sh. That script ends in `jekyll serve
# --watch`, which never returns, so nothing can run after it. A preview shows
# you a page; this tells you whether the deploy gate will pass.
#
# The build goes to a throwaway directory rather than _site, because _site is
# also what `jekyll serve` writes and clobbering it mid-preview is confusing.
# It is removed on exit.

set -eu

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

DRAFTS_FLAG=""
WEIGHTS=0
for arg in "$@"; do
    case "$arg" in
        --drafts)  DRAFTS_FLAG="--drafts" ;;
        --weights) WEIGHTS=1 ;;
        *) printf 'unknown option: %s\n' "$arg" >&2; exit 2 ;;
    esac
done

OUT="$(mktemp -d "${TMPDIR:-/tmp}/blogcheck.XXXXXX")"
# The log lives OUTSIDE the destination. Jekyll cleans its destination before building, so a
# log written into it is deleted before the build that was supposed to fill it.
LOG="$(mktemp "${TMPDIR:-/tmp}/blogcheck.log.XXXXXX")"
trap 'rm -rf "$OUT" "$LOG"' EXIT INT TERM

printf '\n== 1. corpus invariants ==\n'
python3 _verify.py

printf '\n== 2. build ==\n'
if command -v bundle > /dev/null 2>&1 && [ -f Gemfile.lock ]; then
    JEKYLL_ENV=production bundle exec jekyll build --baseurl "" \
        ${DRAFTS_FLAG} --destination "$OUT" > "$LOG" 2>&1 || {
        printf 'BUILD FAILED\n' >&2
        tail -30 "$LOG" >&2
        exit 1
    }
else
    printf 'bundle unavailable; falling back to the plain jekyll on PATH\n'
    JEKYLL_ENV=production jekyll build --baseurl "" \
        ${DRAFTS_FLAG} --destination "$OUT" > "$LOG" 2>&1 || {
        printf 'BUILD FAILED\n' >&2
        tail -30 "$LOG" >&2
        exit 1
    }
fi
grep -iE '^ *Conflict|shared by multiple' "$LOG" || true
printf 'build ok\n'

printf '\n== 3. rendered output ==\n'
python3 _lib/render.py "$OUT"

if [ "$WEIGHTS" = "1" ]; then
    printf '\n== page weight ==\n'
    python3 _lib/render.py "$OUT" --weights
fi

printf '\nall checks passed\n'
