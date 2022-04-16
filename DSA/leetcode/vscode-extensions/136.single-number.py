#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
from typing import List


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


# @lc code=end
