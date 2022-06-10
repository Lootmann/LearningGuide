# dealing with string, split(), toUpperAscii, repeat, ...
import strutils

let
  a = "Hello String with whitespace World"
  b = '!'

echo a.split()
echo a.toUpperAscii()
echo b.repeat(5)
