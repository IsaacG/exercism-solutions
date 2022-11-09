def identity($word):
  $word | ascii_downcase | explode | sort
  ;

.
| (.subject | ascii_downcase) as $subject
| identity(.subject) as $sub
| [
  .candidates[]
  | select((. | ascii_downcase) != $subject and identity(.) == $sub)
]
