#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        if len(digits) == 0:
            return result

        chars = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result += list(chars[int(digits[0]) - 2])

        for digit in digits[1:]:
            idx = int(digit) - 2
            tmp = []

            for ch in list(chars[idx]):
                for res in result:
                    tmp.append(f"{res}{ch}")

            result = tmp

        return result


# @lc code=end
