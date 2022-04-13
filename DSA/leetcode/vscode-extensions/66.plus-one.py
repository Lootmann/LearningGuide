#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        digits[0] += 1

        for i in range(len(digits) - 1):
            if digits[i] >= 10:
                digits[i] -= 10
                digits[i + 1] += 1

        if digits[-1] >= 10:
            digits[-1] -= 10
            digits.append(1)

        return digits[::-1]


# @lc code=end
