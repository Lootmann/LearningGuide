/*
 * Promise Async
 */
"use strict";

import { title, l } from "./util.js";

title("Promise resolve, reject");
{
  // resolve: will trigger when success
  // reject : will trigger when failed
  const promise = new Promise((resolve, reject) => {
    // this Promise will trigger resolve()
    // so console.log("success") happens
    if (true) resolve();
    else reject();
  });

  const onFulfilled = () => {
    l("success");
  };

  const onRejected = () => {
    l("failed");
  };

  // register callback functions resolve, and reject
  promise.then(onFulfilled, onRejected);
}

title("Promise Fetch Sample");
{
  // dummyFetch
  function dummyFetch(path) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (path.startsWith("/success")) {
          resolve({ body: `Response body of ${path}` });
        } else {
          reject(new Error("Path Not Found :^)"));
        }
      }, 1000 * Math.random());
    });
  }

  function onFulfilled(response) {
    l(response);
  }

  function onRejected(error) {
    l(error);
  }

  // dummyFetch return promise
  // promise.then() registers 'resolve', 'reject'
  dummyFetch("/success/data").then(onFulfilled, onRejected);
  // dummyFetch("/failed/data").then(onFulfilled, onRejected);
}

title("Promise.then() only when is success");
{
  function delay(timeoutMs) {
    // this Promise has no reject(), but it's correct.
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, timeoutMs);
    });
  }

  l("1. triggered");
  delay(100).then(() => {
    l("1. elapsed 100 msec");
  });
}

title("Promise.then() another way only when is success ");
{
  function errorPromise(message) {
    // when you don't use resolve...
    return new Promise((resolve, reject) => {
      // only register reject
      reject(new Error(message));
    });
  }

  errorPromise("Error Handling with catch").catch((error) => {
    l(error.message);
  });
}

title("Promise throw");
{
  function throwPromise() {
    return new Promise((resolve, reject) => {
      throw new Error("throw Exceptions");
    });
  }

  throwPromise().catch((error) => {
    l(error.message);
  });
}
