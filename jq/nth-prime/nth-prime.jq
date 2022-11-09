# ===========================
# Three is_prime implementations, with greatly varying speeds.

# Slow. 1001'th prime: 5.4 seconds.
def is_prime_v1($priors; $threshold):
  def under:
    recurse(. + 1; $priors[.] // $threshold < $threshold) | $priors[.]
    ;

  . as $candidate |
  [ 0 | under] |
  all($candidate % . != 0)
 ;

# Fast. 10001'th prime: 5.6 seconds.
def is_prime_v2($priors; $threshold):
  def under:
    if $priors[.] <= $threshold
      then $priors[.], (. + 1 | under)
      else empty
    end
  ;

  . as $candidate |
  [0 | under] |
  all($candidate % . != 0)
 ;

# Fastest. 10001'th prime: 2.9 seconds.
def is_prime($priors; $threshold):
  def _is_prime:
    . as [$idx, $candidate] |
    if $priors[$idx] > $threshold
      then true
      elif $candidate % $priors[$idx] == 0
      then false
      else [$idx + 1, $candidate] | _is_prime
    end
  ;

  [0, .] | _is_prime
;

# ===========================

# Given a list of primes, return a list of primes with one addition.
def next_prime:
  . as $priors |
  last + 2 |
  until(is_prime($priors; sqrt); . + 2) |
  $priors + [.]
;

# Return the nth prime.
def nth_prime:
  if   $n  < 1 then "there is no zeroth prime" | halt_error
  elif $n == 1 then 2
  else
    reduce range(1; $n - 1) as $_ ([3]; next_prime) |
    last
  end
;

nth_prime
