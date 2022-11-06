.heyBob
# Strip whitespace.
| sub("[[:space:]]*$"; "")
| # Silence.
  if . == ""
  then "Fine. Be that way!"
  # Yelling: uppercase, no lowercase.
  elif . | test("^[^[:lower:]]*[[:upper:]][^[:lower:]]*$")
  then
    # Yelling question.
    if . | endswith("?")
    then "Calm down, I know what I'm doing!"
    # Plain yelling.
    else "Whoa, chill out!"
    end
  # Non-yelling question.
  elif . | endswith("?")
  then "Sure."
  else "Whatever."
  end
