import strutils

echo "Input Your birth:"
let birth = readLine(stdin).parseInt() 

let age = 2022 - birth

echo "You are ", age, " years"
