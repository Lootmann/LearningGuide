// ./character_code.js
"use strict";

import { title, l } from "./util.js";

title("Code Point");
{
  const japanese = "あ";

  l(japanese.codePointAt(0));
  l(String.fromCodePoint(12354));
  l(String.fromCodePoint(0x3042));
}

title("Converts Code Units and Code Points");
{
  // code units
  const convertCodeUnits = (str) => {
    const codeUnits = [];
    for (let i = 0; i < str.length; i++) {
      codeUnits.push(str.charCodeAt(i).toString(16));
    }
    return codeUnits;
  };

  // code poitns
  // surrogate pair: 1つの文字(Emoji)を 2つの文字で表現する
  const convertCodePoints = (str) => {
    return Array.from(str).map((char) => {
      return char.codePointAt(0).toString(16);
    });
  };

  // main
  const str = "リンゴ🍎";
  l(convertCodeUnits(str));
  l(convertCodePoints(str));
}
