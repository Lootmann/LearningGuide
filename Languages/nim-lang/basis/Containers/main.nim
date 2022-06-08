echo "*** array"

var
  a: array[3, int] = [1, 2, 3]
  b = [1, 2, 3]
  c: array[3, int] # [0, 0, 0]

echo a
echo b
echo c


echo "*** const size"
const size = 3
var d: array[size, char]
echo d

#[
  let size = 3
  var d: array[size, char]
  cant use 'let'
]#

echo "*** Sequences"
echo "their length doesn't have to be known at compile time."

var
  e1: seq[int] = @[]
  f1 = @["abc", "def"]
  g1 = newSeq[int]()

echo e1
echo f1
echo g1


echo "*** Sequences"
var
  g = @['x', 'y']
  h = @['1', '2', '3']

g.add('z')
echo "g = ", g

h.add(g)
echo "h = ", h

echo "size(g) = ", g.len
echo "size(h) = ", h.len


echo "*** indexing"
let arr: array[5, char] = ['a', 'b', 'c', 'd', 'e']

echo arr
echo arr[0]
echo arr[1]
echo arr[2]
echo arr[^3]
echo arr[^2]
echo arr[^1]

echo arr[0 .. 4]
echo arr[1 .. 3]
echo arr[0 ..< arr.len]


echo "*** tuples"
let t1 = ("Banana", 2, 'c')
echo t1

let t2 = (name: "Apple", cost: 1.2, rating: 'b')
echo t2
echo t2.name, " ", t2.cost, " ", t2.rating
