export function needsLicense(kind) {
  return ["car", "truck"].includes(kind)
}

export function chooseVehicle(option1, option2) {
  return (option1 < option2 ? option1 : option2) + " is clearly the better choice."
}

export function calculateResellPrice(originalPrice, age) {
  if (age < 3) {
    return originalPrice * 0.80
  } else if (age < 10) {
    return originalPrice * 0.70
  } else {
    return originalPrice * 0.50
  }
}
