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
  console.table(board.grid);
}
