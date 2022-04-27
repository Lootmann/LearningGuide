#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False


# @lc code=end
