echo "*** findMax"
proc findMax(x: int, y: int): int =
  if x > y:
    return x
  return y

const
  x = 10
  y = 20

echo findMax(x, y)


# arg: var int means arg changeable value
proc changeArgument(arg: var int) = 
  arg += 10

var n: int = 10
echo "n = ", n
changeArgument(n)
echo "n = ", n


echo "\n*** Uniform Call Syntax"
proc plus(x, y: int): int =
  return x + y

proc multi(x, y: int): int =
  return x * y

let
  a = 2
  b = 3
  c = 4

echo a.plus(b) == plus(a ,b)
echo b.multi(c) == multi(b, c)


echo "\n*** Result Variable"
proc findBiggest(a: seq[int]): int =
  # 'result' variable if return int, result:int = 0 by default
  # but, if 'container a' has some minus integer, result will return wrong :^)
  for number in a:
    if number > result:
      result = number

let d = @[6, 10, 1, 12, 15, 8]
echo findBiggest(d)


echo "\n*** keepOdds"
proc keepOdds(b: seq[int]): seq[int] = 
  for number in b:
    if number mod 2 == 1:
      result.add(number)

let f = @[1, 6, 4, 43, 57, 34, 98]
echo keepOdds(f)

