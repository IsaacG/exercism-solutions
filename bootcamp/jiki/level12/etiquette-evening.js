export function onGuestList(guestList, formalName) {
  let parts = formalName.split(" ").slice(1)
  let surname = parts.join(" ")
  return guestList.some((x) => x.split(" ").slice(-parts.length).join(" ") == surname)
}
