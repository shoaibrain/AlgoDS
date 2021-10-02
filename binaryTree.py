"""
A binary tree a s data structure that is composed of nodes where each node can have upto two hildren and they each parent is connected to their children
through the node poinnter.

Binary search tree is a binary tree where all the node value to the left of the root is smaller than root value and all the value to the right of the root is
greater than or equal to the root value

There are different types of binary tree like compelte bt, full bt, etc
"""
# Node class


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree class


class BinaryTree(object):
    def __init__(self, root):
        # assuming root was passed as a value that was supposed to be a root value of the binary treee
        self.root = Node(root)

    def print(self, traversal_type):
        if traversal_type == 'preorder':
            return self._preorder(tree.root, "")
        elif traversal_type == 'inorder':
            return self._inorder(tree.root, "")
        elif traversal_type == 'postorder':
            return self._postorder(tree.root, "")

    """
    Tree Traversal: bfs
    """
    # preorder: returns a list of node values while traversing in prorder: R->L->R

    # root is pointer to root node, values is list that will be passed from the caller and it will be populated in preorder
    def _preorder(self, root, traversal):
        # check if root is None
        if root:
            traversal += (str(root.value) + "->")
            traversal = self._preorder(root.left, traversal)
            traversal = self._preorder(root.right, traversal)
        return traversal
    # inorder

    def _inorder(self, root, traversal):
        if root:
            traversal = self._inorder(root.left, traversal)
            traversal += (str(root.value) + "->")
            traversal = self._inorder(root.right, traversal)
        return traversal
    # postorder

    def _postorder(self, root, traversal):
        if root:
            traversal = self._postorder(root.left, traversal)
            traversal = self._postorder(root.right, traversal)
            traversal += (str(root.value) + "->")
        return traversal
    # get all paths

    def _getAllPaths(self, root, currentPath, allPaths):
        if not root:
            return
        runnigPath = currentPath + [root.value]
        if root.left is None and root.right is None:
            allPaths.append(runnigPath)
            return
        self._getAllPaths(root.left, runnigPath, allPaths)
        self._getAllPaths(root.right, runnigPath, allPaths)

    # get all levels
    def _getLevels(self, root):
        if not root:
            return
        queue = [root]
        levels = []
        while queue:
            level_length = len(queue)
            level_items = []

            for _ in range(level_length):
                node = queue.pop(0)
                level_items.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level_items)
        return levels


"""
            1
         /      \
        2        3
      /   \     /  \
     4     5   6    7
                     \
                      8
preorder => 1->2->4->5->3->6->7 ->8
inorder =>  4->2->5->1->6->3->7->8
postorder => 4->5->2->6->8->7->3->1
allpaths fro root to leaf
[
[1, 2, 4],
[1, 2, 5],
[1, 3, 6],
[1, 3, 7, 8]
]
by level:
[
[1],
[2, 3],
[4, 5, 6, 7],
[8]
]
"""
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

# print(tree.print("preorder"))
# print(tree.print("inorder"))
# print(tree.print("postorder"))

# allPaths = []
# tree._getAllPaths(tree.root, [], allPaths)
# print(allPaths)
allLevels = tree._getLevels(tree.root)
print(allLevels)
