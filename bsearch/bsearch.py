from typing import Optional

# O(log₂n)
def bsearch[T](sorted_array: list[T], search_value: T) -> Optional[int]:
    """
    Returns index of search_value in the sorted_array or None if value doesn't exist.
    """
    lower_bound = 0
    upper_bound = len(sorted_array) - 1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if search_value == sorted_array[mid]:
            return mid
        elif search_value > sorted_array[mid]:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1
    return None


# Example usage
assert bsearch([1, 4, 8, 10, 12], 1) == 0
assert bsearch([1, 4, 8, 10, 12], 8) == 2
assert bsearch([1, 4, 8, 10, 12], 12) == 4

assert bsearch([1, 4, 8, 10, 12], 0) is None
assert bsearch([1, 4, 8, 10, 12], 5) is None
assert bsearch([1, 4, 8, 10, 12], 13) is None



# Python has a built-in module bisect that has *limited* binary search
# functionality. bisect_left() and bisect_right() functions can be used to
# locate an insertion point. The insertion point can be used as the first
# argument to list.insert()
import bisect
assert bisect.bisect_left([1, 4, 8, 10, 12], 8) == 2
# NOTE how the next call returns 2
assert bisect.bisect_left([1, 4, 8, 10, 12], 7) == 2

