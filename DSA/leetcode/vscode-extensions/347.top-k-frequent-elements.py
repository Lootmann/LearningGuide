#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
import collections
from typing import List


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        sorted(counter)

        result = []
        for elem in counter.most_common():
            if k == 0:
                break
            k -= 1

            result.append(elem[0])

        return result


# @lc code=end
