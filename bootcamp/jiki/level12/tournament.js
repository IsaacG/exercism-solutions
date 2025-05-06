function played(data, team) {
  if (!(team in data)) {
    data[team] = {played: 0, tie: 0, win: 0, lose: 0, name: team}
  }
  data[team].played++
}

export function tournamentTally(data) {
  let tally = {}
  let out = "Team                           | MP |  W |  D |  L |  P"
  if (!data) {
    return out
  }
  
  for (const line of data.split("\n")) {
    let parts = line.split(";")
    let t1 = parts[0]
    let t2 = parts[1]
    if (parts[2] === "loss") {
      let t3 = t2
      t2 = t1
      t1 = t3
    }
    played(tally, t1)
    played(tally, t2)
    
    if (parts[2] === "draw") {
      tally[t1].tie++
      tally[t2].tie++
    } else {
      tally[t1].win++
      tally[t2].lose++
    }
  }
  for (const team of Object.values(tally)) {
    team.points = team.tie + 3 * team.win
  }
  log(data)
  log(tally)
  for (const team of sort(Object.values(tally), "points", "name")) {
    let parts = [
      `${team.name}`.padEnd(30, " "),
      `${team.played}`.padStart(2, " "),
      `${team.win}`.padStart(2, " "),
      `${team.tie}`.padStart(2, " "),
      `${team.lose}`.padStart(2, " "),
      `${team.points}`.padStart(2, " "),
    ]
    out += "\n" + parts.join(" | ")
  }
  return out
}

// We've provided you this function. You might be interested to
// explore how it works, but you don't need to understand it
// or change it. Read the instructions to see how to use it!
function sort(data, pointsKey, nameKey) {
  return data.sort((a, b) => {
    const pointsComparison = b[pointsKey] - a[pointsKey]
    if (pointsComparison != 0) {
      return pointsComparison
    }
    return a[nameKey].localeCompare(b[nameKey])
  })
}
