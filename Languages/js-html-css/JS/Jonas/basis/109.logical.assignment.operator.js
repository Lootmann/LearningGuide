"use strict";
const print = console.log;

const test = {
  numbers: [1, 2, 3, 4, 5],
  strings: ["a", "b", "c", "d", "e"],
  names: ["ash", "bjorn", "casy", "dull"],
  guest: false,
};

test.guest ??= true; // guest is NOT null
test.superuser ??= false; // superuser is null

test.owner_message &&= "<ANONYMOUS>";
test.owner_retry &&= "<ANONYMOUS>";

print(test);

test.owner_message ??= "<ANONYMOUS>";
test.owner_retry ??= "<ANONYMOUS>";

print(test);
