"""
Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""
import math

def smallest_subarray_with_given_sum(s, arr):
    cur_sum, start_window = 0, 0
    min_len = math.inf
    cur_len = 0

    for end_window in range(len(arr)):
        cur_sum += arr[end_window]
        while cur_sum >= s:
            cur_len = end_window - start_window + 1
            min_len = min(min_len,cur_len)
            cur_sum -= arr[start_window]
            start_window += 1
    
    if min_len == math.inf:
        return 0
    
    return min_len
