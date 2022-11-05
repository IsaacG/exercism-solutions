# Shopping list name.
.name,

# Number of items on the list.
(.ingredients | length),

# Quantity of sugar needed.
(.ingredients[] | select(.item == "sugar") | .amount.quantity),

# Map ingredients to substitute ingredients.
(
  [
    (.ingredients  + ."optional ingredients")[]
    | select(has("substitute"))
    | {(.item): .substitute}
  ]
  | add
)
