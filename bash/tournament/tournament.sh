#!/usr/bin/env bash

row () {
  printf '%-30s | %2s | %2s | %2s | %2s | %2s\n' "$@"
}
init () {
  [[ -v 'teams[$1]' ]] && return
  teams[$1]=1
  win[$1]=0 draw[$1]=0 loss[$1]=0
}

row "Team" MP W D L P
declare -A win draw loss teams

compute () {
  while IFS=';' read -r a b r; do
    # echo $a ; echo $b; echo $r
    init "$a"
    init "$b"
    case "$r" in
      win) (( win[$a]++ , loss[$b]++ ));;
      draw) (( draw[$a]++ , draw[$b]++ ));;
      loss) (( loss[$a]++ , win[$b]++ ));;
    *) ;;
    esac
  done
}

if (( $# )); then
  compute < "$1"
elif ! [[ -t 1 ]]; then
  compute
fi
for t in "${!teams[@]}"; do
  matches=$(( win[$t] + draw[$t] + loss[$t] ))
  points=$(( 3 * win[$t] + draw[$t] ))
  row "$t" $matches "${win[$t]}" "${draw[$t]}" "${loss[$t]}" $points
done | sort -t"|" -k6,6nr -k1,1

# vim:ts=2:sw=2:expandtab
