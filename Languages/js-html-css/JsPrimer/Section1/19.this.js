/*
 * function and this
 */
"use strict";
import { title, l } from "./util.js";

title("this in 'module'");
{
  l(this);
  // l(globalThis);
}

title("kind of functions");
{
  function f1() {}
  const f2 = function () {};
  const f3 = () => {};

  l(f1);
  l(f2);
  l(f3);
}

title("kind of methods");
{
  const obj = {
    // ordinary function
    method1: function () {},

    // Array Function
    method2: () => {},

    // shorthand method
    method() {},
  };

  l(obj.method1);
  l(obj.method2);
  l(obj.method);
}

title("this in function");
{
  const obj = {
    m1: function () {
      return this;
    },
    m2() {
      return this;
    },
  };

  l(obj.m1());
  l(obj.m2());
}

/*
 * Arrow Function and this
 *
 * Arrow Function で定義された function, method は
 * 関数の定義時に 静的に決まる
 * */
title("Arrow Function as Callback Function");
{
  const Prefixer = {
    prefix: "pre",
    prefixArray(strings) {
      return strings.map((str) => {
        // 'this' refers prefixArray
        // so 'this.prefix' is 'pre'
        return this.prefix + "-" + str;
      });
    },
  };

  const prefixedStrings = Prefixer.prefixArray(["a", "b", "c"]);
  l(prefixedStrings);
}
