package Grains;
use strict;
use warnings;
use bigint;
use feature qw/signatures/;
use Exporter 'import';
our @EXPORT_OK = qw(grains_on_square total_grains);
use Math::BigInt;

sub grains_on_square ($square) {
  die "Bad square $square" if $square < 1 or $square > 64;
  return 2 ** ($square - 1);
}

sub total_grains () {
  return 2 ** 64 - 1;
}

1;


# vim:ts=2:sw=2:expandtab
