#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def getIntersectionNode(self, A: ListNode, B: ListNode) -> Optional[ListNode]:
        """
        complexity:
            time: O(MlogN)
            space: O(N)
        """
        # Memory O(N)
        list = set()

        # O(N)
        while A:
            list.add(A)
            A = A.next

        # O(M)
        while B:
            # O(logN)
            if B in list:
                return B
            B = B.next

        # O(MlogN) -> worse
        return None


# @lc code=end
