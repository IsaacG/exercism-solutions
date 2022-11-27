.
| (.limit + 1) as $limit
| reduce range(2; $limit) as $i (
    [range($limit)];
    if .[$i] then
      reduce range($i * 2; $limit; $i) as $j(.; .[$j] = false)
    else .
    end
  )
| .[2:]
| [.[] | select(.)]
