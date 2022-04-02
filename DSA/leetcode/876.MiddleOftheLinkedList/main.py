from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        tmp = head

        while tmp is not None:
            length += 1
            tmp = tmp.next

        for _ in range(length // 2):
            head = head.next

        return head

    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)

        return arr[len(arr) // 2]

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def trace(node: ListNode) -> None:
    res = []
    while node is not None:
        res.append(str(node.val))
        node = node.next
    print(" ".join(res))


def main():
    test1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    test2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

    sol = Solution()
    trace(sol.middleNode(test1))
    trace(sol.middleNode(test2))

    trace(sol.middleNode1(test1))
    trace(sol.middleNode1(test2))


if __name__ == "__main__":
    main()
