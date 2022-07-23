"use strict";
/*
 * All functions should have specify types.
 **/
const log = console.log;
function increment(num) {
    return num + 1;
}
log(increment(1));
const factorial = function fact(n) {
    if (n <= 1)
        return 1;
    return n * fact(n - 1);
};
log(factorial(5));
const arrow_increment = (n) => {
    return n + 1;
};
const increment_with_type = (num) => num + 1;
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
function change(n) {
    log(n);
    n = 2;
}
let n = 1;
log(n);
change(n);
log(n);
function changeObj(obj) {
    obj.a = 3;
}
let obj = { a: 1, b: 2 };
log(obj);
changeObj(obj);
log(obj);
function greeting(person) {
    log(person);
}
greeting();
greeting("hello");
function helloWorld(person) {
    person ?? (person = "anonymouse");
    return "Hello, " + person;
}
log(helloWorld());
log(helloWorld("guest"));
function func(...params) {
    log(params);
}
func(1, 2, 3);
function MyMax(...params) {
    if (params.length == 0)
        throw new Error("suck");
    let min = params[0] ?? 0;
    for (const value of params) {
        if (min > value)
            min = value;
    }
    return min;
}
log(MyMax(7, 2, 11, 5, 4));
class Male {
    constructor(name) {
        this.name = name;
    }
    toString() {
        return `Monsieur ${this.name}`;
    }
}
const male = new Male("Lyo");
log(male.toString());
function ff({ x = 0, y = 0, z = 0 } = {}) {
    log(x, y, z);
}
ff({ x: 1, y: 2, z: 3 });
ff();
class Animal {
}
class Duck extends Animal {
}
function isDuck(animal) {
    if (!(animal instanceof Duck))
        throw new Error("YOU Frog");
    return true;
}
const duck = new Duck();
log(isDuck(duck));
