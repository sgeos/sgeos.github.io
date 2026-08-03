#!/bin/sh
# _publish.sh

if [ "${#}" -lt 1 ]
then
  echo "Usage:"
  echo "  ${0} FILE [FILE...]"
  exit 1
fi

for FILENAME in "${@}"
do
  if [ ! -f "${FILENAME}" ]
  then
    echo "'${FILENAME}' does not exist."
  elif [ ! -r "${FILENAME}" ]
  then
    echo "'${FILENAME}' cannot be read."
  else
    # The hyphen must come first in the bracket expression. Written as
    # [+-:0-9 ] it reads as the range + to :, which BSD sed on macOS rejects
    # with "invalid character range". The script then found no date, reported
    # every file as undated, and silently moved nothing. GNU sed accepted the
    # range, so this failed only on macOS.
    DATE=$(sed -n "/^date:[-+:0-9 ]*$/{p; q;}" "${FILENAME}" | awk '{ print $2 }')
    if [ -n "$DATE" ]
    then
      echo "git add '${FILENAME}'"
      git add "${FILENAME}"
      echo "git mv '${FILENAME}' '_posts/${DATE}-$(basename "${FILENAME}")'"
      git mv "${FILENAME}" "_posts/${DATE}-$(basename "${FILENAME}")"
      #echo "git commit -m 'Published _posts/${DATE}-$(basename $FILENAME).'"
      #git commit -m "Published _posts/${DATE}-$(basename $FILENAME)"
    else
      echo "'${FILENAME}' does not have a date."
    fi
  fi
done

