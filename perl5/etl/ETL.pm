package ETL;
use strict;
use warnings;
use feature qw/signatures/;
use Exporter 'import';
our @EXPORT_OK = qw(transform);

sub transform ($mapping) {
  my %new_map = ();
  while(my($val, $chars) = each %$mapping) {
    $new_map{lc $_} = $val for (@$chars);
  }
  return \%new_map;
}

1;


# vim:ts=2:sw=2:expandtab
