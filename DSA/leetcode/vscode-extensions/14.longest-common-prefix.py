#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        prefixes = []

        for i, prefix in enumerate(shortest):
            is_match = True

            for j in range(len(strs)):
                if strs[j][i] != prefix:
                    is_match = False

            if not is_match:
                break

            prefixes.append(prefix)

        return "".join(prefixes)


# @lc code=end
