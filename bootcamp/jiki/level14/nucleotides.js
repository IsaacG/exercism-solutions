export function countNucleotides(dna) {
  const count = {A: 0, C: 0, G: 0, T: 0};
  [...dna].forEach((x) => count[x] += 1)
  if (Object.values(count).some(Number.isNaN)) return false;
  return count
}
