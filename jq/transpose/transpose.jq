def pad:
  .
  | reverse
  | [
    foreach .[] as $i (
      0;                             # Initial length
      [., ($i | length)] | max;      # Set length to max
      $i + " " * (. - ($i | length)) # Pad line to length
    )
  ]
  | reverse
  ;

.lines
| pad
| map(split(""))
| transpose
| map(add)
