const canvas = document.getElementById('board');
const ctx = canvas.getContext('2d'); //2D그래픽 호출

// 캔버스 크기 계산
ctx.canvas.width = COLS * BLOCK_SIZE;
ctx.canvas.height = ROWS * BLOCK_SIZE;

// 컨텍스트에 크기조정 적용
ctx.scale(BLOCK_SIZE, BLOCK_SIZE); // 블럭 사이즈만큼 확대,축소

let board = new Board(ctx);
let currentGameId = null;

function play() {
  resetGame();

  if(currentGameId) {
    cancelAnimationFrame(currentGameId);
  }

  animate();
}

function resetGame() {
  board.reset();
  time = { start: performance.now(), elapsed: 0, level: 1000 };
}

function animate(now = 0) {
  time.elapsed = now - time.start;
  if(time.elapsed > time.level) {
    time.start = now;
    board.drop();
  }
  
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

  board.draw();
  currentGameId = requestAnimationFrame(animate);
}

const moves = {
  [KEY.LEFT]: p => ({ ...p, x: p.x - 1 }),
  [KEY.RIGHT]: p => ({ ...p, x: p.x + 1 }),
  [KEY.DOWN]: p => ({ ...p, y: p.y + 1 }),
  [KEY.SPACE]: p => ({ ...p, y: p.y + 1 }),
  [KEY.UP]: p => board.rotate(p)
};

document.addEventListener('keydown', event => {
  if (moves[event.key]) {
    // stop event burbling
    event.preventDefault();

    let p = moves[event.key](board.piece);

    if (event.key === KEY.SPACE) {
      while (board.valid(p)) {
        board.piece.move(p);
        p = moves[KEY.DOWN](board.piece);
      }
    } else if (board.valid(p)) {
      board.piece.move(p);
    }

    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

    board.piece.draw();
  }
});

