/**
 * @type {CanvasRenderingContext2D}
 */

// const args
class Const {
  static Field = {
    x: {
      min: 0,
      max: 30 * 10,
    },
    y: {
      min: 0,
      max: 30 * 20,
    },
  };
};

function getCanvas() {
  return document.getElementById("canvas");
}

function getCanvasContext(canvas) {
  canvas.width = Const.Field.x.max;
  canvas.height = Const.Field.y.max
  return canvas.getContext('2d');
}

class Mino {
  constructor(x, y, color) {
    this.dx = 30;
    this.x = x;
    this.y = y;
    this.w = this.h = 30;
    this.color = color;
  }

  right() {
    this.x += this.dx;
  }

  left() {
    this.x -= this.dx;
  }

  down() {
    this.y += this.dx;
  }

  canMoveXLeft() {
    return this.x !== Const.Field.x.min;
  }

  canMoveXRight() {
    return this.x !== Const.Field.x.max - 30;
  }

};

function keyevent(keyEvent, mino) {
  switch (keyEvent.key) {
    case 'ArrowUp':
      console.log("Rotation");
      break;

    case 'ArrowDown':
      mino.down();
      break;

    case 'ArrowLeft':
      if (mino.canMoveXLeft())
        mino.left();
      break;

    case 'ArrowRight':
      if (mino.canMoveXRight())
        mino.right();
      break;
  }
}



class Field {
  constructor(ctx) {
    this.ctx = ctx;
    this.mino = null;
    this.is_live = false;
  }

  set(mino) {
    this.is_live = true;
    this.mino = mino;
  }

  background() {
    this.ctx.fillStyle = "black";
    this.ctx.fillRect(0, 0, Const.Field.x.max, Const.Field.y.max);
  }

  draw() {
    this.ctx.fillStyle = this.mino.color;
    this.ctx.fillRect(this.mino.x, this.mino.y, this.mino.w, this.mino.h);
  }

  freeFall() {
    this.mino.down();
  }

  isDieMino() {
    if (this.mino.y === Const.Field.y.max)
      this.is_live = false;
  }
};

const canvas = getCanvas();
const ctx = getCanvasContext(canvas);
const field = new Field(ctx);

let timeCount = 0;

const gameId = setInterval(() => {
  if (!field.is_live) {
    console.log("ye");
    let mino = new Mino(Const.Field.x.min, Const.Field.y.min, "orange");
    document.body.addEventListener("keydown", (event) => keyevent(event, mino));
    field.set(mino);
  }

  field.background();
  field.draw();
  field.isDieMino();
  if (timeCount > 60) {
    field.freeFall();
    timeCount = 0;
  }
  timeCount++;
}, 1 / 60);