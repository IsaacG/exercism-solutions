// The number of minutes it takes to prepare a single layer.
const PREPARATION_MINUTES_PER_LAYER = 2;
const TOTAL_TIME = 40;

/**
 * Determines the number of minutes the lasagna still needs to remain in the
 * oven to be properly prepared.
 */
export function remainingMinutesInOven(actualMinutesInOven) {
  return TOTAL_TIME - actualMinutesInOven;
}

// Given a number of layers, determines the total preparation time.
export function preparationTimeInMinutes(numberOfLayers) {
  return PREPARATION_MINUTES_PER_LAYER * numberOfLayers;
}

/**
 * Calculates the total working time. That is, the time to prepare all the layers
 * of lasagna, and the time already spent in the oven.
 */
export function totalTimeInMinutes(numberOfLayers, actualMinutesInOven) {
  return preparationTimeInMinutes(numberOfLayers) + actualMinutesInOven;
}
