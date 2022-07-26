const log = console.log;

function chooseRandomly<T>(a: T, b: T): T {
  return Math.random() <= 0.5 ? a : b;
}

log(chooseRandomly<string>("a", "b"));
log(chooseRandomly<number>(0, 1));
log(chooseRandomly<string>("left", "right"));
