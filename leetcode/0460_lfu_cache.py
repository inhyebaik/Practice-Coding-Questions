class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class ItemNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.parent = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_node(self, data):
        return self.insert_node(data, prev=self.tail, next=None)

    def insert_node(self, data, prev=None, next=None):
        node = Node(data)
        node.prev = prev
        node.next = next
        if prev:
            prev.next = node
        if next:
            next.prev = node

        if not self.tail or prev is self.tail:
            self.tail = node

        if not self.head or next is self.head:
            self.head = node

        self.count += 1
        return node

    def remove_node(self, node):
        if node is self.head:
            self.head = node.next

        if node is self.tail:
            self.tail = node.prev

        node.prev.next = node.next
        node.next.prev = node.prev

        self.count -= 1

class FrequencyNode(DoublyLinkedList, Node):
    def __init__(self, data):
        DoublyLinkedList.__init__(self)
        Node.__init__(self, data)

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lfu = {}
        self.cache = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """