def bottles($i):
  if $i > 1
  then "\($i) bottles"
  elif $i == 1
  then "1 bottle"
  else "No more bottles"
  end
  ;

def verse($i):
  (if $i == 1 then "it" else "one" end) as $article
  | [
    "\(bottles($i)) of beer on the wall, \(bottles($i) | ascii_downcase) of beer.",
    if $i > 0
    then "Take \($article) down and pass it around, \(bottles($i - 1) | ascii_downcase) of beer on the wall."
    else "Go to the store and buy some more, 99 bottles of beer on the wall."
    end,
    ""
  ];

[range(.startBottles; .startBottles - .takeDown; -1) | verse(.)]
| add
| .[:-1]
