#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        mid = 0

        while right - left > 1:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        return right


# @lc code=end
