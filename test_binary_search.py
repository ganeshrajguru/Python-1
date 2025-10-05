"""
Test cases for binary search implementation
"""

import unittest
from binary_search import binary_search_iterative, binary_search_recursive


class TestBinarySearch(unittest.TestCase):
    """Test cases for both iterative and recursive binary search"""
    
    def setUp(self):
        """Set up test data"""
        self.sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.empty_list = []
        self.single_element = [5]
        
    def test_iterative_element_found(self):
        """Test iterative search when element exists"""
        self.assertEqual(binary_search_iterative(self.sorted_list, 7), 3)
        self.assertEqual(binary_search_iterative(self.sorted_list, 1), 0)
        self.assertEqual(binary_search_iterative(self.sorted_list, 19), 9)
        self.assertEqual(binary_search_iterative(self.sorted_list, 11), 5)
        
    def test_iterative_element_not_found(self):
        """Test iterative search when element doesn't exist"""
        self.assertEqual(binary_search_iterative(self.sorted_list, 0), -1)
        self.assertEqual(binary_search_iterative(self.sorted_list, 20), -1)
        self.assertEqual(binary_search_iterative(self.sorted_list, 8), -1)
        
    def test_iterative_empty_list(self):
        """Test iterative search on empty list"""
        self.assertEqual(binary_search_iterative(self.empty_list, 5), -1)
        
    def test_iterative_single_element(self):
        """Test iterative search on single element list"""
        self.assertEqual(binary_search_iterative(self.single_element, 5), 0)
        self.assertEqual(binary_search_iterative(self.single_element, 3), -1)
        
    def test_recursive_element_found(self):
        """Test recursive search when element exists"""
        self.assertEqual(binary_search_recursive(self.sorted_list, 7), 3)
        self.assertEqual(binary_search_recursive(self.sorted_list, 1), 0)
        self.assertEqual(binary_search_recursive(self.sorted_list, 19), 9)
        self.assertEqual(binary_search_recursive(self.sorted_list, 11), 5)
        
    def test_recursive_element_not_found(self):
        """Test recursive search when element doesn't exist"""
        self.assertEqual(binary_search_recursive(self.sorted_list, 0), -1)
        self.assertEqual(binary_search_recursive(self.sorted_list, 20), -1)
        self.assertEqual(binary_search_recursive(self.sorted_list, 8), -1)
        
    def test_recursive_empty_list(self):
        """Test recursive search on empty list"""
        self.assertEqual(binary_search_recursive(self.empty_list, 5), -1)
        
    def test_recursive_single_element(self):
        """Test recursive search on single element list"""
        self.assertEqual(binary_search_recursive(self.single_element, 5), 0)
        self.assertEqual(binary_search_recursive(self.single_element, 3), -1)
        
    def test_first_and_last_elements(self):
        """Test search for first and last elements"""
        # Iterative
        self.assertEqual(binary_search_iterative(self.sorted_list, 1), 0)
        self.assertEqual(binary_search_iterative(self.sorted_list, 19), 9)
        # Recursive
        self.assertEqual(binary_search_recursive(self.sorted_list, 1), 0)
        self.assertEqual(binary_search_recursive(self.sorted_list, 19), 9)
        
    def test_middle_elements(self):
        """Test search for middle elements"""
        # Iterative
        self.assertEqual(binary_search_iterative(self.sorted_list, 9), 4)
        self.assertEqual(binary_search_iterative(self.sorted_list, 11), 5)
        # Recursive
        self.assertEqual(binary_search_recursive(self.sorted_list, 9), 4)
        self.assertEqual(binary_search_recursive(self.sorted_list, 11), 5)
        
    def test_large_list(self):
        """Test with a larger list"""
        large_list = list(range(0, 1000, 2))  # Even numbers from 0 to 998
        # Iterative
        self.assertEqual(binary_search_iterative(large_list, 500), 250)
        self.assertEqual(binary_search_iterative(large_list, 0), 0)
        self.assertEqual(binary_search_iterative(large_list, 998), 499)
        self.assertEqual(binary_search_iterative(large_list, 501), -1)
        # Recursive
        self.assertEqual(binary_search_recursive(large_list, 500), 250)
        self.assertEqual(binary_search_recursive(large_list, 0), 0)
        self.assertEqual(binary_search_recursive(large_list, 998), 499)
        self.assertEqual(binary_search_recursive(large_list, 501), -1)
        
    def test_negative_numbers(self):
        """Test with negative numbers"""
        negative_list = [-10, -5, -3, -1, 0, 2, 4, 6]
        # Iterative
        self.assertEqual(binary_search_iterative(negative_list, -5), 1)
        self.assertEqual(binary_search_iterative(negative_list, 0), 4)
        self.assertEqual(binary_search_iterative(negative_list, -7), -1)
        # Recursive
        self.assertEqual(binary_search_recursive(negative_list, -5), 1)
        self.assertEqual(binary_search_recursive(negative_list, 0), 4)
        self.assertEqual(binary_search_recursive(negative_list, -7), -1)


if __name__ == '__main__':
    unittest.main()
