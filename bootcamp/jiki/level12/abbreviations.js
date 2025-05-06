export function acronym(sentence) {
  return sentence.split(/[- ]/).map((x) => x.replace(/[^a-zA-Z]*/, "")[0]).join("").toUpperCase()
}
