const map = {G: "C", C: "G", T: "A", A: "U"}

export function dnaToRna(dna) {
  return dna.replace(/./g, x => map[x])
}
