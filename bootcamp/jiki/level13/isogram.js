export function isIsogram(string) {
  const seen = new Set();
  if (!string.length) { return true }
  for (const i of string.toLowerCase().match(/[a-z]/g)) {
    if (seen.has(i)) { return false }
    seen.add(i)
  }
  return true
}
