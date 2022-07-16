/*
 * try ... catch ...
 */
"use strict";
import { title, l } from "./util.js";

title("try ... catch ... finally");
{
  try {
    l("try");
    noDefinedFunction();
  } catch (error) {
    l("catch");
  } finally {
    l("finally");
  }
}

title("throw");
{
  try {
    // Error Object
    throw new Error("Throw Error");
  } catch (error) {
    l(error, error.message);
  }
}

title("Built-in Error");
{
  const reverseString = (str) => {
    if (typeof str !== "string") {
      throw new TypeError(`${str} is not a string.`);
    }
    return Array.from(str).reverse().join("");
  };

  try {
    // error
    reverseString(100);
  } catch (error) {
    l(error instanceof TypeError);
    l(error.name);
    l(error.message);
  }
}
