let
  a = 10
  b = 4

echo "a + b = ", a + b
echo "a - b = ", a - b
echo "a * b = ", a * b
echo "a / b = ", a / b
echo "a div b = ", a div b
echo "a mod b = ", a mod b

# auto convert
let ans = a / b
echo ans, type(ans)

let
  e = 5
  f = 5.0

echo float(e) + f
echo e + int(f)

echo float(e) + f

# characters - single ASCII character.
let
  h = 'h'
  i = 'i'
  k = 'k'

echo h, i, k

# Strings
let
  sa = "h"
  sb = "ello"
  sc = " "
  sd = "world :^)"

echo sa, sb, sc, sd
echo "hello world :^)\nthis is new line\n"


# Strings concatination
let
  p = "hello"
  space = " "
  q = "world"

var result: string = ""

result.add(p)
result.add(space)
result.add(q)

echo result
echo p & space & q


let
  big = 10
  middle = 5
  small = 1
  minus = -5


echo big > middle
echo middle < small
echo small == minus

echo true
echo false
echo true and false
echo true xor true
echo not (small == minus)
