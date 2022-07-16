/*
 * function, scope
 */

"use strict";

import { title, l } from "./util.js";

title("function scope");
{
  function fn() {
    // this x has fn scope
    const x = 1;
    console.log(x);
  }

  fn();
  // console.log(x)
}

title("scope chain");
{
  l("outer block chain");
  const x = "outer";
  {
    l("inner block chain");

    // shadowing
    const x = "inner";
    console.log(x);
  }

  l("outside inner");
  console.log(x);
}

title("IIFE: Immediately-Invoked Function Expression");
{
  (function () {
    // close scope despite using 'var'
    var foo = "foo";
    console.log(foo);
  })();
}

title("Closure");
{
  // 関数閉包: Closure
  function createCounter() {
    let count = 0;

    function increment() {
      count++;
      return count;
    }
    return increment;
  }

  const counter = createCounter();
  l(counter());
  l(counter());
  l(counter());
  // error
  // l(counter.increment());
}
