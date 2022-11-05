.
# Store the number.
| .number as $n
# Select the sounds which divide the number.
| [[3, "Pling"], [5, "Plang"], [7, "Plong"]]
| map(
    if ($n % first == 0) then last else empty end
  )
# Format the result.
| add
| . // $n
 
