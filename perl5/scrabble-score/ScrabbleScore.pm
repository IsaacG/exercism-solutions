package ScrabbleScore;
use strict;
use warnings;
use Exporter 'import';
use List::Util qw(pairmap sum0);
use feature qw(signatures);
our @EXPORT_OK = qw(score);

my %points = (
	'aeioulnrst' => 1,
	'dg' => 2, 'bcmp' => 3, 'fhvwy' => 4,
	'k' => 5, 'jx' => 8, 'qz' => 10
);
%points = pairmap { map { $_ => $b } split '', $a } %points;

sub score ( $word, %extensions ) {
  return sum0 map { $points{$_} } split '', lc $word;
}

1;


# vim:ts=2:sw=2:expandtab
