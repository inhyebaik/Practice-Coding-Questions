class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return '<Node val={}>'.format(self.value)


class LinkedList(object):

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __repr__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return ' ->'.join(values)

    def add(self, value):
        if not self.head:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def add_multiple(self, values):
        for v in values:
            self.add(v)
