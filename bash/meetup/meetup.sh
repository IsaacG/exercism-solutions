#!/usr/bin/env bash

readonly -A offset=([first]=1 [second]=8 [third]=15 [fourth]=22 [fifth]=29 [teenth]=13)

main () {
    local yr=$1 mn=$2 nth=$3 dow=$4 start i
    if [[ "${nth}" == "last" ]]; then
        # Roll up to the following month then reverse 7 days.
        (( mn += 1, mn == 13 && ( yr += 1, mn = 1 )))
        start=$(date -d "${yr}/${mn}/1 - 7 days" +%F)
    else
        start="${yr}/${mn}/${offset[$nth]}"
    fi
    # Find the next date with the correct day of week.
    for i in {0..6}; do
        [[ "$(date -d "${start} + ${i} days" +%A)" == "${dow}" ]] && break
    done
    date -d "${start} + ${i} days" +%F
}

main "$@"
