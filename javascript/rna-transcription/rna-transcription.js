const map = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'};
export const toRna = (dna) => dna.replaceAll(/./g, (x) => map[x]);
