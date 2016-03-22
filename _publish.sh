#!/bin/sh

if [ "${#}" -lt 1 ]
then
  echo "Usage:"
  echo "  ${0} FILE [FILE...]"
fi

for FILENAME in "${@}"
do
  if [ ! -f ${FILENAME} ]
  then
    echo "'${FILENAME}' does not exist."
  elif [ ! -r ${FILENAME} ] 
  then
    echo "'${FILENAME}' can not be read."
  else
    DATE=$(sed -n "/^date:[+-:0-9 ]*$/{p; q;}" "${FILENAME}" | awk '{ print $2 }')
    if [ $DATE ]
    then
      echo "mv ${FILENAME} _posts/${DATE}-$(basename $FILENAME)"
      git mv "${FILENAME}" "_posts/${DATE}-$(basename $FILENAME)"
    else
      echo "'${FILENAME}' does not have a date."
    fi
  fi
done

