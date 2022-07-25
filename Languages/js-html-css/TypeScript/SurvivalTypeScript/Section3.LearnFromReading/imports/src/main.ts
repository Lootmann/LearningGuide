import { StringValidator } from "./module";

export const numberRegexp = /^[0-9]+$/;

export class ZipCodeValidator implements StringValidator {
  isAcceptable(s: string) {
    return s.length === 5 && numberRegexp.test(s);
  }
}

const zipper = new ZipCodeValidator();
const strings: string[] = ["zip code", "123abc", "12334", "00001"];

strings.forEach((str) => {
  console.log(str, zipper.isAcceptable(str));
});
