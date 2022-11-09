def colors: ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"];

def format($units):
  if . % 1000 != 0
  then {value: ., unit: $units[0]}
  else . / 1000 | format($units[1:])
  end
  ;

def format: format(["ohms", "kiloohms", "megaohms", "gigaohms"]);

.colors
| (. | last) as $exponent
| reduce .[0:2][] as $i (0; . * 10 + (colors | index($i)))
| . * pow(10; (colors | index($exponent)))
| format
