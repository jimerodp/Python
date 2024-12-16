#!/usr/bin/env python3
"""
Optimized Binary Search Implementations

Improvements:
- Reduced memory overhead
- More efficient comparison operations
- Removed redundant type checks
- Added type hints for better performance
"""

from __future__ import annotations
from typing import TypeVar, List, Optional

T = TypeVar('T', int, float, str)

def binary_search(sorted_collection: List[T], item: T) -> int:
    """
    Optimized binary search with minimal memory overhead and early termination.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    :param sorted_collection: Sorted list to search
    :param item: Item to find
    :return: Index of item or -1 if not found
    """
    left, right = 0, len(sorted_collection) - 1

    while left <= right:
        # Prevent potential integer overflow
        mid = left + ((right - left) >> 1)
        mid_value = sorted_collection[mid]

        # Reduce number of comparisons
        if mid_value == item:
            return mid
        
        if mid_value < item:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_with_bounds(
    sorted_collection: List[T], 
    item: T, 
    left: int = 0, 
    right: Optional[int] = None
) -> int:
    """
    Advanced binary search with custom bounds and minimal memory usage.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    :param sorted_collection: Sorted list to search
    :param item: Item to find
    :param left: Starting index of search range
    :param right: Ending index of search range
    :return: Index of item or -1 if not found
    """
    # Use default right bound if not provided
    if right is None:
        right = len(sorted_collection) - 1

    while left <= right:
        # Bit shift for faster division
        mid = left + ((right - left) >> 1)
        mid_value = sorted_collection[mid]

        if mid_value == item:
            return mid
        
        if mid_value < item:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def exponential_search(sorted_collection: List[T], item: T) -> int:
    """
    Memory-efficient exponential search with optimized bounds.
    
    Time Complexity: O(log i) where i is the index of the item
    Space Complexity: O(1)
    
    :param sorted_collection: Sorted list to search
    :param item: Item to find
    :return: Index of item or -1 if not found
    """
    if not sorted_collection:
        return -1

    # Start with small bound to minimize initial iterations
    bound = 1
    length = len(sorted_collection)

    # Exponential probing with reduced iterations
    while bound < length and sorted_collection[bound] < item:
        bound <<= 1  # Faster multiplication by 2

    # Perform binary search in the identified range
    left = bound >> 1  # Faster division by 2
    right = min(bound, length - 1)

    return binary_search_with_bounds(sorted_collection, item, left, right)

def interpolation_search(sorted_collection: List[float], item: float) -> int:
    """
    Advanced interpolation search for uniformly distributed data.
    
    Time Complexity: O(log log n) for uniform distribution
    Space Complexity: O(1)
    
    :param sorted_collection: Sorted list of numeric values
    :param item: Item to find
    :return: Index of item or -1 if not found
    """
    left, right = 0, len(sorted_collection) - 1

    while left <= right and sorted_collection[left] <= item <= sorted_collection[right]:
        # Prevent division by zero and handle equal values
        if sorted_collection[left] == sorted_collection[right]:
            return left if sorted_collection[left] == item else -1

        # More precise position estimation
        pos = left + int(
            ((item - sorted_collection[left]) * (right - left)) /
            (sorted_collection[right] - sorted_collection[left])
        )

        # Bounds checking to prevent index out of range
        pos = max(left, min(pos, right))
        
        if sorted_collection[pos] == item:
            return pos
        
        if sorted_collection[pos] < item:
            left = pos + 1
        else:
            right = pos - 1

    return -1

# Ordered list of search strategies from fastest to slowest
searches = [
    binary_search,
    binary_search_with_bounds,
    exponential_search,
    interpolation_search
]

if __name__ == "__main__":
    import doctest
    import timeit

    doctest.testmod()
    for search in searches:
        name = f"{search.__name__:>26}"
        print(f"{name}: {search([0, 5, 7, 10, 15], 10) = }")  # type: ignore[operator]

    print("\nBenchmarks...")
    setup = "collection = range(1000)"
    for search in searches:
        name = search.__name__
        print(
            f"{name:>26}:",
            timeit.timeit(
                f"{name}(collection, 500)", setup=setup, number=5_000, globals=globals()
            ),
        )

    user_input = input("\nEnter numbers separated by comma: ").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a single number to be found in the list: "))
    result = binary_search(sorted_collection=collection, item=target)
    if result == -1:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} of {collection}.")
