import strutils

let contents = readFile("./names.txt").strip()
echo contents

let people = contents.splitLines()
echo people
