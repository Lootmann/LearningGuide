class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data: list):
        self.head = None

        for num in tree_data:
            if self.head == None:
                self.head = TreeNode(num)
            else:
                self.insert(self.head, num)

    def insert(self, node, num):
        if int(num) <= int(node.data):
            if node.left == None:
                node.left = TreeNode(num)
            else:
                self.insert(node.left, num)

        elif int(node.data) < int(num):
            if node.right == None:
                node.right = TreeNode(num)
            else:
                self.insert(node.right, num)

    def data(self):
        return self.head

    def inorder(self, node: TreeNode, lst: list):
        # inorder traversal
        if node:
            if node.left:
                self.inorder(node.left, lst)

            lst.append(node.data)

            if node.right:
                self.inorder(node.right, lst)

    def sorted_data(self):
        lst = []
        self.inorder(self.head, lst)
        return lst
