export function collatzSteps(number) {
  let step = 0
  while (number != 1) {
    step++
    if (number % 2 == 0) {
      number /= 2
    } else {
      number = number * 3 + 1
    }
  }
  return step
}
