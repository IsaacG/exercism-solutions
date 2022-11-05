def colors:
  ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
  ;

if .property == "colors"
then colors
else .input.color as $c | colors | index($c)
end
