#!/usr/bin/env python3
"""
Test suite for optimized binary search implementations.
"""

import unittest
from typing import List, TypeVar
import sys
import os
from time import time

# Add the parent directory to the Python path to import the search functions
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from searches.binary_search import (
    binary_search,
    binary_search_with_bounds,
    exponential_search,
    interpolation_search
)

T = TypeVar('T', int, float, str)

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        """Set up test cases used by all test methods."""
        self.empty_list: List[int] = []
        self.single_element: List[int] = [1]
        self.even_list: List[int] = [1, 2, 3, 4, 5, 6]
        self.odd_list: List[int] = [1, 2, 3, 4, 5]
        self.repeated_list: List[int] = [1, 2, 2, 2, 3, 4, 5]
        self.float_list: List[float] = [1.0, 2.5, 3.7, 4.2, 5.9]
        self.str_list: List[str] = ["apple", "banana", "cherry", "date"]
        self.large_list: List[int] = list(range(10000))

    def test_basic_binary_search(self):
        """Test basic functionality of binary_search."""
        self.assertEqual(binary_search(self.even_list, 1), 0)  # First element
        self.assertEqual(binary_search(self.even_list, 6), 5)  # Last element
        self.assertEqual(binary_search(self.even_list, 3), 2)  # Middle element
        self.assertEqual(binary_search(self.even_list, 7), -1)  # Not found

    def test_binary_search_edge_cases(self):
        """Test edge cases for binary_search."""
        self.assertEqual(binary_search(self.empty_list, 1), -1)
        self.assertEqual(binary_search(self.single_element, 1), 0)
        self.assertEqual(binary_search(self.single_element, 2), -1)

    def test_binary_search_with_bounds(self):
        """Test binary_search_with_bounds with custom ranges."""
        # Test with default bounds
        self.assertEqual(binary_search_with_bounds(self.even_list, 3), 2)
        
        # Test with custom bounds
        self.assertEqual(binary_search_with_bounds(self.even_list, 3, 0, 2), 2)
        self.assertEqual(binary_search_with_bounds(self.even_list, 3, 3, 5), -1)
        
        # Test invalid bounds
        self.assertEqual(binary_search_with_bounds(self.even_list, 3, 4, 2), -1)

    def test_exponential_search(self):
        """Test exponential_search functionality."""
        self.assertEqual(exponential_search(self.even_list, 1), 0)
        self.assertEqual(exponential_search(self.even_list, 6), 5)
        self.assertEqual(exponential_search(self.empty_list, 1), -1)
        self.assertEqual(exponential_search(self.single_element, 1), 0)

    def test_interpolation_search(self):
        """Test interpolation_search with uniform distribution."""
        # Test with float values
        self.assertEqual(interpolation_search(self.float_list, 1.0), 0)
        self.assertEqual(interpolation_search(self.float_list, 5.9), 4)
        self.assertEqual(interpolation_search(self.float_list, 3.7), 2)
        self.assertEqual(interpolation_search(self.float_list, 6.0), -1)

    def test_repeated_elements(self):
        """Test search functions with repeated elements."""
        # Should return the first occurrence
        self.assertEqual(binary_search(self.repeated_list, 2), 1)
        self.assertEqual(binary_search_with_bounds(self.repeated_list, 2), 1)
        self.assertEqual(exponential_search(self.repeated_list, 2), 1)

    def test_type_compatibility(self):
        """Test search functions with different types."""
        # Test with strings
        self.assertEqual(binary_search(self.str_list, "apple"), 0)
        self.assertEqual(binary_search(self.str_list, "date"), 3)
        self.assertEqual(binary_search(self.str_list, "fig"), -1)

        # Test with floats
        self.assertEqual(binary_search(self.float_list, 1.0), 0)
        self.assertEqual(binary_search(self.float_list, 5.9), 4)

    def test_performance(self):
        """Test performance of search functions."""
        target = 9999
        
        # Measure binary search performance
        start = time()
        result = binary_search(self.large_list, target)
        binary_time = time() - start
        self.assertEqual(result, target)

        # Measure binary search with bounds performance
        start = time()
        result = binary_search_with_bounds(self.large_list, target)
        bounds_time = time() - start
        self.assertEqual(result, target)

        # Measure exponential search performance
        start = time()
        result = exponential_search(self.large_list, target)
        exp_time = time() - start
        self.assertEqual(result, target)

        # All searches should complete in reasonable time
        self.assertLess(binary_time, 0.1)
        self.assertLess(bounds_time, 0.1)
        self.assertLess(exp_time, 0.1)

if __name__ == '__main__':
    unittest.main()