// Ball speed
const speed = 1;

class Paddle {
  constructor(width) {
    this.obj = document.querySelector("#paddle")
    this.widthPx = this.obj.getBoundingClientRect().width;
    // Compute the left edge of the bounding box.
    const g = document.querySelector("#game").getBoundingClientRect();
    this.maxLeft = g.right - this.widthPx;
  }
  covers(ball) {
    const b = ball.obj.getBoundingClientRect();
    const b_center = b.left + b.width / 2;
    const p = this.obj.getBoundingClientRect();
    return p.left <= b_center && b_center <= p.right;
  }
  move(e) {
    let centerPx = e.clientX - this.widthPx / 2
    centerPx = Math.min(centerPx, this.maxLeft)
    centerPx = Math.max(centerPx, 0)
    this.obj.style.left = centerPx + "px";
  }
}

class Ball {
  constructor(paddle) {
    this.dx = -1 * speed;
    this.dy = -1 * speed;
    this.ball_x = 50;
    this.radius = 2;
    this.ball_y = 100 - this.radius - 4;
    this.obj = document.querySelector("#ball")
    this.paddle = paddle
  }
  move() {
    this.ball_x += this.dx;
    this.ball_y += this.dy;    
    this.obj.style.top = `${this.ball_y}%`;
    this.obj.style.left = `${this.ball_x}%`;
  }
  bounce() {
    if (this.ball_x == this.radius || this.ball_x == 100 - this.radius) {
      this.dx *= -1;
    }
    if (this.ball_y == this.radius || (this.ball_y == 94 && this.paddle.covers(this))) {
      this.dy *= -1;
    }
  }
}
class Game {
  constructor() {
    this.paddle = new Paddle();
    this.ball = new Ball(this.paddle);
    this.alive = true;
  }

  loop() {
    this.ball.move();
    this.ball.bounce();
    if (this.ball.ball_y + this.ball.radius == 100) {
      document.querySelector("#game").style.background = "darkred";
      document.querySelector("#paddle").style.opacity = "0.2";
      this.alive = false;
    } else {
      requestAnimationFrame(() => this.loop());
    }
  }
  paddle_move(e) {
    if (this.alive) {
      this.paddle.move(e);
    }
  }
}

const game = new Game();
document.querySelector("#game").addEventListener("mousemove", (e) => {game.paddle_move(e)});
requestAnimationFrame(() => game.loop());
