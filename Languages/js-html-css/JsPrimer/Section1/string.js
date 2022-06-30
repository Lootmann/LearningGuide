"use strict";

const l = console.log;
const title = (msg) => {
  console.log(`\n>>> ${msg}`);
};

title("string");
const str = "コンニチハ";

l(str.at(0));
l(str.at(1));
l(str.at(-2));
l(str.at(-1));

title("UniCode CodeUnit");
for (const ch of str) {
  l(ch, ch.charCodeAt(), ch.charCodeAt().toString(16));
}

l(String.fromCharCode(0x30a2, 0x30aa, 0x30a4));

title("split to array");
l("why,hello,there,friend?".split(","));
l("why,hello,there,friend?".split(",").join("-"));

title("string methods");
const str1 = "abcdefghijk";
l(str1.slice(1));
l(str1.slice(1, 5));
l(str1.slice(-1));

// depricated
// l(str1.substring(1));
const url = "https://example.com?param=1";
const indexOfQuery = url.indexOf("?");
const queryString = url.slice(indexOfQuery);
l(queryString);
