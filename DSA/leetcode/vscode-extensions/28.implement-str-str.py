#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            is_match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    is_match = False

            if is_match:
                return i

        return -1


# @lc code=end
