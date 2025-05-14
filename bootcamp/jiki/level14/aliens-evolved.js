export function playGame() {
  const aliens = getStartingAliens();
  const counts = aliens[0].map((_, col) => aliens.reduce((sum, i, row) => sum + i[col], 0));
  
  let remaining = counts.reduce((sum, i) => sum + i)
  let position = 0;
  let direction = 1;
  
  while (remaining) {
    if (counts[position]) {
      shoot()
      counts[position]--
      remaining--
    }
    position += direction
    if (direction == 1) {
      moveRight()
    } else {
      moveLeft()
    }
    if (position == 0 || position == 10) {
      direction *= -1
    }
  }
}
