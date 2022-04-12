#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)
        ans = ""

        for i, _ in enumerate(shortest):
            prefixes = [str[: i + 1] for str in strs]

            if not all(prefixes[0] == elem for elem in prefixes):
                break

            ans = prefixes[0]

        return ans


# @lc code=end
