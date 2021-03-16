'''
https://leetcode.com/problems/contains-duplicate/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for num in nums:
            if num in frequency:
                return True
            frequency[num] = 1
        return False