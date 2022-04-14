#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_total = -(10**8)

        for num in nums:
            total = max(num, total + num)
            max_total = max(max_total, total)

        return max_total


# @lc code=end
