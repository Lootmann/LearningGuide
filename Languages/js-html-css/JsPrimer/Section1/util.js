"use strict";

class Attribute {
  static reset = "\x1b[0m";
  static bright = "\x1b[1m";
  static dim = "\x1b[2m";
  static underscore = "\x1b[4m";
  static blink = "\x1b[5m";
  static reverse = "\x1b[7m";
  static hidden = "\x1b[8m";
}

function attred(attr, msg) {
  let s = "";
  if (attr === "bright") s += Attribute.bright;
  if (attr === "dim") s += Attribute.dim;
  if (attr === "underscore") s += Attribute.underscore;
  if (attr === "blink") s += Attribute.blink;
  if (attr === "reverse") s += Attribute.reverse;
  if (attr === "hidden") s += Attribute.hidden;

  return s + msg;
}

class Colors {
  static black = "\x1b[30m";
  static red = "\x1b[31m";
  static green = "\x1b[32m";
  static yellow = "\x1b[33m";
  static blue = "\x1b[34m";
  static magenta = "\x1b[35m";
  static cyan = "\x1b[36m";
  static white = "\x1b[37m";
  static crimson = "\x1b[38m";
}

function colored(color, msg) {
  let s = "";
  if (color === "black") s += Colors.black;
  if (color === "red") s += Colors.red;
  if (color === "green") s += Colors.green;
  if (color === "yellow") s += Colors.yellow;
  if (color === "blue") s += Colors.blue;
  if (color === "magenta") s += Colors.magenta;
  if (color === "cyan") s += Colors.cyan;
  if (color === "white") s += Colors.white;
  if (color === "crimson") s += Colors.crimson;

  return s + msg;
}

export const l = console.log;

export const title = (msg) => {
  if (!msg) throw new Error("not msg here D:");

  const content = colored("red", ">>> ") + colored("yellow", msg);
  console.log("\n" + attred("reverse", content) + Attribute.reset + "\n");
};

export const subtitle = (msg) => {
  const content = colored("green", "*** ") + colored("blue", msg);
  const line = attred("underscore", content) + Attribute.reset;
  console.log("\n" + line + "\n");
};
