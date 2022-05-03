#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
from tkinter import W
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def getIntersectionNode(self, A: ListNode, B: ListNode) -> Optional[ListNode]:
        tmpA, tmpB = A, B
        lenA, lenB = 0, 0

        while tmpA:
            lenA += 1
            tmpA = tmpA.next

        while tmpB:
            lenB += 1
            tmpB = tmpB.next

        # list A longer than list B
        if lenA > lenB:
            for _ in range(lenA - lenB):
                A = A.next
        else:
            for _ in range(lenB - lenA):
                B = B.next

        # list A and B are same length
        while A != B:
            A, B = A.next, B.next

        return A


# @lc code=end
