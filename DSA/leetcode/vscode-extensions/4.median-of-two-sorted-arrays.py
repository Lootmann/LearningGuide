#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List


# @lc code=start
class Solution:
    def merge_sort(self, n1: List[int], n2: List[int]) -> List[int]:
        """
        O(N) ?
        """
        merged = []
        left = right = 0
        while len(n1) > left and len(n2) > right:
            if n1[left] > n2[right]:
                merged.append(n2[right])
                right += 1
            else:
                merged.append(n1[left])
                left += 1

        while len(n1) > left:
            merged.append(n1[left])
            left += 1

        while len(n2) > right:
            merged.append(n2[right])
            right += 1

        return merged

    def calc_median(self, lst: List[int]) -> float:
        # O(1)
        length = len(lst)

        if length % 2 == 0:
            return float(lst[length // 2 - 1] + lst[length // 2]) / 2
        else:
            return float(lst[length // 2])

    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        merged = self.merge_sort(n1, n2)
        return self.calc_median(merged)


# @lc code=end
