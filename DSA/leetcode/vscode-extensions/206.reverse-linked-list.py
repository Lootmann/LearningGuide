#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]

        nodes[0].next = None

        return nodes[-1]


# @lc code=end
