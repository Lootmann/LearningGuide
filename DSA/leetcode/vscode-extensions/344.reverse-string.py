#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
from typing import List


# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]


# @lc code=end
