#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 0

        for i, _ in enumerate(nums):
            if nums[i] != 0:
                nums[i], nums[prev] = nums[prev], nums[i]
                prev += 1


# @lc code=end
