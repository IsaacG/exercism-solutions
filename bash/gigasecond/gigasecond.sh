#!/usr/bin/env bash

boolRC () { (( $? == 0 )) && echo true || echo false; }

Gs () {
  export TZ=UTC
  birth=$(date +%s -d "$1")
  date -d "@$((birth + 10**9))" +%FT%T
}

(( $# == 1 )) || exit 1
Gs "$1"

# vim:ts=2:sw=2:expandtab
