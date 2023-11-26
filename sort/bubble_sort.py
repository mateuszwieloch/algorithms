# Based on implementation in chapter 4 of the "Common Sense Guide to Data Structures and Algorithms" 2nd ed book.
def bubble_sort[T](array: list[T]):
    """Sorts array in place. O(n²)

    Start from the left and "bubble up" big values by comparing consecutive
    pairs (sliding window). If values in a pair and in a wrong order, swap.

    Each "bubble up" iteration, accumulates one more sorted value on the right
    of the array.

    An additional optimization included in the code is early termination of the
    algorithm if no swaps are performed in an iteration, because it means the
    array has already been sorted.
    """
    unsorted_until_index = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        unsorted_until_index -= 1

    return array


# Usage
assert bubble_sort([2, 1, 4, 3]) == [1, 2, 3, 4]
assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
