class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "-> ".join(values)

    def add(self, value):
        if not self.head:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def delete_node(self, target):

        if self.head.value == target:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None
            return self

        curr = self.head.next
        prev = self.head

        while curr:
            if curr.value == target:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return self


import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.add_multiple([1, 2, 3, 4, 5])
        print("original LL:", self.ll)

    def test_delete(self):
        self.ll.delete_node(3)
        self.assertEqual(str(self.ll), '1-> 2-> 4-> 5')


if __name__ == '__main__':
    unittest.main()
