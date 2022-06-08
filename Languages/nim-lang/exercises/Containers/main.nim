echo "*** Container"
var arr = newSeq[int]()

for n in countup(10, 100, 10):
  arr.add(n)

for i in countup(1, arr.len - 1, 2):
  echo arr[i]

for i in countup(0, arr.len - 1, 2):
  arr[i] -= 5

echo "\n*** Multiply elements on even indices by 5."
echo arr


echo "\n*** Collatz Conjecture"
for num in @[9, 19, 25, 27]:

  var secs = newSeq[int]()
  var n = num

  while n != 1:
    secs.add(n)
    if n mod 2 == 0:
      n = n div 2
    else:
      n = 3 * n + 1

  echo secs.len
  echo secs


echo "\n*** Longest Collatz"

var 
  longestLength = 0
  startingNumber = 0

for i in 1 .. 100:
  var
    n = i
    length = 0
  
  while n != 1:
    length += 1
    if n mod 2 == 0:
      n = n div 2
    else:
      n = 3 * n + 1

    if length > longestLength:
      longestLength = length
      startingNumber = i

echo "longestLength, startingNumber = ", (longestLength, startingNumber)
