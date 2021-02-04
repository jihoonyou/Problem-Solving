'''
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/
'''
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_frequency = Counter(nums)
        longest = 0
        for num in num_frequency:
            if num+1 in num_frequency:
                longest = max(longest, num_frequency[num] + num_frequency[num+1])
        return longest