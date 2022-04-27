#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
from typing import List


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(range(len(nums) + 1))
        return total - sum(nums)


# @lc code=end
