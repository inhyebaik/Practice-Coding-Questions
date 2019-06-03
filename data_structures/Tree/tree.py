class Node(object):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return '<Node value={}>'.format(str(self.value))

    def find_DFS(self, value):
        """Starting at this node, return the node with the given value.
        Return None if not found.
        Depth-first traversal (finding the lowest-ranking)
        """
        to_visit = [self]  # use stack for O(1) FIFO
        while to_visit:
            curr = to_visit.pop()
            if curr.value == value:
                return curr
            else:
                to_visit.extend(curr.children)
        return None

    def find_BFS(self, value):
        """Starting at this node, return the node with the given value.
        Return None if not found.
        Breadth-first traversal (finding the highest-ranking)
        """
        from collections import deque
        to_visit = deque([self])  # use deque for O(1) LIFO
        while to_visit:
            curr = to_visit
            if curr.value == value:
                return curr
            else:
                to_visit.extend(curr.children)
        return None


class Tree(object):
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return '<Tree root={}>'.format(self.root)

    def find_BFS(self, value):
        return self.root.find_BFS(value)

    def find_DFS(self, value):
        return self.root.find_DFS(value)


