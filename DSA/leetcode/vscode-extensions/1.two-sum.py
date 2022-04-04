#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = dict()

        for i, num in enumerate(nums):
            if num in other:
                return [other[num], i]

            left = target - num
            other[left] = i


# @lc code=end
