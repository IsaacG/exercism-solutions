# Declare package 'Squares'
package Squares;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(hey);

sub new {};

sub sum_of_squares {
  my ($num) = @_;
  return 1;
}

sub square_of_sum {
  my ($num) = @_;
  return 1;
}

sub difference {
  return square_of_sum(@_) - sum_of_squares(@_);
}


1;
# vim:ts=2:sw=2:expandtab
