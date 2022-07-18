/*
 * Math
 */
"use strict";

import { title, subtitle, l } from "./util.js";

title("Math");
{
  subtitle("circular function");
  const degree = 90;
  const rad90 = (Math.PI * degree) / 180;
  const sin90 = Math.sin(rad90);
  l(sin90);

  subtitle("random");
  function getRandom(min, max) {
    return Math.random() * (max - min) + min;
  }

  l(getRandom(1, 5));
  l(getRandom(5, 10));
  l(getRandom(7, 19));

  subtitle("plus");
  const nums_plus = [0.4, 0.5, 0.9];
  for (const num of nums_plus) {
    l(num, Math.floor(num), Math.ceil(num), Math.round(num));
  }

  subtitle("minus");
  const nums_minus = [-0.4, -0.5, -0.9];
  for (const num of nums_minus) {
    l(num, Math.floor(num), Math.ceil(num), Math.round(num));
  }
}
