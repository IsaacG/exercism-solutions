.strand
| split("")
| if all([.] | inside("ACGT" | split("")))
  then .
  else "Invalid nucleotide in strand\n" | halt_error
  end
| reduce .[] as $i ({"A": 0, "C": 0, "G": 0, "T": 0}; .[$i] |= . + 1)
