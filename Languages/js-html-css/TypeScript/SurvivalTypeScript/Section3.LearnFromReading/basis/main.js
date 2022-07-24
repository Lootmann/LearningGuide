"use strict";
const log = console.log;
const styles = {
    red: "\x1b[31m",
    blue: "\x1b[34m",
    yellow: "\x1b[33m",
    underilne: "\x1b[4m",
};
const title = (msg) => {
    const closure = styles.red + ">>>";
    const message = styles.yellow + msg;
    const content = styles.underilne + `${closure} ${message}` + "\x1b[0m";
    const line = "\n" + content + "\n";
    log(line);
};
title("hello");
{
    let x = 1;
    log(x);
    x++;
    log(x);
}
title("const, readonly");
{
    const c_nums = [1, 2, 3];
    log(c_nums);
    const ra_chars = ["a", "b", "c"];
    log(ra_chars);
    const obj = { a: 1 };
    obj.a = 2; // can change property
    log(obj);
    let obj1;
    obj1 = { b: 2 };
    log(obj1);
    log(obj1.b);
    // obj1.b = 4; // readonly
}
title("function");
{
    function print() {
        const x = 1;
        if (true) {
            const x = 2;
            log("inner:", x);
        }
        log("outer:", x);
    }
    print();
}
title("Primitive Types");
{
    // boxing: primitive -> Object
    const str = "abc";
    const strObjecst = new String(str);
    log(strObjecst.length);
    log(strObjecst.toUpperCase());
    // automatic boxing
    log("hello".length);
    log("hello".toUpperCase());
}
title("Boolean");
{
    log(true);
    log(false);
}
title("Number Type");
{
    log(110 * 1.1);
    log((110 * 11) / 10);
}
title("null");
{
    log(null);
    log(typeof null);
    log(undefined);
    log(typeof undefined);
}
title("JSON");
{
    log(JSON.stringify({ foo: undefined }));
    log(JSON.stringify({ foo: null }));
}
title("Symbol");
{
    const s1 = Symbol("foo");
    const s2 = Symbol("foo");
    log(s1, "___", s2);
}
title("BigInt");
{
    log(2n + BigInt(10));
    log(BigInt("9007199254740991"));
}
title("Type Coercion");
{
    log("'1' + 1 =", "1" + 1);
}
title("Union Type");
{
    const error_code = 400;
    log("error_code =", error_code);
    const s = "hello";
    log(s, typeof s);
    const n = [1, 2, 3];
    log(n, typeof n);
}
title("Discriminated Union");
{
    function printStatus(status) {
        switch (status.type) {
            case "InProgress":
                log(`Uploading ...: ${status.progress}%`);
                break;
            case "Success":
                log(`Uploaded Success !`, status);
                break;
            case "Failure":
                log(`Wrong Failure D:) ${status.error.message}`);
                break;
            default:
                log("wrong status", status);
        }
    }
    const status = { type: "InProgress", progress: 49 };
    printStatus(status);
}
title("Discriminated Union with variables");
{
    function toCSS(shape) {
        // discriminator
        const { type, color } = shape;
        switch (type) {
            case "circle":
                return {
                    background: color,
                    borderRadius: shape.radius,
                };
            case "square":
                return {
                    background: color,
                    width: shape.size,
                    height: shape.size,
                };
        }
    }
    const obstacle = { type: "square", color: "red", size: 100 };
    log(toCSS(obstacle));
}
title("Intersection");
{
    const me = { id: "a100", name: "Zundamochi" };
    log(me);
}
title("Object");
{
    const person = new Object();
    log(person);
    const calculator = {
        sum(a, b) {
            return a + b;
        },
    };
    log(calculator.sum(1, 2));
    const box = { width: 200, height: 150 };
    log(box);
}
title("Optional property");
{
    let size = {};
    log(size);
}
title("Index Signature");
{
    let obj;
    obj = { a: 1, b: 2 };
    obj.c = 3;
    obj["d"] = 4;
    log(obj);
}
title("Class");
{
    class Counter {
        constructor() {
            this.count = 0;
        }
        countUp() {
            this.count++;
        }
    }
    const counter = new Counter();
    log(counter);
}
title("Destructuring");
{
    const color = { r: 0, g: 122, b: 204, a: 1 };
    const { r, g, b, a } = color;
    log(r, g, b, a);
}
title("Destructuring Nested Object");
{
    const continent = {
        name: "North America",
        us: {
            name: "U.S.A",
            capitalCity: "Washington",
        },
    };
    const { us: { name, capitalCity }, } = continent;
    log(name, capitalCity);
}
title("Shorthand Property Names");
{
    const name = "pikachu";
    const no = 25;
    const genre = "mouse pokemon";
    const pikachu = { name, no, genre };
    log(pikachu);
}
title("Object for loop");
{
    const nums = { a: 1, b: 2, c: 3, d: 4 };
    for (const [key, value] of Object.entries(nums)) {
        log(key, value);
    }
    for (const key of Object.keys(nums)) {
        log(key);
    }
    for (const key of Object.values(nums)) {
        log(key);
    }
}
title("Array");
{
    let array = [1, 2, 3];
    log(array, array[0], array[1]);
    let nums = [1, 2, 3, 4];
    log(nums, nums[0], nums[1]);
    const all = array.concat(nums);
    log(all, all.length);
    const [one, , three] = nums;
    log(one, three);
    const [first, ...rest] = nums;
    log(first, rest);
}
title("Array for loop");
{
    const array = ["a", "b", "c", "d"];
    for (let i = 0; i < array.length; i++) {
        log(i, array[i]);
    }
    for (const value of array) {
        log(value);
    }
    array.forEach((value, i) => {
        log(value, i);
    });
    const arr1 = [...array, "e"];
    log(arr1);
}
title("Tuple");
{
    function t() {
        return [1, "ok", true];
    }
    const list = t();
    log(list);
}
title("Tuple Usage");
{
    async function take3() {
        return "take3";
    }
    async function take5() {
        return "take5";
    }
    // const tuple: [string, string] = await Promise.all([take3(), take5()]);
}
title("Enum");
{
    let Position;
    (function (Position) {
        Position[Position["Top"] = 0] = "Top";
        Position[Position["Right"] = 1] = "Right";
        Position[Position["Bottom"] = 2] = "Bottom";
        Position[Position["Left"] = 3] = "Left";
    })(Position || (Position = {}));
    log(Position);
}
title("Exception");
{
    try {
        throw new Error("Something Wrong");
    }
    catch (e) {
        if (e instanceof TypeError) {
            log(e);
        }
        else if (e instanceof RangeError) {
            log(e);
        }
        else if (e instanceof EvalError) {
            log(e);
        }
    }
    finally {
        log("* finished throw Error");
    }
}
title("never means that has not any type");
{
    function throwError() {
        throw new Error();
    }
}
