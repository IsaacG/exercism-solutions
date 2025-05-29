let dx = -0.5;
let dy = -0.5;
let ball_x = 50;
let ball_y = 100;

function gameLoop() {
  ball_x += dx;
  ball_y += dy;
  if (ball_x == 2 || ball_x == 98) dx *= -1;
  if (ball_y == 4 || ball_y == 100) dy *= -1;
  const ball = document.querySelector("#ball");
  ball.style.top = `${ball_y}%`;
  ball.style.left = `${ball_x}%`;
  requestAnimationFrame(gameLoop);
}

requestAnimationFrame(gameLoop);
