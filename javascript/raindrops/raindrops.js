export const convert = (num) => {
  let out = []
  for (const [factor, sound] of [[3, 'Pling'], [5, 'Plang'], [7, 'Plong']]) {
    if (num % factor == 0) {
      out.push(sound)
    }
  }
  return out.join("") || `${num}`
};
