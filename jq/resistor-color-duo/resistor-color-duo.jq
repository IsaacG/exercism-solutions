def colors:
  ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
  ;

.colors[0:2]
| reduce .[] as $i (0; . * 10 + (colors | index($i)))
