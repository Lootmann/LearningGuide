proc title(msg: string) =
  echo "\n********************"
  echo "* ", msg
  echo "********************"

title("findMax")
proc findMax(x: int, y: int): int =
  if x > y:
    return x
  return y

const
  x = 10
  y = 20

echo findMax(x, y)


title("arg: var in maens arg changeable value")
proc changeArgument(arg: var int) =
  arg += 10

var n: int = 10
echo "n = ", n
changeArgument(n)
echo "n = ", n


title("Uniform Call Syntax")
proc plus(x, y: int): int =
  return x + y

proc multi(x, y: int): int =
  return x * y

let
  a = 2
  b = 3
  c = 4

echo a.plus(b) == plus(a, b)
echo b.multi(c) == multi(b, c)


title("Result Variable")
proc findBiggest(a: seq[int]): int =
  # 'result' variable if return int, result:int = 0 by default
  # but, if 'container a' has some minus integer, result will return wrong :^)
  for number in a:
    if number > result:
      result = number

let d = @[6, 10, 1, 12, 15, 8]
echo findBiggest(d)


title("keepOdds")
proc keepOdds(b: seq[int]): seq[int] =
  for number in b:
    if number mod 2 == 1:
      result.add(number)

let f = @[1, 6, 4, 43, 57, 34, 98]
echo keepOdds(f)


title("isDivisibleBy3")
proc isDivisibleBy3(x: int): bool =
  return x mod 3 == 0

proc filterMultiplesOf3(a: seq[int]): seq[int] =
  for i in a:
    if i.isDivisibleBy3():
      result.add(i)

let
  g = @[2, 6, 5, 7, 9, 0, 5, 3]
  h = @[5, 4, 3, 2, 1]
  i = @[626, 45390, 3219, 4210, 4126]

echo filterMultiplesOf3(g)
echo h.filterMultiplesOf3()
echo filterMultiplesOf3 i


proc minus(x, y: int): int

echo minus(10, 12)
echo minus(10, 1)

proc minus(x, y: int): int =
  return x - y
