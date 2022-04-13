#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for i, num in enumerate(digits):
            total += num * 10 ** (len(digits) - i - 1)

        total += 1
        digits = []

        while total > 0:
            digits.append(total % 10)
            total //= 10

        return digits[::-1]


# @lc code=end
