"use strict";

const title = (msg) => {
  console.log(`\n>>> ${msg}`);
};

let p = console.log;

title("array");
const arr = [];
const arr1 = [1, 2, 3];
const matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

p(arr);
p(arr1);
p(arr1[0]);
p(arr1[123]);
p(matrix);
p(matrix[1][2]);

title("length");
p(arr1.length);
p(matrix.length);

title("sparceArray");
const sparceArray = [1, , 3];
p(sparceArray);

title("Destructuring assignment");
const array = ["one", "two", "three"];
const [first, second, third] = array;
p(first, second, third);

title("Find Arrays");
const array1 = ["PHP", "Python", "Ruby"];

p(array1.indexOf("PHP"));
p(array1.indexOf("Python"));
p(array1.indexOf("Perl"));

title("Find By Objects");
const colors = [{ color: "red" }, { color: "green" }, { color: "blue" }];

const blueColor = colors.find((obj) => {
  return obj.color == "blue";
});

p(blueColor);
