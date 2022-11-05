# (.x * .x + .y * .y | sqrt) as $dist
hypot(.x; .y) as $dist
| [[1, 10], [5, 5], [10, 1]]
| map(
    if ($dist <= first) then last else empty end
  )
| first // 0
