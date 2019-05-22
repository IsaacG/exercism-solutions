# Declare package 'Bob'
package Bob;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(hey);

sub hey {
  my ($msg) = @_;
  my $loud = qr/^[^[:lower:]]*[[:upper:]][^[:lower:]]*$/;
  my $question = qr/\?[[:space:]]*$/;
  my $shh = qr/^[[:space:]]*$/;

  if ($msg =~ $loud and $msg =~ $question) {
    return "Calm down, I know what I'm doing!";
  } elsif ($msg =~ $question) {
    return "Sure.";
  } elsif ($msg =~ $loud) {
    return "Whoa, chill out!";
  } elsif ($msg =~ $shh) {
    return "Fine. Be that way!";
  } else {
    return "Whatever.";
  }
}

1;
