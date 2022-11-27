#!/usr/bin/env bash

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    echo "This library of functions should be sourced into another script" >&2
    exit 4
fi
bash_version=$((10 * BASH_VERSINFO[0] + BASH_VERSINFO[1]))
if (( bash_version < 43 )); then
    echo "This library requires at least bash version 4.3" >&2
    return 4
fi

# Append some elements to the given list.
list::append () {
    local -n arr=$1
    shift
    arr+=("$@")
}

# Return only the list elements that pass the given function.
list::filter () {
    local func=$1
    local -n in=$2 out=$3
    for i in "${in[@]}"; do
        "${func}" "${i}" && out+=("${i}")
    done
}

# Transform the list elements, using the given function, into a new list.
list::map () {
    local func=$1
    local -n in=$2 out=$3
    for i in "${in[@]}"; do
        out+=("$("${func}" "${i}")")
    done
}

# Left-fold the list using the function and the initial value.
list::foldl () {
    local func=$1 val=$2
    local -n in=$3
    for i in "${in[@]}"; do
        val=$("${func}" "${val}" "${i}")
    done
    printf '%s\n' "${val}"
}

# Right-fold the list using the function and the initial value.
list::foldr () {
    local func=$1 val=$2
    local -n in=$3
    for ((i = "${#in[@]}" - 1; i >= 0; i--)); do
        val=$("${func}" "${in[i]}" "${val}")
    done
    printf '%s\n' "${val}"
}

# Return the list reversed
list::reverse () {
    local -n in=$1 out=$2
    for ((i = "${#in[@]}" - 1; i >= 0; i--)); do
        out+=("${in[i]}")
    done
}
