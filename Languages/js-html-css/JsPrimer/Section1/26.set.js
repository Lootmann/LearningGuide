/*
 * Set
 */
"use strict";

import { title, subtitle, l } from "./util.js";

title("Set");
{
  const set = new Set();
  set.add("v1");
  set.add("v2");
  set.add("v3");
  l(set);

  const set1 = new Set(["v1", "v2", "v3"]);
  l(set1);

  l(set1.delete("v1"));
  l(set1);

  set1.clear();
  l(set1);
}

title("Set loop");
{
  const set = new Set(["a", "b"]);
  const res = [];
  set.forEach((v) => {
    res.push(v);
  });
  l(res);

  subtitle(".keys()");
  l(set.keys());
  l(set.entries());
}
