.moment
| (
    if . | test("^\\d{4}(-\\d{2}){2}$")
    then "%Y-%m-%d"
    elif . | test("^\\d{4}(-\\d{2}){2}T\\d{2}(:\\d{2}){2}$")
    then "%Y-%m-%dT%H:%M:%S"
    else "invalid time format\n" | halt_error
    end
  ) as $fmt
| strptime($fmt)|mktime + 1000000000|todate|rtrimstr("Z")
