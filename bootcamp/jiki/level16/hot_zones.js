// Ball initial speed
const speed = 0.5;

class Paddle {
  constructor(width) {
    this.obj = document.querySelector("#paddle")
    this.horizRadius = this.obj.getBoundingClientRect().width / 2;
    // Compute the left edge of the bounding box.
    const g = document.querySelector("#game").getBoundingClientRect();
    this.maxLeft = g.width - this.horizRadius;
  }
  paddlePoint(point) {
    const details = {}
    const p = this.obj.getBoundingClientRect();
    details.hits = p.left <= point && point <= p.right;
    if (!details.hits) {
      return details;
    }
    const paddleCenter = (p.left + p.right) / 2;
    details.edgePercent = Math.abs(point - paddleCenter) / this.horizRadius;
    if (point > paddleCenter) {
      details.paddleSide = 1;
    } else {
      details.paddleSide = -1;
    }
    console.log(`Distance towards edge: ${100*details.edgePercent}`)
    return details;
  }
  move(e) {
    let centerPx = e.clientX - document.querySelector("#game").getBoundingClientRect().left;
    centerPx = Math.min(centerPx, this.maxLeft)
    centerPx = Math.max(centerPx, this.horizRadius)
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
    if (this.ball_x <= this.radius || this.ball_x >= 100 - this.radius) {
      this.dx *= -1;
    }
    if (this.ball_y <= this.radius) {
      this.dy *= -1;
    }
    if (this.ball_y + this.radius >= 96 && this.ball_y < 96) {
      const impact = this.paddle.paddlePoint(this.center);
      if (!impact.hits) return;
      console.log(`Edge percentage ${impact.edgePercent}`);
      this.dy *= (impact.edgePercent + 0.5);
      this.dy = -1 * Math.min(1.5, Math.max(0.5, this.dy));
      let direction = 0;
      if (impact.edgePercent >= 0.50) {
        direction = impact.paddleSide;
      } else {
        direction = Math.sign(this.dx);
      }
      this.dx = direction * impact.edgePercent;
      console.log(impact);
    }
  }

  get center() {
    const b = this.obj.getBoundingClientRect();
    return b.left + b.width / 2;
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
    if (this.ball.ball_y >= 96) {
      this.alive = false;
    }
    if (this.ball.ball_y + this.ball.radius >= 100) {
      document.querySelector("#game").style.background = "darkred";
      document.querySelector("#paddle").style.opacity = "0.2";
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
