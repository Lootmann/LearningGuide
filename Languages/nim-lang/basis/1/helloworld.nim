echo "hello world"

# mutable
var a: int = 123
var b: string = "wow"

echo a, b

b = "boom"
echo b

# immutable
const PI = 3.14
echo PI * 10.0

# Compile Error!
# PI = 3.0

# immutable also
let num1: int = 12
echo num1

# num2 can define at compile time
# 'const' cannot do that, but 'let' can do.
let num2: int = num1 + 12
echo num2
echo num1

# multiple definition
var
  a1: int = 1
  a2: int = 2

echo a1, " ", a2, " ", " :^)"
