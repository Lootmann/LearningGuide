#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
import collections

# @lc code=start


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)

        for i, ch in enumerate(s):
            if counter[ch] == 1:
                return i

        return -1


# @lc code=end
