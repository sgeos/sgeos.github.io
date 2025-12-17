#!/bin/sh
# _preview.sh

set -eu

# Set PORT (use 4000 as fallback if both $1 and $PORT are unset)
PORT="${1:-${PORT:-4000}}"

# Print the blog preview link
printf '\nView blog at: http://localhost:%s/\n' "${PORT}"

# Check if `jekyll` is available
command -v jekyll > /dev/null || {
    printf '%s\n' "jekyll is not installed or not in PATH." >&2
    exit 1
}

# Start the Jekyll server
jekyll serve --host 0.0.0.0 --port "${PORT}" --drafts --future --watch

