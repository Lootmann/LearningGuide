"use strict";

const obj = {
  key: "value",
};

console.dir(obj);
console.dir(new Object());

obj.key1 = "value1";
console.dir(obj);

const newObj = Object.freeze({ key: "value" });
// raise Error because Object is freezed
// newObj.key1 = "new key";
console.log(newObj);

const languages = {
  ja: "Japanese",
  en: "English",
};

const { ja, en } = languages;
console.log(ja, en);
