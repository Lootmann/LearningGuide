#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # not O(1)
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        count = 0
        majority = 0

        for k, v in d.items():
            if v > count:
                majority = k
                count = v

        return majority


# @lc code=end
