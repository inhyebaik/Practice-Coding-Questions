def bubblesort(alist):
    """
    Time: O(N^2)
    """
    swapped = False
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
                swapped = True
        if not swapped:
            return alist

    return alist

import unittest
class Tests(unittest.TestCase):
    def test_bubblesort(self):
        f = bubblesort([3, 2, 1, 7, 6, 5, 4])
        answer = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(f, answer)


if __name__ == '__main__':
    unittest.main()