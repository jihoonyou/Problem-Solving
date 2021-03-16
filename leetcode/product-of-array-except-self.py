'''
https://leetcode.com/problems/product-of-array-except-self/
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        
        for index in range(1,len(nums)):
            res[index] = res[index-1]*nums[index-1]
            
        product = 1
        
        for index in range(len(nums)-2, -1, -1):
            product *= nums[index+1]
            res[index] *= product
            
        return res
        