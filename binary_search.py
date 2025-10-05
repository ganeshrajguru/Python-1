"""
Binary Search Implementation in Python

This module demonstrates how to implement binary search algorithm in Python.
Binary search is an efficient algorithm for finding an item from a sorted list.
It works by repeatedly dividing the search interval in half.

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""


def binary_search_iterative(arr, target):
    """
    Iterative implementation of binary search.
    
    Args:
        arr: A sorted list of elements
        target: The element to search for
        
    Returns:
        The index of target if found, -1 otherwise
        
    Example:
        >>> binary_search_iterative([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search_iterative([1, 2, 3, 4, 5], 6)
        -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Calculate mid point to avoid overflow
        mid = left + (right - left) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target was not found
    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    """
    Recursive implementation of binary search.
    
    Args:
        arr: A sorted list of elements
        target: The element to search for
        left: Left boundary of search (default: 0)
        right: Right boundary of search (default: len(arr) - 1)
        
    Returns:
        The index of target if found, -1 otherwise
        
    Example:
        >>> binary_search_recursive([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search_recursive([1, 2, 3, 4, 5], 6)
        -1
    """
    # Initialize boundaries on first call
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    # Calculate mid point
    mid = left + (right - left) // 2
    
    # Check if target is at mid
    if arr[mid] == target:
        return mid
    # If target is smaller, search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # If target is greater, search right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


# Example usage and demonstration
if __name__ == "__main__":
    # Test data
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("Binary Search Implementation in Python")
    print("=" * 50)
    print(f"\nSorted List: {sorted_list}")
    
    # Test with iterative version
    print("\n--- Iterative Binary Search ---")
    test_values = [7, 15, 1, 19, 20, 0]
    for value in test_values:
        result = binary_search_iterative(sorted_list, value)
        if result != -1:
            print(f"Element {value} found at index {result}")
        else:
            print(f"Element {value} not found in the list")
    
    # Test with recursive version
    print("\n--- Recursive Binary Search ---")
    for value in test_values:
        result = binary_search_recursive(sorted_list, value)
        if result != -1:
            print(f"Element {value} found at index {result}")
        else:
            print(f"Element {value} not found in the list")
    
    # Edge cases
    print("\n--- Edge Cases ---")
    print(f"Empty list search: {binary_search_iterative([], 5)}")
    print(f"Single element (found): {binary_search_iterative([5], 5)}")
    print(f"Single element (not found): {binary_search_iterative([5], 3)}")
    print(f"First element: {binary_search_iterative(sorted_list, 1)}")
    print(f"Last element: {binary_search_iterative(sorted_list, 19)}")
