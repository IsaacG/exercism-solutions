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

def chunk:
  # Chunk the input string into blocks of 3.
  .strand as $s
  | [range(0; $s | length; 3)]
  | map($s[.:. + 3])
  ;

def encode_recursive:
  # Recursively encode codons.
  if . | length == 0 or proteins[.[0]] == "STOP" then
    []
  elif .[0] | in(proteins) | not then
    "Invalid codon\n" | halt_error
  else
    [proteins[.[0]]] + (.[1:] | encode_recursive)
  end
  ;

def encodeB:
  # Non-recursive encoding.
  [
    label $b
    | .[]
    | if proteins[.] == "STOP" then break $b else . end
  ]
  | if all(. | in(proteins)) then . else ("Invalid codon\n" | halt_error) end
  | map(proteins[.])
  ;

chunk | encode_recursive

