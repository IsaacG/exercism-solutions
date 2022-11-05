def proteins:
  {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
  }
  ;

.strand as $s
| [range(0; $s | length; 3)]
| map($s[.:. + 3])
| [
 label $b
  | .[]
  | if proteins[.] == "STOP" then break $b else . end
]
| if all(. | in(proteins)) then . else ("Invalid codon\n" | halt_error) end
| map(proteins[.])
