const map = {
  AUG: "Methionine",
  UUU: "Phenylalanine",
  UUC: "Phenylalanine",
  UUA: "Leucine",
  UUG: "Leucine",
  UCA: "Serine",
  UCC: "Serine",
  UCG: "Serine",
  UCU: "Serine",
  UAC: "Tyrosine",
  UAU: "Tyrosine",
  UGC: "Cysteine",
  UGU: "Cysteine",
  UGG: "Tryptophan",
  UAA: "STOP",
  UAG: "STOP",
  UGA: "STOP",
}

export function translateRna(rna) {
  const out = []
  for (let i = 0; i < rna.length; i += 3) {
    const acid = map[rna.slice(i, i + 3)];
    if (acid === "STOP") 
      break;
    out.push(acid)
  }
  return out
}
