const log = console.log;

function request1(): Promise<number> {
  return new Promise((resolve) => {
    log("request1");
    setTimeout(() => {
      resolve(1);
    }, 1000);
  });
}

function request2(res: number): Promise<number> {
  return new Promise((resolve) => {
    log("request2");
    setTimeout(() => {
      resolve(res + 1);
    }, 1000);
  });
}

function request3(res: number): Promise<number> {
  return new Promise((resolve) => {
    log("request3");
    setTimeout(() => {
      resolve(res + 2);
    }, 1000);
  });
}

async function main() {
  const res1 = await request1();
  const res2 = await request2(res1);
  const res3 = await request3(res2);
  log(res3);
}

main();
