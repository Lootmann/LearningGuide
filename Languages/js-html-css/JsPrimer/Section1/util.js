"use strict";

export const l = console.log;
export const title = (msg) => {
  console.log();
  console.log(`\x1b[4m\x1b[31m>>> \x1b[35m${msg}\x1b[0m\n`);
};
