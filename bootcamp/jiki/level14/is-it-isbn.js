export function isValidIsbn(isbn) {
  const numbers = [...isbn.replaceAll("-", "")];
  if (numbers.length != 10) {
    return false;
  }
  if (numbers[9] == "X") {
    numbers[9] = "10"
  }
  const vals = numbers.map(x => Number(x))
  if (vals.some(x => Number.isNaN(x))) {
    return false
  }
  const sum = vals.reduce(([mult, sum], i) => [mult - 1, sum + mult * i], [10, 0]);
  return sum[1] % 11 == 0;
}
