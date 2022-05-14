#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)

        # O(2^N)
        for bit in range(1 << length):
            subset = []
            for i in range(length):
                if bit & (1 << i):
                    subset.append(nums[i])
            result.append(subset)

        return result


# @lc code=end
