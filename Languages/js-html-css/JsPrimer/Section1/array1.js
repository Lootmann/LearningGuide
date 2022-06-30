"use strict";
const title = (msg) => {
  console.log(`\n>>> ${msg}`);
};
const log = console.log;

title("Stack");
const array = ["a", "b", "c"];
array.push("d");

log(array.pop());

title("Queue");
array.unshift("z");
log(array);

log(array.shift());
log(array);

title("concat");
log(array);
log(array.concat(["d", "e"]));
log(array.concat("f"));

title("spread");
log(["x", "y", "x", ...array]);

title("flatten");
const nested = [[[[1], 2], 3], 4];
log(nested.flat());
log(nested.flat(1));
log(nested.flat(2));
log(nested.flat(3));
log(nested.flat(Infinity));

title("Array.length = 0");
const arr = [1, 2, 3];
log(arr);
arr.length = 0;
log(arr);
