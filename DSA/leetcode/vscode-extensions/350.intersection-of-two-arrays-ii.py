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
        n1 = [0] * 1001
        n2 = [0] * 1001

        for num1 in nums1:
            n1[num1] += 1

        for num2 in nums2:
            n2[num2] += 1

        result = list()

        for i, (num1, num2) in enumerate(zip(n1, n2)):
            if num1 > 0 and num2 > 0:
                result += [i] * min(num1, num2)

        return result


# @lc code=end
