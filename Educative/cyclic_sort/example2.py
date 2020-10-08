"""
Problem Statement
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""
def find_missing_number(nums):
    start, n = 0, len(nums)

    while start < n:
        index = nums[start]
        if nums[start] < n and nums[start] != nums[index]:
            nums[start], nums[index] = nums[index], nums[start]
        else:
            start += 1

    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return n
