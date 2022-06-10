import strutils

proc title(msg: string) =
  let size = msg.len + 3
  echo "\n"
  echo "*".repeat(size)
  echo "* ", msg
  echo "*".repeat(size)

proc calcBMI(height:float, weight: float): float =
  return weight / (height * height)


title("calc BMI")

echo "Input your height(m)"
let height = readLine(stdin).parseFloat()
echo "Input your weight(kg)"
let weight = readLine(stdin).parseFloat()

echo "calcBMI = ", calcBMI(height, weight)


title("Collatz conjucture exercise")

proc collatz(num: var int): seq[int] =
  while num != 1:
    result.add(num)
    if num mod 2 == 0:
      num = num div 2
    else:
      num = 3 * num + 1
  return result

echo "Input num (> 0)"
var num = readLine(stdin).parseInt()
echo collatz(num)


title("reverse strings")

proc reverseString(str: string): string =
  for i in countdown(str.len - 1, 0):
    result.add(str[i])

let strings = readLine(stdin).strip()
echo reverseString(strings)
