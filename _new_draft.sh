#!/bin/sh
DRAFT="_drafts/${1-new_draft}.markdown"
cp _drafts/template.markdown "${DRAFT}"
vim "${DRAFT}"
echo "${DRAFT}"

