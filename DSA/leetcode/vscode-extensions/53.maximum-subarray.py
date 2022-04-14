#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = -(10**8)

        for i in range(len(nums) + 1):
            for j in range(len(nums)):
                if i != 0:
                    total = max(total, sum(nums[j : j + i]))

        return total


# @lc code=end
