const positions = [
  {id: "#sa", x: 9, y: 9},
  {id: "#sb", x: 10, y: 9},
  {id: "#sc", x: 11, y: 9},
  {id: "#sd", x: 12, y: 9},
  {id: "#se", x: 13, y: 9},
];
const directions = [{x: -1, y: 0}, {y: 1, x: 0}, {x: 1, y: 0}, {y: -1, x: 0}]
let curDirection = 0;
let frame = 0;
const frameRate = 10;

function gameLoop() {
  drawSnake();
  if (!(frame++ % frameRate)) {
    moveSnake();
    maybeRotate();
  }
  requestAnimationFrame(gameLoop);
}

function maybeRotate () {
  if (
    (directions[curDirection].x && (positions[0].x == 0 || positions[0].x == 17))
    || (directions[curDirection].y && (positions[0].y == 0 || positions[0].y == 17))
  ) {
    curDirection = (curDirection + 1) % 4
  }
}

function moveSnake () {
  const tail = positions.pop()
  const head = positions[0]
  tail.x = head.x + directions[curDirection].x
  tail.y = head.y + directions[curDirection].y
  positions.unshift(tail);
}
  
function drawSnake () {
  for (let i = 0; i < 5; i++) {
    const p = positions[i];
    const segment = document.querySelector(p.id);
    segment.style.transform = `translate(${1 + p.x}00%, ${1 + p.y}00%)`;
    segment.style.background = `hsl(${370 - i * 25}, 70%, 50%)`;
  }
}

requestAnimationFrame(gameLoop);
