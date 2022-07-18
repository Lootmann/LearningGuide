"use strict";

const log = console.log;
const util = require("./util");

// import CommonJS Module
util.title("CommonJS Module");
const myModule = require("./my-module");
log(myModule);

const program = require("commander");
program.parse(process.argv);

const filePath = program.args[0];
log(filePath);

// fs
util.title("fs");
const fs = require("fs");

fs.readFile(filePath, { encoding: "utf8" }, (err, file) => {
  if (err) {
    console.error(err);
    process.exit(1);
    return;
  } else {
    console.log(file);
  }
});
