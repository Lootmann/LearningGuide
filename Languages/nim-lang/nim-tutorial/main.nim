import strutils


proc title(msg: string) =
  let size = msg.len + 3
  echo "\n"
  echo "*".repeat(size)
  echo "* ", msg
  echo "*".repeat(size)


proc short(msg: string) =
  echo ">>> ", msg

title("block")
block myblock:
  var x = "hi all"

# echo x # cause Error
block myblock:
  echo "entering myblock"

  while true:
    echo "looping"
    break

  echo "still in block"
echo "outside the block"

echo "\n-----\n"

block myblock2:
  echo "entering myblock2"

  while true:
    echo "looping"
    break myblock2

  echo "still in block"
echo "outside the block"



title("for")
for i in 0 .. 3:
  echo i

for i in 0 ..< 3:
  echo i

short("countup")
for i in countup(0, 3):
  echo i

short("countdown")
for i in countdown(3, 0):
  echo i

const str = "hello"
for ch in str:
  echo ch

for i, ch in str:
  echo i, " ", ch

for i in 0 ..< str.len:
  echo i, " ", str[i]

for i, ch in str[0 .. ^1]:
  echo i, " ", ch

short("pairs")
const arr = ['a', 'b', 'c', 'd', 'e']
for i, item in arr.pairs:
  echo item, " at index ", i


var tuples: seq[tuple[x, y: int]] = @[]
for i in [1,2,3,4]:
  tuples.add((i, i + 1))

for idx, t in tuples.pairs:
  echo idx, " ", t

for t in tuples.items:
  echo t
