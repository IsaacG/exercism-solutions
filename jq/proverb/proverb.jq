.strings
| [
  .
  | . as $objects
  | range(length - 1)
  | "For want of a \($objects[.]) the \($objects[. + 1]) was lost."
] + [
  if length > 0
  then "And all for the want of a \(first)."
  else empty
  end
  ]

