# tests/test_node.py
from src.node import SinglyLinkedNode


class TestSinglyLinkedList:
    def setup_method(self):
        self.node = SinglyLinkedNode(10)

    def test_init(self):
        assert self.node.val == 10
        assert self.node.next is None
