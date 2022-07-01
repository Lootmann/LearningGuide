# tests/test_tree.py
from src.node import TreeNode
from src.tree import Tree


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


class TestTree:
    def setup_method(self):
        """
             8
          4    10
        1  6  9  12
        """
        self.tree = Tree()
        self.nums = [8, 4, 10, 1, 6, 9, 12]

    def test_init(self):
        assert self.tree.root is None
        assert self.tree.size == 0

    def test_insert(self):
        for num in self.nums:
            self.tree.insert(num)

        assert self.tree.size == 7

        root = self.tree.root
        assert root.val == 8
        assert root.left.val == 4
        assert root.right.val == 10
        assert root.left.left.val == 1
        assert root.left.right.val == 6
        assert root.right.left.val == 9
        assert root.right.right.val == 12

    def test_find(self):
        for num in self.nums:
            self.tree.insert(num)

        for n in range(0, 13):
            if n in self.nums:
                assert self.tree.find(n) is True
            else:
                assert self.tree.find(n) is not True


class TestTreeTraversal:
    def setup_method(self):
        """
              9
           5      12
        1    7  10  14
        """
        self.tree = Tree()
        self.nums = [9, 5, 12, 1, 7, 10, 14]

        for num in self.nums:
            self.tree.insert(num)

    def test_inorder(self):
        assert self.tree.inorder() == sorted(self.nums)

    def test_preorder(self):
        assert self.tree.preorder() == [9, 5, 1, 7, 12, 10, 14]

    def test_postorder(self):
        assert self.tree.postorder() == [1, 7, 5, 10, 14, 12, 9]
