"use strict";
const log = console.log;
function chooseRandomly(a, b) {
    return Math.random() <= 0.5 ? a : b;
}
log(chooseRandomly("a", "b"));
log(chooseRandomly(0, 1));
log(chooseRandomly("left", "right"));
