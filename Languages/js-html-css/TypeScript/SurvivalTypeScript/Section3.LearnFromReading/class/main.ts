const log = console.log;

class Person {
  private name: string | undefined;

  constructor(name?: string) {
    this.name = name ?? "anonymous";
  }

  greeting(name: string): string {
    return `Hello, ${name}`;
  }

  toString(): string {
    return `Hi, I'm ${this.name}`;
  }
}

const person: Person = new Person();
log(new Person());
log(new Person("Alice"));
log(new Person("Bob"));

class Point {
  public x: number = 0;
  public y: number = 0;

  constructor(x: number = 2, y: number = 3) {
    this.x = x;
    this.y = y;
  }

  protected move(x: number, y: number) {
    this.x += x;
    this.y += y;
  }
}

class Circle extends Point {
  public radius: number = 0;

  constructor(x: number, y: number, radius: number) {
    super(x, y);
    this.radius = radius;
  }

  move(x: number, y: number) {
    super.move(x, y);
  }
}

const circle = new Circle(1, 2, 4);
log(circle);

circle.move(1, 2);
log(circle);

class Octopus {
  readonly name: string = "name";
  readonly legs = 8;

  constructor() {
    // this is ok
    this.name = "wow";
    log(this.name);
  }

  setName(newName: string) {
    // errors cause this.name is readonly
    // this.name = newName;
  }
}

log(new Octopus());

class StaticClass {
  static field: number = 123;

  static doSomething() {
    log("doSomething");
  }
}

log(StaticClass.field);

class Operator {
  protected value: number;

  public constructor(value: number) {
    this.value = value;
  }

  public sum(value: number): Operator {
    this.value += value;
    return this;
  }

  public subtract(value: number): Operator {
    this.value -= value;
    return this;
  }

  public multiply(value: number): Operator {
    this.value *= value;
    return this;
  }

  public divide(value: number): Operator {
    this.value /= value;
    return this;
  }
}

const op: Operator = new Operator(0);
log(op.sum(5));
log(op.sum(10).subtract(3).multiply(6).divide(3));

abstract class Animal {
  constructor(protected name: string) {}
  abstract bark(): void;
}

class Dog extends Animal {
  bark() {
    log("baw");
  }
}

const doggie = new Dog("john");
doggie.bark();
