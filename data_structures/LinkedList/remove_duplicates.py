def remove_duplicates(ll):
    seen = set([ll.head.value])
    curr = ll.head.next
    prev = ll.head

    while curr:
        if curr.value in seen:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
        else:
            seen.add(curr.value)
            prev = curr
            curr = curr.next
    return ll


import unittest
from linked_list import LinkedList

class Test(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.add_multiple([1, 2, 2, 3, 3, 6, 6, 3, 1])
        print("original LL:", self.ll)

    def test_remove_dups(self):
        remove_duplicates(self.ll)
        self.assertEqual(str(self.ll), '1 ->2 ->3 ->6')


if __name__ == '__main__':
    unittest.main()