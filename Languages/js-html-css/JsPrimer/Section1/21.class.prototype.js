/*
 * class prototype
 */
"use strict";
import { title, l } from "./util.js";

title("Example Class");
{
  class ExampleClass {
    instanceMethod = () => {
      l("instance method");
    };

    prototypeMethod() {
      l("prototype method");
    }
  }

  const example = new ExampleClass();
  example.instanceMethod();
  example.prototypeMethod();
}

title("Conflict Class");
{
  class ConflictClass {
    method = () => {
      l("インスタンスオブジェクトのメソッド");
    };

    method() {
      l("プロトタイプメソッド");
    }
  }

  const conflict = new ConflictClass();
  conflict.method(); // instance method

  delete conflict.method;
  conflict.method(); // prototype method
}
