export const numberRegexp = /^[0-9]+$/;
export class ZipCodeValidator {
    isAcceptable(s) {
        return s.length === 5 && numberRegexp.test(s);
    }
}
const zipper = new ZipCodeValidator();
const strings = ["zip code", "123abc", "12334", "00001"];
strings.forEach((str) => {
    console.log(str, zipper.isAcceptable(str));
});
