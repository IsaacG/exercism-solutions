def pad:
  def _width($len):
    if length == 0 then empty
    else
      .
      | ([$len, (first | length)] | max) as $m
      | [$m, .[0]], (.[1:] | _width($m))
    end
    ;

  .
  | reverse
  | [_width(0) | (last + " " * (first - (last | length)))]
  | reverse
  ;

.lines
| pad
| map(split(""))
| transpose
| map(add)
