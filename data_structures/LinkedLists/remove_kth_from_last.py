def remove_kth_from_last(ll, k):
    runner = ll.head
    for _ in range(k):
        runner = runner.next

    curr = ll.head
    while runner.next and runner.next.next:
        curr = curr.next
        runner = runner.next

    curr.next = curr.next.next
    return ll


import unittest
from linked_list import LinkedList

class Test(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.add_multiple([1, 2, 3, 4, 5, 6, 7])
        print("original LL:", self.ll)

    def test_remove_kth_from_last(self):
        remove_kth_from_last(self.ll, 1)
        self.assertEqual(str(self.ll), '1 ->2 ->3 ->4 ->5 ->7')

    def test_remove_kth_from_last2(self):
        remove_kth_from_last(self.ll, 3)
        self.assertEqual(str(self.ll), '1 ->2 ->3 ->5 ->6 ->7')


if __name__ == '__main__':
    unittest.main()