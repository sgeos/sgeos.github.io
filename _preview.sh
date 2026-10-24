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
# FUTURE controls whether forward-dated posts are rendered. It defaults to 1,
# preserving the long-standing behaviour, but that does NOT match the live site:
# _config.yml sets future: false, so forward-dated posts are excluded from the
# real build and return 404 until their dates arrive. A clean preview is
# therefore not evidence that a forward-dated cross-reference is safe. Run with
# FUTURE=0 to see what the deploy will actually publish.
#
# Jekyll runs through `bundle exec`, against the same Gemfile.lock and plugins
# CI uses. The script therefore needs a satisfied bundle; run `bundle install`
# if `bundle check` fails. It previously ran a globally installed jekyll with
# the Bundler require disabled, because the bundle was never installed. That
# path broke when the MacPorts Ruby 3.1 could no longer build its socket
# extension under Apple Clang 21 on Darwin 27 (Ruby bug 21629, not fixed in 3.1),
# and it also skipped the Gemfile plugins, so its pages differed from the deploy.
#
# Usage:
#     ./_preview.sh            # port 4000, drafts off, future-dated shown
#     ./_preview.sh 8080       # custom port
#     DRAFTS=1 ./_preview.sh   # include drafts (may fail, see above)
#     FUTURE=0 ./_preview.sh   # match the live site: hide forward-dated posts
#
# THIS SCRIPT SHOWS YOU A PAGE. IT DOES NOT TELL YOU WHETHER THE DEPLOY WILL
# PASS. It ends in `jekyll serve --watch`, which never returns, so no check can
# run after it, and the rendered-output audit CI runs is therefore not run here.
# Use ./_check.sh for that; it runs _verify.py, a production build and
# _lib/render.py in the same order CI does.

set -eu

# Set PORT (use 4000 as fallback if both $1 and $PORT are unset)
PORT="${1:-${PORT:-4000}}"

# Drafts are off by default; opt in with DRAFTS=1.
DRAFTS_FLAG=""
if [ "${DRAFTS:-0}" != "0" ]; then
    DRAFTS_FLAG="--drafts"
    printf '%s\n' "Including drafts. The build will fail if any draft has an unresolved post_url reference."
fi

# Print the blog preview link
printf '\nView blog at: http://localhost:%s/\n' "${PORT}"

# Forward-dated posts are shown unless FUTURE=0 is set. See the note above:
# the default does not match production.
if [ "${FUTURE:-1}" = "0" ]; then
    FUTURE_FLAG=""
    printf '%s\n' "FUTURE=0: hiding forward-dated posts, matching the live site."
else
    FUTURE_FLAG="--future"
    printf '%s\n' "Showing forward-dated posts. The live site hides them; use FUTURE=0 to match."
fi

# Fail early with a clear message rather than a Bundler stack trace.
command -v bundle > /dev/null || {
    printf '%s\n' "bundle is not installed or not in PATH." >&2
    exit 1
}
bundle check > /dev/null || {
    printf '%s\n' "The bundle is not satisfied. Run: bundle install" >&2
    exit 1
}

# Start the Jekyll server
bundle exec jekyll serve --host 0.0.0.0 --port "${PORT}" ${DRAFTS_FLAG} ${FUTURE_FLAG} --watch
