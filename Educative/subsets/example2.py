"""
Problem Statement 
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
"""
def find_subsets(nums):
    nums.sort()
    subsets = [[]]
    end_index = 0
    # TODO: Write your code here
    for idx in range(len(nums)):
        start_index = 0
        if idx > 0 and nums[idx-1] == nums[idx]:
            start_index = end_index
        end_index = len(subsets)

        for index in range(start_index, end_index):
            new_set = list(subsets[index])
            new_set.append(nums[idx])
            subsets.append(new_set)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
