"use strict";
const log = console.log;
class Person {
    constructor(name) {
        this.name = name ?? "anonymous";
    }
    greeting(name) {
        return `Hello, ${name}`;
    }
    toString() {
        return `Hi, I'm ${this.name}`;
    }
}
const person = new Person();
log(new Person());
log(new Person("Alice"));
log(new Person("Bob"));
class Point {
    constructor(x = 2, y = 3) {
        this.x = 0;
        this.y = 0;
        this.x = x;
        this.y = y;
    }
    move(x, y) {
        this.x += x;
        this.y += y;
    }
}
class Circle extends Point {
    constructor(x, y, radius) {
        super(x, y);
        this.radius = 0;
        this.radius = radius;
    }
    move(x, y) {
        super.move(x, y);
    }
}
const circle = new Circle(1, 2, 4);
log(circle);
circle.move(1, 2);
log(circle);
class Octopus {
    constructor() {
        this.name = "name";
        this.legs = 8;
        // this is ok
        this.name = "wow";
        log(this.name);
    }
    setName(newName) {
        // errors cause this.name is readonly
        // this.name = newName;
    }
}
log(new Octopus());
class StaticClass {
    static doSomething() {
        log("doSomething");
    }
}
StaticClass.field = 123;
log(StaticClass.field);
class Operator {
    constructor(value) {
        this.value = value;
    }
    sum(value) {
        this.value += value;
        return this;
    }
    subtract(value) {
        this.value -= value;
        return this;
    }
    multiply(value) {
        this.value *= value;
        return this;
    }
    divide(value) {
        this.value /= value;
        return this;
    }
}
const op = new Operator(0);
log(op.sum(5));
log(op.sum(10).subtract(3).multiply(6).divide(3));
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    bark() {
        log("baw");
    }
}
const doggie = new Dog("john");
doggie.bark();
