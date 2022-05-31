#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N logN)
        nums.sort()

        for i, _ in enumerate(nums, 1):
            if nums[i] == nums[i - 1]:
                return nums[i]

        return -1


# @lc code=end
