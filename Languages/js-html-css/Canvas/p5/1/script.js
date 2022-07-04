WIDTH = 750;
HEIGHT = 650;

let Color = {
  white: [255, 255, 255],
  red: [255, 0, 0],
  salmon: [255, 178, 102],
  pink: [255, 102, 178],
  lightgreen: [178, 255, 102],
  smokeblud: [102, 178, 255],
  lightblue: [102, 102, 255],
  green: [0, 255, 0],
  blue: [0, 0, 255],
  grey: [128, 128, 128],
  black: [0, 0, 0],
};

function getRandomColor() {
  return Color[random(Object.keys(Color))];
}

function getRandomSign() {
  return random([+1, -1]);
}

class Ball {
  constructor(x = 0, y = 0, diameter = 50, velocity = 3) {
    this.x = x == 0 ? diameter / 2 : x;
    this.y = y == 0 ? diameter / 2 : y;
    this.diameter = diameter;

    this.velocity = velocity;
    this.dx = this.velocity * getRandomSign();
    this.dy = this.velocity * getRandomSign();
    this.color = getRandomColor();
  }

  fluctuation() {
    return random([-0.2, -0.1, 0, 0.1, 0.2]);
  }

  collision() {
    let is_collision = false;

    // horizontal -> this.x
    if (this.x - this.diameter / 2 <= 0) {
      this.dx = +this.velocity + this.fluctuation();
      is_collision = true;
    }
    if (WIDTH <= this.x + this.diameter / 2) {
      this.dx = -this.velocity + this.fluctuation();
      is_collision = true;
    }

    // vertical -> this.y
    if (this.y - this.diameter / 2 <= 0) {
      this.dy = +this.velocity + this.fluctuation();
      is_collision = true;
    }

    if (HEIGHT <= this.y + this.diameter / 2) {
      this.dy = -this.velocity + this.fluctuation();
      is_collision = true;
    }

    if (is_collision) this.color = getRandomColor();
  }

  move() {
    this.collision();
    this.x += this.dx;
    this.y += this.dy;
  }

  out() {
    fill(color(this.color));
    circle(this.x, this.y, this.diameter);
  }
}

const randomPos = (limit, diameter) => {
  return random(diameter, limit - diameter);
};

const balls = [];

function setup() {
  createCanvas(WIDTH, HEIGHT);
  background(Color.grey);
  // noLoop();

  for (let i = 0; i < 200; i++) {
    // balls.push(new Ball(randomPos(WIDTH, 50), randomPos(HEIGHT, 50), 50));
    balls.push(new Ball(WIDTH * 2, HEIGHT * 2, 35));
  }
}

function draw() {
  // clear background color
  background(Color.grey);

  for (const ball of balls) {
    ball.move();
    ball.out();
  }
}
