#!/usr/bin/env bash

set -o errexit
set -o nounset

main () {
  if (( $# != 1 )); then
    echo 'Usage: ./error_handling <greetee>'
    return 1
  fi
  echo "Hello, $1"
}

main "$@"
