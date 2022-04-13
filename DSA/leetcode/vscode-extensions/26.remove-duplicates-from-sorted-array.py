#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        cur, nxt = 0, 1
        while nxt < len(nums):
            if nums[cur] != nums[nxt]:
                cur += 1
                nums[cur] = nums[nxt]
            else:
                nxt += 1

        return cur + 1


# @lc code=end
