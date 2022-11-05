.
| if (.strand1 | length) != (.strand2 | length)
  then "strands must be of equal length" | halt_error
  else .
  end
| [(.strand1 | split("")), (.strand2 | split(""))]
| transpose
| map(if .[0] != .[1] then 1 else 0 end)
| add // 0
