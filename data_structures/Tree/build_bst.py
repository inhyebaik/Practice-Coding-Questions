# Convert a sorted array of integers into a binary search tree

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '<Node value={}>'.format(str(self.value))

    def print_preorder(self):
        """DFS - root, left, right"""
        if self.value:
            curr = self
            print(curr)
            if curr.left:
                curr.left.print_preorder()
            if curr.right:
                curr.right.print_preorder()

    def print_inorder(self):
        """DFS - left, root, right"""
        if self.left:
            self.left.print_inorder()
        print(self)
        if self.right:
            self.right.print_inorder()


    def print_postorder(self):
        """DFS - left, right, root"""
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self)


def convert_sorted_array_to_bst(arr):
    """Converts a sorted array into a BST. Returns the BST root."""

    # mid of array is root
    if not arr:
        return None
    if len(arr) == 1:
        return Node(value=arr.pop())

    mid = len(arr) // 2
    root = Node(value=arr[mid])
    root.left = convert_sorted_array_to_bst(arr[:mid])
    root.right = convert_sorted_array_to_bst(arr[mid+1:])

    return root

arr = range(10)
r = convert_sorted_array_to_bst(arr)
r.print_inorder()
