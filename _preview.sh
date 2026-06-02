#!/bin/sh
# _preview.sh
#
# Local preview server for the blog.
#
# By default this previews PUBLISHED and FUTURE-dated posts only, with drafts
# turned OFF. Drafts are off by default because the _drafts/ directory holds
# long-standing release-candidate drafts that cross-reference one another with
# post_url tags pointing at their planned, not yet published, filenames. The
# post_url tag resolves only against _posts/, so building with --drafts fails
# fatally until those drafts are published. A drafts-free preview always builds.
#
# To include drafts anyway, for example after the cross-references resolve, run
# with DRAFTS=1:
#     DRAFTS=1 ./_preview.sh
# Note that DRAFTS=1 will abort if any draft still has an unresolved post_url.
#
# The Bundler require is disabled and GEM_HOME defaults to the user gem
# directory so the script runs against the locally installed gems rather than
# an unsatisfied bundle. The github-pages-free bundle is built in CI, not here.
#
# Usage:
#     ./_preview.sh            # port 4000, drafts off
#     ./_preview.sh 8080       # custom port, drafts off
#     DRAFTS=1 ./_preview.sh   # include drafts (may fail, see above)

set -eu

# Set PORT (use 4000 as fallback if both $1 and $PORT are unset)
PORT="${1:-${PORT:-4000}}"

# Run against the locally installed gems, not the (unsatisfied) bundle.
export JEKYLL_NO_BUNDLER_REQUIRE=true
export GEM_HOME="${GEM_HOME:-$(ruby -e 'print Gem.user_dir')}"

# Drafts are off by default; opt in with DRAFTS=1.
DRAFTS_FLAG=""
if [ "${DRAFTS:-0}" != "0" ]; then
    DRAFTS_FLAG="--drafts"
    printf '%s\n' "Including drafts. The build will fail if any draft has an unresolved post_url reference."
fi

# Print the blog preview link
printf '\nView blog at: http://localhost:%s/\n' "${PORT}"

# Check if `jekyll` is available
command -v jekyll > /dev/null || {
    printf '%s\n' "jekyll is not installed or not in PATH." >&2
    exit 1
}

# Start the Jekyll server
jekyll serve --host 0.0.0.0 --port "${PORT}" ${DRAFTS_FLAG} --future --watch
