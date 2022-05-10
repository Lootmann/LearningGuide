#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            # print("No.", i)
            if i == 0:
                result.append([1])
            else:
                row = [0] * (i + 1)
                result.append(row)

                for j in range(2):
                    for k in range(j, i + j):
                        result[i][k] += result[i - 1][k - j]

        return result


# @lc code=end
