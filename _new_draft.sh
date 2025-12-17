#!/bin/sh
# _new_draft.sh

set -eu

TEMPLATE="_drafts/template.markdown"
NAME="${1:-new_draft}"
DRAFT="_drafts/${NAME}.markdown"

# Ensure template exists
[ -f "${TEMPLATE}" ] || {
    printf '%s\n' "Template not found: ${TEMPLATE}" >&2
    exit 1
}

# Refuse unsafe names
case "${NAME}" in
    */*|*..*)
        printf '%s\n' "Invalid draft name" >&2
        exit 1
        ;;
esac

# Create draft if it doesn't exist
if [ ! -e "${DRAFT}" ]; then
    cp "${TEMPLATE}" "${DRAFT}"
else
    printf "Warning: \"%s\" exists." "${DRAFT}"
fi

# Open editor
"${EDITOR:-vi}" "${DRAFT}"

printf '%s\n' "${DRAFT}"

