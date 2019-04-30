def reverse(LL):
    # Set head and tail
    old_tail = LL.tail
    old_head = LL.head
    LL.head = old_tail
    LL.tail = old_head

    # Change next pointers of Nodes
    curr = old_head
    prev = None
    while curr:
        next = curr.next  # save the next value
        curr.next = prev
        prev = curr
        curr = next
    return LL


import unittest
from linked_list import LinkedList

class Test(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.add_multiple([1, 2, 3, 4, 5])
        print("original LL:", self.ll)

    def test_reverse(self):
        reverse(self.ll)
        self.assertEqual(str(self.ll), '5 ->4 ->3 ->2 ->1')


if __name__ == '__main__':
    unittest.main()