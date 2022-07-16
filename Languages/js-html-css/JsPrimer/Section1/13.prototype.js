"use strict";

const o = {};
console.log(o.toString());
console.log(typeof Object.prototype.toString);

const obj = {
  key: "value",
};

// true
console.log(obj.toString === Object.prototype.toString);
