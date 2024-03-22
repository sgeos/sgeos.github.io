#!/usr/bin/env sh # _preview.sh

PORT=${1:-${PORT:-4000}}

echo "\nView blog at: http://localhost:${PORT}/\n"
jekyll serve --host 0.0.0.0 --port "${PORT}" --drafts --future --watch

