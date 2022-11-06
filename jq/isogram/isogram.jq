.phrase
| ascii_downcase
| [scan("[a-z]")]
| reduce .[] as $i ({}; .[$i] = (.[$i]//0) + 1)
| [
  to_entries[]
  | .value
]
| max <= 1
