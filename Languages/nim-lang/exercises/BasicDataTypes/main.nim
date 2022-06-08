#[
  Nim-basics Basic data types - Exercises 1

  https://narimiran.github.io/nim-basics/#_exercises 
]#

# 1
const age = 34
echo age * 365, " days"

# 2
echo age mod 3 == 0

# 3
const height = 178

# cm to inch
echo height * (1.0 / 2.54), " inch"
# cm to feet
echo height / 30.48, " feet"

# 4
echo 3/8 * 2.54, " centimeters"

# 5
const firstName = "lyo"
const lastName = "Nikaidoh"
echo firstName & " " & lastName

# 6
const alice = 400 * 15 * 2
const bob = 3.14 * 8 * 7 * 4
echo "alice: ", alice, " bob: ", bob
echo alice > bob
