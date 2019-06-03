class Node(object):

    def __init__(self, value, children=None):
        self.value = value
        self.children = children else []

    def __repr__(self):
        return "<Node value={}>".format(str(self.value))

    def find_DFS(self, value):
        to_visit = [self]

        while to_visit:
            curr = to_visit.pop()
            if curr.value == value:
                return curr
            else:
                to_visit.extend(curr.children)
        return False

    def find_BFS(self, value):
        to_visit = [self]

        while to_visit:
            curr = to_visit.pop(0)
            if curr.value == value:
                return curr
            else:
                to_visit.extend(curr.children)
        return False


class Tree(object):
    def __init__(self):
        self.root = None

    def find_DFS(self, value):
        self.root.find_DFS(value)

    def find_BFS(self, value):
        self.root.find_BFS(value)
