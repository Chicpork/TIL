class Piece {
    x;
    y;
    color;
    shape;
    ctx;

    constructor(ctx) {
        this.ctx = ctx;
        this.spawn();
        this.draw();
    }

    spawn() {
        let type = this.randomizeType(SHAPES.length);
        this.color = COLORS[type];
        this.shape = SHAPES[type];
        this.x = 3;
        this.y = 0;
    }

    draw() {
        this.ctx.fillStyle = this.color;
        this.shape.forEach((row, y) => {
            row.forEach((value, x) => {
                if (value > 0) {
                    this.ctx.fillRect(this.x + x, this.y + y, 1, 1);
                }
            });
        });
    }

    move(p) {
        this.x = p.x;
        this.y = p.y;

        this.shape = p.shape;
    }

    randomizeType(types) {
        return Math.floor(Math.random() * types);
    }
}