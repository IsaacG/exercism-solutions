const sounds = [[3, "Pling"], [5, "Plang"], [7, "Plong"]];

export function stormySounds(number) {
  return sounds
    .filter(([factor, sound])=> !(number % factor))
    .map(([factor, sound])=> sound)
    .join("") || number.toString()
}
