package Anagram;
use strict;
use warnings;
use Exporter 'import';
use feature qw(signatures);
our @EXPORT_OK = qw(match);

sub count($word) {
  my %count;
  $count{$_}++ for split '', lc $word;
  return \%count;
}

sub same($target, $got) {
  return 0 if scalar keys %$target != scalar keys %$got;
  for (keys %$target) {
    return 0 if not exists $got->{$_} or $got->{$_} != $target->{$_}
  }
  return 1;
}

sub match ($word, @words) {
  my $target = count($word);
  my @matches = grep {lc $word ne $_} grep {same $target, count($_)} @words;
  return \@matches;
}

1;

# vim:ts=2:sw=2:expandtab
