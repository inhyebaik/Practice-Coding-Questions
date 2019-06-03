# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = None

def is_BST(root, _min=-float("inf"), _max=float("inf")):
    if not root:
        return True
    if root.value > _max or root.value < _min:
        return False

    return is_BST(root.left, _max=root.value) and \
        is_BST(root.right, _min=root.value)

    return True

# Test
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print is_BST(root)  # True
