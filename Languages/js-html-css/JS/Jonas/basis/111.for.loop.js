"use strict";

function title(msg) {
  console.log(`\n>>> ${msg}`);
}

title("create new Array");
let nums = Array.from(Array(10), (_, i) => 20 - i);
console.log(nums);

title("");
for (const num of nums) {
  console.log(num);
}

title("entries() Like Enumerate");
for (const num of nums.entries()) {
  console.log(num, num[0], num[1]);
}

title("[].entries()");
console.log([...nums.entries()]);
