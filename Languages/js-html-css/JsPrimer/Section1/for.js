"use strict";

const log = console.log;

const title = (msg) => console.log(`\n>>> ${msg}`);

const arr = [1, 2, 3, 4, 5];
title("Array");
log(arr);

title("forEach");

arr.forEach((currentValue, index, array) => {
  console.log(currentValue, index, array);
});

title("map");
const mapArray = arr.map((currentValue, index, array) => {
  return currentValue * (index + 1);
});

log(mapArray);

title("filter");
const filterArray = arr.filter((currentValue, index, array) => {
  return currentValue % 2 == 1;
});

log(filterArray);

title("reduce");
const reduceNum = arr.reduce((acc, cur, i, array) => {
  return acc + cur;
}, 0);
log(reduceNum);

title("Array-Like");
function myFunc() {
  // keyword - arguments
  log(arguments[0]);
  log(arguments[1]);
  log(arguments[2]);
  log(typeof arguments.forEach);
}

myFunc("a", "b", "c");

title("Method Chain");
const arr1 = ["a"].concat("b").concat("c");
log(arr1);

title("Higher-Order Function");
const ECMAScriptVersions = [
  { name: "ECMAScript 1", year: 1997 },
  { name: "ECMAScript 2", year: 1998 },
  { name: "ECMAScript 3", year: 1999 },
  { name: "ECMAScript 5", year: 2009 },
  { name: "ECMAScript 5.1", year: 2011 },
  { name: "ECMAScript 2015", year: 2015 },
  { name: "ECMAScript 2016", year: 2016 },
  { name: "ECMAScript 2017", year: 2017 },
];
// メソッドチェーンで必要な加工処理を並べている
const versionNames = ECMAScriptVersions
  // 2000年以下のデータに絞り込み
  .filter((ECMAScript) => ECMAScript.year <= 2000)
  // それぞれの要素から`name`プロパティを取り出す
  .map((ECMAScript) => ECMAScript.name);
console.log(versionNames);
