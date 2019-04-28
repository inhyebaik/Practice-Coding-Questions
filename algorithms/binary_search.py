def binary_search(alist, target):
    lo = 0
    hi = len(alist)
    while lo < hi:
        mid = (lo + hi) // 2
        if target == alist[mid]:
            return alist[mid]
        elif target < alist[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


import unittest
class Tests(unittest.TestCase):
    def test_binary_search(self):
        a = [1,2,3,4,6,7,8,9]
        self.assertEqual(binary_search(a, 6), 6)
        self.assertEqual(binary_search(a, 90), False)

if __name__ == '__main__':
    unittest.main()
