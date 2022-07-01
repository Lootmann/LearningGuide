# tests/test_tree.py
from src.node import TreeNode


class TestTreeNode:
    def setup_method(self):
        self.node = TreeNode(10)

    def test_init(self):
        assert self.node.val == 10
        assert self.node.left is None
        assert self.node.right is None

    def test_tree_node_has_child(self):
        left = TreeNode(5)
        right = TreeNode(15)

        self.node.left = left
        self.node.right = right

        assert self.node.val == 10
        assert self.node.left.val == 5
        assert self.node.right.val == 15
