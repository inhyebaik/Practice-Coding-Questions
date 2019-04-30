class Node(object):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return "<Node {}>".format(str(self.value))

    def find_DFS(self, target):
        """ Start at this node, and return node with given value; else None."""

        to_visit = [self]

        while to_visit:
            curr = to_visit.pop()
            if curr.value == target:
                return curr
            to_visit.extend(curr.children)
        return None

    def find_BFS(self, target):
        """ Start at this node, and return node with given value; else None."""

        to_visit = [self]

        while to_visit:
            curr = to_visit.pop(0) # BFS -> .pop(0) -> queue 
            if curr.value == target:
                return curr
            to_visit.extend(curr.children)
        return None


class Tree(object):
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return "<Tree root={}>".format(self.root.value)
