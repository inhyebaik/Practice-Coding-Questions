class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0

    def add_node_to_end(self, data):
        return self.insert_node(data, None, self.tail)

    def insert_node(self, data, prev, next):
        node = Node(data)
        node.prev = prev
        node.next = next

        if not self.tail or prev is self.tail:
            self.tail = node
        if not self.head or next is self.head:
            self.head = node
        
        if next:
            next.prev = node
        if prev:
            prev.next = node

        self.count += 1
        return node

    def remove_node(self, node):
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
        elif node is self.head:
            self.head = node.next 
            self.head.prev = None

        node_prev = node.prev 
        node_next = node.next 

        node.prev.next = node_next
        node.next.prev = node_prev

        self.count -= 1



