/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(elapsed) {
  switch (elapsed) {
    case undefined:
      return 'You forgot to set the timer.'
    case 0:
      return 'Lasagna is done.'
    default:
      return 'Not done, please wait.'
  }
}

export function preparationTime(layers, perLayer = 2) {
  return layers.length * perLayer
}

export function quantities(layers) {
  let layerCount = {}
  for (const layer of layers) {
    layerCount[layer] = (layerCount[layer] ?? 0) + 1
  }
  console.log(layerCount)
  return {noodles: (layerCount.noodles ?? 0) * 50, sauce: (layerCount.sauce ?? 0) * 0.2}
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList.slice(-1)[0])
}

export function scaleRecipe(recipe, size) {
  let scaled = {}
  for (const i in recipe) {
    scaled[i] = recipe[i] * size / 2
  }
  return scaled
}
