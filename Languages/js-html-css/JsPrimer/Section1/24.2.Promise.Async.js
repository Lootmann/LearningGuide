/*
 * Promise Async
 */
"use strict";

import { title, l } from "./util.js";

title("Promise.resolve");
{
  const fullfilledPromise = Promise.resolve();

  // as same as this.
  const fullfilledPromiseAsSame = new Promise((resolve) => {
    resolve();
  });
}

title("Promise.resolve(value)");
{
  const fullfilledPromise = Promise.resolve(42);
  fullfilledPromise.then((value) => {
    l(value);
  });
}

title("A/Synchronous Order");
{
  const promise = new Promise((resolve) => {
    // first
    l("1");
    resolve();
  });

  promise.then(() => {
    // fourth = last with Asyncronous
    l("4");
  });

  // second, third with Synchronous
  l("2");
  l("3");
}

title("Promise.reject");
{
  //const rejectedPromise = Promise.reject(new Error("error!"));
  const rP = new Promise((reject) => {
    //reject(new Error("error!"));
  });
}

title("Promise Chains 1");
{
  Promise.resolve()
    .then(() => {
      l("chain :", 1);
    })
    .then(() => {
      l("chain :", 2);
    });
}

title("Promise Chains 2");
{
  function asyncTask() {
    return Math.random() > 0.5
      ? Promise.resolve("success")
      : Promise.reject(new Error("failed"));
  }

  asyncTask()
    .then(function onFulfilled(value) {
      l(value);
    })
    .catch(function onRejected(error) {
      l(error.message);
    });
}
