/*
  17.wrapper_objects

  primitive
  一度作成したらその値自体を変更できない immutable
  Boolean Number BigInt String Undefined null symbol

  object
  except primitive
  Object Array Function Regex Date ...
*/

"use strict";

import { title, l } from "./util.js";

title("primitive");
{
  const str = new String("input value");

  l(str.toUpperCase());
  l(new String(str).toUpperCase());
}

title("primitive to wrapper object");
{
  // String is Primitive
  const str = "string";

  // Primitive to Wrapper object
  // 'str' is Primitive, Wrapper is 'String'
  // automatically convert primitive to Wrapper Object
  l(str.toUpperCase());

  // this code is same as above code.
  l(new String(str).toUpperCase());
}
