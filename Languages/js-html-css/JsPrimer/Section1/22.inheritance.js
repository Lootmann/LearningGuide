/*
 *
 */
"use strict";
import { title, l } from "./util.js";

class Parent {
  constructor(...args) {
    l("Parent Constructor ", ...args);
  }

  hello() {
    l("> Greetings");
  }

  static method() {
    l("* static Parent");
  }
}

class Child extends Parent {
  constructor(...args) {
    super(...args);
    l("Child Constructor", ...args);
  }

  hello() {
    // this.hello() is Child.hello()
    super.hello();
    l("> I'm a Child");
  }

  static method() {
    super.method();
    l("* static Child");
  }
}

title("Parent");
const parentInstance = new Parent();
l(parentInstance);
parentInstance.hello();
Parent.method();

title("Child");
const childInstance = new Child();
l(childInstance);
childInstance.hello();
Child.method();
