.heyBob
# Strip whitespace.
| sub("[[:space:]]*$"; "")
| (. == "") as $silent
| (. | test("^[^[:lower:]]*[[:upper:]][^[:lower:]]*$")) as $yelling
| (. | endswith("?")) as $question
| if $silent
  then "Fine. Be that way!"
  elif $yelling
  then
    if $question
    then "Calm down, I know what I'm doing!"
    else "Whoa, chill out!"
    end
  elif $question
  then "Sure."
  else "Whatever."
  end
