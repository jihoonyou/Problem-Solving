"""
Problem Statement
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
"""
def make_squares(arr):
    squares = [0]*len(arr)
    start, end, highest_index = 0, len(arr)-1, len(arr)-1
    
    while start <= end:
        if abs(arr[start]) < abs(arr[end]):
            squares[highest_index] = arr[end]**2
            end -=1
        else:
            squares[highest_index] = arr[start]**2
            start += 1
        highest_index -= 1

    return squares
