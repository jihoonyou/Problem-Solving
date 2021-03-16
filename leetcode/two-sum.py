'''
https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        
        for i in range(0,len(nums)):
            num = nums[i]
            if num in targets:
                return [targets[num], i]
            else:
                targets[target - num] = i
        