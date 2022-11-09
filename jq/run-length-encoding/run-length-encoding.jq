# Convert a [$count, $char] to run length encoding.
def tuple_to_str:
  . as [$count, $char]
  | if $count == 0 then ""
    elif $count == 1 then $char
    else "\($count)\($char)"
    end
  ;

# Split a continuous string of chars into "runs" of chars.
def split_into_runs:
  . as [$count, $prior, $rest]
  | if $rest[0] == null
    then [$count, $prior]
    elif $rest[0] == $prior
    then ([$count + 1, $prior, $rest[1:]] | split_into_runs)
    else ([$count, $prior], [1, $rest[0], $rest[1:]] | split_into_runs)
    end
  ;

def encode:
  .
  | [0, null, split("") + [null]]
  | [split_into_runs | tuple_to_str ]
  | add
  ;

def decode:
  [
    # Split into number-char pairs.
    scan("([[:digit:]]*)(.)")
    # Replacing missing counts with "1"
    | if first == "" then ["1", last]
      else .
      end
    # Expand chars
    | last * (first | tonumber)
  ] | add // ""
  ;
