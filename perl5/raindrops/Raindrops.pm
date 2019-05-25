package Raindrops;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(raindrop);

sub raindrop {
  my ($number) = @_;
  my $out = "";
  $out .= "Pling" if ($number % 3 == 0);
  $out .= "Plang" if ($number % 5 == 0);
  $out .= "Plong" if ($number % 7 == 0);
  return $out ? $out : $number;
}

1;


# vim:ts=2:sw=2:expandtab
