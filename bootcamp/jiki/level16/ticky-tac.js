function buildWinPatterns() {
  const patterns = []
  let transform = [((i, j) => [i, j]), ((i, j) => [j, i])]
  transform.forEach(f => {
    [0, 1, 2].forEach(i => {
      pattern = [];
      [0, 1, 2].forEach(j => pattern.push(f(i, j)));
      patterns.push(pattern);
    })
  })
  transform = [i => [i, i], i => [i, 2 - i]]
  transform.forEach(f => {
    pattern = [];
    [0, 1, 2].forEach(i => pattern.push(f(i)));
    patterns.push(pattern);
  })
  return patterns
}

function buildGame () {
  const game = {
    turn: "O",
    patterns: buildWinPatterns(),
    board: document.querySelector("#game"),
    done: false,
  };
  const square = {};
  for (let i = 0; i < 9; i++) {
    square[`s${i}`] = {
      x: i % 3,
      y: Math.floor(i / 3),
      obj: document.querySelector(`#s${i}`),
      id: `s${i}`,
      value: null,
    };
  }
  game.square = square;
  
  game.rows = [];
  for (let y = 0; y < 3; y++) {
    game.rows[y] = []
    for (let x = 0; x < 3; x++) {
      game.rows[y].push(game.square[`s${x + y * 3}`]);
    }
  }
  
  game.get = e => game.square[e.target.id];
  game.over = () => Object.values(square).every(s => s.value !== null);
  game.won = () => game.patterns.some(p => p.every(([x, y]) => game.rows[x][y].value == game.turn));
  return game;
}

function gameWon(game) {
  game.patterns.filter(
    p => p.every(([x, y]) => game.rows[x][y].value == game.turn)
  )
  .flat()
  .forEach(([x, y]) => {
    game.rows[x][y].obj.style.background = "purple";
    game.rows[x][y].obj.style.color = "white";
  })
}

function gameTie(game) {
  game.board.style.background = "#ddd";
  Object.values(game.square).forEach(s => s.obj.style.color = "#666");
}

function click (e) {
  const square = game.get(e);
  if (game.done) return;
  if (square.value !== null) return;
  
  square.value = game.turn;
  square.obj.innerHTML = game.turn;

  if (game.won()) {
    gameWon(game);
    game.done = true;
  } else if (game.over()) {
    gameTie(game);
    game.done = true;
  }
  
  game.turn = {X: "O", O: "X"}[game.turn];
}

const game = buildGame();
document.querySelectorAll(".square").forEach(s => s.addEventListener("mousedown", click));
