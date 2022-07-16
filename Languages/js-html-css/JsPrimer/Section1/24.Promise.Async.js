/*
 * Promise Async Function
 */
"use strict";

import { title, l } from "./util.js";

const blockTime = (timeout) => {
  l(">> start block");
  const startTime = Date.now();
  while (true) {
    const diffTime = Date.now() - startTime;
    if (diffTime >= timeout) {
      l(">> end block");
      return;
    }
  }
};

title("Synchronous Processing");
l("> start");
blockTime(1500);
l("> end");

title("Asynchronous Processing");
l("> start");
setTimeout(() => {
  l("  * bloc");
  blockTime(1500);
  l("  * end block");
});
l("> end");
