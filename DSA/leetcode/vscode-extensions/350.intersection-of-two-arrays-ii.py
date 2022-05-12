#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
import collections
from typing import List


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = collections.Counter(nums1)
        n2 = collections.Counter(nums2)
        result = []

        # O(N)
        for k, v in n1.items():
            if k in n2:
                # O(N)
                for _ in range(min(v, n2[k])):
                    result.append(k)

        return result


# @lc code=end
