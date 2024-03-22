#!/usr/bin/env sh # _new_draft.sh

TEMPLATE="_drafts/template.markdown"
DRAFT="_drafts/${1-new_draft}.markdown"

cp -n "${TEMPLATE}" "${DRAFT}"
vim "${DRAFT}"
echo "${DRAFT}"

