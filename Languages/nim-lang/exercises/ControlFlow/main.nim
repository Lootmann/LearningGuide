echo "*** Collatz conjecture"

var num: int = 5

while num != 1:
  echo "num = ", num
  if num mod 2 == 0:
    num = num div 2
  else:
    num = 3 * num + 1


echo "*** for-loop name"
for letter in "Vasilly Lomachenko":
  case letter
    of 'a', 'e', 'i', 'o', 'u':
      echo "vowel"
    else:
      echo "not: ", letter


echo "*** FizzBuzz"
for i in 1 .. 30:
  if i mod 15 == 0:
    echo "FizzBuzz"
  elif i mod 3 == 0:
    echo "Fizz"
  elif i mod 5 == 0:
    echo "Buzz"
  else:
    echo i


echo "*** inch to cm"
for inch in countup(1, 19, 3):
  echo float(inch) * 2.54
