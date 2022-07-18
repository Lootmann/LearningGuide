/*
 * WeakMap (difference with Map)
 * WeakMap has 'Weak Reference'
 */
"use strict";

import { title, subtitle, l } from "./util.js";

title("WeakMap");
{
  const map = new WeakMap();
  let obj = {};
  map.set(obj, "v");

  l(map, map.get(obj));
  obj = null;
  l(map, map.get(obj));
}
