/*
 * class
 */
"use strict";

import { title, l } from "./util.js";

title("Class");
{
  class MyClass {
    constructor() {}
  }

  const myClass = new MyClass();
  const anotherClass = new MyClass();
  l(MyClass == myClass);
  l(myClass instanceof MyClass);
  l(anotherClass instanceof MyClass);
}

title("constructor");
{
  class Point {
    constructor(x, y) {
      this.x = x;
      this.y = y;
      this.count = 0;
    }

    increment() {
      this.count++;
    }
  }

  const point = new Point(1, 2);
  l(point);

  point.increment();
  point.increment();
  point.increment();
  l(point);
}

title("property");
{
  class NumberWrapper {
    constructor(value) {
      this._value = value;
    }

    get value() {
      return this._value;
    }

    set value(newValue) {
      this._value = newValue;
    }
  }

  const number = new NumberWrapper(12);
  l(number);
  l(number.value);

  number.value = 23;
  l(number.value);
}

title("ArrayLike");
{
  class ArrayLike {
    constructor(items = []) {
      this._items = items;
    }

    get items() {
      return this._items;
    }

    get length() {
      return this._items.length;
    }

    set length(newLength) {
      const currentItemLength = this.items.length;

      if (newLength < currentItemLength) {
        this._items = this.items.slice(0, newLength);
      } else if (newLength > currentItemLength) {
        // if newLength is greater than ItemLength
        // push empty items
        this._items = this.items.concat(
          new Array(newLength - currentItemLength)
        );
      }
    }
  }

  const arrayLike = new ArrayLike([1, 2, 3, 4, 5]);
  l(arrayLike.items);

  arrayLike.length = 2;
  l(arrayLike.items);

  arrayLike.length = 5;
  l(arrayLike.items);
}

title("Class Field");
{
  class Counter {
    // public field
    count = 0;

    constructor() {
      this.count = 0;
    }

    increment() {
      this.count++;
    }
  }

  const counter = new Counter();
  counter.increment();
  l(counter);

  counter.count = 10;
  l(counter);
}

title("class field in this");
{
  class Counter {
    count = 0;

    up = this.increment;

    increment() {
      this.count++;
    }
  }

  const counter = new Counter();
  counter.up();
  l(counter);
}

title("class field in arrow function");
{
  class Counter {
    count = 0;

    up = () => {
      this.increment();
    };

    increment() {
      this.count++;
    }
  }

  const counter = new Counter();
  l(counter);

  counter.increment();
  l(counter);

  counter.up();
  l(counter);

  const up = counter.up;
  up(); // Arrow Function is good
  l(counter);

  const increment = counter.increment;
  // increment(); // normal function is bad
  l(counter);
}

title("Private class field");
{
  class PrivateExampleClass {
    #privateField = 42;

    dump() {
      return this.#privateField;
    }
  }

  const pec = new PrivateExampleClass();
  l(pec);
  l(pec.dump());
}

title("Private class Field usage");
{
  class NumberWrapper {
    #value;

    constructor(value) {
      this.#value = value;
    }

    get value() {
      return this.#value;
    }

    set value(newValue) {
      this.#value = newValue;
    }
  }

  const numberWrapper = new NumberWrapper(1);
  // raise Error ofcourse
  // l(numberWrapper.#value);
  l(numberWrapper.value);
}

title("static class field");
{
  class Colors {
    static RED = "red";
    static BLUE = "blue";
    static GREEN = "green";
  }

  l(Colors);
  l(Colors.RED, Colors.BLUE, Colors.GREEN);
}

title("Private class field");
{
  class My {
    static #privateClassField = "this is a private";

    static outputPrivate() {
      l(this.#privateClassField);
    }
  }

  l(new My());
  const m = new My();
  // this is a method, not static
  // m.outputPrivate();
  My.outputPrivate();
}
