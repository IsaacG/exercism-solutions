#!/usr/bin/env bash

# Defaults, overridden with flags.
line_num=0
case_sensitive=1
filename=0
invert=0
full_line=0

my_grep () {
  while [[ $1 = -* ]]; do
    case "$1" in
      -n) line_num=1;;
      -l) filename=1;;
      -i) case_sensitive=0;;
      -v) invert=1;;
      -x) full_line=1;;
      -*) ;;
    esac
    shift
  done

  pattern=$1
  shift
  
  (( ! case_sensitive )) && shopt -s nocasematch || shopt -u nocasematch
  (( multifile = ($# > 1) ? 1 : 0 ))

  for file in "$@"; do
    local -i line=0 cont=1
    while read -r && (( cont )); do
      (( line++ ))
      # Match full or partial line
      [[ $REPLY = $pattern ]] || (( ! full_line )) && [[ $REPLY = *"$pattern"* ]]
      # Check if matched - or failed to.
      if (( (invert && $? == 1) || (! invert && $? == 0) )); then
        if (( filename )); then
          printf '%s\n' "$file"
          (( cont = 0 ))
          break  # don't bother reading the rest of the file.
        fi
        (( multifile )) && printf '%s:' "$file"
        (( line_num )) && printf '%d:' "$line"
        printf '%s\n' "$REPLY"
      fi
    done < "$file"
  done

  return 0
}

my_grep "$@"

# vim:ts=2:sw=2:expandtab
