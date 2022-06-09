import std/strutils
import system/assertions

proc title(msg: string) =
  let size = msg.len + 3
  echo "\n", "*".repeat(size)
  echo "* ", msg
  echo "*".repeat(size)


#[
1.
  Create a procedure which will greet a person (print "Hello <name>")
  based on the provided name.
  Create a sequence of names. Greet each person using the created procedure.
]#
title("Exercise 1")

proc greeting(name: string) =
  echo "Hello ", name

let names = @["Davis", "Shaukr", "Haney"]
for name in names:
  greeting(name)


#[
  2.
    Create a procedure findMax3 which will return the largest of three values.
]#
title("Exercise 2")

proc findMax3(x, y, z: int): int =
  runnableExamples:
    assert findMax3(1, 2, 3) == 3
    assert findMax3(5, 3, 4) == 5
    assert findMax3(3, 4, 2) == 4

  if x > y:
    result = x
  else:
    result = y

  if result > z:
    return result
  else:
    return z

echo findMax3(1, 2, 3)
echo findMax3(12, 11, 10)
echo findMax3(-5, -1, -2)


#[
3.
  Points in 2D plane can be represented as tuple[x, y: float].
  Write a procedure which will receive two points
  and return a new point which is a sum of those two points (add x’s and y’s separately).
]#
title("Exercise 3")

proc sumTuples(p: tuple[x, y: float], q: tuple[x, y: float]): (float, float) =
  runnableExamples:
    assert sumTuples((1.0, 1.0), (2.0, 2.0)) == (3.0, 3.0)

  return (p.x + q.x, p.y + q.y)

let
  t1 = (1.1, 5.5)
  t2 = (6.6, 2.2)
  t3 = (3.3, 7.7)
  t4 = (8.8, 4.4)

let
  new_t1 = sumTuples(t1, t4)
  new_t2 = sumTuples(t2, t3)

echo new_t1
echo new_t2

#[
4.
  Create two procedures tick and tock which echo out the words "tick" and "tock".
  Have a global variable to keep track of how many times they have run,
  and run one from the other until the counter reaches 20.
  The expected output is to get lines with "tick" and "tock" alternating 20 times.
  (Hint: use forward declarations.) 
]#
title("Exercise 4")

# forward declarations
var
  tickCount = 1
  tockCount = 1

proc tick()
proc tock()

proc tick() =
  if tickCount > 20:
    return

  echo "tick : ", tickCount
  tickCount += 1
  tock()

proc tock() =
  if tockCount > 20:
    return

  echo "tock : ", tockCount
  tockCount += 1
  tick()


echo "Start :^)"
tick()
# or tock()
echo "End :^)"
