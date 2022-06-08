# if, else, elif
let
  a = 11
  b = 22
  c = 999

if a < b:
  echo "a < b"
else:
  echo "a > b"

if a < c:
  echo "a < c"
else:
  echo "a > c"


if c < 100:
  echo "c < 100"
elif c < 500:
  echo "c < 500"
elif c < 900:
  echo "c < 900"
else:
  echo "c is bigger than 900"


# case of, else
const ch = 'y'

case ch
  of 'x':
    echo "ch = ", ch
  of 'y':
    echo "ch = ", ch
  of 'z':
    echo "ch = ", ch
  else:
    discard

const i = 7

case i
  of 0:
    echo "0"
  of 2, 4, 6, 8, :
    echo "even !"
  of 1, 3, 5, 7, 9:
    echo "odd !"
  else:
    echo "it's odd ..."


# for in
echo "x .. x"
for n in 0 .. 5:
  echo n

echo "x ..< x"
for n in 0 ..< 5:
  echo n

echo "countup() by even"
for n in countup(0, 10, 2):
  echo n

echo "countdown()"
for n in countdown(4, 0):
  echo n

echo "countdown() by even"
for n in countdown(10, 0, 2):
  echo n


# invalid because countup(n, m, k)
# k needs positive and n < m
# for n in countup(10, 0, -2):
  # echo n

echo "countup(10, 5) doesn't work properly"
for n in countup(10, 5):
  echo n

echo "Strings Loop"
const word = "alphabet"
for letter in word:
  echo letter

for i, ch in "long-string":
  echo i, " : ", ch


echo "*** while loop"
var num = 0
while num < 5:
  echo num
  inc num


echo "*** while break"
var j: int = 1
while j < 100:
  if j == 5:
    break
  echo j
  inc j


echo "*** continue"
for n in 1 .. 8:
  if (n == 3) or (n == 6):
    continue
  echo n
