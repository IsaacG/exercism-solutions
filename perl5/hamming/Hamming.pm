package Hamming;
use strict;
use warnings;
use feature qw(signatures);
use Exporter 'import';
our @EXPORT_OK = qw(hamming_distance);

sub hamming_distance ($strand1, $strand2) {
  die "left and right strands must be of equal length" if (length($strand1) != length($strand2));
  return grep { substr($strand1, $_, 1) ne substr($strand2, $_, 1) } 0.. length($strand1)-1;
}

1;


# vim:ts=2:sw=2:expandtab
