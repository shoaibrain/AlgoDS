"""
entries are ordered
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def _insert(self, value):
        if self.root is None:
            self.root = Node(value)

        else:
            self.insert(value, self.root)
        return

    def insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
                return
            else:
                self.insert(value, current_node.left)

        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
                return
            else:
                self.insert(value, current_node.right)
        else:
            print("Data value already exist")
            return

    def _find(self, value):
        if self.root is None:
            print("The tree is doesn't exist")
        else:
            self.find(value, self.root)
        return

    def find(self, root, value):
        if root is None:
            print("The tree doesn't exist")
            return
        else:
            if root.value == value:
                print("found")
                return True
            elif root.value > value and root.left:
                self.find(root.left, value)
            elif root.value < value and root.right:
                self.find(root.right, value)
            else:
                print("Not found")
                return False
        return

    def _isBST(self, root):
        pass


bst = BinarySearchTree()
bst._insert(4)
bst._insert(2)
bst._insert(8)
bst._insert(5)
bst._insert(10)
bst.find(bst.root, 11)
