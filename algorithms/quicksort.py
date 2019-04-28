def quicksort(alist):
    """Given an item in its position,
    all other items on its left are smaller, and all
    other items on its right are larger.

    Time: O(n*log n)
    """
    return _quicksort(alist, 0, len(alist)-1)

def _quicksort(alist, first, last):
    if first < last:
        pivot = partition(alist, first, last)
        # Once partition is complete, it returns a list with the pivot in right position
        # We quicksort each sublist partitioned by the pivot
        _quicksort(alist, first, pivot - 1)
        _quicksort(alist, pivot + 1, last)
    return alist


def partition(listToSort, lowIndex, highIndex):
    divider = lowIndex
    pivot = highIndex # Randomly select a pivot

    for i in range(lowIndex, highIndex):
        if listToSort[i] < listToSort[pivot]:
            listToSort[i], listToSort[divider] = listToSort[divider], listToSort[i]
            divider += 1

    # Place pivot in correct position
    listToSort[pivot], listToSort[divider] = listToSort[divider], listToSort[pivot]
    return divider


import unittest
class Tests(unittest.TestCase):
    def test_quicksort(self):
        f = quicksort([3, 2, 1, 7, 6, 5, 4])
        answer = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(f, answer)


if __name__ == '__main__':
    unittest.main()