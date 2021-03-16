'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            subset = []
            for index in range(i):
                if nums[index] < nums[i]:
                    subset.append(dp[index])
            dp[i] = 1 + max(subset, default=0)
        return max(dp)