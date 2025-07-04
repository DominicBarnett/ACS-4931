# Exercise 3: Sorting and Searching Demo
# This script demonstrates the use of merge sort and binary search algorithms.
# It imports utility functions from utils.py and shows their usage on a sample list.

from utils import merge_sort, binary_search

if __name__ == '__main__':
    # Define a sample list of numbers
    list_of_nums = [7, 4, 9, 3, 5, 6, 1, 2]
    print('List of nums is:')
    print(list_of_nums)

    # Sort the list using merge sort
    merge_sort(list_of_nums)

    print('Sorted list of nums is:')
    print(list_of_nums)

    # Search for the index of 5 in the sorted list using binary search
    index_of_5 = binary_search(list_of_nums, 5)
    print(f'Index of 5 is: {index_of_5}')