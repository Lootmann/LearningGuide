"use strict";

function print(...elems) {
  console.log(...elems);
}

const p = print;

// test date
const test = {
  numbers: [1, 2, 3, 4, 5],
  strings: ["A", "G", "K", "Z"],
  sat: { open: 10, close: 23 },
  sun: { open: 8, close: 24 },
};

// spread operators
const arr = [1, 2, ...[3, 4]];
p(arr);

const [a, b, ...others] = test.numbers;
p(a, b, others);

// error
// const [...k, l, m] = test.numbers;

// REST Pattern
const add = function (...nums) {
  let sum = 0;
  for (let i = 0; i < nums.length; ++i) {
    sum += nums[i];
  }
  p("sum(", nums, ") =", sum);
};

add(1);
add(2, 2);
add(3, 3, 3);
add(4, 4, 4, 4);
add(5, 5, 5, 5, 5);
