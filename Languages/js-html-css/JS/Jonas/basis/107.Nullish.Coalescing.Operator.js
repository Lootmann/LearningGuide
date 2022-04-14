"use strict";

const test = {
  numbers: [1, 2, 3, 4, 5],
  strings: ["a", "b", "c", "d", "e"],
};

const n = test.num || 999;
console.log(n);

const num = test.num ?? 999;
console.log(num);
