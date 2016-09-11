#!/bin/sh
TEMPLATE="_drafts/template.markdown"
DRAFT="_drafts/${1-new_draft}.markdown"
cp "${TEMPLATE}" "${DRAFT}"
vim "${DRAFT}"
echo "${DRAFT}"

