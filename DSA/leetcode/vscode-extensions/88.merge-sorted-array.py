#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from operator import le
from typing import List


# @lc code=start
class Solution:
    def merge(self, n1: List[int], m: int, n2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b = m - 1, n - 1
        tar = m + n - 1

        while a >= 0 and b >= 0:
            if n1[a] > n2[b]:
                n1[tar] = n1[a]
                a -= 1
            else:
                n1[tar] = n2[b]
                b -= 1
            tar -= 1

        while b >= 0:
            n1[tar] = n2[b]
            tar -= 1
            b -= 1

        return


# @lc code=end
