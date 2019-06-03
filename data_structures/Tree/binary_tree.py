class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "<Node {}>".format(str(self.value))

    def print_BFS(self):
        """BFS - Print each level"""
        pass
        to_visit = [self]
        while to_visit:
            curr = to_visit.pop(0)
            print(curr)
            if self.left:
                to_vist.append(self.left)
            if self.right:
                to_visit.append(self.right)


    def print_preorder(self):
        """DFS - Root, left, right"""
        print(self)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_inorder(self):
        """DFS - Left, root, right"""
        if self.left:
            self.left.print_inorder()
        print(self)
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        """DFS - Left, right, root"""
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self)

class BinaryTree(object):
    def __init__(self):
        self.root = None
