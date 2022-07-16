"use strict";

const l = console.log;
const title = (msg) => {
  console.log();
  console.log(`\x1b[4m\x1b[31m>>> \x1b[35m${msg}\x1b[0m\n`);
};

title("string");
{
  const str = "コンニチハ";

  l(str.at(0));
  l(str.at(1));
  l(str.at(-2));
  l(str.at(-1));
}

title("UniCode CodeUnit");
{
  const str = "コンニチハ";
  for (const ch of str) {
    l(ch, ch.charCodeAt(), ch.charCodeAt().toString(16));
  }

  l(String.fromCharCode(0x30a2, 0x30aa, 0x30a4));
}

title("split to array");
{
  l("why,hello,there,friend?".split(","));
  l("why,hello,there,friend?".split(",").join("-"));
}

title("string methods");
{
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
}

title("Regular Expression Object");
{
  const patternA = /a+/;
  const patternB = new RegExp("a+");

  const string = "bbsasbb";
  l(string, patternA, string.search(patternA));
  l(string, patternB, string.search(patternB));
  l(string, string.search(/b{2}/));
}
