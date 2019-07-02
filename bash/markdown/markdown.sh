#!/usr/bin/env bash

# 1. Fix indentation
# 2. Change [ to [[ or ((
# 3. Rewrite tests
# 4. Rewrite <strong> to a single test/update.
# 5. Use similar code for <em>, removing other <em> code.
# 6. Replace <ul> code with simpler testing in one place.
# 7. Use h+= over h=$h..
# 8. Use a regex for header/list item

list=0
while IFS= read -r line; do

  # Replace _a_ and __a__ with <em> and <strong>
  while [[ $line =~ ^(.*)__(.+)__(.*) ]]; do
    printf -v line "%s<strong>%s</strong>%s" "${BASH_REMATCH[@]:1:3}"
  done

  while [[ $line =~ ^(.*)_(.+)_(.*) ]]; do
    printf -v line "%s<em>%s</em>%s" "${BASH_REMATCH[@]:1:3}"
  done

  # Open or close <ul> as needed.
  if ! (( list )) && [[ $line = '*'* ]]; then
    list=1 h+='<ul>'
  elif (( list )) && [[ $line != '*'* ]]; then
    list=0 h+='</ul>'
  fi

  # Wrap line in <li>|<h#>|<p>
  if [[ $line =~ ^\*\ (.+) ]]; then
    h+="<li>${BASH_REMATCH[1]}</li>"
  elif [[ $line =~ ^(#+)\ (.+) ]]; then
    t=h${#BASH_REMATCH[1]}
    h+="<$t>${BASH_REMATCH[2]}</$t>"
  else
    h+="<p>$line</p>"
  fi
done < "$1"

(( list )) && h+='</ul>'

echo "$h"

# vim:ts=2:sw=2:expandtab
