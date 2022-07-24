/*
 * All functions should have specify types.
 **/
const log = console.log;

function increment(num: number): number {
  return num + 1;
}

log(increment(1));

const factorial = function fact(n: number): number {
  if (n <= 1) return 1;
  return n * fact(n - 1);
};

log(factorial(5));

const arrow_increment = (n: number) => {
  return n + 1;
};

// arrow type
type Func = (num: number) => number;

const increment_with_type: Func = (num: number) => num + 1;
log(increment_with_type(10));

const nums = [1, 2, 3, 4];
const even = nums.filter((n) => n % 2 === 0);
log(even);

// function is just Object
function hello() {
  return "hello world";
}

hello.prop = 123;

log(hello);

// pass by value, pass by reference
function change(n: number) {
  log(n);
  n = 2;
}

let n = 1;

log(n);
change(n);
log(n);

type MyObj = { a: number; b: number };
function changeObj(obj: MyObj) {
  obj.a = 3;
}

let obj: MyObj = { a: 1, b: 2 };

log(obj);
changeObj(obj);
log(obj);

function greeting(person?: string) {
  log(person);
}

greeting();
greeting("hello");

function helloWorld(person?: string) {
  person ??= "anonymouse";
  return "Hello, " + person;
}

log(helloWorld());
log(helloWorld("guest"));

function func(...params: Array<number>) {
  log(params);
}

func(1, 2, 3);

function MyMax(...params: Array<number>) {
  if (params.length == 0) throw new Error("suck");

  let min = params[0] ?? 0;
  for (const value of params) {
    if (min > value) min = value;
  }
  return min;
}

log(MyMax(7, 2, 11, 5, 4));

class Male {
  private name: string;

  public constructor(name: string) {
    this.name = name;
  }

  public toString(): string {
    return `Monsieur ${this.name}`;
  }
}

const male = new Male("Lyo");
log(male.toString());

type Options = {
  x?: number;
  y?: number;
  z?: number;
};
function ff({ x = 0, y = 0, z = 0 }: Options = {}) {
  log(x, y, z);
}

ff({ x: 1, y: 2, z: 3 });
ff();

class Animal {}
class Duck extends Animal {}

function isDuck(animal: Animal): animal is Duck {
  if (!(animal instanceof Duck)) throw new Error("YOU Frog");
  return true;
}

const duck = new Duck();
log(isDuck(duck));
