export function dayRate(ratePerHour) { return ratePerHour * 8 }

export function daysInBudget(budget, ratePerHour) {
  return Math.floor(budget / dayRate(ratePerHour))
}

export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  let remainder = numDays % 22
  let discounted = (numDays - remainder)
  return Math.ceil(dayRate(ratePerHour) * (remainder + discounted * (1 - discount)))
}
