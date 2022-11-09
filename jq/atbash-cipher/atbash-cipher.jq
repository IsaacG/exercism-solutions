.
| .property as $property
| .input.phrase
  # Lowercase and remove non-alpha-numericals
| ascii_downcase
| sub("[^[:alnum:]]"; ""; "g")
| explode
| map(
  if 97 <= . and . <= 122
  # atbash for a-z
  then 219 - .
  # pass-through digits
  else .
  end
)
| implode
| if $property == "encode"
  then [scan(".{1,5}")] | join(" ")
  else .
  end
