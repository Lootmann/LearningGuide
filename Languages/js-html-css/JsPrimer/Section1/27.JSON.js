/*
 *
 */
"use strict";

import { title, subtitle, l } from "./util.js";

title("JSON");
{
  // JSON is just a string.
  const json = '{ "id": 1, "name": "js-primer" }';
  const obj = JSON.parse(json);
  l(obj);
  l(obj.id); // => 1
  l(obj.name); // => "js-primer"
}

title("JSON raise");
{
  const userInput = '{ "id": 1 ]';
  try {
    const json = JSON.parse(userInput);
  } catch (error) {
    l("cannot parse");
  }
}

title("JSON.stringify");
{
  const obj = { id: 1, name: "js-primer", bio: null };
  l(JSON.stringify(obj));

  const replacer = ["id", "name"];
  l(JSON.stringify(obj, replacer));
  // indent
  l(JSON.stringify(obj, null, "  "));
}

title("toJSON");
{
  const o = {
    foo: "foo",
    toJSON() {
      return "bar";
    },
  };

  l(JSON.stringify(o));
  l(JSON.stringify({ x: o }));
}
