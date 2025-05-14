export function hammingDistance(strand1, strand2) {
  return [...strand1].reduce((sum, cur, idx) => sum + (cur !== strand2[idx]), 0)
}
