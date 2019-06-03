#  T1 and T2 are two very large binary trees, with T1
#  much bigger then T2. Create an algorithm to determine
#  if T2 is a subtree of T1.
#  A tree T2 is a subtree of T1 if there exists a node n
#  in T1 such that the subtree of n is identical to T2.
#  That is, if you cut off the tree at node n, the two
#  trees would be identical.

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def are_identical(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.value == root2.value:
        return are_identical(root1.left, root2.left) and /
        are_identical(root1.right, root2.right)

def is_subtree(t, s):
    if s.value == t.value:
        return are_identical(t, s)

    return is_subtree(t.left, s) or is_subtree(t.right, s)