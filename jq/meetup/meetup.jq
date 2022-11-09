def offset($week):
  {"first": 1, "second": 8, "third": 15, "fourth": 22, "fifth": 29, "teenth": 13}
  | .[$week]
  ;

.
| .dayofweek as $dow
| .month |= . - 1
| if .week == "last"
  then
    .
    | (.year * 12 + .month + 1) as $ym
    | [($ym / 12 | floor), ($ym % 12), 1, 0, 0, 0, 0, 0]
    | mktime - (7 * 24 * 60 * 60)
  else
    .
    | [.year, .month, offset(.week), 0, 0, 0, 0, 0]
    | mktime
  end
| until(strftime("%A") == $dow; . + 60 *60 * 24)
| strftime("%Y-%m-%d")
