def toRna:
  .
  | {"G": "C", "C": "G", "T": "A", "A": "U"} as $m
  | split("")
  | map($m[.])
  | add // ""
  ;
