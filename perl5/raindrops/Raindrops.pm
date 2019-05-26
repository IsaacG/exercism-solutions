package Raindrops;
use strict;
use warnings;
use feature qw(signatures);
use Exporter 'import';
our @EXPORT_OK = qw(raindrop);

sub raindrop ($number) {
  my $out = "";
  my @sounds = (["Pling", 3], ["Plang", 5], ["Plong", 7]);
  foreach my $pair (@sounds) {
    my ($sound, $factor) = @$pair;
    $out .= $sound if ($number % $factor == 0);
  }
  return $out || $number;
}

1;


# vim:ts=2:sw=2:expandtab
