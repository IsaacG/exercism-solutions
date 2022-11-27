#!/usr/bin/env bash

main () {
    # Mimic a 2D array by using a map and "$x,$y" for the key.
    local -A board
    local x=0 y=0 dx=1 dy=0 i
    # Walk all the coordinates and fill in subsequent values.
    for (( i = 1; i <= $1 * $1; i++ )); do
        board["$x,$y"]="$i"
        (( nx = x + dx, ny = y + dy ))
        # Check for edges or collisions and rotate.
        if [[ -v board["$nx,$ny"] || "$nx" == "-1" || "$nx" == "$1" || "$ny" == "-1" || "$ny" == "$1" ]]; then
            case "$dx,$dy" in
                1,0) dx=0 dy=1;;
                0,1) dx=-1 dy=0;;
                -1,0) dx=0 dy=-1;;
                0,-1) dx=1 dy=0;;
            esac
        fi
        (( x += dx, y += dy ))
    done

    # Print out the resulting board.
    for (( y = 0; y < $1; y++ )); do
        line=()
        for (( x = 0; x < $1; x++ )); do
            line+=("${board["$x,$y"]}")
        done
        echo "${line[*]}"
    done
}

main "$@"
