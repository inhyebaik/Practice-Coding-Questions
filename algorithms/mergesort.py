def mergesort(arr):
    """
    Time: O(N log N)
    """

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


import unittest
class Tests(unittest.TestCase):
    def test_mergesort(self):
        f = mergesort([3, 2, 1, 7, 6, 5, 4])
        answer = [1,2,3,4,5,6,7]
        self.assertEqual(f, answer)


if __name__ == '__main__':
    unittest.main()