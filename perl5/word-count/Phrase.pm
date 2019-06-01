package Phrase;
use strict;
use warnings;
use feature qw(signatures);
use Exporter 'import';
our @EXPORT_OK = qw(word_count);


sub word_count ($phrase) {
  my %count;
  $count{$_}++ for grep {$_ ne ''} map { s/[^[:alnum:]]//gr } split /\s/, lc $phrase;
  return \%count;
}

1;
# vim:ts=2:sw=2:expandtab
