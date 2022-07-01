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

    def test_tree_str_with_no_children(self):
        assert str(self.node) == "(left, val, right) = (None, 10, None)"

    def test_tree_str_has_children(self):
        self.node.left = TreeNode(1)
        self.node.right = TreeNode(100)
        assert str(self.node) == "(left, val, right) = (1, 10, 100)"


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


class TestTreeDelete:
    def setup_method(self):
        self.tree = Tree()

    def test_delete_lead_with_no_children(self):
        """
             8
          4    10
        1  6  9  12
        """
        for num in [8, 4, 10, 1, 6, 9, 12]:
            self.tree.insert(num)

        assert self.tree.size == 7
        self.tree.delete(1)

        assert self.tree.inorder() == [4, 6, 8, 9, 10, 12]
        assert self.tree.size == 6

    def test_delete_leaf_with_only_left_child(self):
        """
            8
          4   10
        1    9  12
        """
        for num in [8, 4, 10, 1, 9, 12]:
            self.tree.insert(num)

        root = self.tree.root
        assert self.tree.size == 6
        assert root.val == 8
        assert root.left.val == 4
        assert root.left.left.val == 1

        # delete
        self.tree.delete(4)

        root = self.tree.root
        assert self.tree.size == 5
        assert self.tree.inorder() == [1, 8, 9, 10, 12]
        assert root.val == 8
        assert root.left.val == 1
        assert root.left.left is None

    def test_delete_leaf_with_one_depth_children(self):
        """
            8
          4   10
        []   9  12
        """
        for num in [8, 4, 10, 9, 12]:
            self.tree.insert(num)

        root = self.tree.root
        assert self.tree.size == 5
        assert self.tree.inorder() == [4, 8, 9, 10, 12]
        assert root.val == 8
        assert root.right.val == 10
        assert root.right.left.val == 9
        assert root.right.right.val == 12

        # delete
        self.tree.delete(10)
        root = self.tree.root

        assert self.tree.size == 4
        assert self.tree.inorder() == [4, 8, 9, 12]
        assert root.val == 8
        assert root.right.val == 12
        assert root.right.left.val == 9
        assert root.right.right is None


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
