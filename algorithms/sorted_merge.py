def sorted_merge(a, b):
    res = []

    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while j < len(b):
        res.append(b[j])
        j += 1

    while i < len(a):
        res.append(a[i])
        i += 1

    return res

import unittest
class Tests(unittest.TestCase):
    def test_sorted_merge(self):
        a = [1,2,3,8]
        b = [2,3,7,10]
        f = sorted_merge(a, b)
        answer = [1,2,2,3,3,7,8,10]
        self.assertEqual(f, answer)

if __name__ == '__main__':
    unittest.main()