#!/usr/bin/env bash

boolRC () { (( $? == 0 )) && echo true || echo false; }

shopt -s extglob

# Shout must contain an upper and no lower.
shout='*([^[:lower:]])+([[:upper:]])*([^[:lower:]])'

main () {
  read -d '' input <<< "${1:-}" # Trim whitespace
  case "$input" in
    # Forceful question - shouted question.
    $shout\? ) echo "Calm down, I know what I'm doing!";;
    # Normal question, ends in ?
    *\? ) echo "Sure." ;;
    # Shouted
    $shout ) echo "Whoa, chill out!";;
    # Silence
    *([[:space:]]) ) echo "Fine. Be that way!";;
    *) echo "Whatever." ;;
  esac

}

main "$@"


# vim:ts=2:sw=2:expandtab
