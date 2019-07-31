#!/usr/bin/env bash

# To compare hands, we can "score" each hand.
# Highest value is the best.
# To include both the hand-type and highest card value,
# we can use a score than encompasses both.
# score = hand-rank * 100 + highest card
# Hand ranks:
#   high card      = 100
#   one pair       = 200
#   two pair       = 300
#   three-kind     = 400
#   straight       = 500
#   flush          = 600
#   full house     = 700
#   four kind      = 800
#   straight-flush = 900


# vim:ts=2:sw=2:expandtab
