const canvas = document.getElementById('board');
const ctx = canvas.getContext('2d'); //2D그래픽 호출

// 캔버스 크기 계산
ctx.canvas.width = COLS * BLOCK_SIZE;
ctx.canvas.height = ROWS * BLOCK_SIZE;

// 컨텍스트에 크기조정 적용
ctx.scale(BLOCK_SIZE, BLOCK_SIZE); // 블럭 사이즈만큼 확대,축소

let board = new Board();

function play() {
  board.reset();
  let piece = new Piece(ctx);
  piece.draw();

  board.piece = piece;
}

const moves = {
  [KEY.LEFT]: p => ({ ...p, x: p.x - 1 }),
  [KEY.RIGHT]: p => ({ ...p, x: p.x + 1 }),
  [KEY.DOWN]: p => ({ ...p, y: p.y + 1 }),
  [KEY.SPACE]: p => ({ ...p, y: p.y + 1 })
}

document.addEventListener('keydown', event => {
  if (moves[event.keyCode]) {
    // stop event burbling
    event.preventDefault();

    let p = moves[event.keyCode](board.piece);

    if (event.keyCode === KEY.SPACE) {
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