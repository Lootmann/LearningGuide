#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
from typing import List


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        cnt = 1

        length = len(chars)
        for i in range(length - 1):
            if chars[i] == chars[i + 1]:
                cnt += 1
            else:
                chars.append(chars[i])

                if cnt != 1:
                    for ch in str(cnt):
                        chars.append(str(ch))
                    cnt = 1

        chars.append(chars[length - 1])
        if cnt != 1:
            for ch in str(cnt):
                chars.append(ch)

        # delete origin chars [0:size]
        chars[:] = chars[size:]

        return size


# @lc code=end
