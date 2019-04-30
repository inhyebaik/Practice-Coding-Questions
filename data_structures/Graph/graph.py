class Node(object):

    def __init__(self, value, adjacent=None):
        self.value = value
        self.adjacent = adjacent if isinstance(adjacent, set) else set()

class Graph(object):
    
    def __init__(self):
        self.nodes = set()

    def add_nodes(self, nodes):
        self.nodes.add(nodes)

    def set_adjacent(self, node1, node2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def are_connected_BFS(self, node1, node2):
        """Returns bool whether given nodes are adjacent.
        Breadth-first traversal (FIFO using deque).
        """
        from collections import deque
        to_visit = deque()  # Using deque for O(1) FIFO
        to_visit.add(node1)
        seen = set()
        while to_visit:
            curr = to_visit.popleft() # FIFO 
            if curr is node2:
                return True
            else:
                for a in curr.adjacent - seen:
                    to_visit.append(a)  # appends to the right
                    seen.add(a)
        return False

    def are_connected_DFS(self, node1, node2):
        """Returns bool whether given nodes are adjacent.
        Depth-first traversal.
        """
        to_visit = [node1] # Using a stack for O(1) LIFO
        seen = set()
        while to_visit:
            curr = to_visit.pop()
            if curr is node2:
                return True
            else:
                for a in curr.adjacent - seen:
                    to_visit.append(a)
                    seen.add(a)
        return False
